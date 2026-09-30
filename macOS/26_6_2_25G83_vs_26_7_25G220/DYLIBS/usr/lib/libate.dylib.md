## libate.dylib

> `/usr/lib/libate.dylib`

```diff

-3.0.9.0.0
-  __TEXT.__text: 0x3afb8
+3.0.12.0.0
+  __TEXT.__text: 0x3b0ac
   __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x51210
-  __TEXT.__cstring: 0x1b2e
+  __TEXT.__const: 0x51220
+  __TEXT.__cstring: 0x1ba8
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__unwind_info: 0x338
   __TEXT.__eh_frame: 0x50

   - /usr/lib/libobjc.A.dylib
   Functions: 293
   Symbols:   500
-  CStrings:  179
+  CStrings:  180
 
Functions:
~ __ZN9ATEncoder16GetBlockFeaturesE17at_block_format_tP17at_block_buffer_t9at_size_tmPm10at_flags_t : 616 -> 672
~ _DecodeASTC_RGBA_vec : 6436 -> 6624
CStrings:
+ "at_block_get_features Error: src->sliceBytes (%lu) is less than what is required to store a slice of content (%lu bytes)\n"
```
