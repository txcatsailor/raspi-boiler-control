<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Bootstrap TouchSpin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A mobile and touch friendly input spinner component for Bootstrap 3.">
    <meta name="author" content="István Ujj-Mészáros">

    <meta itemprop="name" content="Bootstrap Touchspin">
    <meta itemprop="description" content="A mobile and touch friendly input spinner component for Bootstrap 3.">

    <link rel="shortcut icon" href="libraries/favicon.ico">

    <link href="bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css" media="all">
    <link href="libraries/prettify/prettify.css" rel="stylesheet" type="text/css" media="all">
    <link href="libraries/demo.css" rel="stylesheet" type="text/css" media="all">

    <script src="libraries/jquery-1.9.0.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <script src="libraries/prettify/prettify.js"></script>
    <script src="bootstrap-touchspin/bootstrap.touchspin.js"></script>
</head>

<body>
<div class="container">
    <h1>Bootstrap TouchSpin</h1>

<div class="row">
    <div class="col-md-5">
        <label for="temp">Example using data attributes:</label> 
        <input
            id="temp"
            type="text"
            value="40"
            name="temp"
            data-bts-min="0"
            data-bts-max="100"
            data-bts-init-val=""
            data-bts-step="1"
            data-bts-decimal="0"
            data-bts-step-interval="100"
            data-bts-force-step-divisibility="round"
            data-bts-step-interval-delay="500"
            data-bts-prefix=""
            data-bts-postfix=""
            data-bts-prefix-extra-class=""
            data-bts-postfix-extra-class=""
            data-bts-booster="true"
            data-bts-boostat="10"
            data-bts-max-boosted-step="false"
            data-bts-mousewheel="true"
            data-bts-button-down-class="btn btn-default"
            data-bts-button-up-class="btn btn-default"
            >
    </div>




        <script>
            $("input[name='temp']").TouchSpin({
            });
        </script>

    </div>
</div>

<form action="/settemp" method="POST">
	
	Confirm Password: <input type="password" name="confpassword"><br>
<br/>
<input type="submit" name="save" value="save">
</form>