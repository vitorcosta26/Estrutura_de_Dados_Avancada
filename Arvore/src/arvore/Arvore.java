package arvore;

public class Arvore<T extends Comparable<T>> {
	
	private No<T> raiz;
	
	public Arvore() {
		super();
		this.raiz = null;
	}

	public No<T> getRaiz() {
		return raiz;
	}

	public void setRaiz(No<T> raiz) {
		this.raiz = raiz;
	}
	
	public void adicionar(T elemento) {
		No<T> entrada = new No<T> (elemento);
		int nivel = 0;
		if (this.raiz == null) {
			this.raiz = entrada;
			entrada.setNivel(nivel);
		} else {
			No<T> atual = this.raiz;
			while (true) {
				nivel++;
				entrada.setNivel(nivel);
				if(entrada.getElemento().compareTo(atual.getElemento()) == -1) {
					if (atual.getEsquerdo() != null) {
						atual = atual.getEsquerdo();
					} else {
						atual.setEsquerdo(entrada);
						break;
					}
				} else {
					if (atual.getDireito() != null) {
						atual = atual.getDireito();
					} else {
						atual.setDireito(entrada);
						break;
					}
				}
			}
		}
	}
	
	public void emOrdem(No<T> elemento) {
		if (elemento != null) {
			emOrdem(elemento.getEsquerdo());
			System.out.println("Nó: "+elemento.getElemento());
			System.out.println("Nível: "+elemento.getNivel());
			emOrdem(elemento.getDireito());
		}
	}
	
	public void preOrdem(No<T> elemento) {
		if (elemento != null) {
			System.out.println(elemento.getElemento());
			System.out.println("Nível: "+elemento.getNivel());
			preOrdem(elemento.getEsquerdo());
			preOrdem(elemento.getDireito());
		}
	}
	
	public void posOrdem(No<T> elemento) {
		if (elemento != null) {
			posOrdem(elemento.getEsquerdo());
			posOrdem(elemento.getDireito());
			System.out.println(elemento.getElemento());
			System.out.println("Nível: "+elemento.getNivel());
		}
	}
}
