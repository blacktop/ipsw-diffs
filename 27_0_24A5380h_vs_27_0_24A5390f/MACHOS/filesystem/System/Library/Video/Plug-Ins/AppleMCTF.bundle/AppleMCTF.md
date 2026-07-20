## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.8.0.0.0
-  __TEXT.__text: 0x85e20
+913.29.1.0.0
+  __TEXT.__text: 0x86914
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x2809a
-  __TEXT.__const: 0x22ab8
+  __TEXT.__cstring: 0x2837c
+  __TEXT.__const: 0x22a08
   __TEXT.__gcc_except_tab: 0x628
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x670
   __DATA_CONST.__const: 0x53b0
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 668
   Symbols:   341
-  CStrings:  3412
+  CStrings:  3427
 
Functions:
~ sub_3320 : 6584 -> 7052
~ sub_1ca00 -> sub_1cbd4 : 2780 -> 2772
~ sub_302b8 -> sub_30484 : 1136 -> 1152
~ sub_31598 -> sub_31774 : 5320 -> 5300
~ sub_341b0 -> sub_34378 : 968 -> 984
~ sub_34c40 -> sub_34e18 : 8100 -> 8704
~ sub_38f00 -> sub_39334 : 4036 -> 4040
~ sub_3dda4 -> sub_3e1dc : 28220 -> 29256
~ sub_44f78 -> sub_457bc : 11284 -> 11420
~ sub_494a0 -> sub_49d6c : 7756 -> 7784
~ sub_50bf0 -> sub_514d8 : 1592 -> 1596
~ sub_5123c -> sub_51b28 : 136 -> 492
~ sub_51e28 -> sub_52878 : 264 -> 428
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
+ "21:39:53"
+ "913.29.1"
+ "AVE_CalcBufSizeOfMBInputCtrl"
+ "AuxiliaryLayerProperties = "
+ "EncodesAuxiliaryWithAuxID = %d\n"
+ "HEVCAuxiliaryIDs = "
+ "HEVCAuxiliaryLayerIDs = "
+ "Jul 14 2026"
+ "size >= 0 && size <= 2147483647"
- "21:23:03"
- "913.8.0"
- "Jun 29 2026"
```
