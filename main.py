from pyscript import document

def do_something(event):
    input_text = document.querySelector("#something")
    inputz = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = inputz[::-1]
