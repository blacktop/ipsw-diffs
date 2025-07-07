## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1566.100.4.0.0
-  __TEXT.__text: 0x16a8c8
-  __TEXT.__auth_stubs: 0x2360
-  __TEXT.__objc_methlist: 0x19fc8
-  __TEXT.__cstring: 0x13028
+1569.100.5.2.5
+  __TEXT.__text: 0x16bf74
+  __TEXT.__auth_stubs: 0x2370
+  __TEXT.__objc_methlist: 0x1a0d8
+  __TEXT.__cstring: 0x13148
   __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x11f52
+  __TEXT.__oslogstring: 0x12402
   __TEXT.__gcc_except_tab: 0x18e0
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df

   __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5968
-  __TEXT.__eh_frame: 0x1340
+  __TEXT.__unwind_info: 0x5d30
+  __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x2705
-  __TEXT.__objc_methname: 0x3ba83
-  __TEXT.__objc_methtype: 0x7e8e
-  __TEXT.__objc_stubs: 0x20a20
+  __TEXT.__objc_methname: 0x3be58
+  __TEXT.__objc_methtype: 0x7eec
+  __TEXT.__objc_stubs: 0x20b20
   __DATA_CONST.__got: 0xe50
-  __DATA_CONST.__const: 0x35a8
+  __DATA_CONST.__const: 0x35d8
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae50
+  __DATA_CONST.__objc_selrefs: 0xae98
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x6f8
-  __AUTH_CONST.__auth_got: 0x11c0
-  __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0x11b20
-  __AUTH_CONST.__objc_const: 0x27f68
+  __AUTH_CONST.__auth_got: 0x11c8
+  __AUTH_CONST.__const: 0x30d0
+  __AUTH_CONST.__cfstring: 0x11c00
+  __AUTH_CONST.__objc_const: 0x28030
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x2738
   __AUTH.__data: 0x5e8
-  __DATA.__objc_ivar: 0x17cc
+  __DATA.__objc_ivar: 0x17d4
   __DATA.__data: 0x3320
   __DATA.__bss: 0x1890
   __DATA.__common: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE282E53-BE34-309F-81CC-DFE892566212
-  Functions: 9957
-  Symbols:   29779
-  CStrings:  16315
+  UUID: ABE22BB3-37FE-3359-B431-1539FFE50F2B
+  Functions: 9988
+  Symbols:   29857
+  CStrings:  16362
 
