## com.apple.driver.AppleT8130TypeCPhy

> `com.apple.driver.AppleT8130TypeCPhy`

```diff

-266.40.3.0.0
+266.80.9.0.0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x8837
-  __TEXT.__os_log: 0xe84a
-  __TEXT_EXEC.__text: 0x4eea0
+  __TEXT.__cstring: 0x9b80
+  __TEXT.__os_log: 0xfb65
+  __TEXT_EXEC.__text: 0x535a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2d8
   __DATA.__common: 0x58

   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__const: 0x878
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 89B4C4FB-85C2-36DF-BF3C-75C0B87B3C4D
+  UUID: D80D825F-E492-36A1-BC9D-97AAC260AB9A
   Functions: 130
   Symbols:   0
-  CStrings:  831
+  CStrings:  926
 
Functions:
~ __ZN18AppleT8130TypeCPhy5startEP9IOService : 8772 -> 8896
~ sub_fffffe0009f37aa4 -> sub_fffffe000a01acb0 : 580 -> 628
~ sub_fffffe0009f3bd50 -> sub_fffffe000a01ef8c : 5272 -> 5264
~ __ZN18AppleT8130TypeCPhy13eusb2phy_initEbb : 10564 -> 11320
~ sub_fffffe0009f46160 -> sub_fffffe000a029688 : 2540 -> 2624
~ sub_fffffe0009f75460 -> sub_fffffe000a0589dc : 684 -> 708
~ __ZN18AppleT8130TypeCPhy16loadS2RSavePartAEj : 44504 -> 61380
~ __ZN18AppleT8130TypeCPhy16loadS2RSavePartBEj : 12560 -> 12840
CStrings:
+ "%s@%s: %s::%s: failed to configure usb-repeater %s\n"
+ "%s@%s: %s::%s: found usb-repeater %s\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_CZ_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_CZ_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_CZ_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_CZ_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_RZ_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_RZ_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_RZ_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var ctle_cfg1 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_CTLE_CFG1.AEQ_S2R_CTLE_RZ_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg3 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG3.AEQ_S2R_DFEH1DAC_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg3 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG3.AEQ_S2R_DFEH1DAC_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg3 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG3.AEQ_S2R_DFEH1DAC_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg3 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG3.AEQ_S2R_DFEH1DAC_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg3 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG3.AEQ_S2R_DFEH2DAC_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH2DAC_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH2DAC_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH2DAC_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH3DAC_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH3DAC_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH3DAC_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH3DAC_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG4.AEQ_S2R_DFEH4DAC_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH4DAC_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH4DAC_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH4DAC_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH5DAC_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH5DAC_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH5DAC_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var dfe_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_DFE_CFG5.AEQ_S2R_DFEH5DAC_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG4.AEQ_S2R_DCLK_POS_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG4.AEQ_S2R_DCLK_POS_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG4.AEQ_S2R_DCLK_POS_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg4 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG4.AEQ_S2R_DCLK_POS_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG5.AEQ_S2R_XCLK_POS_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG5.AEQ_S2R_XCLK_POS_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG5.AEQ_S2R_XCLK_POS_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg5 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG5.AEQ_S2R_XCLK_POS_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg6 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG6.AEQ_S2R_DCLKB_POS_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg6 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG6.AEQ_S2R_DCLKB_POS_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg6 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG6.AEQ_S2R_DCLKB_POS_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg6 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG6.AEQ_S2R_DCLKB_POS_GT8G_10G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg7 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG7.AEQ_S2R_XCLKB_POS_2P5G_5G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg7 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG7.AEQ_S2R_XCLKB_POS_GT10G_20G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg7 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG7.AEQ_S2R_XCLKB_POS_GT5G_8G_GRAY = 0x%x\n"
+ "%s@%s: %s::%s: var iqa_cfg7 field AUSPMA_RX_TOP_BLK_AEQ_CTRL_IQA_CFG7.AEQ_S2R_XCLKB_POS_GT8G_10G_GRAY = 0x%x\n"
+ "121111121222121211111112121212121112111122122222222222222222222222221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221111211"
+ "IOService"
+ "usb-repeater"
+ "usb-repeater-options"
- "1211111212221212111111121212121211121111221222222222222222222222222112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122112211221122111121"

```
