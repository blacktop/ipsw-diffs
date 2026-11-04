## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-200.69.0.0.0
-  __TEXT.__const: 0xc3140
-  __TEXT.__cstring: 0x25390
-  __TEXT_EXEC.__text: 0x13c0b0
-  __TEXT_EXEC.__auth_stubs: 0xbd0
+200.74.0.0.0
+  __TEXT.__const: 0xc31d0
+  __TEXT.__cstring: 0x2595b
+  __TEXT_EXEC.__text: 0x13da48
+  __TEXT_EXEC.__auth_stubs: 0xbe0
   __DATA.__data: 0x22388
   __DATA.__common: 0x2738
   __DATA_CONST.__mod_init_func: 0x698
   __DATA_CONST.__mod_term_func: 0x670
-  __DATA_CONST.__const: 0x2ac90
+  __DATA_CONST.__const: 0x2ad60
   __DATA_CONST.__kalloc_type: 0x4e80
   __DATA_CONST.__kalloc_var: 0x13b0
-  __DATA_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__auth_got: 0x5f0
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10276
+  Functions: 10311
   Symbols:   0
-  CStrings:  3715
+  CStrings:  3739
 
CStrings:
+ "%s %s dimension (%u) + offset (%u) > buffer (%u)\n"
+ "%s Plane %u tile-data offset %llu is outside the %llu byte surface\n"
+ "%s Plane %u tiled write extent %llu exceeds plane tile-data size %llu (stride %llu x %llu macroblock rows)\n"
+ "%s Plane %u tiled write extent %llu exceeds the %llu bytes available at offset %llu (pitch %llu x %llu macroblock rows, plane height %llu, macroblock %llux%llu)\n"
+ "%s no memory descriptor\n"
+ "%s plane %d region offset 0x%llx + yOffset %lld rows exceeds plane limit 0x%llx / surface length 0x%llx\n"
+ "%s plane %d tile data offset 0x%llx (plane limit 0x%llx) or metadata offset 0x%llx/size 0x%llx exceeds surface length 0x%llx\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator_kexts/StatusDescriptorRingMSR29.cpp"
+ "Comm API outbound size %u exceeds max %zu\n"
+ "Comm API type %d in wrong slot %d (canonical %d)\n"
+ "GetDiag denied: diagnostics are debug-only\n"
+ "HCU API bad buffer: type=%s addr=%p len=%llu\n"
+ "HCU API entry header past end of buffer: headerEnd=%p bufferEnd=%p\n"
+ "HCU API entry too small: size=%u min=%zu type=%s\n"
+ "Interchange tile %ux%u is not a supported square tile size\n"
+ "SDR loadWritePointer: out-of-range write pointer from FW (ptr_value=%u -> %zu bytes, fLength=%zu); ignoring\n"
+ "[IOSA] Discarding needs-reset SD frame_id %u, no outstanding request\n"
+ "[MSRCPU] %s log ring out of bounds (offset=%08X, size=%08X); disabling\n"
+ "[MSRCPU] main log flush exceeded iteration cap; aborting\n"
+ "[MSRCPU] prof log flush exceeded iteration cap; aborting\n"
+ "loadWritePointer"
+ "main"
+ "prof"
+ "received zero-size TransformSurfaceData\n"
+ "setProperties denied: runtime properties are debug-only\n"
+ "still waiting on thread %d\n"
+ "validateBufferRegions"
- "%s Plane %u Size %llu cannot support a stride of %llu for macroblocks height %llu\n"
- "HCU API bad entry header: headerEnd=%p bufferEnd=%p size=%u min=%zu type=%s\n"
- "given size (%llu) doesn't match TransformSurfaceData's (%lu)\n"
```
