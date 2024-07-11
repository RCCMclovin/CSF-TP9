# CSF-TP9

## Análise de um sistema IoT

Neste trabalho iremos analisar um sistema IoT pré-construido.

### Sistema de monitoramento remoto da qualidade da água

A Colônia Antônio Aleixo é um bairro periférico da cidade de Manaus, com aproximadamente 19 mil habitantes (dados de 2017), que lutam pela emancipação do bairro e elevação à município , em prol de uma qualidade melhor de vida aos seus moradores devido aos impostos desproporcionais às condições financeiras da população. Um dos pontos em prol da emancipação é o fato da comunidade possuir um serviço de fornecimento de água independente, mantido pela própria comunidade. O problema é que para manter esse serviço funcionando de forma legal, é necessário a medição de múltiplos parâmetros de qualidade d'água, como Oxigênio dissolvido, Potencial hidrogeniônico (pH), Temperatura da água, Turbidez, Resíduo total entre outros, que podem ser vistos em [Portal do IqA](https://portalpnqa.ana.gov.br/indicadores-indice-aguas.aspx). Atualmente, para conseguir esses dados a comunidade contrata uma empresa do estado de São Paulo, que uma vez por ano viaja para o local, coleta uma amostra de água e volta para sua sede, onde são feitas as medições em laboratório. Este processo todo acaba sendo muito oneroso. 
Uma solução para esse problema é utilizar-se de técnologias IoT para a criação de um Sistema Embarcado de monitoramento remoto, permitindo não apenas a coleta dos dados necessários, mas uma visão em tempo real da qualidade da água, e de ainda forma menos custosa do que o método atual. Dessa forma, um grupo do Laboratório de IoT para Sustentabilidade propôs um sistema embarcado composto por um nó de coleta, localizado em uma cisterna de água, e um ponto de acesso localizado em um centro admnistrativo na comunidade. O nó de coleta é composto por uma placa Esp32 Heltec Oled LoRa v2, integrado com sensores IoT de baixo custo, como [Thermistor NTC 10k ã Prova D'água](https://cdn.awsli.com.br/821/821277/arquivos/Datasheet%20MF58.pdf), [PH-4502C](https://www.smartprojectsbrasil.com.br/sensor-de-ph-modulo-de-leitura-arduino), [Turbidez ST100](https://www.usinainfo.com.br/outros-sensores-arduino/sensor-de-turbidez-arduino-st100-modulo-de-leitura-4539.html) e [Gravity TD](Shttps://www.usinainfo.com.br/blog/projeto-medidor-de-tds-arduino-para-condutividade-da-agua/). O ponto de acesso é composto por uma placa Raspberry [Pi Model 3b+](https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf), integrado com  [Dragino LoRa/GPS HAT](https://www.dragino.com/products/lora/item/106-lora-gps-hat.html), o que permite que os dois pontos se comuniquem via LoRa. 

Nesta demonstração, usaremos uma versão reduzida do nó de coleta, utilizando apenas dois sensores, temperatura e resíduos totais (TDS). 


![Placeholder Image](/img/img1.jpg)

![Example Image](/img/img2.jpg)

### Relatório

O relatório desta atividade deve conter:

+ Descrição dos componentes do sistema apresentado;
    + Descrevam, também, as conexões entre os componentes, exemplo: "sensor 1 se conecta com o ESP32 através da porta GPIO7"
    + Dica: Organizar as conexões em uma tabela para facilitar visualização, exemplo: "Porta no componente | Porta no ESP32"
+ Descrição do funcionamento do sistema;
    + O que ele faz? Qual a função de cada parte? O que ele faz com as informações coletadas? Onde cada parte do sistema deve ser instalada?
+ Matemática de RF;
    + Considerando a sensibilidade do ESP32, qual o alcance teórico do sistema no espaço livre? Qual o alcance com vegetação?
    + Usem as fórmulas apresentadas em sala de aula.
+ Proponham como testar cada parte do sistema;
+ Discussão sobre o protótipo apresentado:
    + Quais os próximos passos para implementação do sistema? O que pode ser melhorado? 
+ Conclusões;
