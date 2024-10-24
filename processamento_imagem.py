from PIL import Image

def processar_imagem(caminho_imagem):
    
    imagem = Image.open(caminho_imagem)
    
    
    imagem_cinza = imagem.convert("L")
    
    
    caminho_imagem_cinza = "imagem_cinza.jpg"
    imagem_cinza.save(caminho_imagem_cinza)
    
    print(f"Imagem processada salva como {caminho_imagem_cinza}")


caminho_imagem = "portal.jpg" 
processar_imagem(caminho_imagem)
