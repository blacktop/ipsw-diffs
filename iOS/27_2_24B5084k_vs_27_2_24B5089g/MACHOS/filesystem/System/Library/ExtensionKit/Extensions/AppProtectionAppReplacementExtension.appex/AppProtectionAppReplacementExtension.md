## AppProtectionAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/AppProtectionAppReplacementExtension.appex/AppProtectionAppReplacementExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-55.1.1.0.0
-  __TEXT.__text: 0x12fc
-  __TEXT.__auth_stubs: 0x3c0
+55.1.2.100.0
+  __TEXT.__text: 0x1b9c
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x19a

   __TEXT.__objc_methname: 0x245
   __TEXT.__objc_methtype: 0xf5
   __TEXT.__constg_swiftt: 0xec
-  __TEXT.__swift5_typeref: 0x96
+  __TEXT.__swift5_typeref: 0xa4
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_reflstr: 0x1b
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0xa4
+  __TEXT.__oslogstring: 0xf4
   __TEXT.__cstring: 0x19
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__auth_ptr: 0x48
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_ptr: 0x58
   __DATA.__objc_const: 0x200
   __DATA.__objc_selrefs: 0x110
   __DATA.__objc_data: 0xb8
-  __DATA.__data: 0x1a0
+  __DATA.__data: 0x1b0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
+  - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 30
-  Symbols:   83
-  CStrings:  63
+  Functions: 42
+  Symbols:   95
+  CStrings:  64
 
Symbols:
+ _OBJC_CLASS_$_IXDataReplacementRequest
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ _malloc_size
+ _memcpy
+ _memmove
+ _swift_bridgeObjectRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_unknownObjectRetain
CStrings:
+ "AppProtectionAppReplacementMigration initialized. Request class %s"
```
