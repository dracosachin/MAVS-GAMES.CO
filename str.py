s=raw_input("Enter strign")
c="  ".join(c for c in s if c not in "!()_[]{};:\"\"\,<>./?''@#$%^&*-~")
print c