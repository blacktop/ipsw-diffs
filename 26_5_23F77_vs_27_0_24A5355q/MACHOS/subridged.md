## subridged

> `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged`

```diff

-367.120.2.0.0
-  __TEXT.__text: 0x19b28
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x2300
-  __TEXT.__objc_methlist: 0x128c
+393.0.0.0.0
+  __TEXT.__text: 0x1855c
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x2380
+  __TEXT.__objc_methlist: 0x1294
   __TEXT.__const: 0x508
-  __TEXT.__gcc_except_tab: 0x330
-  __TEXT.__cstring: 0x2524
-  __TEXT.__oslogstring: 0x28fe
-  __TEXT.__objc_classname: 0x156
-  __TEXT.__objc_methtype: 0xf8b
-  __TEXT.__objc_methname: 0x3d74
-  __TEXT.__unwind_info: 0x6b0
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1178
-  __DATA_CONST.__cfstring: 0x1b80
+  __TEXT.__gcc_except_tab: 0x258
+  __TEXT.__cstring: 0x26c1
+  __TEXT.__oslogstring: 0x2c2c
+  __TEXT.__objc_classname: 0x13e
+  __TEXT.__objc_methtype: 0xf53
+  __TEXT.__objc_methname: 0x3dc9
+  __TEXT.__unwind_info: 0x530
+  __DATA_CONST.__const: 0x11a0
+  __DATA_CONST.__cfstring: 0x1dc0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2110
-  __DATA.__objc_selrefs: 0xe08
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x2108
+  __DATA.__objc_selrefs: 0xe28
   __DATA.__objc_ivar: 0x13c
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x438

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06A820EE-94C9-342B-BAD1-25E3768BE31E
-  Functions: 493
-  Symbols:   233
-  CStrings:  1500
+  UUID: 70DE2718-FFBF-309D-9092-CC07ACDEA4B4
+  Functions: 494
+  Symbols:   235
+  CStrings:  1551
 
Symbols:
+ _MASetServerUrlOverride
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
- _ASSetAssetServerURLForAssetType
- _ASSetDefaultAssetServerURLForAssetType
- _CFPreferencesAppSynchronize
- _CFPreferencesGetAppIntegerValue
- _CFPreferencesSetAppValue
- _CPFSSizeStrings
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[SUBDescriptor internalMessageFromDenialInfo:]"
+ ": CallOngoing :"
+ ": ChargerRequired :"
+ ": LowBatt(Min/Current) (%@ / %@) :"
+ ": NavigationActive :"
+ ": WorkoutInProgress :"
+ "@20@0:8B16"
+ "CallInProgress"
+ "ConstraintDenialMessage"
+ "DeviceBusyReasons"
+ "INSTALLATION_PAUSED_NAVIGATION"
+ "INSTALLATION_PAUSED_PHONE_CALL"
+ "INSTALLATION_PAUSED_WORKOUT"
+ "INSTALL_EXPIRED_BATTERY"
+ "INSTALL_EXPIRED_CHARGER"
+ "INSTALL_EXPIRED_CHARGER_OPTIONAL"
+ "INSTALL_EXPIRED_NAVIGATION"
+ "INSTALL_EXPIRED_PHONE_CALL"
+ "INSTALL_EXPIRED_WORKOUT"
+ "Install Pause Reason: "
+ "Invalid value passed for minBatteryLevelForApplyOffCharger"
+ "Invalid value passed for minBatteryLevelForApplyOnCharger"
+ "NavigationActive"
+ "WorkoutInProgress"
+ "[DenialReasons]: DeviceBusyReason : %{public}@"
+ "[DenialReasons]: Got invalid value for CurrentBatteryLevel, assuming low battery"
+ "[DenialReasons]: No denial reasons set in descriptor. Returning nil message"
+ "[DenialReasons]: Showing combined battery/charger message in notification due to inability to determine more specific reason"
+ "[DenialReasons]: Showing installation paused due to call"
+ "[DenialReasons]: Showing installation paused due to ongoing navigation"
+ "[DenialReasons]: Showing installation paused due to workout"
+ "[DenialReasons]: Unexpected value passed for chargerConnected. Assuming not connected"
+ "[ShowDuetConditions]: Could not extract installation denial reasons from descriptor"
+ "[ShowDuetConditions]: DenialReasons : %{public}@"
+ "_denialReasonsMessageForExpiredWindow:"
+ "getDenialReasonsMessage"
+ "getExpiredDenialReasonsMessage"
+ "stringByAppendingString:"
+ "stringFromByteCount:countStyle:"
- "-[SUBUserNotification internalMessageFromDenialInfo:]"
- "ChargerRequired: %@ ChargerConnected: %@ BatteryLevel: %@"
- "Resetting asset URLs to default values"
- "SUDefaultsCleanupVersion"
- "fetchDocumentationForDescriptor:localOnly:overrideURL:completion:"
- "v36@0:8@\"SUBDescriptor\"16B24@?<v@?@\"SUBDocumentation\"@\"NSError\">28"

```
