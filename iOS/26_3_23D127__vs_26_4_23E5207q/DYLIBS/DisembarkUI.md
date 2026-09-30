## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

```diff

-267.2.1.0.0
-  __TEXT.__text: 0x18c5c
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x21c8
-  __TEXT.__const: 0x124
-  __TEXT.__cstring: 0x1b7b
-  __TEXT.__gcc_except_tab: 0x228
-  __TEXT.__oslogstring: 0xae2
+267.4.5.0.0
+  __TEXT.__text: 0x1bdc0
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x22b0
+  __TEXT.__const: 0x144
+  __TEXT.__cstring: 0x1956
+  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__oslogstring: 0xb8d
+  __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__swift5_typeref: 0x138
   __TEXT.__swift5_capture: 0xa4
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_reflstr: 0xf
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x670
-  __TEXT.__objc_classname: 0x525
-  __TEXT.__objc_methname: 0x5c38
-  __TEXT.__objc_methtype: 0xf50
-  __TEXT.__objc_stubs: 0x4640
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0xc68
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__objc_classname: 0x65b
+  __TEXT.__objc_methname: 0x5f61
+  __TEXT.__objc_methtype: 0x10a1
+  __TEXT.__objc_stubs: 0x4900
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0xd18
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1680
+  __DATA_CONST.__objc_selrefs: 0x16d8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x4170
-  __AUTH.__objc_data: 0xd48
-  __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x244
-  __DATA.__data: 0x868
-  __DATA.__bss: 0x10
+  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__objc_const: 0x4468
+  __AUTH.__objc_data: 0xde8
+  __AUTH.__data: 0x118
+  __DATA.__objc_ivar: 0x254
+  __DATA.__data: 0x930
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/Disembark.framework/Disembark
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
+  - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup

   - /System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/StorageData.framework/StorageData
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9934986E-2C21-387E-A555-7C2E12A7A934
-  Functions: 767
-  Symbols:   2885
-  CStrings:  1657
+  UUID: D160C406-D62B-3A8D-AAB4-762AAC19B7E4
+  Functions: 799
+  Symbols:   3013
+  CStrings:  1680
 
Symbols:
+ -[DKAnalyticsHandler _forceAnalyticsUploadWithCompletion:]
+ -[DKAnalyticsHandler _sendTerminatedAnalyticsEventWithLastPaneShown:reason:willErase:]
+ -[DKAnalyticsHandler sendAnalyticsBeforeErasing:reason:completion:]
+ -[DKAnalyticsHandler sendTerminatedAnalyticsEventWithLastPaneShown:reason:]
+ -[DKEraseFlow analyticsHandler]
+ -[DKEraseFlow repairProvider]
+ -[DKEraseFlow setAnalyticsHandler:]
+ -[DKEraseFlow setRepairProvider:]
+ -[DKIntroViewController needsToShowRepairModeSpecificFindMy]
+ -[DKNotableUserData isDeviceInRepairMode]
+ -[DKNotableUserData setIsDeviceInRepairMode:]
+ -[DKNotableUserDataProvider fetchNotableUserData:].cold.8
+ -[DKNotableUserDataProvider initWithAccountProvider:findMyProvider:appleCareProvider:repairProvider:walletProvider:]
+ -[DKNotableUserDataProvider repairProvider]
+ -[DKNotableUserDataProvider setRepairProvider:]
+ -[DKRepairProvider fetchIsDeviceInRepairModeWithCompletion:]
+ GCC_except_table26
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table7
+ _OBJC_CLASS_$_DKAnalyticsHandler
+ _OBJC_CLASS_$_DKRepairProvider
+ _OBJC_IVAR_$_DKEraseFlow._analyticsHandler
+ _OBJC_IVAR_$_DKEraseFlow._repairProvider
+ _OBJC_IVAR_$_DKNotableUserData._isDeviceInRepairMode
+ _OBJC_IVAR_$_DKNotableUserDataProvider._repairProvider
+ _OBJC_METACLASS_$_DKAnalyticsHandler
+ _OBJC_METACLASS_$_DKRepairProvider
+ _OSASubmissionClientLibraryCore.frameworkLibrary
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _UIFontTextStyleTitle3
+ __OBJC_$_INSTANCE_METHODS_DKAnalyticsHandler
+ __OBJC_$_INSTANCE_METHODS_DKRepairProvider
+ __OBJC_$_PROP_LIST_DKAnalyticsHandler
+ __OBJC_$_PROP_LIST_DKNotableUserDataProvider.189
+ __OBJC_$_PROP_LIST_DKRepairProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DKAnalyticsHandlerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DKRepairProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DKAnalyticsHandlerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DKRepairProvider
+ __OBJC_$_PROTOCOL_REFS_DKAnalyticsHandlerProtocol
+ __OBJC_$_PROTOCOL_REFS_DKRepairProvider
+ __OBJC_CLASS_PROTOCOLS_$_DKAnalyticsHandler
+ __OBJC_CLASS_PROTOCOLS_$_DKRepairProvider
+ __OBJC_CLASS_RO_$_DKAnalyticsHandler
+ __OBJC_CLASS_RO_$_DKRepairProvider
+ __OBJC_LABEL_PROTOCOL_$_DKAnalyticsHandlerProtocol
+ __OBJC_LABEL_PROTOCOL_$_DKRepairProvider
+ __OBJC_METACLASS_RO_$_DKAnalyticsHandler
+ __OBJC_METACLASS_RO_$_DKRepairProvider
+ __OBJC_PROTOCOL_$_DKAnalyticsHandlerProtocol
+ __OBJC_PROTOCOL_$_DKRepairProvider
+ ___27-[DKEraseFlow _eraseDevice]_block_invoke
+ ___27-[DKEraseFlow _eraseDevice]_block_invoke_2
+ ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke.163
+ ___37-[DKEraseFlow initWithConfiguration:]_block_invoke.35
+ ___37-[DKEraseFlow initWithConfiguration:]_block_invoke.35.cold.1
+ ___37-[DKEraseFlow initWithConfiguration:]_block_invoke.44
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke.122
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke.123
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_2.124
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_3.125
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_4.126
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_5.127
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_6.131
+ ___46-[DKEraseFlow _nextStateFromState:completion:]_block_invoke.132
+ ___50-[DKEraseFlow _supportsNonInteractiveCloudUpload:]_block_invoke.80
+ ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.58
+ ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.60
+ ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.62
+ ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.64
+ ___58-[DKAnalyticsHandler _forceAnalyticsUploadWithCompletion:]_block_invoke
+ ___58-[DKAnalyticsHandler _forceAnalyticsUploadWithCompletion:]_block_invoke_2
+ ___58-[DKAnalyticsHandler _forceAnalyticsUploadWithCompletion:]_block_invoke_3
+ ___58-[DKAnalyticsHandler _forceAnalyticsUploadWithCompletion:]_block_invoke_4
+ ___OSASubmissionClientLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.38
+ ___block_literal_global.47
+ ___block_literal_global.50
+ ___chkstk_darwin
+ ___getOSASubmissionClientClass_block_invoke
+ ___getOSASubmissionClientClass_block_invoke.cold.1
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringOSASubmissionClient
+ _dispatch_after
+ _dispatch_time
+ _free
+ _getOSASubmissionClientClass.softClass
+ _objc_autorelease
+ _objc_getClass
+ _objc_getProperty
+ _objc_msgSend$_fetchCoverageDetails
+ _objc_msgSend$_forceAnalyticsUploadWithCompletion:
+ _objc_msgSend$_sendTerminatedAnalyticsEventWithLastPaneShown:reason:willErase:
+ _objc_msgSend$addChildViewController:
+ _objc_msgSend$analyticsHandler
+ _objc_msgSend$coverageLabel
+ _objc_msgSend$didMoveToParentViewController:
+ _objc_msgSend$fetchIsDeviceInRepairModeWithCompletion:
+ _objc_msgSend$getCachedCoverageDetailsForSerialNumber:requester:completion:
+ _objc_msgSend$hasTheftAndLoss
+ _objc_msgSend$initWithAccountProvider:findMyProvider:appleCareProvider:repairProvider:walletProvider:
+ _objc_msgSend$initWithFetchCoverageDetails:
+ _objc_msgSend$initWithTitle:subtitle:
+ _objc_msgSend$isDeviceInRepairMode
+ _objc_msgSend$isTheftAndLossEnabled
+ _objc_msgSend$needsToShowRepairModeSpecificFindMy
+ _objc_msgSend$preferredFontForTextStyle:
+ _objc_msgSend$repairProvider
+ _objc_msgSend$sendAnalyticsBeforeErasing:reason:completion:
+ _objc_msgSend$sendTerminatedAnalyticsEventWithLastPaneShown:reason:
+ _objc_msgSend$setCoverageLabel:
+ _objc_msgSend$setIsDeviceInRepairMode:
+ _objc_msgSend$setIsTheftAndLossEnabled:
+ _objc_msgSend$submitDRETelemetryAndDiagnostics:
+ _objc_setProperty_atomic
+ _swift_bridgeObjectRelease_n
- -[DKEraseFlow _sendTerminatedAnalyticsEventWithState:willErase:reason:]
- -[DKNotableUserDataProvider initWithAccountProvider:findMyProvider:appleCareProvider:walletProvider:]
- GCC_except_table27
- GCC_except_table44
- GCC_except_table50
- __OBJC_$_PROP_LIST_DKNotableUserDataProvider.177
- ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke.178
- ___37-[DKEraseFlow initWithConfiguration:]_block_invoke.34
- ___37-[DKEraseFlow initWithConfiguration:]_block_invoke.34.cold.1
- ___37-[DKEraseFlow initWithConfiguration:]_block_invoke.43
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke.137
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke.138
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_2.139
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_3.140
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_4.141
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_5.142
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_6.146
- ___46-[DKEraseFlow _nextStateFromState:completion:]_block_invoke.147
- ___50-[DKEraseFlow _supportsNonInteractiveCloudUpload:]_block_invoke.92
- ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.55
- ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.59
- ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.61
- ___block_literal_global.37
- ___block_literal_global.46
- ___block_literal_global.49
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_sendTerminatedAnalyticsEventWithState:willErase:reason:
- _objc_msgSend$initWithAccountProvider:findMyProvider:appleCareProvider:walletProvider:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "@\"<DKAnalyticsHandlerProtocol>\""
+ "@\"<DKRepairProvider>\""
+ "@\"<DKRepairProvider>\"16@0:8"
+ "@56@0:8@16@24@32@40@48"
+ "Advancing from state: %lu, disabling interaction"
+ "Advancing to state: %lu, re-enabling interaction"
+ "Completed submitting analytics with result: %i"
+ "DKAnalyticsHandler"
+ "DKAnalyticsHandlerProtocol"
+ "DKRepairProvider"
+ "Finished fetching repair mode state"
+ "OSASubmissionClient"
+ "RESET_REPAIR_BODY"
+ "RESET_REPAIR_SECOND_EXPLANATORY_TEXT"
+ "RESET_REPAIR_TITLE"
+ "T@\"<DKAnalyticsHandlerProtocol>\",&,V_analyticsHandler"
+ "T@\"<DKRepairProvider>\",&,N"
+ "T@\"<DKRepairProvider>\",&,N,V_repairProvider"
+ "TB,N,V_isDeviceInRepairMode"
+ "Unable to find class %s"
+ "_analyticsHandler"
+ "_forceAnalyticsUploadWithCompletion:"
+ "_isDeviceInRepairMode"
+ "_repairProvider"
+ "_sendTerminatedAnalyticsEventWithLastPaneShown:reason:willErase:"
+ "analyticsHandler"
+ "exiting from %@ because %@"
+ "fetchIsDeviceInRepairModeWithCompletion:"
+ "initWithAccountProvider:findMyProvider:appleCareProvider:repairProvider:walletProvider:"
+ "isDeviceInRepairMode"
+ "needsToShowRepairModeSpecificFindMy"
+ "preferredFontForTextStyle:"
+ "repairProvider"
+ "self.repairProvider"
+ "sendAnalyticsBeforeErasing:reason:completion:"
+ "sendTerminatedAnalyticsEventWithLastPaneShown:reason:"
+ "setAnalyticsHandler:"
+ "setIsDeviceInRepairMode:"
+ "setRepairProvider:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient"
+ "submitDRETelemetryAndDiagnostics:"
+ "v24@0:8@\"<DKRepairProvider>\"16"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?>32"
- "@48@0:8@16@24@32@40"
- "Sending event for %@ with payload %@"
- "User Cancelled (%@)"
- "_sendTerminatedAnalyticsEventWithState:willErase:reason:"
- "initWithAccountProvider:findMyProvider:appleCareProvider:walletProvider:"
- "manager:didFailVerificationWithError:"
- "managerDidFinishVerification:"
- "v36@0:8Q16B24@28"

```
