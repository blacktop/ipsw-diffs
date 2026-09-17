## AppleAVE2FW_H13S.im4p

> `Firmware/ave/AppleAVE2FW_H13S.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xe3c5c
-  __TEXT.__const: 0x22044
+  __TEXT.__text: 0xe3cb0
+  __TEXT.__const: 0x22054
   __TEXT.__cstring: 0x14d7c
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4384 -> 4404
~ __ZN14CAVCController20ProcessTranscodeDoneEP30CAVEControllerTranscodeDoneCmd : 1440 -> 1436
~ __ZN14CAVCController21InitFlatMbLowQPParamsEv : 784 -> 780
~ __ZN14CAVCController25InitStaticAreaLowQPParamsEii : 1988 -> 1964
~ __ZN14CAVCController19InitScalingListRegsEv : 1072 -> 1076
~ __ZN15CHEVCController16PipePrepareParamEPv : 8024 -> 8044
~ __ZN15CHEVCController19CollectDataFromCpusEb : 3572 -> 3564
~ __ZN15CHEVCController22InitEncodingParametersEPv : 23096 -> 23160
~ __ZN15CHEVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS : 26148 -> 26152
~ __ZN14CAVCController7setPipeEP26CAVEControllerAvcEncodeCmd : 25800 -> 25796
~ __Z20AVE_IOP_Config_pandav : 348 -> 352
~ _exp2f : 168 -> 176
~ sub_da520 -> sub_da570 : 384 -> 388
~ sub_e3b1c -> sub_e3b70 : 328 -> 320
CStrings:
+ "9013.48.1"
- "9013.45.1"
```
