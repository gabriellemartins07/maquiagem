import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="MakeupCadastro PRO",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "maquiagens.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1522335789203-aabd1fc54bc9"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_MAQUIAGEM = (
    "https://images.unsplash.com/"
    "photo-1596462502278-27bfdc403348"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
FONTE
========================================================= */

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #FFF5F7 0%,
            #F8E5EA 50%,
            #EFD3DC 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #3D1F2B,
            #632F45
        );

    border-right:
        2px solid #D49AAB;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #F5C7D4 !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #3D1F2B !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #704A58 !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(61,31,43,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(61,31,43,0.97) 0%,
            rgba(61,31,43,0.83) 45%,
            rgba(61,31,43,0.15) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #F0A9BD !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #FCEEF2 !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #B65F7A;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(182,95,122,0.25);

    box-shadow:
        0 10px 25px rgba(61,31,43,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #3D1F2B !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #765563 !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #3D1F2B,
            #663449
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(61,31,43,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #F8E9EE !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.90);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #D9A8B7;

    box-shadow:
        0 10px 30px rgba(61,31,43,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #3D1F2B !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #30232A !important;

    -webkit-text-fill-color:
        #30232A !important;

    border:
        2px solid #C78EA0 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #A94E6B !important;

    box-shadow:
        0 0 0 3px rgba(169,78,107,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #766B70 !important;
    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #403039 !important;

    border:
        2px solid #B56F85 !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #E0A5B8 !important;
}


/* =========================================================
MENU DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #403039 !important;
}

[data-baseweb="menu"] {
    background-color: #403039 !important;
}

[role="option"] {
    background-color: #403039 !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #704054 !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #A94E6B,
            #C87891
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(169,78,107,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #853B55,
            #AA5B75
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #D9A8B7;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #765563 !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Marca",
        "Produto",
        "Categoria",
        "Tipo_Pele",
        "Tonalidade",
        "Peso_g",
        "Estoque",
        "Preco",
        "Observacoes"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(
                ARQUIVO,
                encoding="utf-8-sig"
            )

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# =========================================================
# GARANTIR COLUNAS
# =========================================================

colunas_necessarias = [
    "Marca",
    "Produto",
    "Categoria",
    "Tipo_Pele",
    "Tonalidade",
    "Peso_g",
    "Estoque",
    "Preco",
    "Observacoes"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


# =========================================================
# CONVERTER VALORES NUMÉRICOS
# =========================================================

df["Peso_g"] = pd.to_numeric(
    df["Peso_g"],
    errors="coerce"
).fillna(0)

df["Estoque"] = pd.to_numeric(
    df["Estoque"],
    errors="coerce"
).fillna(0)

df["Preco"] = pd.to_numeric(
    df["Preco"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
💄 MakeupCadastro
</div>

<div class="logo-subtitle">
GESTÃO INTELIGENTE DE MAQUIAGEM
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Maquiagem",
        "💄 Maquiagens Cadastradas"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "MakeupCadastro PRO • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Sua beleza.<br>
Seu estoque.
</div>

<div class="hero-text">
Tenha todos os seus produtos de maquiagem organizados
em um único lugar. Cadastre, consulte e acompanhe
seus produtos de forma simples, rápida e profissional.
</div>

<div class="hero-badge">
💄 GESTÃO INTELIGENTE
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
"""
<div class="page-title">
📊 Visão geral da sua maquiagem
</div>

<div class="page-subtitle">
Acompanhe seus produtos e mantenha seu estoque organizado.
</div>
""",
        unsafe_allow_html=True
    )


    # =====================================================
    # INDICADORES
    # =====================================================

    total_produtos = len(df)

    estoque_total = df["Estoque"].sum()

    valor_total = (
        df["Estoque"] * df["Preco"]
    ).sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💄
</div>

<div class="card-number">
{total_produtos}
</div>

<div class="card-label">
PRODUTOS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
📦
</div>

<div class="card-number">
{estoque_total:,.0f}
</div>

<div class="card-label">
UNIDADES EM ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR TOTAL DO ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # INFORMAÇÕES
    # =====================================================

    coluna1, coluna2 = st.columns(
        [1.1, 1]
    )


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Gestão profissional
</h2>

<p>
O MakeupCadastro PRO permite manter todos os seus
produtos de maquiagem organizados em um único lugar.
</p>

<p>
Cadastre, consulte, pesquise e acompanhe seus produtos,
preços e estoque de maneira moderna e profissional.
</p>

<p>
Ideal para lojas de maquiagem, pequenos negócios,
revendedoras e catálogos de beleza.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_MAQUIAGEM,
            use_container_width=True
        )


# =========================================================
# CADASTRAR MAQUIAGEM
# =========================================================

elif menu == "➕ Cadastrar Maquiagem":

    st.markdown(
"""
<div class="page-title">
➕ Nova maquiagem
</div>

<div class="page-subtitle">
Adicione um novo produto ao seu catálogo.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_maquiagem",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        # =================================================
        # COLUNA 1
        # =================================================

        with col1:

            marca = st.text_input(
                "🏷️ Marca",
                placeholder="Ex: Bella Beauty"
            )


            produto = st.text_input(
                "💄 Nome do Produto",
                placeholder="Ex: Base Matte"
            )


            categoria = st.selectbox(
                "🛍️ Categoria",
                [
                    "Base",
                    "Corretivo",
                    "Pó",
                    "Blush",
                    "Contorno",
                    "Iluminador",
                    "Batom",
                    "Gloss",
                    "Lápis",
                    "Delineador",
                    "Máscara de Cílios",
                    "Sombra",
                    "Paleta de Sombras",
                    "Primer",
                    "Fixador",
                    "Esponja",
                    "Pincel",
                    "Kit de Maquiagem",
                    "Outro"
                ]
            )


            tipo_pele = st.selectbox(
                "✨ Tipo de Pele",
                [
                    "Todos os tipos",
                    "Pele seca",
                    "Pele oleosa",
                    "Pele mista",
                    "Pele normal",
                    "Pele sensível"
                ]
            )


        # =================================================
        # COLUNA 2
        # =================================================

        with col2:

            tonalidade = st.text_input(
                "🎨 Tonalidade / Cor",
                placeholder="Ex: Bege Médio"
            )


            peso = st.number_input(
                "⚖️ Peso / Quantidade (g)",
                min_value=0.0,
                value=10.0,
                step=1.0
            )


            estoque = st.number_input(
                "📦 Quantidade em Estoque",
                min_value=0,
                value=0,
                step=1
            )


            preco = st.number_input(
                "💰 Preço de Venda",
                min_value=0.0,
                value=0.0,
                step=5.0
            )


            observacoes = st.text_area(
                "📝 Observações",
                placeholder="Informações adicionais sobre o produto..."
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR MAQUIAGEM"
        )


    # =====================================================
    # SALVAR
    # =====================================================

    if cadastrar:

        if (
            marca.strip()
            and produto.strip()
        ):

            novo_produto = pd.DataFrame(
                [{
                    "Marca": marca.strip(),
                    "Produto": produto.strip(),
                    "Categoria": categoria,
                    "Tipo_Pele": tipo_pele,
                    "Tonalidade": tonalidade.strip(),
                    "Peso_g": float(peso),
                    "Estoque": int(estoque),
                    "Preco": float(preco),
                    "Observacoes": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_produto
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "💄 Maquiagem cadastrada com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha a Marca e o Nome do Produto."
            )


# =========================================================
# MAQUIAGENS CADASTRADAS
# =========================================================

elif menu == "💄 Maquiagens Cadastradas":

    st.markdown(
"""
<div class="page-title">
💄 Meu catálogo
</div>

<div class="page-subtitle">
Consulte, pesquise e gerencie todos os produtos cadastrados.
</div>
""",
        unsafe_allow_html=True
    )


    # =====================================================
    # CATÁLOGO VAZIO
    # =====================================================

    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
💄 Nenhuma maquiagem cadastrada
</h2>

<p>
Seu catálogo ainda está vazio.
Cadastre seu primeiro produto para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    # =====================================================
    # CATÁLOGO COM PRODUTOS
    # =====================================================

    else:

        busca = st.text_input(
            "🔎 Pesquisar produto",
            placeholder="Digite marca, produto, categoria, cor ou tonalidade..."
        )


        # =================================================
        # PESQUISA
        # =================================================

        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        # =================================================
        # TABELA
        # =================================================

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        # =================================================
        # EXCLUSÃO
        # =================================================

        opcoes_produtos = df.index.tolist()


        produto_excluir = st.selectbox(
            "🗑️ Selecione um produto para excluir",
            options=opcoes_produtos,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} - "
                f"{df.loc[indice, 'Produto']} - "
                f"{df.loc[indice, 'Tonalidade']}"
        )


        if st.button(
            "🗑️ EXCLUIR PRODUTO"
        ):

            df = df.drop(
                produto_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "💄 Produto excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

💄 MakeupCadastro PRO<br>
Gestão inteligente de produtos de beleza

</div>
""",
    unsafe_allow_html=True
)
