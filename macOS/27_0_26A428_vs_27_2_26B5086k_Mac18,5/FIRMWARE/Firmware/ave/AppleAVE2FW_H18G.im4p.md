## AppleAVE2FW_H18G.im4p

> `Firmware/ave/AppleAVE2FW_H18G.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x118ac8
-  __TEXT.__const: 0x17ab8
-  __TEXT.__cstring: 0x1a2ff
+  __TEXT.__text: 0x118acc
+  __TEXT.__const: 0x17ac8
+  __TEXT.__cstring: 0x1a320
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_patchbay: 0x21a

   __DATA.__zerofill: 0xc68e0
   Functions: 1319
   Symbols:   1800
-  CStrings:  2939
+  CStrings:  2940
 
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4464 -> 4472
~ __ZN15CHEVCController16PipePrepareParamEPv : 7928 -> 7936
~ __ZN15CHEVCController22InitEncodingParametersEPv : 29196 -> 29040
~ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb : 236 -> 344
~ __Z14AVE_CSC_Uninitv : 184 -> 200
~ sub_e68c8 -> sub_e68b8 : 952 -> 964
~ __Z20AVE_IOP_Config_pandav : 348 -> 352
~ sub_10d82c : 384 -> 388
CStrings:
+ "%s:%d stopping CtxSched time out %d %d 0x%x"
+ "9013.48.1"
+ "Applying gating for frame: %d"
- "%s:%d stopping CtxSched time out %d 0x%x"
- "9013.45.1"
```
