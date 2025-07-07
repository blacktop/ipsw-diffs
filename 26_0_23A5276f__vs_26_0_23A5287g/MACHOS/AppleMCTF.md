## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.17.0.0.0
-  __TEXT.__text: 0x73800
+904.33.0.0.0
+  __TEXT.__text: 0x73a84
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x648
-  __TEXT.__cstring: 0x22c8f
-  __TEXT.__const: 0x135d8
+  __TEXT.__cstring: 0x22cb1
+  __TEXT.__const: 0x1e778
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x600
   __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3b70
+  __DATA_CONST.__const: 0x4120
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AF22133-E638-3ED4-A106-9C1D5C5CD133
+  UUID: 96DF29CF-400E-3AA9-BB18-5636A4C340DB
   Functions: 612
   Symbols:   353
   CStrings:  2935
Functions:
~ sub_247a8 : 5204 -> 5200
~ sub_26fdc -> sub_26fd8 : 1024 -> 1020
~ sub_2bca0 -> sub_2bc98 : 6828 -> 7100
~ sub_2e0c8 -> sub_2e1d0 : 1524 -> 1528
~ sub_2edc8 -> sub_2eed4 : 756 -> 836
~ sub_39ae8 -> sub_39c44 : 1168 -> 1176
~ sub_3a024 -> sub_3a188 : 8356 -> 8352
~ sub_414b8 -> sub_41618 : 1968 -> 2192
~ sub_504cc -> sub_5070c : 740 -> 784
~ sub_50a6c -> sub_50cd8 : 312 -> 316
~ sub_70b28 -> sub_70d98 : 1452 -> 1472
CStrings:
+ "%lld %d AVE %s: %s sourceFormat CMPixelFormatType = 0x%x"
+ "%lld %d AVE %s: %s sourceFormat CMPixelFormatType = 0x%x\n"
+ "%lld %d AVE %s: %s source_width=%d source_height=%d needed %dx%d"
+ "%lld %d AVE %s: %s source_width=%d source_height=%d needed %dx%d\n"
+ "23:03:36"
+ "904.33.0"
+ "Jun 30 2025"
- "%lld %d AVE %s: %s sourceFormat CMPixelFormatType = %d"
- "%lld %d AVE %s: %s sourceFormat CMPixelFormatType = %d\n"
- "%lld %d AVE %s: %s source_width=%d source_height=%d"
- "%lld %d AVE %s: %s source_width=%d source_height=%d\n"
- "20:51:05"
- "904.17.0"
- "Jun 18 2025"

```
