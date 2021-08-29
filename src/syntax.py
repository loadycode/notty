# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

pygmentImportError = False

import tkinter as tk

try:
	from pygments.lexers import JsonLexer
	from pygments.lexers import CLexer
	from pygments.lexers import HtmlLexer
	from pygments.lexers import CssLexer
	from pygments.lexers import CppLexer
	from pygments.lexers import PythonLexer
	from pygments.lexers import JavascriptLexer
	from pygments.lexers import MarkdownLexer
	from pygments.token import Token
except ImportError:
	pygmentImportError = True
	print ('(!) pygments import error')

array = [
	'json',
	'c lang',
	'c++ lang',
	'html',
	'css',
	'python',
	'javascript',
	'markdown'
]

color_keyword = '#ff00cc'
color_string_literal = '#00cc66'
color_comment = '#999999'
color_name_builtin = '#3399cc'
color_keyword_ext = '#ff0000'

token_type_to_tag = {
		Token.Keyword: 'keyword',
		Token.Keyword.Type: 'keyword_ext',
		Token.Keyword.Reserved: 'keyword_ext',
		Token.Keyword.Constant:'keyword_ext',
		Token.Operator.Word: 'keyword',
		Token.Name.Builtin: 'name_builtin',
		Token.Literal.String.Single: 'string_literal',
		Token.Literal.String.Double: 'string_literal',
		Token.Comment.Single: 'comment',
		Token.Comment.Hashbang: 'comment',
		Token.Comment.Multiline: 'comment'
}

def tokens_init (textbox):

	textbox.tag_config ('keyword', foreground = color_keyword)
	textbox.tag_config ('keyword_ext', foreground = color_keyword_ext)
	textbox.tag_config ('name_builtin', foreground = color_name_builtin)
	textbox.tag_config ('string_literal', foreground = color_string_literal)
	textbox.tag_config ('comment', foreground = color_comment)

def tokens_get(textbox,lexer):

	def get_text_coord (s: str, i: int):
		for row_number, line in enumerate (s.splitlines (keepends=True), 1):
			if i < len (line):
				return f'{row_number}.{i}'
			i -= len (line)
	for tag in textbox.tag_names ():
		textbox.tag_remove (tag, 1.0, 'end')
	s = textbox.get (1.0, 'end')
	tokens = lexer.get_tokens_unprocessed (s)
	for i, token_type, token in tokens:
		j = i + len (token)
		if token_type in token_type_to_tag:
			textbox.tag_add(
				token_type_to_tag [token_type],
				get_text_coord(s, i),
				get_text_coord(s, j)
				)
	textbox.edit_modified (0)

def delete_tokens(textbox):

	for tag in textbox.tag_names ():
		textbox.tag_remove (tag, 1.0, 'end')

def open(extension,
	err_syntax, syntax,
	textbox, p_syntax):
	if extension == '.py' or extension == '.pyw':
		syntax='py'
		if err_syntax!=True:tokens_get(textbox,PythonLexer())
		p_syntax['text']='python'
	elif extension=='.js':
		syntax='js'
		tokens_get(textbox,JavascriptLexer())
		p_syntax['text']='javascript'
	elif extension=='.c':
		syntax='c'
		tokens_get(textbox,CLexer())
		p_syntax['text']='c lang'
	elif extension=='.cpp':
		syntax='cpp'
		tokens_get(textbox,CppLexer())
		p_syntax['text']='c++ lang'
	elif extension=='.html':
		syntax='html'
		tokens_get(textbox,HtmlLexer())
		p_syntax['text']='html'
	elif extension=='.css':
		syntax='css'
		tokens_get(textbox,CssLexer())
		p_syntax['text']='css'
	elif extension=='.json':
		syntax='json'
		tokens_get(textbox,JsonLexer())
		p_syntax['text']='json'
	elif extension == 'md':
		syntax = 'md'
		tokens_get (textbox, MarkdownLexer ())
		p_syntax ['text'] = 'markdown'
def edit_event(err_syntax,syntax,textbox,switched):
	if err_syntax!=True and switched==False:
			if syntax=='py':
				tokens_get(textbox,PythonLexer())
			elif syntax=='js':
				tokens_get(textbox,JavascriptLexer())
			elif syntax=='c':
				tokens_get(textbox,CLexer())
			elif syntax=='cpp':
				tokens_get(textbox,CppLexer())
			elif syntax=='html':
				tokens_get(textbox,HtmlLexer())
			elif syntax=='css':
				tokens_get(textbox,CssLexer())
			elif syntax=='json':
				tokens_get(textbox,JsonLexer())
			elif syntax == 'md':
				tokens_get (textbox, MarkdownLexer ())
def switch(extension,syntax,textbox,p_syntax,switched):
	if syntax!='text':
		syntax='text'
		p_syntax['text']='plain text'
		delete_tokens(textbox)
		switched=True
	elif switched==True:
		if extension=='.py':
			syntax='py'
			p_syntax['text']='python'
			tokens_get(textbox,PythonLexer())
			switched=False
		elif extension=='.c':
			syntax='c'
			p_syntax['text']='c lang'
			tokens_get(textbox,CLexer())
			switched=False
		elif extension == '.cpp':
			syntax = 'cpp'
			p_syntax ['text'] = 'c++ lang'
			tokens_get (textbox, CppLexer ())
			switched = False
		elif extension == '.json':
			syntax = 'json'
			p_syntax ['text'] = 'json'
			tokens_get (textbox, JsonLexer ())
			switched = False
		elif extension == '.html':
			syntax = 'html'
			p_syntax ['text'] = 'html'
			tokens_get (textbox, HtmlLexer ())
			switched = False
		elif extension == '.css':
			syntax = 'css'
			p_syntax ['text'] = 'css'
			tokens_get (textbox, CssLexer ())
			switched = False
		elif extension == '.js':
			syntax = 'js'
			p_syntax ['text'] = 'javascript'
			tokens_get (textbox, JavascriptLexer ())
			switched = False
		elif extension == '.md':
			syntax = 'md'
			p_syntax ['text'] = 'markdown'
			tokens_get(textbox, MarkdownLexer ())

def sset (name, syntax, p_syntax, textbox):

	p_syntax ['text'] = name

	if name == 'plain text': delete_tokens(textbox)
	elif name == 'python': tokens_get (textbox, PythonLexer ())
	elif name == 'c lang': tokens_get (textbox, CLexer ())
	elif name == 'c++ lang': tokens_get (textbox, CppLexer ())
	elif name == 'json': tokens_get (textbox, JsonLexer ())
	elif name == 'html': tokens_get (textbox, HtmlLexer ())
	elif name == 'css': tokens_get (textbox, CssLexer ())
	elif name == 'javascript': tokens_get (textbox, JavascriptLexer ())
	elif name == 'markdown': tokens_get(textbox, MarkdownLexer ())