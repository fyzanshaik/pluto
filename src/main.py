from textnode import TextNode,TextType

def main():
    testNode = TextNode("This is some anchor text", TextType.LINK , "https://github.com/fyzanshaik")
    print(testNode)
    

if __name__ == "__main__":
    main()