## AppleAVE2FW_H19.im4p

> `Firmware/ave/AppleAVE2FW_H19.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x118d58
-  __TEXT.__const: 0x1dc24
-  __TEXT.__cstring: 0x1a2ca
+  __TEXT.__text: 0x118cdc
+  __TEXT.__const: 0x1dc34
+  __TEXT.__cstring: 0x1a2cd
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_patchbay: 0x21a
-  __DATA.__data: 0x1248
+  __DATA.__data: 0x1250
   __DATA._rtk_mtab: 0x298
   __DATA.__const: 0x7598
   __DATA._rtk_power: 0x3b8
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4464 -> 4472
~ __ZN15CHEVCController16PipePrepareParamEPv : 7928 -> 7936
~ __ZN15CHEVCController22InitEncodingParametersEPv : 29196 -> 29040
~ __Z14AVE_CSC_Uninitv : 184 -> 200
~ sub_e6ab0 -> sub_e6a34 : 952 -> 964
~ _pow : 1184 -> 1168
~ sub_10daac -> sub_10da2c : 384 -> 388
CStrings:
+ "%s:%d stopping CtxSched time out %d %d 0x%x"
+ "9013.48.1"
- "%s:%d stopping CtxSched time out %d 0x%x"
- "9013.45.2"
```
