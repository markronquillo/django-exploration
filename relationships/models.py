from django.db import models


"""
    BASIC
    =====
    A Book has many author
    An Author has many book
    A Book has one publication
    A Publication published a lot of books
    --------------------------------------
    * Saving an author, book and their relationship
    b = Book(title='So good they cant ignore you.')
    b.save()
    a = Author(name="Cal Newport")
    a.save()
    b.authors.add(a)

    * Books and Publication
    p = Publication(name="the publisher")
    p.save()
    b = Book(title="So good", publication=p)
    b.save()
    ----------------------------------------
    
    INTERMEDIATE
    ============
    An author can follow other authors and view the books they've published
    --------------------------------------
    * Author follows an Author
    a = Author.objects.create(name='author1')
    a2 = Author.objects.create(name='author2')
    Contact.objects.create(author_from=a, author_to=a2)

"""

class Publication(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    following = models.ManyToManyField('self', 
                                       through='Contact', 
                                       related_name='follower',
                                       symmetrical=False)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publication = models.ForeignKey(Publication, related_name='published_books')


class Contact(models.Model):
    author_from = models.ForeignKey(Author, related_name='rel_from_set')
    author_to = models.ForeignKey(Author, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)


