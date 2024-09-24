from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from .rag_srvc import rag_service
import re

def calculator(expression):
        try:
            return eval(expression)
        except Exception:
            return (f"Invalid expression {Exception}")
class AgentService:
    def __init__(self):
        model_name = "google/flan-t5-base"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        pipe = pipeline(
            "text2text-generation",
            model=model, 
            tokenizer=tokenizer, 
            max_length=1024,
            # truncation=True 
        )   
        self.llm = HuggingFacePipeline(pipeline=pipe)
        self.need_rag_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["query"],
                template = """
Determine whether the query requires specialized academic information from Chapter 11 of the NCERT book (Sound) or if it can be answered with general knowledge.
Answer 'yes' if the query specifically asks for details from Chapter 11 or similar academic content. 
Answer 'no' if the query is about general knowledge or doesn't need specific academic details.

Some examples:
1. Query: "What is sound energy?" 
   Answer: no (General knowledge)
   
2. Query: "What is the activity mentioned in Chapter 11 of NCERT about sound and water?" 
   Answer: yes (Requires information from NCERT)

3. Query: "What is the speed of sound in air?" 
   Answer: no (General knowledge)

4. Query: "Explain the production of sound according to Chapter 11 of NCERT." 
   Answer: yes (Requires NCERT PDF)

Query: {query}
Answer:
"""

            )
        )
        self.response_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["query", "context"],
                template="Use the following pieces of context to answer the query. If the context doesn't help, use your general knowledge.\n\nContext: {context}\n\nQuery: {query}\n\nResponse:"
            )
        )
    def is_greeting(self, query):
        greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
        return any(query.lower().startswith(greeting) for greeting in greetings)
    def process_query(self, query: str):
        if self.is_greeting(query):
            return {
                "response": "Hello! How can I assist you today?",
                "used_tool": "greeting",
                "rag_confidence": 0
            }
        
        calc_match = re.match(r'^calculate\s+(.+)$', query, re.IGNORECASE)
        if calc_match:
            expression = calc_match.group(1)
            try:
                result = eval(expression)
                return {
                    "response": f"The result of {expression} is {result}",
                    "used_tool": "calculator",
                    "rag_confidence": 0
                }
            except:
                return {
                    "response": "I'm sorry, but that's not a valid mathematical expression. Could you please check and try again?",
                    "used_tool": "calculator",
                    "rag_confidence": 0
                }
        need_rag = self.need_rag_chain.run(query).strip().lower()
        if need_rag == 'yes':
            context = rag_service.query(query)
            context_str = "\n".join(context) if context else "No specific information found. Please use general knowledge."
            used_tool = "rag"
            rag_confidence = 1
        else:
            context_str = "Use your general knowledge to answer this question."
            used_tool = "general_knowledge"
            rag_confidence = 0
        response = self.response_chain.run(query=query, context=context_str)
        return {
            "response": response.strip(),
            "used_tool": used_tool,
            "rag_confidence": rag_confidence
        }

agent_service = AgentService()