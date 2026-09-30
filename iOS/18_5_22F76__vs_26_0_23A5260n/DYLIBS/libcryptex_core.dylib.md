## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-493.122.1.0.0
-  __TEXT.__text: 0x15e60
-  __TEXT.__auth_stubs: 0xdf0
+589.0.1.0.0
+  __TEXT.__text: 0x16054
+  __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x18b6
-  __TEXT.__oslogstring: 0x29a6
+  __TEXT.__cstring: 0x18b4
+  __TEXT.__oslogstring: 0x2a14
   __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__unwind_info: 0x4b8
   __TEXT.__objc_classname: 0xcd

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x320
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0x258
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xab0

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B40EBE57-2FF9-3BC6-804E-75C382ED40FA
-  Functions: 416
-  Symbols:   1337
-  CStrings:  732
+  UUID: 8D686415-7A31-398C-A489-6FD6F28D567B
+  Functions: 417
+  Symbols:   1335
+  CStrings:  735
 
Symbols:
+ _AMAuthInstallSsoSetToken
+ _cryptex_scrivener_set_auth_token
Functions:
+ sub_223b11060
- sub_21c8727bc
~ __cryptex_scrivener_dealloc : 144 -> 156
+ _cryptex_scrivener_set_auth_token
~ __cryptex_scrivener_init_tss_common : 1376 -> 1520
CStrings:
+ "%{public}s: AMAuthInstallSsoSetToken: [%d] %{public}s"
+ "%{public}s: empty auth token"
+ "%{public}s: set auth token"
+ "589.0.1"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Fri May 23 06:17:54 PDT 2025; root:libcryptex-589.0.1~224/libcryptex_core/RELEASE_ARM64E"
+ "Darwin Cryptex Core Interface Version 2.0.0: Fri May 23 06:17:54 PDT 2025; root:libcryptex-589.0.1~224/libcryptex_core/RELEASE_ARM64E"
- "493.122.1"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Sat Apr 19 07:20:18 PDT 2025; root:libcryptex-493.122.1~1/libcryptex_core/RELEASE_ARM64E"
- "Darwin Cryptex Core Interface Version 2.0.0: Sat Apr 19 07:20:18 PDT 2025; root:libcryptex-493.122.1~1/libcryptex_core/RELEASE_ARM64E"

```
