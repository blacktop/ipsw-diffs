## SiriInCall

> `/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall`

```diff

 3400.14.1.0.0
-  __TEXT.__text: 0x7cec
-  __TEXT.__auth_stubs: 0x950
+  __TEXT.__text: 0x7ac0
+  __TEXT.__auth_stubs: 0x930
   __TEXT.__const: 0x4f8
-  __TEXT.__swift5_typeref: 0x248
+  __TEXT.__swift5_typeref: 0x246
   __TEXT.__swift5_fieldmd: 0x16c
   __TEXT.__constg_swiftt: 0x4b0
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__cstring: 0x6d1
   __TEXT.__oslogstring: 0x455
   __TEXT.__swift5_capture: 0x64
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__eh_frame: 0x150
+  __TEXT.__unwind_info: 0x320
+  __TEXT.__eh_frame: 0x120
   __TEXT.__objc_classname: 0x24
   __TEXT.__objc_methname: 0x509
   __TEXT.__objc_methtype: 0x19e
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__auth_ptr: 0x1d0
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__auth_ptr: 0x1d8
   __AUTH_CONST.__const: 0x418
   __AUTH_CONST.__objc_const: 0x5a8
   __AUTH.__data: 0x30

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 253
-  Symbols:   143
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 254
+  Symbols:   149
+  CStrings:  101
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "ASS_$_TRIPersistedTaskCapabilityModifier"
+ "_OBJC_CLASS_$_TRIActivateTreatmentBaseTask"
+ "_OBJC_CLASS_$_TRIAssetStoreOperator"
+ "_OBJC_CLASS_$_TRICKAssetMetadata"
+ "_OBJC_CLASS_$_TRICacheDeleteUtils"
+ "_OBJC_CLASS_$_TRIDeferralNotifier"
+ "_OBJC_CLASS_$_TRIDownloadLatencyTaskResultTelemetryBuilder"
+ "_OBJC_CLASS_$_TRIExperimentBaseTaskGuardedData"
+ "_OBJC_CLASS_$_TRIExperimentHistoryDatabase"
+ "_OBJC_CLASS_$_TRIFetchOnDemandFactorsPersistedTask_TreatmentAssetIndexes"
+ "_OBJC_CLASS_$_TRIFetchOnDemandFactorsTaskGuardedData"
+ "_OBJC_CLASS_$_TRIFetchSingleRolloutNotificationPersistedTask"
+ "_OBJC_CLASS_$_TRIGenericRequiredAssets"
+ "_OBJC_CLASS_$_TRIGenericUniqueRequiredAssets"
+ "_OBJC_CLASS_$_TRIHotfixRolloutTargetingScheduler"
+ "_OBJC_CLASS_$_TRILatencyMetricTelemetryValidator"
+ "_OBJC_CLASS_$_TRILimitedCarryProfileManager"
+ "_OBJC_CLASS_$_TRIMemoryEfficientFileDigest"
+ "_OBJC_CLASS_$_TRINamespaceDescriptorSetExternalRefStore"
+ "_OBJC_CLASS_$_TRINamespaceDescriptorSetStorage"
+ "_OBJC_CLASS_$_TRINamespaceResolverStorage"
+ "_OBJC_CLASS_$_TRINotificationReactionChecker"
+ "_OBJC_CLASS_$_TRIPeekEnumerator"
+ "_OBJC_CLASS_$_TRIPersistedClientRolloutArtifact"
+ "_OBJC_CLASS_$_TRIPersistedTaskCapabilityModifier"
+ "_OBJC_CLASS_$_TRIPurgeableNamespacesProvider"
+ "_OBJC_CLASS_$_TRIPushChannelId"
+ "_OBJC_CLASS_$_TRIPushNotificationHandler"
+ "_OBJC_CLASS_$_TRIPushServiceConnectionCreator"
+ "_OBJC_CLASS_$_TRIPushServiceConnectionMultiplexer"
+ "_OBJC_CLASS_$_TRIReferenceManagedDir"
+ "_OBJC_CLASS_$_TRIRemoteAssetDecrypter"
+ "_OBJC_CLASS_$_TRIRemoteAssetPatcher"
+ "_OBJC_CLASS_$_TRIRequiredCloudKitAsset"
+ "_OBJC_CLASS_$_TRIRolloutDeploymentRefStore"
+ "_OBJC_CLASS_$_TRIRolloutTargeter"
+ "_OBJC_CLASS_$_TRIRolloutTargetingOperation"
+ "_OBJC_CLASS_$_TRIRolloutTargetingPersistedTask"
+ "_OBJC_CLASS_$_TRIRolloutTaskSupportGuardedData"
+ "_OBJC_CLASS_$_TRIRuleQualifiedFactorPackSetId"
+ "_OBJC_CLASS_$_TRISandboxExtensionFactory"
+ "_OBJC_CLASS_$_TRISelectRolloutNotificationListPersistedTask"
+ "_OBJC_CLASS_$_TRISelectRolloutNotificationListTask"
+ "_OBJC_CLASS_$_TRISetupAssistantFetchTask"
+ "_OBJC_CLASS_$_TRISetupAssistantFetchUtils"
+ "_OBJC_CLASS_$_TRISizedCKRecordID"
+ "_OBJC_CLASS_$_TRITaskCapabilityModifier"
+ "_OBJC_CLASS_$_TRITelemetryFactory"
+ "_OBJC_CLASS_$_TRITempDirScopeGuard"
+ "_OBJC_CLASS_$_TRITreatmentAssetFetchPlan"
+ "_OBJC_CLASS_$_TRITreatmentQualifiedAssetIndex"
+ "_OBJC_CLASS_$_TRITripersistedClientRolloutArtifactRoot"
+ "_OBJC_CLASS_$_TRIUrgentRollbackScheduler"
+ "_OBJC_CLASS_$_TRIXPCActivityCriteria"
+ "_OBJC_CLASS_$_TRIXPCServerContextPromise"
+ "_OBJC_METACLASS_$_TRIAggregateFetchRecordsProgress"
+ "_OBJC_METACLASS_$_TRIAggregateFetchRecordsProgressGuardedData"
+ "_OBJC_METACLASS_$_TRIAssetDiffQueryGuardedData"
+ "_OBJC_METACLASS_$_TRIAssetMetadataReservedKeys"
+ "_OBJC_METACLASS_$_TRIAssetStoreOperator"
+ "_OBJC_METACLASS_$_TRICKAssetMetadata"
+ "_OBJC_METACLASS_$_TRICKOpCancelingGuardedData"
+ "_OBJC_METACLASS_$_TRICKOperationGroupFactory"
+ "_OBJC_METACLASS_$_TRICKQueryLog"
+ "_OBJC_METACLASS_$_TRICKQueryLogGuardedData"
+ "_OBJC_METACLASS_$_TRICKRecordProgress"
+ "_OBJC_METACLASS_$_TRICacheDeleteUtils"
+ "_OBJC_METACLASS_$_TRICancelableCKOperation"
+ "_OBJC_METACLASS_$_TRIClientFactorPackUtils"
+ "_OBJC_METACLASS_$_TRIDeferralNotifier"
+ "_OBJC_METACLASS_$_TRIDeferredDeleter"
+ "_OBJC_METACLASS_$_TRIDiffableAssetBuilder"
+ "_OBJC_METACLASS_$_TRIDownloadLatencyTaskResultTelemetryBuilder"
+ "_OBJC_METACLASS_$_TRIExperimentBaseTaskGuardedData"
+ "_OBJC_METACLASS_$_TRIExperimentDeploymentRefStore"
+ "_OBJC_METACLASS_$_TRIExperimentHistoryDatabase"
+ "_OBJC_METACLASS_$_TRIFactorPackAssetFetchPlan"
+ "_OBJC_METACLASS_$_TRIFactorPackSet"
+ "_OBJC_METACLASS_$_TRIFactorPackSetExternalReferenceStore"
+ "_OBJC_METACLASS_$_TRIFactorPackSetStorage"
+ "_OBJC_METACLASS_$_TRIFactorPackStorage"
+ "_OBJC_METACLASS_$_TRIFetchFactorPackSetPersistedTask"
+ "_OBJC_METACLASS_$_TRIFetchOnDemandFactorsPersistedTask"
+ "_OBJC_METACLASS_$_TRIFetchOnDemandFactorsPersistedTask_AssetIdFactorName"
+ "_OBJC_METACLASS_$_TRIGenericRequiredAssets"
+ "_OBJC_METACLASS_$_TRIGenericUniqueRequiredAssets"
+ "_OBJC_METACLASS_$_TRILatencyMetricTelemetryValidator"
+ "_OBJC_METACLASS_$_TRILimitedCarryProfileManager"
+ "_OBJC_METACLASS_$_TRIRequiredCloudKitAsset"
+ "_OBJC_METACLASS_$_TRISetupAssistantFetchTask"
+ "_OBJC_METACLASS_$_TRISizedCKRecordID"
+ "_OBJC_METACLASS_$_TRITaskCapabilityModifier"
+ "_OBJC_METACLASS_$_TRITelemetryFactory"
+ "_OBJC_METACLASS_$_TRITreatmentAssetFetchPlan"
+ "_OBJC_METACLASS_$_TRITreatmentQualifiedAssetIndex"
+ "_OBJC_METACLASS_$_TRITripersistedClientRolloutArtifactRoot"
+ "_OBJC_METACLASS_$_TRIUrgentRollbackScheduler"
+ "_OBJC_METACLASS_$_TRIXPCServerContextPromise"
+ "istedTask_FactorPackAssetIds"
+ "stTask"
+ "utDeploymentPersistedTask"

```
