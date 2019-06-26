<?php
    $options = array(
        'uri' => 'http://localhost:8080/server.php'
    );
    $server = new SoapServer(null, $options);

    class MinhaInterfaceSoap
    {
        public function somar($valor1, $valor2)
        {
            return $valor1 + $valor2;
        }

        public function subt($valor1, $valor2)
        {
            return $valor1 - $valor2;
        }

        public function mult($valor1, $valor2)
        {
            return $valor1 * $valor2;
        }

        public function divi($valor1, $valor2)
        {
            return $valor1 / $valor2;
        }

        public function resto($valor1, $valor2)
        {
            return $valor1 % $valor2;
        }
    }

    // $server->setClass('MinhaInterfaceSoap');
    $server->setObject(new MinhaInterfaceSoap());

    $server->handle();
    //Executar o servidor: php -S localhost:8080 
?>
