## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3234.5.0.0.0
-  __TEXT.__text: 0x2700
+3237.1.0.0.0
+  __TEXT.__text: 0x2860
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__objc_stubs: 0x10c0
+  __TEXT.__objc_methlist: 0x188
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x988
+  __TEXT.__cstring: 0xa1c
   __TEXT.__oslogstring: 0x12a
-  __TEXT.__objc_methname: 0xf30
+  __TEXT.__objc_methname: 0xf6b
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
   __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x800
+  __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0xf8
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_selrefs: 0x488
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 33
+  Functions: 34
   Symbols:   87
-  CStrings:  225
+  CStrings:  229
 
Functions:
~ sub_12a0 : 200 -> 208
+ sub_16f4
CStrings:
+ "AssistiveTouchMouseAlwaysShowSoftwareKeyboard"
+ "_AccessibilityMigration__AssistiveTouchAlwaysShowOnscreenKeyboardDomain_27.0"
+ "_raveMigrateAssistiveTouchAlwaysShowOnscreenKeyboardDomain"
+ "com.apple.AssistiveTouch"
```
