## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.60.26.0.0
-  __TEXT.__text: 0x88f84
-  __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_methlist: 0x3c54
-  __TEXT.__const: 0x7f8
-  __TEXT.__oslogstring: 0x9563
-  __TEXT.__cstring: 0x5c0d
-  __TEXT.__gcc_except_tab: 0x1758
-  __TEXT.__unwind_info: 0x1220
-  __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0x8210
-  __TEXT.__objc_methtype: 0x154e
-  __TEXT.__objc_stubs: 0x67a0
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__objc_classlist: 0x2d0
+921.80.167.0.0
+  __TEXT.__text: 0x89fcc
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__objc_methlist: 0x3dcc
+  __TEXT.__const: 0x800
+  __TEXT.__oslogstring: 0x958e
+  __TEXT.__cstring: 0x5c70
+  __TEXT.__gcc_except_tab: 0x17ac
+  __TEXT.__unwind_info: 0x1270
+  __TEXT.__objc_classname: 0x863
+  __TEXT.__objc_methname: 0x8518
+  __TEXT.__objc_methtype: 0x1580
+  __TEXT.__objc_stubs: 0x6aa0
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__const: 0x8d8
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2098
+  __DATA_CONST.__objc_selrefs: 0x21b0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0xb38
-  __AUTH_CONST.__auth_got: 0xb58
+  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_arraydata: 0xb70
+  __AUTH_CONST.__auth_got: 0xb68
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x74c0
-  __AUTH_CONST.__objc_const: 0x5ae0
-  __AUTH_CONST.__objc_arrayobj: 0x750
+  __AUTH_CONST.__cfstring: 0x7520
+  __AUTH_CONST.__objc_const: 0x5da0
+  __AUTH_CONST.__objc_arrayobj: 0x7b0
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0xf50
-  __DATA.__objc_ivar: 0x2f0
+  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH.__objc_data: 0xff0
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x690
   __DATA.__common: 0x30
   __DATA.__bss: 0x98

   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 17152976-1EA1-3F12-85E7-463E5664641F
-  Functions: 2313
-  Symbols:   7632
-  CStrings:  4892
+  UUID: 361FA410-E9F1-35A3-AEFA-67ACDD182D29
+  Functions: 2338
+  Symbols:   7738
+  CStrings:  4958
 
