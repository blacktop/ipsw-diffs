## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-410.1.0.0.0
-  __TEXT.__text: 0x927f8
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x5534
-  __TEXT.__const: 0x8c4
-  __TEXT.__oslogstring: 0x14096
-  __TEXT.__cstring: 0xdaae
+412.0.0.0.0
+  __TEXT.__text: 0x95f98
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_methlist: 0x568c
+  __TEXT.__const: 0x8c0
+  __TEXT.__oslogstring: 0x144ce
+  __TEXT.__cstring: 0xde05
   __TEXT.__gcc_except_tab: 0xc84
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__swift5_typeref: 0x341
-  __TEXT.__swift5_fieldmd: 0x98
-  __TEXT.__constg_swiftt: 0x1d0
+  __TEXT.__swift5_typeref: 0x3a9
+  __TEXT.__swift5_fieldmd: 0xb4
+  __TEXT.__constg_swiftt: 0x220
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x81
-  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_reflstr: 0x87
+  __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__swift5_capture: 0x1c8
-  __TEXT.__swift_as_entry: 0x5c
-  __TEXT.__swift_as_ret: 0x60
-  __TEXT.__unwind_info: 0x1d48
-  __TEXT.__eh_frame: 0x8d0
-  __TEXT.__objc_classname: 0xcbd
-  __TEXT.__objc_methname: 0xf30c
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift5_capture: 0x200
+  __TEXT.__swift_as_entry: 0x64
+  __TEXT.__swift_as_ret: 0x68
+  __TEXT.__unwind_info: 0x1e20
+  __TEXT.__eh_frame: 0x9b8
+  __TEXT.__objc_classname: 0xd0f
+  __TEXT.__objc_methname: 0xf59f
   __TEXT.__objc_methtype: 0x2987
-  __TEXT.__objc_stubs: 0xc500
-  __DATA_CONST.__got: 0x1098
-  __DATA_CONST.__const: 0x2630
-  __DATA_CONST.__objc_classlist: 0x288
+  __TEXT.__objc_stubs: 0xc600
+  __DATA_CONST.__got: 0x10c0
+  __DATA_CONST.__const: 0x26c8
+  __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3780
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x3840
+  __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x8ac0
-  __AUTH_CONST.__objc_const: 0xfc90
+  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__const: 0xc38
+  __AUTH_CONST.__cfstring: 0x8b80
+  __AUTH_CONST.__objc_const: 0x103a8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0xfd8
-  __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x3b0
-  __DATA.__data: 0x1198
-  __DATA.__bss: 0x8f0
+  __AUTH.__objc_data: 0x1138
+  __AUTH.__data: 0x128
+  __DATA.__objc_ivar: 0x3b4
+  __DATA.__data: 0x12a0
+  __DATA.__bss: 0x7d0
   __DATA_DIRTY.__objc_data: 0xa38
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x138
+  __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 060FB4CE-1A08-3C8D-A0FE-E9CB1BA6C65C
-  Functions: 3113
-  Symbols:   10068
-  CStrings:  6399
+  UUID: D356D9E0-D3E9-3269-AD12-9EDF7CA5319F
+  Functions: 3177
+  Symbols:   10172
+  CStrings:  6487
 