Symbols:
+ +[TUUserConfiguration getBooleanFromUserDefaults:default:dataSource:]
+ +[TUUserConfiguration isFilterAsNewCallersEnabledForFaceTime]
+ +[TUUserConfiguration isFilterAsNewCallersEnabledForPhone]
+ -[TUCallNotificationManager callSubtypeChangedForCall:]
+ -[TUCallScreenShareAttributes copyWithZone:]
+ -[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]
+ -[TUConfigurationProvider getSelectedIntelligentCallScreeningMenuOptionForFaceTime]
+ -[TUConfigurationProvider getSelectedIntelligentCallScreeningMenuOptionForPhone]
+ -[TUConfigurationProvider isEligibleForReceptionistOnboardingNotification]
+ -[TUConfigurationProvider setEligibleForReceptionistOnboardingNotification:]
+ -[TUConfigurationProvider setSelectedIntelligentCallScreeningMenuOptionForFaceTime:]
+ -[TUConfigurationProvider setSelectedIntelligentCallScreeningMenuOptionForPhone:]
+ -[TUConversationActivity screenShareAttributes]
+ -[TUConversationActivity setScreenShareAttributes:]
+ -[TUFeatureFlags sharePlaySFXViaInCallServiceEnabled]
+ -[TURouteController dealloc]
+ -[TURouteController performBlockOnQueue:]
+ -[TURouteController queueContext]
+ -[TUScreenShareAttributes copyWithZone:]
+ -[TUScreenSharingRequestMetadata sceneID]
+ -[TUScreenSharingRequestMetadata setSceneID:]
+ -[TUUserConfiguration isEligibleForReceptionistOnboardingNotification]
+ -[TUUserConfiguration setEligibleForReceptionistOnboardingNotification:]
+ -[TUVideoDeviceController provider:cameraDidBecomeInterruptedForForUniqueID:reason:]
+ -[TUVideoDeviceControllerProvider cameraDidBecomeInterruptedForForUniqueID:reason:]
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table167
+ _OBJC_IVAR_$_TUConversationActivity._screenShareAttributes
+ _OBJC_IVAR_$_TUScreenSharingRequestMetadata._sceneID
+ _TUActionFilterUnknownCallers
+ _TUCallSubtypeChangedNotification
+ _TUEligibleForReceptionistOnboardingNotificationKey
+ _TUVideoDeviceControllerDeviceBecomeInterruptedNotification
+ _TUVideoDeviceControllerDeviceBecomeInterruptedReason
+ _TUVideoDeviceControllerDeviceBecomeInterruptedUniqueIDKey
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.663
+ __OBJC_$_CLASS_PROP_LIST_TUScreenShareAttributes.189
+ __OBJC_$_PROP_LIST_TUFeatureFlags.667
+ __OBJC_$_PROP_LIST_TUScreenShareAttributes.224
+ ___45-[TURouteController routesByUniqueIdentifier]_block_invoke
+ ___45-[TURouteController routesByUniqueIdentifier]_block_invoke_2
+ ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.116
+ ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.100
+ ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.103
+ ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.115
+ ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.109
+ ___76-[TUVideoDeviceController provider:didReceiveErrorFromCameraUniqueID:error:]_block_invoke.176
+ ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.113
+ ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke.266
+ ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_2.269
+ ___84-[TUVideoDeviceController provider:cameraDidBecomeInterruptedForForUniqueID:reason:]_block_invoke
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.91
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.91.cold.1
+ ___88-[TUCallServicesInterface routesByUniqueIdentifierForRouteController:completionHandler:]_block_invoke.cold.1
+ ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.106
+ ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.96
+ ___block_literal_global.108
+ ___block_literal_global.112
+ ___block_literal_global.121
+ ___block_literal_global.123
+ ___block_literal_global.154
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.184
+ ___block_literal_global.190
+ ___block_literal_global.196
+ ___block_literal_global.1993
+ ___block_literal_global.1999
+ ___block_literal_global.230
+ ___block_literal_global.255
+ ___block_literal_global.274
+ ___block_literal_global.337
+ ___block_literal_global.374
+ ___block_literal_global.379
+ ___block_literal_global.384
+ ___block_literal_global.95
+ _objc_msgSend$callSubtypeChangedForCall:
+ _objc_msgSend$getBooleanFromUserDefaults:default:dataSource:
+ _objc_msgSend$initWithAttributes:
+ _objc_msgSend$isEligibleForReceptionistOnboardingNotification
+ _objc_msgSend$provider:cameraDidBecomeInterruptedForForUniqueID:reason:
+ _objc_msgSend$publiclyAccessibleCopy
+ _objc_msgSend$routesByUniqueIdentifierForRouteController:completionHandler:
+ _objc_msgSend$sceneID
+ _objc_msgSend$setEligibleForReceptionistOnboardingNotification:
+ _objc_msgSend$setSceneID:
+ _objc_msgSend$setScreenShareAttributes:
- -[TUCallServicesInterface fetchRoutesAsyncForRouteController:completionHandler:]
- -[TURouteController fetchRoutesWithCompletionHandler:]
- GCC_except_table150
- GCC_except_table153
- GCC_except_table156
- GCC_except_table159
- GCC_except_table162
- GCC_except_table165
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.661
- __OBJC_$_CLASS_PROP_LIST_TUScreenShareAttributes.186
- __OBJC_$_PROP_LIST_TUFeatureFlags.665
- __OBJC_$_PROP_LIST_TUScreenShareAttributes.221
- ___53-[TUCallServicesInterface resetCallProvisionalStates]_block_invoke.111
- ___66-[TUCallServicesInterface policyForAddresses:forBundleIdentifier:]_block_invoke.95
- ___69-[TUCallServicesInterface willRestrictAddresses:forBundleIdentifier:]_block_invoke.98
- ___72-[TUCallServicesInterface _handleCurrentCallsChanged:callsDisconnected:]_block_invoke.110
- ___72-[TUCallServicesInterface filterStatusForAddresses:forBundleIdentifier:]_block_invoke.104
- ___76-[TUVideoDeviceController provider:didReceiveErrorFromCameraUniqueID:error:]_block_invoke.167
- ___82-[TUCallServicesInterface isUnknownAddress:normalizedAddress:forBundleIdentifier:]_block_invoke.108
- ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke.263
- ___83-[TUCall initWithUniqueProxyIdentifier:endpointOnCurrentDevice:notificationCenter:]_block_invoke_2.266
- ___92-[TUCallServicesInterface shouldRestrictAddresses:forBundleIdentifier:performSynchronously:]_block_invoke.101
- ___93-[TUCallServicesInterface containsRestrictedHandle:forBundleIdentifier:performSynchronously:]_block_invoke.91
- ___block_literal_global.100
- ___block_literal_global.118
- ___block_literal_global.120
- ___block_literal_global.122
- ___block_literal_global.145
- ___block_literal_global.148
- ___block_literal_global.156
- ___block_literal_global.181
- ___block_literal_global.187
- ___block_literal_global.193
- ___block_literal_global.1990
- ___block_literal_global.1996
- ___block_literal_global.232
- ___block_literal_global.252
- ___block_literal_global.265
- ___block_literal_global.333
- ___block_literal_global.370
- ___block_literal_global.375
- ___block_literal_global.380
- ___block_literal_global.94
- ___block_literal_global.97
- _objc_msgSend$fetchRoutesAsyncForRouteController:completionHandler:
- _objc_msgSend$getLocalRouteControllerRoutes:
- _objc_msgSend$getPairedHostDeviceRouteControllerRoutes:
CStrings:
+ " sceneID=%@"
+ "%@ isEligibleForReceptionistOnboardingNotification called"
+ "%@ setEligibleForReceptionistOnboardingNotification called %d"
+ "@\"TUScreenShareAttributes\""
+ "EligibleForReceptionistOnboardingNotification"
+ "Error using remote object proxy when requesting local routes asynchronously: %@"
+ "Error using remote object proxy when requesting paired host device routes asynchronously: %@"
+ "Intelligent Call Screening: getSelectedIntelligentCallScreeningMenuOptionForFaceTime %ld"
+ "Intelligent Call Screening: getSelectedIntelligentCallScreeningMenuOptionForPhone %ld"
+ "Intelligent Call Screening: isReceptionistAvailable FALSE, returning default IntelligentCallScreeningMenuOptionNever"
+ "Intelligent Call Screening: setSelectedIntelligentCallScreeningMenuOptionForFaceTime %ld"
+ "Intelligent Call Screening: setSelectedIntelligentCallScreeningMenuOptionForFaceTime DONE, now we have receptionistEnabled = %d, silenceUnknownCallersEnabledForFaceTime = %d"
+ "Intelligent Call Screening: setSelectedIntelligentCallScreeningMenuOptionForPhone %ld"
+ "Intelligent Call Screening: setSelectedIntelligentCallScreeningMenuOptionForPhone DONE, now we have receptionistEnabled = %d, silenceUnknownCallersEnabledForPhone = %d"
+ "Proxying localRouteController routes asynchronously"
+ "Proxying pairedHostDeviceRouteController routes asynchronously"
+ "T@\"NSString\",&,N,V_sceneID"
+ "T@\"TUScreenShareAttributes\",C,N,V_screenShareAttributes"
+ "TB,N,GisEligibleForReceptionistOnboardingNotification,SsetEligibleForReceptionistOnboardingNotification:"
+ "TUActionFilterUnknownCallers"
+ "TUCallSubtypeChangedNotification"
+ "TUVideoDeviceControllerDeviceBecomeInterruptedNotification"
+ "TUVideoDeviceControllerDeviceBecomeInterruptedReason"
+ "TUVideoDeviceControllerDeviceBecomeInterruptedUniqueIDKey"
+ "Tq,N,GgetSelectedIntelligentCallScreeningMenuOptionForFaceTime,SsetSelectedIntelligentCallScreeningMenuOptionForFaceTime:"
+ "Tq,N,GgetSelectedIntelligentCallScreeningMenuOptionForPhone,SsetSelectedIntelligentCallScreeningMenuOptionForPhone:"
+ "_sceneID"
+ "callSubtypeChangedForCall %@"
+ "callSubtypeChangedForCall:"
+ "cameraDidBecomeInterruptedForForUniqueID: %@ reason: %ld"
+ "eligibleForReceptionistOnboardingNotification"
+ "getBooleanFromUserDefaults:default:dataSource:"
+ "getSelectedIntelligentCallScreeningMenuOptionForFaceTime"
+ "getSelectedIntelligentCallScreeningMenuOptionForPhone"
+ "intelligentCallScreeningMenuOptionForFaceTime"
+ "intelligentCallScreeningMenuOptionForPhone"
+ "isEligibleForReceptionistOnboardingNotification"
+ "provider:cameraDidBecomeInterruptedForForUniqueID:reason:"
+ "routesByUniqueIdentifierForRouteController:completionHandler:"
+ "sceneID"
+ "setEligibleForReceptionistOnboardingNotification:"
+ "setSceneID:"
+ "setSelectedIntelligentCallScreeningMenuOptionForFaceTime:"
+ "setSelectedIntelligentCallScreeningMenuOptionForPhone:"
+ "sharePlaySFXViaInCallServiceEnabled"
+ "v32@0:8@\"TURouteController\"16@?<v@?@\"NSDictionary\">24"
+ "v40@0:8@\"<TUVideoDeviceControllerProvider>\"16@\"NSString\"24q32"
- "Proxying localRouteControllerRoutes asynchronously"
- "Proxying pairedHostDeviceRouteControllerRotes asynchronously"
- "fetchRoutesAsyncForRouteController:completionHandler:"
- "fetchRoutesWithCompletionHandler:"
- "getLocalRouteControllerRoutes:"
- "getPairedHostDeviceRouteControllerRoutes:"
- "v32@0:8@\"TURouteController\"16@?<v@?@\"NSArray\">24"

```
