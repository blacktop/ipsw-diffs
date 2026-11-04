## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-511.1.2.0.0
-  __TEXT.__text: 0x14e3b4
+511.2.2.0.0
+  __TEXT.__text: 0x14ee08
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x794
   __TEXT.__lazy_helpers: 0xe8
-  __TEXT.__objc_methlist: 0xc86c
+  __TEXT.__objc_methlist: 0xc8bc
   __TEXT.__const: 0xef4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__cstring: 0x16ae5
+  __TEXT.__cstring: 0x16be0
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x1e09f
+  __TEXT.__oslogstring: 0x1e287
   __TEXT.__gcc_except_tab: 0x7f74
-  __TEXT.__unwind_info: 0x50c8
+  __TEXT.__unwind_info: 0x50d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x69e8
+  __DATA_CONST.__const: 0x6a30
   __DATA_CONST.__objc_classlist: 0x9c0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x65d8
+  __DATA_CONST.__objc_selrefs: 0x6608
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x630
   __DATA_CONST.__objc_arraydata: 0x398
   __DATA_CONST.__got: 0x1430
   __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0xf020
-  __AUTH_CONST.__objc_const: 0x18348
+  __AUTH_CONST.__cfstring: 0xf0e0
+  __AUTH_CONST.__objc_const: 0x18368
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x378

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1258
   __AUTH.__data: 0x6e0
-  __DATA.__objc_ivar: 0x970
+  __DATA.__objc_ivar: 0x974
   __DATA.__data: 0x2b40
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x28

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 4999
-  Symbols:   9422
-  CStrings:  4253
+  Functions: 5007
+  Symbols:   9436
+  CStrings:  4268
 
Symbols:
+ +[TRIExternalConfigurationChangeProcessor processAdsMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]
+ +[TRISystemInfo _adsMapsBucketId:]
+ -[TRIExperimentUpdateProcessor _rewriteActiveFactorProviders]
+ -[TRIExperimentUpdateProcessor initWithServerContext:]
+ -[TRIExperimentUpdateScheduler initWithServerContext:taskQueue:]
+ -[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:experimentEndDatesMap:factorPackMap:]
+ -[TRINamespaceResolverStorage _processExperimentRecord:isStaging:namespaceMap:fpNamespaceMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:experimentEndDatesMap:setStorage:]
+ -[TRIPersistentUserSettings persistAdsMapsBucketId:]
+ -[TRIPersistentUserSettings persistedAdsMapsBucketId]
+ -[TRISystemConfiguration adsMapsBucketId]
+ -[TRISystemInfo adsMapsBucketId]
+ -[TRISystemInfo setAdsMapsBucketId:]
+ _OBJC_IVAR_$_TRIExperimentUpdateProcessor._serverContext
+ _OBJC_IVAR_$_TRISystemInfo._adsMapsBucketId
+ _TRIAdsNamespaceAppStore
+ _TRIAdsNamespaceMaps
+ _TRIPersistentAdsMapsBucket
+ _TRISystemCovariate_AdsMapsBucketId
+ ___261-[TRINamespaceResolverStorage _processExperimentRecord:isStaging:namespaceMap:fpNamespaceMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:experimentEndDatesMap:setStorage:]_block_invoke
+ ___286-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:experimentEndDatesMap:factorPackMap:]_block_invoke
+ ___286-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:experimentEndDatesMap:factorPackMap:]_block_invoke_2
+ ___61-[TRIExperimentUpdateProcessor _rewriteActiveFactorProviders]_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e33_v24?0"TRIExperimentRecord"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v24?0"TRIExperimentRecord"8^B16ls32l8s40l8s48l8
- -[TRIExperimentUpdateProcessor initWithExperimentDatabase:]
- -[TRIExperimentUpdateScheduler experimentDatabase]
- -[TRIExperimentUpdateScheduler initWithExperimentDatabase:taskQueue:]
- -[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:]
- -[TRINamespaceResolverStorage _processExperimentRecord:isStaging:namespaceMap:fpNamespaceMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:setStorage:]
- _OBJC_IVAR_$_TRIExperimentUpdateScheduler._experimentDatabase
- ___239-[TRINamespaceResolverStorage _processExperimentRecord:isStaging:namespaceMap:fpNamespaceMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:setStorage:]_block_invoke
- ___264-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:]_block_invoke
- ___264-[TRINamespaceResolverStorage _overwriteActiveFactorProvidersUsingGlobalPath:withNamespaceMap:rolloutDeploymentMap:experimentDeploymentMap:stagedExperimentDeploymentMap:experimentTreatmentMap:treatmentFactorPackSetIdsMap:counterfactualTreatmentsMap:factorPackMap:]_block_invoke_2
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e33_v24?0"TRIExperimentRecord"8^B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
CStrings:
+ "+[TRIExternalConfigurationChangeProcessor processAdsMapsBucketIdChangeIfNecessaryForBucketId:withServerContext:withTaskQueue:]"
+ "Ads: maps bucket id: %@"
+ "AdsMapsBucketId"
+ "Experiment %{public}@ has already expired (end date: %{public}@), rejecting end date extension"
+ "MAPS"
+ "Persisted Ads Maps Bucket Id: %@"
+ "Skipping expired experiment %@ from activeEnvVarNamespaces"
+ "Skipping expired experiment %@ from activeSysctlNamespaces"
+ "Skipping expired experiment from experimentIdsWithEnrollmentAndPostEnrollmentStateAndNamespaceName %{public}@"
+ "TrialXP-511.2.2"
+ "Unable to fetch Ads Maps Bucket Id."
+ "Unable to update the factor providers after experiment end date update."
+ "adsMapsBucketId"
+ "adsMapsBucketId != nil"
+ "com.apple.triald.persisted.Ads.Maps.BucketId"
+ "experimentEndDates"
- "TrialXP-511.1.2"
```
