#!/usr/bin/python
#coding:utf-8
import web

import sys
from pygments import highlight
from pygments.formatters import html

urls = (
    '/', 'index',
    '/submit', 'submit'
)

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.hilite()

class submit:
    def POST(self):
        data = web.input()
        code = data.code
        language = data.lang
        if language == 'python':
            from pygments.lexers.python import PythonLexer
            lexer = PythonLexer()
        elif language == 'php':
            from pygments.lexers.php import PhpLexer
            lexer = PhpLexer()
        elif language == 'java':
            from pygments.lexers.jvm import JavaLexer
            lexer = JavaLexer()
        elif language == 'javascript':
            from pygments.lexers.javascript import JavascriptLexer
            lexer = JavascriptLexer()
        elif language == 'html':
            from pygments.lexers.html import HtmlLexer
            lexer = HtmlLexer()
        elif language == 'cpp':
            from pygments.lexers.c_cpp import CppLexer
            lexer = CppLexer()
        elif language == 'shell':
            from pygments.lexers.shell import ShellSessionLexer
            lexer = ShellSessionLexer()
        elif language == 'matlab':
            from pygments.lexers.matlab import MatlabLexer
            lexer = MatlabLexer()
        elif language == 'ruby':
            from pygments.lexers.ruby import RubyLexer
            lexer = RubyLexer()
        elif language == 'r':
            from pygments.lexers.r import RConsoleLexer
            lexer = RConsoleLexer()
        elif language == 'lisp':
            from pygments.lexers.lisp import SchemeLexer 
            lexer = SchemeLexer()
        elif language == 'go':
            from pygments.lexers.go import GoLexer
            lexer = GoLexer()
        formatter = html.HtmlFormatter(linenos=False, encoding='utf-8', nowrap=False)
        hilighted_snippet = highlight(code, lexer, formatter)
        #return hilighted
        #return render.submit()
        return render.result(hilighted_snippet)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
