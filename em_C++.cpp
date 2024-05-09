
//Isso são metodos de uma classe

typedef struct Tabuleiro_1 {
    int m[3][3]; // no meu caso tem que ser N por N
} Tabuleiro;

class No{
    private:
        Tabuleiro *tabuleiro;
        No *pai;
        Tabuleiro* clonarTabuleiro(Tabuleiro *tabuleiro);

    public:
        Tabuleiro* setTabuleiro(Tabuleiro *tabuleiro);
        Tabuleiro* getTabuleiro();
        No* setPai(No *pai);
        No* getPai();

        TList* movimentosPossiveis();
        No();
        int getLinhaPecaVazia();
        int getColunaPecaVazia();
        bool isSolucao(Tabuleiro *tabuleiro);
        AnsiString representacaoDoTabuleiro();
        AnsiString exibirMovimentos();
        AnsiString caminhoDasPecas(No *no);

};



TList * No::movimentosPossiveis(){ // METODO
    TList *vLista = new TList();
    int linha = getLinhaPecaVazia();
    int coluna = getColunaPecaVazia();
    No *vNo = 0;

    if (linha > 0) { // Pode mover para CIMA
        vNo = new No();
        vNo->setPai(this);
        vNo->setTabuleiro(clonarTabuleiro(this->getTabuleiro()));
        int aux = vNo->getTabuleiro()->m[linha-1][coluna];
        vNo->getTabuleiro()->m[linha-1][coluna] = 0;
        vNo->getTabuleiro()->m[linha][coluna] = aux;
        vLista->Add(vNo);
    };

    if (linha < 2){

    };
    if (coluna > 0){};

    if (coluna < 2){};

    return vLista;
};

int No::getLinhaPecaVazia(){
    for (int linha = 0; linha<3; linha++){
        for (int coluna =0; coluna<3;coluna++){
            if (this->tabuleiro->m[linha][coluna] == 0){
                return linha;
            };
        };
    };
};
// Mesma coisa pra coluna

class BuscaEmLargura{
    private:
        bool resolvido;
    public:
        No* buscar(No *noinicial, No *nofinal);
        bool isresolvido();
        BuscaEmLargura():
}