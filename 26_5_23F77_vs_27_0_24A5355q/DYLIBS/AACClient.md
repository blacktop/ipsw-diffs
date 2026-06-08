## AACClient

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient`

```diff

-28.122.2.0.0
-  __TEXT.__text: 0x1c0f4
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0xd00
-  __TEXT.__const: 0x18d0
-  __TEXT.__cstring: 0x4cb
-  __TEXT.__swift5_typeref: 0xf7f
-  __TEXT.__swift5_reflstr: 0xb7b
+50.0.0.0.0
+  __TEXT.__text: 0x218d4
+  __TEXT.__objc_methlist: 0x1318
+  __TEXT.__const: 0x1910
+  __TEXT.__cstring: 0x4eb
+  __TEXT.__swift5_typeref: 0xfa5
+  __TEXT.__swift5_reflstr: 0xf6b
   __TEXT.__swift5_assocty: 0xf8
-  __TEXT.__constg_swiftt: 0x1580
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_fieldmd: 0xa3c
+  __TEXT.__constg_swiftt: 0x18a0
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_fieldmd: 0xbbc
   __TEXT.__swift5_proto: 0xc4
-  __TEXT.__swift5_types: 0xb8
-  __TEXT.__swift5_capture: 0x628
+  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift5_capture: 0x614
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__oslogstring: 0x61b
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x8a0
-  __TEXT.__eh_frame: 0x428
-  __TEXT.__objc_classname: 0x769
-  __TEXT.__objc_methname: 0x2406
-  __TEXT.__objc_methtype: 0x9e7
-  __TEXT.__objc_stubs: 0xee0
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x1c0
+  __TEXT.__swift_as_cont: 0x30
+  __TEXT.__unwind_info: 0xa10
+  __TEXT.__eh_frame: 0x430
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x840
-  __AUTH_CONST.__const: 0x1ce8
-  __AUTH_CONST.__objc_const: 0x24e8
-  __AUTH.__objc_data: 0x7c0
+  __DATA_CONST.__got: 0x2b0
+  __AUTH_CONST.__const: 0x1cb8
+  __AUTH_CONST.__objc_const: 0x3108
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH.__objc_data: 0xbc0
   __AUTH.__data: 0xde0
-  __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x12b8
+  __DATA.__objc_ivar: 0xe0
+  __DATA.__data: 0x13c8
   __DATA.__bss: 0x1080
   __DATA.__common: 0x80
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D512D6AB-97CF-3EA0-BF34-84190642B4E7
-  Functions: 987
-  Symbols:   1130
-  CStrings:  501
+  UUID: B7B48E69-E3BC-3F04-84AE-C6C16F2ECEBE
+  Functions: 1375
+  Symbols:   1530
+  CStrings:  48
 
