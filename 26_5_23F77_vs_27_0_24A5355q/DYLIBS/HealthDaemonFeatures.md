## HealthDaemonFeatures

> `/System/Library/PrivateFrameworks/HealthDaemonFeatures.framework/HealthDaemonFeatures`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x98e4
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x41c
-  __TEXT.__const: 0x41e
+7027.0.52.2.6
+  __TEXT.__text: 0x9be8
+  __TEXT.__objc_methlist: 0x424
+  __TEXT.__const: 0x40e
   __TEXT.__oslogstring: 0x415
-  __TEXT.__cstring: 0x344
+  __TEXT.__cstring: 0x374
   __TEXT.__constg_swiftt: 0x23c
   __TEXT.__swift5_typeref: 0x196
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_fieldmd: 0x160
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x248
   __TEXT.__eh_frame: 0xc0
-  __TEXT.__objc_classname: 0x35f
-  __TEXT.__objc_methname: 0x123f
-  __TEXT.__objc_methtype: 0x394
-  __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e8
+  __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x440
-  __AUTH_CONST.__const: 0x230
+  __DATA_CONST.__got: 0x1f8
+  __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0xda0
+  __AUTH_CONST.__objc_const: 0xda8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH.__objc_data: 0x170
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x300
   __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x3a8
-  __DATA_DIRTY.__data: 0x2e8
+  __DATA_DIRTY.__data: 0x310
   __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures
+  - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AAD8053D-6CF9-3D9F-A256-DB5B5E06AEEE
-  Functions: 171
-  Symbols:   546
-  CStrings:  256
+  UUID: 5E834C35-BE9A-3A0E-A381-427E3AF5F648
+  Functions: 175
+  Symbols:   562
+  CStrings:  55
 
