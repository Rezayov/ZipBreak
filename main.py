import zipfile
import argparse


class Target:
    def __init__(self):
        self.location = ""
        self.length = 0
        self.passkey = ""

    def adding_inputs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--filename", default="Target.zip")
        parser.add_argument("--lenght", type=int)
        arguments = parser.parse_args()
        self.location = arguments.filename
        self.lenght = arguments.lenght

    def cracker(self):
        MainPass = list("0123456789")
        Indexes = [0] * self.lenght
        PassNumbers = len(MainPass) ** self.lenght
        with zipfile.ZipFile(self.location) as Target_File:
            for i in range(PassNumbers - 1):
                TempPass = ""
                for j in range(self.lenght):
                    TempPass += MainPass[Indexes[j]]
                print("Trying password: ", TempPass, end="")
                try:
                    with Target_File.open(
                        Target_File.namelist()[0], pwd=TempPass.encode()
                    ) as f:
                        f.read(1)
                        print("Password Cracked", TempPass)
                        self.passkey = TempPass
                        return 0
                except:
                    print("\033[1;31m" + "        Failed" + "\033[0m")
                    Indexes[0] += 1
                    for j in range(self.lenght):
                        if Indexes[j] >= len(MainPass):
                            Indexes[j + 1] += 1
                            Indexes[j] = 0
        print("Could not find your password")

        return 0

        # TODO:-> Save the progress for resuming project


if __name__ == "__main__":
    t = Target()
    t.adding_inputs()
    t.cracker()
