## adc-silenus-v5x.im4p

> `adc-silenus-v5x.im4p`

```diff

 
-  __TEXT.__text: 0xb638c0
-  __TEXT.__const: 0x832d10
-  __TEXT.__cstring: 0xa9d6f
+  __TEXT.__text: 0xb65740
+  __TEXT.__const: 0x832ed4
+  __TEXT.__cstring: 0xaa3c0
   __TEXT.text_env: 0x57888
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0xcf4
-  __DATA.__const: 0x61db0
+  __DATA.__const: 0x61ff8
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xfbd90
   __DATA._rtk_power: 0x3f8

   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5dab00
-  UUID: AFF881C3-09FC-331C-AE49-2671EB05AA71
-  Functions: 9753
+  UUID: EC166377-58D1-3BB3-9355-4C3998A84233
+  Functions: 9763
   Symbols:   0
-  CStrings:  18642
+  CStrings:  18677
 
CStrings:
+ "21:27:26"
+ "CH[%zu]: PDAF DISPARITY CAL FDR DATA INVALID: pdafDispCalValid=%d"
+ "CH[%zu]: PDAF DISPARITY CAL FDR DATA IS MISSING (sensor.pCal == nullptr)"
+ "GP processType=%d frame=%d, buffers=%ld ispClient=%#zx, no HWCfg"
+ "Kerns_PDX25_B0_v137_mode000_sifr60_pri_m0a_4224x3024_sec_m0a_4224x3024"
+ "Kerns_PDX25_B0_v137_mode004_sifr60_pri_m0a_4224x3024_sec_n0a_2112x1512"
+ "Kerns_PDX25_B0_v137_mode016_nonsifr240_pri_n1a_2112x1512_sec_skip"
+ "Kerns_PDX25_B0_v137_mode017_sifr60_pri_b0a_4224x3024_sec_b0a_4224x3024"
+ "Kerns_PDX25_B0_v137_mode019_sifr60_pri_b0a_4224x3024_sec_c0a_2112x1512"
+ "Kerns_PDX25_B0_v137_mode029_sifr15_pri_h0a_8448x6048_sec_h0a_8448x6048"
+ "Kerns_PDX25_B0_v137_mode102_nonsifr120_pri_m0a_4224x2376_sec_skip"
+ "Kerns_PDX25_B0_v137_mode116_nonsifr240_pri_n1a_2112x1188_sec_skip"
+ "Kerns_PDX25_B0_v137_mode504_sifr60_pri_m0a_4224x2640_sec_n0a_2112x1320"
+ "Kerns_PDX25_B0_v137_mode506_sifr60_pri_m0a_4224x2640_sec_n1a_2112x1320"
+ "Kerns_PDX25_B0_v137_mode519_sifr60_pri_b0a_4224x2640_sec_c0a_2112x1320"
+ "Kerns_PDX25_B0_v137_mode520_sifr60_pri_b0a_4224x2640_sec_c1a_2112x1320"
+ "Kerns_PDX25_B0_v137_mode550_sifr30_pri_h0a_4736x3360_sec_m0a_2368x1680"
+ "Kerns_PDX25_B0_v137_mode551_sifr30_pri_h0a_4736x2960_sec_m0a_2368x1480"
+ "Kerns_PDX25_B0_v137_mode650_sifr30_pri_h0a_4736x3360_sec_h0a_4736x3360"
+ "ManualAE ch:%d, acctime:%d %d"
+ "TM: CH %zu channel stopped\n"
+ "TM: Release buffer & stop TM timer channel %zu\n"
+ "TMH9: Non channel stop cleanup %zu\n"
+ "ZF:CH%zu SENSOR_CAL FP_BestFocusPosDac_CBAF=%d\n"
+ "ZF:CH%zu SENSOR_CAL FP_BestFocusPosDac_FP=%d\n"
+ "ZF:CH%zu SENSOR_CAL FP_DisparityChartDistance_cm=%.2f\n"
+ "ZF:CH%zu SENSOR_CAL FP_DisparityOffsetAtBestFocus_Localized_FP=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL FP_DisparityOffsetAtBestFocus_Localized_SPD=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL FP_DisparityPerUm=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL FP_FocusSweepTemp_NTC_C=%.2f\n"
+ "ZF:CH%zu SENSOR_CAL FP_LensPosPerDisparity_Localized=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_BestFocusPosDac_CBAF=%d\n"
+ "ZF:CH%zu SENSOR_CAL SPD_BestFocusPosDac_SPD=%d\n"
+ "ZF:CH%zu SENSOR_CAL SPD_DisparityChartDistance_cm=%.2f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_DisparityOffsetAtBestFocus_Localized_FP=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_DisparityOffsetAtBestFocus_Localized_SPD=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_DisparityPerUm=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_FocusSweepTemp_NTC_C=%.2f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_LensPosPerDisparity_Localized=%.6f\n"
+ "ZF:CH%zu SENSOR_CAL SPD_Override_By_FP=%d\n"
+ "ZF:CH%zu SENSOR_CAL is NULL\n"
+ "ZF:CH%zu SENSOR_CAL pdafDispCalValid=%d\n"
+ "[%s]Clean Timemachine... (not a full stop)\n"
+ "[%s]Stop Timemachine...\n"
+ "[%s]Timemachine Clean done! total %.2f ms\n"
+ "[%s]Timemachine Stop done! total %.2f ms\n"
+ "[DSI] All deferred flows should've been released"
+ "[DSI] PDE Shouldn't suspend during FID, %zu"
+ "[DSI] PDE suspend while FID wait for GMC, cnt=%zu"
+ "cmRoi: x=%f y=%f w=%f h=%f\n"
+ "configRect: x=%d y=%d w=%d h=%d\n"
+ "dx_readout = %f, dy_readout = %f\n"
+ "pBuff=%#zx frame %d %d, regId %d %d, step %d %d, pass %d %d"
+ "rdoutRightEdge =%f rdbotEdge=%f\n"
+ "roiRightEdge = %f roiBotEdge = %f\n"
+ "sensorReadOutCrop: x=%d y=%d w=%d h=%d\n"
+ "updated cmRoi: x=%f y=%f\n"
- "09:10:56"
- "GP processType=%d cnt=%d, buffers=%ld, FAIL to get CIspHWRegConfigH18 buffer!!!"
- "Kerns_PDX25_B0_v119_mode000_sifr60_pri_m0a_4224x3024_sec_m0a_4224x3024"
- "Kerns_PDX25_B0_v119_mode004_sifr60_pri_m0a_4224x3024_sec_n0a_2112x1512"
- "Kerns_PDX25_B0_v119_mode016_nonsifr240_pri_n1a_2112x1512_sec_skip"
- "Kerns_PDX25_B0_v119_mode017_sifr60_pri_b0a_4224x3024_sec_b0a_4224x3024"
- "Kerns_PDX25_B0_v119_mode019_sifr60_pri_b0a_4224x3024_sec_c0a_2112x1512"
- "Kerns_PDX25_B0_v119_mode029_sifr15_pri_h0a_8448x6048_sec_h0a_8448x6048"
- "Kerns_PDX25_B0_v119_mode102_nonsifr120_pri_m0a_4224x2376_sec_skip"
- "Kerns_PDX25_B0_v119_mode116_nonsifr240_pri_n1a_2112x1188_sec_skip"
- "Kerns_PDX25_B0_v119_mode504_sifr60_pri_m0a_4224x2640_sec_n0a_2112x1320"
- "Kerns_PDX25_B0_v119_mode506_sifr60_pri_m0a_4224x2640_sec_n1a_2112x1320"
- "Kerns_PDX25_B0_v119_mode519_sifr60_pri_b0a_4224x2640_sec_c0a_2112x1320"
- "Kerns_PDX25_B0_v119_mode520_sifr60_pri_b0a_4224x2640_sec_c1a_2112x1320"
- "Kerns_PDX25_B0_v119_mode550_sifr30_pri_h0a_4736x3360_sec_m0a_2368x1680"
- "Kerns_PDX25_B0_v119_mode551_sifr30_pri_h0a_4736x2960_sec_m0a_2368x1480"
- "Kerns_PDX25_B0_v119_mode650_sifr30_pri_h0a_4736x3360_sec_h0a_4736x3360"
- "[DSI] PDE Shouldn't suspend during FID"
- "[DSI] PDE suspend while FID wait for GMC"
- "pProcessedFrameExtra->frameCount == pFlowExtra->frameNum"
- "pProcessedFrameExtra->passId == pFlowExtra->passId"
- "pProcessedFrameExtra->stepId == pFlowExtra->stepId"

```
