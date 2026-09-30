## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3505.9.1.0.0
-  __TEXT.__text: 0xa241ec
+3505.10.2.0.0
+  __TEXT.__text: 0xa24ae8
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0xd435c
-  __TEXT.__const: 0x11ebc
-  __TEXT.__cstring: 0x7a30a
-  __TEXT.__constg_swiftt: 0x6480
-  __TEXT.__swift5_typeref: 0x18d6
-  __TEXT.__swift5_builtin: 0x3a48
+  __TEXT.__objc_methlist: 0xd440c
+  __TEXT.__const: 0x11f0c
+  __TEXT.__cstring: 0x7a396
+  __TEXT.__constg_swiftt: 0x64a0
+  __TEXT.__swift5_typeref: 0x18dc
+  __TEXT.__swift5_builtin: 0x3a5c
   __TEXT.__swift5_reflstr: 0x212
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xef8
-  __TEXT.__swift5_types: 0xbf8
+  __TEXT.__swift5_proto: 0xefc
+  __TEXT.__swift5_types: 0xbfc
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2a5d8
+  __TEXT.__unwind_info: 0x2a5f0
   __TEXT.__eh_frame: 0x24a0
   __TEXT.__objc_classname: 0x15bf8
-  __TEXT.__objc_methname: 0x1261e0
-  __TEXT.__objc_methtype: 0x28e95
-  __TEXT.__objc_stubs: 0x6a760
+  __TEXT.__objc_methname: 0x126250
+  __TEXT.__objc_methtype: 0x28ec2
+  __TEXT.__objc_stubs: 0x6a7a0
   __DATA_CONST.__got: 0x4d38
-  __DATA_CONST.__const: 0x35078
+  __DATA_CONST.__const: 0x35128
   __DATA_CONST.__objc_classlist: 0x4c18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x371e0
+  __DATA_CONST.__objc_selrefs: 0x37208
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x7658
   __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x21818
-  __AUTH_CONST.__cfstring: 0x6a1e0
-  __AUTH_CONST.__objc_const: 0x11f500
+  __AUTH_CONST.__const: 0x21838
+  __AUTH_CONST.__cfstring: 0x6a2a0
+  __AUTH_CONST.__objc_const: 0x11f5c0
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x119b8
-  __DATA.__objc_ivar: 0xe53c
+  __AUTH.__objc_data: 0x11800
+  __DATA.__objc_ivar: 0xe548
   __DATA.__data: 0x2048
-  __DATA.__bss: 0x18d80
+  __DATA.__bss: 0x18e00
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x1e188
-  __DATA_DIRTY.__data: 0x598
+  __DATA_DIRTY.__objc_data: 0x1e340
+  __DATA_DIRTY.__data: 0x5a0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AABF3353-AB7F-3AF7-B983-7E96222F8BD4
-  Functions: 76806
-  Symbols:   191057
-  CStrings:  78547
+  UUID: 3D3289CE-21BC-36AA-8B0A-41BAA47617DC
+  Functions: 76824
+  Symbols:   191093
+  CStrings:  78566
 
Symbols:
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus currentMode]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteCurrentMode]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasCurrentMode]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setCurrentMode:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasCurrentMode:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus currentMode]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus deleteCurrentMode]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus hasCurrentMode]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus setCurrentMode:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus setHasCurrentMode:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus currentMode]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteCurrentMode]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasCurrentMode]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setCurrentMode:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasCurrentMode:]
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._currentMode
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus._currentMode
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._currentMode
+ _objc_msgSend$currentMode
+ _objc_msgSend$setCurrentMode:
+ _symbolic _____ So20SADSchemaSADSiriModeV
CStrings:
+ "SADSIRIMODE_CLASSIC"
+ "SADSIRIMODE_FULL_UOD"
+ "SADSIRIMODE_HYBRID"
+ "SADSIRIMODE_SYSTEM_ASSISTANT_EXPERIENCE"
+ "SADSIRIMODE_UNKNOWN"
+ "Ti,N,V_currentMode"
+ "_currentMode"
+ "currentMode"
+ "deleteCurrentMode"
+ "hasCurrentMode"
+ "setCurrentMode:"
+ "setHasCurrentMode:"
+ "{?=\"currentStatus\"b1\"previousStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"hasModelCatalogSubscriptionHashChangedFromLastStatus\"b1\"isAppleIntelligenceEligible\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"downloadState\"b1\"timeSinceLastModelCatalogSubscriptionHashChangeInSeconds\"b1\"useCase\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1}"
+ "{?=\"locale\"b1\"status\"b1\"currentSubscriptionHash\"b1\"downloadState\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"lastMobileAssetDownloadAttemptErrorCode\"b1\"errorCount\"b1\"sampledErrorCode\"b1\"sampledErrorHash\"b1\"sampledErrorUnderlyingCode\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"countPSUSAssets\"b1\"countRequiredAssets\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1}"
+ "{?=\"newStatus\"b1\"prevStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"isAppleIntelligenceEligible\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"currentSubscriptionHash\"b1\"previousSubscriptionHash\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"currentMode\"b1}"
- "{?=\"currentStatus\"b1\"previousStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"hasModelCatalogSubscriptionHashChangedFromLastStatus\"b1\"isAppleIntelligenceEligible\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"downloadState\"b1\"timeSinceLastModelCatalogSubscriptionHashChangeInSeconds\"b1\"useCase\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1}"
- "{?=\"locale\"b1\"status\"b1\"currentSubscriptionHash\"b1\"downloadState\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"lastMobileAssetDownloadAttemptErrorCode\"b1\"errorCount\"b1\"sampledErrorCode\"b1\"sampledErrorHash\"b1\"sampledErrorUnderlyingCode\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"countPSUSAssets\"b1\"countRequiredAssets\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1}"
- "{?=\"newStatus\"b1\"prevStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"isAppleIntelligenceEligible\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"currentSubscriptionHash\"b1\"previousSubscriptionHash\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1}"

```
