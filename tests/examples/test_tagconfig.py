import pandas as pd
import mysam.tagconfig as tagconfig
import mysam.tag_const as tag_const

def main():
    configuer = tagconfig.tagConfig()
    configuer.load_config()
    df = pd.DataFrame(configuer.tagsdict)
    print('****tagdict ****')
    print(df)

if __name__ == "__main__":
    main()
