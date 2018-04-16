peta =  {'A':set(['B','C']),
         'B':set(['A','C','D','E']),
         'C':set(['B','A','D']),
         'D':set(['B','C']),
		 'E':set(['B']),
         }
def dfs(graf, mulai, final):
    stack = [[mulai]]
    visited = set()

    while stack:
        #hitung panjang sstack dan masukkan ke variabel panjang_stack
        panjang_stack = len(stack)-1
        
        # masukkan tumpukan ke var rute
        rute =  stack.pop(panjang_stack)

        # simpan node yang dipilih ke variabel state
        state = rute[-1]
		# cek state apakah == final, jika ya maka return rute
        if state == final:
            return rute
        # jika state tidak == final, maka cek state ada di visited atau tidak
        elif state not in visited:
            # jika state tidak == visited cek cabang state
            for cabang in graf.get(state, []): #cek semua cabang dari state
                rute_baru = list(rute) #masukkan variabel jalur ke variabel rute_baru
                rute.append(cabang) #tambah isi rute_baru dengan cabang
                stack.append(rute_baru) #tambah stack dengan rute_baru

            # tandai state yang sudah dikunjungi
            visited.add(state)


        #cek isi tumpukan
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")

print(dfs(peta,'A','E'))
