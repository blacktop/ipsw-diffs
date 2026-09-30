## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial`

```diff

-429.0.4.6.0
-  __TEXT.__text: 0x85d08
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__delay_helper: 0x190
-  __TEXT.__objc_methlist: 0x6538
-  __TEXT.__const: 0xf2a
-  __TEXT.__gcc_except_tab: 0x54c0
-  __TEXT.__cstring: 0x9634
-  __TEXT.__oslogstring: 0x4912
+429.20.0.0.0
+  __TEXT.__text: 0x87c78
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__delay_helper: 0x258
+  __TEXT.__objc_methlist: 0x71f0
+  __TEXT.__const: 0xf0a
   __TEXT.__dlopen_cstrs: 0x101
+  __TEXT.__gcc_except_tab: 0x5568
+  __TEXT.__cstring: 0x9bc1
+  __TEXT.__oslogstring: 0x4be6
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x26a8
+  __TEXT.__unwind_info: 0x26b8
   __TEXT.__objc_classname: 0x13e5
-  __TEXT.__objc_methname: 0xe602
-  __TEXT.__objc_methtype: 0x2e46
-  __TEXT.__objc_stubs: 0x9d00
-  __DATA_CONST.__got: 0x850
-  __DATA_CONST.__const: 0x8c8
+  __TEXT.__objc_methname: 0xeb06
+  __TEXT.__objc_methtype: 0x2e66
+  __TEXT.__objc_stubs: 0x9fe0
+  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__const: 0x8e8
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3358
+  __DATA_CONST.__objc_selrefs: 0x36b0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0x2628
-  __AUTH_CONST.__cfstring: 0x7320
-  __AUTH_CONST.__objc_const: 0xde88
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__const: 0x26e8
+  __AUTH_CONST.__cfstring: 0x7640
+  __AUTH_CONST.__objc_const: 0xc9f8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2580
-  __DATA.__objc_ivar: 0x6f4
-  __DATA.__data: 0xdc0
+  __DATA.__objc_ivar: 0x708
+  __DATA.__data: 0xdc8
   __DATA.__bss: 0x348
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc30

   - /System/Library/PrivateFrameworks/AppleFlatBuffers.framework/Versions/A/AppleFlatBuffers
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5B384580-F3BA-33EE-8120-769B018DA8E7
-  Functions: 2580
-  Symbols:   6666
-  CStrings:  5128
+  UUID: F8016A73-11EE-30D8-894B-7496BAF5219E
+  Functions: 2595
+  Symbols:   6744
+  CStrings:  5226
 
Symbols:
+ +[TRIClient clientWithExperimentIdentifiers:]
+ +[TRIPartialExperimentRecord recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:]
+ +[TRISystemInfo _appleIntelligenceState]
+ -[NSMutableArray(TRI) triRemoveFirstItemPassingTest:]
+ -[NSString(TRI) triParseJson]
+ -[TRIActiveFactorProvidersParser _deploymentIdForExperiment:fromResolverList:]
+ -[TRIActiveFactorProvidersParser _experimentIdForNamespace:fromResolverList:]
+ -[TRIActiveFactorProvidersParser _resolveCounterfactualTreatmentsMap]
+ -[TRIActiveFactorProvidersParser _resolveTreatmentFactorPackSetIdMap]
+ -[TRIActiveFactorProvidersParser _treatmentIdForExperiment:fromResolverList:]
+ -[TRIActiveFactorProvidersParser counterfactualFactorsStatesForNamespace:]
+ -[TRIActiveFactorProvidersParser experimentIdentifiersForNamespace:]
+ -[TRIActiveFactorProvidersParser resolveTargetedFactorPackSetForExperimentFactorsState:]
+ -[TRIClient enumerateCounterfactualsWithNamespace:error:usingBlock:]
+ -[TRIClient hasCounterfactualsForNamespace:]
+ -[TRIDefaultFactorProvider _experimentDeploymentFromActiveFactorProviderWithNamespaceName:]
+ -[TRIDefaultFactorProvider _treatmentIdFromActiveFactorProviderWithNamespaceName:]
+ -[TRIDefaultFactorProvider counterfactualFactorsStatesForNamespace:]
+ -[TRIExperimentIdentifiers asFactorsState]
+ -[TRINamespaceResolver _hasCounterfactualFactorsState]
+ -[TRINamespaceResolver _prepareFactorsStateForCounterfactualsForFactorsState:]
+ -[TRINamespaceResolver counterfactualFactorsStatesForNamespace:]
+ -[TRINamespaceResolver experimentFactorsStateForCounterfactuals]
+ -[TRINamespaceResolver experimentIdentifiersForNamespace:]
+ -[TRIPartialExperimentRecord copyWithReplacementCounterfactualTreatmentIds:]
+ -[TRIPartialExperimentRecord counterfactualTreatmentIds]
+ -[TRIPartialExperimentRecord initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:]
+ -[TRISystemConfiguration appleIntelligenceState]
+ -[TRISystemInfo appleIntelligenceState]
+ -[TRISystemInfo setAppleIntelligenceState:]
+ GCC_except_table43
+ GCC_except_table567
+ GCC_except_table578
+ GCC_except_table590
+ GCC_except_table600
+ GCC_except_table618
+ GCC_except_table627
+ GCC_except_table637
+ GCC_except_table646
+ GCC_except_table656
+ GCC_except_table665
+ GCC_except_table675
+ OBJC_IVAR_$_TRIActiveFactorProvidersParserGuardedData.counterfactualFactorPackDeploymentMap
+ OBJC_IVAR_$_TRIExternalParameterManager._dispatchQueue
+ OBJC_IVAR_$_TRINamespaceResolver._experimentFactorsStateForCounterfactuals
+ OBJC_IVAR_$_TRIPartialExperimentRecord._counterfactualTreatmentIds
+ OBJC_IVAR_$_TRISystemInfo._appleIntelligenceState
+ _OBJC_CLASS_$_GMAvailabilityWrapper
+ __100+[TRIFlatbufferUtils convertFBFactorLevelToProtoFactorLevel:parentDir:namespaceName:isRelativePath:]_block_invoke.13
+ __101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.189
+ __101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.190
+ __109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.201
+ __119-[TRIFPNamespaceFactorProvider _factorLevelsWithFactorPackData:referencePath:outFactorPackId:outNamespaceName:outNCVs:]_block_invoke.42
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.176
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.177
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.181
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.184
+ __131-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:]_block_invoke.173
+ __139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.232
+ __139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.233
+ __139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.234
+ __150-[TRIXPCNamespaceManagementClient registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:error:]_block_invoke.162
+ __203+[TRIFactorDownloadValidator validateDownloadForFactors:withNamespace:paths:container:factorsState:assetIndexesByTreatment:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:error:]_block_invoke.102
+ __203+[TRIFactorDownloadValidator validateDownloadForFactors:withNamespace:paths:container:factorsState:assetIndexesByTreatment:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:error:]_block_invoke.105
+ __218-[TRINamespaceFactorProviderChain computeTreatmentAssetIndexes:withAssociatedExperimentIds:andFactorPackAssetIds:withAssociatedRolloutDeployments:withExperimentFactorNames:andRolloutFactorNames:forFactors:usingFilter:]_block_invoke.130
+ __50+[TRICPrinter printTabularWithLogDefaultForLines:]_block_invoke.19
+ __56-[TRIClientFactorPackStreamingWriter appendFactorLevel:]_block_invoke.96
+ __61-[TRINamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke.101
+ __62-[TRIPruningFactorLevelCache enumerateFactorLevelsUsingBlock:]_block_invoke.50
+ __63-[TRIClient sizesForFactors:withNamespaceName:forMetric:error:]_block_invoke.280
+ __63-[TRIFPNamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke.49
+ __63-[TRIFPNamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke.51
+ __67-[TRIClient downloadNamespaceWithName:options:progress:completion:]_block_invoke.269
+ __72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.33
+ __72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.35
+ __73-[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]_block_invoke.25
+ __73-[TRIEvaluationStatusDefaultProvider enumerateActiveBMLTWithError:block:]_block_invoke.98
+ __74-[TRIActiveFactorProvidersParser counterfactualFactorsStatesForNamespace:]_block_invoke.180
+ __74-[TRIActiveFactorProvidersParser counterfactualFactorsStatesForNamespace:]_block_invoke.181
+ __75-[TRIAllocationStatusDefaultProvider activeExperimentInformationWithError:]_block_invoke.188
+ __80-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]_block_invoke.9
+ __86-[TRIClient statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:]_block_invoke.326
+ __86-[TRIClient statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:]_block_invoke.332
+ __87-[TRIAllocationStatusDefaultProvider addStatusUpdateHandlerForEnvironment:queue:block:]_block_invoke.199
+ __91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke.17
+ __91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke.18
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__function12__value_funcIFN5apple4aiml12flatbuffers26OffsetIvEEmEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvmP10BoxedInt64EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvmP11BoxedDoubleEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvmP9BoxedBoolEED2B8ne190102Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__125__throw_bad_function_callB8ne190102Ev
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEjT1_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_SD_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___125-[TRINamespaceResolver resolveFactorProviderChainForNamespaceName:faultOnMissingInstalledFactors:installedFactorsAccessible:]_block_invoke_2
+ ___41-[TRIActiveFactorProvidersParser dispose]_block_invoke_4
+ ___68-[TRIDefaultFactorProvider counterfactualFactorsStatesForNamespace:]_block_invoke
+ ___69-[TRIActiveFactorProvidersParser _resolveTreatmentFactorPackSetIdMap]_block_invoke
+ ___74-[TRIActiveFactorProvidersParser counterfactualFactorsStatesForNamespace:]_block_invoke
+ ___82-[TRIDefaultFactorProvider _treatmentIdFromActiveFactorProviderWithNamespaceName:]_block_invoke
+ ___88-[TRIActiveFactorProvidersParser resolveTargetedFactorPackSetForExperimentFactorsState:]_block_invoke
+ ___91-[TRIDefaultFactorProvider _experimentDeploymentFromActiveFactorProviderWithNamespaceName:]_block_invoke
+ ___block_descriptor_32_e66_v32?0"TRIExperimentFactorsState"8"TRILockedFactorPackSet"16^B24l
+ ___block_descriptor_48_e8_32s40r_e45_v16?0"TRIDefaultFactorProviderGuardedData"8l
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSString"16^B24l
+ ___block_descriptor_56_e8_32s40r48r_e51_v16?0"TRIActiveFactorProvidersParserGuardedData"8l
+ ___block_descriptor_56_e8_32s40r_e39_v32?0"TRITypedFactorProvider"8Q16^B24l
+ ___block_descriptor_80_e8_32s40bs48r56r_e42_B32?0"NSString"8"TRIFile"16"NSError"24l
+ __block_literal_global.106
+ __block_literal_global.109
+ __block_literal_global.110
+ __block_literal_global.112
+ __block_literal_global.114
+ __block_literal_global.13
+ __block_literal_global.144
+ __block_literal_global.152
+ __block_literal_global.160
+ __block_literal_global.164
+ __block_literal_global.179
+ __block_literal_global.181
+ __block_literal_global.184
+ __block_literal_global.195
+ __block_literal_global.198
+ __block_literal_global.201
+ __block_literal_global.21
+ __block_literal_global.23
+ __block_literal_global.277
+ __block_literal_global.282
+ __block_literal_global.30
+ __block_literal_global.307
+ __block_literal_global.328
+ __block_literal_global.335
+ __block_literal_global.35
+ __block_literal_global.497
+ __block_literal_global.541
+ __block_literal_global.547
+ __block_literal_global.558
+ __block_literal_global.74
+ __block_literal_global.75
+ __block_literal_global.91
+ _dlopenHelper$GenerativeModels
+ _dlopenHelperFlag$GenerativeModels
+ _gotLoadHelper_x8$_OBJC_CLASS_$_GMAvailabilityWrapper
+ _objc_msgSend$_appleIntelligenceState
+ _objc_msgSend$_deploymentIdForExperiment:fromResolverList:
+ _objc_msgSend$_experimentDeploymentFromActiveFactorProviderWithNamespaceName:
+ _objc_msgSend$_experimentIdForNamespace:fromResolverList:
+ _objc_msgSend$_hasCounterfactualFactorsState
+ _objc_msgSend$_prepareFactorsStateForCounterfactualsForFactorsState:
+ _objc_msgSend$_resolveCounterfactualTreatmentsMap
+ _objc_msgSend$_resolveTreatmentFactorPackSetIdMap
+ _objc_msgSend$_treatmentIdForExperiment:fromResolverList:
+ _objc_msgSend$_treatmentIdFromActiveFactorProviderWithNamespaceName:
+ _objc_msgSend$appleIntelligenceState
+ _objc_msgSend$asFactorsState
+ _objc_msgSend$clientWithProjectId:factorsState:
+ _objc_msgSend$counterfactualFactorsStatesForNamespace:
+ _objc_msgSend$counterfactualTreatmentIds
+ _objc_msgSend$currentWithUseCaseIdentifiers:
+ _objc_msgSend$deploymentWithExperimentId:deploymentId:
+ _objc_msgSend$experimentFactorsStateForCounterfactuals
+ _objc_msgSend$experimentIdentifiersForNamespace:
+ _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:
+ _objc_msgSend$resolveTargetedFactorPackSetForExperimentFactorsState:
+ _objc_msgSend$setAppleIntelligenceState:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$triRemoveFirstItemPassingTest:
- +[TRIPartialExperimentRecord recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:]
- -[TRIPartialExperimentRecord initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:]
- GCC_except_table30
- GCC_except_table569
- GCC_except_table580
- GCC_except_table592
- GCC_except_table602
- GCC_except_table620
- GCC_except_table629
- GCC_except_table639
- GCC_except_table648
- GCC_except_table658
- GCC_except_table667
- GCC_except_table677
- __100+[TRIFlatbufferUtils convertFBFactorLevelToProtoFactorLevel:parentDir:namespaceName:isRelativePath:]_block_invoke.7
- __101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.183
- __101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.184
- __109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.195
- __119-[TRIFPNamespaceFactorProvider _factorLevelsWithFactorPackData:referencePath:outFactorPackId:outNamespaceName:outNCVs:]_block_invoke.36
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.170
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.171
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.175
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.178
- __131-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:]_block_invoke.167
- __139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.220
- __139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.221
- __139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.222
- __150-[TRIXPCNamespaceManagementClient registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:error:]_block_invoke.156
- __203+[TRIFactorDownloadValidator validateDownloadForFactors:withNamespace:paths:container:factorsState:assetIndexesByTreatment:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:error:]_block_invoke.90
- __203+[TRIFactorDownloadValidator validateDownloadForFactors:withNamespace:paths:container:factorsState:assetIndexesByTreatment:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:error:]_block_invoke.93
- __218-[TRINamespaceFactorProviderChain computeTreatmentAssetIndexes:withAssociatedExperimentIds:andFactorPackAssetIds:withAssociatedRolloutDeployments:withExperimentFactorNames:andRolloutFactorNames:forFactors:usingFilter:]_block_invoke.118
- __50+[TRICPrinter printTabularWithLogDefaultForLines:]_block_invoke.13
- __56-[TRIClientFactorPackStreamingWriter appendFactorLevel:]_block_invoke.90
- __61-[TRINamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke.95
- __62-[TRIPruningFactorLevelCache enumerateFactorLevelsUsingBlock:]_block_invoke.44
- __63-[TRIClient sizesForFactors:withNamespaceName:forMetric:error:]_block_invoke.268
- __63-[TRIFPNamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke.43
- __63-[TRIFPNamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke.45
- __67-[TRIClient downloadNamespaceWithName:options:progress:completion:]_block_invoke.257
- __72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.25
- __72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.27
- __73-[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]_block_invoke.19
- __73-[TRIEvaluationStatusDefaultProvider enumerateActiveBMLTWithError:block:]_block_invoke.92
- __75-[TRIAllocationStatusDefaultProvider activeExperimentInformationWithError:]_block_invoke.182
- __80-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]_block_invoke.5
- __86-[TRIClient statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:]_block_invoke.314
- __86-[TRIClient statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:]_block_invoke.320
- __87-[TRIAllocationStatusDefaultProvider addStatusUpdateHandlerForEnvironment:queue:block:]_block_invoke.193
- __91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke.13
- __91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke.14
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9exception4whatEv
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__function12__value_funcIFN5apple4aiml12flatbuffers26OffsetIvEEmEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvmP10BoxedInt64EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvmP11BoxedDoubleEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvmP9BoxedBoolEED2B8ne180100Ev
- __ZNSt3__117bad_function_callD0Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__125__throw_bad_function_callB8ne180100Ev
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEjT1_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_SD_T0_
- __ZNSt9exceptionD2Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZTSNSt3__117bad_function_callE
- ___block_descriptor_64_e8_32s40bs48r56r_e42_B32?0"NSString"8"TRIFile"16"NSError"24l
- __block_literal_global.100
- __block_literal_global.102
- __block_literal_global.134
- __block_literal_global.136
- __block_literal_global.138
- __block_literal_global.158
- __block_literal_global.161
- __block_literal_global.17
- __block_literal_global.175
- __block_literal_global.186
- __block_literal_global.189
- __block_literal_global.24
- __block_literal_global.265
- __block_literal_global.270
- __block_literal_global.29
- __block_literal_global.295
- __block_literal_global.316
- __block_literal_global.323
- __block_literal_global.479
- __block_literal_global.523
- __block_literal_global.529
- __block_literal_global.540
- __block_literal_global.68
- __block_literal_global.69
- __block_literal_global.7
- __block_literal_global.85
- __block_literal_global.90
- __block_literal_global.93
- __block_literal_global.98
- _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:
CStrings:
+ "       - %@"
+ "      counterfactualTreatments:"
+ "/System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels"
+ "<TRIPartialExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ isShadow:%@ counterfactualTreatmentIds:%@>"
+ "@\"TRIExperimentFactorsState\""
+ "@92@0:8i16@20@28@36i44q48@56@64@72B80@84"
+ "Active factor provider does not contain experiment for %@:"
+ "Could not resolve to experiment deployment. Attempting to read from active factor provider."
+ "Could not resolve to treatment id. Attempting to read from active factor provider."
+ "Counterfactuals treatments mapping does not exist in plplist: %@"
+ "Error: systemInfo is null."
+ "Failed to resolve targeted experiment factor pack set for factor state: %@. This is expected if this is for investigations and not counterfactuals."
+ "JSON from trialtool with --json flag was not a valid json object: %@"
+ "No FPS ID found trying to resolve factors state %@"
+ "No active factor provider found or it is empty."
+ "Retrieved nil serialized value for nonnull TRIPartialExperimentRecord.counterfactualTreatmentIds"
+ "Skipping counterfactual due to not having a treatment ID: %@"
+ "String output with from trialtool was not a valid UTF-8 string"
+ "T@\"NSArray\",R,N,V_counterfactualTreatmentIds"
+ "T@\"TRIExperimentFactorsState\",R,N,V_experimentFactorsStateForCounterfactuals"
+ "TRIFactorDownloadValidator.m"
+ "Tq,N,V_appleIntelligenceState"
+ "Treatment to FPS mapping not present in plplist"
+ "TrialXP-429.20"
+ "Unable to resolve factor pack set path %@"
+ "Unarchived unexpected class for TRIPartialExperimentRecord key \"counterfactualTreatmentIds\" (expected %@, decoded %@)"
+ "[_activeFactorProvidersParser counterfactualFactorsStatesForNamespace:namespaceName]"
+ "_appleIntelligenceState"
+ "_counterfactualTreatmentIds"
+ "_deploymentIdForExperiment:fromResolverList:"
+ "_experimentDeploymentFromActiveFactorProviderWithNamespaceName:"
+ "_experimentFactorsStateForCounterfactuals"
+ "_experimentIdForNamespace:fromResolverList:"
+ "_hasCounterfactualFactorsState"
+ "_prepareFactorsStateForCounterfactualsForFactorsState:"
+ "_resolveCounterfactualTreatmentsMap"
+ "_resolveTreatmentFactorPackSetIdMap"
+ "_treatmentIdForExperiment:fromResolverList:"
+ "_treatmentIdFromActiveFactorProviderWithNamespaceName:"
+ "appleIntelligenceState"
+ "asFactorsState"
+ "clientWithExperimentIdentifiers:"
+ "com.apple.triald.ExternalParameterChangeQueue"
+ "copyWithReplacementCounterfactualTreatmentIds:"
+ "counterfactualFactorPackDeploymentMap"
+ "counterfactualFactorsStatesForNamespace:"
+ "counterfactualTreatmentIds"
+ "counterfactualTreatmentIds != nil"
+ "counterfactualTreatments"
+ "currentWithUseCaseIdentifiers:"
+ "enumerateCounterfactualsWithNamespace:error:usingBlock:"
+ "experimentFactorsState.treatmentId"
+ "experimentFactorsStateForCounterfactuals"
+ "experimentIdentifiersForNamespace:"
+ "factorProvider.provider.experimentId"
+ "fileLevel.path"
+ "hasCounterfactualsForNamespace:"
+ "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:"
+ "lockedSet for counterfactuals unexpectedly not present"
+ "plplist contains bad experiment deployment."
+ "plplist contains bad provider chain."
+ "plplist contains experiment deployment with bad factor pack set ID: %@"
+ "plplist contains experiment deployment with bad treatment ID."
+ "plplist contains non-array provider chain."
+ "plplist contains unexpected toplevel content."
+ "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:"
+ "resolveTargetedFactorPackSetForExperimentFactorsState:"
+ "self.experimentFactorsStateForCounterfactuals"
+ "setAppleIntelligenceState:"
+ "setByAddingObjectsFromArray:"
+ "treatmentFactorPackSetIds"
+ "triParseJson"
+ "triRemoveFirstItemPassingTest:"
+ "v2/factorPackSets/%@"
+ "v32@?0@\"TRIExperimentFactorsState\"8@\"TRILockedFactorPackSet\"16^B24"
+ "v32@?0@\"TRITypedFactorProvider\"8Q16^B24"
- "<TRIPartialExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ isShadow:%@>"
- "@84@0:8i16@20@28@36i44q48@56@64@72B80"
- "TrialXP-429.0.4.6"
- "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:"
- "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:"

```
