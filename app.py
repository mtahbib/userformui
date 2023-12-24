from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = {
        'firstname': request.form['firstname'],
        'secondname': request.form['secondname'],
        'addressline1': request.form['addressline1'],
        'addressline2': request.form['addressline2'],
        'addressline3': request.form['addressline3'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip': request.form['zip'],
        'homephe': request.form['homephe'],
        'workphe': request.form['workphe'],
        'mobile': request.form['mobile'],
        'email': request.form['email'],
        'email2': request.form['email2'],
        'notes': request.form['notes']
    }

    address_book_name = request.form['addressbookname']
    save_to_file(address_book_name, data)

    return redirect(url_for('index'))

def save_to_file(address_book_name, data):
    directory = 'AddressBookDataBase'
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, address_book_name + '.txt')

    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f'{key}: {value}\n')

    with open(os.path.join(directory, 'filenames.txt'), 'a') as filenames_file:
        filenames_file.write(address_book_name + '\n')

if __name__ == '__main__':
    app.run(debug=True)
