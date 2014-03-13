page ="""
<html>
	<head>
		<style>
			.backgroundImage
			{
				background-color:silver;
			}
			.center
			{
				text-align:center;
			}
		</style>
	</head>
    <title>NLP PROJECT</title>
    <body class = "backgroundImage">
		<div class ="center">
    			<h1>NLP PROJECT SEARCH</h1>
        		<form method = 'post' action = '/searchFile'>
        			<input name ='input' value = '%s' type ='text' >
        			<input name ='submit' value = 'submit' type ='submit' >
        		</form>
		</div>
    </body>
</html>
"""



class HTML_PAGE():
    def pageChange(self,input=''):
        return page%(input)
        