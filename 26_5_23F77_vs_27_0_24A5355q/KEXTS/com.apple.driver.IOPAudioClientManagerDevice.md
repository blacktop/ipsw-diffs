## com.apple.driver.IOPAudioClientManagerDevice

> `com.apple.driver.IOPAudioClientManagerDevice`

```diff

-340.3.0.0.0
+400.34.0.0.0
   __TEXT.__const: 0x8 sha256:3e990d45c83fa01d9bf0c64b79ed7678df3c723614f0f7eccdc3d196fa3073e9
-  __TEXT.__cstring: 0xdc6 sha256:761d7b6fd26fd52dec0d217fcf996a329a85d5c7027911b8951b24e10f2fed24
+  __TEXT.__cstring: 0xd8c sha256:d39a2d9156c7bbbe37ba1440b2cc43db8f00c9a29ba10edd93673cc7092fb5e1
   __TEXT.__os_log: 0x986 sha256:78b8df44fe5a373d456596f12f49fd2c774e4515f02b479fe248deff00d359a3
-  __TEXT_EXEC.__text: 0x4114 sha256:8e8eda44b18181513d7f0aadd8f5159e089eb087498675af75637c01363b0534
+  __TEXT_EXEC.__text: 0x416c sha256:52bc883822a15ba6aded62dec0d7cd6235b0d079d1ec4fdb80bbc4ff133a1926
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:f7453419f8a09a6522e47cecd77588b3a2384b49c1abb3612e16644f54529f2f
+  __DATA.__data: 0xc8 sha256:abfe5670edf0a76dd4215dec5cf3f7a32e110b824f5d73efe7c443bcb9554ff6
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__auth_got: 0x88 sha256:1370ed6129b913b17810e54cda9a2d67b3cbd12c2876f771269f3608ad122655
-  __DATA_CONST.__got: 0x48 sha256:7df88214e8870344aa1bf0e970bd41a721fe5daf5e54b8df72dcd269d6a8dd15
-  __DATA_CONST.__mod_init_func: 0x10 sha256:83337ef75f73320cedd35cf6d08568029efa95402d26bb3094bfbde16239d14f
-  __DATA_CONST.__mod_term_func: 0x10 sha256:792a63f1f7e873672391cc9611571095b01ec22fcbce37c0f1026b367473fc56
-  __DATA_CONST.__const: 0xef8 sha256:aa221a66a325084de677f4387490c4b56890428e1504ee8632e29d046f4c69c5
-  __DATA_CONST.__kalloc_type: 0x80 sha256:323b993a24f21d1a81ccbf15a17ed324f965c8abd8de00302e7dacb1d8d01550
-  UUID: AB806C5C-048C-387F-8E46-8CD383AEDC37
-  Functions: 162
+  __DATA_CONST.__mod_init_func: 0x10 sha256:12d9bac6e51de486af7dedbe19c2803064614a74caa786e2c99dd9406b547731
+  __DATA_CONST.__mod_term_func: 0x10 sha256:fce9ca9d5bb0187a491a63185365049ceace970b7811da3cb12e891524894034
+  __DATA_CONST.__const: 0xf00 sha256:216049edac92c95c155bcd72303accd8a8701c59a0b1c6cc41a577a94b86f317
+  __DATA_CONST.__kalloc_type: 0x80 sha256:67fbe75ff567f68d6bae9e53e361eb7b3d1aa6105ba3707e66f95c8a6e659a0a
+  __DATA_CONST.__auth_got: 0x88 sha256:e94e8a9e4891668468304269c1eb7fc90312e001fdaf5117f32e7f43a3ac0fa1
+  __DATA_CONST.__got: 0x48 sha256:147c0469da2dfc83f373e6b56bffefd6043c28656ec2992ecfb9cbd43b152b0a
+  UUID: 96BF284C-62E8-35BB-93A4-D0AFB6658FE2
+  Functions: 163
   Symbols:   0
   CStrings:  73
 
CStrings:
+ "ret = _enableClientManagerPowerRequest(inEnable, inDirection) == 0 "
- "ret = setClientManagerPowerRequest({ .state = mClientManagerDeviceConfig.targetPowerState, .direction = inDirection, }) == 0 "

```
