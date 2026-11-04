## com.apple.HealthKit.HealthKitAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/com.apple.HealthKit.HealthKitAppReplacementExtension.appex/com.apple.HealthKit.HealthKitAppReplacementExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x3364
-  __TEXT.__auth_stubs: 0x5c0
+7027.2.13.0.0
+  __TEXT.__text: 0x3768
+  __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x1a4
+  __TEXT.__const: 0x1b2
+  __TEXT.__cstring: 0xc7
+  __TEXT.__oslogstring: 0x222
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x391

   __TEXT.__swift5_fieldmd: 0x3c
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__cstring: 0x105
-  __TEXT.__oslogstring: 0x232
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift_as_entry: 0x18
-  __TEXT.__swift_as_ret: 0x18
-  __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__eh_frame: 0x270
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__eh_frame: 0x308
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x228
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0xb8
-  __DATA.__data: 0x1e0
+  __DATA.__data: 0x200
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 75
+  Functions: 83
   Symbols:   95
-  CStrings:  77
+  CStrings:  76
 
CStrings:
+ "App extension replacement: no Health state moved for the extension."
- "Health state for a replaced app extension is not moved yet."
- "Unsupported entity type, the replaced app extension's Health state was not moved: %{public}@"
```
