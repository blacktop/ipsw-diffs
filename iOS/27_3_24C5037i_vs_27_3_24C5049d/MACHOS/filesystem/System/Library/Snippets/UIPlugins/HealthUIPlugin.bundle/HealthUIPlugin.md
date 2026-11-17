## HealthUIPlugin

> `/System/Library/Snippets/UIPlugins/HealthUIPlugin.bundle/HealthUIPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`

```diff

-3610.9.1.0.0
-  __TEXT.__text: 0x7598
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0xc60
+3610.16.1.0.0
+  __TEXT.__text: 0x96c4
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_stubs: 0x60
+  __TEXT.__const: 0xdc0
   __TEXT.__objc_classname: 0x25
-  __TEXT.__constg_swiftt: 0x1fc
-  __TEXT.__swift5_typeref: 0x28a
-  __TEXT.__swift5_fieldmd: 0x254
-  __TEXT.__swift5_reflstr: 0x155
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x94
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0xc5
-  __TEXT.__objc_methname: 0x44
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__constg_swiftt: 0x24c
+  __TEXT.__swift5_typeref: 0x3e4
+  __TEXT.__swift5_fieldmd: 0x2a0
+  __TEXT.__swift5_reflstr: 0x185
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x98
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_capture: 0x50
+  __TEXT.__oslogstring: 0x85
+  __TEXT.__cstring: 0xe5
+  __TEXT.__objc_methname: 0x61
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__eh_frame: 0x230
-  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__const: 0x598
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__auth_ptr: 0x228
+  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_ptr: 0x2e8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x4f0
+  __DATA.__objc_selrefs: 0x18
+  __DATA.__data: 0x610
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 297
-  Symbols:   91
-  CStrings:  9
+  Functions: 349
+  Symbols:   106
+  CStrings:  12
 
Symbols:
+ _OBJC_CLASS_$_UIColor
+ __os_log_impl
+ __swiftImmortalRefCount
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retain_x8
+ _os_log_type_enabled
+ _swift_getAtKeyPath
+ _swift_getKeyPath
+ _swift_getObjectType
+ _swift_release_n
+ _swift_release_x25
+ _swift_retain
+ _swift_retain_n
+ _swift_slowAlloc
+ _swift_slowDealloc
- __swiftEmptySetSingleton
CStrings:
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "history/workouts/"
+ "systemGroupedBackgroundColor"
```
