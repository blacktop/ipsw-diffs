## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1922.0.1.0.0
-  __TEXT.__text: 0x84674
+1922.0.9.0.0
+  __TEXT.__text: 0x84a84
   __TEXT.__auth_stubs: 0x230
   __TEXT.__cstring: 0x585e
-  __TEXT.__const: 0x19978
+  __TEXT.__const: 0x19a38
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x19b8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 960B1CC2-2412-333D-92C9-1DD90DECB266
-  Functions: 2416
-  Symbols:   4326
+  UUID: 3D7BA0B5-93AB-3876-B8FB-636CBE67C693
+  Functions: 2422
+  Symbols:   4338
   CStrings:  502
 
Symbols:
+ _AccelerateCrypto_SHA3_keccak_2x_hwassist
+ _cckeccak_absorb_blocks_parallel
+ _ccsha3_224_vng_hwassist_compress_parallel
+ _ccsha3_256_vng_hwassist_compress_parallel
+ _ccsha3_384_vng_hwassist_compress_parallel
+ _ccsha3_512_vng_hwassist_compress_parallel
Functions:
+ _AccelerateCrypto_SHA3_keccak_2x_hwassist
+ _ccsha3_256_vng_hwassist_compress_parallel
+ _ccsha3_384_vng_hwassist_compress_parallel
+ _ccsha3_512_vng_hwassist_compress_parallel
+ _ccsha3_224_vng_hwassist_compress_parallel
+ _cckeccak_absorb_blocks_parallel
~ _ccaes_ecb_decrypt : 864 -> 868

```
