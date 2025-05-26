## PrivateFederatedLearning

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0x24a14
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x2810
+209.0.0.0.0
+  __TEXT.__text: 0x24c24
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0x2820
   __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x2b06
-  __TEXT.__oslogstring: 0x1c87
+  __TEXT.__cstring: 0x2c9c
+  __TEXT.__oslogstring: 0x1d30
   __TEXT.__gcc_except_tab: 0x224
   __TEXT.__ustring: 0x1e
   __TEXT.__unwind_info: 0x878
-  __TEXT.__objc_classname: 0x6d4
-  __TEXT.__objc_methname: 0x4d1b
-  __TEXT.__objc_methtype: 0xb30
+  __TEXT.__objc_classname: 0x70f
+  __TEXT.__objc_methname: 0x4d47
+  __TEXT.__objc_methtype: 0xaff
   __TEXT.__objc_stubs: 0x4180
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x520
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4fe8
-  __DATA_CONST.__objc_selrefs: 0x13d0
-  __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__objc_const: 0x1c08
-  __AUTH_CONST.__cfstring: 0x2a40
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__objc_const: 0x5038
+  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_arraydata: 0x130
+  __AUTH_CONST.__objc_const: 0x1c98
+  __AUTH_CONST.__cfstring: 0x2d00
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH.__objc_data: 0x1360
+  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH.__objc_data: 0x1400
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x320
+  __DATA.__objc_classrefs: 0x348
   __DATA.__objc_superrefs: 0x198
-  __DATA.__objc_ivar: 0x28c
-  __DATA.__data: 0x660
+  __DATA.__objc_ivar: 0x284
+  __DATA.__data: 0x600
   __DATA.__bss: 0xc8
   __DATA.__common: 0x10
-  - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 971
-  Symbols:   3531
-  CStrings:  1675
+  Functions: 965
+  Symbols:   3533
+  CStrings:  1697
 
