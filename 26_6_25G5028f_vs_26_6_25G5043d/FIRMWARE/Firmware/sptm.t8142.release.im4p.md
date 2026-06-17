## sptm.t8142.release.im4p

> `Firmware/sptm.t8142.release.im4p`

```diff

-611.160.8.0.0
-  __TEXT.__cstring: 0x1249c sha256:34290559648f1424461eb2945d8049a4bd287c1deac8233b6a212ee0129ff217
+611.160.16.0.0
+  __TEXT.__cstring: 0x126ac sha256:0e4532545fae1ce0fde7ddc23accc8cb4319853a1220400a7987bc9c66f9b4f3
   __TEXT.__const: 0xa80 sha256:63c8191d75a06e76bb5a1dc5f81e239f9d1063bd90ece89e234481439c69d5b8
   __TEXT.__binname: 0x40 sha256:bf394488bb180fc4f92c321ab93142f5f89d4c5db48c5dc23b10df2147e8cc06
   __TEXT.__chain_starts: 0x24 sha256:5fd465bdb02cb78c99c9e28360e580ee08c868d6e85ab4d384c856b07862a8c8
-  __DATA_CONST.__const: 0x5c98 sha256:7ee5c2cef4f924695c96dafab338c9768be730d0aa535a86e833fc5f6fc9d444
-  __LATE_CONST.__late_const: 0x7c270 sha256:65c48ca16bfbd1e8b846394af073cd0fcc8c5799c3bd624d030abbc491ae21c7
-  __TEXT_EXEC.__text: 0x5e434 sha256:4606e59d109ca366ac8aee46d8b0b4debc7f22d4ce903e001f25e4c8f90ba8c8
+  __DATA_CONST.__const: 0x5ca8 sha256:5218b211c61fa060dfea6579fc5a99ad983752788d4c2ae40a7b1b89f1cd2c64
+  __LATE_CONST.__late_const: 0x7c270 sha256:5a759c46c19abaa9b35334ba90e8d529400bd8041857d0211cbb3c301d816d8d
+  __TEXT_EXEC.__text: 0x5ec1c sha256:261c63cfd037cbd6a17aeee2a6e078318c44b0b2a721c02c19f609fb0fb1738e
   __LAST.__pinst: 0x8 sha256:fbfe010a65f336a0c74a09adf932e560cbf8dd3dc61641cea7abbff4f544861d
   __DATA.__data: 0xf sha256:19e4507360b4447be5d0e175ca4c36014495cca39af824ef7eb39a42e51890dc
   __DATA.__auth_ptr: 0x18 sha256:46531ea1ff34d23e2a957f72eaa40a98bf65232b9fdb5570bf5882a71d9bebef
   __DATA.__bss: 0x60a8 sha256:1fb054d6fb6753955be0031a1fda9d77d3af0de3bc4ec8f1ec6479b381d22067
   __DATA.__common: 0xdf08 sha256:8ce4472637d541d8c848132d7a65df97f8723f4f1d502510e425d2a6a2cf745e
   __BOOTDATA.__data: 0x14000 sha256:fa569e2360c540e6280e34a4627516770f1a5f34d81d35689334a99cc1013357
-  UUID: 0AD32C12-C9A4-332D-BAB5-C07362340975
-  Functions: 392
+  UUID: 91299325-144D-365A-B208-D8B72097D120
+  Functions: 393
   Symbols:   1
-  CStrings:  2307
+  CStrings:  2317
 
CStrings:
+ "%s: assert '!__builtin_add_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed."
+ "%s: assert '!__builtin_sub_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed."
+ "%s: assert 'cluster_id < CPUTRACE_NB_CLUSTERS' failed."
+ "%s: cluster not deinitialized before hibernating."
+ "%s: clusters not deinitialized before hibernating."
+ "/AppleInternal/Library/BuildRoots/4~CRUeugDIK4eOLf30Xwh36nnbfOceSDQBVwzqu7U/Library/Caches/com.apple.xbs/TemporaryDirectory.ByRYwX/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
+ "/AppleInternal/Library/BuildRoots/4~CRUeugDIK4eOLf30Xwh36nnbfOceSDQBVwzqu7U/Library/Caches/com.apple.xbs/TemporaryDirectory.ByRYwX/Sources/SPTM/sptm/core/sptm_hibentry.c"
+ "/AppleInternal/Library/BuildRoots/4~CRUeugDIK4eOLf30Xwh36nnbfOceSDQBVwzqu7U/Library/Caches/com.apple.xbs/TemporaryDirectory.ByRYwX/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
+ "SPTM-611.160.16|2026-06-07:19:25:24.062696|"
+ "VIOLATION_CPUTRACE_VA_DEINITIALIZED"
+ "VIOLATION_CPUTRACE_VA_INITIALIZED"
+ "cputrace_get_cluster_id()"
+ "cputrace_instance->initialized_count"
+ "relaxed-rw-protections"
+ "sptm_cputrace_hib_wake"
- "%s: assert 'cluster_id <= MAX_CPU_CLUSTER_PHY_ID' failed."
- "/AppleInternal/Library/BuildRoots/4~CPlGugBQ_BEw-3nzXHfBG4bBswGmGo-_CYIFZRs/Library/Caches/com.apple.xbs/TemporaryDirectory.WaEX5G/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
- "/AppleInternal/Library/BuildRoots/4~CPlGugBQ_BEw-3nzXHfBG4bBswGmGo-_CYIFZRs/Library/Caches/com.apple.xbs/TemporaryDirectory.WaEX5G/Sources/SPTM/sptm/core/sptm_hibentry.c"
- "/AppleInternal/Library/BuildRoots/4~CPlGugBQ_BEw-3nzXHfBG4bBswGmGo-_CYIFZRs/Library/Caches/com.apple.xbs/TemporaryDirectory.WaEX5G/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
- "SPTM-611.160.8|2026-05-15:01:15:02.481544|"

```
