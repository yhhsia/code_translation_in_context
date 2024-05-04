import os
import requests
import difflib
import sys


# from codegen_sources.preprocessing.lang_processors.python_processor import PythonProcessor
# Constants
API_TOKEN = ""
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
#API_URL = "https://api.openai.com/v1/chat/completions"
# openai_key = os.environ.get("openai_key")
#API_KEY = "YOUR APIKEY"
#HEADERS = {
#    "Authorization": f"Bearer {API_KEY}"
#}

cpp_types = ["int ", "bool ", "void ", "ll ", "unsigned ", "float ", "long ", "string ", "public "]

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_cpp_functions():
    cpp_functions = {}
    test_files_path = "./test_data_ids/"
    cpp_files_path = test_files_path + "transcoder_test.cpp.tok"
    with open(cpp_files_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line at the first occurrence of '|'
            parts = line.split('|', 1)
            if len(parts) == 2:
                # Trim whitespace and store in dictionary
                func_id = parts[0].strip()
                code = parts[1].strip()
                cpp_functions[func_id] = code

    return cpp_functions
    

def get_python_functions():
    python_functions = {}
    test_files_path = "./test_data_ids/"
    python_files_path = test_files_path + "transcoder_test.python.tok"
    with open(python_files_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line at the first occurrence of '|'
            parts = line.split('|', 1)
            if len(parts) == 2:
                # Trim whitespace and store in dictionary
                func_id = parts[0].strip()
                code = parts[1].strip()
                python_functions[func_id] = code
    return python_functions
    


def get_java_functions():
    java_functions = {}
    test_files_path = "./test_data_ids/"
    java_files_path = test_files_path + "transcoder_test.java.tok"
    with open(java_files_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line at the first occurrence of '|'
            parts = line.split('|', 1)
            if len(parts) == 2:
                # Trim whitespace and store in dictionary
                func_id = parts[0].strip()
                code = parts[1].strip()
                java_functions[func_id] = code
    return java_functions
    


def translate_cpp_to_python(curr_id, prompt):
    if curr_id in cpp_functions:
        # print(cpp_functions[curr_id])
        text = prompt + cpp_functions[curr_id]

        inputs = {"inputs": text,
                  "parameters": {
                        "return_full_text": False
                  }}

    response = query(inputs)

    response_dict = response[0]
    # print(response_dict)
    translated_code =  response_dict["generated_text"]
    translated_code = translated_code.replace('\n', '')
    translated_code = translated_code.replace("DEDEDENT", "DEDENT")
    translated_code = translated_code.replace("NEW\\_LINE", "NEWLINE")
    translated_code = translated_code.replace("NEW_LINE", "NEWLINE")
    translated_code = translated_code.replace("NEWLINE ", "NEWLINE")
    translated_code = translated_code.replace(" NEWLINE ", "NEWLINE")
    translated_code = translated_code.replace("NEWLINE", " NEWLINE ")
    translated_code = translated_code.replace("\\_", "_")
    i = translated_code.find("def ")
    translated_code = translated_code[i:]
    print(translated_code)
    return translated_code

def translate_java_to_python(curr_id, prompt):
    if curr_id in java_functions:
        # print(cpp_functions[curr_id])
        text = prompt + java_functions[curr_id]

        inputs = {"inputs": text,
                  "parameters": {
                        "return_full_text": False
                  }}

    response = query(inputs)

    response_dict = response[0]
    # print(response_dict)
    translated_code =  response_dict["generated_text"]
    translated_code = translated_code.replace('\n', '')
    translated_code = translated_code.replace("DEDEDENT", "DEDENT")
    translated_code = translated_code.replace("NEW\\_LINE", "NEWLINE")
    translated_code = translated_code.replace("NEW_LINE", "NEWLINE")
    translated_code = translated_code.replace("NEWLINE ", "NEWLINE")
    translated_code = translated_code.replace(" NEWLINE ", "NEWLINE")
    translated_code = translated_code.replace("NEWLINE", " NEWLINE ")
    translated_code = translated_code.replace("\\_", "_")
    i = translated_code.find("def ")
    translated_code = translated_code[i:]
    print(translated_code)
    return translated_code

def translate_python_to_cpp(curr_id, prompt):
    if curr_id in python_functions:
        #print(python_functions[curr_id])
        text = prompt + python_functions[curr_id]

        inputs = {"inputs": text,
                  "parameters": {
                        "return_full_text": False
                  }}
    else:
        return None

    response = query(inputs)
    #print(response)
    response_dict = response[0]
    # print(response_dict)
    translated_code =  response_dict["generated_text"]
    translated_code = translated_code.replace('\n', '')
    idxs = [translated_code.find(t) for t in cpp_types]
    first = 1000
    for i in idxs:
        if i < first and i != -1:
            first = i
    translated_code = translated_code[first:]
    print(translated_code)
    return translated_code

def translate_java_to_cpp(curr_id, prompt):
    if curr_id in java_functions:
        # print(cpp_functions[curr_id])
        text = prompt + java_functions[curr_id]

        inputs = {"inputs": text,
                  "parameters": {
                        "return_full_text": False
                  }}

    response = query(inputs)

    response_dict = response[0]
    translated_code =  response_dict["generated_text"]
    translated_code = translated_code.replace('\n', '')
    idxs = [translated_code.find(t) for t in cpp_types]
    first = 1000
    for i in idxs:
        if i < first and i != -1:
            first = i
    translated_code = translated_code[first:]
    # print(response_dict)
    #print(translated_code)
    return translated_code

def translate_python_to_java(curr_id):
    if curr_id in python_functions:
        # print(cpp_functions[curr_id])
        text = python_java_prompt + python_functions[curr_id]

        inputs = {"inputs": text,
                  "parameters": {
                        "return_full_text": False
                  }}

    response = query(inputs)

    response_dict = response[0]
    # print(response_dict)
    translated_code = response_dict["generated_text"]
    #print(translated_code)
    return translated_code

def translate_cpp_to_java(curr_id):
    if curr_id in cpp_functions:
        # print(cpp_functions[curr_id])
        text = cpp_java_prompt + cpp_functions[curr_id]

        inputs = {"inputs": text,
                  "parameters": {
                        "return_full_text": False
                  }}

    response = query(inputs)

    response_dict = response[0]
    # print(response_dict)
    translated_code =  response_dict["generated_text"]
    #print(translated_code)
    return translated_code


def save_code(code, filename):
    with open(filename, 'a') as file:
        file.write(code + '\n')

def read_code(filename):
    with open(filename, 'r') as file:
        return file.read()

# Main flow
if __name__ == "__main__":
    hypotheses_path = "./test_data_ids/"
    ids_cpp_java_path = hypotheses_path + "ids.cpp_sa-java_sa.test.txt"
    ids_cpp_python_path = hypotheses_path + "ids.cpp_sa-python_sa.test.txt"
    ids_java_python_path = hypotheses_path + "ids.java_sa-python_sa.test.txt"


    cpp_python_prompt = "[INST] You are a helpful bot which translates the given C++ code to Python. Provide the Python code in one line starting with the function definition, and don't say anything else. Do not output \"```python\" at the beginning and do not output \"'''\" at the end. To signify a new line put a \" NEWLINE \" and also use \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEWLINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEWLINE \": [/INST]"
    cpp_python_ic_prompt = "[INST] You are a helpful bot which translates the given C++ code to Python. Provide the Python code in one line starting with the function definition, and don't say anything else. Do not output \"```python\" at the beginning and do not output \"'''\" at the end. To signify a new line put a \" NEWLINE \" and also use \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEWLINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEWLINE \". Follow these examples: C++ code: int areaSquare ( int side ) { int area = side * side ; return area ; } Python code: def areaSquare ( side ) : NEW_LINE INDENT area = side * side NEW_LINE return area NEW_LINE DEDENT C++ code: int cassini ( int n ) { return ( n & 1 ) ? - 1 : 1 ; } Python code: def cassini ( n ) : NEW_LINE INDENT return - 1 if ( n & 1 ) else 1 NEW_LINE DEDENT Now translate this C++ code: [/INST]"
    java_python_prompt = "[INST] You are a helpful bot which translates the given C++ code to Python. Provide the Python code in one line starting with the function definition, and don't say anything else. Do not output \"```python\" at the beginning and do not output \"'''\" at the end. To signify a new line put a \" NEWLINE \" and also use \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEWLINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEWLINE \": [/INST]"
    java_python_ic_prompt = "[INST] You are a helpful bot which translates the given Java code to Python. Provide the Python code in one line starting with the function definition, and don't say anything else. Do not output \"```python\" at the beginning and do not output \"'''\" at the end. To signify a new line put a \" NEWLINE \" and also use \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEWLINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEWLINE \". Follow these examples: Java code: static int areaSquare ( int side ) { int area = side * side ; return area ; } Python code: def areaSquare ( side ) : NEW_LINE INDENT area = side * side NEW_LINE return area NEW_LINE DEDENT Java code: static int cassini ( int n ) { return ( n & 1 ) != 0 ? - 1 : 1 ; } Python code: def cassini ( n ) : NEW_LINE INDENT return - 1 if ( n & 1 ) else 1 NEW_LINE DEDENT Now translate this Java code: [/INST]"

    # python_cpp_prompt = "translate this Python code to C++, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```C++\" and the beginning and do not output \"'''\" at the end: "
    # python_cpp_prompt = "[INST] translate the given Python function to C++, don't say anything else, just give the code in one line starting with the function definition, just the translated function with no other output. do not include '\n' in the response. do not output \"```C++\" at the beginning and do not output \"'''\" at the end.\n Here is the function: \n[/INST]"
    python_cpp_prompt = "[INST] You are a helpful bot which translates the given Python code to C++. Provide the C++ code in one line starting with the function definition, and don't say anything else. The first word of the output should be the return type of the function, for example \"int\" for a function that returns an integer value. Don't include any \"\\n\" characters in the output and do not output \"```C++\" at the beginning. Here is the Python code to translate: [/INST]"
    python_cpp_ic_prompt = "[INST] You are a helpful bot which translates the given Python code to C++. Provide the C++ code in one line starting with the function definition, and don't say anything else. The first word of the output should be the return type of the function, for example \"int\" for a function that returns an integer value. Don't include any \"\\n\" characters in the output and do not output \"```C++\" at the beginning. Follow these examples: Python code: def areaSquare ( side ) : NEW_LINE INDENT area = side * side NEW_LINE return area NEW_LINE DEDENT C++ code: int areaSquare ( int side ) { int area = side * side ; return area ; } Python code: def cassini ( n ) : NEW_LINE INDENT return - 1 if ( n & 1 ) else 1 NEW_LINE DEDENT C++ code: int cassini ( int n ) { return ( n & 1 ) ? - 1 : 1 ; } Now translate this Python code: [/INST]"
    java_cpp_prompt = "[INST] You are a helpful bot which translates the given Java code to C++. Provide the C++ code in one line starting with the function definition, and don't say anything else. Don't include a main function or any comments. The first word of the output should be the return type of the function, for example \"int\" for a function that returns an integer value. Don't include any \"\\n\" characters in the output and do not output \"```C++\" at the beginning. Here is the Java code to translate: [/INST]"
    java_cpp_ic_prompt = "[INST] You are a helpful bot which translates the given Java code to C++. Provide the C++ code in one line starting with the function definition, and don't say anything else. The first word of the output should be the return type of the function, for example \"int\" for a function that returns an integer value. Don't include any \"\\n\" characters in the output and do not output \"```C++\" at the beginning. Follow these examples: Java code: static int intersection ( int n ) { return n * ( n - 1 ) ; } C++ code: int intersection ( int n ) { return n * ( n - 1 ) ; } Java code: static int cassini ( int n ) { return ( n & 1 ) != 0 ? - 1 : 1 ; } C++ code: int cassini ( int n ) { return ( n & 1 ) ? - 1 : 1 ; } Now translate this Java code: [/INST]"
    #java_cpp_prompt = "translate this Java code to C++, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```C++\" and the beginning and do not output \"'''\" at the end: "

    python_java_prompt = "translate this Python code to Java, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```Java\" and the beginning and do not output \"'''\" at the end. Also, make it static function, no public: "
    cpp_java_prompt = "translate this C++ code to Java, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```Java\" and the beginning and do not output \"'''\" at the end: "

    cpp_functions = get_cpp_functions()
    python_functions = get_python_functions()
    java_functions = get_java_functions()

    """
    # C++ TO PYTHON
    cpp_python_generated_path =  "./cpp_python_in_context.txt"

    open(cpp_python_generated_path , "w").close()
    with open(ids_cpp_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_cpp_to_python(curr_id, cpp_python_ic_prompt)
            save_code(translated_code, cpp_python_generated_path)
    """
    
    # Java TO PYTHON
    java_python_generated_path =  "./java_python.txt"

    open(java_python_generated_path , "w").close()
    with open(ids_java_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip() 
            translated_code = translate_java_to_python(curr_id, java_python_prompt)
            save_code(translated_code, java_python_generated_path)
    

    """
    # Java TO CPP
    java_cpp_generated_path =  "./java_cpp.txt"

    # open(java_cpp_generated_path , "w").close()
    with open(ids_cpp_java_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_java_to_cpp(curr_id, java_cpp_prompt)
            if translated_code != None:
                save_code(translated_code, java_cpp_generated_path)
    """
    """
    # Java TO CPP in context
    java_cpp_generated_path =  "./java_cpp_in_context.txt"

    # open(java_cpp_generated_path , "w").close()
    with open(ids_cpp_java_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_java_to_cpp(curr_id, java_cpp_ic_prompt)
            if translated_code != None:
                save_code(translated_code, java_cpp_generated_path)

    """
    # # PYTHON TO CPP
    """
    python_cpp_generated_path =  "./python_cpp_in_context.txt"

    open(python_cpp_generated_path , "w").close()
    with open(ids_cpp_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_python_to_cpp(curr_id, python_cpp_ic_prompt)
            if translated_code != None:
                save_code(translated_code, python_cpp_generated_path)
    """


