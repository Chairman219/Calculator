from django.db.models.expressions import result
from django.shortcuts import render
from django.http import JsonResponse
import math

def calculator(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operation = request.POST.get("operation")

        try:
            num1 = float(num1)
            num2 = float(num2) if num2 else None

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    return JsonResponse({"error": "Chyba: dělení nulou není povoleno."})
            elif operation == "power":
                result = num1 ** num2
            elif operation == "sqrt":
                if num1 >= 0:
                    result = math.sqrt(num1)
                else:
                    return JsonResponse({"error": "Chyba: nelze vypočítat odmocninu z negativního čísla."})
            elif operation == "percent":
                result = (num1 * num2) / 100
            else:
                return JsonResponse({"error": "Neplatná operace."})

            return JsonResponse({"result": result})
        except ValueError:
            return JsonResponse({"error": "Neplatný vstup. Prosím zadejte pouze čísla."})

    return render(request, "calculator.html")


