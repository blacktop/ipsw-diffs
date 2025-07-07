## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-466.0.0.0.0
-  __TEXT.__text: 0x14f69c
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__delay_helper: 0x478
-  __TEXT.__objc_methlist: 0xbd54
-  __TEXT.__const: 0xe68
-  __TEXT.__dlopen_cstrs: 0x101
-  __TEXT.__oslogstring: 0x1cd62
-  __TEXT.__gcc_except_tab: 0x9afc
-  __TEXT.__cstring: 0x15887
-  __TEXT.__unwind_info: 0x42c0
+468.0.0.0.0
+  __TEXT.__text: 0x14f544
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__delay_helper: 0x6f4
+  __TEXT.__objc_methlist: 0xbd9c
+  __TEXT.__const: 0xe58
+  __TEXT.__cstring: 0x1579b
+  __TEXT.__oslogstring: 0x1cecd
+  __TEXT.__gcc_except_tab: 0x9a50
+  __TEXT.__unwind_info: 0x4358
   __TEXT.__objc_classname: 0x2850
-  __TEXT.__objc_methname: 0x1e594
-  __TEXT.__objc_methtype: 0x5668
-  __TEXT.__objc_stubs: 0x152a0
-  __DATA_CONST.__got: 0x1358
+  __TEXT.__objc_methname: 0x1e63e
+  __TEXT.__objc_methtype: 0x568d
+  __TEXT.__objc_stubs: 0x15360
+  __DATA_CONST.__got: 0x1378
   __DATA_CONST.__const: 0x6a40
   __DATA_CONST.__objc_classlist: 0x908
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60c8
+  __DATA_CONST.__objc_selrefs: 0x60f8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x5e0
-  __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0x11c0
-  __AUTH_CONST.__cfstring: 0xd960
-  __AUTH_CONST.__objc_const: 0x16790
-  __AUTH_CONST.__objc_intobj: 0x9a8
+  __DATA_CONST.__objc_arraydata: 0x338
+  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__const: 0x1240
+  __AUTH_CONST.__cfstring: 0xd880
+  __AUTH_CONST.__objc_const: 0x16798
+  __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1798
   __AUTH.__data: 0x690
   __DATA.__objc_ivar: 0x8e8
-  __DATA.__data: 0x2684
+  __DATA.__data: 0x2688
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x120
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_ivar: 0x1b8
   __DATA_DIRTY.__objc_data: 0x42b8
-  __DATA_DIRTY.__bss: 0x380
+  __DATA_DIRTY.__bss: 0x360
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/PushKit.framework/PushKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers
+  - /System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
+  - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
-  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C6AAB0E8-C8C3-365B-B438-EAC13F5995D1
-  Functions: 4822
-  Symbols:   17423
-  CStrings:  10616
+  UUID: 8E58B461-13F6-3720-8FF9-A90DBE51707B
+  Functions: 4825
+  Symbols:   17444
+  CStrings:  10608
 
