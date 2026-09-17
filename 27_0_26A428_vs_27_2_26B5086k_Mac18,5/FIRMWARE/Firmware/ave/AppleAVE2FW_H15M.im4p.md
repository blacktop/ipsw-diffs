## AppleAVE2FW_H15M.im4p

> `Firmware/ave/AppleAVE2FW_H15M.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0x1120fc
-  __TEXT.__const: 0x25e34
-  __TEXT.__cstring: 0x17dc5
+  __TEXT.__text: 0x112110
+  __TEXT.__const: 0x25e44
+  __TEXT.__cstring: 0x17de3
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA.__zerofill: 0xd3720
   Functions: 1222
   Symbols:   1710
-  CStrings:  2708
+  CStrings:  2709
 
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4520 -> 4528
~ __ZN14CAVCController28ProcessDataFromCpusMultiCoreE9SliceType : 14844 -> 14832
~ __ZN15CHEVCController16PipePrepareParamEPv : 8656 -> 8664
~ __ZN15CHEVCController22InitEncodingParametersEPv : 24512 -> 24488
~ __ZN15CHEVCController28ProcessDataFromCpusMultiCoreEv : 13272 -> 13260
~ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb : 236 -> 344
~ sub_c292c -> sub_c2978 : 272 -> 268
~ __ZN10CAVEClientC2EPKcP7CObjectP12MappedMemoryPviyjjjjbP14AVE_PIODMACtrl : 3948 -> 3888
~ __Z20AVE_IOP_Config_pandav : 484 -> 488
~ sub_10871c -> sub_10872c : 384 -> 388
~ sub_111fbc -> sub_111fd0 : 328 -> 320
CStrings:
+ "9013.48.1"
+ "Applying gating for frame: %d"
- "9013.45.1"
```
