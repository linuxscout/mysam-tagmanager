import mysam.taginflector

def main():
    tag_maker = mysam.taginflector.tagInflector()
    word = "يَسْتَعْمِلُونَهَا"
    tagcode = 'V-1;M3H-faU;W-H'
    print(tag_maker.inflect(tagcode))

if __name__ == "__main__":
    main()
