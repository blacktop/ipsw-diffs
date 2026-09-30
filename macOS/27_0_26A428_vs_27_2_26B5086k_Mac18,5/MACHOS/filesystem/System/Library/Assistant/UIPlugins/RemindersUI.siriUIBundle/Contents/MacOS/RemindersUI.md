## RemindersUI

> `/System/Library/Assistant/UIPlugins/RemindersUI.siriUIBundle/Contents/MacOS/RemindersUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-4046.21.0.0.0
+4076.0.0.0.0
   __TEXT.__text: 0x4734
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_stubs: 0x1ae0

   __TEXT.__objc_classname: 0x1de
   __TEXT.__objc_methtype: 0xd69
   __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x48

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
   Functions: 129
-  Symbols:   135
+  Symbols:   137
   CStrings:  489
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftGLKit
+ __swift_FORCE_LOAD_$_swiftSceneKit
```
