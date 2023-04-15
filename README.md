<!DOCTYPE html>
<html>
<head>
	<title>Aplicativo Flask</title>
</head>
<body>
	<h1>Aplicativo Flask</h1>
	<p>Este é um aplicativo Flask simples com uma única rota que renderiza um modelo HTML.</p>
php
Copy code
<h2>Requisitos</h2>
<ul>
	<li>Python 3.x</li>
	<li>Flask</li>
</ul>

<h2>Uso</h2>
<ol>
	<li>Clone o repositório:</li>
	<pre><code>git clone https://github.com/seu-nome-de-usuário/seu-repo.git</code></pre>
	<li>Mude para o diretório clonado:</li>
	<pre><code>cd seu-repo</code></pre>
	<li>Instale o Flask:</li>
	<pre><code>pip install flask</code></pre>
	<li>Execute o aplicativo:</li>
	<pre><code>python app.py</code></pre>
	<li>Acesse o aplicativo em seu navegador:</li>
	<pre><code>http://localhost:5000/</code></pre>
</ol>

<h2>Explicação do Código</h2>
<p>O aplicativo é uma aplicação web de página única que renderiza um modelo HTML usando a função <code>render_template</code> do Flask. O decorador <code>@app.route('/')</code> especifica a rota da URL para a página inicial. O bloco <code>if __name__ == '__main__':</code> inicia o servidor de desenvolvimento do Flask quando o script é executado. O parâmetro <code>debug=True</code> habilita o modo de depuração, que fornece mensagens de erro detalhadas em caso de exceções.</p>
</body>
</html>
