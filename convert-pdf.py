from tkinter import Tk, filedialog
from PIL import Image

def selecionar_imagem_e_converter():
    janela = Tk()
    janela.withdraw()
    janela.title("Selecionar imagem")
    
    tipos_arquivos = [("Imagens", "*.jpeg;*.jpg;*.png")]
    
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem para converter em PDF",
        filetypes=tipos_arquivos
    )
    
    if not caminho_imagem:
        print("Nenhuma imagem foi selecionada.")
        return
    
    try:
        imagem = Image.open(caminho_imagem).convert('RGB')
        
        caminho_pdf = filedialog.asksaveasfilename(
            title="Salvar PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if not caminho_pdf:
            print("O processo de salvamento foi cancelado.")
            return
        
        imagem.save(caminho_pdf)
        print(f"PDF salvo com sucesso em: {caminho_pdf}")
    
    except Exception as e:
        print(f"Ocorreu um erro ao converter a imagem: {e}")

if __name__ == "__main__":
    selecionar_imagem_e_converter()
