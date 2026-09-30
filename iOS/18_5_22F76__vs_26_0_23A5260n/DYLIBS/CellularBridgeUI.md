## CellularBridgeUI

> `/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI`

```diff

-1083.5.1.0.0
-  __TEXT.__text: 0x169b4
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x16b8
+1119.0.0.0.0
+  __TEXT.__text: 0x167c0
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x16c8
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x34f2
+  __TEXT.__cstring: 0x343b
   __TEXT.__oslogstring: 0x10ac
   __TEXT.__gcc_except_tab: 0x204
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x568
-  __TEXT.__objc_classname: 0x334
-  __TEXT.__objc_methname: 0x53ea
-  __TEXT.__objc_methtype: 0x13a6
-  __TEXT.__objc_stubs: 0x3800
-  __DATA_CONST.__got: 0x320
+  __TEXT.__unwind_info: 0x578
+  __TEXT.__objc_classname: 0x328
+  __TEXT.__objc_methname: 0x5464
+  __TEXT.__objc_methtype: 0x1428
+  __TEXT.__objc_stubs: 0x3860
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x770
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1510
+  __DATA_CONST.__objc_selrefs: 0x1538
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x308
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x1a60
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x19c0
   __AUTH_CONST.__objc_const: 0x1d08
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0x4b8
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xe8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
   - /System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F474DD88-5F9D-334A-9ABB-E89C84AF11C3
-  Functions: 470
-  Symbols:   1921
-  CStrings:  1668
+  UUID: 2B3183A3-9352-348B-8653-5793742A207B
+  Functions: 469
+  Symbols:   1917
+  CStrings:  1665
 
Symbols:
+ +[PDRDevice(Configuration) activeDevice]
+ -[NPHCellularSetupViewController _fetchCSNfromMetadata:]
+ -[PDRDevice(Configuration) hasHomeButton]
+ -[PDRDevice(Configuration) isCellularSeries3]
+ -[PDRDevice(Configuration) isRunningInternalBuild]
+ -[PDRDevice(Configuration) isRunningInternalBuild].cold.1
+ -[PDRDevice(Configuration) isTinker]
+ _BPSPairingIDRestoredFrom
+ _CFStringCreateWithCStringNoCopy
+ _NPHIsCerberusEnabled
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PDRDarwinNotifications
+ _OBJC_CLASS_$_PDRDevice
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyCSN
+ _PDRDevicePropertyKeyGreenTeaDevice
+ _PDRDevicePropertyKeyHomeButtonType
+ _PDRDevicePropertyKeyProductType
+ __OBJC_$_CATEGORY_CLASS_METHODS_PDRDevice_$_Configuration
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PDRDevice_$_Configuration
+ __OBJC_$_CATEGORY_PDRDevice_$_Configuration
+ ___42-[NPHCellularSetupViewController setUpNow]_block_invoke.370
+ ___42-[NPHCellularSetupViewController setUpNow]_block_invoke_2.371
+ ___42-[NPHCellularSetupViewController setUpNow]_block_invoke_2.371.cold.1
+ ___50-[PDRDevice(Configuration) isRunningInternalBuild]_block_invoke
+ ___56-[NPHBSCellularFauxCardInfoViewController activatePlan:]_block_invoke.60
+ ___60-[NPHCellularBridgeUIManager _updateCoreTelephonyClientInfo]_block_invoke.110
+ ___62-[NPHCellularSetupViewController ctCellularPlanInfoDidChange:]_block_invoke.317
+ ___62-[NPHCellularSetupViewController ctCellularPlanInfoDidChange:]_block_invoke.317.cold.1
+ ___67-[NPHCellularBridgeUIManager _updateCellularPlansWithFetch:forCSN:]_block_invoke.199
+ ___72-[NPHCellularBridgeUIManager _updateSIMStatusForAllSubscriptionContexts]_block_invoke.108
+ ___72-[NPHCellularBridgeUIManager _updateSIMStatusForAllSubscriptionContexts]_block_invoke.108.cold.1
+ ___72-[NPHCellularBridgeUIManager installPendingCellularPlan:withCompletion:]_block_invoke.137
+ ___85-[NPHBSCellularFauxCardViewController addNewRemotePlanWithCardData:confirmationCode:]_block_invoke.23
+ ___93-[NPHBSCellularFauxCardViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke.18
+ ___block_literal_global.10
+ ___block_literal_global.139
+ ___block_literal_global.159
+ ___block_literal_global.18
+ ___block_literal_global.202
+ ___block_literal_global.221
+ ___block_literal_global.223
+ ___block_literal_global.254
+ ___block_literal_global.26
+ ___block_literal_global.274
+ ___block_literal_global.283
+ _objc_msgSend$_fetchCSNfromMetadata:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$deviceForPairingID:
+ _objc_msgSend$getDevicesExcluding:
+ _objc_msgSend$isAltAccount
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$watchDidBecomeActive
- +[NRDevice(Configuration) activeDevice]
- -[NRDevice(Configuration) hasHomeButton]
- -[NRDevice(Configuration) isCellularSeries3]
- -[NRDevice(Configuration) isRunningInternalBuild]
- -[NRDevice(Configuration) isRunningInternalBuild].cold.1
- -[NRDevice(Configuration) isTinker]
- -[NSString(Uppercasing) nph_localizedUppercaseString]
- -[NSString(Uppercasing) nph_localizedUppercaseString].cold.1
- _BPSPairingDeviceRestoredFrom
- _NRDevicePropertyCSN
- _NRDevicePropertyGreenTeaDevice
- _NRDevicePropertyHomeButtonType
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyProductType
- _NRPairedDeviceRegistryWatchDidBecomeActiveDarwinNotification
- _OBJC_CLASS_$_NRDevice
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSUUID
- __OBJC_$_CATEGORY_CLASS_METHODS_NRDevice_$_Configuration
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NRDevice_$_Configuration
- __OBJC_$_CATEGORY_NRDevice_$_Configuration
- __OBJC_$_INSTANCE_METHODS_NSString(NSString_StringWithPositionalSpecifiersFormat|Uppercasing)
- ___42-[NPHCellularSetupViewController setUpNow]_block_invoke.362
- ___42-[NPHCellularSetupViewController setUpNow]_block_invoke_2.363
- ___42-[NPHCellularSetupViewController setUpNow]_block_invoke_2.363.cold.1
- ___49-[NRDevice(Configuration) isRunningInternalBuild]_block_invoke
- ___53-[NSString(Uppercasing) nph_localizedUppercaseString]_block_invoke
- ___56-[NPHBSCellularFauxCardInfoViewController activatePlan:]_block_invoke.57
- ___60-[NPHCellularBridgeUIManager _updateCoreTelephonyClientInfo]_block_invoke.106
- ___62-[NPHCellularSetupViewController ctCellularPlanInfoDidChange:]_block_invoke.309
- ___62-[NPHCellularSetupViewController ctCellularPlanInfoDidChange:]_block_invoke.309.cold.1
- ___67-[NPHCellularBridgeUIManager _updateCellularPlansWithFetch:forCSN:]_block_invoke.195
- ___72-[NPHCellularBridgeUIManager _updateSIMStatusForAllSubscriptionContexts]_block_invoke.104
- ___72-[NPHCellularBridgeUIManager _updateSIMStatusForAllSubscriptionContexts]_block_invoke.104.cold.1
- ___72-[NPHCellularBridgeUIManager installPendingCellularPlan:withCompletion:]_block_invoke.133
- ___85-[NPHBSCellularFauxCardViewController addNewRemotePlanWithCardData:confirmationCode:]_block_invoke.20
- ___93-[NPHBSCellularFauxCardViewController captureOutput:didOutputMetadataObjects:fromConnection:]_block_invoke.15
- ___block_literal_global.132
- ___block_literal_global.138
- ___block_literal_global.15
- ___block_literal_global.155
- ___block_literal_global.198
- ___block_literal_global.20
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.250
- ___block_literal_global.270
- ___block_literal_global.279
- ___block_literal_global.3
- _nph_localizedUppercaseString.map
- _nph_localizedUppercaseString.onceToken
- _objc_msgSend$activeDeviceSelectorBlock
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$localizedUppercaseString
CStrings:
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "_fetchCSNfromMetadata:"
+ "boolForKey:"
+ "cerberusEnabled"
+ "deviceForPairingID:"
+ "getDevicesExcluding:"
+ "isAltAccount"
+ "standardUserDefaults"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "updateSIMTransferStatus:"
+ "v24@0:8@\"NSDictionary\"16"
+ "watchDidBecomeActive"
- "4AA3FF3B-3224-42E6-995E-481F49AE9260"
- "CALL_SERVICE_FACETIME_AUDIO"
- "CALL_SERVICE_FACETIME_AUDIO_UPPERCASE"
- "CALL_SERVICE_FACETIME_VIDEO"
- "CALL_SERVICE_FACETIME_VIDEO_UPPERCASE"
- "Uppercasing"
- "activeDeviceSelectorBlock"
- "com.apple.private.NanoPhoneUI"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "initWithUUIDString:"
- "localizedUppercaseString"
- "nph_localizedUppercaseString"

```
