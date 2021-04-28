from flask import redirect, render_template, request, session, flash, url_for
from . import order
from ..models import Owner, Mattress, Models
from .order_forms import CheckoutForm

@order.route("/checkout/<int:model_id>", methods=['GET', 'POST'])
def checkout(model_id):
    own = Owner.query.all()
    model = Models.query.get_or_404(model_id)
    form_checkout = CheckoutForm()
    str_request = request.args.get('options')
    price = session.get('price')

    if form_checkout.validate_on_submit():
        # create order

        flash('Заказ отправлен', 'success')
        return redirect(url_for('main.index'))

    # if request.method == 'GET':
    #     if request.args.get('options'):
    #         str_request = request.args.get('options')

    return render_template('caravan/order.html', own=own, model=model, form=form_checkout, data_request=str_request, price=price, title='Checkout')
