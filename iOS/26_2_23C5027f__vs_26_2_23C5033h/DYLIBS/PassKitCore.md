## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1642.3.2.0.0
-  __TEXT.__text: 0x7ca688
+1642.3.3.0.0
+  __TEXT.__text: 0x7cb6b8
   __TEXT.__auth_stubs: 0x4a40
-  __TEXT.__objc_methlist: 0x6ca60
-  __TEXT.__const: 0x24898
-  __TEXT.__cstring: 0x68f21
-  __TEXT.__swift5_typeref: 0x5952
+  __TEXT.__objc_methlist: 0x6caa0
+  __TEXT.__const: 0x248b8
+  __TEXT.__cstring: 0x68f81
+  __TEXT.__swift5_typeref: 0x597e
   __TEXT.__constg_swiftt: 0x4e34
   __TEXT.__swift5_reflstr: 0x42cd
   __TEXT.__swift5_fieldmd: 0x51cc

   __TEXT.__swift5_proto: 0xc94
   __TEXT.__swift5_types: 0x524
   __TEXT.__swift5_capture: 0x3ddc
-  __TEXT.__oslogstring: 0x34c89
+  __TEXT.__oslogstring: 0x34c9d
   __TEXT.__swift_as_entry: 0xa8
   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x76ac
+  __TEXT.__gcc_except_tab: 0x76c4
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1b980
+  __TEXT.__unwind_info: 0x1b998
   __TEXT.__eh_frame: 0x4b30
   __TEXT.__objc_classname: 0xf956
-  __TEXT.__objc_methname: 0xcc426
-  __TEXT.__objc_methtype: 0x179a0
-  __TEXT.__objc_stubs: 0x5a180
+  __TEXT.__objc_methname: 0xcc592
+  __TEXT.__objc_methtype: 0x17a24
+  __TEXT.__objc_stubs: 0x5a200
   __DATA_CONST.__got: 0x49d0
-  __DATA_CONST.__const: 0x212d0
+  __DATA_CONST.__const: 0x21380
   __DATA_CONST.__objc_classlist: 0x3ab8
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23490
+  __DATA_CONST.__objc_selrefs: 0x234b8
   __DATA_CONST.__objc_protorefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x2f28
   __DATA_CONST.__objc_arraydata: 0x27d8
   __AUTH_CONST.__auth_got: 0x2530
-  __AUTH_CONST.__const: 0x1e7e8
-  __AUTH_CONST.__cfstring: 0x71540
-  __AUTH_CONST.__objc_const: 0xc4048
+  __AUTH_CONST.__const: 0x1e818
+  __AUTH_CONST.__cfstring: 0x715c0
+  __AUTH_CONST.__objc_const: 0xc4060
   __AUTH_CONST.__objc_arrayobj: 0xd38
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0x1518

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x6494
-  __DATA.__data: 0x7d90
+  __DATA.__data: 0x7da0
   __DATA.__bss: 0x18270
   __DATA.__common: 0xc00
   __DATA_DIRTY.__objc_ivar: 0x25d4

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 734CEC61-8DBB-3946-BA03-422C06660ED7
-  Functions: 49625
-  Symbols:   128403
-  CStrings:  67506
+  UUID: E089E678-39D7-3FA7-9A49-4B27488EC8E7
+  Functions: 49635
+  Symbols:   128435
+  CStrings:  67522
 
