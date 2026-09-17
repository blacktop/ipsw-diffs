## AppleAVE2FW_H15G.im4p

> `Firmware/ave/AppleAVE2FW_H15G.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xf8468
-  __TEXT.__const: 0x21794
-  __TEXT.__cstring: 0x166f1
+  __TEXT.__text: 0xf84fc
+  __TEXT.__const: 0x217a4
+  __TEXT.__cstring: 0x1670f
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA.__zerofill: 0xc67e0
   Functions: 1176
   Symbols:   1627
-  CStrings:  2544
+  CStrings:  2545
 
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4452 -> 4460
~ __ZN15CHEVCController16PipePrepareParamEPv : 8152 -> 8160
~ __ZN15CHEVCController22InitEncodingParametersEPv : 23388 -> 23408
~ __ZN14CAVCController7setPipeEP26CAVEControllerAvcEncodeCmd : 26868 -> 26864
~ __ZN15CHEVCController7setPipeEP18AVE_PICMGMT_PARAMS : 21144 -> 21140
~ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb : 236 -> 344
~ _exp2f : 168 -> 176
~ sub_eec4c -> sub_eecdc : 384 -> 388
CStrings:
+ "9013.48.1"
+ "Applying gating for frame: %d"
- "9013.45.1"
```
