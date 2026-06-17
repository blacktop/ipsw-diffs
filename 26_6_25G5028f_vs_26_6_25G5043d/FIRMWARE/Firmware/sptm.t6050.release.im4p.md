## sptm.t6050.release.im4p

> `Firmware/sptm.t6050.release.im4p`

```diff

-611.160.8.0.0
-  __TEXT.__cstring: 0x1249c sha256:b7adee51a9e2a5371cbc563655201729bef9f725cc8f074aa978c88bd47dd688
+611.160.16.0.0
+  __TEXT.__cstring: 0x126ac sha256:415f1a9133af9b4bae6424a3ae38eb4754a22b7f96830251b0ea38ff04a92824
   __TEXT.__const: 0xa80 sha256:7caf49c55f8a00b8df12aba18a1274b6f69a0bf0de69a8a40b7c583e85bbbf27
   __TEXT.__binname: 0x40 sha256:f65bbd583dea47b6aab7b9750542bbdfa465d789ea296a6dd87d2a925286ca12
   __TEXT.__chain_starts: 0x24 sha256:5fd465bdb02cb78c99c9e28360e580ee08c868d6e85ab4d384c856b07862a8c8
-  __DATA_CONST.__const: 0x5c98 sha256:9fafc3dd2192c8976bf3ef2820081f7a16a95535e4f8fb16de380e2036a6cfcb
-  __LATE_CONST.__late_const: 0x7c5b0 sha256:01ad1a476be6f50efb4e46df1c0b8183228c97b2fd48b4bb037216ad214bb785
-  __TEXT_EXEC.__text: 0x5e460 sha256:abb2fde4805c234c2a0d007030e5796f52ba70b09f51cc0536539e3cb7efcb95
+  __DATA_CONST.__const: 0x5ca8 sha256:694d41998fb2efc66e9f0d0f36668d93c7210d24d232c04fe3b5c0d6853e7861
+  __LATE_CONST.__late_const: 0x7c5b0 sha256:175b56e99d08fc5db15a0d74e6ef6f6e3d7a4eb0b02195f9263992f22ff29240
+  __TEXT_EXEC.__text: 0x5ed00 sha256:a6aba334b42b7ae634f41a7e7963ef25ebe05055969af1ae250e554c37937d45
   __LAST.__pinst: 0x8 sha256:fbfe010a65f336a0c74a09adf932e560cbf8dd3dc61641cea7abbff4f544861d
   __DATA.__data: 0xf sha256:19e4507360b4447be5d0e175ca4c36014495cca39af824ef7eb39a42e51890dc
   __DATA.__auth_ptr: 0x18 sha256:46531ea1ff34d23e2a957f72eaa40a98bf65232b9fdb5570bf5882a71d9bebef
   __DATA.__bss: 0x60a8 sha256:1fb054d6fb6753955be0031a1fda9d77d3af0de3bc4ec8f1ec6479b381d22067
   __DATA.__common: 0x32188 sha256:069c5fba3cee107b78c33e54b0ccea723f677ecabbbf010a640bc3a5602bea0f
   __BOOTDATA.__data: 0x14000 sha256:fa569e2360c540e6280e34a4627516770f1a5f34d81d35689334a99cc1013357
-  UUID: 0A2801A3-D09A-3CAA-8704-4BA84E2985D8
-  Functions: 392
+  UUID: C7963074-2A37-3E31-803F-D086A9FD11FC
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
