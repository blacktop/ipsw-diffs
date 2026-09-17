## AppleAVE2FW_H13D.im4p

> `Firmware/ave/AppleAVE2FW_H13D.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xff410
-  __TEXT.__const: 0x22924
+  __TEXT.__text: 0xff434
+  __TEXT.__const: 0x22934
   __TEXT.__cstring: 0x16615
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4452 -> 4460
~ __ZN14CAVCController28ProcessDataFromCpusMultiCoreE9SliceType : 14844 -> 14832
~ __ZN15CHEVCController16PipePrepareParamEPv : 8628 -> 8636
~ __ZN15CHEVCController22InitEncodingParametersEPv : 24668 -> 24708
~ __ZN15CHEVCController28ProcessDataFromCpusMultiCoreEv : 13484 -> 13472
~ sub_f5b10 -> sub_f5b30 : 384 -> 388
CStrings:
+ "9013.48.1"
- "9013.45.1"
```