Symbols:
+ ___91-[HDExampleFeatureProfileExtension notificationSyncClient:didReceiveInstructionWithAction:]_block_invoke.382
+ ___swift_closure_destructor
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_HealthDaemonFeatures
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x3
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x24
+ _swift_setDeallocating
- _OUTLINED_FUNCTION_3
- ___91-[HDExampleFeatureProfileExtension notificationSyncClient:didReceiveInstructionWithAction:]_block_invoke.361
- _objc_retain_x26
CStrings:
+ "SleepScore"
+ "Vitals"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDFeatureAvailabilityExtension>\"24@0:8@\"NSString\"16"
- "@\"<HDHealthDaemonExtension>\"24@0:8@\"<HDHealthDaemon>\"16"
- "@\"<HDProfileExtension>\"24@0:8@\"HDProfile\"16"
- "@\"HDBackgroundFeatureDeliveryManager\""
- "@\"HDFeatureAvailabilityManager\""
- "@\"HDNotificationSyncClient\""
- "@\"HDProfile\""
- "@\"NSArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCListenerEndpoint\"32@0:8@\"HDXPCClient\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@44@0:8@16@24B32@36"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "GlucoseEnhancedCharting"
- "HDDeviceKeyValueStoreObserver"
- "HDExampleFeatureProfileExtension"
- "HDFeatureAvailabilityExtensionProvider"
- "HDGlucoseExperienceProfileExtension"
- "HDMinorExperiencesPlugin"
- "HDMinorExperiencesProfileExtension"
- "HDNotificationSyncClientDelegate"
- "HDPlugin"
- "HDProfileExtension"
- "HDProtectedDataOperationDelegate"
- "HDRespiratoryRateMeasurementsProfileExtension"
- "HDWristTemperatureMeasurementsProfileExtension"
- "HealthDaemonFeatures"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "WristTemperatureMeasurements"
- "^{_NSZone=}16@0:8"
- "_TtC20HealthDaemonFeatures26HealthDaemonFeaturesPlugin"
- "_TtC20HealthDaemonFeatures32FeatureAlgorithmVersionsObserver"
- "_TtC20HealthDaemonFeatures35FeatureAlgorithmVersionsSyncManager"
- "_TtC20HealthDaemonFeatures36HealthDaemonFeaturesProfileExtension"
- "_TtC20HealthDaemonFeatures37FeatureAlgorithmVersionsChangeManager"
- "_featureAvailabilityManager"
- "_featureDeliveryManager"
- "_featureIdentifier"
- "_minorExperiences"
- "_notificationSyncClient"
- "_profile"
- "_queue"
- "allObjects"
- "anyCountryAvailability"
- "arrayWithObjects:count:"
- "autorelease"
- "behavior"
- "bundleForClass:"
- "capabilityIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:"
- "capabilityIsSupportedOnActiveWatchForFeatureWithIdentifier:supportedOnLocalDevice:"
- "capabilityIsSupportedOnAnyWatch:supportedOnLocalDevice:"
- "categoryIdentifiers"
- "class"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "contextForWriting"
- "count"
- "countryIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:isSupportedIfCountryListMissing:"
- "countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:"
- "countryIsSupportedOnWatchForFeatureWithIdentifier:isSupportedIfCountryListMissing:"
- "currentHandler"
- "currentSyncIdentity"
- "daemon"
- "database"
- "dealloc"
- "debugDescription"
- "defaultHelpTileRequirementsForBackgroundDeliveredFeatureWithFeatureIdentifier:isAgeGatedUserDefaultsKey:"
- "defaultOnboardingEligibilityRequirementsForFeatureIdentifier:"
- "defaultTipsAppVisibilityRequirementsForBackgroundDeliveredFeatureWithFeatureIdentifier:isAgeGatedUserDefaultsKey:"
- "delegate"
- "description"
- "deviceContext"
- "deviceKeyValueStore"
- "deviceKeyValueStoreDidUpdateForStorageGroup:domain:"
- "deviceKeyValueStoreManager"
- "deviceType"
- "dictionaryWithObjects:forKeys:count:"
- "emptyCountrySet"
- "extensionForHealthDaemon:"
- "extensionForProfile:"
- "featureAlgorithmVersionsChangeManager"
- "featureAlgorithmVersionsObserver"
- "featureAlgorithmVersionsSyncManager"
- "featureAttributesDerivedFromOSBuildAndFeatureVersion:"
- "featureAvailabilityExtensionForFeatureIdentifier:"
- "featureIsNotRemotelyDisabledWithIdentifier:"
- "featureIsOnWithIdentifier:isOnIfSettingIsAbsent:"
- "fetchEntriesForDomain:key:protectionCategory:error:"
- "fetchEntryForKey:domain:syncIdentity:category:error:"
- "firstObject"
- "getDeliveredNotificationsWithCompletionHandler:"
- "handleDatabaseObliteration"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "healthDaemon"
- "hk_map:"
- "identifier"
- "identity"
- "init"
- "initWithAllowedCountriesDataSource:profile:featureCapability:loggingCategory:"
- "initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:"
- "initWithDaemon:featureIdentifier:"
- "initWithFeatureIdentifier:defaultCountrySet:healthDaemon:"
- "initWithFeatureIdentifier:localFeatureAttributes:localCountrySetAvailabilityProvider:"
- "initWithInteger:"
- "initWithProfile:"
- "initWithProfile:clientIdentifier:queue:"
- "initWithProfile:debugIdentifier:delegate:"
- "initWithProfile:featureAvailabilityExtension:loggingCategory:"
- "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
- "initWithProfile:featureIdentifier:isBackgroundDeliveryEnabled:loggingCategory:"
- "initWithRequirementsByContext:"
- "initWithUUIDString:"
- "integerValue"
- "invalidateAndWait"
- "isAppleInternalInstall"
- "isAppleWatch"
- "isCompanionCapable"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "key"
- "listenerEndpointForClient:error:"
- "localAvailabilityForGlucoseEnhancedCharting"
- "localAvailabilityForWristTemperatureMeasurements"
- "markPendingNotificationInstructionsAsProcessed:error:"
- "minorExperiencesProfileExtension"
- "modificationDate"
- "notAgeGatedForUserDefaultsKey:"
- "notificationManager"
- "notificationSyncClient:didReceiveInstructionWithAction:"
- "numberValue:"
- "onboardingRecordIsPresentForFeatureWithIdentifier:"
- "onboardingRecordsArePresentForPrerequisiteFeaturesWithIdentifiers:"
- "operation"
- "pendingNotificationDismissInstructionsWithError:"
- "pendingNotificationSendInstructionsWithError:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
- "pluginIdentifier"
- "postNotificationWithIdentifier:content:trigger:completion:"
- "prepareForObliteration"
- "profileIdentifier"
- "profileIsNotFamilySetupPairingProfile"
- "profileType"
- "registerObserver:"
- "release"
- "removeDeliveredNotificationsWithIdentifiers:"
- "request"
- "requestWorkWithPriority:error:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setBody:"
- "setDelegate:"
- "setNumber:forKey:domainName:protectionCategory:error:"
- "setTitle:"
- "sharedBehavior"
- "shouldLoadPluginForDaemon:"
- "sleepSettingsProvider"
- "storageEntries"
- "superclass"
- "syncIdentityManager"
- "synchronizeLocalProperties"
- "type"
- "v16@0:8"
- "v32@0:8@\"HDNotificationSyncClient\"16q24"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
- "v48@0:8@16@24@32@?40"
- "wristDetectionIsEnabledForActiveWatch"
- "zone"

```
