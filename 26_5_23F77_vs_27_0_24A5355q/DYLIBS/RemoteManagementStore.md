## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore`

```diff

-585.120.2.0.0
-  __TEXT.__text: 0x3ae94
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x2390
-  __TEXT.__const: 0x4cc
-  __TEXT.__cstring: 0x107c
-  __TEXT.__oslogstring: 0x33b7
-  __TEXT.__gcc_except_tab: 0x3c4
+621.0.0.502.1
+  __TEXT.__text: 0x3a784
+  __TEXT.__objc_methlist: 0x2420
+  __TEXT.__const: 0x4dc
+  __TEXT.__cstring: 0x10ed
+  __TEXT.__oslogstring: 0x33e7
+  __TEXT.__gcc_except_tab: 0x3a4
   __TEXT.__swift5_typeref: 0x2bf
   __TEXT.__swift5_fieldmd: 0xa8
   __TEXT.__constg_swiftt: 0x9c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_capture: 0x118
+  __TEXT.__swift5_capture: 0x128
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0xef0
-  __TEXT.__eh_frame: 0xaf8
-  __TEXT.__objc_classname: 0x69a
-  __TEXT.__objc_methname: 0x7033
-  __TEXT.__objc_methtype: 0x1754
-  __TEXT.__objc_stubs: 0x4540
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0xf30
+  __TEXT.__swift_as_cont: 0xb4
+  __TEXT.__unwind_info: 0xe90
+  __TEXT.__eh_frame: 0xb60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf58
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x1598
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__cfstring: 0x1020
-  __AUTH_CONST.__objc_const: 0x3638
+  __DATA_CONST.__got: 0x410
+  __AUTH_CONST.__const: 0x7d8
+  __AUTH_CONST.__cfstring: 0x1040
+  __AUTH_CONST.__objc_const: 0x36b8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x6b0
   __AUTH.__objc_data: 0x70
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1ac
-  __DATA.__data: 0x5f0
-  __DATA.__bss: 0x540
+  __DATA.__objc_ivar: 0x1b0
+  __DATA.__data: 0x5e0
+  __DATA.__bss: 0x570
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A98DC37D-3720-324F-97D1-3F20FB3BFD79
-  Functions: 1332
-  Symbols:   3949
-  CStrings:  1710
+  UUID: 29A016E0-2D48-34C3-BB22-018ED5CAEF6D
+  Functions: 1342
+  Symbols:   4011
+  CStrings:  595
 
Symbols:
+ +[RMAssetResolverController resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:]
+ +[RMAssetResolverController resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:].cold.1
+ +[RMAssetResolverController resolveKeychainPasswordAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]
+ +[RMAssetResolverController resolveKeychainPasswordAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:].cold.1
+ +[RMConfigurationSubscriberClient _preWarmLocale]
+ +[RMLog(baseStore) baseStore]
+ +[RMLog(baseStore) baseStore].cold.1
+ +[RMLog(observerStore) observerStore]
+ +[RMLog(observerStore) observerStore].cold.1
+ +[RMLog(providerStore) providerStore]
+ +[RMLog(providerStore) providerStore].cold.1
+ +[RMLog(subscriberStore) subscriberStore]
+ +[RMLog(subscriberStore) subscriberStore].cold.1
+ +[RMStoreDeclarationKey newDeclarationKeyWithSubscriberIdentifier:store:declaration:assets:]
+ -[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:completionHandler:].cold.3
+ -[RMConfigurationSingleApplicator _installDeclarationKey:scope:configurations:completionHandler:].cold.3
+ -[RMStoreProfilesController declarationKeyForReference:]
+ -[RMStoreProfilesController declarationKeyForStore:declaration:assets:]
+ -[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:]
+ -[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:].cold.1
+ -[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:].cold.2
+ -[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:].cold.3
+ -[RMSubscribedConfigurationReference declarationError]
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table34
+ GCC_except_table7
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_IVAR_$_RMSubscribedConfigurationReference._declarationError
+ __OBJC_$_CLASS_METHODS_RMLog(assetResolverController|baseStore|configurationCombineApplicator|configurationMultipleApplicator|configurationSingleApplicator|configurationSubscriberClient|configurationSubscriberDelegate|configurationSubscriberEventStream|configurationSubscriberService|observerStore|profileStore|providerStore|statusPublisherDelegate|statusPublisherDescription|storeKeychainController|profilesAdapter|profilesController|subscribedConfigurationReference|subscriberStore)
+ ___100-[RMConfigurationMultipleApplicator _installDeclarationKeys:scope:configurations:completionHandler:]_block_invoke.53
+ ___100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.87
+ ___100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.87.cold.1
+ ___100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.87.cold.2
+ ___102-[RMConfigurationCombineApplicator _installDeclarationKeysWithScope:configurations:completionHandler:]_block_invoke.54
+ ___102-[RMConfigurationCombineApplicator _installDeclarationKeysWithScope:configurations:completionHandler:]_block_invoke.54.cold.1
+ ___106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.23
+ ___106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.23.cold.1
+ ___106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.16
+ ___106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.16.cold.1
+ ___109-[RMConfigurationSubscriberDelegate didFetchConfigurationsByType:storesByIdentifier:scope:completionHandler:]_block_invoke.11
+ ___117+[RMAssetResolverController resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:]_block_invoke
+ ___117+[RMAssetResolverController resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:]_block_invoke_2
+ ___120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke.32
+ ___120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke.33
+ ___122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.58
+ ___122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.58.cold.1
+ ___122-[RMConfigurationSubscriberDelegate didFetchConfigurationsWithVisibleUIByType:storesByIdentifier:scope:completionHandler:]_block_invoke.14
+ ___122-[RMConfigurationSubscriberDelegate didFetchConfigurationsWithVisibleUIByType:storesByIdentifier:scope:completionHandler:]_block_invoke_2.16
+ ___153+[RMAssetResolverController resolveKeychainPasswordAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]_block_invoke
+ ___153+[RMAssetResolverController resolveKeychainPasswordAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]_block_invoke_2
+ ___29+[RMLog(baseStore) baseStore]_block_invoke
+ ___37+[RMLog(observerStore) observerStore]_block_invoke
+ ___37+[RMLog(providerStore) providerStore]_block_invoke
+ ___38-[RMBaseStore metadataReturningError:]_block_invoke.49
+ ___41+[RMLog(subscriberStore) subscriberStore]_block_invoke
+ ___41-[RMBaseStore metadataValueForKey:error:]_block_invoke.51
+ ___48-[RMBaseStore fetchDataAtURL:completionHandler:]_block_invoke.43
+ ___48-[RMBaseStore fetchDataAtURL:completionHandler:]_block_invoke.43.cold.1
+ ___49-[RMBaseStore declarationsWithCompletionHandler:]_block_invoke.38
+ ___49-[RMBaseStore declarationsWithCompletionHandler:]_block_invoke.38.cold.1
+ ___49-[RMProviderStore setMetadataValue:forKey:error:]_block_invoke.33
+ ___52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.18
+ ___52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.18.cold.1
+ ___53+[RMObserverStore storesWithScope:completionHandler:]_block_invoke.10
+ ___53+[RMObserverStore storesWithScope:completionHandler:]_block_invoke.10.cold.1
+ ___53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.27
+ ___53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.27.cold.1
+ ___53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.29
+ ___53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.29.cold.1
+ ___53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.31
+ ___53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.31.cold.1
+ ___53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.81
+ ___53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.81.cold.1
+ ___53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.81.cold.2
+ ___55+[RMSubscriberStore storesWithScope:completionHandler:]_block_invoke.10
+ ___55+[RMSubscriberStore storesWithScope:completionHandler:]_block_invoke.10.cold.1
+ ___55-[RMBaseStore declarationsWithTypes:completionHandler:]_block_invoke.40
+ ___55-[RMBaseStore declarationsWithTypes:completionHandler:]_block_invoke.40.cold.1
+ ___56-[RMBaseStore declarationManifestWithCompletionHandler:]_block_invoke.34
+ ___56-[RMBaseStore declarationManifestWithCompletionHandler:]_block_invoke.34.cold.1
+ ___59-[RMBaseStore declarationWithIdentifier:completionHandler:]_block_invoke.36
+ ___59-[RMBaseStore declarationWithIdentifier:completionHandler:]_block_invoke.36.cold.1
+ ___60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.20
+ ___60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.20.cold.1
+ ___60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.78
+ ___60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.78.cold.1
+ ___63+[RMObserverStore storeWithIdentifier:scope:completionHandler:]_block_invoke.8
+ ___63+[RMObserverStore storeWithIdentifier:scope:completionHandler:]_block_invoke.8.cold.1
+ ___63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.26
+ ___63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.26.cold.1
+ ___65+[RMSubscriberStore storeWithIdentifier:scope:completionHandler:]_block_invoke.8
+ ___65+[RMSubscriberStore storeWithIdentifier:scope:completionHandler:]_block_invoke.8.cold.1
+ ___69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.25
+ ___69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.25.cold.1
+ ___69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.30
+ ___69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.30.cold.1
+ ___69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.80
+ ___69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.80.cold.1
+ ___69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.80.cold.2
+ ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.46
+ ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.46.cold.1
+ ___73-[RMObserverStore displayableProfileConfigurationsWithCompletionHandler:]_block_invoke.13
+ ___73-[RMObserverStore displayableProfileConfigurationsWithCompletionHandler:]_block_invoke.13.cold.1
+ ___75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.45
+ ___75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.45.cold.1
+ ___75-[RMObserverStore displayPropertiesForConfigurationsWithCompletionHandler:]_block_invoke.12
+ ___75-[RMObserverStore displayPropertiesForConfigurationsWithCompletionHandler:]_block_invoke.12.cold.1
+ ___75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.76
+ ___75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.76.cold.1
+ ___77-[RMBaseStore setShouldInstallConfiguration:shouldInstall:completionHandler:]_block_invoke.42
+ ___77-[RMBaseStore setShouldInstallConfiguration:shouldInstall:completionHandler:]_block_invoke.42.cold.1
+ ___83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.86
+ ___83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.86.cold.1
+ ___83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.86.cold.2
+ ___84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.32
+ ___84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.32.cold.1
+ ___87-[RMStoreProfilesController installProfileData:store:declarationKey:completionHandler:]_block_invoke
+ ___87-[RMStoreProfilesController installProfileData:store:declarationKey:completionHandler:]_block_invoke.24
+ ___87-[RMStoreProfilesController installProfileData:store:declarationKey:completionHandler:]_block_invoke.24.cold.1
+ ___87-[RMStoreProfilesController installProfileData:store:declarationKey:completionHandler:]_block_invoke_2
+ ___87-[RMStoreProfilesController installProfileData:store:declarationKey:completionHandler:]_block_invoke_2.cold.1
+ ___87-[RMStoreProfilesController installProfileData:store:declarationKey:completionHandler:]_block_invoke_2.cold.2
+ ___89-[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:]_block_invoke
+ ___89-[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:]_block_invoke.cold.1
+ ___89-[RMStoreProfilesController installProfileAtPath:store:declarationKey:completionHandler:]_block_invoke.cold.2
+ ___90-[RMConfigurationSubscriberClient sendStatusKeys:storeIdentifier:scope:completionHandler:]_block_invoke.31
+ ___90-[RMConfigurationSubscriberClient sendStatusKeys:storeIdentifier:scope:completionHandler:]_block_invoke.31.cold.1
+ ___95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.14
+ ___95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.14.cold.1
+ ___97-[RMConfigurationSingleApplicator _installDeclarationKey:scope:configurations:completionHandler:]_block_invoke.54
+ ___99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke.35
+ ___99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke.36
+ ___block_descriptor_64_e8_32s40s48bs_e39_v24?0"RMSubscriberStore"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e44_v24?0"RMModelDeclarationBase"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_literal_global.19
+ ___block_literal_global.48
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.4
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.45
+ ___swift_closure_destructor.4Tm
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.69
+ ___swift_closure_destructor.73
+ ___swift_closure_destructor.77
+ ___swift_closure_destructor.8
+ _baseStore.onceToken
+ _baseStore.result
+ _block_copy_helper.61
+ _block_copy_helper.64
+ _block_copy_helper.84
+ _block_copy_helper.87
+ _block_copy_helper.97
+ _block_descriptor.63
+ _block_descriptor.66
+ _block_descriptor.86
+ _block_descriptor.89
+ _block_descriptor.99
+ _block_destroy_helper.62
+ _block_destroy_helper.65
+ _block_destroy_helper.85
+ _block_destroy_helper.88
+ _block_destroy_helper.98
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_preWarmLocale
+ _objc_msgSend$baseStore
+ _objc_msgSend$currentLocale
+ _objc_msgSend$declarationError
+ _objc_msgSend$deviceConfigurationSettingsSchemas
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$newDeclarationKeyWithSubscriberIdentifier:store:declaration:assets:
+ _objc_msgSend$resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:
+ _objc_msgSend$subscriberStore
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _observerStore.onceToken
+ _observerStore.result
+ _providerStore.onceToken
+ _providerStore.result
+ _subscriberStore.onceToken
+ _subscriberStore.result
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x25
- +[RMAssetResolverController resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:].cold.1
- -[RMConfigurationCombineApplicator _installDeclarationKeysWithScope:configurations:completionHandler:].cold.1
- -[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:]
- -[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:].cold.1
- -[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:].cold.2
- -[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:].cold.3
- -[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]
- GCC_except_table24
- GCC_except_table32
- GCC_except_table6
- GCC_except_table72
- GCC_except_table74
- GCC_except_table81
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- __OBJC_$_CLASS_METHODS_RMLog(assetResolverController|configurationCombineApplicator|configurationMultipleApplicator|configurationSingleApplicator|configurationSubscriberClient|configurationSubscriberDelegate|configurationSubscriberEventStream|configurationSubscriberService|profileStore|statusPublisherDelegate|statusPublisherDescription|storeKeychainController|profilesAdapter|profilesController|subscribedConfigurationReference)
- ___100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.82
- ___100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.82.cold.1
- ___100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.82.cold.2
- ___102-[RMConfigurationCombineApplicator _installDeclarationKeysWithScope:configurations:completionHandler:]_block_invoke.55
- ___102-[RMConfigurationCombineApplicator _installDeclarationKeysWithScope:configurations:completionHandler:]_block_invoke.55.cold.1
- ___106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.18
- ___106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.18.cold.1
- ___106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.11
- ___106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.11.cold.1
- ___109-[RMConfigurationSubscriberDelegate didFetchConfigurationsByType:storesByIdentifier:scope:completionHandler:]_block_invoke.12
- ___120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke.30
- ___120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke.31
- ___122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.60
- ___122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.60.cold.1
- ___122-[RMConfigurationSubscriberDelegate didFetchConfigurationsWithVisibleUIByType:storesByIdentifier:scope:completionHandler:]_block_invoke.15
- ___122-[RMConfigurationSubscriberDelegate didFetchConfigurationsWithVisibleUIByType:storesByIdentifier:scope:completionHandler:]_block_invoke_2.17
- ___141+[RMAssetResolverController resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:]_block_invoke
- ___38-[RMBaseStore metadataReturningError:]_block_invoke.41
- ___41-[RMBaseStore metadataValueForKey:error:]_block_invoke.43
- ___48-[RMBaseStore fetchDataAtURL:completionHandler:]_block_invoke.37
- ___48-[RMBaseStore fetchDataAtURL:completionHandler:]_block_invoke.37.cold.1
- ___49-[RMBaseStore declarationsWithCompletionHandler:]_block_invoke.33
- ___49-[RMBaseStore declarationsWithCompletionHandler:]_block_invoke.33.cold.1
- ___49-[RMProviderStore setMetadataValue:forKey:error:]_block_invoke.28
- ___52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.13
- ___52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.13.cold.1
- ___53+[RMObserverStore storesWithScope:completionHandler:]_block_invoke.5
- ___53+[RMObserverStore storesWithScope:completionHandler:]_block_invoke.5.cold.1
- ___53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.22
- ___53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.22.cold.1
- ___53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.24
- ___53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.24.cold.1
- ___53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.26
- ___53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.26.cold.1
- ___53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.76
- ___53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.76.cold.1
- ___53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.76.cold.2
- ___55+[RMSubscriberStore storesWithScope:completionHandler:]_block_invoke.5
- ___55+[RMSubscriberStore storesWithScope:completionHandler:]_block_invoke.5.cold.1
- ___55-[RMBaseStore declarationsWithTypes:completionHandler:]_block_invoke.35
- ___55-[RMBaseStore declarationsWithTypes:completionHandler:]_block_invoke.35.cold.1
- ___56-[RMBaseStore declarationManifestWithCompletionHandler:]_block_invoke.29
- ___56-[RMBaseStore declarationManifestWithCompletionHandler:]_block_invoke.29.cold.1
- ___59-[RMBaseStore declarationWithIdentifier:completionHandler:]_block_invoke.31
- ___59-[RMBaseStore declarationWithIdentifier:completionHandler:]_block_invoke.31.cold.1
- ___60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.15
- ___60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.15.cold.1
- ___60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.73
- ___60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.73.cold.1
- ___63+[RMObserverStore storeWithIdentifier:scope:completionHandler:]_block_invoke.3
- ___63+[RMObserverStore storeWithIdentifier:scope:completionHandler:]_block_invoke.3.cold.1
- ___63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.21
- ___63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.21.cold.1
- ___65+[RMSubscriberStore storeWithIdentifier:scope:completionHandler:]_block_invoke.3
- ___65+[RMSubscriberStore storeWithIdentifier:scope:completionHandler:]_block_invoke.3.cold.1
- ___69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.20
- ___69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.20.cold.1
- ___69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.25
- ___69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.25.cold.1
- ___69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.75
- ___69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.75.cold.1
- ___69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.75.cold.2
- ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.40
- ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.40.cold.1
- ___73-[RMObserverStore displayableProfileConfigurationsWithCompletionHandler:]_block_invoke.8
- ___73-[RMObserverStore displayableProfileConfigurationsWithCompletionHandler:]_block_invoke.8.cold.1
- ___75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.39
- ___75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.39.cold.1
- ___75-[RMObserverStore displayPropertiesForConfigurationsWithCompletionHandler:]_block_invoke.7
- ___75-[RMObserverStore displayPropertiesForConfigurationsWithCompletionHandler:]_block_invoke.7.cold.1
- ___75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.71
- ___75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.71.cold.1
- ___77-[RMBaseStore setShouldInstallConfiguration:shouldInstall:completionHandler:]_block_invoke.36
- ___77-[RMBaseStore setShouldInstallConfiguration:shouldInstall:completionHandler:]_block_invoke.36.cold.1
- ___83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.81
- ___83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.81.cold.1
- ___83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.81.cold.2
- ___84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.27
- ___84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.27.cold.1
- ___87-[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:]_block_invoke
- ___87-[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:]_block_invoke.cold.1
- ___87-[RMStoreProfilesController _installProfileAtPath:store:declaration:completionHandler:]_block_invoke.cold.2
- ___88-[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]_block_invoke
- ___88-[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]_block_invoke.32
- ___88-[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]_block_invoke.32.cold.1
- ___88-[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]_block_invoke_2
- ___88-[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]_block_invoke_2.cold.1
- ___88-[RMStoreProfilesController _installProfileData:store:declarationKey:completionHandler:]_block_invoke_2.cold.2
- ___90-[RMConfigurationSubscriberClient sendStatusKeys:storeIdentifier:scope:completionHandler:]_block_invoke.30
- ___90-[RMConfigurationSubscriberClient sendStatusKeys:storeIdentifier:scope:completionHandler:]_block_invoke.30.cold.1
- ___95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.9
- ___95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.9.cold.1
- ___99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke.33
- ___99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke.34
- ___block_descriptor_64_e8_32s40s48bs_e66_v32?0"RMModelDeclarationBase"8"RMSubscriberStore"16"NSError"24ls48l8s32l8s40l8
- ___block_literal_global.16
- __os_log_default
- _block_copy_helper.62
- _block_copy_helper.65
- _block_copy_helper.80
- _block_copy_helper.83
- _block_copy_helper.89
- _block_descriptor.64
- _block_descriptor.67
- _block_descriptor.82
- _block_descriptor.85
- _block_descriptor.91
- _block_destroy_helper.63
- _block_destroy_helper.66
- _block_destroy_helper.81
- _block_destroy_helper.84
- _block_destroy_helper.90
- _objc_msgSend$_installProfileData:store:declarationKey:completionHandler:
- _objectdestroy.4Tm
- _swift_retain
- _swift_stdlib_isStackAllocationSafe
CStrings:
+ "DeviceConfiguration"
+ "Invalid declaration: %{public}@ error: %{public}@"
+ "baseStore"
+ "subscriberStore"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<RMConfigurationCombineAdapter>\""
- "@\"<RMConfigurationMultipleAdapter>\""
- "@\"<RMConfigurationSingleAdapter>\""
- "@\"NSArray\""
- "@\"NSConditionLock\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"24@0:8^@16"
- "@\"NSDictionary\"32@0:8@\"NSArray\"16^@24"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"RMConfigurationSubscriberDelegate\""
- "@\"RMConfigurationUIDetails\""
- "@\"RMModelDeclarationBase\""
- "@\"RMObserverStore\""
- "@\"RMProviderStore\""
- "@\"RMSharedLock\""
- "@\"RMStatusPublisherDelegate\""
- "@\"RMStoreDeclarationKey\""
- "@\"RMStoreProfilesAdapter\""
- "@\"RMStoreXPCConnection\""
- "@\"RMSubscriberStore\""
- "@\"WrappedCombineAdapter\""
- "@\"WrappedMultipleAdapter\""
- "@\"WrappedSingleAdapter\""
- "@16@0:8"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@\"NSString\"16^@24"
- "@32@0:8@16#24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8q16@24#32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16@24@32@40@48"
- "@60@0:8@16q24@32@40@48B56"
- "@88@0:8@16q24q32@40@48@56@64B72B76@80"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"RMModelDeclarationBase\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B40@0:8@16@\"NSString\"24^@32"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24@32@40"
- "B56@0:8@16@24@32^B40^@48"
- "B64@0:8@16@24@32@40^B48^@56"
- "DMCEnrollmentFlowRMBridge"
- "DMCHexString"
- "DMCSHA256Hash"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "RMAssetResolverControllerProtocol"
- "RMAssetResolverProtocol"
- "RMBaseStore"
- "RMCertificateStatusItem"
- "RMConfigurationCombineApplicator"
- "RMConfigurationMultipleApplicator"
- "RMConfigurationSingleApplicator"
- "RMConfigurationSubscriberClient"
- "RMConfigurationSubscriberDelegate"
- "RMConfigurationSubscriberDescription"
- "RMConfigurationSubscriberEventStream"
- "RMConfigurationSubscriberService"
- "RMConfigurationSubscriberXPCListenerDelegate"
- "RMConfigurationSubscriberXPCService"
- "RMConfigurationUIDetails"
- "RMConfigurationUIItem"
- "RMDeclarationManifest"
- "RMDeclarationManifestItem"
- "RMErSSOStore"
- "RMMutableStoreProtocol"
- "RMObserverStore"
- "RMProviderStore"
- "RMStatusPublisherDelegate"
- "RMStatusPublisherDescription"
- "RMStoreAssetKey"
- "RMStoreDeclarationKey"
- "RMStoreDeclarationKeyPair"
- "RMStoreKeychainController"
- "RMStoreLocalizable"
- "RMStoreProfilesAdapter"
- "RMStoreProfilesController"
- "RMStoreProtocol"
- "RMStoreResolvedAsset"
- "RMStoreUnresolvedAsset"
- "RMStoreUnresolvedKeychainAsset"
- "RMStoreUtility"
- "RMStoreXPCConnection"
- "RMStoreXPCProxy"
- "RMStoreXPCService"
- "RMSubscribedConfigurationReference"
- "RMSubscriberStore"
- "RemoteManagementStore"
- "T#,R"
- "T#,R,C,N,V_publisherClass"
- "T#,R,N,V_publisherClass"
- "T@\"<RMConfigurationCombineAdapter>\",R,N,V_adapter"
- "T@\"<RMConfigurationCombineAdapter>\",R,N,V_wrappedAdapter"
- "T@\"<RMConfigurationMultipleAdapter>\",R,N,V_adapter"
- "T@\"<RMConfigurationMultipleAdapter>\",R,N,V_wrappedAdapter"
- "T@\"<RMConfigurationSingleAdapter>\",R,N,V_adapter"
- "T@\"<RMConfigurationSingleAdapter>\",R,N,V_wrappedAdapter"
- "T@\"NSArray\",R,C,N,V_activations"
- "T@\"NSArray\",R,C,N,V_applicatorClasses"
- "T@\"NSArray\",R,C,N,V_assets"
- "T@\"NSArray\",R,C,N,V_configurations"
- "T@\"NSArray\",R,C,N,V_declarationAssets"
- "T@\"NSArray\",R,C,N,V_management"
- "T@\"NSArray\",R,C,N,V_scopes"
- "T@\"NSArray\",R,C,N,V_types"
- "T@\"NSArray\",R,N,V_assets"
- "T@\"NSArray\",R,N,V_configurationTypes"
- "T@\"NSArray\",R,N,V_detailsUI"
- "T@\"NSArray\",R,N,V_statusKeys"
- "T@\"NSData\",R,C,N,V_assetData"
- "T@\"NSData\",R,C,N,V_assetKeychainReference"
- "T@\"NSData\",R,N,V_persistentRef"
- "T@\"NSDictionary\",R,C,N,V_applicatorClassNameByConfigurationType"
- "T@\"NSDictionary\",R,C,N,V_queryParameters"
- "T@\"NSDictionary\",R,C,N,V_statusKeysByXPCEvent"
- "T@\"NSDictionary\",R,N,V_hiddenDetails"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_applicatorQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_publisherQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
- "T@\"NSObject<OS_os_log>\",R"
- "T@\"NSSet\",R,C,N,V_statusKeys"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_accountIdentifier"
- "T@\"NSString\",C,N,V_extensionToken"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_ownerIdentifier"
- "T@\"NSString\",C,N,V_personaIdentifier"
- "T@\"NSString\",C,N,V_profileIdentifierPrefix"
- "T@\"NSString\",C,N,V_storeDescription"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_assetIdentifier"
- "T@\"NSString\",R,C,N,V_assetKeychainUserName"
- "T@\"NSString\",R,C,N,V_assetServerToken"
- "T@\"NSString\",R,C,N,V_declarationIdentifier"
- "T@\"NSString\",R,C,N,V_declarationServerToken"
- "T@\"NSString\",R,C,N,V_descriptionUI"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_key"
- "T@\"NSString\",R,C,N,V_keyWithoutServerToken"
- "T@\"NSString\",R,C,N,V_keychainDefaultAccessibility"
- "T@\"NSString\",R,C,N,V_keychainGroup"
- "T@\"NSString\",R,C,N,V_storeIdentifier"
- "T@\"NSString\",R,C,N,V_subscriberIdentifier"
- "T@\"NSString\",R,C,N,V_titleUI"
- "T@\"NSString\",R,C,N,V_version"
- "T@\"NSString\",R,N,V_declarationIdentifier"
- "T@\"NSString\",R,N,V_declarationServerToken"
- "T@\"NSString\",R,N,V_declarationType"
- "T@\"NSURL\",C,N,V_enrollmentURL"
- "T@\"NSURL\",R,C,N"
- "T@\"NSURL\",R,C,N,V_assetFile"
- "T@\"NSURL\",R,C,N,V_downloadURL"
- "T@\"NSXPCConnection\",R,V_connection"
- "T@\"RMConfigurationSubscriberDelegate\",&,N,V_subscriberDelegate"
- "T@\"RMConfigurationUIDetails\",R,N,V_declarationDetails"
- "T@\"RMModelDeclarationBase\",R,N,V_declaration"
- "T@\"RMModelDeclarationBase\",R,N,V_dynamicDeclaration"
- "T@\"RMObserverStore\",&,N,V_observerStore"
- "T@\"RMProviderStore\",&,N,V_providerStore"
- "T@\"RMStatusPublisherDelegate\",&,N,V_publisherDelegate"
- "T@\"RMStoreDeclarationKey\",R,C,N,V_applyKey"
- "T@\"RMStoreDeclarationKey\",R,C,N,V_assetKey"
- "T@\"RMStoreDeclarationKey\",R,C,N,V_configurationKey"
- "T@\"RMStoreDeclarationKey\",R,C,N,V_replaceKey"
- "T@\"RMStoreProfilesAdapter\",&,N,V_profilesAdapter"
- "T@\"RMStoreXPCConnection\",&,N,V_xpcConnection"
- "T@\"RMSubscriberStore\",R,N,V_store"
- "T@\"WrappedCombineAdapter\",R,N,V_wrappingAdapter"
- "T@\"WrappedMultipleAdapter\",R,N,V_wrappingAdapter"
- "T@\"WrappedSingleAdapter\",R,N,V_wrappingAdapter"
- "T@,&,N,V_eventStreamObserver"
- "TB,N,V_dataSeparated"
- "TB,N,V_defaultToInteractive"
- "TB,N,V_doKeychainUnassign"
- "TB,N,V_inPlaceUpdates"
- "TB,N,V_isSystemScope"
- "TB,N,V_removeBeforeApply"
- "TB,N,V_retryOnce"
- "TB,N,V_retrying"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_hasServiceEntitlement"
- "TB,R,N,V_isIdentity"
- "TB,R,N,V_useCache"
- "TB,R,N,V_useSystemKeychain"
- "TQ,N,V_installFail"
- "TQ,N,V_installSuccess"
- "TQ,N,V_removeFail"
- "TQ,N,V_removeSuccess"
- "TQ,R"
- "Tq,N,V_scope"
- "Tq,N,V_type"
- "Tq,R,N"
- "Tq,R,N,V_resolveAs"
- "Tq,R,N,V_scope"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "WrappedCombineAdapter"
- "WrappedMultipleAdapter"
- "WrappedSingleAdapter"
- "^{_NSZone=}16@0:8"
- "_accountIdentifier"
- "_activations"
- "_adapter"
- "_allowedErSSOPayloadTypes"
- "_allowedPayloadType:store:"
- "_applicatorClassNameByConfigurationType"
- "_applicatorClasses"
- "_applicatorQueue"
- "_applyDeclarationsForPayload:declarations:completionHandler:"
- "_applyKey"
- "_applyLock"
- "_assetData"
- "_assetFile"
- "_assetIdentifier"
- "_assetKey"
- "_assetKeychainReference"
- "_assetKeychainUserName"
- "_assetServerToken"
- "_assets"
- "_beginProcessingWithConfigurations:storesByIdentifier:scope:completionHandler:"
- "_buildSubscribedReferences:declarations:store:"
- "_bundle"
- "_canAssumeOwnershipOfProfile:newProfile:newDeclarationKey:store:"
- "_canInstallProfile:store:declarationKey:outAssumeOwnership:error:"
- "_canReplaceProfile:newProfile:newDeclarationKey:store:outAssumeOwnership:error:"
- "_canUninstallProfileWithIdentifier:store:error:"
- "_cleanupDeclarationKeyIfNeeded:scope:doIt:completionHandler:"
- "_cleanupDeclarationKeysIfNeeded:scope:doIt:completionHandler:"
- "_configurationByDeclarationKeyFromConfigurations:"
- "_configurationKey"
- "_configurationTypes"
- "_configurations"
- "_configurationsByApplicatorClassNameForConfigurationsByType:"
- "_configuredConfigurationTypesWithScope:"
- "_connection"
- "_createStoreReturningError:"
- "_currentLocaleDidChange:"
- "_dataSeparated"
- "_declaration"
- "_declarationAssets"
- "_declarationDetails"
- "_declarationIdentifier"
- "_declarationKeyForProfile:"
- "_declarationKeyForUserInfo:"
- "_declarationServerToken"
- "_declarationType"
- "_defaultToInteractive"
- "_descriptionUI"
- "_detailsUI"
- "_disallowedPayloadTypes"
- "_doKeychainUnassign"
- "_downloadURL"
- "_dynamicDeclaration"
- "_endProcessingWithSuccess:configurations:storesByIdentifier:scope:completionHandler:"
- "_endProcessingWithSuccess:scope:completionHandler:"
- "_enrollmentURL"
- "_eventDescriptorByNameForEventStreamNamed:"
- "_eventStreamObserver"
- "_extensionToken"
- "_fetchAssetDeclarationWithAssetIdentifier:configurationIdentifier:subscriberStore:scope:completionHandler:"
- "_fetchConfigurations:"
- "_fetchExistingDeclarationKeyWithConfigurations:storesByIdentifier:scope:completionHandler:"
- "_fetchExistingDeclarationKeysWithConfigurations:storesByIdentifier:scope:completionHandler:"
- "_fetchLock"
- "_fetchSubscriberStoreIfNeededWithSubscriberStore:configurationIdentifier:scope:completionHandler:"
- "_filterSupportedStatus:store:unsupported:"
- "_findObserverStoreWithCompletionHandler:"
- "_findProviderStoreWithCompletionHandler:"
- "_handleEvent:"
- "_hasServiceEntitlement"
- "_hiddenDetails"
- "_identifier"
- "_inPlaceUpdates"
- "_installDeclarationKey:scope:configurations:completionHandler:"
- "_installDeclarationKeys:scope:configurations:completionHandler:"
- "_installDeclarationKeysWithScope:configurations:completionHandler:"
- "_installFail"
- "_installOptionsForStore:declarationKey:assumeOwnership:"
- "_installProfileAtPath:store:declaration:completionHandler:"
- "_installProfileData:options:error:"
- "_installProfileData:store:declarationKey:completionHandler:"
- "_installSuccess"
- "_invalidDeclarationKeys:scope:configurations:completionHandler:"
- "_isIdentity"
- "_isManagedByMDM:"
- "_isSystemScope"
- "_key"
- "_keyWithoutServerToken"
- "_keychainDefaultAccessibility"
- "_keychainGroup"
- "_loadDescription:"
- "_loadDescriptionFromStatusEvents:statusKeysByNotification:statusKeysWithoutNotification:"
- "_loadDynamicSchema"
- "_loadManagedSettingsDescription"
- "_management"
- "_metadataKeyForPayload:"
- "_name"
- "_newDeclarationsMap:error:"
- "_observerStore"
- "_oldDeclarationKeysForPayload:store:error:"
- "_ownerIdentifier"
- "_parseDeclarationKey:completionHandler:"
- "_passcodeSettingsForUserEnrollmentWithDeclaration:"
- "_payloadStructure:"
- "_persistentRef"
- "_personaIDForStore:"
- "_personaIdentifier"
- "_processExistingDeclarationKeyWithConfigurations:oldDeclarationKey:storesByIdentifier:scope:completionHandler:"
- "_processExistingDeclarationKeysWithConfigurations:oldDeclarationKeys:storesByIdentifier:scope:completionHandler:"
- "_profileForIdentifier:rmOnly:"
- "_profileIdentifierPrefix"
- "_profilesAdapter"
- "_providerStore"
- "_publisherClass"
- "_publisherDelegate"
- "_publisherQueue"
- "_queryParameters"
- "_reasonsFromErrorWithFirstReason:error:"
- "_registerApplicatorModelClasses:"
- "_registerForLocaleChange"
- "_registerPublisherModelClasses:"
- "_removeBeforeApply"
- "_removeDeclarationKeysForPayload:error:"
- "_removeDeclarationsForPayload:completionHandler:"
- "_removeFail"
- "_removeProfileWithIdentifier:error:"
- "_removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:"
- "_removeSuccess"
- "_replaceKey"
- "_resolveAs"
- "_resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:"
- "_resolveDynamicDeclaration:"
- "_resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:"
- "_resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:"
- "_resolveKeychainAssets:assetIdentifiers:accessGroup:persistentRefs:completionHandler:"
- "_resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:persistentRefs:completionHandler:"
- "_retryOnce"
- "_retrying"
- "_saveDeclarationKeysForPayload:keys:error:"
- "_scope"
- "_scopes"
- "_sendConfigurationUIForConfigurationReference:visible:configurationUI:configurationUIGroup:"
- "_sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:"
- "_sendStatusForSuccessKeys:failedKeys:reasons:applyError:scope:configurations:success:completionHandler:"
- "_sendStatusForSuccessKeys:reasons:scope:configurations:completionHandler:"
- "_setupEventHandler"
- "_setupEventHandlerWithScope:"
- "_statusKeys"
- "_statusKeysByXPCEvent"
- "_store"
- "_storeDescription"
- "_storeIdentifier"
- "_subscriberDelegate"
- "_subscriberIdentifier"
- "_supportedConfigurationType:"
- "_titleUI"
- "_type"
- "_types"
- "_uninstallDeclarationKey:scope:completionHandler:"
- "_uninstallDeclarationKeys:scope:completionHandler:"
- "_useCache"
- "_useSystemKeychain"
- "_usesKeychain"
- "_validateStatusEvents:"
- "_validateStatusKeysByNotification:"
- "_validateStatusKeysWithoutNotification:"
- "_version"
- "_workQueue"
- "_wrappedAdapter"
- "_wrappingAdapter"
- "_writeStatusForDeclaration:validity:reasons:completionHandler:"
- "_xpcConnection"
- "adapter"
- "addEntriesFromDictionary:"
- "addExtensionToken:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "allDeclarationKeys"
- "allDeclarationKeysForScope:completionHandler:"
- "allDeclarationKeysForScope:error:"
- "allKeys"
- "allObjects"
- "allPrefixedProfileIdentifiers"
- "allProfileIdentifiers"
- "allValues"
- "anyObject"
- "appDetailsFromDeclarations:error:"
- "applicatorClassNameByConfigurationType"
- "applicatorClasses"
- "applicatorQueue"
- "applyChangesForStoreIdentifier:completionHandler:"
- "applyChangesWithCompletionHandler:"
- "applyCombinedConfiguration:declarationKeys:scope:completionHandler:"
- "applyCombinedConfiguration:declarationKeys:scope:returningReasons:error:"
- "applyConfiguration:replaceKey:scope:completionHandler:"
- "applyConfiguration:scope:returningReasons:error:"
- "applyConfigurations:storesByIdentifier:scope:completionHandler:"
- "applyKey"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetCannotBeDeserialized:error:completionHandler:"
- "assetCannotBeDownloaded:error:completionHandler:"
- "assetCannotBeVerified:error:completionHandler:"
- "assetData"
- "assetDifferencesOnlyForOldKey:newKey:"
- "assetEncounteredInternalError:error:completionHandler:"
- "assetFile"
- "assetIdentifier"
- "assetKey"
- "assetKeychainReference"
- "assetKeychainUserName"
- "assetReferences"
- "assetServerToken"
- "assetSuccessfullyResolved:completionHandler:"
- "assetWithIdentifier:"
- "attributesOfItemAtPath:error:"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "beginProcessingConfigurationsForScope:completionHandler:"
- "beginProcessingConfigurationsForScope:error:"
- "boolValue"
- "buildWithCode:description:details:"
- "buildWithIdentifier:requirePasscode:requireAlphanumericPasscode:requireComplexPasscode:minimumLength:minimumComplexCharacters:maximumFailedAttempts:failedAttemptsResetInMinutes:maximumGracePeriodInMinutes:maximumInactivityInMinutes:maximumPasscodeAgeInDays:passcodeReuseLimit:changeAtNextAuth:customRegex:"
- "bundleIdentifier"
- "caseInsensitiveCompare:"
- "certificatePersistentRefForAssetKey:completionHandler:"
- "certificatePersistentRefForAssetKey:storeIdentifier:completionHandler:"
- "certificateStatusItemWithPersistentRef:isIdentity:"
- "certificateStatusWithCompletionHandler:"
- "certificateStatusWithStoreIdentifier:completionHandler:"
- "class"
- "combineConfigurations:"
- "compare:"
- "complete"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configurationByDeclarationKeyForConfigurations:"
- "configurationCannotBeDeserialized:error:completionHandler:"
- "configurationClass"
- "configurationClasses"
- "configurationErrorReasons:reasons:completionHandler:"
- "configurationFailedAlreadyPresent:completionHandler:"
- "configurationFailedToApply:error:completionHandler:"
- "configurationIsInvalid:error:completionHandler:"
- "configurationKey"
- "configurationNotSupported:error:completionHandler:"
- "configurationRemovedWithDeclarationIdentifier:declarationServerToken:completionHandler:"
- "configurationSchemaDirectoryForXPCServiceResourceURL:"
- "configurationSuccessfullyApplied:completionHandler:"
- "configurationSuccessfullyApplied:reasons:completionHandler:"
- "configurationTypes"
- "configurationUIForConfiguration:scope:completionHandler:"
- "configurationUIItemWithConfiguration:details:"
- "configurationUIItemWithIdentifier:serverToken:type:details:"
- "configurationUIWithTitle:description:details:"
- "configurationUIWithTitle:description:details:hiddenDetails:"
- "configurationUIsForStoreIdentifier:completionHandler:"
- "configureSandbox"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAssetTypeInvalidError:"
- "createDisallowedStatusValueErrorWithKeyPath:"
- "createErSSOStoreWithDeclarations:chosenBundleID:personaID:isUserEnrollment:completionHandler:"
- "createInternalError"
- "createInternalErrorWithDescription:"
- "createManagementSourceNotFoundErrorWithIdentifier:"
- "createProfileCannotFindRemoveProfile:"
- "createProfileCannotRemoveOtherProfile:"
- "createProfileCannotReplaceOtherProfile:"
- "createProfileInvalidErrorWithUnderlyingError:"
- "createProfilePayloadNotAllowedErrorWithPayloadType:"
- "createStoreWithType:defaultToInteractive:dataSeparated:options:completionHandler:"
- "createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:"
- "createUnsupportedStatusValueErrorWithKeyPath:"
- "currentEnrollmentTypeForStoreType:"
- "currentManagedDevice"
- "currentPlatform"
- "currentScopeForStoreScope:"
- "dataUsingEncoding:"
- "dataWithContentsOfFile:options:error:"
- "dealloc"
- "debugDescription"
- "declarationAssets"
- "declarationClassType"
- "declarationDetails"
- "declarationIdentifier"
- "declarationIdentifiersForProfilePayloadIdentifiers:completionHandler:"
- "declarationKeyForConfiguration:"
- "declarationKeyForStore:declaration:"
- "declarationManifestForStoreIdentifier:completionHandler:"
- "declarationManifestWithCompletionHandler:"
- "declarationManifestWithDeclarations:"
- "declarationServerToken"
- "declarationType"
- "declarationWithIdentifier:completionHandler:"
- "declarationWithIdentifier:storeIdentifier:completionHandler:"
- "declarationsForStoreIdentifier:completionHandler:"
- "declarationsWithCompletionHandler:"
- "declarationsWithTypes:completionHandler:"
- "declarationsWithTypes:storeIdentifier:completionHandler:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultManager"
- "deleteDeclarationWithIdentifier:completionHandler:"
- "deleteDeclarationWithIdentifier:storeIdentifier:completionHandler:"
- "descriptionUI"
- "descriptionWithEventsDictionary:"
- "descriptionWithServiceDictionary:"
- "detailsUI"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didFailToFetchConfigurationsWithTypes:scope:error:"
- "didFetchConfigurationsByType:storesByIdentifier:scope:completionHandler:"
- "didFetchConfigurationsWithVisibleUIByType:storesByIdentifier:scope:completionHandler:"
- "displayPropertiesForConfigurationsWithCompletionHandler:"
- "displayableProfileConfigurationsForStoreIdentifier:completionHandler:"
- "displayableProfileConfigurationsWithCompletionHandler:"
- "doKeychainUnassign"
- "downloadAndInstallProfileConfiguration:fromURL:completionHandler:"
- "downloadAndInstallProfileDeclaration:store:fromURL:completionHandler:"
- "downloadURL"
- "dynamicDeclaration"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endProcessingConfigurations:scope:completionHandler:"
- "endProcessingConfigurations:scope:error:"
- "ensureClassForDeclarations:"
- "ensureClassForStatusItems:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "eventStreamObserver"
- "extensibleSSOProfileIdentifiersWithCompletionHandler:"
- "extensionToken"
- "extractUserIdentityAsset:assetIdentifier:completionHandler:"
- "fetchConfigurationUIsWithTypes:scope:completionHandler:"
- "fetchConfigurationsWithTypes:scope:completionHandler:"
- "fetchDataAtURL:completionHandler:"
- "fetchDataAtURL:storeIdentifier:completionHandler:"
- "fetchStatusForStatusKeys:store:completionHandler:"
- "fetchThenApplyConfigurationsWithScope:completionHandler:"
- "fetchThenUpdateConfigurationUIsWithScope:completionHandler:"
- "fileExistsAtPath:"
- "filterForUserEnrollmentWithDeclaration:"
- "filteredArrayUsingPredicate:"
- "filteredSetUsingPredicate:"
- "firstObject"
- "friendlyName"
- "hasPrefix:"
- "hasServiceEntitlement"
- "hash"
- "i32@0:8@16#24"
- "i36@0:8@16#24B32"
- "inPlaceUpdates"
- "infoDictionary"
- "init"
- "initWithActivations:configurations:assets:management:"
- "initWithAdapter:"
- "initWithAdapter:inPlaceUpdates:"
- "initWithApplicators:"
- "initWithApplicators:publisherClass:"
- "initWithAsset:"
- "initWithAsset:assetKey:configurationKey:group:defaultAccessibility:"
- "initWithAsset:queryParameters:"
- "initWithAsset:queryParameters:downloadURL:"
- "initWithAsset:queryParameters:downloadURL:useCache:"
- "initWithAsset:queryParameters:useCache:"
- "initWithAssetIdentifier:assetServerToken:"
- "initWithAssetIdentifier:queryParameters:downloadURL:useCache:"
- "initWithAssetIdentifier:queryParameters:useCache:"
- "initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:useCache:"
- "initWithAssetKey:"
- "initWithBase64EncodedString:options:"
- "initWithCoder:"
- "initWithCondition:"
- "initWithConfiguration:details:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDeclaration:subscriberStore:assets:"
- "initWithDeclarationKey:"
- "initWithDictionary:"
- "initWithFile:"
- "initWithIdentifier:serverToken:type:details:"
- "initWithIdentifier:type:scope:name:description:enrollmentURL:accountIdentifier:defaultToInteractive:dataSeparated:personaIdentifier:"
- "initWithIdentifier:version:"
- "initWithKeychainReference:"
- "initWithKeychainReference:userName:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:options:"
- "initWithNewKey:replaceKey:"
- "initWithOwner:scope:"
- "initWithProfileIdentifierPrefix:"
- "initWithProfileIdentifierPrefix:scope:"
- "initWithProfilesAdapter:profileIdentifierPrefix:"
- "initWithPublisherClass:"
- "initWithScope:"
- "initWithSubscriberIdentifier:store:declaration:assets:"
- "initWithSubscriberIdentifier:storeIdentifier:declarationIdentifier:declarationServerToken:assetKeys:"
- "initWithSubscriberIdentifier:storeIdentifier:declarationIdentifier:declarationServerToken:assets:"
- "initWithTitle:description:details:hiddenDetails:"
- "initWithTypes:scopes:"
- "initWithWithPersistentRef:isIdentity:"
- "initWithXPCConnection:"
- "installFail"
- "installOptions"
- "installProfile:declarations:completionHandler:"
- "installProfileData:options:outError:"
- "installProfileData:store:declarationKey:completionHandler:"
- "installSuccess"
- "installedDeclarationKey"
- "installedDeclarationKeyForScope:error:"
- "installedProfileIdentifierByDeclarationKey"
- "installedProfileIdentifiers"
- "installedProfileIdentifiersWithFilterFlags:"
- "installedSystemProfileWithIdentifier:"
- "installedUserProfileWithIdentifier:"
- "integerValue"
- "interfaceWithProtocol:"
- "intersectSet:"
- "invalidate"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToCertificateStatus:"
- "isEqualToConfigurationUI:"
- "isEqualToData:"
- "isEqualToManifest:"
- "isEqualToManifestItem:"
- "isEqualToReference:"
- "isEqualToResolvedAsset:"
- "isEqualToSet:"
- "isEqualToStore:"
- "isEqualToString:"
- "isEqualToUnresolvedAsset:"
- "isEqualToUnresolvedKeychainAsset:"
- "isIdentity"
- "isKindOfClass:"
- "isManagedByMDM"
- "isManagedStore"
- "isMemberOfClass:"
- "isPreEnrollmentErSSOStore:"
- "isProxy"
- "isSharediPad"
- "isSupervised"
- "isSupportedForPlatform:scope:enrollmentType:"
- "isSystemScope"
- "isValid"
- "isValidDeclaration:"
- "isValidStatusItem:"
- "isValidURL:"
- "key"
- "keyByReplacingSubscriberIdentifier:"
- "keyEnumerator"
- "keyWithoutServerToken"
- "keychainDefaultAccessibility"
- "keychainGroup"
- "length"
- "linkErSSOStoreToMDMWithProfileIdentifier:accountIdentifier:completionHandler:"
- "linkStoreIdentifier:profileIdentifier:accountIdentifier:completionHandler:"
- "linkStoreToProfileIdentifier:accountIdentifier:completionHandler:"
- "listener:shouldAcceptNewConnection:"
- "load:serializationType:error:"
- "loadData:serializationType:error:"
- "loadDynamicSchemaFromDirectory:"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "lock"
- "lockWhenCondition:"
- "longLongValue"
- "lowercaseString"
- "mainBundle"
- "managedSetting"
- "managedSettingKey"
- "managedSettingsSchemas"
- "metadataForStoreIdentifier:completionHandler:"
- "metadataReturningError:"
- "metadataValueForKey:error:"
- "metadataValueForKey:storeIdentifier:completionHandler:"
- "minusSet:"
- "mutableCopy"
- "newAgentConnection"
- "newAssetKey:"
- "newAssetKeyWithAsset:"
- "newAssetKeyWithAssetIdentifier:assetServerToken:"
- "newConfigurationSubscriberEventStreamWithScope:applicators:publisherClass:"
- "newConfigurationSubscriberServiceWithXPCConnection:"
- "newConnectionWithListenerEndpoint:"
- "newConnectionWithScope:"
- "newDaemonConnection"
- "newDeclarationKey:"
- "newDeclarationKeyPairWithNewKey:"
- "newDeclarationKeyPairWithUpdateKey:replaceKey:"
- "newDeclarationKeyWithSubscriberIdentifier:reference:"
- "newDeclarationKeyWithSubscriberIdentifier:store:declaration:"
- "newDeclarationKeyWithSubscriberIdentifier:storeIdentifier:declarationIdentifier:declarationServerToken:"
- "newDeclarationKeyWithSubscriberIdentifier:storeIdentifier:declarationIdentifier:declarationServerToken:assetKeys:"
- "newDeclarationKeyWithoutAssets:"
- "newInterface"
- "newProfileControllerWithPrefix:scope:"
- "newSharedLockWithDescription:"
- "newXPCEventForDarwinNotification:"
- "newXPCEventForStream:notificationName:descriptor:"
- "nextObject"
- "numberWithBool:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKeyedSubscript:"
- "observerStoreWithCompletionHandler:"
- "observerStoreWithIdentifier:completionHandler:"
- "observerStoresWithCompletionHandler:"
- "ownerIdentifier"
- "path"
- "payloadAppStoreID"
- "payloadBundleID"
- "payloadManifestURL"
- "payloadMaximumInactivityInMinutes"
- "payloadStandardConfigurations"
- "payloads"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "permissiveURLSchemes"
- "persistentRef"
- "postNotificationName:object:userInfo:"
- "predicateWithBlock:"
- "profileIdentifierForConfiguration:"
- "profileIdentifierForDeclaration:store:"
- "profileIdentifierPrefix"
- "profileNameForIdentifier:"
- "profileNameForProfileIdentifier:"
- "profileStoreForOwner:"
- "profileStoreForOwner:scope:"
- "profileWithData:outError:"
- "providerStoreWithCompletionHandler:"
- "providerStoreWithIdentifier:completionHandler:"
- "providerStoresWithCompletionHandler:"
- "publishStatus:completionHandler:"
- "publishStatusKeys:storeIdentifier:scope:completionHandler:"
- "publishStatusWithStoreIdentifier:status:completionHandler:"
- "publisherClass"
- "publisherDelegate"
- "publisherQueue"
- "q16@0:8"
- "q24@0:8q16"
- "queryForStatusWithKeyPaths:store:completionHandler:"
- "queryParameters"
- "rangeOfString:"
- "reasonWithCode:description:underlyingError:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeBeforeApply"
- "removeCombinedConfigurationForScope:completionHandler:"
- "removeCombinedConfigurationForScope:error:"
- "removeDeclarationKey:scope:completionHandler:"
- "removeDeclarationKey:scope:error:"
- "removeErSSOStoreWithCompletionHandler:"
- "removeFail"
- "removeObject:"
- "removeObserver:"
- "removeProfile:completionHandler:"
- "removeProfileWithIdentifier:installationType:"
- "removeStatusWithStoreIdentifier:declarationIdentifier:declarationServerToken:sourceIdentifier:completionHandler:"
- "removeStoreWithIdentifier:completionHandler:"
- "removeStoreWithIdentifier:scope:completionHandler:"
- "removeSuccess"
- "removeTrustForCertificateRef:configurationKey:fullTrust:completionHandler:"
- "removeTrustForCertificateRef:configurationKey:fullTrust:scope:completionHandler:"
- "replaceKey"
- "resolveAs"
- "resolveAsset:completionHandler:"
- "resolveAsset:storeIdentifier:completionHandler:"
- "resolveDataAsset:assetIdentifier:downloadURL:completionHandler:"
- "resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:"
- "resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:"
- "resolveKeychainAsset:assetIdentifier:completionHandler:"
- "resolveKeychainAsset:assetIdentifier:subscriberIdentifier:completionHandler:"
- "resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
- "resolveKeychainAssets:assetIdentifiers:accessGroup:completionHandler:"
- "resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
- "resolveKeychainPasswordAsset:assetIdentifier:accessGroup:completionHandler:"
- "resolveUserNameAndPasswordAsset:assetIdentifier:completionHandler:"
- "resourceURL"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retryOnce"
- "retrying"
- "rms_stringWithScope:"
- "runConfigurationSubscriberClientWithApplicators:publisherClass:"
- "runConfigurationSubscriberClientWithApplicators:publisherClass:initializeSandbox:"
- "saveDeclaration:completionHandler:"
- "saveDeclaration:storeIdentifier:completionHandler:"
- "scheme"
- "scopes"
- "self"
- "sendStatusKeys:storeIdentifier:scope:completionHandler:"
- "serializeWithType:"
- "serviceListener"
- "setAccountIdentifier:"
- "setApplicatorQueue:"
- "setByAddingObjectsFromArray:"
- "setByAddingObjectsFromSet:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConfigurationUI:visible:ui:completionHandler:"
- "setConfigurationUIWithStoreIdentifier:declarationIdentifier:declarationServerToken:visible:ui:completionHandler:"
- "setDataSeparated:"
- "setDefaultToInteractive:"
- "setDelegate:"
- "setDoKeychainUnassign:"
- "setEnrollmentURL:"
- "setEventStreamObserver:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtensionToken:"
- "setIdentifier:"
- "setInPlaceUpdates:"
- "setInstallFail:"
- "setInstallSuccess:"
- "setIsSystemScope:"
- "setMetadataValue:forKey:error:"
- "setMetadataValue:forKey:storeIdentifier:completionHandler:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObserverStore:"
- "setOwnerIdentifier:"
- "setPayloadStandardConfigurations:"
- "setPersonaIdentifier:"
- "setProfileIdentifierPrefix:"
- "setProfilesAdapter:"
- "setProviderStore:"
- "setPublisherDelegate:"
- "setPublisherQueue:"
- "setRemoteObjectInterface:"
- "setRemoveBeforeApply:"
- "setRemoveFail:"
- "setRemoveSuccess:"
- "setRetryOnce:"
- "setRetrying:"
- "setScope:"
- "setShouldInstallConfiguration:shouldInstall:completionHandler:"
- "setShouldInstallConfiguration:shouldInstall:storeIdentifier:completionHandler:"
- "setStoreDescription:"
- "setSubscriberDelegate:"
- "setTrustForCertificateRef:configurationKey:fullTrust:completionHandler:"
- "setTrustForCertificateRef:configurationKey:fullTrust:scope:completionHandler:"
- "setType:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setWorkQueue:"
- "setXpcConnection:"
- "sharedConnection"
- "sharedDelegateWithApplicators:"
- "sharedDelegateWithPublisherClass:"
- "sortedArrayUsingSelector:"
- "start"
- "statusKeys"
- "statusKeysByXPCEvent"
- "statusSchemaDirectoryForXPCServiceResourceURL:"
- "storeDescription"
- "storeForStoreDeclarationKeyString:scope:completionHandler:"
- "storeIdentifier"
- "storeWithIdentifier:scope:completionHandler:"
- "storeXPCConnection:"
- "storesWithCompletionHandler:"
- "storesWithScope:completionHandler:"
- "string:"
- "stringWithFormat:"
- "stubObjectForStatusItemType:"
- "subscribedDeclarationsWithTypes:storeIdentifier:completionHandler:"
- "subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:"
- "subscribedStoreConfigurationsVisibleUIWithTypes:completionHandler:"
- "subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:"
- "subscribedStoreDeclarationsWithTypes:completionHandler:"
- "subscriberDelegate"
- "subscriberIdentifier"
- "subscriberStoreWithIdentifier:completionHandler:"
- "subscriberStoresWithCompletionHandler:"
- "substringFromIndex:"
- "substringToIndex:"
- "superclass"
- "supportedConfigurationClasses"
- "supportedConfigurationClassesArray"
- "supportedConfigurationTypes"
- "supportedStatusClasses"
- "supportsSecureCoding"
- "synchronizeOldKeys:newKeys:returningUnchangedKeys:returningApplyKeys:returningRemoveKeys:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "titleUI"
- "tokenForURL:"
- "tryLockWhenCondition:"
- "types"
- "unassignAssets:completionHandler:"
- "unassignAssets:scope:completionHandler:"
- "uninstallProfileWithIdentifier:store:completionHandler:"
- "unionSet:"
- "unlock"
- "unlockWithCondition:"
- "useCache"
- "useSystemKeychain"
- "userInfo"
- "usesKeychainAssets"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"RMDeclarationManifest\"@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\"@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"RMDeclarationManifest\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"RMModelDeclarationBase\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"RMObserverStore\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"RMProviderStore\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"RMSubscriberStore\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"RMModelDeclarationBase\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"RMStoreDeclarationKey\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"RMStoreUnresolvedAsset\"16@?<v@?@\"RMStoreResolvedAsset\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8d16@?24"
- "v32@0:8d16@?<v@?@\"NSError\">24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSError\">24"
- "v36@0:8@\"RMModelDeclarationBase\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8B16q20@?28"
- "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSSet\"16d24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"RMModelDeclarationBase\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@\"RMModelDeclarationBase\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"RMStoreDeclarationKey\"16q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"RMStoreUnresolvedAsset\"16@\"NSString\"24@?<v@?@\"RMStoreResolvedAsset\"@\"NSError\">32"
- "v40@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@?<v@?@\"RMModelAssetUserIdentityDeclaration\"@\"NSError\">32"
- "v40@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@?<v@?@\"RMModelUserNameAndPasswordCredentialDeclaration\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16d24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24@?32"
- "v40@0:8q16@24@?32"
- "v44@0:8@\"NSData\"16@\"RMStoreDeclarationKey\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@\"RMModelDeclarationBase\"16B24@\"NSString\"28@?<v@?@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16B24@28@36"
- "v44@0:8@16B24@28@?36"
- "v44@0:8@16q24B32@?36"
- "v48@0:8@\"NSArray\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSSet\"16d24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSString\"@\"NSError\">40"
- "v48@0:8@\"RMSubscribedConfigurationReference\"16@\"NSString\"24@\"NSURL\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v48@0:8@16d24@32@?40"
- "v48@0:8@16q24@32@?40"
- "v48@0:8q16B24B28@\"NSDictionary\"32@?<v@?@\"RMProviderStore\"@\"NSError\">40"
- "v48@0:8q16B24B28@32@?40"
- "v52@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16@24B32q36@?44"
- "v52@0:8B16@20@28q36@?44"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32q40@?48"
- "v56@0:8@16@24^@32^@40^@48"
- "v56@0:8@16@24q32@40@?48"
- "v56@0:8q16q24B32B36@40@?48"
- "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@\"RMConfigurationUIDetails\"44@?<v@?@\"NSError\">52"
- "v60@0:8@16@24@32B40@44@?52"
- "v64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSArray\"@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSData\"@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@\"RMSubscriberStore\"40q48@?<v@?B@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24@32@40q48@?56"
- "v64@0:8@16@24@32q40@48@?56"
- "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48B56@\"NSArray\"60@?<v@?@\"NSError\">68"
- "v76@0:8@16@24@32@40@48B56@60@?68"
- "v76@0:8@16@24@32@40q48@56B64@?68"
- "valueForEntitlement:"
- "waitForActiveAndValidDeclarations:timeout:completionHandler:"
- "waitForActiveAndValidDeclarations:timeout:storeIdentifier:completionHandler:"
- "waitForActiveAndValidDeclarationsInErSSOStoreWithTimeout:completionHandler:"
- "waitForCompletion"
- "waitForProcessingOfDeclarations:timeout:completionHandler:"
- "waitForProcessingOfDeclarations:timeout:storeIdentifier:completionHandler:"
- "workQueue"
- "wrappedAdapter"
- "wrappingAdapter"
- "writeStatusWithStoreIdentifier:declarationType:declarationIdentifier:declarationServerToken:sourceIdentifier:validity:reasons:completionHandler:"
- "xpcConnection"
- "zone"

```