Symbols:
+ +[TRIPushServiceConnection _validateChannelId:]
+ +[TRIPushServiceConnection subsetOfChannels:currentChannelCount:hardLimit:]
+ -[TRIPersistentUserSettings persistActiveDictationLocales:]
+ -[TRIPersistentUserSettings persistedActiveDictationLocales]
+ -[TRIPushServiceConnection _subscribeToChannels:]
+ -[TRIPushServiceConnection subscribeToChannels:]
+ -[TRIPushServiceConnectionMultiplexer _expectedChannelsForRolloutDeployments:experimentIds:maxChannelsAllowed:]
+ -[TRISandboxedPushServiceConnection subscribeToChannels:]
+ _OBJC_CLASS_$_CTBundle
+ _OBJC_CLASS_$_CoreTelephonyClient
+ _OBJC_CLASS_$_TIInputModeController
+ _OBJC_CLASS_$__ANEDeviceInfo
+ __OBJC_$_CATEGORY_CLASS_METHODS_TRIClientTreatment_$_CloudKit
+ __OBJC_$_CATEGORY_NSDictionary_$_TRICloudKit
+ __OBJC_$_CATEGORY_NSMutableDictionary_$_TRI
+ __OBJC_$_CATEGORY_NSString_$_TRITreatmentId
+ __OBJC_$_CATEGORY_TRIClientTreatment_$_CloudKit
+ __OBJC_$_CATEGORY_TRISystemDimensions_$_Factory
+ __OBJC_$_CLASS_METHODS_NSDictionary(TRICloudKit|TRI|TRIDAG|TRIFunctions)
+ __OBJC_$_CLASS_METHODS_TRIClientExperimentArtifact(CloudKit|Counterfactuals|FactorPacks)
+ __OBJC_$_CLASS_METHODS_TRIExperimentDatabase(EnvVarNamespacesProviding|SysctlNamespacesProviding|CountProviding)
+ __OBJC_$_CLASS_METHODS_TRIExperimentPostLaunchEvent(ExperimentHistoryRecord|EventFactory)
+ __OBJC_$_CLASS_METHODS_TRIPushServiceConnection
+ __OBJC_$_CLASS_METHODS_TRISystemDimensions(Factory|ServerFactory)
+ __OBJC_$_CLASS_METHODS_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(TRICloudKit|TRI|TRIDAG|TRIFunctions)
+ __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(TRI|TRIFunctions)
+ __OBJC_$_INSTANCE_METHODS_NSString(TRITreatmentId|TRIFunctions)
+ __OBJC_$_INSTANCE_METHODS_TRIClientExperimentArtifact(CloudKit|Counterfactuals|FactorPacks)
+ __OBJC_$_INSTANCE_METHODS_TRIClientTreatment(CloudKit|TRIUtil)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentDatabase(EnvVarNamespacesProviding|SysctlNamespacesProviding|CountProviding)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentHistoryDatabase(PostLaunchLogging|PreviousStateProviding)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentPostLaunchEvent(ExperimentHistoryRecord|EventFactory)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentRecord(VersionedNamespaces|Counterfactuals|Utils)
+ __OBJC_$_INSTANCE_METHODS_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentDatabase(EnvVarNamespacesProviding|SysctlNamespacesProviding|CountProviding)
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentHistoryDatabase(PostLaunchLogging|PreviousStateProviding)
+ __OBJC_CLASS_PROTOCOLS_$_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
+ ___106-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]_block_invoke.204
+ ___111-[TRIPushServiceConnectionMultiplexer _expectedChannelsForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke
+ ___111-[TRIPushServiceConnectionMultiplexer _expectedChannelsForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke_2
+ ___122-[TRIPushServiceConnectionMultiplexer ensureSubscriptionsExistOnlyForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke
+ ___122-[TRIPushServiceConnectionMultiplexer ensureSubscriptionsExistOnlyForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke.49
+ ___122-[TRIPushServiceConnectionMultiplexer ensureSubscriptionsExistOnlyForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke_2
+ ___48-[TRIPushServiceConnection subscribeToChannels:]_block_invoke
+ ___49-[TRIPushServiceConnection _subscribeToChannels:]_block_invoke
+ ___57-[TRISandboxedPushServiceConnection subscribeToChannels:]_block_invoke
+ ___75+[TRIPushServiceConnection subsetOfChannels:currentChannelCount:hardLimit:]_block_invoke
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.237
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.241
+ ___block_descriptor_32_e26_16?0"TRIPushChannelId"8l
+ ___block_descriptor_40_e26_16?0"TRIPushChannelId"8l
+ ___block_descriptor_40_e8_32s_e26_B16?0"TRIPushChannelId"8ls32l8
+ ___block_literal_global.103
+ ___block_literal_global.113
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.235
+ ___block_literal_global.24
+ ___block_literal_global.323
+ ___block_literal_global.384
+ _dlopenHelper$AppleNeuralEngine
+ _dlopenHelper$CoreTelephony
+ _dlopenHelper$TextInput
+ _dlopenHelperFlag$AppleNeuralEngine
+ _dlopenHelperFlag$CoreTelephony
+ _dlopenHelperFlag$TextInput
+ _gotLoadHelper_x20$_OBJC_CLASS_$__ANEDeviceInfo
+ _gotLoadHelper_x8$_OBJC_CLASS_$_CTBundle
+ _gotLoadHelper_x8$_OBJC_CLASS_$_CoreTelephonyClient
+ _gotLoadHelper_x8$_OBJC_CLASS_$_TIInputModeController
+ _objc_msgSend$_expectedChannelsForRolloutDeployments:experimentIds:maxChannelsAllowed:
+ _objc_msgSend$_pas_mappedSetWithTransform:
+ _objc_msgSend$_subscribeToChannels:
+ _objc_msgSend$_validateChannelId:
+ _objc_msgSend$persistActiveDictationLocales:
+ _objc_msgSend$persistedActiveDictationLocales
+ _objc_msgSend$subscribeToChannels:
+ _objc_msgSend$subscribeToChannels:forTopic:
+ _objc_msgSend$subsetOfChannels:currentChannelCount:hardLimit:
- -[TRIPersistentUserSettings persistActiveDicationLocales:]
- -[TRIPersistentUserSettings persistedActiveDicationLocales]
- -[TRIPushServiceConnectionMultiplexer _expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:]
- _CoreTelephonyLibrary
- _CoreTelephonyLibraryCore.frameworkLibrary
- __OBJC_$_CATEGORY_INSTANCE_METHODS_TRIClientTreatment_$_TRIUtil
- __OBJC_$_CATEGORY_NSDictionary_$_TRIFunctions
- __OBJC_$_CATEGORY_NSMutableDictionary_$_TRIFunctions
- __OBJC_$_CATEGORY_NSString_$_TRIFunctions
- __OBJC_$_CATEGORY_TRIClientTreatment_$_TRIUtil
- __OBJC_$_CATEGORY_TRISystemDimensions_$_ServerFactory
- __OBJC_$_CLASS_METHODS_NSDictionary(TRIFunctions|TRICloudKit|TRI|TRIDAG)
- __OBJC_$_CLASS_METHODS_TRIClientExperimentArtifact(Counterfactuals|FactorPacks|CloudKit)
- __OBJC_$_CLASS_METHODS_TRIClientTreatment(TRIUtil|CloudKit)
- __OBJC_$_CLASS_METHODS_TRIExperimentDatabase(SysctlNamespacesProviding|EnvVarNamespacesProviding|CountProviding)
- __OBJC_$_CLASS_METHODS_TRIExperimentPostLaunchEvent(EventFactory|ExperimentHistoryRecord)
- __OBJC_$_CLASS_METHODS_TRISystemDimensions(ServerFactory|Factory)
- __OBJC_$_CLASS_METHODS_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(TRIFunctions|TRICloudKit|TRI|TRIDAG)
- __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(TRIFunctions|TRI)
- __OBJC_$_INSTANCE_METHODS_NSString(TRIFunctions|TRITreatmentId)
- __OBJC_$_INSTANCE_METHODS_TRIClientExperimentArtifact(Counterfactuals|FactorPacks|CloudKit)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentDatabase(SysctlNamespacesProviding|EnvVarNamespacesProviding|CountProviding)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentHistoryDatabase(PreviousStateProviding|PostLaunchLogging)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentPostLaunchEvent(EventFactory|ExperimentHistoryRecord)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentRecord(Utils|VersionedNamespaces|Counterfactuals)
- __OBJC_$_INSTANCE_METHODS_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
- __OBJC_CLASS_PROTOCOLS_$_TRIExperimentDatabase(SysctlNamespacesProviding|EnvVarNamespacesProviding|CountProviding)
- __OBJC_CLASS_PROTOCOLS_$_TRIExperimentHistoryDatabase(PreviousStateProviding|PostLaunchLogging)
- __OBJC_CLASS_PROTOCOLS_$_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
- ___106-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:serverContext:completion:]_block_invoke.202
- ___113-[TRIPushServiceConnectionMultiplexer _expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke
- ___113-[TRIPushServiceConnectionMultiplexer _expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke_2
- ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.235
- ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.239
- ___AppleNeuralEngineLibraryCore_block_invoke
- ___CoreTelephonyLibraryCore_block_invoke
- ___TextInputLibraryCore_block_invoke
- ___block_descriptor_48_e5_v8?0l
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.233
- ___block_literal_global.30
- ___block_literal_global.319
- ___getCTBundleClass_block_invoke
- ___getCoreTelephonyClientClass_block_invoke
- ___getTIInputModeControllerClass_block_invoke
- ___get_ANEDeviceInfoClass_block_invoke
- __sl_dlopen
- _audit_stringAppleNeuralEngine
- _audit_stringCoreTelephony
- _audit_stringTextInput
- _getCTBundleClass.softClass
- _getCoreTelephonyClientClass.softClass
- _get_ANEDeviceInfoClass
- _objc_getClass
- _objc_msgSend$_expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:
- _objc_msgSend$persistActiveDicationLocales:
- _objc_msgSend$persistedActiveDicationLocales
CStrings:
+ "/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony"
+ "/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine"
+ "/System/Library/PrivateFrameworks/TextInput.framework/TextInput"
+ "@16@?0@\"TRIPushChannelId\"8"
+ "@40@0:8@16q24q32"
+ "Adding %ld subscriptions for the following channels: %@"
+ "B16@?0@\"TRIPushChannelId\"8"
+ "Jun 28 2025"
+ "New subscription denied since we reached the channel limit (current: %tu, limit: %tu)"
+ "Only some of the requested channels will be subscribed since we reached the channel limit (current: %tu, wanted to subscribe: %tu, actual to be subscribed: %tu, limit: %tu)"
+ "Subscribing to channels: %@"
+ "TrialXP-468"
+ "Unsubscribing %ld channels: %@"
+ "[Sandbox] Subscribing to channels %@"
+ "_expectedChannelsForRolloutDeployments:experimentIds:maxChannelsAllowed:"
+ "_pas_mappedSetWithTransform:"
+ "_subscribeToChannels:"
+ "_validateChannelId:"
+ "experiment %@ with namespace %@ has compatibility version %u which is incompatible with compatibility version %u found locally"
+ "persistActiveDictationLocales:"
+ "persistedActiveDictationLocales"
+ "subscribeToChannels:"
+ "subscribeToChannels:forTopic:"
+ "subsetOfChannels:currentChannelCount:hardLimit:"
+ "v24@0:8@\"NSArray\"16"
- "%s"
- "CTBundle"
- "Class getCTBundleClass(void)_block_invoke"
- "Class getCoreTelephonyClientClass(void)_block_invoke"
- "Class getTIInputModeControllerClass(void)_block_invoke"
- "CoreTelephonyClient"
- "Jun 13 2025"
- "TIInputModeController"
- "TRICellularParameterManager.m"
- "TRISystemInfo.m"
- "TrialXP-466"
- "Unable to find class %s"
- "Unable to load soft-linked CTBundle class"
- "Unable to load soft-linked CoreTelephonyClient class"
- "Unable to load soft-linked TIInputModeController class"
- "Unable to load soft-linked _ANEDeviceInfo class"
- "_ANEDeviceInfo"
- "_expectedChannelIdsForRolloutDeployments:experimentIds:maxChannelsAllowed:"
- "experiment %@ with namespace %@ has compatibility version %u which is incompatible with compability version %u found locally"
- "persistActiveDicationLocales:"
- "persistedActiveDicationLocales"
- "softlink:o:path:/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony"
- "softlink:o:path:/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine"
- "softlink:r:path:/System/Library/PrivateFrameworks/TextInput.framework/TextInput"
- "void *CoreTelephonyLibrary(void)"
- "void *TextInputLibrary(void)"

```
