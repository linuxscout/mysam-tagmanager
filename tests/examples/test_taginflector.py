import mysam.taginflector

def main():
    inflector = mysam.taginflector.tagInflector()
    word = "يَسْتَعْمِلُونَهَا"
    tagcode = 'V-1;M3H-faU;W-H'
    print(inflector.inflect(tagcode))

if __name__ == "__main__":
    main()
