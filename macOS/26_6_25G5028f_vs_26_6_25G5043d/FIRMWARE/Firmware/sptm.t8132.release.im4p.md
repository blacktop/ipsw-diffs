## sptm.t8132.release.im4p

> `Firmware/sptm.t8132.release.im4p`

```diff

-611.160.8.0.0
-  __TEXT.__cstring: 0x1207d sha256:2e1ab64617e133c91d6bfdf7f60e7515df7a4656e2f45b157d1f3bd9280804ad
+611.160.16.0.0
+  __TEXT.__cstring: 0x1228d sha256:d745264d0f723d6671abb1facf752e32016d8c186be223c71ec01c439fa7cd54
   __TEXT.__const: 0xa80 sha256:63c8191d75a06e76bb5a1dc5f81e239f9d1063bd90ece89e234481439c69d5b8
   __TEXT.__binname: 0x40 sha256:f085ea18ad1a1f286ffb97ed5e8837dca16f6b646eb46ab36441b587554af4fc
   __TEXT.__chain_starts: 0x24 sha256:5fd465bdb02cb78c99c9e28360e580ee08c868d6e85ab4d384c856b07862a8c8
-  __DATA_CONST.__const: 0x5c98 sha256:79e44ca2baf89f8e1a27cc7c74a2c961644acab7d56e4a7f2bcc5dcf3bdcc0ac
-  __LATE_CONST.__late_const: 0x7c260 sha256:78b4c8ace3d5a31172fa3cb4e8bb0053d9572e7cd50777b33d4335af44bf8d45
-  __TEXT_EXEC.__text: 0x5d1b4 sha256:7ac0c41e6794af3b8e4f662d0f893552187bad1a4064e1de8ee449c517d265bb
+  __DATA_CONST.__const: 0x5ca8 sha256:0bbcfaac4bed4ca315c6f4fd0419aff771ba782223875449c1ae7608ca27a072
+  __LATE_CONST.__late_const: 0x7c260 sha256:1e69109cc7982fac4a10035b7b6b113b08e4a692b3fae5d2a04561a1f17e3e95
+  __TEXT_EXEC.__text: 0x5d8c8 sha256:3fda4ffb1536dc3d1c99de213ef6fc44400028cd25e4d39f39084ca77827bc71
   __LAST.__pinst: 0x8 sha256:fbfe010a65f336a0c74a09adf932e560cbf8dd3dc61641cea7abbff4f544861d
   __DATA.__data: 0xf sha256:19e4507360b4447be5d0e175ca4c36014495cca39af824ef7eb39a42e51890dc
   __DATA.__auth_ptr: 0x18 sha256:46531ea1ff34d23e2a957f72eaa40a98bf65232b9fdb5570bf5882a71d9bebef
   __DATA.__bss: 0x60a8 sha256:1fb054d6fb6753955be0031a1fda9d77d3af0de3bc4ec8f1ec6479b381d22067
   __DATA.__common: 0xd288 sha256:92bc0b37693065e53578ef6906a430f8357b478d159d134447a5202bd5565067
   __BOOTDATA.__data: 0x14000 sha256:fa569e2360c540e6280e34a4627516770f1a5f34d81d35689334a99cc1013357
-  UUID: 3E4029A5-57C1-3122-9595-3AE6C2FCC382
-  Functions: 383
+  UUID: 36395319-6C2D-39A1-91A6-FF77AADEC350
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
