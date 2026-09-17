## Bluetooth

> `/System/Library/ExtensionKit/Extensions/Bluetooth.appex/Contents/MacOS/Bluetooth`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.51.0.0.0
+2701.3.0.0.0
   __TEXT.__text: 0x6965c
   __TEXT.__auth_stubs: 0x1bf0
   __TEXT.__objc_stubs: 0x10a0

   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x2218
   __TEXT.__eh_frame: 0x2e0
-  __DATA_CONST.__const: 0x2310
+  __DATA_CONST.__const: 0x2320
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x38

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMediaIO.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftQuickLookUI.dylib
+  - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2693
-  Symbols:   183
+  Symbols:   185
   CStrings:  575
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftGLKit
+ __swift_FORCE_LOAD_$_swiftSceneKit
```
