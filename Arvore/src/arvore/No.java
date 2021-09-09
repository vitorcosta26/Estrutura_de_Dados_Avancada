package arvore;

public class No<T> {
	
	private T elemento;
	private int nivel;

	private No<T> esquerdo;
	private No<T> direito;
	
	public No (T elementoEntrada){
		this.elemento = elementoEntrada;
		this.esquerdo = null;
		this.direito = null;
	}

	public T getElemento() {
		return elemento;
	}

	public void setElemento(T elemento) {
		this.elemento = elemento;
	}
	
	public int getNivel() {
		return nivel;
	}

	public void setNivel(int nivel) {
		this.nivel = nivel;
	}

	public No<T> getEsquerdo() {
		return esquerdo;
	}

	public void setEsquerdo(No<T> esquerdo) {
		this.esquerdo = esquerdo;
	}

	public No<T> getDireito() {
		return direito;
	}

	public void setDireito(No<T> direito) {
		this.direito = direito;
	}
}
