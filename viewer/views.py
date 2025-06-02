from django.shortcuts import render


def hello(request):
    # práce s databází
    #context = {'adjectives': ['nice', 'cruel', 'blue', 'beautiful']}

    adjectives = ['nice', 'cruel', 'blue', 'beautiful']
    name = 'Petr'
    context = {'adjectives': adjectives, 'name': name}
    return render(request=request,
                  template_name='hello.html',
                  context=context)
