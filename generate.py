import pyperclip as clip


def main():
    #while True:
        #clip.copy(genetrate())
    clip.copy(tag_list())


def genetrate():
    tag = input("Tag name: ")
    output = f"""
                    <tr>
                        <td>
                            &lt{tag}&gt&lt/{tag}&gt
                        </td>
                        <td>
                            {tag} usage info here
                        </td>
                        <td>
                            <{tag}>example</{tag}>
                        </td>
                    </tr>"""
    return output


def tag_list():
    rez = ''
    while True:
        tag = input('Add tag name to list: ')
        if tag == 'quit':
            break
        rez += f'&lt{tag}&gt, '

    return rez[:-2]


if __name__ == "__main__":
    main()
