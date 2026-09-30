## libJP2.dylib

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJP2.dylib`

```diff

-2851.0.0.0.0
-  __TEXT.__text: 0xd20e0
-  __TEXT.__gcc_except_tab: 0x5f64
+2851.1.4.0.0
+  __TEXT.__text: 0xd237c
+  __TEXT.__gcc_except_tab: 0x5f84
   __TEXT.__const: 0x2e7e
   __TEXT.__cstring: 0x280af
   __TEXT.__unwind_info: 0x3050

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2385
+  Functions: 2384
   Symbols:   2426
   CStrings:  2023
 
Functions:
~ __ZN7kd_tile10initializeEv : 13040 -> 13208
~ __ZN7kd_tile7recycleEP11kd_tile_ref10kdu_coords8kdu_dims : 4208 -> 4384
~ __ZL12OpenJP2InputP17MyAccessCallbacksP10JP2Storage : 564 -> 576
~ __ZN11MyJP2Source4readEN7bounded2v111bounded_ptrIhEEi : 124 -> 132
~ __ZN11MyJP2Source4seekEx : 52 -> 60
~ __ZN16kdc_flow_controlC2EP12kdu_image_in14kdu_codestreamib : 760 -> 800
~ __ZN12kdu_image_in12readNextLineEv : 96 -> 104
~ __cg_JP2CompressorSetup : 576 -> 856
~ __ZN21MyJP2CompressedTarget5writeEN7bounded2v111bounded_ptrIKhEEi : 120 -> 128
+ _ZN12kd_synthesis25simulate_vertical_liftingEi.cold.1
- _ZN12kd_synthesis25simulate_vertical_liftingEi.cold.1
- _ZN12kd_synthesis4pullER12kdu_line_buf.cold.9
```
