# "gravity works diffrrent in zortan we have to calculate the weight
# zortanweight =(Earth Weight +32)/8"

def zortan_weight(weight:float):
    return (weight+32)/8

def main():
    print(f"zortan weight{zortan_weight(10):.2f}")

main()  
