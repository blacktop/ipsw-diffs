## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3245.8.4.2.0
-  __TEXT.__text: 0x285c
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x188
-  __TEXT.__const: 0x40
+3245.8.9.0.0
+  __TEXT.__text: 0x29cc
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0x194
+  __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0xa1c
-  __TEXT.__oslogstring: 0x17d
-  __TEXT.__objc_methname: 0xf6b
+  __TEXT.__cstring: 0xa51
+  __TEXT.__oslogstring: 0x1e9
+  __TEXT.__objc_methname: 0xf8b
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x860
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_selrefs: 0x490
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 34
-  Symbols:   88
-  CStrings:  231
+  Functions: 35
+  Symbols:   92
+  CStrings:  235
 
Symbols:
+ _AXDeviceIsPhone
+ __AXSHomeButtonRestingUnlock
+ __AXSHomeButtonRestingUnlockPreferredForDevice
+ _kAXSRestingHomeButtonUnlockPreference
Functions:
~ sub_1294 : 396 -> 404
+ sub_1428
CStrings:
+ "Clearing existing Rest Finger to Open preference."
+ "Device prefers Rest Finger to Open. Currently enabled: %i"
+ "_AccessibilityMigration_MigrateRestFingerToOpen_27_1"
+ "_ravePopMigrateRestFingerToOpen"
```
