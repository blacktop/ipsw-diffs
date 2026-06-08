## newfs_exfat

> `/System/Library/Filesystems/exfat.fs/newfs_exfat`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0x345c sha256:13ca8dc717707b3ed455844b35b7dd53410be74214e8cf18f639a5d7f1ecc97f
-  __TEXT.__auth_stubs: 0x380 sha256:58f3887b4e0e512aa03941dcd60fd64b1e08832ac66f5451d5bc4fdf507c864a
+560.0.0.0.0
+  __TEXT.__text: 0x353c sha256:3b01bc185c01dc6a8be34e94a71e7a783ecf5efb6f0fc8b111f555f406d4cecf
+  __TEXT.__auth_stubs: 0x380 sha256:a1c15c39d89fa750a61bf5c90e0df549153c6c833a616bfac285a42c747189b2
   __TEXT.__const: 0x4a58 sha256:b2f7529e4b859a0a3b13515ca7aad54d05ac35b27b5732a375ff04104e675be6
-  __TEXT.__cstring: 0xed0 sha256:d639a9c1f448f440c04195c3961743192a4937a20542d92327f21eb949570a09
-  __TEXT.__unwind_info: 0xd8 sha256:8133cd9c2b3012ad163bb62a22cb66e825627b797a73a030617a331237ee3a59
-  __DATA_CONST.__auth_got: 0x1c0 sha256:6c406d1ffd4f692629f26fe3e0499ac79f3057a7381612ccbc844244cb94de18
-  __DATA_CONST.__got: 0x30 sha256:2c0420205250a4ad53720da9085df77b2d8c733ca2a19dc89a707ad2a258cd80
-  __DATA_CONST.__cfstring: 0x60 sha256:ae039a15459791f4363b82f3fb6cc2ed1f1623c2456fdd54d196aab631202f39
-  __DATA.__data: 0x1ee3 sha256:4107afa5d276beb3db42893e59d8045fca1afb41fc241f37256c98cbf8683746
+  __TEXT.__cstring: 0xecf sha256:218d8511b57326096f59029ef4006f8a9ff4c6d0bddc33f770138e6b84a1275f
+  __TEXT.__unwind_info: 0xe0 sha256:1a65e93c9c8084b34be9cdff413265a8eadeab126720f6c7a35c232a0ca5f312
+  __DATA_CONST.__cfstring: 0x60 sha256:7e1004248777e54ea1ac45c624978fb5c70121abbdb9a7fd60edbc88ce7c406f
+  __DATA_CONST.__auth_got: 0x1c0 sha256:5d0c61bae70857102032c6a63ff074af428343752f96cb591743e0de2b12a64d
+  __DATA_CONST.__got: 0x30 sha256:8ff91f231141349b8c85d0fb821777afa9740783d472647dcd0034b97191d1dc
+  __DATA.__data: 0x1ee3 sha256:7aebeeee826cb527ea08e00b38f1fc040f4e6df28ff51ae9b90a9f25867c868f
   __DATA.__common: 0x68 sha256:39f37f8d1931b3bdf767e7510dd69509fbf23af1f7654933d0a4d291cbdd4418
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E59B5B36-B811-3DA7-AB48-198B30A8210B
-  Functions: 56
+  UUID: E612EF75-85E4-306A-B253-B09F05812098
+  Functions: 57
   Symbols:   65
   CStrings:  107
 
CStrings:
+ "Partition offset was not initialized, setting to default value (%d)\n"
- "Partition offset was not initialized , setting to default value (%d)\n"

```
