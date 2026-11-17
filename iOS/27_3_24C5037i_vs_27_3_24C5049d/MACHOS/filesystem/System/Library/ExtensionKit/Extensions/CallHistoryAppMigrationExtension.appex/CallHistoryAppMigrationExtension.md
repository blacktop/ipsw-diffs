## CallHistoryAppMigrationExtension

> `/System/Library/ExtensionKit/Extensions/CallHistoryAppMigrationExtension.appex/CallHistoryAppMigrationExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-156.300.51.0.0
-  __TEXT.__text: 0x1000
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x1a0
+156.300.74.0.0
+  __TEXT.__text: 0x1290
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0x182
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x2a5
+  __TEXT.__objc_methname: 0x2d2
   __TEXT.__objc_methtype: 0x12a
   __TEXT.__constg_swiftt: 0xdc
   __TEXT.__swift5_typeref: 0xde

   __TEXT.__swift5_reflstr: 0x1b
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x24
-  __TEXT.__cstring: 0xba
+  __TEXT.__cstring: 0x11a
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__eh_frame: 0x40
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__eh_frame: 0x70
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x200
-  __DATA.__objc_selrefs: 0x118
+  __DATA.__objc_selrefs: 0x120
   __DATA.__objc_data: 0xb0
   __DATA.__data: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 36
-  Symbols:   86
-  CStrings:  63
+  Functions: 37
+  Symbols:   93
+  CStrings:  66
 
Symbols:
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _objc_release_x25
+ _objc_release_x27
+ _objc_retain_x21
+ _objc_retain_x25
+ _swift_bridgeObjectRetain
+ _swift_release_x24
+ _swift_retain_x26
- _swift_retain_x21
Functions:
~ sub_10000198c : 1320 -> 212
+ sub_100001a60
CStrings:
+ "Error querying LaunchServices: "
+ "Failed to acquire application extension identifiers"
+ "Unknown entity type, abandoning replacement"
+ "initWithBundleIdentifier:requireValid:error:"
- "Failed to acquire application identifiers: "
```
