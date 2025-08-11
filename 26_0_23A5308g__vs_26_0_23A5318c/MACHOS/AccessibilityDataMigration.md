## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

```diff

-3189.2.0.0.0
-  __TEXT.__text: 0x2118
+3190.5.0.0.0
+  __TEXT.__text: 0x221c
   __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x134
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x140
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x7c2
+  __TEXT.__cstring: 0x81c
   __TEXT.__oslogstring: 0x12a
-  __TEXT.__objc_methname: 0xcd3
+  __TEXT.__objc_methname: 0xcfe
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x3f8
+  __DATA.__objc_selrefs: 0x408
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A48CFC5E-E176-362B-951F-2E7EB77CA61B
-  Functions: 27
+  UUID: 421AA739-BAC9-3EED-A828-2E7B4E76DCF2
+  Functions: 28
   Symbols:   82
-  CStrings:  255
+  CStrings:  263
 
Functions:
~ sub_12a0 : 152 -> 160
+ sub_1340
CStrings:
+ "AXSMotionCuesMode"
+ "AXSMotionCuesStyle"
+ "_AccessibilityMigration__DefaultMotionCuesStyle_26.0"
+ "_luckMigrateMotionCuesStyle"
+ "numberWithInt:"

```
