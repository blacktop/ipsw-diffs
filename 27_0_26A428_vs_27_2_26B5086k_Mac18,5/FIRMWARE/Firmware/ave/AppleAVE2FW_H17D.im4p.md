## AppleAVE2FW_H17D.im4p

> `Firmware/ave/AppleAVE2FW_H17D.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0x1140c4
-  __TEXT.__const: 0x27cc4
-  __TEXT.__cstring: 0x17f3c
+  __TEXT.__text: 0x1140d8
+  __TEXT.__const: 0x27cd4
+  __TEXT.__cstring: 0x17f5a
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA.__zerofill: 0xd3720
   Functions: 1223
   Symbols:   1713
-  CStrings:  2715
+  CStrings:  2716
 
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4520 -> 4528
~ __ZN14CAVCController28ProcessDataFromCpusMultiCoreE9SliceType : 14844 -> 14832
~ __ZN15CHEVCController16PipePrepareParamEPv : 8660 -> 8668
~ __ZN15CHEVCController22InitEncodingParametersEPv : 24592 -> 24572
~ __ZN15CHEVCController28ProcessDataFromCpusMultiCoreEv : 13272 -> 13260
~ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb : 236 -> 344
~ sub_c485c -> sub_c48ac : 272 -> 268
~ __ZN10CAVEClientC2EPKcP7CObjectP12MappedMemoryPviyjjjjbP14AVE_PIODMACtrl : 3948 -> 3888
~ sub_10a6e4 -> sub_10a6f4 : 384 -> 388
~ sub_113f84 -> sub_113f98 : 320 -> 328
CStrings:
+ "9013.48.1"
+ "Applying gating for frame: %d"
- "9013.45.1"
```
