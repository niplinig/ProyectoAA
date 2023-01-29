import json
import sys

original_stdout = sys.stdout

# Dicionario ordenado
dic = {
 0: {
  "a": [],
  0: {
   "a": [],
   0: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   },
   1: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   }
  },
  1: {
   "a": [],
   0: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   },
   1: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   }
  }
 },
 1: {
  "a": [],
  0: {
   "a": [],
   0: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   },
   1: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   }
  },
  1: {
   "a": [],
   0: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   },
   1: {
    "a": [],
    0: {
     "a": [],
    },
    1: {
     "a": [],
    }
   }
  }
 }
}

def ended():

	with open('result.txt', 'w') as f:

		sys.stdout = f
		
		if (len(dic[0]["a"]) > 1):
	
				print("25%")
	
				print(dic[0]["a"])
	
				if (len(dic[0][0]["a"]) > 1):
	
						print("50%")
	
						print(dic[0][0]["a"])
	
						if (len(dic[0][0][0]["a"]) > 1):
	
								print("75%")
	
								print(dic[0][0][0]["a"])
	
								if (len(dic[0][0][0][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][0][0][0]["a"])
	
								if (len(dic[0][0][0][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][0][0][1]["a"])
	
						if (len(dic[0][0][1]["a"]) > 1):
	
								print("75%")
	
								print(dic[0][0][1]["a"])
	
								if (len(dic[0][0][1][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][0][1][0]["a"])
	
								if (len(dic[0][0][1][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][0][1][1]["a"])
	
				if (len(dic[0][1]["a"]) > 1):
	
						print("50%")
	
						print(dic[0][1]["a"])
	
						if (len(dic[0][1][0]["a"]) > 1):
	
								print("75%")
	
								print(dic[0][1][0]["a"])
	
								if (len(dic[0][1][0][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][1][0][0]["a"])
	
								if (len(dic[0][1][0][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][1][0][1]["a"])
	
						if (len(dic[0][1][1]["a"]) > 1):
	
								print("75%")
	
								print(dic[0][1][1]["a"])
	
								if (len(dic[0][1][1][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][1][1][0]["a"])
	
								if (len(dic[0][1][1][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[0][1][1][1]["a"])
	
		if (len(dic[1]["a"]) > 1):
	
				print("25%")
	
				print(dic[1]["a"])
	
				if (len(dic[1][0]["a"]) > 1):
	
						print("50%")
	
						print(dic[1][0]["a"])
	
						if (len(dic[1][0][0]["a"]) > 1):
	
								print("75%")
	
								print(dic[1][0][0]["a"])
	
								if (len(dic[1][0][0][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][0][0][0]["a"])
	
								if (len(dic[1][0][0][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][0][0][1]["a"])
	
						if (len(dic[1][0][1]["a"]) > 1):
	
								print("75%")
	
								print(dic[1][0][1]["a"])
	
								if (len(dic[1][0][1][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][0][1][0]["a"])
	
								if (len(dic[1][0][1][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][0][1][1]["a"])
	
				if (len(dic[1][1]["a"]) > 1):
	
						print(dic[1][1]["a"])
	
						if (len(dic[1][1][0]["a"]) > 1):
	
								print("75%")
	
								print(dic[1][1][0]["a"])
	
								if (len(dic[1][1][0][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][1][0][0]["a"])
	
								if (len(dic[1][1][0][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][1][0][1]["a"])
	
						if (len(dic[1][1][1]["a"]) > 1):
	
								print("75%")
	
								print(dic[1][1][1]["a"])
	
								if (len(dic[1][1][1][0]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][1][1][0]["a"])
	
								if (len(dic[1][1][1][1]["a"]) > 1):
	
										print("100%")
	
										print(dic[1][1][1][1]["a"])
									
		sys.stdout = original_stdout
	
def main():

	# Opening JSON file
	f = open("dataTest.json", "r")

	# read_content = file1.read()

	data = json.load(f)

	while (len(data) > 0):

		i = data.pop()
		
		id = i["ID"]
		array = i["points"]
		longitud = len(i["points"])
		inicio = 0
		fin = longitud - 1
		mitad = round(longitud / 2)
		inicio_mitad = round(mitad / 2)
		mitad_fin = mitad + round(mitad / 2)

		I_IM = round((array[inicio_mitad]["y"] - array[inicio]["y"]) /
		             (array[inicio_mitad]["x"] - array[inicio]["x"]))
		IM_F = round((array[fin]["y"] - array[inicio_mitad]["y"]) /
		             (array[fin]["x"] - array[inicio_mitad]["x"]))
		MF_F = round((array[fin]["y"] - array[mitad_fin]["y"]) /
		             (array[fin]["x"] - array[mitad_fin]["x"]))
		I_MF = round((array[mitad_fin]["y"] - array[inicio]["y"]) /
		             (array[inicio_mitad]["x"] - array[inicio]["x"]))

		if I_IM >= 0:

			dic[0]["a"].append(id)

			if IM_F >= 0:

				dic[0][0]["a"].append(id)

				if MF_F >= 0:

					dic[0][0][0]["a"].append(id)

					if I_MF >= 0:

						dic[0][0][0][0]["a"].append(id)

					else:

						dic[0][0][0][1]["a"].append(id)

				else:

					dic[0][0][1]["a"].append(id)

					if I_MF >= 0:

						dic[0][0][1][0]["a"].append(id)

					else:

						dic[0][0][1][1]["a"].append(id)

			else:

				dic[0][1]["a"].append(id)

				if MF_F >= 0:

					dic[0][1][0]["a"].append(id)

					if I_MF >= 0:

						dic[0][1][0][0]["a"].append(id)

					else:

						dic[0][1][0][1]["a"].append(id)

				else:

					dic[0][1][1]["a"].append(id)

					if I_MF >= 0:

						dic[0][1][1][0]["a"].append(id)

					else:

						dic[0][1][1][1]["a"].append(id)
		else:

			dic[1]["a"].append(id)

			if IM_F >= 0:

				dic[1][0]["a"].append(id)

				if MF_F >= 0:

					dic[1][0][0]["a"].append(id)

					if I_MF >= 0:

						dic[1][0][0][0]["a"].append(id)

					else:

						dic[1][0][0][1]["a"].append(id)

				else:

					dic[1][0][1]["a"].append(id)

					if I_MF >= 0:

						dic[1][0][1][0]["a"].append(id)

					else:

						dic[1][0][1][1]["a"].append(id)

			else:

				dic[1][1]["a"].append(id)

				if MF_F >= 0:

					dic[1][1][0]["a"].append(id)

					if I_MF >= 0:

						dic[1][1][0][0]["a"].append(id)

					else:

						dic[1][1][0][1]["a"].append(id)

				else:

					dic[1][1][1]["a"].append(id)

					if I_MF >= 0:

						dic[1][1][1][0]["a"].append(id)

					else:

						dic[1][1][1][1]["a"].append(id)

	f.close()


# Using the special varible
# __name__


if __name__ == "__main__":
	main()
	ended()
