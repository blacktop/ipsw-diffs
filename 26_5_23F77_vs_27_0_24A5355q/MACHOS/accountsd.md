## accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

-1036.0.0.0.0
-  __TEXT.__text: 0x520 sha256:9b07aa2532ec57fa49b27013439e4865752e125dc94f963a271de4d8c2cd028f
-  __TEXT.__auth_stubs: 0x180 sha256:da660fcf98995133b97e736810af673ad535a84af92447c3a529a8ebd0788f3b
-  __TEXT.__objc_stubs: 0x300 sha256:aefea6b766ff69cf43bf7d9b09e824c2d4386be6490ab06ee78869c8e87814d7
+1116.0.0.0.0
+  __TEXT.__text: 0x468 sha256:7f4bb08bff9e2b1b7f0b553776a1fc5f19bd03233ded450af930841e0814a2bb
+  __TEXT.__auth_stubs: 0x170 sha256:f79cc5c82c0736d1e57b6804683addb3028f64dac28306353e3dc58215104b3c
+  __TEXT.__objc_stubs: 0x300 sha256:e73bc06e7f37c969c83e9a6f4ce5ed7449b1700c6381629c2afa1cd94eddd252
   __TEXT.__const: 0x10 sha256:11b2d32c5d2e465b69d40818d52512f0c252cd1c3101503c49c428172248ecb7
   __TEXT.__oslogstring: 0x6e sha256:aab9b7de2eff6065f3dba77482fc96e3fc5a0bdacb564e634b5659646793b12d
   __TEXT.__cstring: 0xaf sha256:bd6d8f506d0ec197ee5f92faf93ccc01f6518127e38645e0b57ee55c41259110
   __TEXT.__objc_methname: 0x244 sha256:44a7c0755c307b70cebc661e7025968eb2cc6f0d3d9ce6c4ffe35fd66e14323c
-  __TEXT.__unwind_info: 0x68 sha256:7fbf58dc1ffcc838badf091a361d9cee08d7c9b516d5a0bf5a68bffc8f81d804
-  __DATA_CONST.__auth_got: 0xc8 sha256:8dbb4e970afcca96d9901fb3800c860238c5a83b07da1217b50bfdbc868c48ab
-  __DATA_CONST.__got: 0x60 sha256:15842b76290202d6fdf36b7a068f3f7b611e4dc10e645b47aee4f7f63baf392e
-  __DATA_CONST.__const: 0x40 sha256:2421361ef0bb974d68fe25c9c3425b8bb7e18bcfc73c491717341035bfad0cdc
-  __DATA_CONST.__cfstring: 0xc0 sha256:3266213827f7442da2f8ce6137d0ef5916845cf8bb26a9e00d1179d6f795330c
+  __TEXT.__unwind_info: 0x68 sha256:d3e82cc78f2e29065f4ad52e8b269ed421737f01c8101423501924efe64bf1b7
+  __DATA_CONST.__const: 0x40 sha256:ad0093435afd9e4e4985fc353ce406b4f0ef5746f2136fef7df07e0061079def
+  __DATA_CONST.__cfstring: 0xc0 sha256:f9f5dc2b0e7593bff681b735509bcbb4e9c600de446b957a6f968f6aa573bd35
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0xc0 sha256:a5865b8f43ef3f68aa89ef0d47b62dcea3fcc550a6278d9449e013c3bc457f30
+  __DATA_CONST.__linkguard: 0x1d sha256:8f315ce7a5d6d63e12d4b09b18c2d94a7158e88edc826dad0b706f7924c238da
+  __DATA_CONST.__auth_got: 0xc0 sha256:b0f87904057e6acb1ff054ee5f9a9c4657e974874a34f18a4668a6878bcc5c71
+  __DATA_CONST.__got: 0x58 sha256:d93eb427347c585b07a6006663de1df8c310fc690ae5efbf09911af261167821
+  __DATA.__objc_selrefs: 0xc0 sha256:3a73bc9a20436d0c42c4d9ab774bffda7c3f074d702d2cb490134b9a86833c9f
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99E60291-1080-375C-9C1F-D8A96584E7BA
-  Functions: 5
-  Symbols:   41
+  UUID: 0CC2CE75-F0C2-30F3-B62B-6ED70431304A
+  Functions: 4
+  Symbols:   40
   CStrings:  40
 
Symbols:
+ __linkguard_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19

```