Symbols:
+ +[CDPDBootSessionIDProvider bootSessionUUID]
+ +[CDPDBootSessionIDProvider bootSessionUUID].cold.1
+ +[CDPRPDProbationDurationProvider _defaultProbationDurationForUserType:]
+ +[CDPRPDProbationDurationProvider _serverProbationDurationForUserType:rpdDurationConfigurations:]
+ +[CDPRPDProbationDurationProvider _userTypeForRecoveryContext:]
+ +[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]
+ -[CDPDManateeStateObserver deviceDidUnlockForTheFirstTime]
+ -[CDPDManateeStateObserver deviceDidUnlockForTheFirstTime].cold.1
+ -[CDPDManateeStateObserver deviceDidUnlockForTheFirstTime].cold.2
+ -[CDPDStateMachine _cachedRecoveryFlowContext]
+ GCC_except_table131
+ GCC_except_table26
+ GCC_except_table98
+ _OBJC_CLASS_$_CDPDBootSessionIDProvider
+ _OBJC_CLASS_$_CDPDFirstUnlockObserver
+ _OBJC_CLASS_$_CDPRPDProbationDurationProvider
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_CDPDStateMachine._recoveryFlowContext
+ _OBJC_METACLASS_$_CDPDBootSessionIDProvider
+ _OBJC_METACLASS_$_CDPDFirstUnlockObserver
+ _OBJC_METACLASS_$_CDPRPDProbationDurationProvider
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA_CDPDFirstUnlockObserver
+ __DATA__TtC15CoreCDPInternalP33_CCDB1C447E12AE43C6597553DD12C27C11UUIDWrapper
+ __INSTANCE_METHODS_CDPDFirstUnlockObserver
+ __IVARS_CDPDFirstUnlockObserver
+ __IVARS__TtC15CoreCDPInternalP33_CCDB1C447E12AE43C6597553DD12C27C11UUIDWrapper
+ __METACLASS_DATA_CDPDFirstUnlockObserver
+ __METACLASS_DATA__TtC15CoreCDPInternalP33_CCDB1C447E12AE43C6597553DD12C27C11UUIDWrapper
+ __OBJC_$_CLASS_METHODS_CDPDBootSessionIDProvider
+ __OBJC_$_CLASS_METHODS_CDPRPDProbationDurationProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CDPDFirstUnlockListener
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CDPDFirstUnlockListener
+ __OBJC_$_PROTOCOL_REFS_CDPDFirstUnlockListener
+ __OBJC_CLASS_RO_$_CDPDBootSessionIDProvider
+ __OBJC_CLASS_RO_$_CDPRPDProbationDurationProvider
+ __OBJC_LABEL_PROTOCOL_$_CDPDFirstUnlockListener
+ __OBJC_METACLASS_RO_$_CDPDBootSessionIDProvider
+ __OBJC_METACLASS_RO_$_CDPRPDProbationDurationProvider
+ __OBJC_PROTOCOL_$_CDPDFirstUnlockListener
+ __PROPERTIES_CDPDFirstUnlockObserver
+ __PROTOCOLS_CDPDFirstUnlockObserver
+ __PROTOCOLS_CDPDFirstUnlockObserver.2
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2122
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2122.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2123
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2123.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2186
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2186.cold.1
+ ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2186.cold.2
+ ___44+[CDPDBootSessionIDProvider bootSessionUUID]_block_invoke
+ ___44+[CDPDBootSessionIDProvider bootSessionUUID]_block_invoke.cold.1
+ ___44-[CDPDRecoveryFlowController beginRecovery:]_block_invoke.26
+ ___44-[CDPDRecoveryFlowController beginRecovery:]_block_invoke_2
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2187
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2189
+ ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2189.cold.1
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke.47
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke.49
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke.50
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke.cold.1
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke.cold.2
+ ___82+[CDPRPDProbationDurationProvider probationDurationForRecoveryContext:completion:]_block_invoke.cold.3
+ ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.73
+ ___86-[CDPDRecoveryValidatedJoinFlowController _handleNoRecoveryFactorsWithMask:validator:]_block_invoke.242
+ ___91-[CDPDStateMachine _isEligibleForRecoveryTokenWithContext:cdpStateMachineError:completion:]_block_invoke.47
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e8_v16?0d8ls32l8s40l8s56l8s48l8
+ ___block_literal_global.1017
+ ___block_literal_global.1028
+ ___block_literal_global.1132
+ ___block_literal_global.1179
+ ___block_literal_global.1259
+ ___block_literal_global.1288
+ ___block_literal_global.2091
+ ___block_literal_global.2103
+ ___block_literal_global.2119
+ ___block_literal_global.2191
+ ___block_literal_global.514
+ _bootSessionUUID._bootSessionUUID
+ _bootSessionUUID.onceToken
+ _flat unique So23CDPDFirstUnlockListener_p
+ _kAAFClickFollowupEvent
+ _objc_msgSend$_cachedRecoveryFlowContext
+ _objc_msgSend$_defaultProbationDurationForUserType:
+ _objc_msgSend$_serverProbationDurationForUserType:rpdDurationConfigurations:
+ _objc_msgSend$_userTypeForRecoveryContext:
+ _objc_msgSend$fetchRPDProbationDurationConfigsWithCompletion:
+ _objc_msgSend$hasViableICSC
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$isWalrusEnabled
+ _objc_msgSend$probationDurationForRecoveryContext:completion:
+ _objc_msgSend$setHasViableICSC:
+ _objc_msgSend$valueForKey:
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_getSingletonMetadata
+ _swift_updateClassMetadata2
+ _symbolic SccySb_____G s5NeverO
+ _symbolic So23CDPDFirstUnlockObserverC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 15CoreCDPInternal11UUIDWrapper33_CCDB1C447E12AE43C6597553DD12C27CLLC
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic ______p So23CDPDFirstUnlockListenerP
+ _symbolic ypSg
+ _sysctlbyname
- -[CDPDRecoveryFlowController beginInteractiveRecoveryForDevices:isUsingMultipleICSC:usingValidator:].cold.4
- -[CDPDRecoveryValidatedJoinFlowController _isProbationActive]
- -[CDPDRecoveryValidatedJoinFlowController _shouldOfferEDPRecoveryTokenBasedRecoveryWithCompletion:].cold.1
- -[CDPDRecoveryValidatedJoinFlowController _shouldOfferEDPRecoveryTokenBasedRecoveryWithCompletion:].cold.2
- -[CDPDRecoveryValidatedJoinFlowController _shouldOfferEDPRecoveryTokenBasedRecoveryWithCompletion:].cold.3
- GCC_except_table100
- GCC_except_table130
- GCC_except_table25
- GCC_except_table46
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2116
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2116.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2117
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2117.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2180
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2180.cold.1
- ___36-[CDPDAnalyticsTransport sendEvent:]_block_invoke.2180.cold.2
- ___44-[CDPDRecoveryFlowController beginRecovery:]_block_invoke.25
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke.2181
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2183
- ___81-[CDPDAnalyticsTransport configureSessionForEvent:sendEventBlock:telemetryQueue:]_block_invoke_2.2183.cold.1
- ___85-[CDPDRecoveryValidatedJoinFlowController _accountResetRecoveryOptionWithCompletion:]_block_invoke.74
- ___86-[CDPDRecoveryValidatedJoinFlowController _handleNoRecoveryFactorsWithMask:validator:]_block_invoke.243
- ___91-[CDPDStateMachine _isEligibleForRecoveryTokenWithContext:cdpStateMachineError:completion:]_block_invoke.46
- ___99-[CDPDRecoveryValidatedJoinFlowController _shouldOfferEDPRecoveryTokenBasedRecoveryWithCompletion:]_block_invoke
- ___99-[CDPDRecoveryValidatedJoinFlowController _shouldOfferEDPRecoveryTokenBasedRecoveryWithCompletion:]_block_invoke.cold.1
- ___block_literal_global.1011
- ___block_literal_global.1022
- ___block_literal_global.1126
- ___block_literal_global.1173
- ___block_literal_global.1253
- ___block_literal_global.1282
- ___block_literal_global.2085
- ___block_literal_global.2097
- ___block_literal_global.2113
- ___block_literal_global.2185
- ___block_literal_global.508
- _objc_msgSend$_isProbationActive
- _objc_msgSend$cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:
- _objc_msgSend$rpdProbationDuration
- _objc_msgSend$rpdProbationIsInEffectForDuration:context:
- _symbolic Si
CStrings:
+ "%{public}s - Checking if current device unlocked for the first time..."
+ "%{public}s - Could not get boot session UUID. Not treating as first unlock."
+ "%{public}s - Current boot session ID is different than the one we saved, meaning we have rebooted. This is first unlock."
+ "%{public}s - device is not unlocked. Found lock state %{public}d."
+ "%{public}s - device is unlocked but no saved boot session ID was found. Acting as first unlock."
+ "%{public}s device is unlocked but boot session ID (%s) did not change."
+ "%{public}s ignoring notification event '%{public}s'"
+ "%{public}s received a nil eventName"
+ "%{public}s recognizes first unlock. Notifying listeners and saving boot ID."
+ "?"
+ "@\"AKURLBag\""
+ "@\"CDPLocalDevice\""
+ "@\"NSUserDefaults\""
+ "Broadcasting Manatee availability"
+ "CDPDBootSessionIDProvider"
+ "CDPDFirstUnlockListener"
+ "CDPDFirstUnlockObserver"
+ "CDPRPDProbationDurationProvider"
+ "CoreCDPInternal_Bridged.FirstUnlockObserver"
+ "Could not convert %{public}s to UUID"
+ "Could not get boot session UUID. Not notifying listeners of first unlock."
+ "Device did not unlock for the first time. Ignoring lock status event"
+ "Failed to create Manatee controller. Not posting notification."
+ "Failed to retrieve boot session UUID with exit code %d"
+ "Fetching manatee status for primary account after first unlock"
+ "Found MobileKeyBag's first unlock notification."
+ "Kill switch is on. Ignoring computed first unlock through lock state listener"
+ "Ledger: probationDuration: %f"
+ "Manatee is not available due to error: %@"
+ "No saved boot session ID"
+ "Not posting manatee notification after first unlock. isSharediPad=%{BOOL}d, isPrimaryAccount=%{BOOL}d"
+ "Notifying listener %{public}s of first unlock"
+ "Probation days is nil, falling back to default values. Error: %@"
+ "RPD Config is nil, falling back to default values. Error: %@"
+ "Saved boot session ID is %{public}s"
+ "T@\"AKURLBag\",N,R,VurlBag"
+ "T@\"CDPLocalDevice\",N,R,VlocalDevice"
+ "T@\"NSArray\",N,C"
+ "T@\"NSUUID\",N,R"
+ "T@\"NSUserDefaults\",N,R,VuserDefaults"
+ "Updating saved boot session ID to %{public}s"
+ "Using Probation days from url bag"
+ "_TtC15CoreCDPInternalP33_CCDB1C447E12AE43C6597553DD12C27C11UUIDWrapper"
+ "_cachedRecoveryFlowContext"
+ "_defaultProbationDurationForUserType:"
+ "_recoveryFlowContext"
+ "_serverProbationDurationForUserType:rpdDurationConfigurations:"
+ "_userTypeForRecoveryContext:"
+ "adpWithNoViableICSC"
+ "adpWithViableICSC"
+ "bootSessionID"
+ "bootSessionIDWrapper"
+ "bootSessionUUID"
+ "cdpWithNoViableICSC"
+ "cdpWithViableICSC"
+ "com.apple.corecdp.bootSessionID"
+ "com.apple.mobile.keybagd.first_unlock"
+ "com.apple.mobile.keybagd.lock_status"
+ "com.apple.pcs.enrollRecoveryToken"
+ "com.apple.security.octagonTrustLost"
+ "currentDeviceUnlockedForTheFirstTime"
+ "currentLockState"
+ "deviceDidUnlockForTheFirstTime"
+ "fetchRPDProbationDurationConfigsWithCompletion:"
+ "hasViableICSC"
+ "initWithUTF8String:"
+ "initWithUUIDString:"
+ "initWithUserDefaults:localDevice:bootSessionID:"
+ "initWithUserDefaults:urlBag:localDevice:bootSessionID:"
+ "isManateeNotificationOnFirstUnlockEnabledUsingURLBag:completion:"
+ "kern.bootsessionuuid"
+ "localDevice"
+ "probationDurationForRecoveryContext:completion:"
+ "reactTo:"
+ "recognizeFirstUnlockWith:"
+ "savedBootSessionID"
+ "setHasViableICSC:"
+ "updateSavedBootSessionIDTo:"
+ "urlBag"
+ "userDefaults"
+ "v16@?0d8"
+ "v24@0:8r*16"
+ "valueForKey:"
- "%s: recoveryTokenNeeded=%{BOOL}d, error=%@"
- "-[CDPDRecoveryValidatedJoinFlowController _shouldOfferEDPRecoveryTokenBasedRecoveryWithCompletion:]_block_invoke"
- "Beginning initial password based repair if needed"
- "Interactive recovery with EDP status - %lu"
- "Invoking cdpContext:promptForRemoteSecretWithDevices in CDPDRecoveryFlowController"
- "Ledger: CLI asked for a force EDP reset. Overriding all other checks."
- "Ledger: edpRPDBlockingError - Finding first unsatisfied requirement in conditions: %s"
- "Ledger: edpRPDBlockingError - context is nil"
- "Ledger: isProbationCheckRequired: %{bool}d."
- "Ledger: rpdProbationDuration is not set. Deafulting to CDPRPDProbationTimeInterval"
- "User is Walrus enabled, will not use EDP Recovery Token as an escape offer..."
- "_isProbationActive"
- "cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:"
- "isRequiredContext=%{BOOL}d because CDPContextType is %ld"

```
