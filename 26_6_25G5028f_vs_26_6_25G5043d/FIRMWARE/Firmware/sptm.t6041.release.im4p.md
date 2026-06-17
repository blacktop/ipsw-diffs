## sptm.t6041.release.im4p

> `Firmware/sptm.t6041.release.im4p`

```diff

-611.160.8.0.0
-  __TEXT.__cstring: 0x1207a sha256:6f805ba90c97e82710f1bc0c34beddc2cdf39eadf13433377cfc862fbc3fec28
+611.160.16.0.0
+  __TEXT.__cstring: 0x1228a sha256:d5deb48cb31328c622c66ef10086377bd9faad59e8ea686b24ea04f7d99e9347
   __TEXT.__const: 0xa80 sha256:8c19d722ee5b7dfa1999e59f76ad535c29bcef2544747e3477e6f6b343b84643
   __TEXT.__binname: 0x40 sha256:a37cc4ec7f9766910bfd0f7654e20cc6c0afa1b3131bb175df9ea47b6b06abb7
   __TEXT.__chain_starts: 0x24 sha256:5fd465bdb02cb78c99c9e28360e580ee08c868d6e85ab4d384c856b07862a8c8
-  __DATA_CONST.__const: 0x5c98 sha256:18de89ab66c7c246310ee489a1b649c6dd41a9c5ccfa60cbdd450aedac447eab
-  __LATE_CONST.__late_const: 0x7c320 sha256:0ceda0a43b30ab86f5e4b164c1b019bae15fe7af4d6e4f9877ea0f6431ddee31
-  __TEXT_EXEC.__text: 0x5d1b4 sha256:85b56908a084a68f33e01e7e062bd695839cbc3c6b1b557338b95f5745420dff
+  __DATA_CONST.__const: 0x5ca8 sha256:19dc6ce291e0679614f333bb8ecd20fdc651fd61ae1688eff17f7e530359344e
+  __LATE_CONST.__late_const: 0x7c320 sha256:f210743e8e6dff48426037e2888597776316374f9eb11a2cd3eae501ced8470c
+  __TEXT_EXEC.__text: 0x5d8d4 sha256:12f90332cc189d3758a06d8eee8154cb28191fcb906ee1f8b0d4b71df568451f
   __LAST.__pinst: 0x8 sha256:fbfe010a65f336a0c74a09adf932e560cbf8dd3dc61641cea7abbff4f544861d
   __DATA.__data: 0xf sha256:19e4507360b4447be5d0e175ca4c36014495cca39af824ef7eb39a42e51890dc
   __DATA.__auth_ptr: 0x18 sha256:46531ea1ff34d23e2a957f72eaa40a98bf65232b9fdb5570bf5882a71d9bebef
   __DATA.__bss: 0x60a8 sha256:1fb054d6fb6753955be0031a1fda9d77d3af0de3bc4ec8f1ec6479b381d22067
   __DATA.__common: 0x15088 sha256:ec1438edde9f02cc55f63cf8ebbd039ce233c38c74141db90070e916fdc82266
   __BOOTDATA.__data: 0x14000 sha256:fa569e2360c540e6280e34a4627516770f1a5f34d81d35689334a99cc1013357
-  UUID: 61532BD6-7E62-32B0-88A7-585343E920FE
-  Functions: 383
+  UUID: 09B05FB5-9664-3E67-8992-114BDE73C33C
+  Functions: 384
   Symbols:   1
-  CStrings:  2274
+  CStrings:  2284
 
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
