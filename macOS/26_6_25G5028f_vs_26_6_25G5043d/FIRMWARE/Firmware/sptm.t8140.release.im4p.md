## sptm.t8140.release.im4p

> `Firmware/sptm.t8140.release.im4p`

```diff

-611.160.8.0.0
-  __TEXT.__cstring: 0x1207c sha256:f662a92cbd9a73bf0a65d651fe4567f155b73aea57713e0b038c755d318dc4e0
+611.160.16.0.0
+  __TEXT.__cstring: 0x1228c sha256:7cb710714a5826c61d8c85c66ae83fb8ea21aa534823a09634fb066e22c9ad6a
   __TEXT.__const: 0xa80 sha256:834654feaa80d7c930fe28ebfe3e6b0cb59f6751524c35e25bf1e070cb084afb
   __TEXT.__binname: 0x40 sha256:d2a04d8c22f15df03fb0f904a3f74a431ab71f38675a747d7bcdfd72cbffb719
   __TEXT.__chain_starts: 0x24 sha256:5fd465bdb02cb78c99c9e28360e580ee08c868d6e85ab4d384c856b07862a8c8
-  __DATA_CONST.__const: 0x5c98 sha256:bdf2dc1063e2c033b1a5e592e86fa41985a0599447b904440ddde46f824d685d
-  __LATE_CONST.__late_const: 0x7c1e0 sha256:11cc9b502f895ed36082d4e15724f0c869803b50921401e684abf6b302080f63
-  __TEXT_EXEC.__text: 0x5d0f0 sha256:e16ddb3e28e42260e9c551b7c4b7020e4ba93985abcb41583dd5ffa44287990d
+  __DATA_CONST.__const: 0x5ca8 sha256:3b2ee37e87f7c7100626fbbaa8c2cabe51c20341502c0db185da22fae25bfd4d
+  __LATE_CONST.__late_const: 0x7c1e0 sha256:b4e659477133cbb9339292e469ebccf9c06669f7a6c3d1a1a0a4d90f033f4eb2
+  __TEXT_EXEC.__text: 0x5d804 sha256:32e895c360539ec7d0e1332fbcfd72afb2d5a4d160ec809a3d9bfc1678b65789
   __LAST.__pinst: 0x8 sha256:fbfe010a65f336a0c74a09adf932e560cbf8dd3dc61641cea7abbff4f544861d
   __DATA.__data: 0xf sha256:19e4507360b4447be5d0e175ca4c36014495cca39af824ef7eb39a42e51890dc
   __DATA.__auth_ptr: 0x18 sha256:46531ea1ff34d23e2a957f72eaa40a98bf65232b9fdb5570bf5882a71d9bebef
   __DATA.__bss: 0x60a8 sha256:1fb054d6fb6753955be0031a1fda9d77d3af0de3bc4ec8f1ec6479b381d22067
   __DATA.__common: 0x7e88 sha256:1473f762028c6de7d3827d2842e4f0a31700beb96197c4f618ea8bf13a02faac
   __BOOTDATA.__data: 0x14000 sha256:fa569e2360c540e6280e34a4627516770f1a5f34d81d35689334a99cc1013357
-  UUID: 3402403D-E5E2-3B6D-A6CC-1B3EA2DD3E5B
-  Functions: 383
+  UUID: AC633BE4-60D1-392D-9D09-4B1574917EF5
+  Functions: 384
   Symbols:   1
-  CStrings:  2275
+  CStrings:  2285
 
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
