## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x264c
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x158
+3229.1.6.0.0
+  __TEXT.__text: 0x25a4
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x170
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x8bd
+  __TEXT.__cstring: 0x927
   __TEXT.__oslogstring: 0x12a
-  __TEXT.__objc_methname: 0xe3d
+  __TEXT.__objc_methname: 0xee0
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
   __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x780
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x448
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF838C03-936D-35A5-B74B-34F92CDCBFB1
-  Functions: 30
-  Symbols:   83
-  CStrings:  275
+  UUID: 7A2B5C54-6937-3D53-A787-5777BFEB65AA
+  Functions: 32
+  Symbols:   84
+  CStrings:  284
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "_AccessibilityMigration__ResetSingleLetterQuickNav_27.0"
+ "_AccessibilityMigration__VoiceOverHintOption_27.0"
+ "_raveMigrateResetSingleLetterQuickNav"
+ "_raveMigrateVoiceOverHintsOption"
+ "setVoiceOverHintOption:"
+ "setVoiceOverTouchSingleLetterQuickNavEnabled:"
+ "voiceOverHintsEnabled"

```
