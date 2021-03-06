def runlen_encode(img):
    c_img = img.reshape(580*420, order='F')
    runs = []
    npixels = len(c_img)
    run_start = 1
    run_length = 0
    for i in range(npixels):
        c = c_img[i]
        if c == 0:
            if run_length != 0:
                runs.append((run_start + 1, run_length))
                run_length = 0
        else:
            if run_length == 0:
                run_start = i
            run_length += 1
    if run_length != 0:
        runs.append((run_start + 1, run_length))
    return runs