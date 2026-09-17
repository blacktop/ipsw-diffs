## AppleAVE2FW_H14D.im4p

> `Firmware/ave/AppleAVE2FW_H14D.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xff1bc
-  __TEXT.__const: 0x22c44
+  __TEXT.__text: 0xff1e0
+  __TEXT.__const: 0x22c54
   __TEXT.__cstring: 0x165aa
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4520 -> 4528
~ __ZN14CAVCController28ProcessDataFromCpusMultiCoreE9SliceType : 14844 -> 14832
~ __ZN15CHEVCController16PipePrepareParamEPv : 8632 -> 8640
~ __ZN15CHEVCController22InitEncodingParametersEPv : 24688 -> 24728
~ __ZN15CHEVCController28ProcessDataFromCpusMultiCoreEv : 13272 -> 13260
~ sub_f581c -> sub_f583c : 384 -> 388
~ sub_ff07c -> sub_ff0a0 : 328 -> 320
CStrings:
+ "9013.48.1"
- "9013.45.1"
```