Symbols:
+ +[FedStatsCohortQueryInstalledApps cohortInstance]
+ -[FedStatsCohortQueryInstalledApps .cxx_destruct]
+ -[FedStatsCohortQueryInstalledApps _isSupportedIntentMediaApp:::]
+ -[FedStatsCohortQueryInstalledApps cohortKeyForParameters:possibleError:]
+ -[FedStatsCohortQueryInstalledApps domainToBundleIds]
+ -[FedStatsCohortQueryInstalledApps init]
+ -[FedStatsCohortQueryInstalledApps lsAppRecords]
+ -[FedStatsCohortQueryInstalledApps lsPluginKitExtensions]
+ -[FedStatsCohortQueryInstalledApps numOfMediaApps]
+ -[FedStatsCohortQueryInstalledApps numOfPhoneApps]
+ -[FedStatsCohortQueryInstalledApps resolveDomainToBundleIds]
+ -[FedStatsCohortQueryInstalledApps setDomainToBundleIds:]
+ -[FedStatsCohortQueryInstalledAppsMedia cohortKeyForParameters:possibleError:]
+ -[FedStatsCohortQueryInstalledAppsPhone cohortKeyForParameters:possibleError:]
+ _INExtensionAttributesIntentsSupportedKey
+ _INExtensionAttributesSupportedIntentsKey
+ _INIntentsServiceExtensionPointName
+ _INSupportedMediaCategories
+ _INTENT_MEDIA_SUPPORTED_CATEGORIES
+ _INTENT_MEDIA_SUPPORTED_INTENTS
+ _NSExtensionPointName
+ _OBJC_CLASS_$_FedStatsCohortQueryInstalledApps
+ _OBJC_CLASS_$_FedStatsCohortQueryInstalledAppsMedia
+ _OBJC_CLASS_$_FedStatsCohortQueryInstalledAppsPhone
+ _OBJC_CLASS_$_INAddMediaIntent
+ _OBJC_CLASS_$_INPlayMediaIntent
+ _OBJC_CLASS_$_INSearchForMediaIntent
+ _OBJC_CLASS_$_INUpdateMediaAffinityIntent
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSDate
+ _OBJC_IVAR_$_FedStatsCohortQueryInstalledApps._domainToBundleIds
+ _OBJC_IVAR_$_FedStatsCohortQueryInstalledApps._numOfMediaApps
+ _OBJC_IVAR_$_FedStatsCohortQueryInstalledApps._numOfPhoneApps
+ _OBJC_METACLASS_$_FedStatsCohortQueryInstalledApps
+ _OBJC_METACLASS_$_FedStatsCohortQueryInstalledAppsMedia
+ _OBJC_METACLASS_$_FedStatsCohortQueryInstalledAppsPhone
+ __OBJC_$_CLASS_METHODS_FedStatsCohortQueryInstalledApps
+ __OBJC_$_INSTANCE_METHODS_FedStatsCohortQueryInstalledApps
+ __OBJC_$_INSTANCE_METHODS_FedStatsCohortQueryInstalledAppsMedia
+ __OBJC_$_INSTANCE_METHODS_FedStatsCohortQueryInstalledAppsPhone
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsCohortQueryInstalledApps
+ __OBJC_$_PROP_LIST_FedStatsCohortQueryInstalledApps
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsCohortQueryInstalledApps
+ __OBJC_CLASS_RO_$_FedStatsCohortQueryInstalledApps
+ __OBJC_CLASS_RO_$_FedStatsCohortQueryInstalledAppsMedia
+ __OBJC_CLASS_RO_$_FedStatsCohortQueryInstalledAppsPhone
+ __OBJC_METACLASS_RO_$_FedStatsCohortQueryInstalledApps
+ __OBJC_METACLASS_RO_$_FedStatsCohortQueryInstalledAppsMedia
+ __OBJC_METACLASS_RO_$_FedStatsCohortQueryInstalledAppsPhone
+ ___57-[FedStatsCohortQueryInstalledApps lsPluginKitExtensions]_block_invoke
+ ___57-[FedStatsCohortQueryInstalledApps lsPluginKitExtensions]_block_invoke.cold.1
+ ___57-[FedStatsCohortQueryInstalledApps lsPluginKitExtensions]_block_invoke.cold.2
+ ___block_descriptor_48_e8_32s40s_e38_v24?0"LSPlugInKitProxy"8"NSError"16ls32l8s40l8
+ _objc_msgSend$_isSupportedIntentMediaApp:::
+ _objc_msgSend$containingBundle
+ _objc_msgSend$date
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$enumeratePluginsMatchingQuery:withBlock:
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$lsAppRecords
+ _objc_msgSend$lsPluginKitExtensions
+ _objc_msgSend$nextObject
+ _objc_msgSend$numOfMediaApps
+ _objc_msgSend$numOfPhoneApps
+ _objc_msgSend$objectForInfoDictionaryKey:ofClass:inScope:
+ _objc_msgSend$resolveDomainToBundleIds
+ _objc_msgSend$set
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$supportedIntentMediaCategories
+ _objc_msgSend$supportedIntents
+ _objc_msgSend$timeIntervalSinceDate:
+ _sharedInstance.onceToken.168
- +[PFLBackgroundSession sharedInstance]
- -[PFLBackgroundSession .cxx_destruct]
- -[PFLBackgroundSession dataSource]
- -[PFLBackgroundSession didCompleteAllTasks]
- -[PFLBackgroundSession init]
- -[PFLBackgroundSession queue]
- -[PFLBackgroundSession readyCondition]
- -[PFLBackgroundSession registerWithIdentifier:]
- -[PFLBackgroundSession registerWithIdentifier:].cold.1
- -[PFLBackgroundSession resumeWithDataSource:]
- -[PFLBackgroundSession resumeWithDataSource:].cold.1
- -[PFLBackgroundSession session]
- -[PFLBackgroundSession setDataSource:]
- -[PFLBackgroundSession setSession:]
- -[PFLBackgroundSession setTask:]
- -[PFLBackgroundSession submitTaskRequestWithIdentifier:andError:]
- -[PFLBackgroundSession submitTaskRequestWithIdentifier:andError:].cold.1
- -[PFLBackgroundSession task]
- _OBJC_CLASS_$_BGProcessingTaskRequest
- _OBJC_CLASS_$_BGTaskScheduler
- _OBJC_CLASS_$_NSCondition
- _OBJC_CLASS_$_PFLBackgroundSession
- _OBJC_IVAR_$_PFLBackgroundSession._dataSource
- _OBJC_IVAR_$_PFLBackgroundSession._queue
- _OBJC_IVAR_$_PFLBackgroundSession._readyCondition
- _OBJC_IVAR_$_PFLBackgroundSession._session
- _OBJC_IVAR_$_PFLBackgroundSession._task
- _OBJC_METACLASS_$_PFLBackgroundSession
- __OBJC_$_CLASS_METHODS_PFLBackgroundSession
- __OBJC_$_INSTANCE_METHODS_PFLBackgroundSession
- __OBJC_$_INSTANCE_VARIABLES_PFLBackgroundSession
- __OBJC_$_PROP_LIST_PFLBackgroundSession
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PFLForegroundSessionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PFLForegroundSessionDelegate
- __OBJC_CLASS_PROTOCOLS_$_PFLBackgroundSession
- __OBJC_CLASS_RO_$_PFLBackgroundSession
- __OBJC_LABEL_PROTOCOL_$_PFLForegroundSessionDelegate
- __OBJC_METACLASS_RO_$_PFLBackgroundSession
- __OBJC_PROTOCOL_$_PFLForegroundSessionDelegate
- ___38+[PFLBackgroundSession sharedInstance]_block_invoke
- ___47-[PFLBackgroundSession registerWithIdentifier:]_block_invoke
- ___47-[PFLBackgroundSession registerWithIdentifier:]_block_invoke.8
- ___block_descriptor_48_e8_32s40s_e16_v16?0"BGTask"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- _objc_msgSend$getPendingTaskRequestsWithCompletionHandler:
- _objc_msgSend$lock
- _objc_msgSend$queue
- _objc_msgSend$readyCondition
- _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
- _objc_msgSend$session
- _objc_msgSend$setRequiresExternalPower:
- _objc_msgSend$setRequiresNetworkConnectivity:
- _objc_msgSend$setSession:
- _objc_msgSend$setTask:
- _objc_msgSend$setTaskCompletedWithSuccess:
- _objc_msgSend$shared
- _objc_msgSend$sharedScheduler
- _objc_msgSend$signal
- _objc_msgSend$submitAnalyticsForKey:value:
- _objc_msgSend$submitTaskRequest:error:
- _objc_msgSend$submitTaskRequestWithIdentifier:andError:
- _objc_msgSend$unlock
- _objc_msgSend$wait
- _sharedInstance.onceToken.133
CStrings:
+ "%d"
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
+ "_domainToBundleIds"
+ "_isSupportedIntentMediaApp:::"
+ "_numOfMediaApps"
+ "_numOfPhoneApps"
+ "action"
+ "at_least_10"
+ "bundle record: %@ has supported intent %@ and supported media categories: %@"
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
+ "intersectSet:"
+ "lsAppRecords"
+ "lsPluginKitExtensions"
+ "media"
+ "nextObject"
+ "numOfMediaApps"
+ "numOfPhoneApps"
+ "objectForInfoDictionaryKey:ofClass:inScope:"
+ "phone"
+ "pillClicked"
+ "pluginkit record: %@ has supported intent %@ and supported media categories: %@"
+ "resolveDomainToBundleIds"
+ "screenDistance"
+ "set"
+ "setDomainToBundleIds:"
+ "setWithSet:"
+ "supportedIntentMediaCategories"
+ "supportedIntents"
+ "timeIntervalSinceDate:"
+ "v24@?0@\"LSPlugInKitProxy\"8@\"NSError\"16"
- "%@ already submitted, skipping submission"
- "@\"BGTask\""
- "@\"NSCondition\""
- "@\"PFLForegroundSession\""
- "PFLBackgroundSession"
- "PFLForegroundSessionDelegate"
- "T@\"BGTask\",&,N,V_task"
- "T@\"NSCondition\",R,N,V_readyCondition"
- "T@\"PFLForegroundSession\",&,N,V_session"
- "_readyCondition"
- "_session"
- "_task"
- "failed to register task with identifier %@"
- "failed to submit task request err:%@"
- "getPendingTaskRequestsWithCompletionHandler:"
- "launch handler launching task %@"
- "lock"
- "not ready to start PFLSession dataSource:%@"
- "pendingTasks"
- "readyCondition"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "registerWithIdentifier:"
- "resume already called, ignoring dataSource:%@"
- "resumeWithDataSource:"
- "session"
- "setRequiresExternalPower:"
- "setRequiresNetworkConnectivity:"
- "setSession:"
- "setTask:"
- "setTaskCompletedWithSuccess:"
- "sharedScheduler"
- "starting PFLSession with dataSource:%@"
- "statusCode"
- "submitTaskRequest:error:"
- "submitTaskRequestWithIdentifier:andError:"
- "successfully registered BGTask with identifier %@"
- "successfully submitted identifier %@"
- "unlock"
- "v16@?0@\"BGTask\"8"
- "wait"

```
