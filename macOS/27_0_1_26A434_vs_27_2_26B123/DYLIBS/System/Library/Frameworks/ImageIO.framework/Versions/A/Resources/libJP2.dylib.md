## libJP2.dylib

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJP2.dylib`

```diff

-2851.0.0.0.0
-  __TEXT.__text: 0xd2aac
-  __TEXT.__gcc_except_tab: 0x5f64
+2851.1.8.0.0
+  __TEXT.__text: 0xd2e80
+  __TEXT.__gcc_except_tab: 0x5f84
   __TEXT.__const: 0x2e7e
   __TEXT.__cstring: 0x280af
   __TEXT.__unwind_info: 0x2030

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2385
+  Functions: 2384
   Symbols:   2426
   CStrings:  2023
 
Functions:
~ __ZN8kd_block13retrieve_dataEP9kdu_blocki : 768 -> 848
~ __ZN15kd_block_reader8get_byteEv : 132 -> 180
~ __ZN15kd_block_reader9get_bytesEN7bounded2v111bounded_ptrIhEEi : 216 -> 280
~ __ZN7kd_tile10initializeEv : 13040 -> 13208
~ __ZN7kd_tile7recycleEP11kd_tile_ref10kdu_coords8kdu_dims : 4208 -> 4384
~ __ZL12OpenJP2InputP17MyAccessCallbacksP10JP2Storage : 564 -> 576
~ __ZN11MyJP2Source4readEN7bounded2v111bounded_ptrIhEEi : 124 -> 132
~ __ZN11MyJP2Source4seekEx : 52 -> 60
~ __ZN16kdc_flow_controlC2EP12kdu_image_in14kdu_codestreamib : 760 -> 820
~ __ZN12kdu_image_in12readNextLineEv : 96 -> 104
~ __cg_JP2CompressorSetup : 576 -> 956
~ __ZN21MyJP2CompressedTarget5writeEN7bounded2v111bounded_ptrIKhEEi : 120 -> 128
+ _ZN12kd_synthesis25simulate_vertical_liftingEi.cold.1
- _ZN12kd_synthesis25simulate_vertical_liftingEi.cold.1
- _ZN12kd_synthesis4pullER12kdu_line_buf.cold.9
```
