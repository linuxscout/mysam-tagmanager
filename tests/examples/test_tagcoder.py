import mysam.tagcoder

def main():
    taglists = [
        ['اسم', 'هاء', 'مجرور'],
        'تعريف::مرفوع:متحرك:ينون:::'.split(":"),
    ]
    tgcoder = mysam.tagcoder.tagCoder()
    for taglist in taglists:
        tagcode = tgcoder.encode(taglist)
        print("tags list:", ";".join(taglist))
        print("tagcode:", tagcode)
        print("decode:", tgcoder.decode(tagcode))

    # مثال add_tag
    tagcode = 'V-0;M1H-faU;W--'
    tag = "ضمير متصل"
    print("add_tag:", mysam.tagcoder.tagCoder().add_tag(tag, tagcode))

    # مثال remove_tag
    print("remove_tag:", mysam.tagcoder.tagCoder().remove_tag(tag, tagcode))

    # مثال has_tag
    tags = ['اسم', 'مجرور', 'مذكر', "مفرد", "واو"]
    tagcode = tgcoder.encode(tags)
    print("has_tag(مجرور):", tgcoder.has_tag("مجرور", tagcode))
    print("has_tag(فعل):", tgcoder.has_tag("فعل", tagcode))

if __name__ == "__main__":
    main()
