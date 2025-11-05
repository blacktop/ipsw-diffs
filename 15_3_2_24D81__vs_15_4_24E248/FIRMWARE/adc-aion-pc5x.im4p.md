## adc-aion-pc5x.im4p

> `adc-aion-pc5x.im4p`

```diff

 
-  __TEXT.__text: 0x6c0240
-  __TEXT.__data_copy: 0x80000
-  __TEXT.__const: 0x14c9f8
-  __TEXT.__cstring: 0xd28a7
+  __TEXT.__text: 0x6ce8bc
+  __TEXT.__cstring: 0xd3032
+  __TEXT.__const: 0x14b190
+  __TEXT.text_env: 0x115b0
   __TEXT._rtk_mtab: 0x2a0
+  __TEXT.__data_copy: 0x80000
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
-  __TEXT.text_env: 0x115b0
-  __DATA.__const: 0x45008
+  __DATA.__const: 0x44e58
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0x6a78
-  __DATA._rtk_patchbay: 0x208
+  __DATA._rtk_patchbay: 0x228
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_page_tables: 0x300000
   __DATA._rtk_threads: 0x0
   __DATA._fwinfo: 0x100
+  __DATA.__mod_init_func: 0x10
   __DATA._rtk_boot_l1: 0x80
   __DATA.__gxf_data: 0x10
-  __DATA.__mod_init_func: 0x10
   __DATA.__noinit: 0x0
   __DATA.__zerofill: 0xbea78
-  UUID: 8C6C39D4-97C4-3FD6-AEE9-7F55840A1105
+  UUID: 37AF4EE7-4018-3A76-9654-943107A4CC57
   Functions: 0
   Symbols:   0
-  CStrings:  22970
+  CStrings:  22999
 
CStrings:
+ "  0x10b: Offloading - n/a\n"
+ "  0x10c: size - n/a\n"
+ "  0x10d: LTM\n"
+ "!include_source"
+ "((size_t)allowed_length) <= max_string_length"
+ "(size_t)(n + 2) <= MAX_LENGTH"
+ "(size_t)n <= MAX_LENGTH"
+ "./h10isp/filters/IC/CImageCaptureH6.cpp"
+ "20:56:33"
+ ">>> [MSTF] bCurrMSTFEn=%d\n"
+ ">>> [MSTF] bCurrMSTFScale0En=%d\n"
+ ">>> [MSTF] bMSTFEn=%d\n"
+ ">>> [MSTF] currFusionType=%d\n"
+ ">>> [MSTF] mstfScale0TFStrength=%d\n"
+ "AlgoMisc WARNING: ill or uninitialized  Matrix detected!"
+ "CAM Strob used but not set"
+ "CISP_CMD_APPLE_CH_TNR_STRENGTH_HIGH_ENABLE"
+ "CmdTNRStrengthHighEnable"
+ "GetStatDefaultIndex"
+ "IMX343RegSetting.cpp"
+ "MRCAMStrobeGpioGet"
+ "Mar  7 2025"
+ "[H15 iPads EW IMX814] MSTF(YUV) stdScalePlus=%f, stdScale=[%.2f, %.2f, %.2f, %.2f, %.2f, %.2f]\n"
+ "[H15 iPads EW IMX814] MSTF(YUV), bTNRStrengthHighEn=%d, gainTotal = %f\n"
+ "[H15 iPads EW IMX814] YSH totGain=%.2f, currShKnobLevel=%d, yshKnobScaleb=%.2f."
+ "[H15 iPads FCAM PA IMX614 & EW IMX814] Still capture use case, no bcfCoeff overwrite in FW layer\n"
+ "[H15 iPads FaceTime bTNRStrengthHighEn==1], apply BCF LPF to reduce grainy noises under lowlight.\n\tknobValueBcfLpfG=%d, knobValueBcfLpfRB=%d.\n"
+ "[H15 iPads IN IMX405] 4K High FPS (MCTF off), less YSH applied for mid/lowlight."
+ "[H15 iPads IN IMX405] MSTF(YUV) stdScalePlus=%f, stdScale=[%.2f, %.2f, %.2f, %.2f, %.2f, %.2f]\n"
+ "[H15 iPads IN IMX405] More aggressive temporal NR for shadow region.\n"
+ "[H15 iPads IN IMX405] Still capture use case, no bcfCoeff overwrite in FW layer\n"
+ "[H15 iPads IN IMX405] Still capture use case, no knobLuma/knobChroma overwrite in FW layer\n"
+ "[H15 iPads IN IMX405] Still capture use case, no knobMBNR overwrite in FW layer\n"
+ "[H15 iPads IN IMX405] YSH totGain=%.2f, currShKnobLevel=%d, yshKnobScaleb=%.2f."
+ "[H15 iPads IN IMX405] apply BCF LPF to reduce grainy noises.\n\tknobValueBcfLpfG=%d, knobValueBcfLpfRB=%d.\n"
+ "[H15 iPads IN IMX405] paramMsMbnr.knobValue=%d, paramMsMbnr.sigmaLuma[1-5]=[%d,%d,%d,%d,%d]"
+ "[H15 iPads IN IMX405] total gain=%.2f, paramMbnr.knobValue=%d"
+ "[H15 iPads PA IMX614] MSMLNR ParamLumaNet[0].Knee=%d, Slope=%d\n"
+ "[H15 iPads PA IMX614] MSMLNR ParamLuma[0].Knee=%d, Slope=%d\n"
+ "[H15 iPads PA IMX614] MSTF(YUV) stdScalePlus=%f, stdScale=[%.2f, %.2f, %.2f, %.2f, %.2f, %.2f]\n"
+ "[H15 iPads PA IMX614] Still capture use case, no knobLuma/knobChroma overwrite in FW layer\n"
+ "[H15 iPads PA IMX614] Still capture use case, no knobMBNR overwrite in FW layer\n"
+ "[H15 iPads PA IMX614] YSH totGain=%.2f, currShKnobLevel=%d, yshKnobScaleb=%.2f."
+ "[H15 iPads PA IMX614] adapKnee=%d, adapSlope=%d\n"
+ "[H15 iPads PA IMX614] paramMsMbnr.knobValue=%d, paramMsMbnr.sigmaLuma[1-5]=[%d,%d,%d,%d,%d]"
+ "[H15 iPads PA IMX614] total gain=%.2f, paramMbnr.knobValue=%d"
+ "[J48x FFC (PA-IMX614)] MSTF(YUV), bTNRStrengthHighEn=%d, gainTotal = %f\n"
+ "[ResMgr]Get Ch %d Stats default %d"
+ "ch%d, bTNRStrengthHighEn %d"
+ "gpioCfg.mRCAMStrobeGpio != GPIO_NOT_SET"
+ "include_source"
+ "inputDataLength + 2 <= MAX_LENGTH"
+ "lensPositionCount <= MAX_LENS_COUNT"
+ "oH:%d is less than vio max input, no need to downscale"
+ "oW:%d is less than vio max input, no need to downscale"
+ "outHeight:%d is more than max VIO input height i.e.,1023"
+ "outWidth:%d is more than max VIO input width i.e.,640"
+ "windowCount <= MAX_WIN_COUNT"
- "%s GetOutputs: unsupported channel %d\n"
- "./h10isp/drivers/SENSOR/IMX356/IMX356RegSetting.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/ar_imx613.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/be_imx713.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/db_imx703.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/ht_imx633.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/in_imx405.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/kv_imx803.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/mt_imx353.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/mt_imx353_h10.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/mw_imx904.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/on_imx503.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/pt_imx772.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/sc_imx714.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/tx_imx403.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/wi_imx603.cpp"
- "./h10isp/filters/Algorithm/PDAF/config/wy_imx343.cpp"
- "18:55:05"
- "CDM: Got an unknown Command %zu\n"
- "Dec 13 2024"
- "Got an unknown EndPoint command %d\n"
- "IMX356RegSetting.cpp"
- "MapHomographyMatrix"
- "MapHomographyMatrix failed"
- "Unknown LED grouping %d\n"
- "Unknown endpoint command"
- "[DSI] Invalid Compliance mode value."
- "interpWeight >= 0.f"
- "mapping->SIF == -1 || hSif != 0"

```
