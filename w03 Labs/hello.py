from cs110 import expect, summarize
def front_hello_world(word: str) -> str:
    return 'Hello world! ' + word

expect(front_hello_world("!"), "Hello world!!")  
summarize()