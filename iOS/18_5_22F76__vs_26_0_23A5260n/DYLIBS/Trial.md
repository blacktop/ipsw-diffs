## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Trial`

```diff

-429.20.2.0.0
-  __TEXT.__text: 0x7baf8
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__delay_helper: 0x258
-  __TEXT.__objc_methlist: 0x71e0
-  __TEXT.__const: 0xf02
-  __TEXT.__dlopen_cstrs: 0x101
-  __TEXT.__gcc_except_tab: 0x5460
-  __TEXT.__cstring: 0x9994
-  __TEXT.__oslogstring: 0x4a3a
+463.0.0.0.0
+  __TEXT.__text: 0x696ac
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x5c78
+  __TEXT.__const: 0xeca
+  __TEXT.__cstring: 0x835e
+  __TEXT.__gcc_except_tab: 0x52bc
+  __TEXT.__oslogstring: 0x3da7
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x25e8
-  __TEXT.__objc_classname: 0x13e5
-  __TEXT.__objc_methname: 0xea8f
-  __TEXT.__objc_methtype: 0x2e1c
-  __TEXT.__objc_stubs: 0x9f80
-  __DATA_CONST.__got: 0x868
-  __DATA_CONST.__const: 0x1c48
-  __DATA_CONST.__objc_classlist: 0x4f8
-  __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0xe0
+  __TEXT.__unwind_info: 0x2150
+  __TEXT.__objc_classname: 0x1069
+  __TEXT.__objc_methname: 0xc07c
+  __TEXT.__objc_methtype: 0x257c
+  __TEXT.__objc_stubs: 0x8340
+  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__const: 0x1918
+  __DATA_CONST.__objc_classlist: 0x418
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3690
+  __DATA_CONST.__objc_selrefs: 0x2d48
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x600
-  __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0x7640
-  __AUTH_CONST.__objc_const: 0xc9d0
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_arraydata: 0x1b8
+  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__const: 0xda0
+  __AUTH_CONST.__cfstring: 0x6780
+  __AUTH_CONST.__objc_const: 0xa568
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x550
+  __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x6b0
-  __DATA.__data: 0xe80
-  __DATA.__bss: 0x88
-  __DATA.__common: 0x8
+  __DATA.__objc_ivar: 0x578
+  __DATA.__data: 0xb30
+  __DATA.__bss: 0x78
+  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x54
-  __DATA_DIRTY.__objc_data: 0x2c60
-  __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x2d8
-  - /System/Library/Frameworks/Accounts.framework/Accounts
+  __DATA_DIRTY.__objc_data: 0x2580
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers
-  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
-  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
-  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
-  - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CFBB233B-A434-36DE-9566-82E2A0DDE249
-  Functions: 2540
-  Symbols:   9230
-  CStrings:  5206
+  UUID: B1236E71-CB43-3C1E-9AF3-7552339C2194
+  Functions: 2093
+  Symbols:   7694
+  CStrings:  4411
 
Symbols:
+ +[NSData(TRI) triDataWithHexString:]
+ +[TRIActiveExperimentsSysdiagnoseProvider _isFactorRecordFileType:]
+ +[TRIActiveRolloutsSysdiagnoseProvider _isFactorRecordFileType:]
+ +[TRIAllocationStatus _defaultProviderImpl]
+ +[TRICCommandRunner runCommand:withArgs:withTimesToAttemptOnTimeOut:withTimeOut:]
+ +[TRIClient clientForTrialdSystem:]
+ +[TRIClient clientWithIdentifier:forTrialdSystem:]
+ +[TRIClient client]
+ +[TRIFlatbufferUtils clientTreatmentWithFactorLevels:parentDir:isRelativePath:]
+ +[TRINamespaceDescriptor factorsURLFromPath:]
+ +[TRINamespaceFactorProviderChain factorProviderWithPaths:namespaceName:resolver:faultOnMissingInstalledFactors:]
+ +[TRIPartialExperimentRecord recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:]
+ +[TRIPartialRolloutRecord recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:]
+ +[TRIProcessInfo callerBundleId]
+ +[TRIProcessInfo callerIsRunningFromSystemContext]
+ +[TRIProcessInfo hostingProcessName]
+ +[TRIStandardPaths pathsForUser:]
+ +[TRIStandardPaths sharedPathsForSystem]
+ +[TRIStandardPaths sharedPaths]
+ -[TRIActiveExperimentsSysdiagnoseProvider .cxx_destruct]
+ -[TRIActiveExperimentsSysdiagnoseProvider filename]
+ -[TRIActiveExperimentsSysdiagnoseProvider initWithAllocationStatusProvider:outputFilename:environments:]
+ -[TRIActiveExperimentsSysdiagnoseProvider sysdiagnoseLinesWithError:]
+ -[TRIActiveFactorProvidersParser _resolverPropertyListWithGlobalRolloutsResolvedPath:]
+ -[TRIActiveRolloutsSysdiagnoseProvider .cxx_destruct]
+ -[TRIActiveRolloutsSysdiagnoseProvider filename]
+ -[TRIActiveRolloutsSysdiagnoseProvider initWithNamespaceManagementClient:]
+ -[TRIActiveRolloutsSysdiagnoseProvider init]
+ -[TRIActiveRolloutsSysdiagnoseProvider sysdiagnoseLinesWithError:]
+ -[TRIAllocationStatusDefaultProvider initForTrialdSystem:]
+ -[TRIAllocationStatusDefaultProvider isOptedOutOfExperimentation]
+ -[TRIClient _getLogger]
+ -[TRIClient initWithClientIdentifier:paths:factorsState:staleFactorsUsageGracePeriod:logger:]
+ -[TRIFBFastFactorLevels sourceAsDefaultsCString]
+ -[TRIFBFastFactorLevels sourceAsDefaultsData]
+ -[TRIFBFastFactorLevels sourceAsDefaults]
+ -[TRIFBFastFactorLevelsBuilder setSourceWithDefaults:]
+ -[TRIFBFastFactorLevelsChanges replaceSourceWithDefaults:]
+ -[TRIFBMobileAssetReference hasHasOnDemandFlag]
+ -[TRIFBMobileAssetReference hasOnDemandFlag]
+ -[TRIFBMobileAssetReferenceBuilder setHasOnDemandFlag:]
+ -[TRIFBMobileAssetReferenceChanges omitHasOnDemandFlag]
+ -[TRIFBMobileAssetReferenceChanges preserveHasOnDemandFlag]
+ -[TRIFBMobileAssetReferenceChanges replaceHasOnDemandFlag:]
+ -[TRINamespaceDescriptor optedOutOfDefaults]
+ -[TRINamespaceFactorProvider flatbufferLevelForFactor:]
+ -[TRINamespaceFactorProvider protobufLevelForFactor:]
+ -[TRINamespaceResolver _hasOverrideExperimentFactorsState]
+ -[TRINamespaceResolver _prepareFactorsStateForCounterfactualsOrInvestigationsForFactorsState:]
+ -[TRINamespaceResolver overrideExperimentFactorsState]
+ -[TRIPartialExperimentRecord copyWithReplacementExperimentType:]
+ -[TRIPartialExperimentRecord experimentType]
+ -[TRIPartialExperimentRecord initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:]
+ -[TRIPartialRolloutRecord initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:]
+ -[TRIStandardPaths allowEnvVarDefaultLevelsDir]
+ -[TRIStandardPaths forTrialdSystem]
+ -[TRIStandardPaths initWithSchemaVersion:forUser:forTrialdSystem:]
+ -[TRIStandardPaths systemInteropDirectory]
+ -[TRIVersionedNamespace(StringFormatting) userFacingString]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table153
+ GCC_except_table167
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table189
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table251
+ GCC_except_table259
+ GCC_except_table263
+ GCC_except_table267
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table280
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table285
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table305
+ GCC_except_table306
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table34
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table348
+ GCC_except_table351
+ GCC_except_table356
+ GCC_except_table359
+ GCC_except_table362
+ GCC_except_table373
+ GCC_except_table381
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table393
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table406
+ GCC_except_table413
+ GCC_except_table416
+ GCC_except_table420
+ GCC_except_table421
+ GCC_except_table423
+ GCC_except_table426
+ GCC_except_table427
+ GCC_except_table428
+ GCC_except_table430
+ GCC_except_table432
+ GCC_except_table437
+ GCC_except_table451
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table460
+ GCC_except_table462
+ GCC_except_table465
+ GCC_except_table479
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table493
+ GCC_except_table50
+ GCC_except_table507
+ GCC_except_table508
+ GCC_except_table514
+ GCC_except_table515
+ GCC_except_table516
+ GCC_except_table518
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table553
+ GCC_except_table563
+ GCC_except_table574
+ GCC_except_table586
+ GCC_except_table596
+ GCC_except_table614
+ GCC_except_table623
+ GCC_except_table633
+ GCC_except_table64
+ GCC_except_table642
+ GCC_except_table652
+ GCC_except_table66
+ GCC_except_table661
+ GCC_except_table671
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table92
+ GCC_except_table95
+ OBJC_IVAR_$_TRIActiveFactorProvidersParserGuardedData.overrideFactorPackDeploymentMap
+ _OBJC_CLASS_$_TRIActiveExperimentsSysdiagnoseProvider
+ _OBJC_CLASS_$_TRIActiveRolloutsSysdiagnoseProvider
+ _OBJC_IVAR_$_TRIActiveExperimentsSysdiagnoseProvider._environments
+ _OBJC_IVAR_$_TRIActiveExperimentsSysdiagnoseProvider._filename
+ _OBJC_IVAR_$_TRIActiveExperimentsSysdiagnoseProvider._statusProvider
+ _OBJC_IVAR_$_TRIActiveRolloutsSysdiagnoseProvider._namespaceClient
+ _OBJC_IVAR_$_TRIFBMobileAssetReferenceChanges._changeTypeHasOnDemandFlag
+ _OBJC_IVAR_$_TRIFBMobileAssetReferenceChanges._replacementHasOnDemandFlag
+ _OBJC_IVAR_$_TRINamespaceDescriptor._optedOutOfDefaults
+ _OBJC_IVAR_$_TRINamespaceFactorProviderChain._paths
+ _OBJC_IVAR_$_TRINamespaceResolver._overrideExperimentFactorsState
+ _OBJC_IVAR_$_TRIPartialExperimentRecord._experimentType
+ _OBJC_IVAR_$_TRIStandardPaths._forTrialdSystem
+ _OBJC_IVAR_$_TRIStandardPaths._forUserId
+ _OBJC_IVAR_$_TRIXPCNamespaceManagementClient._internalAgentToSystemHelper
+ _OBJC_METACLASS_$_TRIActiveExperimentsSysdiagnoseProvider
+ _OBJC_METACLASS_$_TRIActiveRolloutsSysdiagnoseProvider
+ _TRICloudKitRecordExperimentNotification_ForLaunchDaemon
+ _TRICloudKitRecordRolloutNotification_ForLaunchDaemon
+ _TRILogCategory_ClientFramework.log
+ _TRILogCategory_ClientFramework.onceToken
+ _TRILogCategory_InternalTool.log
+ _TRILogCategory_InternalTool.onceToken
+ _TRILogCategory_Server.log
+ _TRILogCategory_Server.onceToken
+ _TRISysdiagnoseKey_ActiveFactorPackSetId
+ _TRISysdiagnoseKey_AssetReference
+ _TRISysdiagnoseKey_Compatibility
+ _TRISysdiagnoseKey_CounterfactualTreatments
+ _TRISysdiagnoseKey_DeploymentId
+ _TRISysdiagnoseKey_Experiment
+ _TRISysdiagnoseKey_FactorPackId
+ _TRISysdiagnoseKey_Factors
+ _TRISysdiagnoseKey_LevelValue
+ _TRISysdiagnoseKey_Metadata
+ _TRISysdiagnoseKey_Name
+ _TRISysdiagnoseKey_Namespaces
+ _TRISysdiagnoseKey_Ncvs
+ _TRISysdiagnoseKey_Path
+ _TRISysdiagnoseKey_RampId
+ _TRISysdiagnoseKey_RolloutId
+ _TRISysdiagnoseKey_Size
+ _TRISysdiagnoseKey_Status
+ _TRISysdiagnoseKey_TargetedFactorPackSetId
+ _TRISysdiagnoseKey_TreatmentId
+ _TRISysdiagnoseKey_Type
+ __MergedGlobals.3
+ __OBJC_$_CLASS_METHODS_TRIActiveExperimentsSysdiagnoseProvider
+ __OBJC_$_CLASS_METHODS_TRIActiveRolloutsSysdiagnoseProvider
+ __OBJC_$_INSTANCE_METHODS_TRIActiveExperimentsSysdiagnoseProvider
+ __OBJC_$_INSTANCE_METHODS_TRIActiveRolloutsSysdiagnoseProvider
+ __OBJC_$_INSTANCE_METHODS_TRIVersionedNamespace(StringFormatting)
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveExperimentsSysdiagnoseProvider
+ __OBJC_$_INSTANCE_VARIABLES_TRIActiveRolloutsSysdiagnoseProvider
+ __OBJC_$_PROP_LIST_TRIPaths
+ __OBJC_$_PROP_LIST_TRIStandardPaths
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_TRIActiveExperimentsSysdiagnoseProvider
+ __OBJC_CLASS_PROTOCOLS_$_TRIActiveRolloutsSysdiagnoseProvider
+ __OBJC_CLASS_RO_$_TRIActiveExperimentsSysdiagnoseProvider
+ __OBJC_CLASS_RO_$_TRIActiveRolloutsSysdiagnoseProvider
+ __OBJC_LABEL_PROTOCOL_$_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_METACLASS_RO_$_TRIActiveExperimentsSysdiagnoseProvider
+ __OBJC_METACLASS_RO_$_TRIActiveRolloutsSysdiagnoseProvider
+ __OBJC_PROTOCOL_$_TRIXPCInternalAgentToSystemServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_TRIXPCInternalAgentToSystemServiceProtocol
+ __ZN5apple4aiml12flatbuffers214DetachedBufferD1Ev
+ __ZNK16FastFactorLevels18source_as_defaultsEv
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110__function12__value_funcIFN5apple4aiml12flatbuffers26OffsetIvEEmEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvmP10BoxedInt64EED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvmP11BoxedDoubleEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvmP9BoxedBoolEED2B8ne200100Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EELi0EEEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EELi0EEEvT1_SD_SD_SD_SD_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.192
+ ___109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.203
+ ___111-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:startingFromCursor:error:block:]_block_invoke
+ ___111-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:startingFromCursor:error:block:]_block_invoke_2
+ ___111-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:startingFromCursor:error:block:]_block_invoke_3
+ ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.183
+ ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.184
+ ___139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.231
+ ___139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.232
+ ___139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.233
+ ___203+[TRIFactorDownloadValidator validateDownloadForFactors:withNamespace:paths:container:factorsState:assetIndexesByTreatment:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:error:]_block_invoke.110
+ ___31+[TRIStandardPaths sharedPaths]_block_invoke
+ ___32+[TRIProcessInfo callerBundleId]_block_invoke
+ ___36+[TRIProcessInfo hostingProcessName]_block_invoke
+ ___47+[TRISysdiagnoseOutputFormatter formatRecords:]_block_invoke_3
+ ___58-[TRIAllocationStatusDefaultProvider initForTrialdSystem:]_block_invoke
+ ___58-[TRIAllocationStatusDefaultProvider initForTrialdSystem:]_block_invoke_2
+ ___58-[TRIAllocationStatusDefaultProvider initForTrialdSystem:]_block_invoke_3
+ ___58-[TRIAllocationStatusDefaultProvider initForTrialdSystem:]_block_invoke_4
+ ___63-[TRIClient sizesForFactors:withNamespaceName:forMetric:error:]_block_invoke.276
+ ___65-[TRIAllocationStatusDefaultProvider isOptedOutOfExperimentation]_block_invoke
+ ___65-[TRIAllocationStatusDefaultProvider isOptedOutOfExperimentation]_block_invoke_2
+ ___66-[TRIActiveRolloutsSysdiagnoseProvider sysdiagnoseLinesWithError:]_block_invoke
+ ___69-[TRIActiveExperimentsSysdiagnoseProvider sysdiagnoseLinesWithError:]_block_invoke
+ ___81+[TRICCommandRunner runCommand:withArgs:withTimesToAttemptOnTimeOut:withTimeOut:]_block_invoke
+ ___86-[TRIActiveFactorProvidersParser _resolverPropertyListWithGlobalRolloutsResolvedPath:]_block_invoke
+ ___86-[TRIClient statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:]_block_invoke.320
+ ___Block_byref_object_copy_.641
+ ___Block_byref_object_dispose_.642
+ ____loggingAppDomain_block_invoke
+ ___block_descriptor_32_e31_16?0"TRIVersionedNamespace"8l
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_literal_global.10
+ ___block_literal_global.103
+ ___block_literal_global.118
+ ___block_literal_global.133
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.150
+ ___block_literal_global.156
+ ___block_literal_global.16
+ ___block_literal_global.162
+ ___block_literal_global.166
+ ___block_literal_global.19
+ ___block_literal_global.197
+ ___block_literal_global.2
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.24
+ ___block_literal_global.26
+ ___block_literal_global.278
+ ___block_literal_global.28
+ ___block_literal_global.302
+ ___block_literal_global.31
+ ___block_literal_global.316
+ ___block_literal_global.322
+ ___block_literal_global.346
+ ___block_literal_global.385
+ ___block_literal_global.5
+ ___block_literal_global.59
+ ___block_literal_global.7
+ ___block_literal_global.84
+ __loggingAppDomain
+ _descriptor.descriptor.20
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _kTRISystemContextOverrideUserDefaultsKey
+ _objc_msgSend$_defaultProviderImpl
+ _objc_msgSend$_hasOverrideExperimentFactorsState
+ _objc_msgSend$_prepareFactorsStateForCounterfactualsOrInvestigationsForFactorsState:
+ _objc_msgSend$_resolverPropertyListWithGlobalRolloutsResolvedPath:
+ _objc_msgSend$activeExperimentInformationWithEnvironments:completion:
+ _objc_msgSend$activeRolloutInformationWithCompletion:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$callerIsRunningFromSystemContext
+ _objc_msgSend$clientWithIdentifier:forTrialdSystem:
+ _objc_msgSend$experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:
+ _objc_msgSend$experimentRecordsWithDeploymentEnvironments:completion:
+ _objc_msgSend$experimentType
+ _objc_msgSend$factorProviderWithPaths:namespaceName:resolver:faultOnMissingInstalledFactors:
+ _objc_msgSend$factorsURLFromPath:
+ _objc_msgSend$flatbufferLevelForFactor:
+ _objc_msgSend$initForTrialdSystem:
+ _objc_msgSend$initWithAllocationStatusProvider:outputFilename:environments:
+ _objc_msgSend$initWithClientIdentifier:paths:factorsState:staleFactorsUsageGracePeriod:logger:
+ _objc_msgSend$initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:
+ _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:
+ _objc_msgSend$initWithNamespaceManagementClient:
+ _objc_msgSend$initWithSchemaVersion:forUser:forTrialdSystem:
+ _objc_msgSend$initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:
+ _objc_msgSend$isOptedOutOfExperimentation
+ _objc_msgSend$isOptedOutOfExperimentationWithCompletion:
+ _objc_msgSend$object
+ _objc_msgSend$optedOutOfDefaults
+ _objc_msgSend$overrideExperimentFactorsState
+ _objc_msgSend$pathExtension
+ _objc_msgSend$protobufLevelForFactor:
+ _objc_msgSend$rolloutAllocationStatusWithCompletion:
+ _objc_msgSend$setSourceWithDefaults:
+ _objc_msgSend$sharedPaths
+ _objc_msgSend$sharedPathsForSystem
+ _objc_msgSend$sourceAsDefaults
+ _objc_msgSend$sourceAsDefaultsCString
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$userFacingString
+ _strtol
- +[TRIAllocationStatus _defaultProvider]
- +[TRIAllocationStatus activeBMLTInformationWithError:]
- +[TRIBMLTActiveEvaluationTuple supportsSecureCoding]
- +[TRIBMLTActiveEvaluationTuple tupleWithBmlt:factorsState:]
- +[TRIBMLTDeployment deploymentWithBackgroundMLTaskId:deploymentId:]
- +[TRIBMLTDeployment supportsSecureCoding]
- +[TRIBMLTFactorsState supportsSecureCoding]
- +[TRIBackgroundMLTaskHistoryRecord recordWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:]
- +[TRIBackgroundMLTaskHistoryRecord supportsSecureCoding]
- +[TRICKServerEnvironmentReader currentEnvironment]
- +[TRICKServerEnvironmentReader currentPopulation]
- +[TRICKServerEnvironmentReader validatedEnvironmentFromNumber:]
- +[TRICKServerEnvironmentReader validatedPopulationFromNumber:]
- +[TRICellularParameterManager sharedInstance]
- +[TRIClient activeBMLTInformation:]
- +[TRIClient clientWithIdentifier:unit:]
- +[TRIClient printedBMLTInformation:]
- +[TRIClient printedExperimentInformationWithEnvironments:error:]
- +[TRIClient printedRolloutInformation:]
- +[TRIClient sysdiagnoseInfoWithError:]
- +[TRIEvaluationStatus defaultProvider]
- +[TRIEvaluationStatus freshProvider]
- +[TRIEvaluationStatus supportsSecureCoding]
- +[TRIEvaluationStatusCursor supportsSecureCoding]
- +[TRIMLRuntimeActiveEvaluationTuple supportsSecureCoding]
- +[TRIMLRuntimeActiveEvaluationTuple tupleWithEval:factorsState:]
- +[TRIMLRuntimeEvaluationHistoryRecord recordWithEvaluation:status:]
- +[TRIMLRuntimeEvaluationHistoryRecord supportsSecureCoding]
- +[TRINamespaceFactorProviderChain factorProviderWithPaths:namespaceName:resolver:]
- +[TRINamespaceLogPolicy shouldPrivacyFilterNamespace:policy:]
- +[TRIPartialBMLTRecord recordWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:]
- +[TRIPartialBMLTRecord supportsSecureCoding]
- +[TRIPartialExperimentRecord recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:]
- +[TRIPartialRolloutRecord recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:]
- +[TRIPersistedBMLTFactorsState descriptor]
- +[TRIPersistedEvaluationStatus descriptor]
- +[TRIPersistedRolloutFactorsState descriptor]
- +[TRIRolloutFactorsState supportsSecureCoding]
- +[TRIStandardPaths sharedSystemPaths]
- +[TRISystemConfiguration _sharedSystemInfo]
- +[TRISystemConfiguration sharedInstance]
- +[TRISystemDimensions(Factory) systemDimensions]
- +[TRISystemInfo _aneVersion]
- +[TRISystemInfo _appleIntelligenceState]
- +[TRISystemInfo _carrierBundleIdentifier]
- +[TRISystemInfo _carrierCountryIsoCode]
- +[TRISystemInfo _hasAne]
- +[TRISystemInfo _iCloudIdentifier]
- +[TRISystemInfo _isAutomatedTestDevice]
- +[TRISystemInfo _isDiagnosticsAndUsageEnabled]
- +[TRISystemInfo _isSeedBuild]
- +[TRISystemInfo _isVirtualMachine]
- +[TRISystemInfo _persistentSystemInfoPath]
- +[TRISystemInfo _siriUserActivitySegment]
- +[TRISystemInfo _sysEnabledInputModeIdentifiers]
- +[TRISystemInfo _sysIsEnrolledInBetaProgram]
- +[TRISystemInfo createSystemInfoWithFactorProvider:]
- +[TRISystemInfo info]
- +[TRISystemInfo loadSystemInfo]
- +[TRISystemInfo supportsSecureCoding]
- +[TRISystemInfo systemInfoFromFile:]
- -[TRIAllocationStatusDefaultProvider activeBMLTInformationWithError:]
- -[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:]
- -[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForTestingPrivacyFilterPolicyWithEnvironment:startingFromCursor:error:block:]
- -[TRIBMLTActiveEvaluationTuple .cxx_destruct]
- -[TRIBMLTActiveEvaluationTuple bmlt]
- -[TRIBMLTActiveEvaluationTuple copyWithReplacementBmlt:]
- -[TRIBMLTActiveEvaluationTuple copyWithReplacementFactorsState:]
- -[TRIBMLTActiveEvaluationTuple copyWithZone:]
- -[TRIBMLTActiveEvaluationTuple description]
- -[TRIBMLTActiveEvaluationTuple encodeWithCoder:]
- -[TRIBMLTActiveEvaluationTuple factorsState]
- -[TRIBMLTActiveEvaluationTuple hash]
- -[TRIBMLTActiveEvaluationTuple initWithBmlt:factorsState:]
- -[TRIBMLTActiveEvaluationTuple initWithCoder:]
- -[TRIBMLTActiveEvaluationTuple init]
- -[TRIBMLTActiveEvaluationTuple isEqual:]
- -[TRIBMLTActiveEvaluationTuple isEqualToTuple:]
- -[TRIBMLTDeployment .cxx_destruct]
- -[TRIBMLTDeployment backgroundMLTaskId]
- -[TRIBMLTDeployment copyWithReplacementBackgroundMLTaskId:]
- -[TRIBMLTDeployment copyWithReplacementDeploymentId:]
- -[TRIBMLTDeployment copyWithZone:]
- -[TRIBMLTDeployment deploymentId]
- -[TRIBMLTDeployment description]
- -[TRIBMLTDeployment encodeWithCoder:]
- -[TRIBMLTDeployment hash]
- -[TRIBMLTDeployment initWithBackgroundMLTaskId:deploymentId:]
- -[TRIBMLTDeployment initWithCoder:]
- -[TRIBMLTDeployment init]
- -[TRIBMLTDeployment isEqual:]
- -[TRIBMLTDeployment isEqualToDeployment:]
- -[TRIBMLTDeployment(Utils) hasDeploymentId]
- -[TRIBMLTDeployment(Utils) shortDesc]
- -[TRIBMLTDeployment(Utils) taskTag]
- -[TRIBMLTFactorsState .cxx_destruct]
- -[TRIBMLTFactorsState _isEqualToState:]
- -[TRIBMLTFactorsState bmltIdentifiers]
- -[TRIBMLTFactorsState deployment]
- -[TRIBMLTFactorsState description]
- -[TRIBMLTFactorsState encodeWithCoder:]
- -[TRIBMLTFactorsState hash]
- -[TRIBMLTFactorsState initWithDeployment:]
- -[TRIBMLTFactorsState isEqual:]
- -[TRIBMLTFactorsState persisted]
- -[TRIBackgroundMLTaskHistoryRecord .cxx_destruct]
- -[TRIBackgroundMLTaskHistoryRecord backgroundMLTaskId]
- -[TRIBackgroundMLTaskHistoryRecord copyWithReplacementBackgroundMLTaskId:]
- -[TRIBackgroundMLTaskHistoryRecord copyWithReplacementDeploymentId:]
- -[TRIBackgroundMLTaskHistoryRecord copyWithReplacementEventDate:]
- -[TRIBackgroundMLTaskHistoryRecord copyWithReplacementEventType:]
- -[TRIBackgroundMLTaskHistoryRecord copyWithReplacementFactorPackSetId:]
- -[TRIBackgroundMLTaskHistoryRecord copyWithZone:]
- -[TRIBackgroundMLTaskHistoryRecord deploymentId]
- -[TRIBackgroundMLTaskHistoryRecord description]
- -[TRIBackgroundMLTaskHistoryRecord encodeWithCoder:]
- -[TRIBackgroundMLTaskHistoryRecord eventDate]
- -[TRIBackgroundMLTaskHistoryRecord eventType]
- -[TRIBackgroundMLTaskHistoryRecord factorPackSetId]
- -[TRIBackgroundMLTaskHistoryRecord hash]
- -[TRIBackgroundMLTaskHistoryRecord initWithCoder:]
- -[TRIBackgroundMLTaskHistoryRecord initWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:]
- -[TRIBackgroundMLTaskHistoryRecord init]
- -[TRIBackgroundMLTaskHistoryRecord isEqual:]
- -[TRIBackgroundMLTaskHistoryRecord isEqualToRecord:]
- -[TRIBackgroundMLTaskIdentifiers .cxx_destruct]
- -[TRIBackgroundMLTaskIdentifiers bmltTaskId]
- -[TRIBackgroundMLTaskIdentifiers copyWithZone:]
- -[TRIBackgroundMLTaskIdentifiers deploymentId]
- -[TRIBackgroundMLTaskIdentifiers description]
- -[TRIBackgroundMLTaskIdentifiers factorPackId]
- -[TRIBackgroundMLTaskIdentifiers hash]
- -[TRIBackgroundMLTaskIdentifiers initWithBMLTTaskId:deploymentId:treatmentId:]
- -[TRIBackgroundMLTaskIdentifiers initWithBMLTaskId:deploymentId:factorPackId:]
- -[TRIBackgroundMLTaskIdentifiers isEqual:]
- -[TRIBackgroundMLTaskIdentifiers isEqualToBMLTTaskIdentifiers:]
- -[TRIBackgroundMLTaskIdentifiers treatmentId]
- -[TRIBiomeDataStreamProvider .cxx_destruct]
- -[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]
- -[TRIBiomeDataStreamProvider _unsubscribeAllDataStreams]
- -[TRIBiomeDataStreamProvider dealloc]
- -[TRIBiomeDataStreamProvider init]
- -[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]
- -[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]
- -[TRIBiomeDataStreamProvider setShouldSubscribeWithWaking:]
- -[TRIBiomeDataStreamProvider subscribeDataStreamForIdentifier:eventHandler:]
- -[TRIBiomeDataStreamProvider unsubscribeAllDataStreams]
- -[TRICellularParameterGuardedData .cxx_destruct]
- -[TRICellularParameterGuardedData description]
- -[TRICellularParameterManager .cxx_destruct]
- -[TRICellularParameterManager _dispatchQueueForCarrierInfoGathering]
- -[TRICellularParameterManager _fetchCarrierBundleIdentifier:]
- -[TRICellularParameterManager _fetchCarrierCountryIsoCode:]
- -[TRICellularParameterManager _updateSystemInfo]
- -[TRICellularParameterManager carrierBundleChange:]
- -[TRICellularParameterManager carrierBundleIdentifier]
- -[TRICellularParameterManager carrierCountryIsoCode]
- -[TRICellularParameterManager init]
- -[TRICellularParameterManager preferredDataSimChanged:]
- -[TRICellularParameterManager setCarrierBundleIdentifier:]
- -[TRICellularParameterManager setCarrierCountryIsoCode:]
- -[TRICellularParameterManager subscriberCountryCodeDidChange:]
- -[TRIClient _bmltIdentifiersWithNamespaceName:]
- -[TRIClient _logBMLTCustomTargetingWithResult:]
- -[TRIClient backgroundMLTaskIdentifiersWithNamespaceName:]
- -[TRIClient evaluateBMLTTargetingExpression:withParameters:error:]
- -[TRIClient initWithClientIdentifier:paths:unit:factorsState:staleFactorsUsageGracePeriod:logger:]
- -[TRIClient initWithClientIdentifier:paths:unit:staleFactorsUsageGracePeriod:logger:]
- -[TRIDefaultFactorProvider bmltDeploymentWithNamespaceName:]
- -[TRIDefaultFactorProvider factorPackIdForBmltWithNamespaceName:]
- -[TRIEvaluationStatus .cxx_destruct]
- -[TRIEvaluationStatus copyWithZone:]
- -[TRIEvaluationStatus date]
- -[TRIEvaluationStatus encodeWithCoder:]
- -[TRIEvaluationStatus evalState]
- -[TRIEvaluationStatus evaluationId]
- -[TRIEvaluationStatus hash]
- -[TRIEvaluationStatus initWithCoder:]
- -[TRIEvaluationStatus initWithType:evaluationId:date:evalState:]
- -[TRIEvaluationStatus isEqual:]
- -[TRIEvaluationStatus type]
- -[TRIEvaluationStatusCursor copyWithZone:]
- -[TRIEvaluationStatusCursor date]
- -[TRIEvaluationStatusCursor encodeWithCoder:]
- -[TRIEvaluationStatusCursor hash]
- -[TRIEvaluationStatusCursor initWithCoder:]
- -[TRIEvaluationStatusCursor initWithSecondsFromEpoch:]
- -[TRIEvaluationStatusCursor isEqual:]
- -[TRIEvaluationStatusDefaultProvider .cxx_destruct]
- -[TRIEvaluationStatusDefaultProvider enumerateActiveBMLTWithError:block:]
- -[TRIEvaluationStatusDefaultProvider enumerateActiveEvaluationsForMLRuntimeWithError:block:]
- -[TRIEvaluationStatusDefaultProvider enumerateStatusOfEvaluationsForMLRuntimeWithCursor:error:block:]
- -[TRIEvaluationStatusDefaultProvider init]
- -[TRIEvaluationStatusDefaultProvider syncProxyWithErrorHandler:]
- -[TRIExternalParameterGuardedData .cxx_destruct]
- -[TRIExternalParameterGuardedData description]
- -[TRIExternalParameterManager .cxx_destruct]
- -[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]
- -[TRIExternalParameterManager _readParametersFromFile]
- -[TRIExternalParameterManager _readSiriDeviceAggregationIdRotationDateFromEvent:]
- -[TRIExternalParameterManager _updateSystemInfo]
- -[TRIExternalParameterManager _writeParametersToFile]
- -[TRIExternalParameterManager dictionary]
- -[TRIExternalParameterManager initWithProvider:paths:]
- -[TRIExternalParameterManager init]
- -[TRIExternalParameterManager siriDeviceAggregationIdRotationDate]
- -[TRIFactorsState bmltIdentifiers]
- -[TRIFactorsState rolloutIdentifiers]
- -[TRIFactorsStateBMLTIdentifiers .cxx_destruct]
- -[TRIFactorsStateBMLTIdentifiers bmltId]
- -[TRIFactorsStateBMLTIdentifiers copyWithZone:]
- -[TRIFactorsStateBMLTIdentifiers deploymentId]
- -[TRIFactorsStateBMLTIdentifiers description]
- -[TRIFactorsStateBMLTIdentifiers hash]
- -[TRIFactorsStateBMLTIdentifiers initWithBMLTId:deploymentId:]
- -[TRIFactorsStateBMLTIdentifiers init]
- -[TRIFactorsStateBMLTIdentifiers isEqual:]
- -[TRIFactorsStateBMLTIdentifiers isEqualToIdentifiers:]
- -[TRIFactorsStateRolloutIdentifiers .cxx_destruct]
- -[TRIFactorsStateRolloutIdentifiers copyWithZone:]
- -[TRIFactorsStateRolloutIdentifiers deploymentId]
- -[TRIFactorsStateRolloutIdentifiers description]
- -[TRIFactorsStateRolloutIdentifiers hash]
- -[TRIFactorsStateRolloutIdentifiers initWithRolloutId:deploymentId:]
- -[TRIFactorsStateRolloutIdentifiers init]
- -[TRIFactorsStateRolloutIdentifiers isEqual:]
- -[TRIFactorsStateRolloutIdentifiers isEqualToIdentifiers:]
- -[TRIFactorsStateRolloutIdentifiers rolloutId]
- -[TRILogger .cxx_destruct]
- -[TRILogger _dispatchLogEvent:]
- -[TRILogger _incrementedLogEventCount]
- -[TRILogger initWithClient:projectId:logHandlers:]
- -[TRILogger initWithProjectId:]
- -[TRILogger initWithProjectId:logHandlers:]
- -[TRILogger init]
- -[TRILogger logEvent:]
- -[TRILogger logHandlers]
- -[TRILogger logWithMLRuntimeDimensions:metrics:factorState:]
- -[TRILogger logWithNamespaceName:metrics:dimensions:]
- -[TRILogger logWithProjectNameAndTrackingId:metrics:dimensions:trialSystemTelemetry:]
- -[TRILogger logWithTrackingId:logLevel:message:]
- -[TRILogger logWithTrackingId:logLevel:message:args:]
- -[TRILogger logWithTrackingId:message:]
- -[TRILogger logWithTrackingId:metric:]
- -[TRILogger logWithTrackingId:metric:dimensions:]
- -[TRILogger logWithTrackingId:metrics:dimensions:]
- -[TRILogger logWithTrackingId:metrics:dimensions:systemDimensions:trialSystemTelemetry:]
- -[TRILogger logWithTrackingId:metrics:dimensions:trialSystemTelemetry:]
- -[TRILogger messageWithOneofField:withName:]
- -[TRIMLRuntimeActiveEvaluationTuple .cxx_destruct]
- -[TRIMLRuntimeActiveEvaluationTuple copyWithReplacementEval:]
- -[TRIMLRuntimeActiveEvaluationTuple copyWithReplacementFactorsState:]
- -[TRIMLRuntimeActiveEvaluationTuple copyWithZone:]
- -[TRIMLRuntimeActiveEvaluationTuple description]
- -[TRIMLRuntimeActiveEvaluationTuple encodeWithCoder:]
- -[TRIMLRuntimeActiveEvaluationTuple eval]
- -[TRIMLRuntimeActiveEvaluationTuple factorsState]
- -[TRIMLRuntimeActiveEvaluationTuple hash]
- -[TRIMLRuntimeActiveEvaluationTuple initWithCoder:]
- -[TRIMLRuntimeActiveEvaluationTuple initWithEval:factorsState:]
- -[TRIMLRuntimeActiveEvaluationTuple init]
- -[TRIMLRuntimeActiveEvaluationTuple isEqual:]
- -[TRIMLRuntimeActiveEvaluationTuple isEqualToTuple:]
- -[TRIMLRuntimeEvaluationHistoryRecord .cxx_destruct]
- -[TRIMLRuntimeEvaluationHistoryRecord copyWithReplacementEvaluation:]
- -[TRIMLRuntimeEvaluationHistoryRecord copyWithReplacementStatus:]
- -[TRIMLRuntimeEvaluationHistoryRecord copyWithZone:]
- -[TRIMLRuntimeEvaluationHistoryRecord description]
- -[TRIMLRuntimeEvaluationHistoryRecord encodeWithCoder:]
- -[TRIMLRuntimeEvaluationHistoryRecord evaluation]
- -[TRIMLRuntimeEvaluationHistoryRecord hash]
- -[TRIMLRuntimeEvaluationHistoryRecord initWithCoder:]
- -[TRIMLRuntimeEvaluationHistoryRecord initWithEvaluation:status:]
- -[TRIMLRuntimeEvaluationHistoryRecord init]
- -[TRIMLRuntimeEvaluationHistoryRecord isEqual:]
- -[TRIMLRuntimeEvaluationHistoryRecord isEqualToRecord:]
- -[TRIMLRuntimeEvaluationHistoryRecord status]
- -[TRINamespaceFactorProvider overlayLevelsFromFactorProvider:]
- -[TRINamespaceResolver _factorProviderForNamespaceName:fromNamespaceDescriptorSetWithDir:resolvedPath:]
- -[TRINamespaceResolver _faultOnceWithMessage:]
- -[TRINamespaceResolver _hasBMLTFactorsState]
- -[TRINamespaceResolver _hasCounterfactualFactorsState]
- -[TRINamespaceResolver _hasExperimentFactorsState]
- -[TRINamespaceResolver _hasRolloutFactorsState]
- -[TRINamespaceResolver _prepareFactorsStateForCounterfactualsForFactorsState:]
- -[TRINamespaceResolver _prepareFactorsStateForExperimentsOnFactorPackSetPathForDeployment:]
- -[TRINamespaceResolver _prepareFactorsStateForExperimentsOnTreatmentPathForDeployment:]
- -[TRINamespaceResolver _resolveTargetedFactorPackSetForBMLTDeployment:]
- -[TRINamespaceResolver _resolveTargetedNamespaceDescriptorSetForExperimentDeployment:]
- -[TRINamespaceResolver bmltDeploymentForFactorsState]
- -[TRINamespaceResolver experimentDeploymentForFactorsState]
- -[TRINamespaceResolver experimentFactorsStateForCounterfactuals]
- -[TRINamespaceResolver rolloutDeploymentForFactorsState]
- -[TRINamespaceResolverGuardedData .cxx_destruct]
- -[TRIPETLogHandler logEvent:subgroupName:queue:]
- -[TRIPartialBMLTRecord .cxx_destruct]
- -[TRIPartialBMLTRecord activeFactorPackSetId]
- -[TRIPartialBMLTRecord activeTargetingRuleIndex]
- -[TRIPartialBMLTRecord bmltDeployment]
- -[TRIPartialBMLTRecord copyWithReplacementActiveFactorPackSetId:]
- -[TRIPartialBMLTRecord copyWithReplacementActiveTargetingRuleIndex:]
- -[TRIPartialBMLTRecord copyWithReplacementBmltDeployment:]
- -[TRIPartialBMLTRecord copyWithReplacementEndDate:]
- -[TRIPartialBMLTRecord copyWithReplacementNamespace:]
- -[TRIPartialBMLTRecord copyWithReplacementPluginId:]
- -[TRIPartialBMLTRecord copyWithReplacementStatus:]
- -[TRIPartialBMLTRecord copyWithReplacementTargetedFactorPackSetId:]
- -[TRIPartialBMLTRecord copyWithReplacementTargetedTargetingRuleIndex:]
- -[TRIPartialBMLTRecord copyWithZone:]
- -[TRIPartialBMLTRecord description]
- -[TRIPartialBMLTRecord encodeWithCoder:]
- -[TRIPartialBMLTRecord endDate]
- -[TRIPartialBMLTRecord hash]
- -[TRIPartialBMLTRecord initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:]
- -[TRIPartialBMLTRecord initWithCoder:]
- -[TRIPartialBMLTRecord init]
- -[TRIPartialBMLTRecord isEqual:]
- -[TRIPartialBMLTRecord isEqualToRecord:]
- -[TRIPartialBMLTRecord namespace]
- -[TRIPartialBMLTRecord pluginId]
- -[TRIPartialBMLTRecord status]
- -[TRIPartialBMLTRecord targetedFactorPackSetId]
- -[TRIPartialBMLTRecord targetedTargetingRuleIndex]
- -[TRIPartialExperimentRecord copyWithReplacementIsShadow:]
- -[TRIPartialExperimentRecord initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:]
- -[TRIPartialExperimentRecord isShadow]
- -[TRIPartialRolloutRecord copyWithReplacementIsShadow:]
- -[TRIPartialRolloutRecord initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:]
- -[TRIPartialRolloutRecord isShadow]
- -[TRIRolloutFactorsState .cxx_destruct]
- -[TRIRolloutFactorsState _isEqualToState:]
- -[TRIRolloutFactorsState deployment]
- -[TRIRolloutFactorsState description]
- -[TRIRolloutFactorsState encodeWithCoder:]
- -[TRIRolloutFactorsState hash]
- -[TRIRolloutFactorsState initWithDeployment:]
- -[TRIRolloutFactorsState isEqual:]
- -[TRIRolloutFactorsState persisted]
- -[TRIRolloutFactorsState rolloutIdentifiers]
- -[TRIStandardPaths allowedLowLevelDefaultLevelsDir]
- -[TRIStandardPaths initWithCurrentSchemaVersion]
- -[TRIStandardPaths initWithSchemaVersion:]
- -[TRIStandardPaths initWithSchemaVersion:container:asClientProcess:]
- -[TRIStandardPaths namespaceDescriptorsBMLTDir]
- -[TRIStandardPaths namespaceDescriptorsRolloutDir]
- -[TRIStandardPaths pathsForContainer:asClientProcess:]
- -[TRISystemConfiguration .cxx_destruct]
- -[TRISystemConfiguration _dispatchQueueForCarrierInfoGathering]
- -[TRISystemConfiguration _systemInfoWithIsStale:]
- -[TRISystemConfiguration _trialVersion]
- -[TRISystemConfiguration _updateSystemInfo:]
- -[TRISystemConfiguration aneVersion]
- -[TRISystemConfiguration appleIntelligenceState]
- -[TRISystemConfiguration carrierBundleIdentifier]
- -[TRISystemConfiguration carrierCountryIsoCode]
- -[TRISystemConfiguration createDeviceIdentifierWithPath:]
- -[TRISystemConfiguration createPersistentDeviceIdentifier]
- -[TRISystemConfiguration deleteDeviceIdentifierWithPath:]
- -[TRISystemConfiguration deleteDeviceIdentifier]
- -[TRISystemConfiguration deviceClass]
- -[TRISystemConfiguration deviceId]
- -[TRISystemConfiguration deviceInfoForQuestion:]
- -[TRISystemConfiguration deviceModelCode]
- -[TRISystemConfiguration enabledInputModeIdentifiers]
- -[TRISystemConfiguration hasAne]
- -[TRISystemConfiguration iCloudId]
- -[TRISystemConfiguration initWithPaths:]
- -[TRISystemConfiguration init]
- -[TRISystemConfiguration isAutomatedTestDevice]
- -[TRISystemConfiguration isBetaBuild]
- -[TRISystemConfiguration isBetaUserWithIsStale:]
- -[TRISystemConfiguration isDiagnosticsAndUsageEnabled]
- -[TRISystemConfiguration isInternalBuild]
- -[TRISystemConfiguration marketingOSVersion]
- -[TRISystemConfiguration osBuild]
- -[TRISystemConfiguration osType]
- -[TRISystemConfiguration populationType]
- -[TRISystemConfiguration readDeviceIdentifierWithPath:]
- -[TRISystemConfiguration reloadDeviceId]
- -[TRISystemConfiguration reloadSystemInfo]
- -[TRISystemConfiguration resetDeviceIdentifier]
- -[TRISystemConfiguration setDeviceIdentifier:]
- -[TRISystemConfiguration setDeviceIdentifier:path:]
- -[TRISystemConfiguration siriDeviceAggregationIdRotationDate]
- -[TRISystemConfiguration siriUserActivitySegment]
- -[TRISystemConfiguration storedDeviceIdentifier]
- -[TRISystemConfiguration systemInfo]
- -[TRISystemConfiguration trialVersionMajor]
- -[TRISystemConfiguration trialVersionMinor]
- -[TRISystemConfiguration trialVersionTag]
- -[TRISystemConfiguration userSettingsBCP47DeviceLocale]
- -[TRISystemConfiguration userSettingsLanguageCode]
- -[TRISystemConfiguration userSettingsRegionCode]
- -[TRISystemInfo .cxx_destruct]
- -[TRISystemInfo _getSiriDeviceAggregationIdRotationDate]
- -[TRISystemInfo aneVersion]
- -[TRISystemInfo appleIntelligenceState]
- -[TRISystemInfo carrierBundleIdentifier]
- -[TRISystemInfo carrierCountryIsoCode]
- -[TRISystemInfo enabledInputModeIdentifiers]
- -[TRISystemInfo encodeWithCoder:]
- -[TRISystemInfo externalParamManager]
- -[TRISystemInfo hasAne]
- -[TRISystemInfo iCloudIdentifier]
- -[TRISystemInfo initFromSystemWithFactorProvider:]
- -[TRISystemInfo initWithCoder:]
- -[TRISystemInfo isAutomatedTestDevice]
- -[TRISystemInfo isDiagnosticsAndUsageEnabled]
- -[TRISystemInfo isEnrolledInBetaProgram]
- -[TRISystemInfo logUserKeyboardEnabledInputMode]
- -[TRISystemInfo logUserSettingsLanguageCode]
- -[TRISystemInfo logUserSettingsRegionCode]
- -[TRISystemInfo saveToFile:]
- -[TRISystemInfo save]
- -[TRISystemInfo setAneVersion:]
- -[TRISystemInfo setAppleIntelligenceState:]
- -[TRISystemInfo setCarrierBundleIdentifier:]
- -[TRISystemInfo setCarrierCountryIsoCode:]
- -[TRISystemInfo setEnabledInputModeIdentifiers:]
- -[TRISystemInfo setHasAne:]
- -[TRISystemInfo setICloudIdentifier:]
- -[TRISystemInfo setIsAutomatedTestDevice:]
- -[TRISystemInfo setIsDiagnosticsAndUsageEnabled:]
- -[TRISystemInfo setIsEnrolledInBetaProgram:]
- -[TRISystemInfo setLogUserKeyboardEnabledInputMode:]
- -[TRISystemInfo setLogUserSettingsLanguageCode:]
- -[TRISystemInfo setLogUserSettingsRegionCode:]
- -[TRISystemInfo setSiriDeviceAggregationIdRotationDate:]
- -[TRISystemInfo setSiriUserActivitySegment:]
- -[TRISystemInfo siriDeviceAggregationIdRotationDate]
- -[TRISystemInfo siriUserActivitySegment]
- -[TRISystemInfoGuardedData .cxx_destruct]
- GCC_except_table101
- GCC_except_table105
- GCC_except_table111
- GCC_except_table114
- GCC_except_table119
- GCC_except_table130
- GCC_except_table134
- GCC_except_table141
- GCC_except_table143
- GCC_except_table152
- GCC_except_table158
- GCC_except_table173
- GCC_except_table175
- GCC_except_table177
- GCC_except_table178
- GCC_except_table179
- GCC_except_table18
- GCC_except_table183
- GCC_except_table187
- GCC_except_table191
- GCC_except_table192
- GCC_except_table193
- GCC_except_table2
- GCC_except_table202
- GCC_except_table207
- GCC_except_table220
- GCC_except_table223
- GCC_except_table225
- GCC_except_table226
- GCC_except_table227
- GCC_except_table228
- GCC_except_table236
- GCC_except_table240
- GCC_except_table244
- GCC_except_table245
- GCC_except_table248
- GCC_except_table249
- GCC_except_table253
- GCC_except_table258
- GCC_except_table261
- GCC_except_table264
- GCC_except_table266
- GCC_except_table270
- GCC_except_table274
- GCC_except_table284
- GCC_except_table286
- GCC_except_table287
- GCC_except_table289
- GCC_except_table290
- GCC_except_table292
- GCC_except_table298
- GCC_except_table307
- GCC_except_table308
- GCC_except_table312
- GCC_except_table313
- GCC_except_table316
- GCC_except_table317
- GCC_except_table318
- GCC_except_table332
- GCC_except_table337
- GCC_except_table340
- GCC_except_table352
- GCC_except_table355
- GCC_except_table361
- GCC_except_table363
- GCC_except_table366
- GCC_except_table371
- GCC_except_table372
- GCC_except_table374
- GCC_except_table376
- GCC_except_table384
- GCC_except_table391
- GCC_except_table392
- GCC_except_table400
- GCC_except_table401
- GCC_except_table404
- GCC_except_table408
- GCC_except_table409
- GCC_except_table417
- GCC_except_table425
- GCC_except_table439
- GCC_except_table445
- GCC_except_table446
- GCC_except_table447
- GCC_except_table449
- GCC_except_table453
- GCC_except_table467
- GCC_except_table47
- GCC_except_table473
- GCC_except_table474
- GCC_except_table475
- GCC_except_table477
- GCC_except_table481
- GCC_except_table495
- GCC_except_table501
- GCC_except_table502
- GCC_except_table503
- GCC_except_table505
- GCC_except_table520
- GCC_except_table545
- GCC_except_table555
- GCC_except_table566
- GCC_except_table578
- GCC_except_table588
- GCC_except_table606
- GCC_except_table615
- GCC_except_table625
- GCC_except_table63
- GCC_except_table634
- GCC_except_table644
- GCC_except_table65
- GCC_except_table653
- GCC_except_table663
- GCC_except_table69
- GCC_except_table73
- GCC_except_table77
- GCC_except_table79
- GCC_except_table83
- GCC_except_table88
- GCC_except_table89
- GCC_except_table93
- GCC_except_table99
- OBJC_IVAR_$_TRIActiveFactorProvidersParserGuardedData.counterfactualFactorPackDeploymentMap
- OBJC_IVAR_$_TRICellularParameterGuardedData.guardedCarrierBundleIdentifier
- OBJC_IVAR_$_TRICellularParameterGuardedData.guardedCarrierCountryIsoCode
- OBJC_IVAR_$_TRIExternalParameterGuardedData.guardedSiriDeviceAggregationIdRotationDate
- OBJC_IVAR_$_TRINamespaceResolverGuardedData.hasIssuedWarnings
- OBJC_IVAR_$_TRINamespaceResolverGuardedData.targetedBMLTDeploymentMap
- OBJC_IVAR_$_TRINamespaceResolverGuardedData.targetedExperimentNamespaceDescriptorDeploymentMap
- OBJC_IVAR_$_TRISystemInfoGuardedData.isStale
- OBJC_IVAR_$_TRISystemInfoGuardedData.systemInfo
- _AAErrorDomain
- _BiomeLibrary
- _CoreTelephonyLibrary
- _CoreTelephonyLibraryCore.frameworkLibrary
- _MGCopyAnswer
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_CLASS_$_BMBiomeScheduler
- _OBJC_CLASS_$_GMAvailabilityWrapper
- _OBJC_CLASS_$_NSExpression
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSLock
- _OBJC_CLASS_$_NSScanner
- _OBJC_CLASS_$_OSASystemConfiguration
- _OBJC_CLASS_$_PETEventTracker2
- _OBJC_CLASS_$_TRIBMLTActiveEvaluationTuple
- _OBJC_CLASS_$_TRIBMLTDeployment
- _OBJC_CLASS_$_TRIBMLTFactorsState
- _OBJC_CLASS_$_TRIBackgroundMLTaskHistoryRecord
- _OBJC_CLASS_$_TRIBackgroundMLTaskIdentifiers
- _OBJC_CLASS_$_TRIBiomeDataStreamProvider
- _OBJC_CLASS_$_TRICKServerEnvironmentReader
- _OBJC_CLASS_$_TRICellularParameterGuardedData
- _OBJC_CLASS_$_TRICellularParameterManager
- _OBJC_CLASS_$_TRIClientBackgroundMLTask
- _OBJC_CLASS_$_TRIEvaluationStatus
- _OBJC_CLASS_$_TRIEvaluationStatusCursor
- _OBJC_CLASS_$_TRIEvaluationStatusDefaultProvider
- _OBJC_CLASS_$_TRIExternalParameterGuardedData
- _OBJC_CLASS_$_TRIExternalParameterManager
- _OBJC_CLASS_$_TRIFactorsStateBMLTIdentifiers
- _OBJC_CLASS_$_TRIFactorsStateRolloutIdentifiers
- _OBJC_CLASS_$_TRILogger
- _OBJC_CLASS_$_TRIMLRuntimeActiveEvaluationTuple
- _OBJC_CLASS_$_TRIMLRuntimeEvaluation
- _OBJC_CLASS_$_TRIMLRuntimeEvaluationHistoryRecord
- _OBJC_CLASS_$_TRIMetric
- _OBJC_CLASS_$_TRINamespaceLogPolicy
- _OBJC_CLASS_$_TRINamespaceResolverGuardedData
- _OBJC_CLASS_$_TRIPETLogHandler
- _OBJC_CLASS_$_TRIPartialBMLTRecord
- _OBJC_CLASS_$_TRIPersistedBMLTFactorsState
- _OBJC_CLASS_$_TRIPersistedEvaluationStatus
- _OBJC_CLASS_$_TRIPersistedRolloutFactorsState
- _OBJC_CLASS_$_TRIProject
- _OBJC_CLASS_$_TRIRolloutFactorsState
- _OBJC_CLASS_$_TRISystemConfiguration
- _OBJC_CLASS_$_TRISystemDimensions
- _OBJC_CLASS_$_TRISystemInfo
- _OBJC_CLASS_$_TRISystemInfoGuardedData
- _OBJC_CLASS_$_TRITrialSystemTelemetry
- _OBJC_CLASS_$_TRIUserDimension
- _OBJC_IVAR_$_TRIBMLTActiveEvaluationTuple._bmlt
- _OBJC_IVAR_$_TRIBMLTActiveEvaluationTuple._factorsState
- _OBJC_IVAR_$_TRIBMLTDeployment._backgroundMLTaskId
- _OBJC_IVAR_$_TRIBMLTDeployment._deploymentId
- _OBJC_IVAR_$_TRIBMLTFactorsState._deployment
- _OBJC_IVAR_$_TRIBackgroundMLTaskHistoryRecord._backgroundMLTaskId
- _OBJC_IVAR_$_TRIBackgroundMLTaskHistoryRecord._deploymentId
- _OBJC_IVAR_$_TRIBackgroundMLTaskHistoryRecord._eventDate
- _OBJC_IVAR_$_TRIBackgroundMLTaskHistoryRecord._eventType
- _OBJC_IVAR_$_TRIBackgroundMLTaskHistoryRecord._factorPackSetId
- _OBJC_IVAR_$_TRIBackgroundMLTaskIdentifiers._bmltTaskId
- _OBJC_IVAR_$_TRIBackgroundMLTaskIdentifiers._deploymentId
- _OBJC_IVAR_$_TRIBackgroundMLTaskIdentifiers._factorPackId
- _OBJC_IVAR_$_TRIBackgroundMLTaskIdentifiers._treatmentId
- _OBJC_IVAR_$_TRIBiomeDataStreamProvider._providerQueue
- _OBJC_IVAR_$_TRIBiomeDataStreamProvider._shouldSubscribeWithWaking
- _OBJC_IVAR_$_TRIBiomeDataStreamProvider._streamIdentifierstoSubscribedSinks
- _OBJC_IVAR_$_TRICellularParameterManager._carrierBundleIdentifier
- _OBJC_IVAR_$_TRICellularParameterManager._carrierCountryIsoCode
- _OBJC_IVAR_$_TRICellularParameterManager._lock
- _OBJC_IVAR_$_TRICellularParameterManager._subscriptionContext
- _OBJC_IVAR_$_TRICellularParameterManager._telephonyClient
- _OBJC_IVAR_$_TRIEvaluationStatus._date
- _OBJC_IVAR_$_TRIEvaluationStatus._evalState
- _OBJC_IVAR_$_TRIEvaluationStatus._evaluationId
- _OBJC_IVAR_$_TRIEvaluationStatus._type
- _OBJC_IVAR_$_TRIEvaluationStatusCursor._secondsFromEpoch
- _OBJC_IVAR_$_TRIEvaluationStatusDefaultProvider._clientHelper
- _OBJC_IVAR_$_TRIExternalParameterManager._dispatchQueue
- _OBJC_IVAR_$_TRIExternalParameterManager._lock
- _OBJC_IVAR_$_TRIExternalParameterManager._paramProvider
- _OBJC_IVAR_$_TRIExternalParameterManager._plistPath
- _OBJC_IVAR_$_TRIFactorsStateBMLTIdentifiers._bmltId
- _OBJC_IVAR_$_TRIFactorsStateBMLTIdentifiers._deploymentId
- _OBJC_IVAR_$_TRIFactorsStateRolloutIdentifiers._deploymentId
- _OBJC_IVAR_$_TRIFactorsStateRolloutIdentifiers._rolloutId
- _OBJC_IVAR_$_TRILogger._client
- _OBJC_IVAR_$_TRILogger._logHandlers
- _OBJC_IVAR_$_TRILogger._loggingQueue
- _OBJC_IVAR_$_TRILogger._projectId
- _OBJC_IVAR_$_TRIMLRuntimeActiveEvaluationTuple._eval
- _OBJC_IVAR_$_TRIMLRuntimeActiveEvaluationTuple._factorsState
- _OBJC_IVAR_$_TRIMLRuntimeEvaluationHistoryRecord._evaluation
- _OBJC_IVAR_$_TRIMLRuntimeEvaluationHistoryRecord._status
- _OBJC_IVAR_$_TRINamespaceFactorProvider._isFBReadEnabled
- _OBJC_IVAR_$_TRINamespaceFactorProvider._isFBWriteEnabled
- _OBJC_IVAR_$_TRINamespaceFactorProviderChain._bmltProvider
- _OBJC_IVAR_$_TRINamespaceResolver._bmltDeploymentForFactorsState
- _OBJC_IVAR_$_TRINamespaceResolver._experimentDeploymentForFactorsState
- _OBJC_IVAR_$_TRINamespaceResolver._experimentFactorsStateForCounterfactuals
- _OBJC_IVAR_$_TRINamespaceResolver._lock
- _OBJC_IVAR_$_TRINamespaceResolver._rolloutDeploymentForFactorsState
- _OBJC_IVAR_$_TRIPartialBMLTRecord._activeFactorPackSetId
- _OBJC_IVAR_$_TRIPartialBMLTRecord._activeTargetingRuleIndex
- _OBJC_IVAR_$_TRIPartialBMLTRecord._bmltDeployment
- _OBJC_IVAR_$_TRIPartialBMLTRecord._endDate
- _OBJC_IVAR_$_TRIPartialBMLTRecord._namespace
- _OBJC_IVAR_$_TRIPartialBMLTRecord._pluginId
- _OBJC_IVAR_$_TRIPartialBMLTRecord._status
- _OBJC_IVAR_$_TRIPartialBMLTRecord._targetedFactorPackSetId
- _OBJC_IVAR_$_TRIPartialBMLTRecord._targetedTargetingRuleIndex
- _OBJC_IVAR_$_TRIPartialExperimentRecord._isShadow
- _OBJC_IVAR_$_TRIPartialRolloutRecord._isShadow
- _OBJC_IVAR_$_TRIRolloutFactorsState._deployment
- _OBJC_IVAR_$_TRIStandardPaths._isClient
- _OBJC_IVAR_$_TRISystemConfiguration._cachedDeviceIdentifier
- _OBJC_IVAR_$_TRISystemConfiguration._persistentDeviceIdentifierPath
- _OBJC_IVAR_$_TRISystemInfo._aneVersion
- _OBJC_IVAR_$_TRISystemInfo._appleIntelligenceState
- _OBJC_IVAR_$_TRISystemInfo._carrierBundleIdentifier
- _OBJC_IVAR_$_TRISystemInfo._carrierCountryIsoCode
- _OBJC_IVAR_$_TRISystemInfo._enabledInputModeIdentifiers
- _OBJC_IVAR_$_TRISystemInfo._hasAne
- _OBJC_IVAR_$_TRISystemInfo._iCloudIdentifier
- _OBJC_IVAR_$_TRISystemInfo._isAutomatedTestDevice
- _OBJC_IVAR_$_TRISystemInfo._isDiagnosticsAndUsageEnabled
- _OBJC_IVAR_$_TRISystemInfo._isEnrolledInBetaProgram
- _OBJC_IVAR_$_TRISystemInfo._logUserKeyboardEnabledInputMode
- _OBJC_IVAR_$_TRISystemInfo._logUserSettingsLanguageCode
- _OBJC_IVAR_$_TRISystemInfo._logUserSettingsRegionCode
- _OBJC_IVAR_$_TRISystemInfo._siriDeviceAggregationIdRotationDate
- _OBJC_IVAR_$_TRISystemInfo._siriUserActivitySegment
- _OBJC_IVAR_$_TRIXPCNamespaceManagementClient._internalSystemHelper
- _OBJC_METACLASS_$_TRIBMLTActiveEvaluationTuple
- _OBJC_METACLASS_$_TRIBMLTDeployment
- _OBJC_METACLASS_$_TRIBMLTFactorsState
- _OBJC_METACLASS_$_TRIBackgroundMLTaskHistoryRecord
- _OBJC_METACLASS_$_TRIBackgroundMLTaskIdentifiers
- _OBJC_METACLASS_$_TRIBiomeDataStreamProvider
- _OBJC_METACLASS_$_TRICKServerEnvironmentReader
- _OBJC_METACLASS_$_TRICellularParameterGuardedData
- _OBJC_METACLASS_$_TRICellularParameterManager
- _OBJC_METACLASS_$_TRIEvaluationStatus
- _OBJC_METACLASS_$_TRIEvaluationStatusCursor
- _OBJC_METACLASS_$_TRIEvaluationStatusDefaultProvider
- _OBJC_METACLASS_$_TRIExternalParameterGuardedData
- _OBJC_METACLASS_$_TRIExternalParameterManager
- _OBJC_METACLASS_$_TRIFactorsStateBMLTIdentifiers
- _OBJC_METACLASS_$_TRIFactorsStateRolloutIdentifiers
- _OBJC_METACLASS_$_TRILogger
- _OBJC_METACLASS_$_TRIMLRuntimeActiveEvaluationTuple
- _OBJC_METACLASS_$_TRIMLRuntimeEvaluationHistoryRecord
- _OBJC_METACLASS_$_TRINamespaceLogPolicy
- _OBJC_METACLASS_$_TRINamespaceResolverGuardedData
- _OBJC_METACLASS_$_TRIPETLogHandler
- _OBJC_METACLASS_$_TRIPartialBMLTRecord
- _OBJC_METACLASS_$_TRIPersistedBMLTFactorsState
- _OBJC_METACLASS_$_TRIPersistedEvaluationStatus
- _OBJC_METACLASS_$_TRIPersistedRolloutFactorsState
- _OBJC_METACLASS_$_TRIRolloutFactorsState
- _OBJC_METACLASS_$_TRISystemConfiguration
- _OBJC_METACLASS_$_TRISystemInfo
- _OBJC_METACLASS_$_TRISystemInfoGuardedData
- _TRICloudKitRecordBMLTCatalogNotification
- _TRICloudKitRecordBMLTCatalogNotification_CatalogDefinition
- _TRICloudKitRecordBMLTCatalogNotification_CatalogDefinitionSignature
- _TRICloudKitRecordBMLTCatalogNotification_Population
- _TRICloudKitRecordBMLTCatalogNotification_PublicCertificate
- _TRICloudKitRecordBMLTCatalogNotification_Status
- _TRICloudKitRecordBMLTNotification
- _TRICloudKitRecordBMLTNotification_BackgroundMLTaskId
- _TRICloudKitRecordBMLTNotification_DeploymentDate
- _TRICloudKitRecordBMLTNotification_DeploymentId
- _TRICloudKitRecordBMLTNotification_DeploymentType
- _TRICloudKitRecordBMLTNotification_NamespaceName
- _TRICloudKitRecordBMLTNotification_Populations
- _TRICloudKitRecordBMLTNotification_PublicCertificate
- _TRICloudKitRecordBMLTNotification_Status
- _TRICloudKitRecordBMLTNotification_TaskDefinition
- _TRICloudKitRecordBMLTNotification_TaskDefinitionSignature
- _TRILoggedNamespaceName
- _TRIPopulationOverrideKey
- __MergedGlobals.1
- __OBJC_$_CATEGORY_CLASS_METHODS_TRISystemDimensions_$_Factory
- __OBJC_$_CATEGORY_TRISystemDimensions_$_Factory
- __OBJC_$_CLASS_METHODS_TRIBMLTActiveEvaluationTuple
- __OBJC_$_CLASS_METHODS_TRIBMLTDeployment
- __OBJC_$_CLASS_METHODS_TRIBMLTFactorsState
- __OBJC_$_CLASS_METHODS_TRIBackgroundMLTaskHistoryRecord
- __OBJC_$_CLASS_METHODS_TRICKServerEnvironmentReader
- __OBJC_$_CLASS_METHODS_TRICellularParameterManager
- __OBJC_$_CLASS_METHODS_TRIEvaluationStatus
- __OBJC_$_CLASS_METHODS_TRIEvaluationStatusCursor
- __OBJC_$_CLASS_METHODS_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_$_CLASS_METHODS_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_$_CLASS_METHODS_TRINamespaceLogPolicy
- __OBJC_$_CLASS_METHODS_TRIPartialBMLTRecord
- __OBJC_$_CLASS_METHODS_TRIPersistedBMLTFactorsState
- __OBJC_$_CLASS_METHODS_TRIPersistedEvaluationStatus
- __OBJC_$_CLASS_METHODS_TRIPersistedRolloutFactorsState
- __OBJC_$_CLASS_METHODS_TRIRolloutFactorsState
- __OBJC_$_CLASS_METHODS_TRISystemConfiguration
- __OBJC_$_CLASS_METHODS_TRISystemInfo
- __OBJC_$_CLASS_PROP_LIST_TRIBMLTActiveEvaluationTuple
- __OBJC_$_CLASS_PROP_LIST_TRIBMLTDeployment
- __OBJC_$_CLASS_PROP_LIST_TRIBackgroundMLTaskHistoryRecord
- __OBJC_$_CLASS_PROP_LIST_TRIEvaluationStatus
- __OBJC_$_CLASS_PROP_LIST_TRIEvaluationStatusCursor
- __OBJC_$_CLASS_PROP_LIST_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_$_CLASS_PROP_LIST_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_$_CLASS_PROP_LIST_TRIPartialBMLTRecord
- __OBJC_$_CLASS_PROP_LIST_TRISystemInfo
- __OBJC_$_INSTANCE_METHODS_TRIBMLTActiveEvaluationTuple
- __OBJC_$_INSTANCE_METHODS_TRIBMLTDeployment(Utils)
- __OBJC_$_INSTANCE_METHODS_TRIBMLTFactorsState
- __OBJC_$_INSTANCE_METHODS_TRIBackgroundMLTaskHistoryRecord
- __OBJC_$_INSTANCE_METHODS_TRIBackgroundMLTaskIdentifiers
- __OBJC_$_INSTANCE_METHODS_TRIBiomeDataStreamProvider
- __OBJC_$_INSTANCE_METHODS_TRICellularParameterGuardedData
- __OBJC_$_INSTANCE_METHODS_TRICellularParameterManager
- __OBJC_$_INSTANCE_METHODS_TRIEvaluationStatus
- __OBJC_$_INSTANCE_METHODS_TRIEvaluationStatusCursor
- __OBJC_$_INSTANCE_METHODS_TRIEvaluationStatusDefaultProvider
- __OBJC_$_INSTANCE_METHODS_TRIExternalParameterGuardedData
- __OBJC_$_INSTANCE_METHODS_TRIExternalParameterManager
- __OBJC_$_INSTANCE_METHODS_TRIFactorsStateBMLTIdentifiers
- __OBJC_$_INSTANCE_METHODS_TRIFactorsStateRolloutIdentifiers
- __OBJC_$_INSTANCE_METHODS_TRILogger
- __OBJC_$_INSTANCE_METHODS_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_$_INSTANCE_METHODS_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_$_INSTANCE_METHODS_TRINamespaceResolverGuardedData
- __OBJC_$_INSTANCE_METHODS_TRIPETLogHandler
- __OBJC_$_INSTANCE_METHODS_TRIPartialBMLTRecord
- __OBJC_$_INSTANCE_METHODS_TRIRolloutFactorsState
- __OBJC_$_INSTANCE_METHODS_TRISystemConfiguration
- __OBJC_$_INSTANCE_METHODS_TRISystemInfo
- __OBJC_$_INSTANCE_METHODS_TRISystemInfoGuardedData
- __OBJC_$_INSTANCE_METHODS_TRIVersionedNamespace
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTActiveEvaluationTuple
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTDeployment
- __OBJC_$_INSTANCE_VARIABLES_TRIBMLTFactorsState
- __OBJC_$_INSTANCE_VARIABLES_TRIBackgroundMLTaskHistoryRecord
- __OBJC_$_INSTANCE_VARIABLES_TRIBackgroundMLTaskIdentifiers
- __OBJC_$_INSTANCE_VARIABLES_TRIBiomeDataStreamProvider
- __OBJC_$_INSTANCE_VARIABLES_TRICellularParameterGuardedData
- __OBJC_$_INSTANCE_VARIABLES_TRICellularParameterManager
- __OBJC_$_INSTANCE_VARIABLES_TRIEvaluationStatus
- __OBJC_$_INSTANCE_VARIABLES_TRIEvaluationStatusCursor
- __OBJC_$_INSTANCE_VARIABLES_TRIEvaluationStatusDefaultProvider
- __OBJC_$_INSTANCE_VARIABLES_TRIExternalParameterGuardedData
- __OBJC_$_INSTANCE_VARIABLES_TRIExternalParameterManager
- __OBJC_$_INSTANCE_VARIABLES_TRIFactorsStateBMLTIdentifiers
- __OBJC_$_INSTANCE_VARIABLES_TRIFactorsStateRolloutIdentifiers
- __OBJC_$_INSTANCE_VARIABLES_TRILogger
- __OBJC_$_INSTANCE_VARIABLES_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_$_INSTANCE_VARIABLES_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_$_INSTANCE_VARIABLES_TRINamespaceResolverGuardedData
- __OBJC_$_INSTANCE_VARIABLES_TRIPartialBMLTRecord
- __OBJC_$_INSTANCE_VARIABLES_TRIRolloutFactorsState
- __OBJC_$_INSTANCE_VARIABLES_TRISystemConfiguration
- __OBJC_$_INSTANCE_VARIABLES_TRISystemInfo
- __OBJC_$_INSTANCE_VARIABLES_TRISystemInfoGuardedData
- __OBJC_$_PROP_LIST_TRIBMLTActiveEvaluationTuple
- __OBJC_$_PROP_LIST_TRIBMLTDeployment
- __OBJC_$_PROP_LIST_TRIBMLTFactorsState
- __OBJC_$_PROP_LIST_TRIBackgroundMLTaskHistoryRecord
- __OBJC_$_PROP_LIST_TRIBackgroundMLTaskIdentifiers
- __OBJC_$_PROP_LIST_TRICellularParameterManager
- __OBJC_$_PROP_LIST_TRIEvaluationStatus
- __OBJC_$_PROP_LIST_TRIEvaluationStatusCursor
- __OBJC_$_PROP_LIST_TRIExternalParameterManager
- __OBJC_$_PROP_LIST_TRIFactorsStateBMLTIdentifiers
- __OBJC_$_PROP_LIST_TRIFactorsStateRolloutIdentifiers
- __OBJC_$_PROP_LIST_TRILogger
- __OBJC_$_PROP_LIST_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_$_PROP_LIST_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_$_PROP_LIST_TRIPETLogHandler
- __OBJC_$_PROP_LIST_TRIPartialBMLTRecord
- __OBJC_$_PROP_LIST_TRIPersistedBMLTFactorsState
- __OBJC_$_PROP_LIST_TRIPersistedEvaluationStatus
- __OBJC_$_PROP_LIST_TRIPersistedRolloutFactorsState
- __OBJC_$_PROP_LIST_TRIRolloutFactorsState
- __OBJC_$_PROP_LIST_TRISystemInfo
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientCarrierBundleDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientDataDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientSubscriberDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIEvaluationStatusProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIExternalParameterProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRILogHandling
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TRIXPCInternalSystemServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientCarrierBundleDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientDataDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientSubscriberDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_TRIEvaluationStatusProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_TRIExternalParameterProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_TRILogHandling
- __OBJC_$_PROTOCOL_METHOD_TYPES_TRIXPCInternalSystemServiceProtocol
- __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientCarrierBundleDelegate
- __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientDataDelegate
- __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientSubscriberDelegate
- __OBJC_$_PROTOCOL_REFS_TRILogHandling
- __OBJC_CLASS_PROTOCOLS_$_TRIBMLTActiveEvaluationTuple
- __OBJC_CLASS_PROTOCOLS_$_TRIBMLTDeployment
- __OBJC_CLASS_PROTOCOLS_$_TRIBackgroundMLTaskHistoryRecord
- __OBJC_CLASS_PROTOCOLS_$_TRIBackgroundMLTaskIdentifiers
- __OBJC_CLASS_PROTOCOLS_$_TRIBiomeDataStreamProvider
- __OBJC_CLASS_PROTOCOLS_$_TRICellularParameterManager
- __OBJC_CLASS_PROTOCOLS_$_TRIEvaluationStatus
- __OBJC_CLASS_PROTOCOLS_$_TRIEvaluationStatusCursor
- __OBJC_CLASS_PROTOCOLS_$_TRIEvaluationStatusDefaultProvider
- __OBJC_CLASS_PROTOCOLS_$_TRIFactorsStateBMLTIdentifiers
- __OBJC_CLASS_PROTOCOLS_$_TRIFactorsStateRolloutIdentifiers
- __OBJC_CLASS_PROTOCOLS_$_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_CLASS_PROTOCOLS_$_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_CLASS_PROTOCOLS_$_TRIPETLogHandler
- __OBJC_CLASS_PROTOCOLS_$_TRIPartialBMLTRecord
- __OBJC_CLASS_PROTOCOLS_$_TRISystemInfo
- __OBJC_CLASS_RO_$_TRIBMLTActiveEvaluationTuple
- __OBJC_CLASS_RO_$_TRIBMLTDeployment
- __OBJC_CLASS_RO_$_TRIBMLTFactorsState
- __OBJC_CLASS_RO_$_TRIBackgroundMLTaskHistoryRecord
- __OBJC_CLASS_RO_$_TRIBackgroundMLTaskIdentifiers
- __OBJC_CLASS_RO_$_TRIBiomeDataStreamProvider
- __OBJC_CLASS_RO_$_TRICKServerEnvironmentReader
- __OBJC_CLASS_RO_$_TRICellularParameterGuardedData
- __OBJC_CLASS_RO_$_TRICellularParameterManager
- __OBJC_CLASS_RO_$_TRIEvaluationStatus
- __OBJC_CLASS_RO_$_TRIEvaluationStatusCursor
- __OBJC_CLASS_RO_$_TRIEvaluationStatusDefaultProvider
- __OBJC_CLASS_RO_$_TRIExternalParameterGuardedData
- __OBJC_CLASS_RO_$_TRIExternalParameterManager
- __OBJC_CLASS_RO_$_TRIFactorsStateBMLTIdentifiers
- __OBJC_CLASS_RO_$_TRIFactorsStateRolloutIdentifiers
- __OBJC_CLASS_RO_$_TRILogger
- __OBJC_CLASS_RO_$_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_CLASS_RO_$_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_CLASS_RO_$_TRINamespaceLogPolicy
- __OBJC_CLASS_RO_$_TRINamespaceResolverGuardedData
- __OBJC_CLASS_RO_$_TRIPETLogHandler
- __OBJC_CLASS_RO_$_TRIPartialBMLTRecord
- __OBJC_CLASS_RO_$_TRIPersistedBMLTFactorsState
- __OBJC_CLASS_RO_$_TRIPersistedEvaluationStatus
- __OBJC_CLASS_RO_$_TRIPersistedRolloutFactorsState
- __OBJC_CLASS_RO_$_TRIRolloutFactorsState
- __OBJC_CLASS_RO_$_TRISystemConfiguration
- __OBJC_CLASS_RO_$_TRISystemInfo
- __OBJC_CLASS_RO_$_TRISystemInfoGuardedData
- __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientCarrierBundleDelegate
- __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientDataDelegate
- __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientSubscriberDelegate
- __OBJC_LABEL_PROTOCOL_$_TRIEvaluationStatusProvider
- __OBJC_LABEL_PROTOCOL_$_TRIExternalParameterProviding
- __OBJC_LABEL_PROTOCOL_$_TRILogHandling
- __OBJC_LABEL_PROTOCOL_$_TRIXPCInternalSystemServiceProtocol
- __OBJC_METACLASS_RO_$_TRIBMLTActiveEvaluationTuple
- __OBJC_METACLASS_RO_$_TRIBMLTDeployment
- __OBJC_METACLASS_RO_$_TRIBMLTFactorsState
- __OBJC_METACLASS_RO_$_TRIBackgroundMLTaskHistoryRecord
- __OBJC_METACLASS_RO_$_TRIBackgroundMLTaskIdentifiers
- __OBJC_METACLASS_RO_$_TRIBiomeDataStreamProvider
- __OBJC_METACLASS_RO_$_TRICKServerEnvironmentReader
- __OBJC_METACLASS_RO_$_TRICellularParameterGuardedData
- __OBJC_METACLASS_RO_$_TRICellularParameterManager
- __OBJC_METACLASS_RO_$_TRIEvaluationStatus
- __OBJC_METACLASS_RO_$_TRIEvaluationStatusCursor
- __OBJC_METACLASS_RO_$_TRIEvaluationStatusDefaultProvider
- __OBJC_METACLASS_RO_$_TRIExternalParameterGuardedData
- __OBJC_METACLASS_RO_$_TRIExternalParameterManager
- __OBJC_METACLASS_RO_$_TRIFactorsStateBMLTIdentifiers
- __OBJC_METACLASS_RO_$_TRIFactorsStateRolloutIdentifiers
- __OBJC_METACLASS_RO_$_TRILogger
- __OBJC_METACLASS_RO_$_TRIMLRuntimeActiveEvaluationTuple
- __OBJC_METACLASS_RO_$_TRIMLRuntimeEvaluationHistoryRecord
- __OBJC_METACLASS_RO_$_TRINamespaceLogPolicy
- __OBJC_METACLASS_RO_$_TRINamespaceResolverGuardedData
- __OBJC_METACLASS_RO_$_TRIPETLogHandler
- __OBJC_METACLASS_RO_$_TRIPartialBMLTRecord
- __OBJC_METACLASS_RO_$_TRIPersistedBMLTFactorsState
- __OBJC_METACLASS_RO_$_TRIPersistedEvaluationStatus
- __OBJC_METACLASS_RO_$_TRIPersistedRolloutFactorsState
- __OBJC_METACLASS_RO_$_TRIRolloutFactorsState
- __OBJC_METACLASS_RO_$_TRISystemConfiguration
- __OBJC_METACLASS_RO_$_TRISystemInfo
- __OBJC_METACLASS_RO_$_TRISystemInfoGuardedData
- __OBJC_PROTOCOL_$_CoreTelephonyClientCarrierBundleDelegate
- __OBJC_PROTOCOL_$_CoreTelephonyClientDataDelegate
- __OBJC_PROTOCOL_$_CoreTelephonyClientSubscriberDelegate
- __OBJC_PROTOCOL_$_TRIEvaluationStatusProvider
- __OBJC_PROTOCOL_$_TRIExternalParameterProviding
- __OBJC_PROTOCOL_$_TRILogHandling
- __OBJC_PROTOCOL_$_TRIXPCInternalSystemServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_TRIXPCInternalSystemServiceProtocol
- __ZN5apple4aiml12flatbuffers214DetachedBufferD2Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110__function12__value_funcIFN5apple4aiml12flatbuffers26OffsetIvEEmEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvmP10BoxedInt64EED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvmP11BoxedDoubleEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvmP9BoxedBoolEED2B8ne190102Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI11FactorLevelEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetI22FactorMetadataKeyValueEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__125__throw_bad_function_callB8ne190102Ev
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEbT1_SD_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEjT1_SD_SD_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI11FactorLevelEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERN5apple4aiml12flatbuffers217FlatBufferBuilder18TableKeyComparatorI22FactorMetadataKeyValueEEPNS4_6OffsetIS7_EEEEvT1_SD_SD_SD_SD_T0_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZTIN5apple4aiml12flatbuffers210objc_apple18AllocatorExceptionE
- __ZTSN5apple4aiml12flatbuffers210objc_apple18AllocatorExceptionE
- __Znwm
- ___101-[TRIEvaluationStatusDefaultProvider enumerateStatusOfEvaluationsForMLRuntimeWithCursor:error:block:]_block_invoke
- ___101-[TRIEvaluationStatusDefaultProvider enumerateStatusOfEvaluationsForMLRuntimeWithCursor:error:block:]_block_invoke_2
- ___101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.183
- ___109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.194
- ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.174
- ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.175
- ___131-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:]_block_invoke
- ___131-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:]_block_invoke_2
- ___131-[TRIAllocationStatusDefaultProvider enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:]_block_invoke_3
- ___139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.228
- ___139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.229
- ___139-[TRIClient _registerUpdateHandlerForNamespaceName:notificationCallback:clientMethodNameForLogging:callingFunctionReturnAddressForLogging:]_block_invoke.230
- ___203+[TRIFactorDownloadValidator validateDownloadForFactors:withNamespace:paths:container:factorsState:assetIndexesByTreatment:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:error:]_block_invoke.104
- ___24+[TRISystemInfo _hasAne]_block_invoke
- ___28+[TRISystemInfo _aneVersion]_block_invoke
- ___31-[TRILogger _dispatchLogEvent:]_block_invoke
- ___31-[TRINamespaceResolver dispose]_block_invoke
- ___31-[TRINamespaceResolver dispose]_block_invoke_2
- ___33-[TRISystemConfiguration osBuild]_block_invoke
- ___34+[TRISystemInfo _isVirtualMachine]_block_invoke
- ___36+[TRIClient printedBMLTInformation:]_block_invoke
- ___37+[TRIClient _sysdiagnoseLogProviders]_block_invoke_2
- ___37+[TRIClient _sysdiagnoseLogProviders]_block_invoke_3
- ___37+[TRIClient _sysdiagnoseLogProviders]_block_invoke_4
- ___37+[TRIStandardPaths sharedSystemPaths]_block_invoke
- ___37-[TRISystemConfiguration deviceClass]_block_invoke
- ___37-[TRISystemInfo externalParamManager]_block_invoke
- ___38+[TRIEvaluationStatus defaultProvider]_block_invoke
- ___38-[TRILogger _incrementedLogEventCount]_block_invoke
- ___39+[TRIClient printedRolloutInformation:]_block_invoke
- ___40+[TRISystemConfiguration sharedInstance]_block_invoke
- ___41-[TRIExternalParameterManager dictionary]_block_invoke
- ___41-[TRISystemConfiguration deviceModelCode]_block_invoke
- ___42-[TRIAllocationStatusDefaultProvider init]_block_invoke
- ___42-[TRIAllocationStatusDefaultProvider init]_block_invoke_2
- ___42-[TRIAllocationStatusDefaultProvider init]_block_invoke_3
- ___42-[TRIAllocationStatusDefaultProvider init]_block_invoke_4
- ___42-[TRIEvaluationStatusDefaultProvider init]_block_invoke
- ___42-[TRIEvaluationStatusDefaultProvider init]_block_invoke_2
- ___42-[TRISystemConfiguration reloadSystemInfo]_block_invoke
- ___43+[TRISystemConfiguration _sharedSystemInfo]_block_invoke
- ___44-[TRISystemConfiguration _updateSystemInfo:]_block_invoke
- ___45+[TRICellularParameterManager sharedInstance]_block_invoke
- ___46-[TRINamespaceResolver _faultOnceWithMessage:]_block_invoke
- ___48+[TRISystemInfo _sysEnabledInputModeIdentifiers]_block_invoke
- ___48+[TRISystemInfo _sysEnabledInputModeIdentifiers]_block_invoke_2
- ___48-[TRIPETLogHandler logEvent:subgroupName:queue:]_block_invoke
- ___49-[TRISystemConfiguration _systemInfoWithIsStale:]_block_invoke
- ___51-[TRICellularParameterManager carrierBundleChange:]_block_invoke
- ___52-[TRICellularParameterManager carrierCountryIsoCode]_block_invoke
- ___54-[TRICellularParameterManager carrierBundleIdentifier]_block_invoke
- ___54-[TRIExternalParameterManager initWithProvider:paths:]_block_invoke
- ___55-[TRIBiomeDataStreamProvider unsubscribeAllDataStreams]_block_invoke
- ___55-[TRICellularParameterManager preferredDataSimChanged:]_block_invoke
- ___61-[TRINamespaceFactorProvider _readAllFactorLevelsFromStorage]_block_invoke_3
- ___62-[TRICellularParameterManager subscriberCountryCodeDidChange:]_block_invoke
- ___62-[TRINamespaceFactorProvider overlayLevelsFromFactorProvider:]_block_invoke
- ___63-[TRIClient sizesForFactors:withNamespaceName:forMetric:error:]_block_invoke.275
- ___63-[TRISystemConfiguration _dispatchQueueForCarrierInfoGathering]_block_invoke
- ___64+[TRIClient printedExperimentInformationWithEnvironments:error:]_block_invoke
- ___66-[TRIExternalParameterManager siriDeviceAggregationIdRotationDate]_block_invoke
- ___68-[TRICellularParameterManager _dispatchQueueForCarrierInfoGathering]_block_invoke
- ___69-[TRIAllocationStatusDefaultProvider activeBMLTInformationWithError:]_block_invoke
- ___69-[TRIAllocationStatusDefaultProvider activeBMLTInformationWithError:]_block_invoke_2
- ___71-[TRINamespaceResolver _resolveTargetedFactorPackSetForBMLTDeployment:]_block_invoke
- ___72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke
- ___72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.33
- ___72-[TRIExternalParameterManager _fetchSiriDeviceAggregationIdRotationDate]_block_invoke.35
- ___73-[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]_block_invoke
- ___73-[TRIBiomeDataStreamProvider _subscribeForStreamIdentifier:eventHandler:]_block_invoke.20
- ___73-[TRIEvaluationStatusDefaultProvider enumerateActiveBMLTWithError:block:]_block_invoke
- ___73-[TRIEvaluationStatusDefaultProvider enumerateActiveBMLTWithError:block:]_block_invoke_2
- ___76-[TRIBiomeDataStreamProvider subscribeDataStreamForIdentifier:eventHandler:]_block_invoke
- ___80-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]_block_invoke
- ___80-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:eventHandler:]_block_invoke.9
- ___86-[TRIClient statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:]_block_invoke.319
- ___86-[TRINamespaceResolver _resolveTargetedNamespaceDescriptorSetForExperimentDeployment:]_block_invoke
- ___91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke
- ___91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke.13
- ___91-[TRIBiomeDataStreamProvider readLastDataStreamEventForIdentifier:withFilter:eventHandler:]_block_invoke_2
- ___92-[TRIEvaluationStatusDefaultProvider enumerateActiveEvaluationsForMLRuntimeWithError:block:]_block_invoke
- ___92-[TRIEvaluationStatusDefaultProvider enumerateActiveEvaluationsForMLRuntimeWithError:block:]_block_invoke_2
- ___AppleNeuralEngineLibraryCore_block_invoke
- ___Block_byref_object_copy_.638
- ___Block_byref_object_dispose_.639
- ___CoreTelephonyLibraryCore_block_invoke
- ___TextInputLibraryCore_block_invoke
- ___block_descriptor_32_e41_v16?0"TRINamespaceResolverGuardedData"8l
- ___block_descriptor_32_e58_v32?0"TRIBMLTDeployment"8"TRILockedFactorPackSet"16^B24l
- ___block_descriptor_40_e8_32bs_e22_B16?0"BMStoreEvent"8ls32l8
- ___block_descriptor_40_e8_32bs_e22_v16?0"BMStoreEvent"8ls32l8
- ___block_descriptor_40_e8_32bs_e23_v16?0"BPSCompletion"8ls32l8
- ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
- ___block_descriptor_40_e8_32r_e34_v16?0"TRISystemInfoGuardedData"8lr32l8
- ___block_descriptor_40_e8_32r_e41_v16?0"TRICellularParameterGuardedData"8lr32l8
- ___block_descriptor_40_e8_32r_e41_v16?0"TRIExternalParameterGuardedData"8lr32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e22_B16?0"NSDictionary"8ls32l8
- ___block_descriptor_40_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e41_v16?0"TRIExternalParameterGuardedData"8ls32l8
- ___block_descriptor_40_e8_32s_e41_v16?0"TRINamespaceResolverGuardedData"8ls32l8
- ___block_descriptor_48_e5_v8?0l
- ___block_descriptor_48_e8_32r_e34_v16?0"TRISystemInfoGuardedData"8lr32l8
- ___block_descriptor_48_e8_32s40r_e34_v16?0"TRISystemInfoGuardedData"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e41_v16?0"TRICellularParameterGuardedData"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e41_v16?0"TRIExternalParameterGuardedData"8ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48r_e41_v16?0"TRINamespaceResolverGuardedData"8lr48l8s32l8s40l8
- ___block_literal_global.104
- ___block_literal_global.106
- ___block_literal_global.109
- ___block_literal_global.113
- ___block_literal_global.117
- ___block_literal_global.12
- ___block_literal_global.139
- ___block_literal_global.141
- ___block_literal_global.143
- ___block_literal_global.145
- ___block_literal_global.147
- ___block_literal_global.15
- ___block_literal_global.160
- ___block_literal_global.164
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.18
- ___block_literal_global.182
- ___block_literal_global.188
- ___block_literal_global.196
- ___block_literal_global.198
- ___block_literal_global.201
- ___block_literal_global.21
- ___block_literal_global.23
- ___block_literal_global.277
- ___block_literal_global.30
- ___block_literal_global.301
- ___block_literal_global.315
- ___block_literal_global.321
- ___block_literal_global.35
- ___block_literal_global.4
- ___block_literal_global.481
- ___block_literal_global.529
- ___block_literal_global.535
- ___block_literal_global.540
- ___block_literal_global.545
- ___block_literal_global.6
- ___block_literal_global.72
- ___block_literal_global.74
- ___block_literal_global.9
- ___block_literal_global.91
- ___getCTBundleClass_block_invoke
- ___getCoreTelephonyClientClass_block_invoke
- ___getTIInputModeControllerClass_block_invoke
- ___get_ANEDeviceInfoClass_block_invoke
- __sl_dlopen
- _audit_stringAppleNeuralEngine
- _audit_stringCoreTelephony
- _audit_stringTextInput
- _descriptor.descriptor.27
- _descriptor.descriptor.44
- _descriptor.descriptor.54
- _descriptor.descriptor.64
- _descriptor.fields.28
- _descriptor.fields.45
- _descriptor.fields.55
- _dispatch_assert_queue$V2
- _dispatch_sync
- _dlopen
- _dlopenHelper$Accounts
- _dlopenHelper$AppleAccount
- _dlopenHelper$GenerativeModels
- _dlopenHelperFlag$Accounts
- _dlopenHelperFlag$AppleAccount
- _dlopenHelperFlag$GenerativeModels
- _dummyValue
- _getCTBundleClass.softClass
- _getCoreTelephonyClientClass.softClass
- _get_ANEDeviceInfoClass
- _gotLoadHelper_x8$_AAErrorDomain
- _gotLoadHelper_x8$_OBJC_CLASS_$_ACAccountStore
- _gotLoadHelper_x8$_OBJC_CLASS_$_GMAvailabilityWrapper
- _kTRIEvaluationStatusEntitlement
- _objc_getClass
- _objc_msgSend$DSLPublisher
- _objc_msgSend$_aneVersion
- _objc_msgSend$_appleIntelligenceState
- _objc_msgSend$_bmltIdentifiersWithNamespaceName:
- _objc_msgSend$_carrierBundleIdentifier
- _objc_msgSend$_carrierCountryIsoCode
- _objc_msgSend$_defaultProvider
- _objc_msgSend$_dispatchLogEvent:
- _objc_msgSend$_dispatchQueueForCarrierInfoGathering
- _objc_msgSend$_factorProviderForNamespaceName:fromNamespaceDescriptorSetWithDir:resolvedPath:
- _objc_msgSend$_fetchCarrierBundleIdentifier:
- _objc_msgSend$_fetchCarrierCountryIsoCode:
- _objc_msgSend$_fetchSiriDeviceAggregationIdRotationDate
- _objc_msgSend$_getSiriDeviceAggregationIdRotationDate
- _objc_msgSend$_hasAne
- _objc_msgSend$_hasBMLTFactorsState
- _objc_msgSend$_hasCounterfactualFactorsState
- _objc_msgSend$_hasExperimentFactorsState
- _objc_msgSend$_hasRolloutFactorsState
- _objc_msgSend$_iCloudIdentifier
- _objc_msgSend$_incrementedLogEventCount
- _objc_msgSend$_isAutomatedTestDevice
- _objc_msgSend$_isDiagnosticsAndUsageEnabled
- _objc_msgSend$_isSeedBuild
- _objc_msgSend$_isVirtualMachine
- _objc_msgSend$_logBMLTCustomTargetingWithResult:
- _objc_msgSend$_persistentSystemInfoPath
- _objc_msgSend$_prepareFactorsStateForCounterfactualsForFactorsState:
- _objc_msgSend$_prepareFactorsStateForExperimentsOnFactorPackSetPathForDeployment:
- _objc_msgSend$_prepareFactorsStateForExperimentsOnTreatmentPathForDeployment:
- _objc_msgSend$_readParametersFromFile
- _objc_msgSend$_readSiriDeviceAggregationIdRotationDateFromEvent:
- _objc_msgSend$_resolveTargetedFactorPackSetForBMLTDeployment:
- _objc_msgSend$_resolveTargetedNamespaceDescriptorSetForExperimentDeployment:
- _objc_msgSend$_sharedSystemInfo
- _objc_msgSend$_siriUserActivitySegment
- _objc_msgSend$_subscribeForStreamIdentifier:eventHandler:
- _objc_msgSend$_sysEnabledInputModeIdentifiers
- _objc_msgSend$_sysIsEnrolledInBetaProgram
- _objc_msgSend$_systemInfoWithIsStale:
- _objc_msgSend$_trialVersion
- _objc_msgSend$_unsubscribeAllDataStreams
- _objc_msgSend$_updateSystemInfo
- _objc_msgSend$_writeParametersToFile
- _objc_msgSend$aa_altDSID
- _objc_msgSend$aa_primaryAppleAccount
- _objc_msgSend$activeBMLTInformation:
- _objc_msgSend$activeBMLTInformationWithError:
- _objc_msgSend$activeBMLTInformationWithPrivacyFilterPolicy:completion:
- _objc_msgSend$activeEvaluationsForBMLTWithCompletion:
- _objc_msgSend$activeEvaluationsForMLRuntimeWithCompletion:
- _objc_msgSend$activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:
- _objc_msgSend$activeRolloutInformationWithPrivacyFilterPolicy:completion:
- _objc_msgSend$addNamespaceName:
- _objc_msgSend$aneSubType
- _objc_msgSend$aneVersion
- _objc_msgSend$appleIntelligenceState
- _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$assignmentExpression
- _objc_msgSend$automatedDeviceGroup
- _objc_msgSend$backgroundMLTaskId
- _objc_msgSend$bmlt
- _objc_msgSend$bmltDeployment
- _objc_msgSend$bmltDeploymentForFactorsState
- _objc_msgSend$bmltDeploymentWithNamespaceName:
- _objc_msgSend$bmltId
- _objc_msgSend$bmltIdentifiers
- _objc_msgSend$bmltTaskId
- _objc_msgSend$cancel
- _objc_msgSend$carrierBundleIdentifier
- _objc_msgSend$carrierCountryIsoCode
- _objc_msgSend$clientWithIdentifier:unit:
- _objc_msgSend$context
- _objc_msgSend$copyBundleIdentifier:bundleType:error:
- _objc_msgSend$copyLastKnownMobileSubscriberCountryCode:error:
- _objc_msgSend$copyMobileSubscriberIsoCountryCode:error:
- _objc_msgSend$countryCode
- _objc_msgSend$createDeviceIdentifierWithPath:
- _objc_msgSend$createPersistentDeviceIdentifier
- _objc_msgSend$createSystemInfoWithFactorProvider:
- _objc_msgSend$currentCalendar
- _objc_msgSend$currentLocale
- _objc_msgSend$currentPopulation
- _objc_msgSend$currentWithUseCaseIdentifiers:
- _objc_msgSend$dateWithTimeIntervalSince1970:
- _objc_msgSend$defaultStore
- _objc_msgSend$deleteDeviceIdentifier
- _objc_msgSend$deleteDeviceIdentifierWithPath:
- _objc_msgSend$deviceClass
- _objc_msgSend$deviceIdentifierFile
- _objc_msgSend$deviceInfoForQuestion:
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$enabledInputModeIdentifiers
- _objc_msgSend$ensureBMLTFields
- _objc_msgSend$ensureExperimentFields
- _objc_msgSend$ensureRolloutFields
- _objc_msgSend$enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:
- _objc_msgSend$eval
- _objc_msgSend$evalState
- _objc_msgSend$evaluation
- _objc_msgSend$evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:
- _objc_msgSend$evaluationId
- _objc_msgSend$eventBody
- _objc_msgSend$eventWithTrackingId:projectId:
- _objc_msgSend$experimentDeploymentForFactorsState
- _objc_msgSend$experimentFactorsStateForCounterfactuals
- _objc_msgSend$experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:
- _objc_msgSend$experimentIdentifiersWithNamespaceName:
- _objc_msgSend$experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:
- _objc_msgSend$expressionValueWithObject:context:
- _objc_msgSend$expressionWithFormat:
- _objc_msgSend$externalParamManager
- _objc_msgSend$externalParametersFile
- _objc_msgSend$factorPackIdForBmltWithNamespaceName:
- _objc_msgSend$factorProviderWithPaths:namespaceName:resolver:
- _objc_msgSend$factorsState
- _objc_msgSend$filterWithIsIncluded:
- _objc_msgSend$freshProvider
- _objc_msgSend$getPreferredDataSubscriptionContextSync:
- _objc_msgSend$hasANE
- _objc_msgSend$hasAne
- _objc_msgSend$hasAssignmentExpression
- _objc_msgSend$hasBmltId
- _objc_msgSend$hasEvalState
- _objc_msgSend$hasEvaluationId
- _objc_msgSend$hasTrialSystemTelemetry
- _objc_msgSend$iCloudIdentifier
- _objc_msgSend$info
- _objc_msgSend$initFromSystemWithFactorProvider:
- _objc_msgSend$initWithBMLTId:deploymentId:
- _objc_msgSend$initWithBMLTTaskId:deploymentId:treatmentId:
- _objc_msgSend$initWithBMLTaskId:deploymentId:factorPackId:
- _objc_msgSend$initWithBackgroundMLTaskId:deploymentId:
- _objc_msgSend$initWithBmlt:factorsState:
- _objc_msgSend$initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:
- _objc_msgSend$initWithBundleType:
- _objc_msgSend$initWithClient:projectId:logHandlers:
- _objc_msgSend$initWithClientIdentifier:paths:unit:factorsState:staleFactorsUsageGracePeriod:logger:
- _objc_msgSend$initWithClientIdentifier:paths:unit:staleFactorsUsageGracePeriod:logger:
- _objc_msgSend$initWithCurrentSchemaVersion
- _objc_msgSend$initWithDeployment:
- _objc_msgSend$initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:
- _objc_msgSend$initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:
- _objc_msgSend$initWithEval:factorsState:
- _objc_msgSend$initWithEvaluation:status:
- _objc_msgSend$initWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:
- _objc_msgSend$initWithIdentifier:targetQueue:waking:
- _objc_msgSend$initWithProjectId:
- _objc_msgSend$initWithProvider:paths:
- _objc_msgSend$initWithQueue:
- _objc_msgSend$initWithSchemaVersion:
- _objc_msgSend$initWithSchemaVersion:container:asClientProcess:
- _objc_msgSend$initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:
- _objc_msgSend$initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:interruptionHandler:invalidationHandler:logHandle:
- _objc_msgSend$initWithString:
- _objc_msgSend$initWithType:evaluationId:date:evalState:
- _objc_msgSend$isAutomatedTestDevice
- _objc_msgSend$isBetaBuild
- _objc_msgSend$isBetaUserWithIsStale:
- _objc_msgSend$isDiagnosticsAndUsageEnabled
- _objc_msgSend$isEnrolledInBetaProgram
- _objc_msgSend$isEqualToBMLTTaskIdentifiers:
- _objc_msgSend$isEqualToTuple:
- _objc_msgSend$isShadow
- _objc_msgSend$json
- _objc_msgSend$languageCode
- _objc_msgSend$last
- _objc_msgSend$loadSystemInfo
- _objc_msgSend$logEvent:
- _objc_msgSend$logEvent:subgroupName:queue:
- _objc_msgSend$logMessage:
- _objc_msgSend$logMessage:subGroup:
- _objc_msgSend$logUserKeyboardEnabledInputMode
- _objc_msgSend$logUserSettingsLanguageCode
- _objc_msgSend$logUserSettingsRegionCode
- _objc_msgSend$logWithProjectNameAndTrackingId:metrics:dimensions:trialSystemTelemetry:
- _objc_msgSend$logWithTrackingId:metric:dimensions:
- _objc_msgSend$logWithTrackingId:metrics:dimensions:
- _objc_msgSend$logWithTrackingId:metrics:dimensions:trialSystemTelemetry:
- _objc_msgSend$metricWithName:
- _objc_msgSend$metricWithName:integerValue:
- _objc_msgSend$namespace
- _objc_msgSend$namespaceDescriptorsBMLTDir
- _objc_msgSend$namespaceDescriptorsRolloutDir
- _objc_msgSend$namespaceString
- _objc_msgSend$now
- _objc_msgSend$nsexpressionLanguage
- _objc_msgSend$operatingSystemVersion
- _objc_msgSend$optInApple
- _objc_msgSend$osBuild
- _objc_msgSend$parseVersionFromString:withPrefix:
- _objc_msgSend$pathsForContainer:asClientProcess:
- _objc_msgSend$persisted
- _objc_msgSend$pluginId
- _objc_msgSend$populationType
- _objc_msgSend$printedExperimentInformationWithEnvironments:error:
- _objc_msgSend$printedRolloutInformation:
- _objc_msgSend$projectNameFromId:
- _objc_msgSend$publisher
- _objc_msgSend$readDeviceIdentifierWithPath:
- _objc_msgSend$readLastDataStreamEventForIdentifier:withFilter:eventHandler:
- _objc_msgSend$reloadSystemInfo
- _objc_msgSend$requiresLogging
- _objc_msgSend$rollout
- _objc_msgSend$rolloutAllocationStatusWithPrivacyFilterPolicy:completion:
- _objc_msgSend$rolloutDeploymentForFactorsState
- _objc_msgSend$rolloutIdentifiers
- _objc_msgSend$save
- _objc_msgSend$saveToFile:
- _objc_msgSend$scanUpToString:intoString:
- _objc_msgSend$setAneVersion:
- _objc_msgSend$setAppleIntelligenceState:
- _objc_msgSend$setBmltId:
- _objc_msgSend$setCarrierBundleIdentifier:
- _objc_msgSend$setCarrierCountryIsoCode:
- _objc_msgSend$setClientBmltId:
- _objc_msgSend$setClientDeploymentId:
- _objc_msgSend$setClientExperimentId:
- _objc_msgSend$setClientProjectId:
- _objc_msgSend$setClientRolloutId:
- _objc_msgSend$setClientTreatmentId:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setDeviceClass:
- _objc_msgSend$setDeviceIdentifier:path:
- _objc_msgSend$setEvalState:
- _objc_msgSend$setEvaluationId:
- _objc_msgSend$setIsAutomatedTestDevice:
- _objc_msgSend$setLogger:
- _objc_msgSend$setMetrics:
- _objc_msgSend$setMlruntimeDimensions:
- _objc_msgSend$setOsBuild:
- _objc_msgSend$setProcessEventIndex:
- _objc_msgSend$setSystemDimensions:
- _objc_msgSend$setTargetedPopulation:
- _objc_msgSend$setTrialSystemTelemetry:
- _objc_msgSend$setUserDimensions:
- _objc_msgSend$setUserKeyboardEnabledInputModeIdentifiers:
- _objc_msgSend$setUserSettingsBcp47DeviceLocale:
- _objc_msgSend$setValue:
- _objc_msgSend$setVersionTag:
- _objc_msgSend$sharedInstance
- _objc_msgSend$sharedSystemPaths
- _objc_msgSend$shouldPrivacyFilterNamespace:policy:
- _objc_msgSend$sinkWithCompletion:receiveInput:
- _objc_msgSend$siriDeviceAggregationIdRotationDate
- _objc_msgSend$siriUserActivitySegment
- _objc_msgSend$state
- _objc_msgSend$storedDeviceIdentifier
- _objc_msgSend$streamWithIdentifier:error:
- _objc_msgSend$subscribeOn:
- _objc_msgSend$systemDataFile
- _objc_msgSend$systemDimensions
- _objc_msgSend$systemInfo
- _objc_msgSend$systemInfoFromFile:
- _objc_msgSend$trackingId
- _objc_msgSend$trialSystemTelemetry
- _objc_msgSend$trialVersionTag
- _objc_msgSend$unarchivedObjectOfClass:fromData:error:
- _objc_msgSend$unsubscribeAllDataStreams
- _objc_msgSend$userSettingsBCP47DeviceLocale
- _objc_msgSend$validatedEnvironmentFromNumber:
- _objc_msgSend$validatedPopulationFromNumber:
- _objc_msgSend$writeData:
- _objc_msgSend$writeToFile:atomically:encoding:error:
- _objc_retain_x5
- _objc_storeWeak
- _sysctlbyname
CStrings:
+ "            overrideLevel: %@"
+ "      namespaces: [%@]"
+ "%@.%u"
+ ".bin"
+ "<TRIPartialExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ experimentType:%@ counterfactualTreatmentIds:%@>"
+ "<TRIPartialRolloutRecord | deployment:%@ rampId:%@ activeFactorPackSetId:%@ activeTargetingRuleIndex:%@ targetedFactorPackSetId:%@ targetedTargetingRuleIndex:%@ status:%@ namespaces:%@>"
+ "@\"<TRINamespaceManagementProtocol>\""
+ "@\"TRIAllocationStatusDefaultProvider\""
+ "@16@?0@\"TRIVersionedNamespace\"8"
+ "@24@0:8i16B20"
+ "@28@0:8I16I20B24"
+ "@36@0:8@16@24B32"
+ "@52@0:8i16@20@28d36@44"
+ "@80@0:8@16@24@32@40@48@56q64@72"
+ "@92@0:8i16@20@28@36i44q48@56@64@72i80@84"
+ "Accessed union field \"TRIFBFastFactorLevels.sourceAsDefaults\", but the value stored in the union does not match this type."
+ "Accessed union field \"TRIFBFastFactorLevels.sourceAsDefaultsCString\", but the value stored in the union does not match this type."
+ "Accessed union field \"TRIFBFastFactorLevels.sourceAsDefaultsData\", but the value stored in the union does not match this type."
+ "Current population is %@ with population override: %@"
+ "Failed to create log file: %@"
+ "Failed to resolve targeted experiment factor pack set for factor state: %@"
+ "Invalid invocation of [TRIPaths pathsForUser:] Should call [TRIPaths sharedPaths]"
+ "Invalid invocation of [TRIPaths sharedPathsForSystem:] Should call [TRIPaths sharedPaths]"
+ "Loading namespace descriptor from path: %@"
+ "Looking for experiment identifiers for namespace name: %{private}@"
+ "Missing serialized value for TRIPartialExperimentRecord.experimentType"
+ "Protobuf treatment storage is disabled."
+ "Requested namespace descriptor %@ doesn't exist (for treatment layer: 0x%llx)"
+ "Retrying command... (attempt %ld)\n"
+ "StringFormatting"
+ "SystemInterop"
+ "T@\"TRIExperimentFactorsState\",R,N,V_overrideExperimentFactorsState"
+ "T@,R,N,V_logger"
+ "TB,R,N,V_forTrialdSystem"
+ "TB,R,N,V_optedOutOfDefaults"
+ "TRIActiveExperimentsSysdiagnoseProvider"
+ "TRIActiveRolloutsSysdiagnoseProvider"
+ "TRIFBSource_defaults"
+ "TRIXPCInternalAgentToSystemServiceProtocol"
+ "Ti,R,N,V_experimentType"
+ "TrialXP-463"
+ "Unable to acquire shared lock on managed-directory \"%@\": %s (%d). Please check for sandboxing errors if you see this repeatedly."
+ "Unable to derive factors URL without a path."
+ "Unable to get a valid UID, which may be because you attempted to run this command as root. Please log back in as a user and try again.\n"
+ "V1 Rollouts are deprecated. Cannot instantiate a TRINamespaceFactorProvider with a treatmentLayer type of TRITreatmentLayer_Rollout"
+ "Warning: Command timed out.\n"
+ "Wrong param provided to [TRIClient clientWithIdentifier:forTrialdSystem:] triald_system only exists on macOS"
+ "[[TRIClient alloc] initWithClientIdentifier:projectId paths:paths factorsState:nil staleFactorsUsageGracePeriod:kTwentyFourHoursInSeconds logger:nil]"
+ "_defaultProviderImpl"
+ "_environments"
+ "_experimentType"
+ "_fbs.bin"
+ "_filename"
+ "_forTrialdSystem"
+ "_forUserId"
+ "_getLogger"
+ "_hasOverrideExperimentFactorsState"
+ "_internalAgentToSystemHelper"
+ "_namespaceClient"
+ "_optedOutOfDefaults"
+ "_overrideExperimentFactorsState"
+ "_prepareFactorsStateForCounterfactualsOrInvestigationsForFactorsState:"
+ "_resolverPropertyListWithGlobalRolloutsResolvedPath:"
+ "_statusProvider"
+ "activeExperimentInformationWithEnvironments:completion:"
+ "activeRolloutInformationWithCompletion:"
+ "addWithoutRunningForTask:options:completion:"
+ "added update handler %lu for namespace %@ — now %lu handlers for this namespace"
+ "allowEnvVarDefaultLevelsDir"
+ "appendBytes:length:"
+ "bin"
+ "callerBundleId"
+ "callerIsRunningFromSystemContext"
+ "client"
+ "clientForTrialdSystem:"
+ "clientTreatmentWithFactorLevels:parentDir:isRelativePath:"
+ "clientWithIdentifier:forTrialdSystem:"
+ "com.apple.trial.system.status"
+ "com.apple.triald.override.as_system_context"
+ "com.apple.triald.system.from-agent"
+ "copyWithReplacementExperimentType:"
+ "dispatching updates to %lu callbacks"
+ "experimentHistoryRecordsWithLimit:newerThanDate:deploymentEnvironment:completion:"
+ "experimentRecordsWithDeploymentEnvironments:completion:"
+ "experimentType"
+ "factorProviderWithPaths:namespaceName:resolver:faultOnMissingInstalledFactors:"
+ "factorsPath"
+ "factorsURLFromPath:"
+ "flatbufferLevelForFactor:"
+ "forLaunchDaemon"
+ "forTrialdSystem"
+ "hostingProcessName"
+ "i48@0:8@16@24q32d40"
+ "initForTrialdSystem:"
+ "initWithAllocationStatusProvider:outputFilename:environments:"
+ "initWithClientIdentifier:paths:factorsState:staleFactorsUsageGracePeriod:logger:"
+ "initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:"
+ "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:"
+ "initWithNamespaceManagementClient:"
+ "initWithSchemaVersion:forUser:forTrialdSystem:"
+ "initWithServiceName:connectionOptions:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:"
+ "isOptedOutOfExperimentation"
+ "isOptedOutOfExperimentationWithCompletion:"
+ "lockedSet for counterfactuals or investigations unexpectedly not present"
+ "no experiments because the device is opted-out of experimentation"
+ "object"
+ "optedOutOfDefaults"
+ "overrideExperimentFactorsState"
+ "overrideFactorPackDeploymentMap"
+ "pathExtension"
+ "paths"
+ "pathsForUser:"
+ "plplist (global) contains bad experiment deployment: %@ for map: %@"
+ "plplist contains bad experiment deployment: %@ for map: %@"
+ "protobufLevelForFactor:"
+ "recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:"
+ "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:experimentType:counterfactualTreatmentIds:"
+ "removeLegacyProtobufTreatmentStorage"
+ "replaceSourceWithDefaults:"
+ "resumeTaskQueueWithCompletion:"
+ "rolloutAllocationStatusWithCompletion:"
+ "runCommand:withArgs:withTimesToAttemptOnTimeOut:withTimeOut:"
+ "self.overrideExperimentFactorsState"
+ "setSourceWithDefaults:"
+ "sharedPaths"
+ "sharedPathsForSystem"
+ "sourceAsDefaults"
+ "sourceAsDefaultsCString"
+ "sourceAsDefaultsData"
+ "stringByDeletingPathExtension"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "systemInteropDirectory"
+ "treatmentValidForExperimentWithId:treatmentId:completion:"
+ "triDataWithHexString:"
+ "unable to check opt-out status while device is class C locked qos:%{public}u"
+ "userFacingString"
+ "v2/globalActiveFactorProviders.plplist"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v44@0:8Q16@\"NSDate\"24i32@?<v@?@\"NSNumber\"@\"NSArray\"@\"NSDate\"@\"NSError\">36"
+ "v44@0:8Q16@24i32@?36"
- "    - bmlt: %@.%d"
- "  BMLT is no longer supported, and is no longer logged"
- "%@(deployment: %@.%d)"
- "%@-%@"
- "%s"
- "(unknown: %i)"
- "-[TRILogger initWithProjectId:]"
- "-[TRILogger logWithTrackingId:logLevel:message:]"
- "-[TRILogger logWithTrackingId:logLevel:message:args:]"
- "-[TRILogger logWithTrackingId:message:]"
- "-[TRILogger logWithTrackingId:metric:]"
- ".fb"
- "/System/Library/Frameworks/Accounts.framework/Accounts"
- "/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
- "/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels"
- "<%@,Siri device aggregation ID rotation date:%@>"
- "<%@,bundleId:%@,countryCode:%@>"
- "<TRIBMLTActiveEvaluationTuple | bmlt:%@ factorsState:%@>"
- "<TRIBMLTDeployment | backgroundMLTaskId:%@ deploymentId:%@>"
- "<TRIBackgroundMLTaskHistoryRecord | eventDate:%@ eventType:%@ backgroundMLTaskId:%@ deploymentId:%@ factorPackSetId:%@>"
- "<TRIBackgroundMLTaskIdentifiers | bmltTaskId:%@ deploymentId:%@ factorPackId:%@>"
- "<TRIBackgroundMLTaskIdentifiers | bmltTaskId:%@ deploymentId:%@ treatmentId:%@>"
- "<TRIFactorsStateBMLTIdentifiers | bmltId:%@ deploymentId:%@>"
- "<TRIFactorsStateRolloutIdentifiers | rolloutId:%@ deploymentId:%@>"
- "<TRIMLRuntimeActiveEvaluationTuple | eval:%@ factorsState:%@>"
- "<TRIMLRuntimeEvaluationHistoryRecord | evaluation:%@ status:%@>"
- "<TRIPartialBMLTRecord | bmltDeployment:%@ pluginId:%@ activeFactorPackSetId:%@ activeTargetingRuleIndex:%@ targetedFactorPackSetId:%@ targetedTargetingRuleIndex:%@ status:%@ endDate:%@ namespace:%@>"
- "<TRIPartialExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ isShadow:%@ counterfactualTreatmentIds:%@>"
- "<TRIPartialRolloutRecord | deployment:%@ rampId:%@ activeFactorPackSetId:%@ activeTargetingRuleIndex:%@ targetedFactorPackSetId:%@ targetedTargetingRuleIndex:%@ status:%@ namespaces:%@ isShadow:%@>"
- "<private>"
- "@\"<TRIExternalParameterProviding>\""
- "@\"<TRIPaths>\"28@0:8@\"TRIAppContainer\"16B24"
- "@\"CTXPCServiceSubscriptionContext\""
- "@\"CoreTelephonyClient\""
- "@\"TRIBMLTDeployment\""
- "@\"TRIClient\""
- "@\"TRIClientBackgroundMLTask\""
- "@\"TRIEvaluationStatus\""
- "@\"TRIEvaluationStatusCursor\"40@0:8@\"TRIEvaluationStatusCursor\"16^@24@?<v@?@\"TRIMLRuntimeEvaluation\"@\"TRIEvaluationStatus\"^B>32"
- "@\"TRILogger\""
- "@\"TRIMLRuntimeEvaluation\""
- "@\"TRISystemInfo\""
- "@24@0:8^B16"
- "@24@0:8i16i20"
- "@32@0:8I16@20B28"
- "@40@0:8@16@24^@32"
- "@40@0:8@16^@24@?32"
- "@44@0:8C16@20@28@36"
- "@48@0:8@16C24@28i36@40"
- "@48@0:8i16@20i28d32@40"
- "@48@0:8i16C20@24^@32@?40"
- "@56@0:8i16@20i28@32d40@48"
- "@84@0:8@16@24@32@40@48@56q64@72B80"
- "@88@0:8@16@24@32@40@48@56q64@72@80"
- "@92@0:8i16@20@28@36i44q48@56@64@72B80@84"
- "Attempting to update System info due to cellular parameter change"
- "B16@?0@\"BMStoreEvent\"8"
- "B16@?0@\"NSDictionary\"8"
- "B24@0:8^B16"
- "B28@0:8@16C24"
- "B32@0:8^@16@?<v@?@\"TRIClientBackgroundMLTask\"@\"TRIFactorsState\"^B>24"
- "B32@0:8^@16@?<v@?@\"TRIMLRuntimeEvaluation\"@\"TRIFactorsState\"^B>24"
- "BMLTs:"
- "BackgroundMLTaskCatalog"
- "BackgroundMLTaskNotification"
- "BuildVersion"
- "CTBundle"
- "Class getCTBundleClass(void)_block_invoke"
- "Class getCoreTelephonyClientClass(void)_block_invoke"
- "Class getTIInputModeControllerClass(void)_block_invoke"
- "CoreTelephonyClient"
- "CoreTelephonyClientCarrierBundleDelegate"
- "CoreTelephonyClientDataDelegate"
- "CoreTelephonyClientSubscriberDelegate"
- "Current population is %@"
- "DSLPublisher"
- "DeviceClass"
- "Error creating persistent identifier folder: %@"
- "Error deleting persistent identifier file: %@"
- "Error reading Siri.AnalyticsIdentifiers.UserAggregationId data stream %{public}@"
- "Error writing persistent identifier: %@"
- "Error: Failed to create the plist path for the app group identifier: %@"
- "Error: Failed to read the plist dictionary from %@"
- "Error: Failed to retrieve the container URL for the app group identifier: %@"
- "Error: SegmentStore.plist does not exist at the expected location."
- "Error: The activitySegment in the plist is not a string."
- "Error: systemInfo is null."
- "FED_STATS_BIOME"
- "Failed to enumerate namespace descriptor filenames: %@"
- "Failed to evaluate targeting expression. Please verify parameters are valid for expression %@ with parameters %@"
- "Failed to load namespace descriptor from parent dir: %@"
- "Failed to parse ClientTreatment from in-memory representation: %@"
- "Failed to resolve targeted experiment factor pack set for deployment: %@. This is expected for old experiments downloaded before FPE was enabled."
- "Failed to resolve targeted experiment factor pack set for factor state: %@. This is expected if this is for investigations and not counterfactuals."
- "Failed to resolve targeted namespace descriptor for deployment: %@"
- "Fetched Carrier bundle identifier from CoreTelephony: %{public}@"
- "Fetched Carrier country code from CoreTelephony: %{public}@"
- "GENERAL_PUBLIC"
- "If the `type` is TRIEvaluationStatusTypeActivated, the `evalState` must be non-nil."
- "Ignoring FPS-based experiment deployment info in plplist as the feature is not yet enabled: %@"
- "Invalid event body for Siri.AnalyticsIdentifiers.UserAggregationId data stream"
- "Invalid type for Siri.AnalyticsIdentifiers.UserAggregationId event %@"
- "LIMITED_CARRY"
- "Logging log event: %@"
- "Missing serialized value for TRIBMLTDeployment.deploymentId"
- "Missing serialized value for TRIBackgroundMLTaskHistoryRecord.deploymentId"
- "Missing serialized value for TRIBackgroundMLTaskHistoryRecord.eventType"
- "Missing serialized value for TRIPartialBMLTRecord.status"
- "Missing serialized value for TRIPartialExperimentRecord.isShadow"
- "Missing serialized value for TRIPartialRolloutRecord.isShadow"
- "No cached external parameters."
- "ORGANIZATION"
- "Opening treatment via id-based namespace descriptor path: %@"
- "POPULATION_UNKNOWN"
- "Persistent identifier file read error: %@"
- "ProductType"
- "RC_SEED_BUILD is false. Not considering device as enrolled in beta program"
- "RC_SEED_BUILD is true. Considering device as enrolled in beta program"
- "Reading currentPopulation from NSUserDefaults"
- "Reading params from cache: %@"
- "Received delegate callback: carrierBundleChange"
- "Received delegate callback: preferredDataSimChanged"
- "Received delegate callback: subscriberCountryCodeDidChange"
- "Retrieved nil serialized value for nonnull TRIBMLTActiveEvaluationTuple.bmlt"
- "Retrieved nil serialized value for nonnull TRIBMLTActiveEvaluationTuple.factorsState"
- "Retrieved nil serialized value for nonnull TRIBMLTDeployment.backgroundMLTaskId"
- "Retrieved nil serialized value for nonnull TRIBackgroundMLTaskHistoryRecord.backgroundMLTaskId"
- "Retrieved nil serialized value for nonnull TRIBackgroundMLTaskHistoryRecord.eventDate"
- "Retrieved nil serialized value for nonnull TRIMLRuntimeActiveEvaluationTuple.eval"
- "Retrieved nil serialized value for nonnull TRIMLRuntimeActiveEvaluationTuple.factorsState"
- "Retrieved nil serialized value for nonnull TRIMLRuntimeEvaluationHistoryRecord.evaluation"
- "Retrieved nil serialized value for nonnull TRIMLRuntimeEvaluationHistoryRecord.status"
- "Retrieved nil serialized value for nonnull TRIPartialBMLTRecord.bmltDeployment"
- "Retrieved nil serialized value for nonnull TRIPartialBMLTRecord.pluginId"
- "Segment/SegmentStore.plist"
- "Set up TRICellularParameterManager"
- "Siri.AnalyticsIdentifiers.UserAggregationId"
- "SiriDeviceAggregationIdRotationDate"
- "SiriUserActivitySegment"
- "Subscribed sink already exists. Replacing: %@"
- "Subscribing to events from Biome stream: %@"
- "SysConfig is stale, leaving population unset"
- "System info update successful"
- "T@\"NSArray\",&,N,V_enabledInputModeIdentifiers"
- "T@\"NSArray\",R,N,V_logHandlers"
- "T@\"NSDate\",&,N,V_siriDeviceAggregationIdRotationDate"
- "T@\"NSString\",&,N,V_aneVersion"
- "T@\"NSString\",&,N,V_carrierBundleIdentifier"
- "T@\"NSString\",&,N,V_carrierCountryIsoCode"
- "T@\"NSString\",&,N,V_iCloudIdentifier"
- "T@\"NSString\",&,N,V_siriUserActivitySegment"
- "T@\"NSString\",R,N,V_backgroundMLTaskId"
- "T@\"NSString\",R,N,V_bmltId"
- "T@\"NSString\",R,N,V_bmltTaskId"
- "T@\"NSString\",R,N,V_evaluationId"
- "T@\"NSString\",R,N,V_namespace"
- "T@\"NSString\",R,N,V_pluginId"
- "T@\"TRIBMLTDeployment\",R,N,V_bmltDeployment"
- "T@\"TRIBMLTDeployment\",R,N,V_bmltDeploymentForFactorsState"
- "T@\"TRIBMLTDeployment\",R,N,V_deployment"
- "T@\"TRIClientBackgroundMLTask\",R,N,V_bmlt"
- "T@\"TRIEvaluationStatus\",R,N,V_status"
- "T@\"TRIExperimentDeployment\",R,N,V_experimentDeploymentForFactorsState"
- "T@\"TRIExperimentFactorsState\",R,N,V_experimentFactorsStateForCounterfactuals"
- "T@\"TRIFactorsState\",R,N,V_evalState"
- "T@\"TRIFactorsState\",R,N,V_factorsState"
- "T@\"TRIFactorsStateBMLTIdentifiers\",R,N"
- "T@\"TRIFactorsStateRolloutIdentifiers\",R,N"
- "T@\"TRILogger\",R,N,V_logger"
- "T@\"TRIMLRuntimeEvaluation\",R,N,V_eval"
- "T@\"TRIMLRuntimeEvaluation\",R,N,V_evaluation"
- "T@\"TRIPersistedBMLTFactorsState\",&,D,N"
- "T@\"TRIPersistedFactorsState\",&,D,N"
- "T@\"TRIPersistedRolloutFactorsState\",&,D,N"
- "T@\"TRIRolloutDeployment\",R,N,V_rolloutDeploymentForFactorsState"
- "TB,N,V_hasAne"
- "TB,N,V_isAutomatedTestDevice"
- "TB,N,V_isDiagnosticsAndUsageEnabled"
- "TB,N,V_isEnrolledInBetaProgram"
- "TB,N,V_logUserKeyboardEnabledInputMode"
- "TB,N,V_logUserSettingsLanguageCode"
- "TB,N,V_logUserSettingsRegionCode"
- "TB,R,N,V_isShadow"
- "TIInputModeController"
- "TRIBMLTActiveEvaluationTuple"
- "TRIBMLTActiveEvaluationTupleOCNTErrorDomain"
- "TRIBMLTDeployment"
- "TRIBMLTDeploymentOCNTErrorDomain"
- "TRIBMLTFactorsState"
- "TRIBackgroundMLTaskHistoryRecord"
- "TRIBackgroundMLTaskHistoryRecordOCNTErrorDomain"
- "TRIBackgroundMLTaskIdentifiers"
- "TRIBiomeDataStreamProvider"
- "TRICKServerEnvironmentReader"
- "TRICellularParameterGuardedData"
- "TRICellularParameterManager"
- "TRICellularParameterManager failed to update system info"
- "TRICellularParameterManager.m"
- "TRIEvaluationStatus"
- "TRIEvaluationStatusCursor"
- "TRIEvaluationStatusDefaultProvider"
- "TRIEvaluationStatusProvider"
- "TRIEvaluationStatusProvider.m"
- "TRIExternalParameterGuardedData"
- "TRIExternalParameterManager"
- "TRIExternalParameterProviding"
- "TRIFactorsStateBMLTIdentifiers"
- "TRIFactorsStateRolloutIdentifiers"
- "TRILogHandling"
- "TRILogger"
- "TRIMLRuntimeActiveEvaluationTuple"
- "TRIMLRuntimeActiveEvaluationTupleOCNTErrorDomain"
- "TRIMLRuntimeEvaluationHistoryRecord"
- "TRIMLRuntimeEvaluationHistoryRecordOCNTErrorDomain"
- "TRINamespaceLogPolicy"
- "TRINamespaceResolverGuardedData"
- "TRIPETLogHandler"
- "TRIPartialBMLTRecord"
- "TRIPartialBMLTRecordOCNTErrorDomain"
- "TRIPersistedBMLTFactorsState"
- "TRIPersistedEvaluationStatus"
- "TRIPersistedRolloutFactorsState"
- "TRIRolloutFactorsState"
- "TRISystemConfiguration"
- "TRISystemInfo"
- "TRISystemInfo.m"
- "TRISystemInfoGuardedData"
- "TRIXPCInternalSystemServiceProtocol"
- "Targeting expression is not formatted correctly. Could not parse BMLT assignment string %@"
- "Tq,N,V_appleIntelligenceState"
- "TrialXP-"
- "TrialXP-429.20.2"
- "Unable to acquire shared lock on managed-directory \"%@\": %s (%d)"
- "Unable to find class %s"
- "Unable to get carrier bundle identifier: %{public}@"
- "Unable to get carrier country code: %{public}@"
- "Unable to get last known mobile subscriber country code: %{public}@"
- "Unable to get preferred data subscription context"
- "Unable to get preferred data subscription context: %{public}@"
- "Unable to load soft-linked CTBundle class"
- "Unable to load soft-linked CoreTelephonyClient class"
- "Unable to load soft-linked TIInputModeController class"
- "Unable to load soft-linked _ANEDeviceInfo class"
- "Unable to read 'kern.hv_vmm_present' code: %d"
- "Unable to resolve BMLT deployment %@: %s (%d)"
- "Unarchived unexpected class for TRIBackgroundMLTaskHistoryRecord key \"eventDate\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIBackgroundMLTaskHistoryRecord key \"factorPackSetId\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIPartialBMLTRecord key \"activeFactorPackSetId\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIPartialBMLTRecord key \"activeTargetingRuleIndex\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIPartialBMLTRecord key \"endDate\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIPartialBMLTRecord key \"targetedFactorPackSetId\" (expected %@, decoded %@)"
- "Unarchived unexpected class for TRIPartialBMLTRecord key \"targetedTargetingRuleIndex\" (expected %@, decoded %@)"
- "Unexpected namespace descriptor filename: %@"
- "Updating iCloudID using Alt. DSID of account: %@"
- "UserAggregationId rotation date is null, eventBody: %@"
- "Using population override: %d"
- "[[NSString alloc] initWithUTF8String:rp]"
- "[_paths pathsForContainer:container asClientProcess:YES]"
- "[self initWithClientIdentifier:projectId paths:paths unit:unit factorsState:nil staleFactorsUsageGracePeriod:staleFactorsUsageGracePeriod logger:logger]"
- "_ANEDeviceInfo"
- "_aneVersion"
- "_appleIntelligenceState"
- "_backgroundMLTaskId"
- "_bmlt"
- "_bmltDeployment"
- "_bmltDeploymentForFactorsState"
- "_bmltId"
- "_bmltIdentifiersWithNamespaceName:"
- "_bmltProvider"
- "_bmltTaskId"
- "_cachedDeviceIdentifier"
- "_carrierBundleIdentifier"
- "_carrierCountryIsoCode"
- "_client"
- "_defaultProvider"
- "_dispatchLogEvent:"
- "_dispatchQueueForCarrierInfoGathering"
- "_enabledInputModeIdentifiers"
- "_eval"
- "_evalState"
- "_evaluation"
- "_evaluationId"
- "_experimentDeploymentForFactorsState"
- "_experimentFactorsStateForCounterfactuals"
- "_factorProviderForNamespaceName:fromNamespaceDescriptorSetWithDir:resolvedPath:"
- "_fetchCarrierBundleIdentifier:"
- "_fetchCarrierCountryIsoCode:"
- "_fetchSiriDeviceAggregationIdRotationDate"
- "_getSiriDeviceAggregationIdRotationDate"
- "_hasAne"
- "_hasBMLTFactorsState"
- "_hasCounterfactualFactorsState"
- "_hasExperimentFactorsState"
- "_hasRolloutFactorsState"
- "_iCloudIdentifier"
- "_incrementedLogEventCount"
- "_internalSystemHelper"
- "_isAutomatedTestDevice"
- "_isClient"
- "_isDiagnosticsAndUsageEnabled"
- "_isEnrolledInBetaProgram"
- "_isFBReadEnabled"
- "_isFBWriteEnabled"
- "_isSeedBuild"
- "_isShadow"
- "_isVirtualMachine"
- "_logBMLTCustomTargetingWithResult:"
- "_logHandlers"
- "_logUserKeyboardEnabledInputMode"
- "_logUserSettingsLanguageCode"
- "_logUserSettingsRegionCode"
- "_loggingQueue"
- "_namespace"
- "_paramProvider"
- "_persistentDeviceIdentifierPath"
- "_persistentSystemInfoPath"
- "_plistPath"
- "_pluginId"
- "_prepareFactorsStateForCounterfactualsForFactorsState:"
- "_prepareFactorsStateForExperimentsOnFactorPackSetPathForDeployment:"
- "_prepareFactorsStateForExperimentsOnTreatmentPathForDeployment:"
- "_providerQueue"
- "_readParametersFromFile"
- "_readSiriDeviceAggregationIdRotationDateFromEvent:"
- "_resolveTargetedFactorPackSetForBMLTDeployment:"
- "_resolveTargetedNamespaceDescriptorSetForExperimentDeployment:"
- "_rolloutDeploymentForFactorsState"
- "_sharedSystemInfo"
- "_shouldSubscribeWithWaking"
- "_siriDeviceAggregationIdRotationDate"
- "_siriUserActivitySegment"
- "_streamIdentifierstoSubscribedSinks"
- "_subscribeForStreamIdentifier:eventHandler:"
- "_subscriptionContext"
- "_sysEnabledInputModeIdentifiers"
- "_sysIsEnrolledInBetaProgram"
- "_systemInfoWithIsStale:"
- "_telephonyClient"
- "_trialVersion"
- "_unsubscribeAllDataStreams"
- "_updateSystemInfo"
- "_updateSystemInfo:"
- "_writeParametersToFile"
- "aa_altDSID"
- "aa_primaryAppleAccount"
- "activeBMLTInformation:"
- "activeBMLTInformationWithError:"
- "activeBMLTInformationWithPrivacyFilterPolicy:completion:"
- "activeEvaluationsForBMLTWithCompletion:"
- "activeEvaluationsForMLRuntimeWithCompletion:"
- "activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:"
- "activeRolloutInformationWithPrivacyFilterPolicy:completion:"
- "activitySegment"
- "addNamespaceName:"
- "added update handler %lu for namespace %@ -- now %lu handlers for this namespace"
- "allowedLowLevelDefaultLevelsDir"
- "anbrActivationState:enabled:"
- "anbrBitrateRecommendation:bitrate:direction:"
- "aneSubType"
- "aneVersion"
- "appleIntelligenceState"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithCapacity:"
- "assignment string is missing or empty"
- "assignmentExpression"
- "authTokenChanged:"
- "automatedDeviceGroup"
- "backgroundMLTaskId"
- "backgroundMLTaskId != nil"
- "backgroundMLTaskIdentifiersWithNamespaceName:"
- "bmlt"
- "bmlt != nil"
- "bmltDeployment"
- "bmltDeployment != nil"
- "bmltDeploymentForFactorsState"
- "bmltDeploymentWithNamespaceName:"
- "bmltId"
- "bmltId != nil"
- "bmltIdentifiers"
- "bmltRecordsWithCompletion:"
- "bmltTaskId"
- "bmlt_custom_targeting"
- "bmlts:"
- "called deprecated method %s"
- "cancel"
- "cannot enumerate evaluations before class C locked"
- "cannot set factor levels for namespace %@, provider is for different namespace %@"
- "carrierBundleChange:"
- "carrierBundleIdentifier"
- "carrierCountryIsoCode"
- "catalogDefinition"
- "catalogDefinitionSignature"
- "clientWithIdentifier:unit:"
- "cloudIdentifier"
- "com.apple.trial.%@"
- "com.apple.trial.biome-provider"
- "com.apple.trial.external-parameter-change"
- "com.apple.trial.status.evaluation.mlruntime.allow"
- "com.apple.trial.system-config.carrier"
- "com.apple.triald.ExternalParameterChangeQueue"
- "connectionActivationError:connection:error:"
- "connectionAvailability:availableConnections:"
- "connectionStateChanged:connection:dataConnectionStatusInfo:"
- "context"
- "copyBundleIdentifier:bundleType:error:"
- "copyLastKnownMobileSubscriberCountryCode:error:"
- "copyMobileSubscriberIsoCountryCode:error:"
- "copyWithReplacementBackgroundMLTaskId:"
- "copyWithReplacementBmlt:"
- "copyWithReplacementBmltDeployment:"
- "copyWithReplacementEval:"
- "copyWithReplacementEvaluation:"
- "copyWithReplacementFactorsState:"
- "copyWithReplacementIsShadow:"
- "copyWithReplacementNamespace:"
- "copyWithReplacementPluginId:"
- "could not evaluate BMLT assignment expression \"%@\" -- %@"
- "could not parse BMLT assignment string \"%@\" -- %@"
- "counterfactualFactorPackDeploymentMap"
- "countryCode"
- "createDeviceIdentifierWithPath:"
- "createPersistentDeviceIdentifier"
- "createSystemInfoWithFactorProvider:"
- "currentCalendar"
- "currentDataServiceDescriptorChanged:"
- "currentDataSimChanged:"
- "currentEnvironment"
- "currentLocale"
- "currentPopulation"
- "currentWithUseCaseIdentifiers:"
- "dataRoamingSettingsChanged:status:"
- "dataSettingsChanged:"
- "dataStatus:dataStatusInfo:"
- "dateWithTimeIntervalSince1970:"
- "defaultBundleChange"
- "defaultStore"
- "deleteDeviceIdentifier"
- "deleteDeviceIdentifierWithPath:"
- "deploymentWithBackgroundMLTaskId:deploymentId:"
- "deviceClass"
- "deviceInfoForQuestion:"
- "deviceModelCode"
- "dictionaryWithContentsOfURL:"
- "didDetectSimDeactivation:info:"
- "dispatching updates to %tu callbacks"
- "effectiveFrom"
- "enabledInputModeIdentifiers"
- "encodeWithCoder: enabledInputModeIdentifiers is nil"
- "enroll"
- "ensureBMLTFields"
- "ensureExperimentFields"
- "ensureRolloutFields"
- "enumerateActiveBMLTWithError:block:"
- "enumerateActiveEvaluationsForMLRuntimeWithError:block:"
- "enumerateExperimentStatusesForEnvironment:privacyFilterPolicy:startingFromCursor:error:block:"
- "enumerateExperimentStatusesForTestingPrivacyFilterPolicyWithEnvironment:startingFromCursor:error:block:"
- "enumerateStatusOfEvaluationsForMLRuntimeWithCursor:error:block:"
- "eval"
- "eval != nil"
- "evalState"
- "evaluateBMLTTargetingExpression:withParameters:error:"
- "evaluation"
- "evaluation != nil"
- "evaluationHistoryRecordsForMLRuntimeWithLimit:newerThanDate:completion:"
- "evaluationId"
- "eventBody"
- "experimentDeploymentForFactorsState"
- "experimentFactorsStateForCounterfactuals"
- "experimentHistoryRecordsWithLimit:newerThanDate:privacyFilterPolicy:deploymentEnvironment:completion:"
- "experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:completion:"
- "expressionValueWithObject:context:"
- "expressionWithFormat:"
- "externalParamManager"
- "factor level from flatbuffer storage:%@ does not match factor level from pb: %@"
- "factorPackIdForBmltWithNamespaceName:"
- "factorPacksExperimentsRead"
- "factorProviderWithPaths:namespaceName:resolver:"
- "factorsState"
- "factorsState != nil"
- "failed to create directory for path %@ -- %@"
- "failed to encode system info -- %@"
- "failed to parse external parameter dictionary from file: %@ (%@)"
- "failed to read system info from file %@: %@"
- "failed to to read Biome stream: %@"
- "failed to write system info to path %@ -- %@"
- "filterWithIsIncluded:"
- "flatbufferTreatmentStorageRead"
- "flatbufferTreatmentStorageWrite"
- "freshProvider"
- "getPreferredDataSubscriptionContextSync:"
- "group.com.apple.siri.userfeedbacklearning"
- "guardedCarrierBundleIdentifier"
- "guardedCarrierCountryIsoCode"
- "guardedSiriDeviceAggregationIdRotationDate"
- "hasANE"
- "hasAne"
- "hasAssignmentExpression"
- "hasBmltId"
- "hasEvalState"
- "hasEvaluationId"
- "hasTrialSystemTelemetry"
- "i24@0:8q16"
- "iCloudId"
- "iCloudIdentifier"
- "ignore"
- "info"
- "initFromSystemWithFactorProvider:"
- "initWithBMLTId:deploymentId:"
- "initWithBMLTTaskId:deploymentId:treatmentId:"
- "initWithBMLTaskId:deploymentId:factorPackId:"
- "initWithBackgroundMLTaskId:deploymentId:"
- "initWithBmlt:factorsState:"
- "initWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:"
- "initWithBundleType:"
- "initWithClient:projectId:logHandlers:"
- "initWithClientIdentifier:paths:unit:factorsState:staleFactorsUsageGracePeriod:logger:"
- "initWithClientIdentifier:paths:unit:staleFactorsUsageGracePeriod:logger:"
- "initWithCoder: enabledInputModeIdentifiers is nil"
- "initWithCurrentSchemaVersion"
- "initWithDeployment:"
- "initWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:"
- "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:"
- "initWithEval:factorsState:"
- "initWithEvaluation:status:"
- "initWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:"
- "initWithIdentifier:targetQueue:waking:"
- "initWithProjectId:"
- "initWithProjectId:logHandlers:"
- "initWithProvider:paths:"
- "initWithQueue:"
- "initWithSchemaVersion is expected to initialize to non-nil"
- "initWithSchemaVersion:"
- "initWithSchemaVersion:container:asClientProcess:"
- "initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:allowSystemToUserConnection:interruptionHandler:invalidationHandler:logHandle:"
- "initWithServiceName:allowlistedServerInterface:allowlistedClientInterface:serverInitiatedRequestHandler:interruptionHandler:invalidationHandler:logHandle:"
- "initWithString:"
- "initWithType:evaluationId:date:evalState:"
- "internetConnectionActivationError:"
- "internetConnectionAvailability:"
- "internetConnectionStateChanged:"
- "internetDataStatus:"
- "internetDataStatusBasic:"
- "isAutomatedTestDevice"
- "isBetaBuild"
- "isBetaUser"
- "isBetaUserWithIsStale:"
- "isDiagnosticsAndUsageEnabled"
- "isEnrolledInBetaProgram"
- "isEqualToBMLTTaskIdentifiers:"
- "isEqualToTuple:"
- "isShadow"
- "isStale"
- "json"
- "kern.hv_vmm_present"
- "languageCode"
- "last"
- "legacyNamespaceDescriptors"
- "loadSystemInfo"
- "lockedSet for counterfactuals unexpectedly not present"
- "lockedSet for factors state unexpectedly not present"
- "lockedSet for namespace descriptor set unexpectedly not present"
- "logEvent:"
- "logEvent:subgroupName:queue:"
- "logHandlers"
- "logMessage:"
- "logMessage:subGroup:"
- "logUserKeyboardEnabledInputMode"
- "logUserSettingsLanguageCode"
- "logUserSettingsRegionCode"
- "logWithMLRuntimeDimensions:metrics:factorState:"
- "logWithNamespaceName:metrics:dimensions:"
- "logWithProjectNameAndTrackingId:metrics:dimensions:trialSystemTelemetry:"
- "logWithTrackingId:logLevel:message:"
- "logWithTrackingId:logLevel:message:args:"
- "logWithTrackingId:message:"
- "logWithTrackingId:metric:"
- "logWithTrackingId:metric:dimensions:"
- "logWithTrackingId:metrics:dimensions:"
- "logWithTrackingId:metrics:dimensions:systemDimensions:trialSystemTelemetry:"
- "logWithTrackingId:metrics:dimensions:trialSystemTelemetry:"
- "marketingOSVersion"
- "messageWithOneofField:withName:"
- "metricWithName:"
- "metricWithName:integerValue:"
- "namespace"
- "namespace mismatch (exp %@, act %@)"
- "namespaceDescriptorsBMLTDir"
- "namespaceDescriptorsRolloutDir"
- "namespaceString"
- "no BMLTs"
- "none"
- "now"
- "nrSliceAppStateChanged:status:trafficDescriptors:"
- "nrSlicedRunningAppStateChanged:"
- "nsexpressionLanguage"
- "operatingSystemVersion"
- "operatorBundleChange:"
- "optInApple"
- "osBuild"
- "osType"
- "overlayLevelsFromFactorProvider:"
- "pathsForContainer:asClientProcess:"
- "plplist contains bad experiment deployment: %@"
- "pluginId"
- "pluginId != nil"
- "populationType"
- "preferredDataServiceDescriptorChanged:"
- "preferredDataSimChanged:"
- "printedBMLTInformation:"
- "printedExperimentInformationWithEnvironments:error:"
- "printedRolloutInformation:"
- "prlVersionDidChange:version:"
- "projectNameFromId:"
- "publisher"
- "readDeviceIdentifierWithPath:"
- "readLastDataStreamEventForIdentifier:eventHandler:"
- "readLastDataStreamEventForIdentifier:withFilter:eventHandler:"
- "recordWithBmltDeployment:pluginId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:endDate:namespace:"
- "recordWithDeployment:rampId:activeFactorPackSetId:activeTargetingRuleIndex:targetedFactorPackSetId:targetedTargetingRuleIndex:status:namespaces:isShadow:"
- "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:counterfactualTreatmentIds:"
- "recordWithEvaluation:status:"
- "recordWithEventDate:eventType:backgroundMLTaskId:deploymentId:factorPackSetId:"
- "regDataModeChanged:dataMode:"
- "reloadDeviceId"
- "reloadSystemInfo"
- "resetDeviceIdentifier"
- "rollout"
- "rolloutAllocationStatusWithPrivacyFilterPolicy:completion:"
- "rolloutDeploymentForFactorsState"
- "rolloutIdentifiers"
- "saveToFile:"
- "scanUpToString:intoString:"
- "self.bmltDeploymentForFactorsState"
- "self.experimentDeploymentForFactorsState"
- "self.experimentFactorsStateForCounterfactuals"
- "self.rolloutDeploymentForFactorsState"
- "server-side experiments:"
- "serviceDisconnection:status:"
- "servingNetworkChanged:"
- "setAneVersion:"
- "setAppleIntelligenceState:"
- "setBmltId:"
- "setCarrierBundleIdentifier:"
- "setCarrierCountryIsoCode:"
- "setClientBmltId:"
- "setClientDeploymentId:"
- "setClientExperimentId:"
- "setClientProjectId:"
- "setClientRolloutId:"
- "setClientTreatmentId:"
- "setDelegate:"
- "setDeviceClass:"
- "setDeviceIdentifier:"
- "setDeviceIdentifier:path:"
- "setEnabledInputModeIdentifiers:"
- "setEvalState:"
- "setEvaluationId:"
- "setHasAne:"
- "setICloudIdentifier:"
- "setIsAutomatedTestDevice:"
- "setIsDiagnosticsAndUsageEnabled:"
- "setIsEnrolledInBetaProgram:"
- "setLogUserKeyboardEnabledInputMode:"
- "setLogUserSettingsLanguageCode:"
- "setLogUserSettingsRegionCode:"
- "setMetrics:"
- "setMlruntimeDimensions:"
- "setOsBuild:"
- "setProcessEventIndex:"
- "setShouldSubscribeWithWaking:"
- "setSiriDeviceAggregationIdRotationDate:"
- "setSiriUserActivitySegment:"
- "setSystemDimensions:"
- "setTargetedPopulation:"
- "setTrialSystemTelemetry:"
- "setUserDimensions:"
- "setUserKeyboardEnabledInputModeIdentifiers:"
- "setUserSettingsBcp47DeviceLocale:"
- "setValue:"
- "setVersionTag:"
- "sharedInstance"
- "sharedSystemPaths"
- "shortLabelsDidChange"
- "shouldPrivacyFilterNamespace:policy:"
- "simLockSaveRequestDidComplete:success:"
- "simPinChangeRequestDidComplete:success:"
- "simPinEntryErrorDidOccur:status:"
- "simPukEntryErrorDidOccur:status:"
- "simStatusDidChange:status:"
- "sinkWithCompletion:receiveInput:"
- "siriDeviceAggregationIdRotationDate"
- "siriUserActivitySegment"
- "softlink:o:path:/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony"
- "softlink:o:path:/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine"
- "softlink:r:path:/System/Library/PrivateFrameworks/TextInput.framework/TextInput"
- "status != nil"
- "storedDeviceIdentifier"
- "streamWithIdentifier:error:"
- "subscribeDataStreamForIdentifier:eventHandler:"
- "subscribeOn:"
- "subscriberCountryCodeDidChange:"
- "successfully parsed BMLT assignment string %@ to ENROLL"
- "successfully parsed BMLT assignment string %@ to IGNORE"
- "sysdiagnoseInfoWithError:"
- "systemDimensions"
- "systemInfo"
- "systemInfoFromFile:"
- "targetedBMLTDeploymentMap"
- "targetedExperimentNamespaceDescriptorDeploymentMap"
- "targetedNamespaceDescriptorSet"
- "taskDefinition"
- "taskDefinitionSignature"
- "taskId"
- "tetheringStatus:"
- "tetheringStatus:connectionType:"
- "trialSystemTelemetry"
- "trialVersionMajor"
- "trialVersionMinor"
- "trialVersionTag"
- "triclient_missing_datavault"
- "tupleWithBmlt:factorsState:"
- "tupleWithEval:factorsState:"
- "unable to fetch active BMLTs while device is class C locked qos:%{public}u"
- "unable to get BMLT info"
- "unable to write external parameters to file %@ -- %@"
- "unarchivedObjectOfClass:fromData:error:"
- "unsubscribeAllDataStreams"
- "userDefaultVoiceSlotDidChange:"
- "userSettingsBCP47DeviceLocale"
- "userSettingsLanguageCode"
- "userSettingsRegionCode"
- "v16@?0@\"BMStoreEvent\"8"
- "v16@?0@\"BPSCompletion\"8"
- "v16@?0@\"TRICellularParameterGuardedData\"8"
- "v16@?0@\"TRIExternalParameterGuardedData\"8"
- "v16@?0@\"TRINamespaceResolverGuardedData\"8"
- "v16@?0@\"TRISystemInfoGuardedData\"8"
- "v2/bmlt/%@/%d/%@"
- "v24@0:8@\"CTDataConnectionStatus\"16"
- "v24@0:8@\"CTDataSettings\"16"
- "v24@0:8@\"CTDataStatus\"16"
- "v24@0:8@\"CTDataStatusBasic\"16"
- "v24@0:8@\"CTServiceDescriptor\"16"
- "v24@0:8@\"CTSlicedRunningAppInfoContainer\"16"
- "v24@0:8@\"CTTetheringStatus\"16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v28@0:8@\"CTServiceDescriptor\"16B24"
- "v28@0:8@\"CTTetheringStatus\"16i24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
- "v28@0:8@16i24"
- "v28@0:8C16@?20"
- "v28@0:8C16@?<v@?@\"NSArray\"@\"NSError\">20"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTDataStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTServiceDisconnectionStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSimDeactivationInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSString\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28"
- "v32@0:8@16i24i28"
- "v32@?0@\"TRIBMLTDeployment\"8@\"TRILockedFactorPackSet\"16^B24"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24i32"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16i24@\"CTDataConnectionStatus\"28"
- "v36@0:8@\"NSSet\"16C24@?<v@?@\"NSArray\">28"
- "v36@0:8@\"NSSet\"16C24@?<v@?@\"NSArray\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@\"CTTrafficDescriptorsContainer\"28"
- "v36@0:8@16@24i32"
- "v36@0:8@16B24@28"
- "v36@0:8@16C24@?28"
- "v36@0:8@16i24@28"
- "v40@0:8@\"NSString\"16@?<B@?@\"NSDictionary\">24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"TRILogEvent\"16@\"NSString\"24@\"NSObject<OS_dispatch_queue>\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8Q16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16q24@32*40"
- "v48@0:8Q16@\"NSDate\"24C32i36@?<v@?@\"NSNumber\"@\"NSArray\"@\"NSDate\"@\"NSError\">40"
- "v48@0:8Q16@24C32i36@?40"
- "v56@0:8@16@24@32@40@48"
- "validatedEnvironmentFromNumber:"
- "validatedPopulationFromNumber:"
- "validityDays"
- "void *CoreTelephonyLibrary(void)"
- "void *TextInputLibrary(void)"
- "writeData:"
- "writeToFile:atomically:encoding:error:"
- "{?=qqq}16@0:8"

```
