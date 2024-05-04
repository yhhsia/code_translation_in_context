

import os
import requests
import difflib
import sys


# Constants
API_URL = "https://api.openai.com/v1/chat/completions"

API_KEY = ""
HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}



def get_cpp_functions():
    cpp_functions = {}
    test_files_path = "./../test_data_ids/"
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
    test_files_path = "./../test_data_ids/"
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
    test_files_path = "./../test_data_ids/"
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
    


def translate_cpp_to_python(curr_id):
    if curr_id in cpp_functions:
        # print(cpp_functions[curr_id])
        text = cpp_python_prompt + cpp_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code


def translate_cpp_to_python_in_context(curr_id):
    if curr_id in cpp_functions:
        # print(cpp_functions[curr_id])
        text = cpp_python_incontext_prompt + cpp_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_java_to_python(curr_id):
    if curr_id in java_functions:
        # print(cpp_functions[curr_id])
        text = java_python_prompt + java_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_java_to_python_in_context(curr_id):
    if curr_id in java_functions:
        # print(cpp_functions[curr_id])
        text = java_python_incontext_prompt + java_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code



def translate_python_to_cpp(curr_id):
    if curr_id in python_functions:
        # print(cpp_functions[curr_id])
        text = python_cpp_prompt + python_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_python_to_cpp_in_context(curr_id):
    if curr_id in python_functions:
        # print(cpp_functions[curr_id])
        text = python_cpp_incontext_prompt + python_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_java_to_cpp(curr_id):
    if curr_id in java_functions:
        # print(cpp_functions[curr_id])
        text = java_cpp_prompt + java_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_java_to_cpp_in_context(curr_id):
    if curr_id in java_functions:
        # print(cpp_functions[curr_id])
        text = java_cpp_incontext_prompt + java_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_python_to_java(curr_id):
    if curr_id in python_functions:
        # print(cpp_functions[curr_id])
        text = python_java_prompt + python_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code

def translate_cpp_to_java(curr_id):
    if curr_id in cpp_functions:
        # print(cpp_functions[curr_id])
        text = cpp_java_prompt + cpp_functions[curr_id]

        payload = {
            "model": "gpt-4-turbo-2024-04-09",
            "messages": [{"role": "user", "content": text}],
            "max_tokens": 500
        }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    response_dict = response.json()
    # print(response_dict)
    translated_code =  response_dict["choices"][0]["message"]["content"]
    print(translated_code)
    return translated_code


def save_code(code, filename):
    with open(filename, 'a') as file:
        file.write(code + '\n')

def read_code(filename):
    with open(filename, 'r') as file:
        return file.read()

