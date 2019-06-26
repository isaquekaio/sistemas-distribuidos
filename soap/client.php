<?php
    $options = array(
        'uri' => 'http://localhost:8080/server.php',
        'location' => 'http://localhost:8080/server.php'
    );

    $client = new SoapClient(null, $options);

    // Já estamos conectados, vamos usar o método "somar" do servidor:
    echo(var_dump($client->somar(10, 15)));// 25
    echo(var_dump($client->subt(10, 15)));
    echo(var_dump($client->mult(10, 15)));
    echo(var_dump($client->divi(10, 15)));
    echo(var_dump($client->resto(10, 15)));
    //Executar o cliente: php client.php
?>