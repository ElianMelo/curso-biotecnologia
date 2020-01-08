# -*- coding: utf-8 -*-

import re

loremIpsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Maecenas id varius enim. Nunc sollicitudin lacus eu eros sagittis eleifend in quis nunc.
In egestas dapibus mollis. 
Vivamus euismod, leo non cursus molestie, lacus purus aliquam neque, nec fermentum magna felis tristique nunc. 
Phasellus vehicula malesuada ex, vel pretium quam vehicula sed. 
Suspendisse hendrerit consectetur gravida. 
Sed mattis quis tortor dapibus bibendum. Proin et euismod massa. 
Donec ullamcorper in arcu vel sollicitudin. 
Donec sit amet ex leo. Donec vestibulum ante id faucibus feugiat. 
Etiam luctus leo sem, id imperdiet ante facilisis quis.
Curabitur pharetra placerat tempus. Nulla erat nunc, lobortis at ullamcorper ac, rutrum eu ante. 
Etiam cursus eu est id lacinia.
"""

palavrasC = re.findall("[^ ]*[q][^ |\.]*", loremIpsum)

print(palavrasC)