Symbols:
+ +[CRKeyStrokeMonitor physicalIntentGestureKeys]
+ -[CRFDRWatch1DeviceHandler spcWithComponent:withIdentifier:]
+ -[CRIOServiceController _closeRepairService]
+ -[CRIOServiceController _openRepairService]
+ -[CRIOServiceController _openRepairService].cold.1
+ -[CRIOServiceController _openRepairService].cold.2
+ -[CRIOServiceController assertRepairPin:]
+ -[CRIOServiceController assertRepairPin:].cold.1
+ -[CRIOServiceController connection]
+ -[CRIOServiceController init]
+ -[CRIOServiceController isRepairPinAsserted]
+ -[CRIOServiceController isRepairPinAsserted].cold.1
+ -[CRIOServiceController service]
+ -[CRIOServiceController setConnection:]
+ -[CRIOServiceController setService:]
+ -[CRKeyStrokeMonitor .cxx_destruct]
+ -[CRKeyStrokeMonitor callback]
+ -[CRKeyStrokeMonitor client]
+ -[CRKeyStrokeMonitor gestureKeys]
+ -[CRKeyStrokeMonitor handleKeyboardEvent:event:]
+ -[CRKeyStrokeMonitor initWithGestureKeys:callback:]
+ -[CRKeyStrokeMonitor pressedKeys]
+ -[CRKeyStrokeMonitor setCallback:]
+ -[CRKeyStrokeMonitor setClient:]
+ -[CRKeyStrokeMonitor setGestureKeys:]
+ -[CRKeyStrokeMonitor setPressedKeys:]
+ -[CRKeyStrokeMonitor setTriggered:]
+ -[CRKeyStrokeMonitor setVerbose:]
+ -[CRKeyStrokeMonitor start]
+ -[CRKeyStrokeMonitor stop]
+ -[CRKeyStrokeMonitor triggered]
+ -[CRKeyStrokeMonitor verbose]
+ _OBJC_CLASS_$_CRIOServiceController
+ _OBJC_CLASS_$_CRKeyStrokeMonitor
+ _OBJC_CLASS_$_HIDEventSystemClient
+ _OBJC_IVAR_$_CRIOServiceController._connection
+ _OBJC_IVAR_$_CRIOServiceController._service
+ _OBJC_IVAR_$_CRKeyStrokeMonitor._callback
+ _OBJC_IVAR_$_CRKeyStrokeMonitor._client
+ _OBJC_IVAR_$_CRKeyStrokeMonitor._gestureKeys
+ _OBJC_IVAR_$_CRKeyStrokeMonitor._pressedKeys
+ _OBJC_IVAR_$_CRKeyStrokeMonitor._triggered
+ _OBJC_IVAR_$_CRKeyStrokeMonitor._verbose
+ _OBJC_METACLASS_$_CRIOServiceController
+ _OBJC_METACLASS_$_CRKeyStrokeMonitor
+ __OBJC_$_CLASS_METHODS_CRKeyStrokeMonitor
+ __OBJC_$_INSTANCE_METHODS_CRIOServiceController
+ __OBJC_$_INSTANCE_METHODS_CRKeyStrokeMonitor
+ __OBJC_$_INSTANCE_VARIABLES_CRIOServiceController
+ __OBJC_$_INSTANCE_VARIABLES_CRKeyStrokeMonitor
+ __OBJC_$_PROP_LIST_CRIOServiceController
+ __OBJC_$_PROP_LIST_CRKeyStrokeMonitor
+ __OBJC_CLASS_RO_$_CRIOServiceController
+ __OBJC_CLASS_RO_$_CRKeyStrokeMonitor
+ __OBJC_METACLASS_RO_$_CRIOServiceController
+ __OBJC_METACLASS_RO_$_CRKeyStrokeMonitor
+ ___27-[CRKeyStrokeMonitor start]_block_invoke
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.258
+ ___block_descriptor_40_e8_32w_e39_v24?0"HIDServiceClient"8"HIDEvent"16lw32l8
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$_closeRepairService
+ _objc_msgSend$_openRepairService
+ _objc_msgSend$activate
+ _objc_msgSend$callback
+ _objc_msgSend$cancel
+ _objc_msgSend$client
+ _objc_msgSend$connection
+ _objc_msgSend$gestureKeys
+ _objc_msgSend$handleKeyboardEvent:event:
+ _objc_msgSend$initWithType:
+ _objc_msgSend$integerValueForField:
+ _objc_msgSend$isRepairPinAsserted
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$options
+ _objc_msgSend$pressedKeys
+ _objc_msgSend$service
+ _objc_msgSend$setClient:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setEventHandler:
+ _objc_msgSend$setPressedKeys:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setService:
+ _objc_msgSend$timestamp
+ _objc_setProperty_atomic
+ _objc_setProperty_atomic_copy
- -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.1
- -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.2
- -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.3
- -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.4
- -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.5
- _AMFDRSealingManifestCopyMinimalManifestClassesAndInstances
- _AMFDRSealingMapCopyMinimalManifestClassesAndInstances
- ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.255
CStrings:
+ "%@ repair_en"
+ "@\"HIDEventSystemClient\""
+ "@32@0:8@16@?24"
+ "AppleSecureRepair"
+ "Asserting"
+ "B20@0:8B16"
+ "CRIOServiceController"
+ "CRKeyStrokeMonitor"
+ "ClientEventFilter"
+ "De-asserting"
+ "Failed to call kAppleRepairAssertRepair (%08x)"
+ "Failed to find AppleSecureRepair IOService"
+ "Failed to open Repair IOService with status: %08lx"
+ "GESTURE DETECTED"
+ "KEYDOWN: usagePage: 0x%lx usage: 0x%lx"
+ "KEYUP: usagePage: 0x%lx usage: 0x%lx"
+ "T@\"HIDEventSystemClient\",&,V_client"
+ "T@\"NSArray\",&,V_gestureKeys"
+ "T@\"NSMutableDictionary\",&,V_pressedKeys"
+ "T@?,C,V_callback"
+ "TB,V_triggered"
+ "TB,V_verbose"
+ "TI,N,V_connection"
+ "TI,N,V_service"
+ "_callback"
+ "_client"
+ "_closeRepairService"
+ "_connection"
+ "_gestureKeys"
+ "_openRepairService"
+ "_pressedKeys"
+ "_service"
+ "_triggered"
+ "_verbose"
+ "activate"
+ "assertRepairPin:"
+ "callback"
+ "cancel"
+ "client"
+ "connection"
+ "gestureKeys"
+ "handleKeyboardEvent:event:"
+ "initWithGestureKeys:callback:"
+ "initWithType:"
+ "integerValueForField:"
+ "isRepairPinAsserted"
+ "numberWithUnsignedLongLong:"
+ "options"
+ "physicalIntentGestureKeys"
+ "pressedKeys"
+ "setCallback:"
+ "setClient:"
+ "setConnection:"
+ "setDispatchQueue:"
+ "setEventHandler:"
+ "setGestureKeys:"
+ "setPressedKeys:"
+ "setProperty:forKey:"
+ "setService:"
+ "setTriggered:"
+ "setVerbose:"
+ "start"
+ "stop"
+ "stopping keyboard monitor"
+ "timestamp"
+ "triggered"
+ "usagePage: 0x%lx usage: 0x%lx keyDown: %ld builtIn: %ld longPress: %ld flags:%u"
+ "v24@?0@\"HIDServiceClient\"8@\"HIDEvent\"16"
+ "verbose"
- "AMFDRSealingManifestCopyMinimalManifestClassesAndInstances failed: %@"
- "AMFDRSealingMapCopyMinimalManifestClassesAndInstances failed: %@"
- "Current MinimalManifests: %@, %@, %@"
- "Decode KBB sealing manifest failed: %@"
- "KBB MinimalManifests: %@, %@, %@"

```
