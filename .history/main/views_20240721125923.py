from django.shortcuts import render


def products(request):
    person = [
        {'img': 'data:image/jpeg;base64,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',  }
    ]
    return render(request, 'product.html')

