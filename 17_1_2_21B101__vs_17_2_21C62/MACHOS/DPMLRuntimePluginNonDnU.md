## DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0x1b4dc
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x1208
+209.0.0.0.0
+  __TEXT.__text: 0x1c7a4
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0x34a0
+  __TEXT.__objc_methlist: 0x1300
   __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x3115
-  __TEXT.__objc_methname: 0x35e2
-  __TEXT.__oslogstring: 0x10b4
-  __TEXT.__objc_classname: 0x46c
+  __TEXT.__cstring: 0x334c
+  __TEXT.__objc_methname: 0x38e8
+  __TEXT.__oslogstring: 0x12c1
+  __TEXT.__objc_classname: 0x4ef
   __TEXT.__objc_methtype: 0x766
-  __TEXT.__gcc_except_tab: 0x128
+  __TEXT.__gcc_except_tab: 0x144
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x460
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x430
-  __DATA_CONST.__cfstring: 0x2de0
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__unwind_info: 0x484
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__cfstring: 0x3120
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x1b0
-  __DATA_CONST.__objc_arraydata: 0xf8
+  __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x30f8
-  __DATA.__objc_selrefs: 0xe78
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x3438
+  __DATA.__objc_selrefs: 0xf38
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x298
-  __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x110
-  __DATA.__objc_data: 0xcd0
+  __DATA.__objc_classrefs: 0x2f8
+  __DATA.__objc_superrefs: 0xd8
+  __DATA.__objc_ivar: 0x11c
+  __DATA.__objc_data: 0xe10
   __DATA.__data: 0x2b8
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Photos.framework/Photos

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy
+  - /System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 5DB063AA-9E5F-3449-9B3E-A40D202DE207
-  Functions: 459
-  Symbols:   290
-  CStrings:  1634
+  UUID: EB69C2BB-D1E2-3A87-9035-6E559BD29C82
+  Functions: 479
+  Symbols:   312
+  CStrings:  1729
 
Symbols:
+ _INExtensionAttributesIntentsSupportedKey
+ _INExtensionAttributesSupportedIntentsKey
+ _INIntentsServiceExtensionPointName
+ _INSupportedMediaCategories
+ _NSExtensionPointName
+ _OBJC_CLASS_$_FedStatsCohortQueryInstalledApps
+ _OBJC_CLASS_$_FedStatsCohortQueryInstalledAppsMedia
+ _OBJC_CLASS_$_FedStatsCohortQueryInstalledAppsPhone
+ _OBJC_CLASS_$_INAddMediaIntent
+ _OBJC_CLASS_$_INPlayMediaIntent
+ _OBJC_CLASS_$_INSearchForMediaIntent
+ _OBJC_CLASS_$_INUpdateMediaAffinityIntent
+ _OBJC_CLASS_$_LBFEventManager
+ _OBJC_CLASS_$_LBFLighthouseEvent
+ _OBJC_CLASS_$_LBFTrialIdentifiers
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$__DPMLRuntimeTelemetry
+ _OBJC_METACLASS_$_FedStatsCohortQueryInstalledApps
+ _OBJC_METACLASS_$_FedStatsCohortQueryInstalledAppsMedia
+ _OBJC_METACLASS_$_FedStatsCohortQueryInstalledAppsPhone
+ _OBJC_METACLASS_$__DPMLRuntimeTelemetry
CStrings:
+ "%d"
+ "Bitacora donation error: %@"
+ "Error enumerating app records; app record: %@ has nil bundle identifier"
+ "Error enumerating plugins; matching query: %@, error: %@"
+ "Error enumerating plugins; missing containing bundle of plugin: %@"
+ "FedStatsCohortQueryInstalledApps"
+ "FedStatsCohortQueryInstalledApps#resolveDomainToBundleIds complete in %fms"
+ "FedStatsCohortQueryInstalledApps#resolveDomainToBundleIds start."
+ "FedStatsCohortQueryInstalledAppsMedia"
+ "FedStatsCohortQueryInstalledAppsPhone"
+ "INMediaCategoryAudiobooks"
+ "INMediaCategoryGeneral"
+ "INMediaCategoryMusic"
+ "INMediaCategoryPodcasts"
+ "INMediaCategoryRadio"
+ "INMediaCategoryVideo"
+ "Invalid call to FedStatsCohortQueryInstalledApps#.cohortKeyForParameters"
+ "T@\"NSDictionary\",&,N,V_domainToBundleIds"
+ "TQ,R,N,V_numOfMediaApps"
+ "TQ,R,N,V_numOfPhoneApps"
+ "_DPMLRuntimeTelemetry"
+ "_domainToBundleIds"
+ "_isSupportedIntentMediaApp:::"
+ "_numOfMediaApps"
+ "_numOfPhoneApps"
+ "action"
+ "addLighthousePluginEvent:identifiers:error:"
+ "at_least_10"
+ "bundle record: %@ has supported intent %@ and supported media categories: %@"
+ "bundleIdentifier"
+ "choice"
+ "cohortName:cohortKey => %@=%@ for namespace %@"
+ "com.apple.Music"
+ "com.apple.podcasts"
+ "completedSetup"
+ "containingBundle"
+ "date"
+ "defaultWorkspace"
+ "domainToBundleIds"
+ "enabled"
+ "enumeratePluginsMatchingQuery:withBlock:"
+ "enumeratorWithOptions:"
+ "firstUpdate"
+ "firstUpdateAnyGesture"
+ "flowType"
+ "initWithExperimentID:deploymentID:treatmentID:"
+ "initWithPerformTrialTaskStatus:error:usePrivateUpload:"
+ "lsAppRecords"
+ "lsPluginKitExtensions"
+ "media"
+ "numOfMediaApps"
+ "numOfPhoneApps"
+ "objectForInfoDictionaryKey:ofClass:inScope:"
+ "phone"
+ "pillClicked"
+ "pluginkit record: %@ has supported intent %@ and supported media categories: %@"
+ "reportPluginForTrialClient:withError:"
+ "reportPluginSucceedForTrialClient:"
+ "resolveDomainToBundleIds"
+ "screenDistance"
+ "setDomainToBundleIds:"
+ "setWithSet:"
+ "supportedIntentMediaCategories"
+ "supportedIntents"
+ "timeIntervalSinceDate:"
+ "v24@?0@\"LSPlugInKitProxy\"8@\"NSError\"16"

```
