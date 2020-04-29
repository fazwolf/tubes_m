def plot_rdw(n_terinfeksi):
  i=0
  while n_terinfeksi > 0:
      terinfeksi = 0 
      sembuh = 0
      x_pos.append([])
      y_pos.append([])
      
      for j in range(n_individu):

          if (status_kesehatan[j] == 1):
              if (waktu_infeksi[j] <= t_sembuh):
                waktu_infeksi[j] +=1
              elif (waktu_infeksi[j] > t_sembuh):
                sembuh += 1
                imun[j] = 1
                status_kesehatan[j] = 0
                n_terinfeksi -= 1

                x_sembuh.append(x_pos[i][j])
                y_sembuh.append(y_pos[i][j])
                i_sembuh.append(j)

                temp = i_terinfeksi.index(j)

                # Delete Arr
                del i_terinfeksi[temp]
                del x_terinfeksi[temp]
                del y_terinfeksi[temp]

          # Posisi Sebelum
          curr_xpos = x_pos[i][j]
          curr_ypos = y_pos[i][j]

          # Update Posisi
          rand = np.random.rand(1,1)
          move = np.random.rand(1,1)
          
          # Probabilitas Individu Bergerak
          if(move > p): 
            x_pos[i+1].append(curr_xpos)
            y_pos[i+1].append(curr_ypos)
          else: 
            # Gerak Ke Kanan
            if rand <= 0.25:
                if x_max <= curr_xpos:
                    x_pos[i+1].append(curr_xpos-x_range)
                    y_pos[i+1].append(curr_ypos)
                else:
                    x_pos[i+1].append(curr_xpos+1)
                    y_pos[i+1].append(curr_ypos)
            # Gerak Ke Bawah       
            elif rand <= 0.50:
                if y_min >= curr_ypos:
                    y_pos[i+1].append(curr_ypos+y_range)
                    x_pos[i+1].append(curr_xpos)
                else:
                    y_pos[i+1].append(curr_ypos-1)
                    x_pos[i+1].append(curr_xpos)
            # Gerak Ke Kiri
            elif rand <= 0.75:
                if x_min >= curr_xpos:
                    x_pos[i+1].append(curr_xpos+x_range)
                    y_pos[i+1].append(curr_ypos)
                else:
                    x_pos[i+1].append(curr_xpos-1)
                    y_pos[i+1].append(curr_ypos)
            # Gerak Ke Atas
            else:
                if y_max <= curr_ypos:
                    y_pos[i+1].append(curr_ypos-y_range)
                    x_pos[i+1].append(curr_xpos)
                else:
                    y_pos[i+1].append(curr_ypos+1)
                    x_pos[i+1].append(curr_xpos)

          # Posisi Sehat
          for k in i_sehat: 
            if (k == j):
                temp = i_sehat.index(k)
                x_sehat[temp] = x_pos[i][temp]
                y_sehat[temp] = y_pos[i][temp]
          # Posisi Terinfeksi
          for k in i_terinfeksi: 
            if (k == j):
                temp = i_terinfeksi.index(k)
                x_terinfeksi[temp] = x_pos[i][temp]
                y_terinfeksi[temp] = y_pos[i][temp]
            # Update Terinfeksi 
            if ((x_pos[i][k] == x_pos[i][j]) and (y_pos[i][k] == y_pos[i][j]) 
            and (j != k) and (i_terinfeksi[-1] < j)):
                x_terinfeksi.append(x_pos[i][j])
                y_terinfeksi.append(y_pos[i][j])
                i_terinfeksi.append(j)
                temp = i_sehat.index(j)
                # Delete Arr
                del i_sehat[temp]
                del x_sehat[temp]
                del y_sehat[temp]
                status_kesehatan[j] = 1
                n_terinfeksi+=1
                terinfeksi +=1
          # Posisi Sembuh
          for k in i_sembuh: 
            if (k == j):
                temp = i_sembuh.index(k)
                x_sembuh[temp] = x_pos[i][temp]
                y_sembuh[temp] = y_pos[i][temp]
      i+=1

      hari = i
      gen_img(x_sehat, x_terinfeksi, x_sembuh, y_sehat, y_terinfeksi, y_sembuh, 
            n_terinfeksi, len(i_sembuh), sembuh, terinfeksi, i+1)
      
  return hari
