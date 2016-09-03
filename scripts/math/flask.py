#!/usr/bin/env python

import pygal

gm = pygal.Line()
gm.title = '% Type of electric cars used per year.'
gm.x_labels = ['2000', '2001', '2002', '2003', '2004']
gm.add('Nissan', [45, 90, 100, 66, 71])
gm.add('Toyota', [1, 25, 35, 45, 30])

gm.render_to_file('flask.svg')
