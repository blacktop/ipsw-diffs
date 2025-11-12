## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x34947c
+6200.3.8.0.0
+  __TEXT.__text: 0x3494f4
   __TEXT.__auth_stubs: 0x3790
-  __TEXT.__objc_methlist: 0x3042c
-  __TEXT.__cstring: 0x35e63
-  __TEXT.__const: 0xac772
+  __TEXT.__objc_methlist: 0x3043c
+  __TEXT.__cstring: 0x36d93
+  __TEXT.__const: 0x11ff02
   __TEXT.__oslogstring: 0xc773
-  __TEXT.__gcc_except_tab: 0x4298
+  __TEXT.__gcc_except_tab: 0x42a4
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x644
   __TEXT.__constg_swiftt: 0x3064

   __TEXT.__unwind_info: 0xfe98
   __TEXT.__eh_frame: 0x4628
   __TEXT.__objc_classname: 0x8aba
-  __TEXT.__objc_methname: 0x5f813
-  __TEXT.__objc_methtype: 0xc049
+  __TEXT.__objc_methname: 0x5f832
+  __TEXT.__objc_methtype: 0xc065
   __TEXT.__objc_stubs: 0x2c000
   __DATA_CONST.__got: 0x1b68
-  __DATA_CONST.__const: 0xf6e0
+  __DATA_CONST.__const: 0x10ae0
   __DATA_CONST.__objc_classlist: 0x1ae8
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x808
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11908
+  __DATA_CONST.__objc_selrefs: 0x11910
   __DATA_CONST.__objc_protorefs: 0x618
   __DATA_CONST.__objc_superrefs: 0x1740
   __DATA_CONST.__objc_arraydata: 0x6968
   __AUTH_CONST.__auth_got: 0x1be0
   __AUTH_CONST.__const: 0xc700
   __AUTH_CONST.__cfstring: 0x32b20
-  __AUTH_CONST.__objc_const: 0x50b08
+  __AUTH_CONST.__objc_const: 0x50b10
   __AUTH_CONST.__objc_intobj: 0x4620
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F7871108-1A8B-3F32-BA95-F70FE1DCE7F8
+  UUID: 77BB244E-87CB-34C4-9E02-C790A25123F9
   Functions: 24376
   Symbols:   61508
-  CStrings:  30267
+  CStrings:  30589
 
