## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

```diff

-3191.3.0.0.0
-  __TEXT.__text: 0x22d4
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x14c
+3191.7.1.1.0
+  __TEXT.__text: 0x23fc
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x158
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x860
+  __TEXT.__cstring: 0x8bd
   __TEXT.__oslogstring: 0x12a
-  __TEXT.__objc_methname: 0xd7a
+  __TEXT.__objc_methname: 0xe3d
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
   __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x420
+  __DATA.__objc_selrefs: 0x448
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9B36612-2537-3B0E-9375-C2817B3B7D97
-  Functions: 29
-  Symbols:   82
-  CStrings:  268
+  UUID: 90190943-5987-301C-B5DA-315DA0529A7E
+  Functions: 30
+  Symbols:   85
+  CStrings:  275
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ __AXSAssistiveTouchScannerEnabled
+ __AXSZoomTouchEnabled
Functions:
~ sub_12a0 : 168 -> 176
+ sub_1400
CStrings:
+ "_AccessibilityMigration__AvoidShowingHelpBannerIfVoiceOverOrSwitchControlAlreadyEnabled_26.1"
+ "_luckBMigrateAvoidShowingHelpBannerIfVoiceOverOrSwitchControlAlreadyEnabled"
+ "distantPast"
+ "setAccessibilityHelpBannerFirstShownTimestamp:"
+ "touchAccommodationsAreConfigured"
+ "touchAccommodationsEnabled"

```
