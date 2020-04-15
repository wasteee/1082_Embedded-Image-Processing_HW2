# 1082_Embedded-Image-Processing_HW2

作業2 : 抓取人形 </p>

從學校首頁另存「等公車的影像」，將影像放到樹莓派裡面，對影像進行sobel或canny，調整參數，將人形的輪廓畫出來。比較哪種方法比較好? 差異在哪? </p>

# 結果 </p>

- 原始影像</p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW2/blob/master/image/gray.jpg)

- 執行結果 </p>
Canny 中的 threshold1 設定為 70 ，threshold2 設定為 210。 </p>
Sobel 中的 dx , dy 設定為 1。 </p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW2/blob/master/image/combine.jpg)
左邊為Canny，右邊為Sobel，經過比較後可發現，Canny處理過後的圖像有較少的灰階，整體圖案深淺保留較少，而至於人形邊緣的部分，使用兩種方式都可以有效的找出左1的人形外框，而右1和中間的人則因為背景樹木的關係，在頭部的部分較不明顯，整體而言 Sobel 在這兩者頭部的處理較好，但背景的干擾也較多。 </p>

- 修改測試 </p>
接下來試著先對原圖高斯模糊，kerenl 設定為 5x5，再使用 Sobel，效果如下圖  </p>
![image](https://github.com/wasteee/1082_Embedded-Image-Processing_HW2/blob/master/image/SobelandBlur.jpg)

可發現背景的樹木變得較為不明顯，且人型外框與背景的對比更為明顯一點，但對於中間的人頭部則沒有較明顯的改善。 </p>
