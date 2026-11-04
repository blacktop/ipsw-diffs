## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x29cc
+3245.8.14.0.0
+  __TEXT.__text: 0x2ae0
   __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x194
+  __TEXT.__objc_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x1a0
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0xa51
-  __TEXT.__oslogstring: 0x1e9
-  __TEXT.__objc_methname: 0xf8b
+  __TEXT.__cstring: 0xa9d
+  __TEXT.__oslogstring: 0x234
+  __TEXT.__objc_methname: 0x1040
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x100
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x880
+  __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x490
+  __DATA.__objc_selrefs: 0x4a8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 35
+  Functions: 36
   Symbols:   92
-  CStrings:  235
+  CStrings:  240
 
Functions:
~ sub_1294 : 404 -> 412
+ sub_1430
CStrings:
+ "Setting BSI single-hand activation gesture to match activation gesture: %i"
+ "_AccessibilityMigration__BrailleScreenInputSingleHandActivationGesture_27.3"
+ "_raveCMigrateBrailleScreenInputSingleHandActivationGesture"
+ "setVoiceOverTouchBrailleGesturesSingleHandActivationGestureEnabled:"
+ "voiceOverTouchBrailleGesturesActivationGestureEnabled"
```
