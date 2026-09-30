## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/Versions/A/RemoteManagementStore`

```diff

-502.2.7.0.0
-  __TEXT.__text: 0x2f5d0
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x1bf0
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0xf3a
-  __TEXT.__oslogstring: 0x2d53
-  __TEXT.__gcc_except_tab: 0x3b8
-  __TEXT.__swift5_typeref: 0x57
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__constg_swiftt: 0x54
+560.4.11.0.0
+  __TEXT.__text: 0x418f0
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x22ec
+  __TEXT.__const: 0x33c
+  __TEXT.__cstring: 0x11e6
+  __TEXT.__oslogstring: 0x3337
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__swift5_typeref: 0x2b7
+  __TEXT.__swift5_fieldmd: 0xa8
+  __TEXT.__constg_swiftt: 0x9c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x134
+  __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xa38
-  __TEXT.__objc_classname: 0x673
-  __TEXT.__objc_methname: 0x6403
-  __TEXT.__objc_methtype: 0x135f
-  __TEXT.__objc_stubs: 0x3e40
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x198
-  __DATA_CONST.__objc_classlist: 0x138
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift5_capture: 0x108
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__unwind_info: 0xeb0
+  __TEXT.__eh_frame: 0xb70
+  __TEXT.__objc_classname: 0x68d
+  __TEXT.__objc_methname: 0x6cdd
+  __TEXT.__objc_methtype: 0x1663
+  __TEXT.__objc_stubs: 0x4100
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a8
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x1470
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x1070
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x3ce8
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xc30
-  __DATA.__objc_ivar: 0x188
-  __DATA.__data: 0x450
-  __DATA.__bss: 0x138
+  __DATA_CONST.__objc_arraydata: 0x50
+  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__const: 0x1620
+  __AUTH_CONST.__cfstring: 0x11e0
+  __AUTH_CONST.__objc_const: 0x34d8
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0xca0
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x190
+  __DATA.__data: 0x670
+  __DATA.__bss: 0x5d0
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
+  - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/Versions/A/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities
   - /System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement
   - /System/Library/PrivateFrameworks/RemoteManagementModel.framework/Versions/A/RemoteManagementModel

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib
   - /usr/lib/swift/libswift_stdio.dylib
   - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 592B2FCA-9582-36BD-B93D-D40EEDC4255A
-  Functions: 1037
-  Symbols:   2443
-  CStrings:  1556
+  UUID: 4214D218-73E3-30E8-8550-72F4F5523A5F
+  Functions: 1340
+  Symbols:   2682
+  CStrings:  1698
 
Symbols:
+ +[RMAssetResolverController _fetchAssetDeclarationWithAssetIdentifier:configurationIdentifier:subscriberStore:scope:completionHandler:]
+ +[RMAssetResolverController _fetchSubscriberStoreIfNeededWithSubscriberStore:configurationIdentifier:scope:completionHandler:]
+ +[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]
+ +[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:].cold.1
+ +[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]
+ +[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:].cold.1
+ +[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:].cold.2
+ +[RMAssetResolverController _resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:persistentRefs:completionHandler:]
+ +[RMAssetResolverController resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:]
+ +[RMAssetResolverController resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:].cold.1
+ +[RMAssetResolverController resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]
+ +[RMAssetResolverController resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:].cold.1
+ +[RMAssetResolverController resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]
+ +[RMAssetResolverController resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:].cold.1
+ +[RMConfigurationUIDetails configurationUIWithTitle:description:details:hiddenDetails:]
+ +[RMLog(assetResolverController) assetResolverController].cold.1
+ +[RMLog(configurationCombineApplicator) configurationCombineApplicator].cold.1
+ +[RMLog(configurationMultipleApplicator) configurationMultipleApplicator].cold.1
+ +[RMLog(configurationSingleApplicator) configurationSingleApplicator].cold.1
+ +[RMLog(configurationSubscriberClient) configurationSubscriberClient].cold.1
+ +[RMLog(configurationSubscriberDelegate) configurationSubscriberDelegate].cold.1
+ +[RMLog(configurationSubscriberEventStream) configurationSubscriberEventStream].cold.1
+ +[RMLog(configurationSubscriberService) configurationSubscriberService].cold.1
+ +[RMLog(profileStore) profileStore].cold.1
+ +[RMLog(profilesAdapter) profilesAdapter].cold.1
+ +[RMLog(profilesController) profilesController].cold.1
+ +[RMLog(statusPublisherDelegate) statusPublisherDelegate].cold.1
+ +[RMLog(statusPublisherDescription) statusPublisherDescription].cold.1
+ +[RMLog(storeKeychainController) storeKeychainController].cold.1
+ +[RMLog(subscribedConfigurationReference) subscribedConfigurationReference].cold.1
+ +[RMStoreLocalizable _bundle].cold.1
+ +[RMSubscriberStore storeForStoreDeclarationKeyString:scope:completionHandler:]
+ +[RMSubscriberStore storeForStoreDeclarationKeyString:scope:completionHandler:].cold.1
+ -[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]
+ -[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]
+ -[RMConfigurationCombineApplicator _sendStatusForSuccessKeys:failedKeys:reasons:applyError:scope:configurations:success:completionHandler:]
+ -[RMConfigurationUIDetails hiddenDetails]
+ -[RMConfigurationUIDetails initWithTitle:description:details:hiddenDetails:]
+ -[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]
+ -[RMStatusPublisherDescription _loadManagedSettingsDescription]
+ -[RMStoreProfilesAdapter _allowedErSSOPayloadTypes]
+ -[RMStoreProfilesAdapter _allowedErSSOPayloadTypes].cold.1
+ -[RMStoreProfilesAdapter _allowedPayloadType:store:]
+ -[RMStoreProfilesAdapter _disallowedPayloadTypes].cold.1
+ -[RMStoreUnresolvedAsset initWithAsset:queryParameters:downloadURL:useCache:]
+ -[RMStoreUnresolvedAsset initWithAsset:queryParameters:useCache:]
+ -[RMStoreUnresolvedAsset initWithAssetIdentifier:queryParameters:downloadURL:useCache:]
+ -[RMStoreUnresolvedAsset initWithAssetIdentifier:queryParameters:useCache:]
+ -[RMStoreUnresolvedAsset initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:useCache:]
+ -[RMStoreUnresolvedAsset useCache]
+ GCC_except_table28
+ GCC_except_table35
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table97
+ OBJC_IVAR_$_RMConfigurationUIDetails._hiddenDetails
+ OBJC_IVAR_$_RMStoreUnresolvedAsset._useCache
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_RMErSSOStore
+ _OBJC_CLASS_$_RMManagedDevice
+ _OBJC_CLASS_$_RMModelActivationSimpleDeclaration
+ _OBJC_CLASS_$_RMModelAppManagedDeclaration
+ _OBJC_CLASS_$_RMModelLegacyProfileDeclaration
+ _OBJC_CLASS_$_RMModelStatusBase
+ _OBJC_METACLASS_$_RMErSSOStore
+ _PROTOCOLS_RMErSSOStore.2
+ _RMStoreOptionEnrollmentURL
+ _RMStoreOptionMetaData
+ _RMUIConfigurationUIHiddenDetailAppBundleID
+ __100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.94
+ __100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.94.cold.1
+ __100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.94.cold.2
+ __106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.18
+ __106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.18.cold.1
+ __106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.15
+ __106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.15.cold.1
+ __120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke.35
+ __120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke.36
+ __120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke_2.cold.1
+ __120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke_2.cold.2
+ __120-[RMStatusPublisherDescription _loadDescriptionFromStatusEvents:statusKeysByNotification:statusKeysWithoutNotification:]_block_invoke.43
+ __122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.65
+ __122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.65.cold.1
+ __122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.66
+ __122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.66.cold.1
+ __122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke.cold.1
+ __38-[RMBaseStore metadataReturningError:]_block_invoke.48
+ __41-[RMBaseStore metadataValueForKey:error:]_block_invoke.51
+ __49-[RMProviderStore setMetadataValue:forKey:error:]_block_invoke.33
+ __52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.17
+ __52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.17.cold.1
+ __53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.24
+ __53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.24.cold.1
+ __53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.28
+ __53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.28.cold.1
+ __53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.30
+ __53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.30.cold.1
+ __53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.88
+ __53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.88.cold.1
+ __53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.88.cold.2
+ __60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.21
+ __60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.21.cold.1
+ __60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.83
+ __60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.83.cold.1
+ __63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.23
+ __63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.23.cold.1
+ __69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.20
+ __69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.20.cold.1
+ __69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.29
+ __69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.29.cold.1
+ __69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.87
+ __69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.87.cold.1
+ __69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.87.cold.2
+ __75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.47
+ __75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.47.cold.1
+ __75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke.cold.1
+ __75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.79
+ __75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.79.cold.1
+ __83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.93
+ __83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.93.cold.1
+ __83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.93.cold.2
+ __84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.31
+ __84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.31.cold.1
+ __84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke.cold.1
+ __95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.11
+ __95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.11.cold.1
+ __99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke.38
+ __99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke.39
+ __99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke_2.cold.1
+ __99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke_2.cold.2
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_RMErSSOStore
+ __DATA_RMErSSOStore
+ __INSTANCE_METHODS_RMErSSOStore
+ __METACLASS_DATA_RMErSSOStore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentFlowRMBridge
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentFlowRMBridge
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentFlowRMBridge
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentFlowRMBridge
+ __OBJC_PROTOCOL_$_DMCEnrollmentFlowRMBridge
+ __PROTOCOLS_RMErSSOStore
+ ___120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke
+ ___120+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:]_block_invoke_2
+ ___122-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:]_block_invoke
+ ___135+[RMAssetResolverController _fetchAssetDeclarationWithAssetIdentifier:configurationIdentifier:subscriberStore:scope:completionHandler:]_block_invoke
+ ___135+[RMAssetResolverController _fetchAssetDeclarationWithAssetIdentifier:configurationIdentifier:subscriberStore:scope:completionHandler:]_block_invoke_2
+ ___139-[RMConfigurationCombineApplicator _sendStatusForSuccessKeys:failedKeys:reasons:applyError:scope:configurations:success:completionHandler:]_block_invoke
+ ___139-[RMConfigurationCombineApplicator _sendStatusForSuccessKeys:failedKeys:reasons:applyError:scope:configurations:success:completionHandler:]_block_invoke_2
+ ___141+[RMAssetResolverController resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:]_block_invoke
+ ___145+[RMAssetResolverController resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]_block_invoke
+ ___145+[RMAssetResolverController resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]_block_invoke_2
+ ___147+[RMAssetResolverController resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:]_block_invoke
+ ___157+[RMAssetResolverController _resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:persistentRefs:completionHandler:]_block_invoke
+ ___51-[RMStoreProfilesAdapter _allowedErSSOPayloadTypes]_block_invoke
+ ___75-[RMBaseStore waitForActiveAndValidDeclarations:timeout:completionHandler:]_block_invoke
+ ___84-[RMProviderStore linkStoreToProfileIdentifier:accountIdentifier:completionHandler:]_block_invoke
+ ___99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke
+ ___99+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:]_block_invoke_2
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs_e66_v32?0"RMModelDeclarationBase"8"RMSubscriberStore"16"NSError"24l
+ ___block_descriptor_72_e8_32s40s48s56bs_e39_v24?0"RMSubscriberStore"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56bs_e66_v32?0"RMModelDeclarationBase"8"RMSubscriberStore"16"NSError"24l
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ __block_literal_global.72
+ __block_literal_global.80
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_RemoteManagementStore
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _allowedErSSOPayloadTypes.allowedErSSOPayloadTypes
+ _allowedErSSOPayloadTypes.onceToken
+ _associated conformance 21RemoteManagementStore10ErSSOErrorOSHAASQ
+ _associated conformance So16RMStoreOptionKeyaSHSCSQ
+ _associated conformance So16RMStoreOptionKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So16RMStoreOptionKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _bzero
+ _kRMBridgeAppStoreIDKey
+ _kRMBridgeBundleIDKey
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_allowedErSSOPayloadTypes
+ _objc_msgSend$_allowedPayloadType:store:
+ _objc_msgSend$_fetchAssetDeclarationWithAssetIdentifier:configurationIdentifier:subscriberStore:scope:completionHandler:
+ _objc_msgSend$_fetchSubscriberStoreIfNeededWithSubscriberStore:configurationIdentifier:scope:completionHandler:
+ _objc_msgSend$_loadManagedSettingsDescription
+ _objc_msgSend$_resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:
+ _objc_msgSend$_resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:
+ _objc_msgSend$_resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:persistentRefs:completionHandler:
+ _objc_msgSend$_sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:
+ _objc_msgSend$_sendStatusForSuccessKeys:failedKeys:reasons:applyError:scope:configurations:success:completionHandler:
+ _objc_msgSend$array
+ _objc_msgSend$declarationWithIdentifier:completionHandler:
+ _objc_msgSend$hiddenDetails
+ _objc_msgSend$initWithAsset:queryParameters:downloadURL:useCache:
+ _objc_msgSend$initWithAsset:queryParameters:useCache:
+ _objc_msgSend$initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:useCache:
+ _objc_msgSend$initWithTitle:description:details:hiddenDetails:
+ _objc_msgSend$isPreEnrollmentErSSOStore:
+ _objc_msgSend$isValid
+ _objc_msgSend$linkStoreIdentifier:profileIdentifier:accountIdentifier:completionHandler:
+ _objc_msgSend$managedSetting
+ _objc_msgSend$managedSettingKey
+ _objc_msgSend$managedSettingsSchemas
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:
+ _objc_msgSend$storeForStoreDeclarationKeyString:scope:completionHandler:
+ _objc_msgSend$stubObjectForStatusItemType:
+ _objc_msgSend$useCache
+ _objc_msgSend$waitForActiveAndValidDeclarations:timeout:storeIdentifier:completionHandler:
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release_n
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_stdlib_isStackAllocationSafe
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _swift_willThrowTypedImpl
+ _symbolic $sSY
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SDyS2SG
+ _symbolic SDySSypG
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SaySSG
+ _symbolic SaySSGSg______pSgIeggg_ s5ErrorP
+ _symbolic SaySo22RMModelDeclarationBaseCG
+ _symbolic Sb
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic SccySaySo15RMProviderStoreCG______pG s5ErrorP
+ _symbolic SccySaySo22RMModelDeclarationBaseCG______pG s5ErrorP
+ _symbolic SccySo15RMProviderStoreC______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic Sd
+ _symbolic So12RMErSSOStoreC
+ _symbolic So12RMErSSOStoreCXDXMT
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 21RemoteManagementStore10ErSSOErrorO
+ _symbolic _____ So16RMStoreOptionKeya
+ _symbolic ______pSgIegg_ s5ErrorP
+ _symbolic ______ypt So16RMStoreOptionKeya
+ _symbolic _____yS2SG s18_DictionaryStorageC
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySo21RMStoreDeclarationKeyCSSG s18_DictionaryStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So16RMStoreOptionKeya
+ _symbolic _____y_____ypG s18_DictionaryStorageC So16RMStoreOptionKeya
+ _symbolic ypSg
+ _symbolic ytIeAgHr_
+ block_copy_helper.15
+ block_copy_helper.29
+ block_copy_helper.32
+ block_copy_helper.56
+ block_copy_helper.59
+ block_copy_helper.74
+ block_copy_helper.77
+ block_copy_helper.82
+ block_copy_helper.86
+ block_descriptor.17
+ block_descriptor.31
+ block_descriptor.34
+ block_descriptor.58
+ block_descriptor.61
+ block_descriptor.76
+ block_descriptor.79
+ block_descriptor.84
+ block_descriptor.88
+ block_destroy_helper.16
+ block_destroy_helper.30
+ block_destroy_helper.33
+ block_destroy_helper.57
+ block_destroy_helper.60
+ block_destroy_helper.75
+ block_destroy_helper.78
+ block_destroy_helper.83
+ block_destroy_helper.87
+ objectdestroy.4Tm
- +[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:].cold.2
- +[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:].cold.3
- +[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:].cold.3
- -[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]
- -[RMConfigurationCombineApplicator _sendStatusForSuccessKeys:failedKeys:reasons:scope:configurations:completionHandler:]
- -[RMConfigurationUIDetails initWithTitle:description:details:]
- -[RMStoreUnresolvedAsset initWithAssetIdentifier:queryParameters:]
- -[RMStoreUnresolvedAsset initWithAssetIdentifier:queryParameters:downloadURL:]
- -[RMStoreUnresolvedAsset initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:]
- GCC_except_table25
- GCC_except_table85
- GCC_except_table87
- GCC_except_table96
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- __100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.93
- __100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.93.cold.1
- __100-[RMSubscriberStore _removeStatusForDeclarationIdentifier:declarationServerToken:completionHandler:]_block_invoke.93.cold.2
- __106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.12
- __106+[RMProviderStore createStoreWithType:scope:defaultToInteractive:dataSeparated:options:completionHandler:]_block_invoke.12.cold.1
- __106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.13
- __106+[RMSubscriberStore subscribedStoreConfigurationsVisibleUIWithScope:configurationTypes:completionHandler:]_block_invoke.13.cold.1
- __111-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]_block_invoke.63
- __111-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]_block_invoke.63.cold.1
- __111-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]_block_invoke.64
- __111-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]_block_invoke.64.cold.1
- __111-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]_block_invoke.cold.1
- __120-[RMStatusPublisherDescription _loadDescriptionFromStatusEvents:statusKeysByNotification:statusKeysWithoutNotification:]_block_invoke.25
- __38-[RMBaseStore metadataReturningError:]_block_invoke.47
- __41-[RMBaseStore metadataValueForKey:error:]_block_invoke.50
- __49-[RMProviderStore setMetadataValue:forKey:error:]_block_invoke.26
- __52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.16
- __52-[RMSubscriberStore resolveAsset:completionHandler:]_block_invoke.16.cold.1
- __53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.18
- __53+[RMProviderStore storesWithScope:completionHandler:]_block_invoke.18.cold.1
- __53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.22
- __53-[RMProviderStore applyChangesWithCompletionHandler:]_block_invoke.22.cold.1
- __53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.24
- __53-[RMProviderStore saveDeclaration:completionHandler:]_block_invoke.24.cold.1
- __53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.87
- __53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.87.cold.1
- __53-[RMSubscriberStore publishStatus:completionHandler:]_block_invoke.87.cold.2
- __60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.20
- __60+[RMSubscriberStore unassignAssets:scope:completionHandler:]_block_invoke.20.cold.1
- __60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.82
- __60-[RMSubscriberStore certificateStatusWithCompletionHandler:]_block_invoke.82.cold.1
- __63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.17
- __63+[RMProviderStore storeWithIdentifier:scope:completionHandler:]_block_invoke.17.cold.1
- __69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.14
- __69+[RMProviderStore removeStoreWithIdentifier:scope:completionHandler:]_block_invoke.14.cold.1
- __69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.23
- __69-[RMProviderStore deleteDeclarationWithIdentifier:completionHandler:]_block_invoke.23.cold.1
- __69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.86
- __69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.86.cold.1
- __69-[RMSubscriberStore setConfigurationUI:visible:ui:completionHandler:]_block_invoke.86.cold.2
- __75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.78
- __75-[RMSubscriberStore certificatePersistentRefForAssetKey:completionHandler:]_block_invoke.78.cold.1
- __83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.92
- __83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.92.cold.1
- __83-[RMSubscriberStore _writeStatusForDeclaration:validity:reasons:completionHandler:]_block_invoke.92.cold.2
- __92+[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:]_block_invoke.20
- __92+[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:]_block_invoke.21
- __92+[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:]_block_invoke_2.cold.1
- __92+[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:]_block_invoke_2.cold.2
- __95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.9
- __95+[RMSubscriberStore subscribedStoreDeclarationsWithScope:configurationTypes:completionHandler:]_block_invoke.9.cold.1
- __97+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:]_block_invoke.33
- __97+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:]_block_invoke.34
- __97+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:]_block_invoke_2.cold.1
- __97+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:]_block_invoke_2.cold.2
- ___111-[RMConfigurationCombineApplicator _sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:]_block_invoke
- ___120-[RMConfigurationCombineApplicator _sendStatusForSuccessKeys:failedKeys:reasons:scope:configurations:completionHandler:]_block_invoke
- ___120-[RMConfigurationCombineApplicator _sendStatusForSuccessKeys:failedKeys:reasons:scope:configurations:completionHandler:]_block_invoke_2
- ___92+[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:]_block_invoke
- ___92+[RMAssetResolverController resolveDataAsset:assetIdentifier:downloadURL:completionHandler:]_block_invoke_2
- ___97+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:]_block_invoke
- ___97+[RMAssetResolverController _resolveKeychainAsset:assetIdentifier:accessGroup:completionHandler:]_block_invoke_2
- __block_literal_global.71
- _objc_msgSend$_sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:
- _objc_msgSend$_sendStatusForSuccessKeys:failedKeys:reasons:scope:configurations:completionHandler:
- _objc_msgSend$classForStatusItemType:
- _objc_msgSend$initWithAsset:queryParameters:
- _objc_msgSend$initWithAsset:queryParameters:downloadURL:
- _objc_msgSend$initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:
- _objc_msgSend$initWithTitle:description:details:
CStrings:
+ "@\"NSDictionary\"32@0:8@\"NSArray\"16^@24"
+ "@44@0:8@16@24@32B40"
+ "@60@0:8@16q24@32@40@48B56"
+ "Activation does not reference configuration: %s"
+ "AppBundleID"
+ "Assets not specified for keychain item"
+ "Cannot deserialize declaration"
+ "Cannot deserialize declaration data"
+ "Configuration can't use manifest"
+ "Configurations do not specify a usable app"
+ "Created ErSSO store"
+ "Creating ErSSO store"
+ "DMCEnrollmentFlowRMBridge"
+ "Declarations are active and valid"
+ "ErSSO declarations:\n    Activation: %s\n    Configurations: %s\n    Assets: %s\n    AppStoreID: %s\n    BundleIDs: %s\n    Profiles: %ld"
+ "ErSSO store does not exist"
+ "ErSSO store does not exist - ignoring"
+ "ErSSO store exists - removing it"
+ "ErSSO store profile identifiers: %s"
+ "ErSSO store ready"
+ "Failed XPC connection while linking store: %{public}@"
+ "Failed XPC connection while waiting for declarations: %{public}@"
+ "Failed to clean up ErSSO store: %@"
+ "Failed to link store: %{public}@"
+ "Failed to wait for declarations: %{public}@"
+ "Fetching extensible SSO profile identifiers"
+ "Invalid configuration type: %s"
+ "JSONObjectWithData:options:error:"
+ "Linked store"
+ "Linking ErSSO store to MDM"
+ "Load ErSSO app details"
+ "ManagedSettings"
+ "Missing activation"
+ "Missing asset: %{public}@"
+ "Missing configuration"
+ "Only one activation allowed"
+ "RMErSSOStore"
+ "Removing ErSSO store"
+ "Saving declarations to ErSSO store"
+ "SettingsGroups"
+ "T@\"NSDictionary\",R,N,V_hiddenDetails"
+ "TB,R,N,V_useCache"
+ "Using AppStoreID requires only one configuration be present"
+ "Waiting for active and valid declarations in ErSSO store"
+ "Wrong asset type: %{public}@"
+ "_allowedErSSOPayloadTypes"
+ "_allowedPayloadType:store:"
+ "_fetchAssetDeclarationWithAssetIdentifier:configurationIdentifier:subscriberStore:scope:completionHandler:"
+ "_fetchSubscriberStoreIfNeededWithSubscriberStore:configurationIdentifier:scope:completionHandler:"
+ "_hiddenDetails"
+ "_loadManagedSettingsDescription"
+ "_resolveDataAsset:assetIdentifier:store:downloadURL:completionHandler:"
+ "_resolveKeychainAsset:assetIdentifier:configurationKey:store:accessGroup:completionHandler:"
+ "_resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:persistentRefs:completionHandler:"
+ "_sendStatusForFailedKeys:enumerator:applyError:scope:configurations:completionHandler:"
+ "_sendStatusForSuccessKeys:failedKeys:reasons:applyError:scope:configurations:success:completionHandler:"
+ "_useCache"
+ "appDetailsFromDeclarations:error:"
+ "array"
+ "com.apple.ManagedSettings.effective-settings.changed"
+ "com.apple.extensiblesso"
+ "com.apple.remotemanagement.effective-settings.changed"
+ "com.apple.security.acme"
+ "com.apple.security.pem"
+ "com.apple.security.pkcs1"
+ "com.apple.security.pkcs12"
+ "com.apple.security.root"
+ "com.apple.security.scep"
+ "com.apple.security.selfsignedcertificate"
+ "configurationUIWithTitle:description:details:hiddenDetails:"
+ "createErSSOStoreWithDeclarations:chosenBundleID:personaID:isUserEnrollment:completionHandler:"
+ "currentManagedDevice"
+ "declarationKey is invalid: %{public}@"
+ "extensibleSSOProfileIdentifiersWithCompletionHandler:"
+ "hiddenDetails"
+ "initWithAsset:queryParameters:downloadURL:useCache:"
+ "initWithAsset:queryParameters:useCache:"
+ "initWithAssetIdentifier:queryParameters:downloadURL:useCache:"
+ "initWithAssetIdentifier:queryParameters:useCache:"
+ "initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:useCache:"
+ "initWithTitle:description:details:hiddenDetails:"
+ "isPreEnrollmentErSSOStore:"
+ "isSupervised"
+ "linkErSSOStoreToMDMWithProfileIdentifier:accountIdentifier:completionHandler:"
+ "linkStoreIdentifier:profileIdentifier:accountIdentifier:completionHandler:"
+ "linkStoreToProfileIdentifier:accountIdentifier:completionHandler:"
+ "managedSetting"
+ "managedSettingKey"
+ "managedSettingsSchemas"
+ "payloadAppStoreID"
+ "payloadBundleID"
+ "payloadManifestURL"
+ "payloadStandardConfigurations"
+ "removeAllObjects"
+ "removeErSSOStoreWithCompletionHandler:"
+ "resolveDataAssetWithAssetIdentifier:configurationIdentifier:downloadURL:subscriberStore:scope:completionHandler:"
+ "resolveKeychainAssetWithAssetIdentifier:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
+ "resolveKeychainAssetsWithAssetIdentifiers:configurationIdentifier:accessGroup:subscriberStore:scope:completionHandler:"
+ "rmstore.enrollment.url"
+ "rmstore.meta.data"
+ "setPayloadStandardConfigurations:"
+ "storeForStoreDeclarationKeyString:scope:completionHandler:"
+ "stubObjectForStatusItemType:"
+ "use-cache"
+ "useCache"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSError\">24"
+ "v32@?0@\"RMModelDeclarationBase\"8@\"RMSubscriberStore\"16@\"NSError\"24"
+ "v40@0:8@\"NSSet\"16d24@?<v@?@\"NSError\">32"
+ "v40@0:8@16d24@?32"
+ "v48@0:8@\"NSSet\"16d24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16d24@32@?40"
+ "v52@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
+ "v64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSArray\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"RMSubscriberStore\"40q48@?<v@?@\"NSData\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@\"RMSubscriberStore\"40q48@?<v@?B@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v64@0:8@16@24@32@40q48@?56"
+ "v76@0:8@16@24@32@40q48@56B64@?68"
+ "waitForActiveAndValidDeclarations:timeout:completionHandler:"
+ "waitForActiveAndValidDeclarations:timeout:storeIdentifier:completionHandler:"
+ "waitForActiveAndValidDeclarationsInErSSOStoreWithTimeout:completionHandler:"
- "@56@0:8@16q24@32@40@48"
- "_sendStatusForFailedKeys:enumerator:scope:configurations:completionHandler:"
- "_sendStatusForSuccessKeys:failedKeys:reasons:scope:configurations:completionHandler:"
- "classForStatusItemType:"
- "initWithAssetIdentifier:queryParameters:"
- "initWithAssetIdentifier:queryParameters:downloadURL:"
- "initWithAssetIdentifier:resolveAs:queryParameters:downloadURL:extensionToken:"
- "initWithTitle:description:details:"

```
