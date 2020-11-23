import java.util.HashMap;
public class Frecuencia_de_Texto {

    public static void main(String[] args) {
        
        String Texto = "El lema que anima a la Universidad Nacional, Por mi raza hablará el espíritu, revela la vocación humanística con la que fue concebida. El autor de esta célebre frase, José Vasconcelos, asumió la rectoría en 1920, en una época en que las esperanzas de la Revolución aún estaban vivas, había una gran fé en la Patria y el ánimo redentor se extendía en el ambiente.";        
        System.out.println(Texto);
        Texto = Texto.toLowerCase();
        Texto = Texto.replace(",", "");
        Texto = Texto.replace(".", "");
        Texto = Texto.replace("á", "a");
        Texto = Texto.replace("é", "e");
        Texto = Texto.replace("í", "i");
        Texto = Texto.replace("ó", "o");
        Texto = Texto.replace("ú", "u");
        System.out.println(Texto);        
        
        String[] arr = Texto.split(" ");  
        HashMap < String, Integer > Frecuencia = new HashMap<>();
        
        for(String palabras : arr){
            if(Frecuencia.containsKey(palabras)){
                Frecuencia.put(palabras, Frecuencia.get(palabras)+1);
            }
            else{
                Frecuencia.put(palabras, 1);
            }            
        }
        System.out.println("\nFrecuencia: \t/\tPalabra:");
        for(HashMap.Entry<String, Integer> entry : Frecuencia.entrySet()){
            System.out.println("    "+entry.getValue() + "\t\t-\t"+ entry.getKey());
        }
    }    
}
