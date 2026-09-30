## LocationLogEncryption

> `/System/Library/PrivateFrameworks/LocationLogEncryption.framework/LocationLogEncryption`

```diff

-3068.0.15.0.0
-  __TEXT.__text: 0x1f7c
-  __TEXT.__auth_stubs: 0x3b0
+3072.0.40.0.1
+  __TEXT.__text: 0x2120
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x94
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x224
-  __TEXT.__cstring: 0x1ee
-  __TEXT.__oslogstring: 0x4a5
+  __TEXT.__gcc_except_tab: 0x228
+  __TEXT.__cstring: 0x22d
+  __TEXT.__oslogstring: 0x53f
   __TEXT.__unwind_info: 0x110
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x2a3

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1e8
+  __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCB00CEF-356E-34D4-BB1A-2C97C306A471
+  UUID: 89906593-AD45-3480-8966-8F60AE7764D8
   Functions: 23
-  Symbols:   82
-  CStrings:  92
+  Symbols:   83
+  CStrings:  94
 
Symbols:
+ _objc_release_x9
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_release_x26
- _objc_retain_x2
- _objc_retain_x8
- _objc_storeStrong
Functions:
~ _LocationLogEncryptionKeyStoreDirPathForTime : 212 -> 216
~ _LocationLogEncryptionClearObsoleteKeys : 1216 -> 1236
~ _LocationLogEncryptionSetDisabled : 84 -> 460
~ _LocationLogEncryptionDataSize : 176 -> 192
~ sub_25a4bfe2c -> sub_25f6c7fcc : 684 -> 680
~ sub_25a4c00d8 -> sub_25f6c8274 : 1772 -> 1792
~ sub_25a4c07c8 -> sub_25f6c8978 : 432 -> 420
CStrings:
+ "/Library/Caches/com.apple.xbs/981DCE78-4EF2-43A1-B581-257023D8E82E/TemporaryDirectory.86TLii/Sources/CoreLocationFramework/Framework/LocationLogEncryption/LocationLogEncryption.mm"
+ "Location log encryption is disabled, locations will be unredacted"
+ "Location log encryption is not available on customer builds, locations will be redacted"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/LocationLogEncryption/LocationLogEncryption.mm"

```
