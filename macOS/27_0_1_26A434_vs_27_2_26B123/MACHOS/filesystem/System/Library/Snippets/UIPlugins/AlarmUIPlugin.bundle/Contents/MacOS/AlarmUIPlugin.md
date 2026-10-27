## AlarmUIPlugin

> `/System/Library/Snippets/UIPlugins/AlarmUIPlugin.bundle/Contents/MacOS/AlarmUIPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA.__objc_const`

```diff

-3600.26.13.0.0
-  __TEXT.__text: 0x2a48
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__const: 0x282
-  __TEXT.__swift5_typeref: 0x4f8
-  __TEXT.__swift5_reflstr: 0x51
-  __TEXT.__swift5_assocty: 0x30
+3605.13.1.0.0
+  __TEXT.__text: 0x3510
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__const: 0x33e
+  __TEXT.__swift5_typeref: 0x524
+  __TEXT.__swift5_reflstr: 0x61
+  __TEXT.__swift5_assocty: 0x48
   __TEXT.__objc_classname: 0x23
-  __TEXT.__constg_swiftt: 0xb4
-  __TEXT.__swift5_fieldmd: 0x48
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__constg_swiftt: 0xec
+  __TEXT.__swift5_fieldmd: 0x54
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_proto: 0x18
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__cstring: 0x81
+  __TEXT.__oslogstring: 0x85
+  __TEXT.__unwind_info: 0x1a8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x208
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__auth_ptr: 0x158
+  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0x90
-  __DATA.__data: 0x240
-  __DATA.__bss: 0x210
+  __DATA.__data: 0x268
+  __DATA.__bss: 0x320
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
   - /System/Library/PrivateFrameworks/AlarmUIFramework.framework/Versions/A/AlarmUIFramework

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 66
-  Symbols:   60
-  CStrings:  1
+  Functions: 86
+  Symbols:   73
+  CStrings:  3
 
Symbols:
+ __os_log_impl
+ __swiftImmortalRefCount
+ _memcpy
+ _memmove
+ _objc_release
+ _os_log_type_enabled
+ _swift_getAtKeyPath
+ _swift_getForeignTypeMetadata
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
```
