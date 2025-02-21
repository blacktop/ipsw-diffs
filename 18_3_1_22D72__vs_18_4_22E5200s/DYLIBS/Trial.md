## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Trial`

```diff

-429.0.4.6.0
-  __TEXT.__text: 0x79cf8
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__delay_helper: 0x190
-  __TEXT.__objc_methlist: 0x6538
-  __TEXT.__const: 0xf22
-  __TEXT.__gcc_except_tab: 0x53b8
-  __TEXT.__cstring: 0x93d1
-  __TEXT.__oslogstring: 0x4766
+429.17.0.0.0
+  __TEXT.__text: 0x7b884
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__delay_helper: 0x258
+  __TEXT.__objc_methlist: 0x71e0
+  __TEXT.__const: 0xf02
   __TEXT.__dlopen_cstrs: 0x101
+  __TEXT.__gcc_except_tab: 0x5460
+  __TEXT.__cstring: 0x9953
+  __TEXT.__oslogstring: 0x4a3a
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x25f8
+  __TEXT.__unwind_info: 0x2630
   __TEXT.__objc_classname: 0x13e5
-  __TEXT.__objc_methname: 0xe578
-  __TEXT.__objc_methtype: 0x2df2
-  __TEXT.__objc_stubs: 0x9ce0
-  __DATA_CONST.__got: 0x848
-  __DATA_CONST.__const: 0x1b88
+  __TEXT.__objc_methname: 0xea7c
+  __TEXT.__objc_methtype: 0x2e12
+  __TEXT.__objc_stubs: 0x9fc0
+  __DATA_CONST.__got: 0x868
+  __DATA_CONST.__const: 0x1c48
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3340
+  __DATA_CONST.__objc_selrefs: 0x3698
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0xf78
-  __AUTH_CONST.__cfstring: 0x72e0
-  __AUTH_CONST.__objc_const: 0xde48
+  __AUTH_CONST.__cfstring: 0x7600
+  __AUTH_CONST.__objc_const: 0xc9d0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x550
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x69c
-  __DATA.__data: 0xe78
+  __DATA.__objc_ivar: 0x6b0
+  __DATA.__data: 0xe80
   __DATA.__bss: 0x88
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_ivar: 0x54

   - /System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2524
-  Symbols:   3301
-  CStrings:  4207
+  Functions: 2539
+  Symbols:   3340
+  CStrings:  4280
 
Symbols:
+ OBJC_IVAR_$_TRIActiveFactorProvidersParserGuardedData.counterfactualFactorPackDeploymentMap
+ _OBJC_CLASS_$_GMAvailabilityWrapper
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
CStrings:
+ "\b"
+ "       - %@"
+ "      counterfactualTreatments:"
+ "#\x14"
+ "/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels"
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
+ "TrialXP-429.17"
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
- "\a"
- "#\x13"
- "<TRIPartialExperimentRecord | deploymentEnvironment:%@ experimentDeployment:%@ treatmentId:%@ factorPackSetId:%@ type:%@ status:%@ startDate:%@ endDate:%@ namespaces:%@ isShadow:%@>"
- "@84@0:8i16@20@28@36i44q48@56@64@72B80"
- "TrialXP-429.0.4.6"
- "initWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:"
- "recordWithDeploymentEnvironment:experimentDeployment:treatmentId:factorPackSetId:type:status:startDate:endDate:namespaces:isShadow:"

```
