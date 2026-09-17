## AppleAVE2FW_H16S.im4p

> `Firmware/ave/AppleAVE2FW_H16S.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0x113d24
-  __TEXT.__const: 0x27764
-  __TEXT.__cstring: 0x17f0d
+  __TEXT.__text: 0x113d38
+  __TEXT.__const: 0x27774
+  __TEXT.__cstring: 0x17f2b
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA.__zerofill: 0xc9ba0
   Functions: 1222
   Symbols:   1711
-  CStrings:  2713
+  CStrings:  2714
 
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4520 -> 4528
~ __ZN14CAVCController28ProcessDataFromCpusMultiCoreE9SliceType : 14844 -> 14832
~ __ZN15CHEVCController16PipePrepareParamEPv : 8660 -> 8668
~ __ZN15CHEVCController22InitEncodingParametersEPv : 24592 -> 24572
~ __ZN15CHEVCController28ProcessDataFromCpusMultiCoreEv : 13272 -> 13260
~ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb : 236 -> 344
~ sub_c45b0 -> sub_c4600 : 272 -> 268
~ __ZN10CAVEClientC2EPKcP7CObjectP12MappedMemoryPviyjjjjbP14AVE_PIODMACtrl : 3948 -> 3888
~ sub_10a344 -> sub_10a354 : 384 -> 388
~ sub_113be4 -> sub_113bf8 : 320 -> 328
CStrings:
+ "9013.48.1"
+ "Applying gating for frame: %d"
- "9013.45.1"
```
