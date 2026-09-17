## AppleAVE2FW_H13G.im4p

> `Firmware/ave/AppleAVE2FW_H13G.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0xdf58c
-  __TEXT.__const: 0x1ead4
+  __TEXT.__text: 0xdf580
+  __TEXT.__const: 0x1eae4
   __TEXT.__cstring: 0x14cc1
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
Functions:
~ __ZN14CAVCController16PipePrepareParamEPv : 4364 -> 4384
~ __ZN14CAVCController25InitStaticAreaLowQPParamsEii : 1988 -> 1968
~ __ZN15CHEVCController9ManageDPBEP18AVE_PICMGMT_PARAMSj : 1872 -> 1864
~ __ZN15CHEVCController8calc_rpsEhiP23HEVC_SPS_SHORT_TERM_RPSP19HEVC_SHORT_TERM_RPSPK22HEVC_SPS_LONG_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSj : 1420 -> 1416
~ __ZN15CHEVCController16PipePrepareParamEPv : 8616 -> 8636
~ __ZN15CHEVCController22InitEncodingParametersEPv : 23476 -> 23460
~ _exp2f : 176 -> 168
~ sub_d5e50 -> sub_d5e40 : 384 -> 388
~ sub_df44c -> sub_df440 : 328 -> 320
CStrings:
+ "9013.48.1"
- "9013.45.1"
```
