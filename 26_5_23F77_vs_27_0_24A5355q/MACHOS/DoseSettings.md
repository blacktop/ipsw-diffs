## DoseSettings

> `/System/Library/NanoPreferenceBundles/Applications/DoseSettings.bundle/DoseSettings`

```diff

-148.4.0.0.0
-  __TEXT.__text: 0x38a4
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x1380
+151.0.0.0.0
+  __TEXT.__text: 0x33fc
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_stubs: 0x1340
   __TEXT.__objc_methlist: 0x6a4
-  __TEXT.__cstring: 0x3c1
-  __TEXT.__objc_methname: 0x1a09
-  __TEXT.__objc_classname: 0xe4
+  __TEXT.__cstring: 0x3c3
+  __TEXT.__objc_methname: 0x19d3
+  __TEXT.__objc_classname: 0xe2
   __TEXT.__objc_methtype: 0x785
   __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__unwind_info: 0x118
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x198
   __DATA.__objc_const: 0x768
-  __DATA.__objc_selrefs: 0x7f8
+  __DATA.__objc_selrefs: 0x7e8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x1e8

   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D453547-C737-3EE6-BD6F-339E5001D1C4
+  UUID: 1F3B3A76-9C73-3865-A188-452F054D7D5C
   Functions: 66
-  Symbols:   126
-  CStrings:  439
+  Symbols:   123
+  CStrings:  437
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _NRDevicePropertyIsAltAccount
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "getActivePairedDeviceIncludingAltAccount"
+ "isAltAccount"
- "activeDeviceSelectorBlock"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "valueForProperty:"

```
