# **Documentação da Classe Controle**

A classe **`Controle`** é um componente do Spring MVC desenvolvido para lidar com requisições relacionadas a mensagens de boas-vindas em um aplicativo web. Esta classe inclui métodos que respondem a diferentes endpoints, fornecendo mensagens de boas-vindas de maneiras variadas.

## **Overview**

A classe **`Controle`** é anotada com **`@RestController`**, indicando que os métodos desta classe retornam diretamente os valores de retorno como respostas HTTP apropriadas. Os métodos são mapeados para diferentes endpoints usando a anotação **`@GetMapping`**.

## **Métodos**

### **1. Método `mensagem()`**

Este método manipula requisições para o endpoint padrão ("/") e retorna a mensagem "Hello World!".

- **Endpoint:** "/"
- **Método HTTP:** GET
- **Retorno:** Uma mensagem de saudação padrão.

```java
javaCopy code
@GetMapping("")
public String mensagem() {
    return "Hello World!";
}
```

### **2. Método `boasVindas()`**

Este método manipula requisições para o endpoint "/boasVindas/" e retorna a mensagem "Seja bem vindo(a)".

- **Endpoint:** "/boasVindas/"
- **Método HTTP:** GET
- **Retorno:** Uma mensagem de boas-vindas genérica.

```java
javaCopy code
@GetMapping("/boasVindas/")
public String boasVindas() {
    return "Seja bem vindo(a)";
}
```

### **3. Método `boasVindas(String nome)`**

Este método manipula requisições para o endpoint "/boasVindas/{nome}" e retorna uma mensagem de boas-vindas personalizada com o nome fornecido como parâmetro de caminho.

- **Endpoint:** "/boasVindas/{nome}"
- **Método HTTP:** GET
- **Parâmetro:** **`nome`** - O nome a ser incluído na mensagem de boas-vindas.
- **Retorno:** Uma mensagem de boas-vindas personalizada com o nome fornecido.

```java
javaCopy code
@GetMapping("/boasVindas/{nome}")
public String boasVindas(@PathVariable String nome) {
    return "Seja bem vindo(a) " + nome;
}
```

A classe **`Controle`** oferece endpoints simples, mas versáteis, para fornecer mensagens de boas-vindas. Os métodos são projetados para serem facilmente integrados em um aplicativo web Spring MVC, proporcionando uma experiência amigável aos usuários.
