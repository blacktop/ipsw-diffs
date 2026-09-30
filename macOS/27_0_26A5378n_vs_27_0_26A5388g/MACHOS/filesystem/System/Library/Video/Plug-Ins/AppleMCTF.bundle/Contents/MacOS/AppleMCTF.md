## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/Contents/MacOS/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.8.0.0.0
-  __TEXT.__text: 0x85c1c
+913.29.1.0.0
+  __TEXT.__text: 0x86710
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x2809a
-  __TEXT.__const: 0x22ac8
+  __TEXT.__cstring: 0x2837c
+  __TEXT.__const: 0x22a18
   __TEXT.__gcc_except_tab: 0x628
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x670
   __DATA_CONST.__const: 0x53b0
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 666
   Symbols:   341
-  CStrings:  3412
+  CStrings:  3427
 
Functions:
~ sub_3360 : 6584 -> 7052
~ sub_1cab4 -> sub_1cc88 : 2780 -> 2772
~ sub_3037c -> sub_30548 : 1136 -> 1152
~ sub_31664 -> sub_31840 : 5320 -> 5300
~ sub_3427c -> sub_34444 : 968 -> 984
~ sub_34d0c -> sub_34ee4 : 8100 -> 8704
~ sub_38fcc -> sub_39400 : 4036 -> 4040
~ sub_3de70 -> sub_3e2a8 : 28200 -> 29240
~ sub_45030 -> sub_45878 : 11272 -> 11404
~ sub_49550 -> sub_49e1c : 7756 -> 7784
~ sub_50ca0 -> sub_51588 : 1592 -> 1596
~ sub_512ec -> sub_51bd8 : 136 -> 492
~ sub_51ed8 -> sub_52928 : 264 -> 428
CStrings:
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s::%s:%d  ps[%d] aveType=%d layerID=%d size=%d byte0=0x%02x byte1=0x%02x hevcNalType=%d"
+ "%lld %d AVE %s: %s::%s:%d  ps[%d] aveType=%d layerID=%d size=%d byte0=0x%02x byte1=0x%02x hevcNalType=%d\n"
+ "%lld %d AVE %s: %s::%s:%d VTEncoderSessionCreateVideoFormatDescription failed res=%d; dumping %d HEVC NAL units"
+ "%lld %d AVE %s: %s::%s:%d VTEncoderSessionCreateVideoFormatDescription failed res=%d; dumping %d HEVC NAL units\n"
+ "%s%d"
+ "%s%s:%d:%d"
+ ","
+ "21:33:36"
+ "913.29.1"
+ "AVE_CalcBufSizeOfMBInputCtrl"
+ "AuxiliaryLayerProperties = "
+ "EncodesAuxiliaryWithAuxID = %d\n"
+ "HEVCAuxiliaryIDs = "
+ "HEVCAuxiliaryLayerIDs = "
+ "Jul 14 2026"
+ "size >= 0 && size <= 2147483647"
- "21:06:00"
- "913.8.0"
- "Jun 30 2026"
```
