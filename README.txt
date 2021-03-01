 A Django application to store the information about Pizza.
admin- username-trilok, password- 12345
app name- piz
-------------------------------------------------

Mongo DB database configuration used to store data.
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'test1',
    }
}
------------------------------------------------

# What should I do After running ( py manage.py runserver )?

  A Home page will be appear which consists the two button, one is to show all stored pizza of all sizes that you would have created, and second one is to create new one.
If you'll go for stored pizzas, all pizzas created by you will appear with type, size and toppings. Every entry consist two buttons [Delete] and [Edit] to make operations as well.
After Deletion, you will be redirected to same page after deletion.
By clicking on Edit, a page will be open which shows the previous data and a form to make changes and after making changes hit on save changes, the record will be update on same id.

 If you want to filter them, on the right side of the page, the filter operation can perform on the basis of size of pizza( Small, Medium and Large).

If you'll go for Create new one, a form will appear consists two dropdown for type( Regular , Square) and size( Small, Medium , Large ) of the pizza, checkboxes for toppings will be appear. After filling details hit on create and the pizza will be added to the stored pizzas.

------------------------------------------------------------------
