## AppleAVE2FW_H14G.im4p

> `Firmware/ave/AppleAVE2FW_H14G.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xe54a8
-  __TEXT.__const: 0x1f054
+  __TEXT.__text: 0xe54bc
+  __TEXT.__const: 0x1f064
   __TEXT.__cstring: 0x14f09
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4384 -> 4392
~ __ZN15CHEVCController16PipePrepareParamEPv : 8020 -> 8028
~ __ZN15CHEVCController22InitEncodingParametersEPv : 23488 -> 23500
~ __ZN14CAVCController7setPipeEP26CAVEControllerAvcEncodeCmd : 26732 -> 26728
~ __ZN15CHEVCController7setPipeEP18AVE_PICMGMT_PARAMS : 20944 -> 20940
~ __Z20AVE_IOP_Config_pandav : 352 -> 348
~ sub_dbccc -> sub_dbcdc : 384 -> 388
CStrings:
+ "9013.48.1"
- "9013.45.1"
```
