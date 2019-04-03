/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 20172014040034
 */
//public class client {}
import java.net.*;
import java.io.*;

public class client{
    private String endereco;
    private int porta;
    private InputStream is;
    private Socket s;
    public client(){
    }
    
    public client(String endereco, int porta){
        this.endereco = endereco;
        this.porta = porta;
        try{
            s = new Socket(endereco, porta);
            is = s.getInputStream();
            
            /*byte[] b = new byte[1000];

            is.read(b);//read
            is.close();
            System.out.println("Dados: "+new String(b).trim());*/
        }catch(UnknownHostException uhe){
            uhe.printStackTrace();
        }catch(IOException ioe){
            ioe.printStackTrace();
        }
    }

    public String receber() throws IOException{
            byte[] b = new byte[1000];
            is.read(b);//read
            is.close();
            //System.out.println("Dados: "+new String(b).trim());
            return new String(b).trim();
    }
    
    
    public static void main(String args[]){
        client c = new client();
    }
}