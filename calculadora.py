import streamlit as st

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa Vibe")
st.write("Bem-vindo ao seu primeiro app web interativo criado com Python e Streamlit!")

st.divider()

# 2. Dois campos de entrada numérica com valor padrão 0.0
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Digite o primeiro número:", value=0.0)

with col2:
    num2 = st.number_input("Digite o segundo número:", value=0.0)

# 3. Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.write("") # Pequeno espaçamento visual

# 4. Botão de ação
if st.button("Calcular", type="primary"):
    
    # Processamento e regras de negócio
    if operacao == "Soma (+)":
        resultado = num1 + num2
        st.success(f"✨ O resultado de **{num1} + {num2}** é: **{resultado}**")
        
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
        st.success(f"✨ O resultado de **{num1} - {num2}** é: **{resultado}**")
        
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
        st.success(f"✨ O resultado de **{num1} × {num2}** é: **{resultado}**")
        
    elif operacao == "Divisão (/)":
        # 5. Tratamento amigável para divisão por zero
        if num2 == 0.0:
            st.error("⚠️ **Erro matemático:** Não é possível realizar uma divisão por zero. Por favor, escolha um segundo número diferente de zero.")
        else:
            resultado = num1 / num2
            st.success(f"✨ O resultado de **{num1} ÷ {num2}** é: **{resultado:.2f}**")
            