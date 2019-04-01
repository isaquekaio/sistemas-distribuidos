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
    private String endereco = end;
    private int porta = port;
    
    public client(){
        try{
            Socket s = new Socket(endereco, porta);
            InputStream is = s.getInputStream();
            
            byte[] b = new byte[1000];

            is.read(b);//read
            is.close();
            System.out.println("Dados: "+new String(b).trim());
        }catch(UnknownHostException uhe){
            uhe.printStackTrace();
        }catch(IOException ioe){
            ioe.printStackTrace();
        }
    }

    public static void main(String args[]){
        client c = new client();
    }
}