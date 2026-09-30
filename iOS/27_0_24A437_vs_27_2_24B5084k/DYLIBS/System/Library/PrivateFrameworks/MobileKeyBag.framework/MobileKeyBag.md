## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-697.0.6.0.0
-  __TEXT.__text: 0x16180
+697.40.4.0.0
+  __TEXT.__text: 0x162c0
   __TEXT.__objc_methlist: 0x544
-  __TEXT.__cstring: 0x5f24
+  __TEXT.__cstring: 0x5fc3
   __TEXT.__const: 0x478
   __TEXT.__oslogstring: 0xec
   __TEXT.__gcc_except_tab: 0x5a4

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x3de0
+  __AUTH_CONST.__cfstring: 0x3e40
   __AUTH_CONST.__objc_const: 0x2e8
-  __AUTH_CONST.__auth_got: 0x8a0
+  __AUTH_CONST.__auth_got: 0x8a8
   __DATA.__data: 0x2e0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 543
-  Symbols:   1054
-  CStrings:  774
+  Symbols:   1055
+  CStrings:  777
 
Symbols:
+ _objc_release_x9
Functions:
~ _MKBCopyCryptoIDKeysForFileDescriptor : 2216 -> 2492
~ __MKBBackupCheckKey : 396 -> 440
CStrings:
+ "backup key from db too large (%zu > %zu), ignoring"
+ "entry overruns blob offset=%zu keysize=%u blob_size=%zu"
+ "got oversized key (%u > %zu) for crypto id 0x%016qx"
+ "wrapped key size too big (%u>%zu)"
- "wrapped key size too big (%lu>%u)"
```
