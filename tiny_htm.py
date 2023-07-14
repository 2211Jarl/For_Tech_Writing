from tinyhtml import html, h, frag, raw

#to generate HTML code
htm=html(lang="en")(
    h("head")(
        h("meta", charset='utf-8')
    ),
).render()

print("HTML Code: \n", htm)

#how frag() works
htm_frag=html(lang="en")(
    frag(h("h1")("This is a sample header"), 
         h("p")("This is a sample paragraph declared under the head in HTML"))
).render()
print("\n\nThis is an use case of frag()\n", htm_frag)

#how raw() works
htm_raw=raw('<h1>Printing the Raw HTML code</h1>')
print("\n\nThe raw way of printing HTML code: \n", htm_raw)