## com.apple.iokit.IOSurface

> `com.apple.iokit.IOSurface`

```diff

-393.5.7.0.0
-  __TEXT.__cstring: 0x2e7a sha256:3d2907d5b61cfa8001f846f5933debddc299a0afda48ec13db4f6a0390424fef
+393.5.8.0.0
+  __TEXT.__cstring: 0x2f23 sha256:cdcf4fa7e8b673969eb56cb69dd58d7478de12138cdf0e7232b4f8687fa581ad
   __TEXT.__const: 0x40 sha256:cf37b0e3127b6c290acea7a2db6c4018053cf7d348bd26001ce799cee936d67b
-  __TEXT.__os_log: 0x2fa6 sha256:c903e2a94f1c75f9d4d21743a95e4dd9194c65a073d937b868497c9016bdd438
-  __TEXT_EXEC.__text: 0x2eef4 sha256:ca146c80f08d3ee943efbb459d3f4c18942647bc47953087eb604048bb40ae51
+  __TEXT.__os_log: 0x3029 sha256:64522883903b6cbb0bd3c28c1208fdd256b99ed1f4a0c20279c31496bb287bbf
+  __TEXT_EXEC.__text: 0x2efc4 sha256:21e2565b9651a56deb70898eeca88db34270b029c389813757ff9080a0f2f3ad
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x178 sha256:2d9c5b8f10f54ffa6f1d19a1224d9add14814a5243fc3c1463db26b2459e0409
+  __DATA.__data: 0x178 sha256:176be9b7d9f4d571ba8f544276d305fc03a0be34ef5f61f88d9d7b02b3780abe
   __DATA.__common: 0x410 sha256:256fb9c4796b15a7ec4b0d5319e9e493ca4cffda658310420bdfd31e1c59da79
   __DATA.__bss: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__auth_got: 0x480 sha256:69a6146b5a24282b474fc7c181262e5e91550190185ec31f07f258e20741cede
-  __DATA_CONST.__got: 0xd0 sha256:6d58dd1d9b87f5254c1ad51f7802d2447904b20249ff1b4d215e89c7273c38f0
-  __DATA_CONST.__mod_init_func: 0x80 sha256:9204ef890f1a05a4e6992f3e479d94ea66c7d570cccea9c6612a09f1cd0ed85d
-  __DATA_CONST.__mod_term_func: 0x80 sha256:e0d43d7c8b5ad96ee1a8dbfd621dcd4131a26aac2d07a07784dc22b4a39973fa
-  __DATA_CONST.__const: 0x4300 sha256:a42ab8f8aa15a40f3e6de8bc844a70c89f698d59a55d86f17862090755482d1a
-  __DATA_CONST.__kalloc_type: 0xbc0 sha256:74463220219f8e1d56b403df1c5536c4e61be65f8f47fdddcf25e3685ead5469
-  __DATA_CONST.__kalloc_var: 0x960 sha256:c3eebf048c6d044e67f09075b50db503ee9399b536d981924c4f6a7fe0c0c199
-  UUID: A0CFC976-7961-337F-AA3F-B9851AE06069
+  __DATA_CONST.__auth_got: 0x480 sha256:2c3c205092df93dba5abbfdb490f44eb55d96722922b9c3e7ff23c7c5e997225
+  __DATA_CONST.__got: 0xd0 sha256:f2d3564a4202bb437bbfa77cee3b9514636f1b7cc3692dd0edf123546f042fcd
+  __DATA_CONST.__mod_init_func: 0x80 sha256:d1faa86ea388dfc0891bc1da8f9b0de938d5bebeb13407f296c10e4a2af3d509
+  __DATA_CONST.__mod_term_func: 0x80 sha256:3ab03a07482cc3ef3aa40dd255239c56210bc5410e3a4c7d9265dcaa9a255fff
+  __DATA_CONST.__const: 0x4300 sha256:820065b9ae3c79825733f59d56e0c45915f64c4dc35d2affa7fe6cfc48d27227
+  __DATA_CONST.__kalloc_type: 0xbc0 sha256:c8cd58456675a7337d046fb410424514489ed273648e8a5ae6ed6a5e9e5e9b23
+  __DATA_CONST.__kalloc_var: 0x960 sha256:79a7d87a2503fa8eae64bd8a7ec9cc726fb6f51af31f1a040571c09934db429b
+  UUID: A05D8E4F-432B-3E4F-9138-BFC95E4CB3EC
   Functions: 1257
   Symbols:   0
-  CStrings:  578
+  CStrings:  583
 
CStrings:
+ "%s pool off limits for poolId 0x%llX"
+ "====> %s:%d IOSurfaceMemoryPool: %s (%d) can't access pool id %llu (wrong entitlements)\n"
+ "====> %s:%d IOSurfaceMemoryPool: %s (%d) invalid task (%p) can't access pool id %llu (wrong entitlements)\n"
+ "IOSurfaceMemoryPool: %s (%d) invalid task (%p) can't access pool id %llu (wrong entitlements)"
+ "newWiredMemoryDescriptorWithLength"
+ "taskCanUsePool"
- "IOSurfaceMemoryPool: %s (%d) can't access pool id %llu (wrong entitlements)\n"

```
