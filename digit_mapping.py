str=input('enter the number')
digi_map={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four'
}
for ch in str:
    print(digi_map.get(ch))
