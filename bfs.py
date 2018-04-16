peta =  {'A':set(['B','C']),
         'B':set(['A','C','D','E']),
         'C':set(['B','A','D']),
         'D':set(['B','C']),
		 'E':set(['B']),
         }
def bfs(graf, mulai, final):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian 
        rute = queue.pop(0)
		# simpan node ke variabel state
        state = rute[-1]

        # cek state apakah == final, jika tdk kembali ke rute
        if state == final:
            return rute
        # jika state tdk == final ,cek state ada atau tdk di variable visited
        elif state not in visited:
            # jika tidak ada di visited , cek cabang state
            for cabang in graf.get(state, []): #cek semua cabang
                rute_baru = list(rute) #masukkan isi dari variabel jalur ke variabel jalur_baru
                rute_baru.append(cabang) #tambah isi jalur_baru dengan cabang
                queue.append(rute_baru) #tambah antrian dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

print(bfs(peta,'A','E'))