Symbols:
+ -[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]
+ -[PKMobileAssetManager _purgeCashStickersWithCompletion:]
+ -[PKMobileAssetManager updateCashStickersIfNecessaryWithCompletion:]
+ -[PKPassLibrary automaticallyPresentedPassForPasses:applicationIdentifier:]
+ -[PKPassLibrary inAppPaymentPassUniqueIDForPaymentRequest:]
+ GCC_except_table106
+ GCC_except_table117
+ GCC_except_table152
+ GCC_except_table157
+ GCC_except_table229
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table293
+ GCC_except_table305
+ GCC_except_table310
+ GCC_except_table317
+ GCC_except_table322
+ GCC_except_table346
+ GCC_except_table376
+ GCC_except_table392
+ GCC_except_table397
+ GCC_except_table453
+ GCC_except_table458
+ GCC_except_table460
+ GCC_except_table463
+ GCC_except_table523
+ GCC_except_table531
+ GCC_except_table533
+ GCC_except_table548
+ GCC_except_table551
+ GCC_except_table554
+ GCC_except_table557
+ GCC_except_table575
+ GCC_except_table67
+ _.str.886
+ _PKForceAppleCashStickerPackEligible
+ _PKForceAppleCashStickerPackEligibleKey
+ _PKPaymentNetworkConecs
+ ___100-[PKPassLibrary checkFidoKeyPresenceForRelyingParty:relyingPartyAccountHash:fidoKeyHash:completion:]_block_invoke.257
+ ___100-[PKPassLibrary inAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.157
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.411
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.412
+ ___108-[PKPassLibrary createFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:externalizedAuth:completion:]_block_invoke.255
+ ___110-[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]_block_invoke.275
+ ___112-[PKPassLibrary inAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.155
+ ___115-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.158
+ ___127-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.156
+ ___134-[PKPassLibrary hasInAppPaymentPassesForNetworks:capabilities:issuerCountryCodes:paymentRequestType:isMultiTokensRequest:withHandler:]_block_invoke.154
+ ___140-[PKPassLibrary configureHomeAuxiliaryCapabilitiesForSerialNumber:homeIdentifier:fromUnifiedAccessDescriptor:andAliroDescriptor:completion:]_block_invoke.185
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.465
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.467
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.469
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.470
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.466
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.468
+ ___142-[PKPassLibrary signWithFidoKeyForRelyingParty:relyingPartyAccountHash:fidoKeyHash:challenge:publicKeyIdentifier:externalizedAuth:completion:]_block_invoke.258
+ ___155-[PKPassLibrary requestPersonalizationOfPassWithUniqueIdentifier:contact:personalizationToken:requiredPersonalizationFields:personalizationSource:handler:]_block_invoke.209
+ ___31-[PKPassLibrary backupMetadata]_block_invoke.249
+ ___35-[PKPassLibrary setBackupMetadata:]_block_invoke.250
+ ___41-[PKPassLibrary archivePassWithUniqueID:]_block_invoke.295
+ ___41-[PKPassLibrary recoverPassWithUniqueID:]_block_invoke.294
+ ___43-[PKPassLibrary expressFelicaTransitPasses]_block_invoke.228
+ ___47-[PKPassLibrary unexpiredPassesOrderedByGroup:]_block_invoke.160
+ ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke.472
+ ___48-[PKPassLibrary exportableCardEntry:completion:]_block_invoke.273
+ ___50-[PKPassLibrary exportableManifestWithCompletion:]_block_invoke.271
+ ___51-[PKPassLibrary resetApplePayWithDiagnosticReason:]_block_invoke.299
+ ___52-[PKPassLibrary passLocalizedStringForKey:uniqueID:]_block_invoke.167
+ ___53-[PKPassLibrary canPresentPaymentRequest:completion:]_block_invoke.194
+ ___54-[PKPassLibrary addISO18013Blobs:cardType:completion:]_block_invoke.264
+ ___54-[PKPassLibrary defaultPaymentPassesWithRemotePasses:]_block_invoke.227
+ ___57-[PKPassLibrary _defaultPaymentPassWithoutPaymentRequest]_block_invoke.238
+ ___57-[PKPassLibrary addPassesWithData:withCompletionHandler:]_block_invoke.169
+ ___57-[PKPassLibrary removePassWithUniqueID:diagnosticReason:]_block_invoke.292
+ ___57-[PKPassLibrary removePassesOfType:withDiagnosticReason:]_block_invoke.296
+ ___58-[PKPassLibrary addPassesContainer:withCompletionHandler:]_block_invoke.172
+ ___58-[PKPassLibrary meetsProvisioningRequirements:completion:]_block_invoke.218
+ ___58-[PKPassLibrary prepareForBackupRestoreWithSafeHavenPath:]_block_invoke.254
+ ___59-[PKPassLibrary inAppPaymentPassUniqueIDForPaymentRequest:]_block_invoke
+ ___59-[PKPassLibrary inAppPaymentPassUniqueIDForPaymentRequest:]_block_invoke.147
+ ___60-[PKPassLibrary passUniqueIDsMatchingSearchTerm:completion:]_block_invoke.161
+ ___60-[PKPassLibrary removePassesWithUniqueIDs:diagnosticReason:]_block_invoke.293
+ ___61-[PKPassLibrary availableHomeKeyPassesWithCompletionHandler:]_block_invoke.178
+ ___62-[PKPassLibrary addSharedFlight:fromSenderAddress:completion:]_block_invoke.212
+ ___62-[PKPassLibrary canAddCarKeyPassWithConfiguration:completion:]_block_invoke.216
+ ___62-[PKPassLibrary enabledValueAddedServicePassesWithCompletion:]_block_invoke.159
+ ___62-[PKPassLibrary resetApplePayWithDiagnosticReason:completion:]_block_invoke.298
+ ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke.174
+ ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke_2.175
+ ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke.181
+ ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke_2.182
+ ___65-[PKPassLibrary paymentSetupFeaturesForConfiguration:completion:]_block_invoke.192
+ ___67-[PKPassLibrary canAddSecureElementPassWithConfiguration:outError:]_block_invoke.214
+ ___67-[PKPassLibrary presentPaymentSetupRequest:orientation:completion:]_block_invoke.191
+ ___67-[PKPassLibrary sortedTransitPassesForAppletDataFormat:completion:]_block_invoke.230
+ ___68-[PKMobileAssetManager updateCashStickersIfNecessaryWithCompletion:]_block_invoke
+ ___68-[PKMobileAssetManager updateCashStickersIfNecessaryWithCompletion:]_block_invoke.433
+ ___68-[PKPassLibrary getContainmentStatusAndSettingsForPass:withHandler:]_block_invoke.210
+ ___68-[PKPassLibrary prepareForBackupRestoreWithExistingPreferencesData:]_block_invoke.251
+ ___68-[PKPassLibrary removePassesOfType:withDiagnosticReason:completion:]_block_invoke.297
+ ___69-[PKPassLibrary addISO18013BlobsFromCredentials:cardType:completion:]_block_invoke.263
+ ___69-[PKPassLibrary canAddSecureElementPassWithConfiguration:completion:]_block_invoke.215
+ ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.244
+ ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.245
+ ___70-[PKPassLibrary addPassesWithIngestionPayloads:withCompletionHandler:]_block_invoke.170
+ ___70-[PKPassLibrary pushProvisioningNoncesWithCredentialCount:completion:]_block_invoke.239
+ ___70-[PKPassLibrary requestUpdateOfObjectWithUniqueIdentifier:completion:]_block_invoke.208
+ ___70-[PKPassLibrary sendRKEPassThroughMessage:forSessionIdentifier:error:]_block_invoke.248
+ ___71-[PKPassLibrary paymentPassWithAssociatedAccountIdentifier:completion:]_block_invoke.193
+ ___72-[PKPassLibrary fetchHomePaymentApplicationsForSerialNumber:completion:]_block_invoke.187
+ ___72-[PKPassLibrary provisionHomeKeyPassForSerialNumbers:completionHandler:]_block_invoke.176
+ ___73-[PKPassLibrary generateAuxiliaryCapabilitiesForRequirements:completion:]_block_invoke.266
+ ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.477
+ ___74-[PKPassLibrary signData:signatureEntanglementMode:withCompletionHandler:]_block_invoke.269
+ ___78-[PKPassLibrary generateSEEncryptionCertificateForSubCredentialId:completion:]_block_invoke.260
+ ___79-[PKPassLibrary _fetchContentForUniqueID:usingSynchronousProxy:withCompletion:]_block_invoke.221
+ ___79-[PKPassLibrary generateISOEncryptionCertificateForSubCredentialId:completion:]_block_invoke.261
+ ___79-[PKPassLibrary sortedTransitPassesForTransitNetworkIdentifiersWithCompletion:]_block_invoke.229
+ ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.452
+ ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.455
+ ___80-[PKPassLibrary presentContactlessInterfaceForDefaultPassFromSource:completion:]_block_invoke.196
+ ___82-[PKPassLibrary startVehicleConnectionSessionWithPassUniqueIdentifier:completion:]_block_invoke.247
+ ___83-[PKPassLibrary containsPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.163
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.437
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.439
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.442
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke_2
+ ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.322
+ ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.323
+ ___87-[PKPassLibrary generateTransactionKeyWithReaderIdentifier:readerPublicKey:completion:]_block_invoke.183
+ ___89-[PKPassLibrary _activateSecureElementPass:withActivationCode:activationData:completion:]_block_invoke.207
+ ___89-[PKPassLibrary longTermPrivacyKeyForCredentialGroupIdentifier:reuseExisting:completion:]_block_invoke.265
+ ___91-[PKPassLibrary enableExpressForPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.188
+ ___94-[PKPassLibrary presentContactlessInterfaceForPassWithUniqueIdentifier:fromSource:completion:]_block_invoke.197
+ ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.319
+ ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.320
+ ___99-[PKPassLibrary requestIssuerBoundPassesWithBindingWithData:automaticallyProvision:withCompletion:]_block_invoke.268
+ ___PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1107
+ ___block_descriptor_49_e8_32s40s_e61_v32?0"PKAsyncOperationState"8"NSNull"16?<v?"NSNull"B>24ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e8_v16?0q8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e50_v24?0"PKPaymentEligibilityResponse"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.1002
+ ___block_literal_global.1011
+ ___block_literal_global.1024
+ ___block_literal_global.1026
+ ___block_literal_global.1028
+ ___block_literal_global.1033
+ ___block_literal_global.1041
+ ___block_literal_global.1044
+ ___block_literal_global.1072
+ ___block_literal_global.1077
+ ___block_literal_global.1079
+ ___block_literal_global.1084
+ ___block_literal_global.1089
+ ___block_literal_global.1094
+ ___block_literal_global.1099
+ ___block_literal_global.1104
+ ___block_literal_global.1106
+ ___block_literal_global.1109
+ ___block_literal_global.1114
+ ___block_literal_global.1129
+ ___block_literal_global.1146
+ ___block_literal_global.1165
+ ___block_literal_global.1244
+ ___block_literal_global.1249
+ ___block_literal_global.1256
+ ___block_literal_global.1259
+ ___block_literal_global.1268
+ ___block_literal_global.1282
+ ___block_literal_global.1440
+ ___block_literal_global.1442
+ ___block_literal_global.1445
+ ___block_literal_global.1681
+ ___block_literal_global.1683
+ ___block_literal_global.1688
+ ___block_literal_global.1692
+ ___block_literal_global.1706
+ ___block_literal_global.1708
+ ___block_literal_global.1713
+ ___block_literal_global.1733
+ ___block_literal_global.1740
+ ___block_literal_global.1742
+ ___block_literal_global.1744
+ ___block_literal_global.1747
+ ___block_literal_global.233
+ ___block_literal_global.301
+ ___block_literal_global.408
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.459
+ ___block_literal_global.484
+ ___block_literal_global.690
+ ___block_literal_global.701
+ ___block_literal_global.706
+ ___block_literal_global.711
+ ___block_literal_global.716
+ ___block_literal_global.721
+ ___block_literal_global.731
+ ___block_literal_global.736
+ ___block_literal_global.738
+ ___block_literal_global.744
+ ___block_literal_global.747
+ ___block_literal_global.776
+ ___block_literal_global.779
+ ___block_literal_global.781
+ ___block_literal_global.939
+ ___block_literal_global.956
+ ___block_literal_global.967
+ ___block_literal_global.969
+ ___block_literal_global.994
+ _block_copy_helper.54
+ _block_descriptor.56
+ _block_destroy_helper.55
+ _flat unique So8NSObject_p
+ _flat unique So9NSCopying_p
+ _objc_msgSend$_downloadPrefetchableAssetsForType:isDiscretionary:completion:
+ _objc_msgSend$_purgeCashStickersWithCompletion:
+ _objc_msgSend$automaticallyPresentedPassForPasses:applicationIdentifier:
+ _objc_msgSend$inAppPaymentPassUniqueIDForNetworks:capabilities:issuerCountryCodes:paymentRequestType:isMultiTokensRequest:withHandler:
+ _objc_msgSend$setApplicationIdentifierOverride:
+ _objc_msgSend$setUsageDescriptionKey:
+ _objc_msgSend$updateCashStickersIfNecessaryWithCompletion:
+ _symbolic ___________p So9NSCopyingP So8NSObjectP
- -[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]
- -[PKMobileAssetManager _purgeCashStickers]
- -[PKMobileAssetManager updateCashStickersIfNecessary]
- GCC_except_table144
- GCC_except_table146
- GCC_except_table225
- GCC_except_table227
- GCC_except_table261
- GCC_except_table264
- GCC_except_table273
- GCC_except_table289
- GCC_except_table301
- GCC_except_table303
- GCC_except_table306
- GCC_except_table313
- GCC_except_table372
- GCC_except_table393
- GCC_except_table449
- GCC_except_table454
- GCC_except_table456
- GCC_except_table459
- GCC_except_table519
- GCC_except_table527
- GCC_except_table529
- GCC_except_table544
- GCC_except_table547
- GCC_except_table550
- GCC_except_table571
- _.str.880
- ___100-[PKPassLibrary checkFidoKeyPresenceForRelyingParty:relyingPartyAccountHash:fidoKeyHash:completion:]_block_invoke.251
- ___100-[PKPassLibrary inAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.151
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.402
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.403
- ___108-[PKPassLibrary createFidoKeyForRelyingParty:relyingPartyAccountHash:challenge:externalizedAuth:completion:]_block_invoke.249
- ___110-[PKPassLibrary overrideStateOfRelevancyPresentmentOfType:containingPassUniqueIdentifier:newState:completion:]_block_invoke.269
- ___112-[PKPassLibrary inAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:]_block_invoke.149
- ___115-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForWebDomain:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.152
- ___127-[PKPassLibrary hasInAppPrivateLabelPaymentPassesForApplicationIdentifier:issuerCountryCodes:isMultiTokensRequest:withHandler:]_block_invoke.150
- ___134-[PKPassLibrary hasInAppPaymentPassesForNetworks:capabilities:issuerCountryCodes:paymentRequestType:isMultiTokensRequest:withHandler:]_block_invoke.148
- ___140-[PKPassLibrary configureHomeAuxiliaryCapabilitiesForSerialNumber:homeIdentifier:fromUnifiedAccessDescriptor:andAliroDescriptor:completion:]_block_invoke.179
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.454
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.456
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.458
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.459
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.455
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.457
- ___142-[PKPassLibrary signWithFidoKeyForRelyingParty:relyingPartyAccountHash:fidoKeyHash:challenge:publicKeyIdentifier:externalizedAuth:completion:]_block_invoke.252
- ___155-[PKPassLibrary requestPersonalizationOfPassWithUniqueIdentifier:contact:personalizationToken:requiredPersonalizationFields:personalizationSource:handler:]_block_invoke.203
- ___31-[PKPassLibrary backupMetadata]_block_invoke.243
- ___35-[PKPassLibrary setBackupMetadata:]_block_invoke.244
- ___41-[PKPassLibrary archivePassWithUniqueID:]_block_invoke.289
- ___41-[PKPassLibrary recoverPassWithUniqueID:]_block_invoke.288
- ___43-[PKPassLibrary expressFelicaTransitPasses]_block_invoke.222
- ___47-[PKPassLibrary unexpiredPassesOrderedByGroup:]_block_invoke.154
- ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke.461
- ___48-[PKPassLibrary exportableCardEntry:completion:]_block_invoke.267
- ___50-[PKPassLibrary exportableManifestWithCompletion:]_block_invoke.265
- ___51-[PKPassLibrary resetApplePayWithDiagnosticReason:]_block_invoke.293
- ___52-[PKPassLibrary passLocalizedStringForKey:uniqueID:]_block_invoke.161
- ___53-[PKMobileAssetManager updateCashStickersIfNecessary]_block_invoke
- ___53-[PKPassLibrary canPresentPaymentRequest:completion:]_block_invoke.188
- ___54-[PKPassLibrary addISO18013Blobs:cardType:completion:]_block_invoke.258
- ___54-[PKPassLibrary defaultPaymentPassesWithRemotePasses:]_block_invoke.221
- ___57-[PKPassLibrary _defaultPaymentPassWithoutPaymentRequest]_block_invoke.232
- ___57-[PKPassLibrary addPassesWithData:withCompletionHandler:]_block_invoke.163
- ___57-[PKPassLibrary removePassWithUniqueID:diagnosticReason:]_block_invoke.286
- ___57-[PKPassLibrary removePassesOfType:withDiagnosticReason:]_block_invoke.290
- ___58-[PKPassLibrary addPassesContainer:withCompletionHandler:]_block_invoke.166
- ___58-[PKPassLibrary meetsProvisioningRequirements:completion:]_block_invoke.212
- ___58-[PKPassLibrary prepareForBackupRestoreWithSafeHavenPath:]_block_invoke.248
- ___60-[PKPassLibrary passUniqueIDsMatchingSearchTerm:completion:]_block_invoke.155
- ___60-[PKPassLibrary removePassesWithUniqueIDs:diagnosticReason:]_block_invoke.287
- ___61-[PKPassLibrary availableHomeKeyPassesWithCompletionHandler:]_block_invoke.172
- ___62-[PKPassLibrary addSharedFlight:fromSenderAddress:completion:]_block_invoke.206
- ___62-[PKPassLibrary canAddCarKeyPassWithConfiguration:completion:]_block_invoke.210
- ___62-[PKPassLibrary enabledValueAddedServicePassesWithCompletion:]_block_invoke.153
- ___62-[PKPassLibrary resetApplePayWithDiagnosticReason:completion:]_block_invoke.292
- ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke.168
- ___63-[PKPassLibrary addUnsignedPassesAtURLs:withCompletionHandler:]_block_invoke_2.169
- ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke.175
- ___64-[PKPassLibrary replaceUnsignedPassAtURL:withCompletionHandler:]_block_invoke_2.176
- ___65-[PKPassLibrary paymentSetupFeaturesForConfiguration:completion:]_block_invoke.186
- ___67-[PKPassLibrary canAddSecureElementPassWithConfiguration:outError:]_block_invoke.208
- ___67-[PKPassLibrary presentPaymentSetupRequest:orientation:completion:]_block_invoke.185
- ___67-[PKPassLibrary sortedTransitPassesForAppletDataFormat:completion:]_block_invoke.224
- ___68-[PKPassLibrary getContainmentStatusAndSettingsForPass:withHandler:]_block_invoke.204
- ___68-[PKPassLibrary prepareForBackupRestoreWithExistingPreferencesData:]_block_invoke.245
- ___68-[PKPassLibrary removePassesOfType:withDiagnosticReason:completion:]_block_invoke.291
- ___69-[PKPassLibrary addISO18013BlobsFromCredentials:cardType:completion:]_block_invoke.257
- ___69-[PKPassLibrary canAddSecureElementPassWithConfiguration:completion:]_block_invoke.209
- ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.238
- ___69-[PKPassLibrary configurePushProvisioningConfigurationV2:completion:]_block_invoke.239
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.429
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.431
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke.434
- ___70-[PKMobileAssetManager _downloadPrefetchableAssetsForType:completion:]_block_invoke_2
- ___70-[PKPassLibrary addPassesWithIngestionPayloads:withCompletionHandler:]_block_invoke.164
- ___70-[PKPassLibrary pushProvisioningNoncesWithCredentialCount:completion:]_block_invoke.233
- ___70-[PKPassLibrary requestUpdateOfObjectWithUniqueIdentifier:completion:]_block_invoke.202
- ___70-[PKPassLibrary sendRKEPassThroughMessage:forSessionIdentifier:error:]_block_invoke.242
- ___71-[PKPassLibrary paymentPassWithAssociatedAccountIdentifier:completion:]_block_invoke.187
- ___72-[PKPassLibrary fetchHomePaymentApplicationsForSerialNumber:completion:]_block_invoke.181
- ___72-[PKPassLibrary provisionHomeKeyPassForSerialNumbers:completionHandler:]_block_invoke.170
- ___73-[PKPassLibrary generateAuxiliaryCapabilitiesForRequirements:completion:]_block_invoke.260
- ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.466
- ___74-[PKPassLibrary signData:signatureEntanglementMode:withCompletionHandler:]_block_invoke.263
- ___78-[PKPassLibrary generateSEEncryptionCertificateForSubCredentialId:completion:]_block_invoke.254
- ___79-[PKPassLibrary _fetchContentForUniqueID:usingSynchronousProxy:withCompletion:]_block_invoke.215
- ___79-[PKPassLibrary generateISOEncryptionCertificateForSubCredentialId:completion:]_block_invoke.255
- ___79-[PKPassLibrary sortedTransitPassesForTransitNetworkIdentifiersWithCompletion:]_block_invoke.223
- ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.444
- ___80-[PKPassLibrary presentContactlessInterfaceForDefaultPassFromSource:completion:]_block_invoke.190
- ___82-[PKPassLibrary startVehicleConnectionSessionWithPassUniqueIdentifier:completion:]_block_invoke.241
- ___83-[PKPassLibrary containsPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.157
- ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.317
- ___87-[PKPassLibrary _getGroupsControllerSnapshotWithOptions:synchronously:retries:handler:]_block_invoke.318
- ___87-[PKPassLibrary generateTransactionKeyWithReaderIdentifier:readerPublicKey:completion:]_block_invoke.177
- ___89-[PKPassLibrary _activateSecureElementPass:withActivationCode:activationData:completion:]_block_invoke.201
- ___89-[PKPassLibrary longTermPrivacyKeyForCredentialGroupIdentifier:reuseExisting:completion:]_block_invoke.259
- ___91-[PKPassLibrary enableExpressForPassWithPassTypeIdentifier:serialNumber:completionHandler:]_block_invoke.182
- ___94-[PKPassLibrary presentContactlessInterfaceForPassWithUniqueIdentifier:fromSource:completion:]_block_invoke.191
- ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.314
- ___96-[PKPassLibrary _getPassesAndCatalogOfPassTypes:synchronously:limitResults:withRetries:handler:]_block_invoke.315
- ___99-[PKPassLibrary requestIssuerBoundPassesWithBindingWithData:automaticallyProvision:withCompletion:]_block_invoke.262
- ___PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1104
- ___block_descriptor_64_e8_32s40s48s56bs_e50_v24?0"PKPaymentEligibilityResponse"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.1005
- ___block_literal_global.1018
- ___block_literal_global.1020
- ___block_literal_global.1022
- ___block_literal_global.1027
- ___block_literal_global.1038
- ___block_literal_global.1066
- ___block_literal_global.1071
- ___block_literal_global.1073
- ___block_literal_global.1078
- ___block_literal_global.1083
- ___block_literal_global.1088
- ___block_literal_global.1093
- ___block_literal_global.1098
- ___block_literal_global.1103
- ___block_literal_global.1108
- ___block_literal_global.1113
- ___block_literal_global.1115
- ___block_literal_global.1140
- ___block_literal_global.1159
- ___block_literal_global.1238
- ___block_literal_global.1243
- ___block_literal_global.1247
- ___block_literal_global.1250
- ___block_literal_global.1262
- ___block_literal_global.1276
- ___block_literal_global.1434
- ___block_literal_global.1436
- ___block_literal_global.1439
- ___block_literal_global.1675
- ___block_literal_global.1677
- ___block_literal_global.1682
- ___block_literal_global.1686
- ___block_literal_global.1700
- ___block_literal_global.1702
- ___block_literal_global.1707
- ___block_literal_global.1721
- ___block_literal_global.1730
- ___block_literal_global.1732
- ___block_literal_global.1734
- ___block_literal_global.1741
- ___block_literal_global.227
- ___block_literal_global.295
- ___block_literal_global.297
- ___block_literal_global.399
- ___block_literal_global.443
- ___block_literal_global.482
- ___block_literal_global.684
- ___block_literal_global.689
- ___block_literal_global.700
- ___block_literal_global.710
- ___block_literal_global.715
- ___block_literal_global.725
- ___block_literal_global.730
- ___block_literal_global.732
- ___block_literal_global.733
- ___block_literal_global.737
- ___block_literal_global.770
- ___block_literal_global.773
- ___block_literal_global.933
- ___block_literal_global.948
- ___block_literal_global.950
- ___block_literal_global.953
- ___block_literal_global.955
- ___block_literal_global.957
- ___block_literal_global.988
- ___block_literal_global.990
- _objc_msgSend$_downloadPrefetchableAssetsForType:completion:
- _objc_msgSend$_purgeCashStickers
- _objc_msgSend$updateCashStickersIfNecessary
CStrings:
+ "Conecs"
+ "Finished updating cash sticker assets. Has stickers: %ld"
+ "Mobile asset bundle exists for identifier %@ but is not installed. Ignoring"
+ "NETWORK_NAME_CONECS"
+ "NETWORK_NAME_CONECS_CARD_NAME"
+ "PKForceAppleCashStickerPackEligibleKey"
+ "_downloadPrefetchableAssetsForType:isDiscretionary:completion:"
+ "_purgeCashStickersWithCompletion:"
+ "applicationsDidUpdateMetadata:"
+ "automaticallyPresentedPassForPasses:applicationIdentifier:"
+ "inAppPaymentPassUniqueIDForNetworks:capabilities:issuerCountryCodes:paymentRequestType:isMultiTokensRequest:withHandler:"
+ "inAppPaymentPassUniqueIDForPaymentRequest:"
+ "localizedLongDescription"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "updateCashStickersIfNecessaryWithCompletion:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v60@0:8@\"NSSet\"16Q24@\"NSSet\"32@\"NSNumber\"40B48@?<v@?@\"NSString\">52"
- "Warning: %@ requested without a valid hostApplicationIdentifier or web domain. This is likely not what you want!"
- "_downloadPrefetchableAssetsForType:completion:"
- "_purgeCashStickers"
- "updateCashStickersIfNecessary"

```
