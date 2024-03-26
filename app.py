from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/sample', methods=['GET', 'POST'])
def choices():
    if request.method == 'POST':
        val = request.form.get('button')
    
    choice = int(val)
    
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    comp_choice = random.randint(1,3)
    
    if comp_choice == 1:
        choice_name2 = "Rock"
    elif comp_choice == 2:
        choice_name2 = "Paper"
    else:
        choice_name2 = "Scissor"
    
    result = ["Draw!","You won!","You Lost!"]
    
    if choice == comp_choice:
        i = 0
        res = result[i]
    elif choice == 1 and comp_choice == 2:
        i = 2
        res = result[i]
    elif choice == 1 and comp_choice == 3:
        i = 1
        res = result[i]
    elif choice == 2 and comp_choice == 1:
        i = 1
        res = result[i]
    elif choice == 2 and comp_choice == 3:
        i = 2
        res = result[i]
    elif choice == 3 and comp_choice == 1:
        i = 2
        res = result[i]
    elif choice == 3 and comp_choice == 2:
        i = 1
        res = result[i]
    else:
        print("Unexpected error")           
     
    return render_template('index.html',choice_name=choice_name,choice_name2=choice_name2,res=res)

if __name__=='__main__':
    app.run(debug=True, port=5500)