Symbols:
+ -[AECAssessmentConfigurationWrapper _allowedCollaborationIDs]
+ -[AECAssessmentConfigurationWrapper _allowsAirPlay]
+ -[AECAssessmentConfigurationWrapper _allowsDonatingClipboardHistoryToSpotlight]
+ -[AECAssessmentConfigurationWrapper _allowsSharingServices]
+ -[AECAssessmentConfigurationWrapper _allowsSpotlight]
+ -[AECAssessmentConfigurationWrapper allowLockdownMode]
+ -[AECAssessmentConfigurationWrapper allowOnlyParticipantsToRun]
+ -[AECAssessmentConfigurationWrapper allowPrivateRelay]
+ -[AECAssessmentConfigurationWrapper allowedAppleMenuItems]
+ -[AECAssessmentConfigurationWrapper allowedBluetoothDeviceNames]
+ -[AECAssessmentConfigurationWrapper allowedBluetoothProfiles]
+ -[AECAssessmentConfigurationWrapper allowedDirectoriesAndFiles]
+ -[AECAssessmentConfigurationWrapper allowedMenuBarItems]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityAlternativeInputMethods]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityBackgroundSounds]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityHoverText]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityLiveSpeech]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilitySpokenContent]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilitySwitchControl]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityVoiceControl]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityVoiceOver]
+ -[AECAssessmentConfigurationWrapper allowsAccessibilityZoom]
+ -[AECAssessmentConfigurationWrapper allowsAutoFill]
+ -[AECAssessmentConfigurationWrapper allowsDock]
+ -[AECAssessmentConfigurationWrapper allowsMenuBar]
+ -[AECAssessmentConfigurationWrapper allowsStructuralInput]
+ -[AECAssessmentConfigurationWrapper allowsUserScriptExecution]
+ -[AECAssessmentConfigurationWrapper maxBluetoothDevicesAllowed]
+ -[AECAssessmentConfigurationWrapper requiresManagedDevice]
+ -[AECAssessmentConfigurationWrapper requiresSIP]
+ -[AECAssessmentConfigurationWrapper requiresSingleUser]
+ -[AECAssessmentConfigurationWrapper requiresUserAccountType]
+ -[AECAssessmentConfigurationWrapper setAllowLockdownMode:]
+ -[AECAssessmentConfigurationWrapper setAllowOnlyParticipantsToRun:]
+ -[AECAssessmentConfigurationWrapper setAllowPrivateRelay:]
+ -[AECAssessmentConfigurationWrapper setAllowedAppleMenuItems:]
+ -[AECAssessmentConfigurationWrapper setAllowedBluetoothDeviceNames:]
+ -[AECAssessmentConfigurationWrapper setAllowedBluetoothProfiles:]
+ -[AECAssessmentConfigurationWrapper setAllowedDirectoriesAndFiles:]
+ -[AECAssessmentConfigurationWrapper setAllowedMenuBarItems:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityAlternativeInputMethods:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityBackgroundSounds:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityHoverText:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityLiveSpeech:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilitySpokenContent:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilitySwitchControl:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityVoiceControl:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityVoiceOver:]
+ -[AECAssessmentConfigurationWrapper setAllowsAccessibilityZoom:]
+ -[AECAssessmentConfigurationWrapper setAllowsAutoFill:]
+ -[AECAssessmentConfigurationWrapper setAllowsDock:]
+ -[AECAssessmentConfigurationWrapper setAllowsMenuBar:]
+ -[AECAssessmentConfigurationWrapper setAllowsStructuralInput:]
+ -[AECAssessmentConfigurationWrapper setAllowsUserScriptExecution:]
+ -[AECAssessmentConfigurationWrapper setMaxBluetoothDevicesAllowed:]
+ -[AECAssessmentConfigurationWrapper setRequiresManagedDevice:]
+ -[AECAssessmentConfigurationWrapper setRequiresSIP:]
+ -[AECAssessmentConfigurationWrapper setRequiresSingleUser:]
+ -[AECAssessmentConfigurationWrapper setRequiresUserAccountType:]
+ -[AECAssessmentConfigurationWrapper set_allowedCollaborationIDs:]
+ -[AECAssessmentConfigurationWrapper set_allowsAirPlay:]
+ -[AECAssessmentConfigurationWrapper set_allowsDonatingClipboardHistoryToSpotlight:]
+ -[AECAssessmentConfigurationWrapper set_allowsSharingServices:]
+ -[AECAssessmentConfigurationWrapper set_allowsSpotlight:]
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper.__allowedCollaborationIDs
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper.__allowsAirPlay
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper.__allowsDonatingClipboardHistoryToSpotlight
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper.__allowsSharingServices
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper.__allowsSpotlight
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowLockdownMode
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowOnlyParticipantsToRun
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowPrivateRelay
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowedAppleMenuItems
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowedBluetoothDeviceNames
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowedBluetoothProfiles
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowedDirectoriesAndFiles
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowedMenuBarItems
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityAlternativeInputMethods
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityBackgroundSounds
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityHoverText
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityLiveSpeech
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilitySpokenContent
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilitySwitchControl
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityVoiceControl
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityVoiceOver
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAccessibilityZoom
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsAutoFill
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsDock
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsMenuBar
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsStructuralInput
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsUserScriptExecution
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._maxBluetoothDevicesAllowed
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._requiresManagedDevice
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._requiresSIP
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._requiresSingleUser
+ _OBJC_IVAR_$_AECAssessmentConfigurationWrapper._requiresUserAccountType
+ __OBJC_$_PROP_LIST_AEFeatureFlags
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AEFeatureFlags
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AEFeatureFlags
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.104
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.15
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.19
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.21
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.33
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.35Tm
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.4
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.49
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.57
+ ___swift_closure_destructor.60
+ ___swift_closure_destructor.63
+ ___swift_closure_destructor.66
+ ___swift_closure_destructor.69
+ ___swift_closure_destructor.7
+ ___swift_closure_destructor.72
+ ___swift_closure_destructor.75
+ ___swift_closure_destructor.81
+ ___swift_closure_destructor.87
+ ___swift_closure_destructor.90
+ ___swift_closure_destructor.94
+ ___swift_closure_destructorTm
+ ___swift_exist.box.addr_destructor
+ ___swift_exist.box.addr_destructor.110
+ ___swift_exist.box.addr_destructor.113
+ ___swift_exist.box.addr_destructorTm
+ _block_copy_helper.100
+ _block_copy_helper.106
+ _block_copy_helper.14
+ _block_copy_helper.21
+ _block_copy_helper.27
+ _block_copy_helper.77
+ _block_copy_helper.83
+ _block_copy_helper.96
+ _block_descriptor.102
+ _block_descriptor.108
+ _block_descriptor.16
+ _block_descriptor.23
+ _block_descriptor.29
+ _block_descriptor.79
+ _block_descriptor.85
+ _block_descriptor.98
+ _block_destroy_helper.101
+ _block_destroy_helper.107
+ _block_destroy_helper.15
+ _block_destroy_helper.22
+ _block_destroy_helper.28
+ _block_destroy_helper.78
+ _block_destroy_helper.84
+ _block_destroy_helper.97
+ _keypath_get.107Tm
+ _keypath_get.51Tm
+ _keypath_set.106Tm
+ _keypath_set.52Tm
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_allowedCollaborationIDs
+ _objc_msgSend$_allowsAirPlay
+ _objc_msgSend$_allowsDonatingClipboardHistoryToSpotlight
+ _objc_msgSend$_allowsSharingServices
+ _objc_msgSend$_allowsSpotlight
+ _objc_msgSend$allowLockdownMode
+ _objc_msgSend$allowOnlyParticipantsToRun
+ _objc_msgSend$allowPrivateRelay
+ _objc_msgSend$allowedAppleMenuItems
+ _objc_msgSend$allowedBluetoothDeviceNames
+ _objc_msgSend$allowedBluetoothProfiles
+ _objc_msgSend$allowedDirectoriesAndFiles
+ _objc_msgSend$allowedMenuBarItems
+ _objc_msgSend$allowsAccessibilityAlternativeInputMethods
+ _objc_msgSend$allowsAccessibilityBackgroundSounds
+ _objc_msgSend$allowsAccessibilityHoverText
+ _objc_msgSend$allowsAccessibilityLiveSpeech
+ _objc_msgSend$allowsAccessibilitySpokenContent
+ _objc_msgSend$allowsAccessibilitySwitchControl
+ _objc_msgSend$allowsAccessibilityVoiceControl
+ _objc_msgSend$allowsAccessibilityVoiceOver
+ _objc_msgSend$allowsAccessibilityZoom
+ _objc_msgSend$allowsAutoFill
+ _objc_msgSend$allowsDock
+ _objc_msgSend$allowsMenuBar
+ _objc_msgSend$allowsStructuralInput
+ _objc_msgSend$allowsUserScriptExecution
+ _objc_msgSend$maxBluetoothDevicesAllowed
+ _objc_msgSend$requiresManagedDevice
+ _objc_msgSend$requiresSIP
+ _objc_msgSend$requiresSingleUser
+ _objc_msgSend$requiresUserAccountType
+ _objc_msgSend$setAllowLockdownMode:
+ _objc_msgSend$setAllowOnlyParticipantsToRun:
+ _objc_msgSend$setAllowPrivateRelay:
+ _objc_msgSend$setAllowedAppleMenuItems:
+ _objc_msgSend$setAllowedBluetoothDeviceNames:
+ _objc_msgSend$setAllowedBluetoothProfiles:
+ _objc_msgSend$setAllowedDirectoriesAndFiles:
+ _objc_msgSend$setAllowedMenuBarItems:
+ _objc_msgSend$setAllowsAccessibilityAlternativeInputMethods:
+ _objc_msgSend$setAllowsAccessibilityBackgroundSounds:
+ _objc_msgSend$setAllowsAccessibilityHoverText:
+ _objc_msgSend$setAllowsAccessibilityLiveSpeech:
+ _objc_msgSend$setAllowsAccessibilitySpokenContent:
+ _objc_msgSend$setAllowsAccessibilitySwitchControl:
+ _objc_msgSend$setAllowsAccessibilityVoiceControl:
+ _objc_msgSend$setAllowsAccessibilityVoiceOver:
+ _objc_msgSend$setAllowsAccessibilityZoom:
+ _objc_msgSend$setAllowsAutoFill:
+ _objc_msgSend$setAllowsDock:
+ _objc_msgSend$setAllowsMenuBar:
+ _objc_msgSend$setAllowsStructuralInput:
+ _objc_msgSend$setAllowsUserScriptExecution:
+ _objc_msgSend$setMaxBluetoothDevicesAllowed:
+ _objc_msgSend$setRequiresManagedDevice:
+ _objc_msgSend$setRequiresSIP:
+ _objc_msgSend$setRequiresSingleUser:
+ _objc_msgSend$setRequiresUserAccountType:
+ _objc_msgSend$set_allowedCollaborationIDs:
+ _objc_msgSend$set_allowsAirPlay:
+ _objc_msgSend$set_allowsDonatingClipboardHistoryToSpotlight:
+ _objc_msgSend$set_allowsSharingServices:
+ _objc_msgSend$set_allowsSpotlight:
+ _objc_release_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_setProperty_nonatomic_copy
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x10
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ShySSGSg
+ _symbolic _____ 8Catalyst18CATAsyncSerializerC
+ _symbolic _____ So21AECoreUserAccountTypeV
+ _symbolic _____Sg 8Catalyst18CATAsyncSerializerC16PreEnqueueActionO
- _block_copy_helper.102
- _block_copy_helper.108
- _block_copy_helper.15
- _block_copy_helper.22
- _block_copy_helper.28
- _block_copy_helper.79
- _block_copy_helper.85
- _block_copy_helper.98
- _block_descriptor.100
- _block_descriptor.104
- _block_descriptor.110
- _block_descriptor.17
- _block_descriptor.24
- _block_descriptor.30
- _block_descriptor.81
- _block_descriptor.87
- _block_destroy_helper.103
- _block_destroy_helper.109
- _block_destroy_helper.16
- _block_destroy_helper.23
- _block_destroy_helper.29
- _block_destroy_helper.80
- _block_destroy_helper.86
- _block_destroy_helper.99
- _keypath_get.22Tm
- _keypath_set.23Tm
- _objc_retain_x27
- _objectdestroy.36Tm
- _objectdestroy.5Tm
- _objectdestroy.9Tm
- _swift_unknownObjectRelease_n
- _symbolic _____ 8Catalyst13CATSerializerC
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "2"
- "?"
- "@\"<AECAssessmentSessionWrapperDelegate>\""
- "@\"<AEDObservation>\"24@0:8@?<v@?>16"
- "@\"<AEDWindow>\"24@0:8q16"
- "@\"<AEObservation>\"40@0:8@\"NSString\"16@\"OS_dispatch_queue\"24@?<v@?>32"
- "@\"<AEPerformancePrimitivesInFlightInterval>\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"<AEPolicyDeactivation>\"24@0:8@\"<AEPolicyReadOnlyScratchpad>\"16"
- "@\"<AEPolicyReadOnlyScratchpad><AERemovable>\"24@0:8@\"NSString\"16"
- "@\"<AEPolicyWriteOnlyScratchpad><AEPersistable>\"24@0:8@\"NSString\"16"
- "@\"AEAssessmentIndividualConfiguration\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"NSString\"16"
- "@\"NSMutableDictionary\""
- "@\"NSNumber\"24@0:8@\"NSString\"16"
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"_TtC9AACClient20AECAssessmentSession\""
- "@\"_TtC9AACClient26AECAssessmentConfiguration\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "AACClient"
- "AACClient1"
- "AECAssessmentConfigurationWrapper"
- "AECAssessmentSessionWrapper"
- "AECPublicErrorsWrapper"
- "AEDObservation"
- "AEDSingleAppModePrimitives"
- "AEDSingleAppModeSession"
- "AEDUIPrimitives"
- "AEDWindow"
- "AEDWindowPrimitives"
- "AEDevicePrimitives"
- "AEFeatureFlags"
- "AELifecycleEventHandling"
- "AEPerformancePrimitives"
- "AEPersistable"
- "AEPolicyAction"
- "AEPolicyActivation"
- "AEPolicyDeactivation"
- "AEPolicyReadOnlyScratchpad"
- "AEPolicySession"
- "AEPolicyStore"
- "AEPolicyWriteOnlyScratchpad"
- "AEPreferencePrimitives"
- "AEProcessInfoPrimitives"
- "AERemovable"
- "AESystemNotificationPrimitives"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<AECAssessmentSessionWrapperDelegate>\",W,N,V_delegate"
- "T@\"<_TtP9AACClient28AECAssessmentSessionDelegate_>\",N,W,Vdelegate"
- "T@\"AEAssessmentIndividualConfiguration\",C,N,V_mainIndividualConfiguration"
- "T@\"AEAssessmentIndividualConfiguration\",N,&,VmainIndividualConfiguration"
- "T@\"AECAssessmentConfigurationWrapper\",R,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSDictionary\",N,C"
- "T@\"NSMutableDictionary\",C,N,V_configurationsByApplicationDescriptor"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"_TtC9AACClient20AECAssessmentSession\",R,N,V_session"
- "T@\"_TtC9AACClient26AECAssessmentConfiguration\",N,&,Vconfiguration"
- "TB,N,R"
- "TB,N,R,Vexists"
- "TB,N,R,VhasPersistentData"
- "TB,N,S_setAllowsContentCapture:,V__allowsContentCapture"
- "TB,N,S_setAllowsNetworkAccess:,V__allowsNetworkAccess"
- "TB,N,V_allowsAccessibilityKeyboard"
- "TB,N,V_allowsAccessibilityLiveCaptions"
- "TB,N,V_allowsAccessibilityReader"
- "TB,N,V_allowsAccessibilitySpeech"
- "TB,N,V_allowsAccessibilityTypingFeedback"
- "TB,N,V_allowsActivityContinuation"
- "TB,N,V_allowsAutoCorrection"
- "TB,N,V_allowsContentCapture"
- "TB,N,V_allowsContinuousPathKeyboard"
- "TB,N,V_allowsDictation"
- "TB,N,V_allowsEmojiKeyboard"
- "TB,N,V_allowsKeyboardMathSolving"
- "TB,N,V_allowsKeyboardShortcuts"
- "TB,N,V_allowsMathPaperSolving"
- "TB,N,V_allowsNetworkAccess"
- "TB,N,V_allowsPasswordAutoFill"
- "TB,N,V_allowsPredictiveKeyboard"
- "TB,N,V_allowsScreenshots"
- "TB,N,V_allowsSmartPunctuation"
- "TB,N,V_allowsSpellCheck"
- "TB,N,VallowsAccessibilityKeyboard"
- "TB,N,VallowsAccessibilityLiveCaptions"
- "TB,N,VallowsAccessibilityReader"
- "TB,N,VallowsAccessibilitySpeech"
- "TB,N,VallowsAccessibilityTypingFeedback"
- "TB,N,VallowsActivityContinuation"
- "TB,N,VallowsAutoCorrection"
- "TB,N,VallowsContinuousPathKeyboard"
- "TB,N,VallowsDictation"
- "TB,N,VallowsEmojiKeyboard"
- "TB,N,VallowsKeyboardMathSolving"
- "TB,N,VallowsKeyboardShortcuts"
- "TB,N,VallowsMathPaperSolving"
- "TB,N,VallowsPasswordAutoFill"
- "TB,N,VallowsPredictiveKeyboard"
- "TB,N,VallowsScreenshots"
- "TB,N,VallowsSmartPunctuation"
- "TB,N,VallowsSpellCheck"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisActive"
- "TB,R,N,GisFailable"
- "TB,R,N,GisVisible"
- "TQ,R"
- "Td,R"
- "Tq,N,R"
- "Tq,R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC9AACClient12AECTaskQueue"
- "_TtC9AACClient15AECPublicErrors"
- "_TtC9AACClient18AECNoOpPolicyStore"
- "_TtC9AACClient20AECAssessmentSession"
- "_TtC9AACClient21AECLifetimeConnection"
- "_TtC9AACClient23AECSingleAppModeToggler"
- "_TtC9AACClient25AECAssessmentStateConduit"
- "_TtC9AACClient26AECAssessmentConfiguration"
- "_TtC9AACClient33AECWindowContentCaptureController"
- "_TtC9AACClient36AECParticipantConfigurationValidator"
- "_TtC9AACClient38AECConcreteRestrictedContentPrimitives"
- "_TtC9AACClient40AECAutocorrectModeConfigurationValidator"
- "_TtC9AACClient40AECUnionAssessmentConfigurationValidator"
- "_TtC9AACClient42AECAssessmentConfigurationValidatorFactory"
- "_TtC9AACClientP33_16674D75A621CF5D8821BE5D8D8594FC43AECConcreteRestrictedWindowContentAssertion"
- "_TtC9AACClientP33_5888192FE4890FBCEE84B63B946F5CEA26AECAssessmentModeAssertion"
- "_TtC9AACClientP33_6F4724F3B2C765B7F0AFE9E03A88CB2826RestrictedContentAssertion"
- "_TtC9AACClientP33_8E57ACA1EB1F0A0CB8F6ADAE6EA7784123AECNoOpPolicyScratchpad"
- "_TtC9AACClientP33_EFD39109592C6EDA2BBCB1B6AD748AF525AECPolicyActivationRunner"
- "_TtC9AACClientP33_EFD39109592C6EDA2BBCB1B6AD748AF527AECPolicyDeactivationRunner"
- "_TtP9AACClient28AECAssessmentSessionDelegate_"
- "__allowsContentCapture"
- "__allowsNetworkAccess"
- "_allowsAccessibilityKeyboard"
- "_allowsAccessibilityLiveCaptions"
- "_allowsAccessibilityReader"
- "_allowsAccessibilitySpeech"
- "_allowsAccessibilityTypingFeedback"
- "_allowsActivityContinuation"
- "_allowsAutoCorrection"
- "_allowsContentCapture"
- "_allowsContinuousPathKeyboard"
- "_allowsDictation"
- "_allowsEmojiKeyboard"
- "_allowsKeyboardMathSolving"
- "_allowsKeyboardShortcuts"
- "_allowsMathPaperSolving"
- "_allowsNetworkAccess"
- "_allowsPasswordAutoFill"
- "_allowsPredictiveKeyboard"
- "_allowsScreenshots"
- "_allowsSmartPunctuation"
- "_allowsSpellCheck"
- "_configurationsByApplicationDescriptor"
- "_delegate"
- "_mainIndividualConfiguration"
- "_session"
- "_setAllowsContentCapture:"
- "_setAllowsNetworkAccess:"
- "activateSessionWithCompletion:"
- "activateSingleAppModeSessionWithConfiguration:completion:"
- "activateWithScratchpad:invalidationHandler:completion:"
- "activation"
- "active"
- "ae_verboseDescription"
- "allowsAccessibilityKeyboard"
- "allowsAccessibilityLiveCaptions"
- "allowsAccessibilityReader"
- "allowsAccessibilitySpeech"
- "allowsAccessibilityTypingFeedback"
- "allowsActivityContinuation"
- "allowsAutoCorrection"
- "allowsContinuousPathKeyboard"
- "allowsDictation"
- "allowsEmojiKeyboard"
- "allowsKeyboardMathSolving"
- "allowsKeyboardShortcuts"
- "allowsMathPaperSolving"
- "allowsPasswordAutoFill"
- "allowsPredictiveKeyboard"
- "allowsScreenshots"
- "allowsSmartPunctuation"
- "allowsSpellCheck"
- "anonymousListener"
- "antiphony"
- "antiphonyMembership"
- "arrayForKey:"
- "assertion"
- "assessmentSession:failedToBeginWithError:"
- "assessmentSession:wasInterruptedWithError:"
- "assessmentSessionDidBegin:"
- "assessmentSessionDidEnd:"
- "assessmentSessionDidUpdate:"
- "assessmentSessionWrapper:failedToBeginWithError:"
- "assessmentSessionWrapper:failedToUpdateToConfigurationWrapper:error:"
- "assessmentSessionWrapper:wasInterruptedWithError:"
- "assessmentSessionWrapperDidBegin:"
- "assessmentSessionWrapperDidEnd:"
- "assessmentSessionWrapperDidUpdate:"
- "assessmentSesson:failedToUpdateToConfiguration:error:"
- "autorelease"
- "base"
- "begin"
- "beginIntervalWithCategory:name:"
- "beginSessionTimestamp"
- "bundleForClass:"
- "bundleIdentifier"
- "class"
- "cleanUpPolicyStoreWithError:"
- "close"
- "collectionPublisher"
- "collectionSubscription"
- "conduit"
- "configuration"
- "configurationInfo"
- "configurationValidator"
- "configurationWrapper"
- "configurationsByApplicationDescriptor"
- "conformsToProtocol:"
- "connection"
- "contentCaptureController"
- "copy"
- "currentWindows"
- "currentWindowsSubscription"
- "d16@0:8"
- "daemonProxyWithQueue:"
- "deactivateWithCompletion:"
- "deactivation"
- "deactivationForScratchpad:"
- "dealloc"
- "debugDescription"
- "defaultPreferences"
- "delegate"
- "deltaQueue"
- "demand"
- "description"
- "deviceType"
- "domain"
- "doubleValue"
- "end"
- "endPublications:"
- "endpoint"
- "event"
- "exists"
- "failable"
- "frame"
- "group"
- "handleEventDidBeginWithCompletion:"
- "handleEventDidInvalidateWithError:completion:"
- "handleEventWantsBeginSingleAppModeWithCompletion:"
- "handleEventWantsEndSingleAppModeWithCompletion:"
- "handleEventWantsPresentBannerWithTitle:duration:completion:"
- "handleEventWantsStartWindowContentCaptureWithCompletion:"
- "handleEventWantsStopWindowContentCaptureWithCompletion:"
- "hasEntitlement:"
- "hasPersistentData"
- "hash"
- "i16@0:8"
- "i20@0:8B16"
- "identifier"
- "init"
- "initWithConfiguration:queue:"
- "initWithConfigurationWrapper:queue:"
- "initWithDomain:"
- "initWithDomain:code:userInfo:"
- "initWithPolicyStore:performancePrimitives:activations:queue:"
- "initialState"
- "invalidate"
- "invalidationHandler"
- "isActive"
- "isBeingTested"
- "isCanceled"
- "isEqual:"
- "isFailable"
- "isInternalOS"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isObserving"
- "isProxy"
- "isVisible"
- "knownValues"
- "lifetimeConnection"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "mainIndividualConfiguration"
- "makeConfiguration"
- "makeFeatureFlags"
- "makeInterface"
- "makePrimitives"
- "mutableCopy"
- "numberForKey:"
- "objectForKey:"
- "observation"
- "observationProvider"
- "observeSystemNotificationWithName:onQueue:withHandler:"
- "observeWindowLifecycleChangesWithHandler:"
- "observeWindowResizeEventsWithHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistWithError:"
- "policyBundleFactory"
- "policySession"
- "policySessionPrimitives"
- "postSystemNotificationWithName:"
- "preferencesWithPreferencePrimitives:systemNotificationPrimitives:queue:"
- "presentBannerWithTitle:duration:completion:"
- "primitives"
- "processInfoPrimitives"
- "propertyList:isValidForFormat:"
- "proxyWithEndpoint:queue:"
- "publishAssessmentState:withCompletion:"
- "publisherProxy"
- "q16@0:8"
- "queue"
- "readOnlyScratchpadForIdentifier:"
- "refresh"
- "refreshSubscription"
- "registerPublisherWithLifetimeEndpoint:completion:"
- "release"
- "removeWithError:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serializer"
- "session"
- "setAllowsAccessibilityKeyboard:"
- "setAllowsAccessibilityLiveCaptions:"
- "setAllowsAccessibilityReader:"
- "setAllowsAccessibilitySpeech:"
- "setAllowsAccessibilityTypingFeedback:"
- "setAllowsActivityContinuation:"
- "setAllowsAutoCorrection:"
- "setAllowsContinuousPathKeyboard:"
- "setAllowsDictation:"
- "setAllowsEmojiKeyboard:"
- "setAllowsKeyboardMathSolving:"
- "setAllowsKeyboardShortcuts:"
- "setAllowsMathPaperSolving:"
- "setAllowsPasswordAutoFill:"
- "setAllowsPredictiveKeyboard:"
- "setAllowsScreenshots:"
- "setAllowsSmartPunctuation:"
- "setAllowsSpellCheck:"
- "setArray:forKey:"
- "setConfiguration:"
- "setConfigurationsByApplicationDescriptor:"
- "setDelegate:"
- "setEnabled:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInvalidationHandler:"
- "setMainIndividualConfiguration:"
- "setNumber:forKey:"
- "setObject:forKey:"
- "setRestrictsContentCapture:"
- "setShowsUserConfirmationPromptsAndBanners:"
- "setString:forKey:"
- "set_allowsContentCapture:"
- "set_allowsNetworkAccess:"
- "singleAppModePrimitives"
- "singleAppModeSession"
- "singleAppModeToggler"
- "stateAntiphony"
- "stateSubscription"
- "stringForKey:"
- "subscriber"
- "subscription"
- "subscriptions"
- "superclass"
- "supportsMultiAppConfiguration"
- "systemUptime"
- "task"
- "taskQueue"
- "transform"
- "uiPrimitives"
- "updateSubscription"
- "updateToConfigurationWrapper:"
- "updateWithConfiguration:"
- "v16@0:8"
- "v16@?0@\"NSError\"8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"_TtC9AACClient20AECAssessmentSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@?0@\"<AEDSingleAppModeSession>\"8@\"NSError\"16"
- "v24@?0@\"AEActivePolicySession\"8@\"NSError\"16"
- "v24@?0@\"NSXPCListenerEndpoint\"8@\"NSError\"16"
- "v32@0:8@\"AEDSingleAppModeConfiguration\"16@?<v@?@\"<AEDSingleAppModeSession>\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@\"NSString\"24"
- "v32@0:8@\"NSObject\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"_TtC9AACClient20AECAssessmentSession\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"<AEPolicyWriteOnlyScratchpad><AEPersistable>\"16@?<v@?@\"NSError\">24@?<v@?@\"<AEPolicyDeactivation>\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16d24@?<v@?>32"
- "v40@0:8@\"_TtC9AACClient20AECAssessmentSession\"16@\"_TtC9AACClient26AECAssessmentConfiguration\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16d24@?32"
- "v8@?0"
- "validators"
- "valueSubjectsByIdentifier"
- "visible"
- "windowForWindowNumber:"
- "windowNumber"
- "windowPrimitives"
- "windowResizeSubscriptionByWindowNumber"
- "workQueue"
- "wrapperFromConfiguration:"
- "writeOnlyScratchpadForIdentifier:"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