# Main flow
if __name__ == "__main__":
    hypotheses_path = "./../test_data_ids/"
    ids_cpp_java_path = hypotheses_path + "ids.cpp_sa-java_sa.test.txt"
    ids_cpp_python_path = hypotheses_path + "ids.cpp_sa-python_sa.test.txt"
    ids_java_python_path = hypotheses_path + "ids.java_sa-python_sa.test.txt"

    cpp_example = "unsigned int factorial ( unsigned int n ) { int res = 1 , i ; for ( i = 2 ; i <= n ; i ++ ) res *= i ; return res ; }"
    python_example = "def factorial ( n ) : NEW_LINE INDENT return 1 if ( n == 1 or n == 0 ) else n * factorial ( n - 1 ) NEW_LINE DEDENT"
    java_example = "static int factorial ( int n ) { int res = 1 , i ; for ( i = 2 ; i <= n ; i ++ ) res *= i ; return res ; }"


    cpp_python_prompt = "translate this C++ to Python, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```python\" and the beginning and do not output \"'''\" at the end. To signifiy a new line put a \" NEW_LINE \" and also put \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEW_LINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEW_LINE \": "
    cpp_python_incontext_prompt = "translate this C++ code to Python, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```python\" and the beginning and do not output \"'''\" at the end. To signifiy a new line put a \" NEW_LINE \" and also put \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEW_LINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEW_LINE \". Follow this example, C++ code: " + cpp_example + " and this is the translated python code : " + python_example + " now translate this C++ code: "
    java_python_prompt = "translate this Java code to Python, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```python\" and the beginning and do not output \"'''\" at the end. To signifiy a new line put a \" NEW_LINE \" and also put \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEW_LINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEW_LINE \": "
    java_python_incontext_prompt = "translate this Java code to Python, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```python\" and the beginning and do not output \"'''\" at the end. To signifiy a new line put a \" NEW_LINE \" and also put \" INDENT \" and \" DEDENT \" to signify in the code when you would indent and dedent. Make sure to put a \" NEW_LINE \" at the end before the last \" DEDENT \". The last \" DEDENT \" should be after the last \" NEW_LINE \". Follow this example, C++ code: " + java_example + " and this is the translated python code : " + python_example + " now translate this Java code: "

    python_cpp_prompt = "translate this Python code to C++, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```C++\" and the beginning and do not output \"'''\" at the end: "
    python_cpp_incontext_prompt = "translate this Python code to C++, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```C++\" and the beginning and do not output \"'''\" at the end. Follow this example, Python code: " + python_example + " and this is the translated C++ code : " + cpp_example + " now translate this Python code: "
    java_cpp_prompt = "translate this Java code to C++, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```C++\" and the beginning and do not output \"'''\" at the end: "
    java_cpp_incontext_prompt = "translate this Java code to C++, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```C++\" and the beginning and do not output \"'''\" at the end. Follow this example, Java code: " + java_example + " and this is the translated C++ code : " + cpp_example + " now translate this Java code: "
    python_java_prompt = "translate this Python code to Java, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```Java\" and the beginning and do not output \"'''\" at the end. Also, make it static function, no public: "
    cpp_java_prompt = "translate this C++ code to Java, don't say anything else, just give the code in one line, just the code with nothing else. do not output \"```Java\" and the beginning and do not output \"'''\" at the end: "

    cpp_functions = get_cpp_functions()
    python_functions = get_python_functions()
    java_functions = get_java_functions()

    # C++ TO PYTHON
    cpp_python_generated_path =  "./cpp_python.txt"

    open(cpp_python_generated_path , "w").close()
    with open(ids_cpp_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_cpp_to_python(curr_id)
            save_code(translated_code, cpp_python_generated_path)


    # C++ TO PYTHON IN CONTEXT
    cpp_python_generated_path =  "./cpp_python_in_context.txt"

    open(cpp_python_generated_path , "w").close()
    with open(ids_cpp_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_cpp_to_python_in_context(curr_id)
            save_code(translated_code, cpp_python_generated_path)

    # # Java TO PYTHON
    java_python_generated_path =  "./java_python.txt"

    open(java_python_generated_path , "w").close()
    with open(ids_java_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip() 
            translated_code = translate_java_to_python(curr_id)
            save_code(translated_code, java_python_generated_path)


    # JAVA TO PYTHON IN CONTEXT
    java_python_generated_path =  "./java_python_in_context.txt"

    open(java_python_generated_path , "w").close()
    with open(ids_java_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip() 
            translated_code = translate_java_to_python_in_context(curr_id)
            save_code(translated_code, java_python_generated_path)


    # Java TO CPP
    java_cpp_generated_path =  "./java_cpp.txt"

    # open(java_cpp_generated_path , "w").close()
    with open(ids_cpp_java_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_java_to_cpp(curr_id)
            save_code(translated_code, java_cpp_generated_path)

    # JAVA TO CPP IN CONTEXT
    java_cpp_generated_path =  "./java_cpp_in_context.txt"

    # open(java_cpp_generated_path , "w").close()
    with open(ids_cpp_java_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_java_to_cpp_in_context(curr_id)
            save_code(translated_code, java_cpp_generated_path)


    # # PYTHON TO CPP
    python_cpp_generated_path =  "./python_cpp.txt"

    open(python_cpp_generated_path , "w").close()
    with open(ids_cpp_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_python_to_cpp(curr_id)
            save_code(translated_code, python_cpp_generated_path)

    # PYTOHN TO CPP INCONTEXT
    python_cpp_generated_path =  "./python_cpp_in_context.txt"

    open(python_cpp_generated_path , "w").close()
    with open(ids_cpp_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_python_to_cpp_in_context(curr_id)
            save_code(translated_code, python_cpp_generated_path)

    # PYTHON TO JAVA
    python_java_generated_path =  "./python_java.txt"

    open(python_java_generated_path , "w").close()
    with open(ids_java_python_path, 'r') as file:
        for line in file:
            curr_id = line.strip()  
            translated_code = translate_python_to_java(curr_id)
            save_code(translated_code, python_java_generated_path)



    # # CPP to JAVA
    cpp_java_generated_path =  "./cpp_java.txt"

    open(cpp_java_generated_path , "w").close()
    with open(ids_cpp_java_path, 'r') as file:
        for line in file:
            curr_id = line.strip() 
            translated_code = translate_cpp_to_java(curr_id)
            save_code(translated_code, cpp_java_generated_path)



