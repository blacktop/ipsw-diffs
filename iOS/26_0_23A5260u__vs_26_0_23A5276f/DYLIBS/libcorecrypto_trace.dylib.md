## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1922.0.1.0.0
-  __TEXT.__text: 0x8519c
+1922.0.9.0.0
+  __TEXT.__text: 0x855dc
   __TEXT.__auth_stubs: 0x230
   __TEXT.__cstring: 0x5b6d
-  __TEXT.__const: 0x19978
+  __TEXT.__const: 0x19a38
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1ad8
+  __TEXT.__unwind_info: 0x1ae0
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf50

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 2B18DF8D-537B-39CD-A706-E441D40A5EA3
-  Functions: 2421
-  Symbols:   4346
+  UUID: A9EE6797-D592-35AC-836C-1EC67ECCEAA9
+  Functions: 2428
+  Symbols:   4358
   CStrings:  533
 
Symbols:
+ _AccelerateCrypto_SHA3_keccak_2x_hwassist
+ _cckeccak_absorb_blocks_parallel
+ _ccsha3_224_vng_hwassist_compress_parallel
+ _ccsha3_256_vng_hwassist_compress_parallel
+ _ccsha3_384_vng_hwassist_compress_parallel
+ _ccsha3_512_vng_hwassist_compress_parallel

```
