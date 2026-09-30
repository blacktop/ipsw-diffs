## AppleAVE2FW_H18.im4p

> `AppleAVE2FW_H18.im4p`

```diff

 
-  __TEXT.__text: 0x105ba8
+  __TEXT.__text: 0x105c40
   __TEXT.__const: 0x20614
-  __TEXT.__cstring: 0x16a1d
+  __TEXT.__cstring: 0x16a72
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__const: 0x3978
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x16f8
+  __DATA.__data: 0x1700
   __DATA._rtk_mtab: 0x320
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc67f8
-  UUID: 9BD58D73-F2DF-31B7-8A25-D0501231CB96
+  UUID: 8F3324E4-78AC-371D-B165-3C5EC6A56ACA
   Functions: 1195
   Symbols:   1678
-  CStrings:  2564
+  CStrings:  2566
 
Functions:
~ __ZN18CAVEPipeISRManager19HevcXc1WrBfrHandlerEPv : 236 -> 108
~ sub_232e8 -> __ZN18CAVEPipeISRManager11GetSlicePosERjPj : 184 -> 372
~ __ZN15CHEVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDR : 1712 -> 1724
~ __ZN15CMCTFController11ProcessInitEPv : 544 -> 552
~ __ZN15CMCTFController16ProcessHMESCDoneEP15sCmdInformation : 320 -> 340
~ __ZN15CMCTFController15SetFilterGatingEP14MCTF_FrameInfoPb : 1252 -> 1276
~ __ZN7AVE_FPS3AddEPK11_S_AVE_Time : 792 -> 796
~ sub_f55c4 -> sub_f5644 : 72 -> 84
~ sub_f560c -> sub_f5698 : 168 -> 200
~ sub_104f10 -> sub_104fbc : 2496 -> 2476
~ sub_105a6c -> sub_105b04 : 324 -> 316
CStrings:
+ "9003.60.0"
+ "AVE Error: SliceCnt exceed %d [%d, %d]"
+ "AVE Error: slicePosCnt[1] supposed to be zero"
- "9003.47.6"

```
