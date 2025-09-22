msg = {
    "role": "user",
    "content": "Fala galera"
}

texto_msg = msg["content"]
print(texto_msg)

lista_msg = [
    {"role": "user", "content": "Fala Galera"},
    {"role": "assistant", "content":"Resposta da IA"},
    {"role": "user", "content": "TMJ"}
]

lista_msg.append(
    {"role": "assistant", "content": "Já é"}
)

print(lista_msg)

for msg in lista_msg:
    print(msg)
