## CoreServicesAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/CoreServicesAppReplacementExtension.appex/CoreServicesAppReplacementExtension`

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
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-469.1.6.0.0
-  __TEXT.__text: 0x1420
-  __TEXT.__auth_stubs: 0x3d0
+469.1.7.0.0
+  __TEXT.__text: 0x1ea0
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x19a

   __TEXT.__objc_methname: 0x2b9
   __TEXT.__objc_methtype: 0xf5
   __TEXT.__constg_swiftt: 0xec
-  __TEXT.__swift5_typeref: 0x9c
+  __TEXT.__swift5_typeref: 0xaa
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_reflstr: 0x1b
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0x72
+  __TEXT.__oslogstring: 0xf2
   __TEXT.__cstring: 0x1a
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0x128
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__auth_ptr: 0x50
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x200
   __DATA.__objc_selrefs: 0x120
   __DATA.__objc_data: 0xb8
-  __DATA.__data: 0x1b0
+  __DATA.__data: 0x1c0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 32
-  Symbols:   81
-  CStrings:  64
+  Functions: 44
+  Symbols:   93
+  CStrings:  66
 
Symbols:
+ _OBJC_CLASS_$_IXDataReplacementRequest
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_release_x8
+ _objc_retain_x28
+ _swift_bridgeObjectRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_unknownObjectRetain
- _objc_release_x27
- _objc_retain_x21
CStrings:
+ "CoreServicesAppReplacementMigration initialized. Request class %s"
+ "migrated CoreServices goop from %@ to %@"
```
