## securityuploadd

> `/usr/libexec/securityuploadd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x14b54
+62460.0.55.0.1
+  __TEXT.__text: 0x149f0
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_stubs: 0x1fe0
-  __TEXT.__objc_methlist: 0x920
+  __TEXT.__objc_stubs: 0x2060
+  __TEXT.__objc_methlist: 0x910
   __TEXT.__const: 0x350
   __TEXT.__objc_classname: 0x14b
-  __TEXT.__objc_methname: 0x2407
+  __TEXT.__objc_methname: 0x244b
   __TEXT.__objc_methtype: 0x5ed
   __TEXT.__constg_swiftt: 0x1a0
   __TEXT.__swift5_typeref: 0x18f
   __TEXT.__swift5_reflstr: 0xa2
   __TEXT.__swift5_fieldmd: 0xfc
-  __TEXT.__oslogstring: 0x100a
+  __TEXT.__oslogstring: 0xf93
   __TEXT.__swift5_capture: 0xf0
-  __TEXT.__cstring: 0xef7
+  __TEXT.__cstring: 0xf32
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__unwind_info: 0x448
   __TEXT.__eh_frame: 0x180
   __DATA_CONST.__const: 0xd58
-  __DATA_CONST.__cfstring: 0x14a0
+  __DATA_CONST.__cfstring: 0x14e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__got: 0x358
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA.__objc_const: 0xe40
-  __DATA.__objc_selrefs: 0xa58
+  __DATA.__objc_const: 0xe38
+  __DATA.__objc_selrefs: 0xa78
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x330
   __DATA.__data: 0x4a0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 366
-  Symbols:   369
-  CStrings:  784
+  Functions: 363
+  Symbols:   375
+  CStrings:  789
 
Symbols:
+ _NSCocoaErrorDomain
+ _NSFileGroupOwnerAccountID
+ _NSFileOwnerAccountID
+ _NSFilePosixPermissions
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_NSConstantDictionary
CStrings:
+ "62460.0.55.0.1"
+ "ValidCacheFiles"
+ "domain"
+ "failed to fix trustd file permissions"
+ "failed to set attributes on %s: %s"
+ "firstObject"
+ "fixTrustdPermissions:"
+ "numberWithUnsignedShort:"
+ "protected trustd directory unavailable"
+ "setAttributes:ofItemAtPath:error:"
+ "unsignedShortValue"
+ "valid.sqlite3-journal"
+ "valid.sqlite3-shm"
+ "valid.sqlite3-wal"
- ".valid_replace"
- "62460.0.38.0.1"
- "Client (pid: %d) properly entitled for trustd file helper interface, let's go"
- "changeOwnerOfValidFile:error:"
- "com.apple.private.trustd.FileHelp"
- "failed to change owner of %s: %s"
- "failed to fix Valid permissions for trustd"
- "fixValidPermissions:"
- "trustd/%@"
```
