from collections import Counter


def packet(data):

    lis = []
    lis[:0] = data

    for i in range(len(lis)):
        temp = lis[i:i+14]
        count = Counter(temp)
        count = count.values()
        yes = 0
        for c in count:
            if c == 1:
                yes += 1
                if yes == 14:
                    print(i)
                    print(i + 14)
                    return

string = 'cbhbmmqnmmqvqfqgqcqmmtvvvdsvscvssmfmhfmhhgdgcclhlnnvmnvmnnwngnqggqlqhhbqbfbvffcpfcfpcpmcppsgssvcvmmdwmwsmwswnwvnvvtgvgfgqqnlltgllpplhpllrnrwrtrzrlrzllpnlpnplnlwnnzfztzcchczctcbbpwpbbfhhqllgrllnnghnnlnznzzlqqmggqbgbjjlnlnjllwlnwnjnbjnnhhcddgmdmqmllfjllddmgmpggtvvqqwmmhcmmjpjdpdqqnhhqbhhscstsvttbwtwdtwwjffvccrwrvvnqqtwwhgwhwthwthhvshsfsjstshthqqdfdhdqhqrqggfffvhffhbbwtbtvtwvvwgvvjjjvtjvvlmlmtmztmthmhttjwwmqqjffhvhqvvrddbsbfbgffmcfffqqfzzgmggzvggbjjmccftcftfnttqqjzjdzdrrgvgsgvvlqvlqqlplnnjccjqcjcgjgfjgjlgjjzhhjbbbfdbfddgccncppsbbjjsttcqtqgqpqllqggtsthhtvvtrttbthtnhhddvnnbggmtggcsgcscmmvmllttjbjggbzbttrfttgsstwtftdthdththbttcggdldtdlttbvvpgpjpwpwvwcwjwsjsttznztzftzzjpzzrtzrztrrtsrrdtrdtdbdhhdgdwwnjnnvjvsjjrwjjvrrzvrvllrgghgbbgbsssslqlrllbjbttzfztzpzzvtvccszsddtqttjllqgqgpqphptpwttwtmtltljjfnnzwzmzlzssghssqhhphbhfftwwqmwmzzqtzqzqrrndrrmrqrzrszzrcrbccglgcgwgrgdggtvtpptgtfgflglgrrnvrvhrrhlrhhfchfhdhzzwggvbbgfgrrpdrdccfllqflfmlfmlmbbhnbbsblbzbgbqqjppcddcvvsddjfjjlnnwbbflfzzmlmddjssjffcqffwdfdqqphpnhppbttjfjzzdvdjvvddnfffmjfmfmpfmmmdlmlrrhqqcpcmclmmbmppzczjjmlltqlqzzqgqcggdmdzznnnnsjjvbjjwbwhbhfhvvtmmsfmmcgmcmwcwhwnhhpccmbmdbmbgbjbggqqccfllfqqmqwwzbblffthhdnncqnccqppldlpldpllzmmsqqdffnggqlqtllwlglnlnhlhflfssvzzrllbtbnbgnnfvfllwslszswsnnpwwppvspsmmnfnpffrmrhmmctttrjrbjrjpjtpjpssdwdtwtmmtgtsgttlwttfrfvvpjpcjccmtthhldhllzslshhnrnvvfddnllltclcrrhnnjwwwpfpddmtmsmfflslrlmlmwmllgfgmfgmmjttpcpspslsjspsqstqsqqpsprphrrpqqfzqqwcwcddsjjpvvfnfvnnnrncnwcwczzcwzwnwmwffbdfbdfdjjhrhvhhvwvsvhshnhwwzlwlnnphhtjjmljjqzjjsjgsjshhwjjmttvgvsgstggrcrmmrqrhrqrzrmzmggqvqtqgtqqqqltqqwggmmzggjccgmgwgqqmnqnrnprptrrvfrvffnmnfmmnnnwzzldlvlgvlvqqpnphpgglhlshlhzzpcptpssblqvdbpbbcrngctqgptccwpdcpbcjwdmcrzmhwffgzqmmqwpqvplwzmjlzmvmzmbtqjnhzrpppnpntvmjbzmvhjvbgflmmjnwssvqvbnbddfcwqdtvpvddctmpptcjmvwszhbsttcbjlfjvwlljhlqlvvsnzphdjhfswltdhzprltzcszrgcmnmfznmbccstjvjngwpbsfqssfwvpdhhmlmzttzlszsgpvvbcfvzrlsttlqpnqhwtbqfjnbztnwfnhlhfltgdtsrrwrfhlssvsgzpffnnrhgcvclqnjgfhhzswllvcjffpngcmtjphwnbdfrrgjfrfqbnvbwgccsjvvmjgcvqvtggnvgvgnnchbblqnvvdgjtvdmfrzvhvhzcbqzdslphjjqtcwjqptstvvpqgdbgbcmmchjpvjhvbwtlmlnqpldfcbmwvrmpqcsfdhmmwnbvmpglcfbnsgjmljcwpzpwffcqfrbdrztzhqzhzpcrjfdmrctttdrzlmzcqwjftngwjmgqscftnpbjwqrcvqwbwbdhbhvrdcvgrvctjgwjtmdgzwgvdbmsrjpsbhwcqlqzjnzmgpctlwqhfnbmgsprjcqtfjjvzljqpfqgnvrgnjjlmpqgnzpmpsvzjmtvnfgslldjtjdwlzrvqrbvcpspzpcdnpdjmhcdhsbmthmgjqchqwwsnfjnwgpctlwcdpqpmzqcrptscngqnmhzwjdcqwvdmlzntsfbstbtmmnlsspjbjjdspnslgcnlbfnbhjlzjhrrmdbbwtswqpbpwtzhcnldbsfrvndzvcgzjprcrclhfwbvzgthcglfzqrshgtvbflvnznhmlzdtfnrsltnnppqgrtndbsfqmftdnzmqfwdpcrmssldmrrnzchnqpflgbqzqjjrzlfnptqdwzdhmctfbztmfcmbqcwjmgnwgqzqjctphrrthgvpvppztvpzgzhdszfhlzlcnwmfrlsnvftfrlfvbnlwzctphhpfvszntqcvnfmvmwwhsjlnpfhcpjvrncgmsbprwwllvnsbjfhtbtmcvvpzcvqrrqdvgzvllvcvnvvbftngqcqcvvbsqfshmnhwptcsbsnjzltqzmflftrhblqszrzsbfcpgzncvwhlqlcbmgjdpfcmlgdfphsfcgqccthmlzjbdwpsbddwwrtwmsvqwbzwhzmghhrspvbptznqsqvhgnhlwqjnhgnzprrtjddwtqfsshjrvlglhdlstghftmllvzmmfglnscnrtgcwwwzjphzhvqlctdwjlqvbsvlgzrdpvjhhcthgjhlwsgfzlschhfprfcrzfrzmnlwvqsnqlllczwfhswchrlggqszwrvpldrffnzrffbhtfbslgcdrqpjcrbqsrgfrhttcptncfndcbsdbjsqjvgbmnmhlnbltdcgbmllpgjmgljvglrwmrvgthhhzrsmzvgwcfgvcsbzpjcqnhrzhznzjcjghhwqvllrmsvlpzlssrdsqwvzvqwsvfsjqvbgrfbmfzlchqsjgncbljtvzsfdnvmfzcbrlnnvvmjbmgjmqzjtdzpljdwqtvwsrlbslwfvlgbtnmlpcwmngncnmdhqctshmjmnhpqcqzhvlbvgptctrvggdgnpnrlnngrfhsqdfthvcnpwjfjnslcqlfrfvhnctmsqgnqmgpwtlzhtdqhqqrcllzjccnszsqvrzhcffvnfnstgdmljdrqrndljdnfbbjvmpqdnqhtdlnzcvnfjlvzmfzrndhtglvngmbrdbpbnhvfmrbcwqzttnjplgrhchjtfjwfbjfbmzlrnllhzccpfhfhnjpfvzlpbqnhwmpssvwtzhdbtnbtllhpfdcqjjnzgbdrfjjbcltnzdrmtmsmvpjtmdnqszgbqncsvhjbgwswhmghpvstrqbglgrtgbchttbznvvdhppzwnttpgcbdjdhlsqhhtlphjjrjncrmfdtjhdwmjgmpngnbptzwgwdztmhtpglnftwpnnmrmcwfhwnhlsbwsrjnlmdlmffbzsnhsvnbldwtrrhdhfsjdrsnzlgtfzcwwqrfhtrmjhmphqndwtbpczvmfgczmdlqjqdlwmvjjzwmqnpvwzmtjwtprlnbvjdhpjgndrwzcfthnwhnhqpwtcjlhrhdplzsncfmszmhjmgljhnlsrrfwplclcvjjqmtpnwbtsbwdnjdlqntvdnfgwbpwspssprbffjdlcvbwcqlttnwnhwdspfsjhppbhspnrvrsfmzvbwwtjfzmnzwgqddbmcjzzqhqlgrglsvgsjdwlnsbtmqgsnfwwqrjsbcgdlmbgqwvgpqllqwbcplfjrgnzsdtdtvqnrbcrqjhdtqqplvszvtlflgbpwnpzczbvhzfjrslcwcswsgfvvsswzzwhtfjfpsrvcfnrs'


packet(string)