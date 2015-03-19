#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import WikiPage

names = {}

for root, dirs, filenames in os.walk('../slegwiki/'):
	for f in [x for x in filenames if x.endswith('.md') and x != 'Home.md']:
		print('--------------%s-------------' % f)
		p = WikiPage.WikiPage('../slegwiki/%s' % f)
		p.validate()
		# q = open('newiki/%s' % f, 'w')
		# q.write(str(p))
		# q.close()
		# 
		for lang in p.getLanguages():
			if lang not in names.keys():
				names[lang] = []
			for name in p.getNames(lang):
				if name not in names[lang]:
					names[lang].append(name)
				try:
					f = open('../slebok/sleg/%s.html' % name, 'w', encoding="utf-8")
					f.write(p.getHtml(name).replace('../slegwiki/', 'wiki/'))
					f.close()
				except IOError:
					print(' !!! "%s" cannot be accessed' % name)

#
f = open('../slebok/sleg/index.html', 'w', encoding="utf-8")
f.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:xhtml="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
	<meta name="keywords" content="software linguistics, software language engineering, book of knowledge, glossary"/>
	<title>SLEBOK — SLEG</title>
	<link href="../www/sleg.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="left">
	<a href="index.html"><img src="../www/sleg.200.png" alt="Software Language Engineering Glossary (SLEG)" class="pad"/></a><br/>
	<a href="http://creativecommons.org/licenses/by-sa/4.0/" title="CC-BY-SA"><img src="../www/cc-by-sa.png" alt="CC-BY-SA"/></a><br/>
	<a href="http://creativecommons.org/licenses/by-sa/4.0/" title="Open Knowledge"><img src="../www/open-knowledge.png" alt="Open Knowledge" class="pad" /></a><br/>
	<a href="http://validator.w3.org/check/referer" title="XHTML 1.0 W3C Rec"><img src="../www/xhtml.88.png" alt="XHTML 1.0 W3C Rec" /></a><br/>
	<a href="http://jigsaw.w3.org/css-validator/check/referer" title="CSS 2.1 W3C CanRec"><img src="../www/css.88.png" alt="CSS 2.1 W3C CanRec" class="pad" /></a><br/>
	<div>[<a href="mailto:vadim@grammarware.net">Complain!</a>]</div>
</div>
<div class="main">
	<h1>SLEG is a work in progress!</h1>
	<h2>Unordered list of all possible pages</h2>• ''')
for l in WikiPage.languages:
	if l in names:
		f.write('<a href="#%s">%s</a> • ' % (l, l))
for i in range(len(WikiPage.languages)):
	if WikiPage.languages[i] not in names:
		continue
	s = '<hr/><h3>'
	if WikiPage.flags[i]:
		s += '<img src="../www/%s.png" alt="%s"/>' % (WikiPage.flags[i], WikiPage.languages[i])
	s += '<a name="{0}"/>{0}</h3>\n<div class="mult">\n'.format(WikiPage.languages[i])
	for name in sorted(names[WikiPage.languages[i]]):
		s += '<a href="{0}.html">{0}</a><br/>\n'.format(name)
	f.write(s+'</div>')
f.write('''</div><div style="clear:both"/><hr />
	<div class="last">
		<em>
			<a href="http://github.com/grammarware/sleg">Software Language Engineering Glossary</a> (SLEG) is
			created and maintained by <a href="http://grammarware.net">Dr. Vadim Zaytsev</a>.<br/>
			Hosted as a part of <a href="http://slebok.github.io/">SLEBOK</a> on <a href="http://www.github.com/">GitHub</a>.
		</em>
	</div></body></html>''')
f.close()
