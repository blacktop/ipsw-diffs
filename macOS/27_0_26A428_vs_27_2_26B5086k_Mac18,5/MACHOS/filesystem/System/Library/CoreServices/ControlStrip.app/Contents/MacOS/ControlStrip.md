## ControlStrip

> `/System/Library/CoreServices/ControlStrip.app/Contents/MacOS/ControlStrip`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 238.400.0.0.0
-  __TEXT.__text: 0x50f5c
+  __TEXT.__text: 0x50f74
   __TEXT.__auth_stubs: 0x2280
   __TEXT.__objc_stubs: 0x2080
   __TEXT.__objc_methlist: 0x121c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x2148
   __TEXT.__eh_frame: 0x588
-  __DATA_CONST.__const: 0x46f0
+  __DATA_CONST.__const: 0x4700
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

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
   Functions: 3129
-  Symbols:   905
+  Symbols:   907
   CStrings:  969
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftGLKit
+ __swift_FORCE_LOAD_$_swiftSceneKit
Functions:
~ sub_100043c9c -> sub_100043d24 : 100 -> 108
~ sub_10004ba4c -> sub_10004badc : 28 -> 36
~ sub_100051878 -> sub_100051910 : 176 -> 184
```
