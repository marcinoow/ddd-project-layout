Usage
=====

``$ pip install -r requirements.txt``
``$ python main.py``

Output:

.. code::

    Fake action in simple service...
    Creating posts...
    Creating comment...
    Getting post from db...
    Post(id='a864467d-03ea-4369-95c1-6d2607ed6993', title='Post 1', content='Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
    Getting comment from db...
    Comment(id='f5e4c317-cdab-4f1b-8897-7709daace739', content="Lorem Ipsum has been the industry's standard dummy text", post=Post(id='a864467d-03ea-4369-95c1-6d2607ed6993', title='Post 1', content='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'))

