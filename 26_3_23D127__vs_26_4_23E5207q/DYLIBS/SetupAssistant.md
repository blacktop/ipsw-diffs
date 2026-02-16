## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5381.3.1.0.0
-  __TEXT.__text: 0x456b4
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x4124
-  __TEXT.__const: 0x138
-  __TEXT.__gcc_except_tab: 0x1158
-  __TEXT.__oslogstring: 0x58e9
-  __TEXT.__cstring: 0x30c4
+5382.4.7.0.0
+  __TEXT.__text: 0x482ac
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_methlist: 0x417c
+  __TEXT.__const: 0x130
+  __TEXT.__gcc_except_tab: 0x1140
+  __TEXT.__oslogstring: 0x5927
+  __TEXT.__cstring: 0x33b8
   __TEXT.__dlopen_cstrs: 0x138b
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x1338
-  __TEXT.__objc_classname: 0x8ca
-  __TEXT.__objc_methname: 0xb1bc
-  __TEXT.__objc_methtype: 0x1254
-  __TEXT.__objc_stubs: 0x88c0
-  __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x1718
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__unwind_info: 0x14e8
+  __TEXT.__objc_classname: 0x8da
+  __TEXT.__objc_methname: 0xb2c0
+  __TEXT.__objc_methtype: 0x1262
+  __TEXT.__objc_stubs: 0x8940
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x1758
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bf8
+  __DATA_CONST.__objc_selrefs: 0x2c28
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0x61c0
+  __AUTH_CONST.__cfstring: 0x3a60
+  __AUTH_CONST.__objc_const: 0x6288
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3c8
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x3cc
   __DATA.__data: 0xa90
   __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A13ED24-D790-3634-AC53-ED11EA0C8377
-  Functions: 1772
-  Symbols:   6500
-  CStrings:  3652
+  UUID: 80D91AC9-C7FF-3649-BF34-6F00A6142CA5
+  Functions: 1793
+  Symbols:   6599
+  CStrings:  3713
 
Symbols:
+ +[BYEnumUtilities humanReadableStringForD2DCancellationCause:]
+ +[BYEnumUtilities humanReadableStringForProximitySetupFinishCause:]
+ -[BYDeviceMigrationManager cancelWithCause:proximitySetupFinishCause:]
+ -[BYDeviceMigrationManager proximitySetupFinishCause]
+ -[BYDeviceMigrationManager setProximitySetupFinishCause:]
+ -[BuddyFeatureFlags isNewRestoreSUFlowEnabled]
+ -[BuddyFeatureFlags isSDPAutoEnablementEnabled]
+ _BYAssistantUserHasSeenSiri
+ _OBJC_CLASS_$_BYEnumUtilities
+ _OBJC_IVAR_$_BYDeviceMigrationManager._proximitySetupFinishCause
+ _OBJC_METACLASS_$_BYEnumUtilities
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_CLASS_METHODS_BYEnumUtilities
+ __OBJC_CLASS_RO_$_BYEnumUtilities
+ __OBJC_METACLASS_RO_$_BYEnumUtilities
+ ___54-[BYDeviceMigrationManager restartDeviceTransferTask:]_block_invoke.11
+ ___54-[BYDeviceMigrationManager restartDeviceTransferTask:]_block_invoke.11.cold.1
+ ___70-[BYDeviceMigrationManager cancelWithCause:proximitySetupFinishCause:]_block_invoke
+ ___BYDaemonCreateMetadataArchive_block_invoke.373
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$cancelWithCause:proximitySetupFinishCause:
+ _objc_msgSend$humanReadableStringForD2DCancellationCause:
+ _objc_msgSend$humanReadableStringForProximitySetupFinishCause:
+ _objc_msgSend$setProximitySetupFinishCause:
- -[BuddyFeatureFlags isMDMEnrollmentFlowControllerAdoptionEnabled]
- GCC_except_table26
- _BYPrivacySubscriptionBundleIdentifier
- ___44-[BYDeviceMigrationManager cancelWithCause:]_block_invoke
- ___54-[BYDeviceMigrationManager restartDeviceTransferTask:]_block_invoke.10
- ___54-[BYDeviceMigrationManager restartDeviceTransferTask:]_block_invoke.10.cold.1
- ___BYDaemonCreateMetadataArchive_block_invoke.322
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "App termination"
+ "BYEnumUtilities"
+ "Backup failed"
+ "Cancellation cause is not specified"
+ "Cancelling device to device migration with cancellation cause: %ld (%{public}@)..."
+ "Cancelling migration with finish cause: %{public}@ (%lu)"
+ "Connection lost"
+ "Dependent sign-in failed"
+ "Dependent sign-in succeeded"
+ "DimpleKey_AutoEnablement"
+ "Erasing device"
+ "Express restore customize tapped"
+ "Failed to determine software update availability"
+ "Mandatory update install started"
+ "Mandatory update required"
+ "Migration is not supported"
+ "NewBuddyRestoreSUFlow"
+ "No additional data is needed from source device"
+ "Passcode validation canceled by user"
+ "Personal sign-in failed"
+ "Preexisting connection"
+ "Proximity connection terminated"
+ "Setting Siri data sharing opt-in to %ld"
+ "Skipped due to Cloud Config"
+ "Software Update not found"
+ "SoftwareUpdateUI"
+ "TQ,N,V_proximitySetupFinishCause"
+ "Target disconnected from source device"
+ "Unknown cancellation cause"
+ "User chose to restore from another iOS device"
+ "User chose to start over"
+ "User initiated cancellation from source"
+ "User selected Cloud or Other transfer option"
+ "_proximitySetupFinishCause"
+ "cancelWithCause:proximitySetupFinishCause:"
+ "humanReadableStringForD2DCancellationCause:"
+ "humanReadableStringForProximitySetupFinishCause:"
+ "isNewRestoreSUFlowEnabled"
+ "isSDPAutoEnablementEnabled"
+ "proximitySetupFinishCause"
+ "setProximitySetupFinishCause:"
+ "v32@0:8q16Q24"
- "Cancelling device to device migration with cancellation cause: %ld..."
- "MDMFlowControllerAdoption"
- "Setting Siri data sharing opt-in to %{public}ld"
- "com.apple.onboarding.subscriptionbundle"
- "isMDMEnrollmentFlowControllerAdoptionEnabled"

```
