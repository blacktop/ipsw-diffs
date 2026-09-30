## DeviceManagementTools

> `/System/Library/PrivateFrameworks/DeviceManagementTools.framework/DeviceManagementTools`

```diff

-75.0.0.0.0
-  __TEXT.__text: 0x164b8
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x202c
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1d9e
-  __TEXT.__ustring: 0x3a6
-  __TEXT.__oslogstring: 0x193c
-  __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__unwind_info: 0x6a0
-  __TEXT.__objc_classname: 0x950
-  __TEXT.__objc_methname: 0x500c
-  __TEXT.__objc_methtype: 0xe37
-  __TEXT.__objc_stubs: 0x34a0
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x828
-  __DATA_CONST.__objc_classlist: 0x170
+76.0.0.0.0
+  __TEXT.__text: 0x1757c
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x20ac
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x2001
+  __TEXT.__ustring: 0x55e
+  __TEXT.__oslogstring: 0x1b25
+  __TEXT.__gcc_except_tab: 0x380
+  __TEXT.__unwind_info: 0x740
+  __TEXT.__objc_classname: 0x964
+  __TEXT.__objc_methname: 0x525f
+  __TEXT.__objc_methtype: 0xe60
+  __TEXT.__objc_stubs: 0x36e0
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_selrefs: 0x10c8
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__objc_arraydata: 0x130
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x22e0
-  __AUTH_CONST.__objc_const: 0x5008
-  __AUTH_CONST.__objc_dictobj: 0x230
+  __AUTH_CONST.__cfstring: 0x2480
+  __AUTH_CONST.__objc_const: 0x5160
+  __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x26c
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x27c
   __DATA.__data: 0xa80
   __DATA.__bss: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 947452E6-489A-3AF4-8E10-31A1616B00A1
-  Functions: 719
-  Symbols:   2919
-  CStrings:  1746
+  UUID: 5F75A1B7-B8CE-377F-BB8B-941569B0E318
+  Functions: 740
+  Symbols:   2996
+  CStrings:  1808
 
Symbols:
+ +[DMTPairingConstants localeIdentifierKey]
+ -[DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController isActive]
+ -[DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController setActive:]
+ -[DMTCatalystSharingBackedDeviceSession initWithDevice:locale:]
+ -[DMTCatalystSharingBackedDeviceSession locale]
+ -[DMTCatalystSharingBackedDeviceSession performPairingWithCompletion:]
+ -[DMTCatalystSharingBackedDeviceSession performPairingWithPreAuthWithCompletion:]
+ -[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:]
+ -[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:].cold.1
+ -[DMTSharingBroadcastPrimitives remoteLocaleIdentifier]
+ -[DMTSharingBroadcastPrimitives setRemoteLocaleIdentifier:]
+ -[DMTSharingDevice deviceContext]
+ -[DMTSharingDevice setDeviceContext:]
+ -[DMTSharingDevice updateDeviceContext:]
+ GCC_except_table10
+ GCC_except_table14
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table51
+ _NSKeyValueChangeNewKey
+ _NSKeyValueChangeOldKey
+ _OBJC_CLASS_$_DMTPairingConstants
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController._active
+ _OBJC_IVAR_$_DMTCatalystSharingBackedDeviceSession._locale
+ _OBJC_IVAR_$_DMTSharingBroadcastPrimitives._remoteLocaleIdentifier
+ _OBJC_IVAR_$_DMTSharingDevice._deviceContext
+ _OBJC_METACLASS_$_DMTPairingConstants
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_DMTPairingConstants
+ __OBJC_$_CLASS_PROP_LIST_DMTPairingConstants
+ __OBJC_CLASS_RO_$_DMTPairingConstants
+ __OBJC_METACLASS_RO_$_DMTPairingConstants
+ ___101-[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:]_block_invoke
+ ___101-[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:]_block_invoke.26
+ ___101-[DMTCatalystSharingBackedDeviceSession sendRequestID:unencryptedRequestData:withTimeout:completion:]_block_invoke.cold.1
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.19
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.19.cold.1
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.19.cold.2
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.19.cold.3
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.34
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.34.cold.1
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.35
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.35.cold.1
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.35.cold.2
+ ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.37
+ ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.10
+ ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.10.cold.1
+ ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.13
+ ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.13.cold.1
+ ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.15
+ ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.15.cold.1
+ ___61-[DMTCatalystSharingBackedDeviceSession addPrimitiveHandlers]_block_invoke.8
+ ___61-[DMTCatalystSharingBackedDeviceSession addPrimitiveHandlers]_block_invoke_2.10
+ ___61-[DMTCatalystSharingBackedDeviceSession addPrimitiveHandlers]_block_invoke_3.11
+ ___70-[DMTCatalystSharingBackedDeviceSession performPairingWithCompletion:]_block_invoke
+ ___70-[DMTCatalystSharingBackedDeviceSession performPairingWithCompletion:]_block_invoke.cold.1
+ ___81-[DMTCatalystSharingBackedDeviceSession performPairingWithPreAuthWithCompletion:]_block_invoke
+ ___81-[DMTCatalystSharingBackedDeviceSession performPairingWithPreAuthWithCompletion:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32bs40w_e51_v32?0"NSError"8"NSDictionary"16"NSDictionary"24lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSError""NSDictionary""NSDictionary">24lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e51_v32?0"NSError"8"NSDictionary"16"NSDictionary"24lr48l8w56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e5_v8?0lr48l8w56l8s32l8s40l8
+ ___block_literal_global.124
+ _dispatch_after
+ _dispatch_time
+ _objc_msgSend$currentLocale
+ _objc_msgSend$deregisterRequestID:
+ _objc_msgSend$initWithDevice:locale:
+ _objc_msgSend$isActive
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$locale
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$localeIdentifierKey
+ _objc_msgSend$performPairingWithCompletion:
+ _objc_msgSend$performPairingWithPreAuthWithCompletion:
+ _objc_msgSend$registerRequestID:options:handler:
+ _objc_msgSend$remoteLocaleIdentifier
+ _objc_msgSend$sendRequestID:options:request:responseHandler:
+ _objc_msgSend$sendRequestID:unencryptedRequestData:withTimeout:completion:
+ _objc_msgSend$setActive:
+ _objc_msgSend$setDeviceContext:
+ _objc_msgSend$setRemoteLocaleIdentifier:
+ _objc_msgSend$updateDeviceContext:
- +[DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController keyPathsForValuesAffectingBroadcasting]
- -[DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController isBroadcasting]
- -[DMTCatalystSharingBackedDeviceSession initWithDevice:]
- GCC_except_table12
- GCC_except_table13
- GCC_except_table23
- GCC_except_table27
- GCC_except_table31
- GCC_except_table36
- GCC_except_table40
- GCC_except_table9
- __OBJC_$_CLASS_METHODS_DMTBuddyDaemonProximityAutomatedDeviceEnrollmentController
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.10
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.10.cold.1
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.11
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.11.cold.1
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.11.cold.2
- ___54-[DMTSharingBroadcastPrimitives addDependencyHandlers]_block_invoke.13
- ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.11
- ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.11.cold.1
- ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.14
- ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.14.cold.1
- ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.9
- ___54-[DMTSharingDiscoveryPrimitives addDependencyHandlers]_block_invoke.9.cold.1
- ___61-[DMTCatalystSharingBackedDeviceSession addPrimitiveHandlers]_block_invoke.9
- ___61-[DMTCatalystSharingBackedDeviceSession addPrimitiveHandlers]_block_invoke_2.11
- ___61-[DMTCatalystSharingBackedDeviceSession addPrimitiveHandlers]_block_invoke_3.12
- ___65-[DMTCatalystSharingBackedDeviceSession beginPairWithCompletion:]_block_invoke
- ___65-[DMTCatalystSharingBackedDeviceSession beginPairWithCompletion:]_block_invoke.cold.1
- ___block_literal_global.123
CStrings:
+ "%{public}@ Calling sendRequestID: %{public}@"
+ "%{public}@ received response to sendRequestID:'%{public}@' (error: %{public}@, response: %{public}@)"
+ "%{public}@ timed out waiting for response to sendRequestID:'%{public}@'"
+ "%{public}@: isBroadcasting changed from %{public}@ to %{public}@"
+ "@\"NSLocale\""
+ "@\"NSObject<DMTRemoteSetupBroadcasting>\""
+ "Apple Vision"
+ "Apple Vision Pro Added"
+ "DMTPairingConstants"
+ "E"
+ "Failed to Add Apple Vision Pro"
+ "Ignoring %{public}@, already active"
+ "Ignoring %{public}@, not active"
+ "Ignoring updated Pin, no longer active"
+ "PreAuth request received non-dictionary object (%{public}@)"
+ "Received SFMessageRequestIDPreAuth request: %{public}@"
+ "Received locale identifier '%{public}@' from AC host"
+ "SFMessageRequestIDPreAuth inRequest is not a dictionary"
+ "T@\"NSDictionary\",C,N,V_deviceContext"
+ "T@\"NSLocale\",R,N,V_locale"
+ "T@\"NSObject<DMTRemoteSetupBroadcasting>\",&,N,V_broadcaster"
+ "T@\"NSString\",&,N,V_remoteLocaleIdentifier"
+ "T@\"NSString\",R"
+ "TB,N,GisActive,V_active"
+ "There was a problem adding this Apple Vision Pro. Double-click Digital Crown to erase Apple Vision Pro to try again."
+ "This Apple Vision Pro has been added to %@.\n\nAssign this iPad to a device management service in %@ to configure its enrollment settings and enable Automated Device Enrollment."
+ "This Apple Vision Pro will be added to %@ in %@."
+ "This device has been added to %@.\n\nAssign this device to a device management service in %@ to configure its enrollment settings and enable Automated Device Enrollment."
+ "This iPad has been added to %@.\n\nAssign this iPad to a device management service in %@ to configure its enrollment settings and enable Automated Device Enrollment."
+ "This iPhone has been added to %@.\n\nAssign this iPhone to a device management service in %@ to configure its enrollment settings and enable Automated Device Enrollment."
+ "_active"
+ "_deviceContext"
+ "_locale"
+ "_pa"
+ "_remoteLocaleIdentifier"
+ "active"
+ "allowUnencrypted"
+ "currentLocale"
+ "deregisterRequestID:"
+ "deviceContext"
+ "direct"
+ "initWithDevice:locale:"
+ "isActive"
+ "isEqualToNumber:"
+ "locID"
+ "locale"
+ "localeIdentifier"
+ "localeIdentifierKey"
+ "performPairingWithCompletion:"
+ "performPairingWithPreAuthWithCompletion:"
+ "productType"
+ "registerRequestID:options:handler:"
+ "remoteLocaleIdentifier"
+ "sendRequestID:options:request:responseHandler:"
+ "sendRequestID:unencryptedRequestData:withTimeout:completion:"
+ "setActive:"
+ "setDeviceContext:"
+ "setRemoteLocaleIdentifier:"
+ "updateDeviceContext:"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">24"
+ "v32@?0@\"NSError\"8@\"NSDictionary\"16@\"NSDictionary\"24"
+ "v48@0:8@16@24Q32@?40"
- "@\"<DMTRemoteSetupBroadcasting>\""
- "Ignoring %{public}@, already broadcasting"
- "Ignoring %{public}@, not broadcasting"
- "Ignoring updated Pin, no longer broadcasting"
- "T@\"<DMTRemoteSetupBroadcasting>\",&,N,V_broadcaster"
- "TB,R,N,GisBroadcasting"
- "This device has been added to %@.\n\nAssign this device to an MDM server in %@ to configure its enrollment settings and enable Automated Device Enrollment."
- "This iPad has been added to %@.\n\nAssign this iPad to an MDM server in %@ to configure its enrollment settings and enable Automated Device Enrollment."
- "This iPhone has been added to %@.\n\nAssign this iPhone to an MDM server in %@ to configure its enrollment settings and enable Automated Device Enrollment."
- "broadcaster.isBroadcasting"
- "keyPathsForValuesAffectingBroadcasting"

```
