from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Pizza import Pizza
from utils import db

bp_pizzas = Blueprint('pizzas', __name__)

@bp_pizzas.route('/pizzas/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        sabor = request.form['sabor']
        imagem = request.form['imagem']
        ingredientes = request.form['ingredientes']
        preco = float(request.form['preco'])

        nova_pizza = Pizza(sabor=sabor, imagem=imagem, ingredientes=ingredientes, preco=preco)
        db.session.add(nova_pizza)
        db.session.commit()
        flash('Pizza cadastrada com sucesso!')
        return redirect(url_for('pizzas.list'))

    return render_template('create_pizza.html')

@bp_pizzas.route('/pizzas/recovery', methods=['GET'])
def recovery():
    pizzas = Pizza.query.all()
    return render_template('recovery_pizza.html', pizzas=pizzas)
