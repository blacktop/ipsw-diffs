## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-589.0.19.0.0
-  __TEXT.__text: 0x16084
+589.40.11.0.0
+  __TEXT.__text: 0x1612c
   __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x18b7
-  __TEXT.__oslogstring: 0x2a14
+  __TEXT.__cstring: 0x18b8
+  __TEXT.__oslogstring: 0x2a4f
   __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__unwind_info: 0x4c0
   __TEXT.__objc_classname: 0xcd
-  __TEXT.__objc_methname: 0xaa0
-  __TEXT.__objc_methtype: 0x19b
+  __TEXT.__objc_methname: 0xab9
+  __TEXT.__objc_methtype: 0x19e
   __TEXT.__objc_stubs: 0xa20
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0xb38
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x320
+  __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0x258

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B94852E3-FE4E-3EC9-9490-ACB3FCC47AD2
+  UUID: FE356480-207F-365E-9AC8-B06C3CC5A495
   Functions: 418
   Symbols:   1336
-  CStrings:  735
+  CStrings:  737
 
Symbols:
+ -[CollationCore initWithID:queue:]
+ -[CollationCore initWithXPC:queue:]
+ ___35-[CollationCore initWithXPC:queue:]_block_invoke
+ _objc_msgSend$initWithID:queue:
- -[CollationCore initWithID:]
- -[CollationCore initWithXPC:]
- ___29-[CollationCore initWithXPC:]_block_invoke
- _objc_msgSend$initWithID:
Functions:
~ _cryptex_core_get_nonce_domain : 424 -> 520
~ -[CollationCore initWithID:] -> -[CollationCore initWithID:queue:] : 296 -> 324
~ -[CollationCore initWithXPC:] -> -[CollationCore initWithXPC:queue:] : 224 -> 248
~ __cryptex_magister_init : 1648 -> 1656
~ __cryptex_scrivener_init : 2076 -> 2088
CStrings:
+ "%{public}s: No such nonce domain exists.: %{darwin.errno}d"
+ "589.40.11"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Sun Sep  7 21:48:48 PDT 2025; root:libcryptex-589.40.11~64/libcryptex_core/RELEASE_ARM64E"
+ "@28@0:8I16@20"
+ "Darwin Cryptex Core Interface Version 2.0.0: Sun Sep  7 21:48:48 PDT 2025; root:libcryptex-589.40.11~64/libcryptex_core/RELEASE_ARM64E"
+ "initWithID:queue:"
+ "initWithXPC:queue:"
- "589.0.19"
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Sun Aug  3 00:09:45 PDT 2025; root:libcryptex-589.0.19~475/libcryptex_core/RELEASE_ARM64E"
- "@20@0:8I16"
- "Darwin Cryptex Core Interface Version 2.0.0: Sun Aug  3 00:09:45 PDT 2025; root:libcryptex-589.0.19~475/libcryptex_core/RELEASE_ARM64E"
- "initWithID:"

```
