## libAppleEXR.dylib

> `/usr/lib/libAppleEXR.dylib`

```diff

-1006.0.0.0.0
-  __TEXT.__text: 0x9f644
+1010.0.0.0.0
+  __TEXT.__text: 0xa0a30
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x211bc
-  __TEXT.__gcc_except_tab: 0x4e0
-  __TEXT.__cstring: 0x456f
+  __TEXT.__gcc_except_tab: 0x4e4
+  __TEXT.__cstring: 0x469c
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xbe8
+  __TEXT.__unwind_info: 0xc00
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 730
-  Symbols:   946
-  CStrings:  450
+  Functions: 733
+  Symbols:   949
+  CStrings:  452
 
Symbols:
+ __ZN14AXRChunkHeader11GetMipLevelE11ChunkLayout
+ __ZN4Part11InitOffsetsEPKvmRmm11axr_flags_t
+ __ZNK15TileDecoder_B4426HasSubsampledPartialBlocksEv
+ __ZNK4Part20CheckChunkPartNumberEPKvmmm11axr_flags_t
+ __ZZN4Part11InitOffsetsEPKvmRmm11axr_flags_tE13kRowSizeProcs
- __ZN4Part11InitOffsetsEPKvmRm11axr_flags_t
- __ZZN4Part11InitOffsetsEPKvmRm11axr_flags_tE13kRowSizeProcs
CStrings:
+ "%s error: expected rowBytes for channel size (%lu) x RGBA channel count (%lu) x width (%u) = %lu bytes\n\tThe provided destination row bytes is only %lu and the data will not fit.\n\tSkipping operation."
+ "EXR File corrupted: chunk appears in the offset table for part %lu, but reports it belongs to part %d"
```
