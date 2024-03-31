from flask import Flask,render_template,url_for,request
from db_connector import getAvailableBooks,loginUser,addBookToCart,addUser


app=Flask(__name__)


@app.route("/")
def index():
    books=getAvailableBooks()
    return render_template("HomePage.html",all_books=books)

@app.route("/product")
def getProducts():
    book_id=request.args.get('book_id')
    title=request.args.get('title')
    img_url=request.args.get('img_url')
    price=request.args.get('price')
    desc=request.args.get('desc')
    return render_template("ProductDetails.html",book_id=book_id,title=title,img_url=img_url,price=price,desc=desc)

@app.route("/cart")
def getCart():  
    return render_template("Cart.html")

@app.route("/books")
def getBooks():
    return render_template("ViewBooks.html")

@app.route('/addBook',methods=['POST'])
def addBook():
    title=request.form.get('title')
    price=request.form.get('price')
    desc=request.form.get('desc')

@app.route("/login",methods=['POST'])
def login():
    email=request.form.get('signupEmail')
    password=request.form.get('signupPassword')
    user_details=loginUser(email,password)
    print(user_details)
    if len(user_details)>0:
        books=getAvailableBooks()
        if user_details[0][6]=='Buyer':
            return render_template('BuyerHomePage.html',all_books=books)
        else:
            return render_template("SellerHomePage.html",all_books=books)
    return "InValid Email & Password"


@app.route('/signUp',methods=['POST'])
def signUpUser():
    email=request.form.get('signupEmail')
    password=request.form.get('signupPassword')
    fname=request.form.get('fname')
    lname=request.form.get('lname')
    contact=request.form.get('contact')
    # print(email,password,fname,lname,contact)
    addUser(fname,lname,contact,email,password)
    return render_template("BuyerHomePage.html")


@app.route('/addToCart')
def addToCart():
    book_id=request.args.get('book_id')
    print(book_id)
    addBookToCart('1',book_id,'Added To Cart')
    return render_template("Cart.html")

if __name__=="__main__":
    app.run(debug=True)