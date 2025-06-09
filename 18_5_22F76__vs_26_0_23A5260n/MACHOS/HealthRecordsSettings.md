## HealthRecordsSettings

> `/System/Library/PreferenceBundles/HealthRecordsSettings.bundle/HealthRecordsSettings`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x488
+6074.1.2.4.0
+  __TEXT.__text: 0x4a4
   __TEXT.__auth_stubs: 0xe0
-  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_stubs: 0x120
   __TEXT.__objc_methlist: 0x384
-  __TEXT.__objc_methname: 0x5a4
-  __TEXT.__cstring: 0x3c
+  __TEXT.__objc_methname: 0x5d7
+  __TEXT.__cstring: 0xf
   __TEXT.__objc_classname: 0x7e
   __TEXT.__objc_methtype: 0x413
   __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0x78
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x3e8
-  __DATA.__objc_selrefs: 0x1c0
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x180

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F0BD749C-C2D8-398B-8188-ADAEA4E195FC
+  UUID: 0098F734-EA98-3865-AC9F-8D4A33D03D4B
   Functions: 17
   Symbols:   24
-  CStrings:  126
+  CStrings:  125
 
Symbols:
+ _OBJC_CLASS_$_HAServicesDefines
- _OBJC_CLASS_$_NSURL
Functions:
~ sub_bb0 -> sub_c20 : 140 -> 168
CStrings:
+ "healthSettingsHealthRecordsSpecifier"
+ "internalHealthSettingsURLTo:"
- "URLWithString:"
- "prefs://root=HEALTH&path=HEALTH_RECORDS_ITEM"

```