Symbols:
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.397
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.398
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.318
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.326
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.319
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.319.cold.1
+ ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.387
+ ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.403
+ ___33-[HKHealthStore dropEntitlement:]_block_invoke.641
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.542
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.542.cold.1
+ ___36-[HKHealthStore restoreEntitlement:]_block_invoke.642
+ ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.414
+ ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.660
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.559
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.559.cold.1
+ ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.661
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.516
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.517
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.560
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.560.cold.1
+ ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.385
+ ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.430
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.602
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.602.cold.1
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.312
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.313
+ ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.615
+ ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.399
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.635
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.521
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.522
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.578
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.578.cold.1
+ ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.401
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.620
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.620.cold.1
+ ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.426
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.316
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.317
+ ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.415
+ ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.434
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.654
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.381
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.382
+ ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.441
+ ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.449
+ ___block_literal_global.315
+ ___block_literal_global.339
+ ___block_literal_global.354
+ ___block_literal_global.438
+ ___block_literal_global.446
+ ___block_literal_global.453
+ ___block_literal_global.480
+ ___block_literal_global.488
+ ___block_literal_global.495
+ ___block_literal_global.503
+ ___block_literal_global.544
+ ___block_literal_global.546
+ ___block_literal_global.548
+ ___block_literal_global.562
+ ___block_literal_global.564
+ ___block_literal_global.566
+ ___block_literal_global.577
+ ___block_literal_global.585
+ ___block_literal_global.591
+ ___block_literal_global.601
+ ___block_literal_global.603
+ ___block_literal_global.604
+ ___block_literal_global.609
+ ___block_literal_global.620
+ ___block_literal_global.622
+ ___block_literal_global.624
+ ___block_literal_global.626
+ ___block_literal_global.637
+ ___block_literal_global.639
+ ___block_literal_global.641
+ ___block_literal_global.643
+ ___block_literal_global.645
+ ___block_literal_global.649
+ ___block_literal_global.651
+ ___block_literal_global.656
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.388
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.389
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.309
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.317
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310.cold.1
- ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.378
- ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.394
- ___33-[HKHealthStore dropEntitlement:]_block_invoke.632
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.533
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.533.cold.1
- ___36-[HKHealthStore restoreEntitlement:]_block_invoke.633
- ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.405
- ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.651
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550.cold.1
- ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.652
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.507
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.508
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551.cold.1
- ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.376
- ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.421
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593.cold.1
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.303
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.304
- ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.606
- ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.390
- ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.626
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.512
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.513
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569.cold.1
- ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.392
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611.cold.1
- ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.417
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.307
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.308
- ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.406
- ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.425
- ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.645
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.372
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.373
- ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.432
- ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.440
- ___block_literal_global.306
- ___block_literal_global.330
- ___block_literal_global.345
- ___block_literal_global.429
- ___block_literal_global.437
- ___block_literal_global.444
- ___block_literal_global.471
- ___block_literal_global.479
- ___block_literal_global.486
- ___block_literal_global.494
- ___block_literal_global.535
- ___block_literal_global.537
- ___block_literal_global.539
- ___block_literal_global.541
- ___block_literal_global.553
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.576
- ___block_literal_global.582
- ___block_literal_global.592
- ___block_literal_global.594
- ___block_literal_global.595
- ___block_literal_global.600
- ___block_literal_global.610
- ___block_literal_global.611
- ___block_literal_global.613
- ___block_literal_global.615
- ___block_literal_global.617
- ___block_literal_global.621
- ___block_literal_global.623
- ___block_literal_global.634
- ___block_literal_global.636
- ___block_literal_global.638
- ___block_literal_global.640
- ___block_literal_global.642
Functions:
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em : 60 -> 64
~ -[_HKZipArchiveEntry _getDataWithBufferingWithMaxSizeBytes:error:] : 328 -> 348
~ __ZN2PB9PtrVectorIN12binarysample21ElectrocardiogramLeadEE12emplace_backIJKS2_EEEvDpOT_ : 340 -> 344
~ __ZNSt3__16__treeINS_12__value_typeIN12binarysample26ElectrocardiogramLead_NameENS2_21ElectrocardiogramLeadEEENS_19__map_value_compareIS3_S5_NS_4lessIS3_EELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS3_JRKNS_21piecewise_construct_tENS_5tupleIJRKS3_EEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 244 -> 252
~ __ZN2PB9PtrVectorIN12binarysample21ElectrocardiogramLeadEE12emplace_backIJRKS2_EEEvDpOT_ : 340 -> 344
~ __ZN2PB9PtrVectorIN12binarysample21ElectrocardiogramLeadEE12emplace_backIJEEEvDpOT_ : 332 -> 336
~ +[HKImportExclusionDeviceDataSource(HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysisAllowedDeviceSerialNumbers) isDeviceSerialNumberOnAllowedListForHKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis:] : 644 -> 656
~ __ZNKSt3__120__shared_ptr_pointerIPNS_13__empty_stateIcEENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 376 -> 380
~ __ZNSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPNS_7__stateIcEENS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_ : 268 -> 272
~ -[HKEADFFileParser newBuilderWithStartDate:] : 572 -> 592
~ sub_191d0df3c -> sub_191cf0f9c : 56 -> 48
~ sub_191d0df74 -> sub_191cf0fcc : 196 -> 204
~ -[HKFeatureStatusManager _queue_unregisterForFeatureStatusChanges] : 68 -> 76
~ -[HKActiveDataCollectionObserver _restartTaskServerIfNeeded] : 124 -> 136
~ -[HKOntologyShardRegistryEntry _copy] : 144 -> 140
~ -[_HKMappingKey objectMatches:] : 128 -> 124
~ -[HKUnitPreferenceController _initHKUnitPreferencesWithCompletion:] : 128 -> 140
~ -[_HKStateOfMindComparisonFilter _acceptsStateOfMindWithReflectiveInterval:] : 256 -> 252
~ -[_HKStateOfMindComparisonFilter _acceptsStateOfMindWithValence:] : 256 -> 252
~ -[HKBluetoothDeviceDataSource _endDiscovery] : 120 -> 132
~ -[HKFeatureAvailabilityRequirementEntitlement typeDescription] : 64 -> 60
CStrings:
+ "230BOCKB0001"
+ "230BOCKB0002"
+ "230BOCKB0003"
+ "230BOCKB0004"
+ "230BOCKB0005"
+ "230BOCKB0006"
+ "230BOCKB0007"
+ "230BOCKB0008"
+ "230BOCKB0009"
+ "230BOCKB0010"
+ "230BOCKB0011"
+ "230BOCKB0012"
+ "230BOCKB0013"
+ "230BOCKB0014"
+ "230BOCKB0015"
+ "230BOCKB0016"
+ "230BOCKB0017"
+ "230BOCKB0018"
+ "230BOCKB0019"
+ "230BOCKB0020"
+ "230BOCKB0021"
+ "230BOCKB0022"
+ "230BOCKB0023"
+ "230BOCKB0024"
+ "230BOCKB0025"
+ "230BOCKB0026"
+ "230BOCKB0027"
+ "230BOCKB0028"
+ "230BOCKB0029"
+ "230BOCKB0030"
+ "230BOCKB0031"
+ "230BOCKB0032"
+ "230BOCKB0033"
+ "230BOCKB0034"
+ "230BOCKB0036"
+ "230BOCKB0037"
+ "230BOCKB0038"
+ "230BOCKB0039"
+ "230BOCKB0040"
+ "230BOCKB0041"
+ "230BOCKB0042"
+ "230BOCKB0043"
+ "230BOCKB0044"
+ "230BOCKB0045"
+ "230BOCKB0046"
+ "230BOCKB0047"
+ "230BOCKB0048"
+ "230BOCKB0049"
+ "230BOCKB0050"
+ "230BOCKB0051"
+ "230BOCKB0052"
+ "230BOCKB0053"
+ "230BOCKB0054"
+ "230BOCKB0055"
+ "230BOCKB0056"
+ "230BOCKB0057"
+ "230BOCKB0058"
+ "230BOCKB0059"
+ "230BOCKB0060"
+ "230BOCKB0061"
+ "230BOCKB0062"
+ "230BOCKB0063"
+ "230BOCKB0064"
+ "230BOCKB0065"
+ "230BOCKB0066"
+ "230BOCKB0067"
+ "230BOCKB0068"
+ "230BOCKB0069"
+ "230BOCKB0070"
+ "230BOCKB0071"
+ "230BOCKB0072"
+ "230BOCKB0073"
+ "230BOCKB0074"
+ "230BOCKB0075"
+ "230BOCKB0076"
+ "230BOCKB0077"
+ "230BOCKB0078"
+ "230BOCKB0079"
+ "230BOCKB0080"
+ "230BOCKB0081"
+ "230BOCKB0082"
+ "230BOCKB0083"
+ "230BOCKB0084"
+ "230BOCKB0085"
+ "230BOCKB0086"
+ "230BOCKB0087"
+ "230BOCKB0088"
+ "230BOCKB0089"
+ "230BOCKB0090"
+ "230BOCKB0091"
+ "230BOCKB0092"
+ "230BOCKB0093"
+ "230BOCKB0094"
+ "230BOCKB0095"
+ "230BOCKB0096"
+ "230BOCKB0097"
+ "230BOCKB0098"
+ "230BOCKB0099"
+ "230BOCKB0100"
+ "230BOCKB0101"
+ "230BOCKB0102"
+ "230BOCKB0103"
+ "230BOCKB0104"
+ "230BOCKB0105"
+ "230BOCKB0106"
+ "230BOCKB0107"
+ "230BOCKB0108"
+ "230BOCKB0109"
+ "230BOCKB0110"
+ "230BOCKB0111"
+ "230BOCKB0112"
+ "230BOCKB0113"
+ "230BOCKB0114"
+ "230BOCKB0115"
+ "230BOCKB0116"
+ "230BOCKB0117"
+ "230BOCKB0118"
+ "230BOCKB0119"
+ "230BOCKB0120"
+ "230BOCKB0121"
+ "230BOCKB0122"
+ "230BOCKB0123"
+ "230BOCKB0124"
+ "230BOCKB0125"
+ "230BOCKB0126"
+ "230BOCKB0127"
+ "230BOCKB0128"
+ "230BOCKB0129"
+ "230BOCKB0130"
+ "230BOCKB0131"
+ "230BOCKB0132"
+ "230BOCKB0133"
+ "230BOCKB0134"
+ "230BOCKB0135"
+ "230BOCKB0136"
+ "230BOCKB0137"
+ "230BOCKB0138"
+ "230BOCKB0139"
+ "230BOCKB0140"
+ "230BOCKB0141"
+ "230BOCKB0142"
+ "230BOCKB0143"
+ "230BOCKB0144"
+ "230BOCKB0145"
+ "230BOCKB0146"
+ "230BOCKB0149"
+ "230BOCKB0151"
+ "230BOCKB0152"
+ "230BOCKB0154"
+ "230BOCKB0156"
+ "230BOCKB0162"
+ "230BOCKB0165"
+ "230BOCKB0167"
+ "230BOCKB0168"
+ "230BOCKB0179"
+ "230BOCKB0183"
+ "230BOCKB0185"
+ "230BOCKB0192"
+ "230BOCKB0194"
+ "230BOCKB0195"
+ "230BOCKB0196"
+ "230BOCKB0198"
+ "230BOCKB0199"
+ "230BOCKB0200"
+ "230BOCKB0201"
+ "230BOCKB0205"
+ "230BOCKB0208"
+ "230BOCKB0211"
+ "230BOCKB0212"
+ "230BOCKB0213"
+ "230BOCKB0215"
+ "230BOCKB0217"
+ "230BOCKB0218"
+ "230BOCKB0219"
+ "230BOCKB0220"
+ "230DCB0001"
+ "230DCB0002"
+ "230DCB0003"
+ "230DCB0004"
+ "230DCB0005"
+ "230DCB0006"
+ "230DCB0007"
+ "230DCB0008"
+ "230DCB0009"
+ "230DCB0010"
+ "230DCB0011"
+ "230DCB0012"
+ "230DCB0013"
+ "230DCB0014"
+ "230DCB0015"
+ "230DCB0016"
+ "230DCB0017"
+ "230DCB0018"
+ "230DCB0019"
+ "230DCB0020"
+ "230DCB0021"
+ "230DCB0022"
+ "230DCB0023"
+ "230DCB0024"
+ "230DCB0025"
+ "230DCB0026"
+ "230DCB0027"
+ "230DCB0028"
+ "230DCB0029"
+ "230DCB0030"
+ "230DCB0031"
+ "230DCB0032"
+ "230DCB0033"
+ "230DCB0034"
+ "230DCB0035"
+ "230DCB0036"
+ "230DCB0037"
+ "230DCB0038"
+ "230DCB0039"
+ "230DCB0040"
+ "230DCB0041"
+ "230DCB0042"
+ "230DCB0043"
+ "230DCB0044"
+ "230DCB0045"
+ "230DCB0046"
+ "230DCB0047"
+ "230DCB0048"
+ "230DCB0049"
+ "230DCB0050"
+ "230DCB0051"
+ "230DCB0052"
+ "230DCB0053"
+ "230DCB0054"
+ "230DCB0055"
+ "230DCB0056"
+ "230DCB0057"
+ "230DCB0058"
+ "230DCB0059"
+ "230DCB0060"
+ "230DCB0061"
+ "230DCB0062"
+ "230DCB0063"
+ "230DCB0064"
+ "230DCB0065"
+ "230DCB0066"
+ "230DCB0067"
+ "230DCB0068"
+ "230DCB0069"
+ "230DCB0070"
+ "230DCB0071"
+ "230DCB0072"
+ "230DCB0074"
+ "230DCB0076"
+ "230DCB0078"
+ "230DCB0079"
+ "230DCB0080"
+ "230DCB0081"
+ "230DCB0083"
+ "230DCB0087"
+ "230DCB0089"
+ "230DCB0090"
+ "230DCB0094"
+ "230DCB0095"
+ "230DCB0096"
+ "230DCB0099"
+ "230DCB0101"
+ "230DCB0103"
+ "230DCB0104"
+ "230DCB0105"
+ "230DCB0106"
+ "230DCB0107"
+ "230DCB0109"
+ "230DCB0112"
+ "230DCB0113"
+ "230DCB0114"
+ "230DCB0115"
+ "230DCB0116"
+ "230DCB0117"
+ "230DCB0121"
+ "230DCB0123"
+ "230DCB0124"
+ "230DCB0127"
+ "230DCB0128"
+ "230DCB0129"
+ "230DCB0131"
+ "230DCB0132"
+ "230DCB0133"
+ "230DCB0136"
+ "230DCB0139"
+ "230DCB0140"
+ "230DCB0141"
+ "230DCB0142"
+ "230DCB0143"
+ "230DCB0145"
+ "230DCB0146"
+ "230DCB0147"
+ "230DCB0149"
+ "230DCB0150"
+ "230DCB0151"
+ "230DCB0152"
+ "230DCB0154"
+ "230DCB0155"
+ "230DCB0156"
+ "230DCB0157"
+ "230DCB0158"
+ "230DCB0159"
+ "230DCB0160"
+ "230DCB0161"
+ "230DCB0162"
+ "230DCB0163"
+ "230DCB0164"
+ "230DCB0165"
+ "230DCB0166"
+ "230DCB0167"
+ "230DCB0168"
+ "230DCB0169"
+ "230DCB0170"
+ "230DCB0171"
+ "230DCB0172"
+ "230DCB0173"
+ "230DCB0176"
+ "230DCB0177"
+ "230DCB0178"
+ "230DCB0179"
+ "230DCB0180"
+ "applicationsDidUpdateMetadata:"
+ "v64@0:8{Electrocardiogram=^^?d{PtrVector<binarysample::ElectrocardiogramLead>={vector<std::unique_ptr<binarysample::ElectrocardiogramLead>, std::allocator<std::unique_ptr<binarysample::ElectrocardiogramLead>>>=^v^v{?=^v}}}{?=b1}}16"
+ "{Electrocardiogram=\"_vptr$Base\"^^?\"_frequency\"d\"_leads\"{PtrVector<binarysample::ElectrocardiogramLead>=\"_v\"{vector<std::unique_ptr<binarysample::ElectrocardiogramLead>, std::allocator<std::unique_ptr<binarysample::ElectrocardiogramLead>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}}\"_has\"{?=\"frequency\"b1}}"
+ "{map<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead, std::less<binarysample::ElectrocardiogramLead_Name>, std::allocator<std::pair<const binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>>>=\"__tree_\"{__tree<std::__value_type<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>, std::__map_value_compare<binarysample::ElectrocardiogramLead_Name, std::__value_type<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>, std::less<binarysample::ElectrocardiogramLead_Name>>, std::allocator<std::__value_type<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unique_ptr<HKIntervalTree<double>, std::default_delete<HKIntervalTree<double>>>=\"\"{?=\"__ptr_\"^v}}"
- "v64@0:8{Electrocardiogram=^^?d{PtrVector<binarysample::ElectrocardiogramLead>={vector<std::unique_ptr<binarysample::ElectrocardiogramLead>, std::allocator<std::unique_ptr<binarysample::ElectrocardiogramLead>>>=^v^v^v}}{?=b1}}16"
- "{Electrocardiogram=\"_vptr$Base\"^^?\"_frequency\"d\"_leads\"{PtrVector<binarysample::ElectrocardiogramLead>=\"_v\"{vector<std::unique_ptr<binarysample::ElectrocardiogramLead>, std::allocator<std::unique_ptr<binarysample::ElectrocardiogramLead>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}}\"_has\"{?=\"frequency\"b1}}"
- "{map<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead, std::less<binarysample::ElectrocardiogramLead_Name>, std::allocator<std::pair<const binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>>>=\"__tree_\"{__tree<std::__value_type<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>, std::__map_value_compare<binarysample::ElectrocardiogramLead_Name, std::__value_type<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>, std::less<binarysample::ElectrocardiogramLead_Name>>, std::allocator<std::__value_type<binarysample::ElectrocardiogramLead_Name, binarysample::ElectrocardiogramLead>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unique_ptr<HKIntervalTree<double>, std::default_delete<HKIntervalTree<double>>>=\"__ptr_\"^v}"

```
