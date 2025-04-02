## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.101.2.0.0
-  __TEXT.__text: 0x2b06c4
+1487.120.46.0.0
+  __TEXT.__text: 0x2b5e40
   __TEXT.__auth_stubs: 0x2330
-  __TEXT.__objc_stubs: 0x22260
-  __TEXT.__objc_methlist: 0x103e4
+  __TEXT.__objc_stubs: 0x226e0
+  __TEXT.__objc_methlist: 0x105c4
   __TEXT.__const: 0x485e
-  __TEXT.__cstring: 0x37236
-  __TEXT.__objc_methname: 0x3d4a6
-  __TEXT.__objc_classname: 0xe0d
-  __TEXT.__objc_methtype: 0x39fb
-  __TEXT.__oslogstring: 0x4a4e3
-  __TEXT.__gcc_except_tab: 0x2e04
+  __TEXT.__cstring: 0x37b46
+  __TEXT.__objc_methname: 0x3dc0d
+  __TEXT.__objc_classname: 0xe8a
+  __TEXT.__objc_methtype: 0x3bf5
+  __TEXT.__oslogstring: 0x4b6db
+  __TEXT.__gcc_except_tab: 0x2fc8
   __TEXT.__swift5_typeref: 0x1093
   __TEXT.__constg_swiftt: 0x14fc
   __TEXT.__swift5_fieldmd: 0xfec

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x47d8
+  __TEXT.__unwind_info: 0x4820
   __TEXT.__eh_frame: 0x332c
   __DATA_CONST.__auth_got: 0x11a8
   __DATA_CONST.__got: 0x670
   __DATA_CONST.__auth_ptr: 0x968
-  __DATA_CONST.__const: 0x6908
-  __DATA_CONST.__cfstring: 0x2b300
+  __DATA_CONST.__const: 0x6948
+  __DATA_CONST.__cfstring: 0x2b980
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x97b8
+  __DATA_CONST.__objc_selrefs: 0x98e8
   __DATA_CONST.__objc_intobj: 0x558
-  __DATA_CONST.__objc_arraydata: 0xb50
+  __DATA_CONST.__objc_arraydata: 0xb98
   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x15120
-  __DATA.__objc_classrefs: 0x7d0
+  __DATA.__objc_const: 0x15250
+  __DATA.__objc_protorefs: 0x18
+  __DATA.__objc_classrefs: 0x7d8
   __DATA.__objc_superrefs: 0x2f8
-  __DATA.__objc_ivar: 0x13f0
+  __DATA.__objc_ivar: 0x13fc
   __DATA.__objc_data: 0x2778
-  __DATA.__data: 0x25aa
+  __DATA.__data: 0x26ca
   __DATA.__s_async_hook: 0x190
   __DATA.__swift56_hooks: 0xb0
-  __DATA.__bss: 0x54f8
+  __DATA.__bss: 0x5518
   __DATA.__common: 0x90
   - /System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity
   - /System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/Versions/A/MobileAssetExclaveServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/Seeding.framework/Versions/A/Seeding

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8431
-  Symbols:   15418
-  CStrings:  16602
+  Functions: 8466
+  Symbols:   15518
+  CStrings:  16764
 
Symbols:
+ +[MADAutoAssetControlManager autoAssetJobCoalescePostedToFinishedSetSchedulerTrigger:]
+ +[MADAutoAssetControlManager autoAssetJobCoalescePostedToFinishedSingletonSchedulerTrigger:]
+ +[SecureMobileAssetBundle _requiresLiveExclaveNonce]
+ +[SecureMobileAssetBundle _requiresLiveExclaveNonce].cold.1
+ +[SecureMobileAssetBundle _shouldUseConclave:]
+ +[SecureMobileAssetBundle commitStagedManifestsToExclavesForSelectors:darwinOnly:error:]
+ +[SecureMobileAssetBundle getExclaveManager:]
+ -[ControlManager registerWithSpaceAttributionArray]
+ -[ControlManager setRegisterWithSpaceAttributionArray:]
+ -[ControlManager setUnregisterWithSpaceAttributionArray:]
+ -[ControlManager unregisterWithSpaceAttributionArray]
+ -[ControlManager updateSAFRegistrationArrayWithPath:doRegistration:]
+ -[MADAutoAssetControlManager _doesSetDescriptorDownloadedMatchLatestToVend:forSetDescriptor:]
+ -[MADAutoAssetControlManager action_CoalesceLateJobScheduled:error:]
+ -[MADAutoAssetControlManager action_CoalesceLateJobSetScheduled:error:]
+ -[MADAutoAssetControlManager locateDownloadedNewForSelector:assetSelector:limitedToStaging:]
+ -[MADAutoAssetControlManager setDescriptorWalkKeysForClientDomainName:assetSetIdentifier:]
+ -[MADAutoAssetControlManager trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:isReadOnlyForResumeFromPersisted:]
+ -[MADAutoAssetJob _autoAssetJobDead:]
+ -[MADAutoAssetJob action_FinshedCoalescedClientReply:error:]
+ -[MADAutoAssetJob action_NowDeadClear:error:]
+ -[MADAutoAssetJob action_RerouteSchedulerTrigger:error:]
+ -[MADAutoAssetJob finishedAcknowledgeAutoAssetJob]
+ -[MADAutoAssetJob firstLookupError]
+ -[MADAutoAssetJob setFirstLookupError:]
+ -[MADAutoAssetPersisted persistedEntryIDs:assetSelector:]
+ -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:isReadOnlyForResumeFromPersisted:]
+ -[SecureMobileAssetBundle _activateManifestInExclaves:error:]
+ -[SecureMobileAssetBundle _storeManifestToExclaves:infoPlist:stage:error:]
+ -[SecureMobileAssetBundle isPersonalizedForExclaves:staged:]
+ GCC_except_table107
+ GCC_except_table12
+ GCC_except_table149
+ GCC_except_table168
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table243
+ GCC_except_table31
+ GCC_except_table39
+ GCC_except_table446
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table637
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table663
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table796
+ GCC_except_table83
+ GCC_except_table89
+ GCC_except_table90
+ MABrainUtilityConclaveEnabled.answer
+ MABrainUtilityConclaveEnabled.cold.1
+ MABrainUtilityConclaveEnabled.onceToken
+ OBJC_IVAR_$_ControlManager._registerWithSpaceAttributionArray
+ OBJC_IVAR_$_ControlManager._unregisterWithSpaceAttributionArray
+ OBJC_IVAR_$_MADAutoAssetJob._firstLookupError
+ _MABrainUtilityConclaveEnabled
+ _OBJC_CLASS_$_SecureMobileAssetExclaveManager
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1124
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1125
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1133
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1134
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1172
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1219
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1274
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1281
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1160
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2323
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2524
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2525
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3315
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3316
+ __MABrainUtilityConclaveEnabled_block_invoke.cold.1
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol
+ __OBJC_PROTOCOL_$_MAExclaveManifestStorageServiceProtocol2
+ __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceBaseProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_MAExclaveManifestStorageServiceProtocol2
+ ___52+[SecureMobileAssetBundle _requiresLiveExclaveNonce]_block_invoke
+ ___MABrainUtilityConclaveEnabled_block_invoke
+ __block_literal_global.1155
+ __block_literal_global.1169
+ __block_literal_global.1171
+ __block_literal_global.1271
+ __block_literal_global.1319
+ __block_literal_global.1321
+ __block_literal_global.1334
+ __block_literal_global.1540
+ __block_literal_global.1754
+ __block_literal_global.2242
+ __block_literal_global.2253
+ __block_literal_global.2261
+ __block_literal_global.2269
+ __block_literal_global.2277
+ __block_literal_global.2285
+ __block_literal_global.2293
+ __block_literal_global.2301
+ __block_literal_global.2309
+ __block_literal_global.2321
+ __block_literal_global.3981
+ __block_literal_global.405
+ __block_literal_global.5005
+ __os_feature_enabled_impl
+ _getMappedExclavePath
+ _objc_msgSend$_activateManifestInExclaves:error:
+ _objc_msgSend$_autoAssetJobDead:
+ _objc_msgSend$_doesSetDescriptorDownloadedMatchLatestToVend:forSetDescriptor:
+ _objc_msgSend$_requiresLiveExclaveNonce
+ _objc_msgSend$_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:isReadOnlyForResumeFromPersisted:
+ _objc_msgSend$_shouldUseConclave:
+ _objc_msgSend$_storeManifestToExclaves:infoPlist:stage:error:
+ _objc_msgSend$action_CoalesceLateJobScheduled:error:
+ _objc_msgSend$action_CoalesceLateJobSetScheduled:error:
+ _objc_msgSend$action_FinshedCoalescedClientReply:error:
+ _objc_msgSend$action_NowDeadClear:error:
+ _objc_msgSend$action_RerouteSchedulerTrigger:error:
+ _objc_msgSend$activateCommittedManifestForFSTag:specifier:error:
+ _objc_msgSend$autoAssetJobCoalescePostedToFinishedSetSchedulerTrigger:
+ _objc_msgSend$autoAssetJobCoalescePostedToFinishedSingletonSchedulerTrigger:
+ _objc_msgSend$checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:
+ _objc_msgSend$checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:
+ _objc_msgSend$commitStagedManifestForFSTags:error:
+ _objc_msgSend$commitStagedManifestForFSTags:specifiers:error:
+ _objc_msgSend$commitStagedManifestsToExclavesForSelectors:darwinOnly:error:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$darwinOnly
+ _objc_msgSend$finishedAcknowledgeAutoAssetJob
+ _objc_msgSend$firstLookupError
+ _objc_msgSend$getExclaveManager:
+ _objc_msgSend$integrityCatalogPath
+ _objc_msgSend$isPersonalizedForExclaves:staged:
+ _objc_msgSend$locateDownloadedNewForSelector:assetSelector:limitedToStaging:
+ _objc_msgSend$persistedEntryIDs:assetSelector:
+ _objc_msgSend$proposeNonce:
+ _objc_msgSend$setDescriptorWalkKeysForClientDomainName:assetSetIdentifier:
+ _objc_msgSend$setFirstLookupError:
+ _objc_msgSend$setRegisterWithSpaceAttributionArray:
+ _objc_msgSend$setUnregisterWithSpaceAttributionArray:
+ _objc_msgSend$stageManifest:infoPlist:catalog:error:
+ _objc_msgSend$stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:
+ _objc_msgSend$storeManifest:infoPlist:catalog:error:
+ _objc_msgSend$trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:isReadOnlyForResumeFromPersisted:
+ _objc_msgSend$updateSAFRegistrationArrayWithPath:doRegistration:
+ _requiresLiveExclaveNonce.onceToken
+ _requiresLiveExclaveNonce.required
- -[MADAutoAssetControlManager trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:]
- -[MADAutoAssetScheduler _scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:]
- GCC_except_table148
- GCC_except_table167
- GCC_except_table175
- GCC_except_table180
- GCC_except_table242
- GCC_except_table41
- GCC_except_table441
- GCC_except_table51
- GCC_except_table631
- GCC_except_table635
- GCC_except_table643
- GCC_except_table657
- GCC_except_table66
- GCC_except_table789
- GCC_except_table80
- GCC_except_table81
- GCC_except_table87
- _SecCertificateCreateWithBytes
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1121
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1122
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1130
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1131
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1148
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1195
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1250
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1257
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1070
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2308
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2509
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2510
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3294
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3295
- __block_literal_global.1145
- __block_literal_global.1147
- __block_literal_global.1268
- __block_literal_global.1310
- __block_literal_global.1316
- __block_literal_global.1318
- __block_literal_global.1424
- __block_literal_global.1607
- __block_literal_global.2227
- __block_literal_global.2238
- __block_literal_global.2246
- __block_literal_global.2254
- __block_literal_global.2262
- __block_literal_global.2270
- __block_literal_global.2278
- __block_literal_global.2286
- __block_literal_global.2308
- __block_literal_global.3954
- __block_literal_global.4978
- _objc_msgSend$_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:
- _objc_msgSend$isEqualSelector:
- _objc_msgSend$trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:
CStrings:
+ "\n[ELIMINATE]{%{public}@} no active job withVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
+ "\n[ELIMINATE]{%{public}@} no active job withoutVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
+ "%@:locateDownloadedNewForSelector"
+ "%@:removeCurrentJob"
+ "'\x14I"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/MobileAssetBrain/ControlManager.m"
+ "2.6.1"
+ "@\"NSDictionary\"24@0:8^@16"
+ "A Certificate inside the CertificateChain is not an NSData"
+ "Activating committed manifest is not supported on this OS"
+ "B24@0:8I16B20"
+ "B28@0:8I16^@20"
+ "B32@0:8@\"NSArray\"16^@24"
+ "B36@0:8I16@\"NSString\"20^@28"
+ "B36@0:8I16@20^@28"
+ "B40@0:8@\"NSArray\"16@\"NSArray\"24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32^@40"
+ "B60@0:8I16@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44^@52"
+ "B60@0:8I16@20@28@36@44^@52"
+ "B64@0:8I16B20@\"NSData\"24@\"NSData\"32@\"NSData\"40^B48^@56"
+ "B64@0:8I16B20@24@32@40^B48^@56"
+ "B72@0:8I16@\"NSString\"20I28@\"NSData\"32@\"NSData\"40@\"NSData\"48^B56^@64"
+ "B72@0:8I16@20I28@32@40@48^B56^@64"
+ "Cannot map to Exclaves: _storeManifestToExclaves failed"
+ "Cannot map to Exclaves: info plist data is nil"
+ "Cannot map to Exclaves: info plist path is nil"
+ "Cannot map to Exclaves: ticket data is nil"
+ "Cannot map to Exclaves: ticket path is nil"
+ "Certificate data is not an NSData"
+ "CertificateChain"
+ "CertificateChain is not an NSArray"
+ "CoalesceLateJobScheduled"
+ "CoalesceLateJobSetScheduled"
+ "DEL_AI_DROP_MATCHES_LATEST "
+ "Dead"
+ "Failed to activate committed manifest in Exclaves"
+ "Failed to allocate NSNumber for fstag"
+ "Failed to commit staged manifests to Exclaves"
+ "Failed to get exclave nonces"
+ "Failed to get shared instance of SecureMobileAssetExclave"
+ "FinishAcknowledged"
+ "Finished"
+ "FinshedCoalescedClientReply"
+ "GlowFSeed"
+ "JobFinishedRerouteScheduled"
+ "LiveStorageExclaveNonce"
+ "MAExclaveManifestStorageServiceBaseProtocol"
+ "MAExclaveManifestStorageServiceProtocol"
+ "MAExclaveManifestStorageServiceProtocol2"
+ "MobileAssetExclaveServices is not available on this version of the OS"
+ "NewerErr"
+ "NowDeadClear"
+ "RerouteSchedulerTrigger"
+ "SetJobFinishedRerouteScheduled"
+ "Starting built-in MobileAsset brain built Mar 21 2025 21:13:14"
+ "Starting downloaded MobileAsset brain (version: %@) built Mar 21 2025 21:13:14"
+ "T@\"NSError\",&,N,V_firstLookupError"
+ "T@\"NSMutableArray\",&,N,V_registerWithSpaceAttributionArray"
+ "T@\"NSMutableArray\",&,N,V_unregisterWithSpaceAttributionArray"
+ "The CertificateChain array is empty"
+ "Unable to unregister fstag mapping"
+ "[%{public}@] {%{public}@}\n[ROUTING-TABLE-REMOVE] removed from currentJobsBySelector | withVersionSelector:%{public}@ | autoJobBySelector:%{public}@"
+ "[%{public}@] {%{public}@}\n[ROUTING-TABLE-REMOVE] removed from currentJobsBySelector | withoutVersionSelector:%{public}@ | autoJobBySelector:%{public}@"
+ "[%{public}@] {%{public}@}\n[ROUTING-TABLE-REMOVE] removed from currentJobsByUUID | autoAssetJobUUID:%{public}@ | autoJobByUUID:%{public}@"
+ "[%{public}@] {%{public}@}\n[ROUTING-TABLE-REMOVE] removed from currentJobsByUUID | secondaryAutoAssetUUID:%{public}@ | autoJobByUUID:%{public}@"
+ "[%{public}@] {%{public}@}\n[ROUTING-TABLE-REMOVE] removed from currentSetJobsByIdentifier | clientDomainName:%{public}@ | setJobIdentifier:%{public}@ | autoSetJob:%{public}@"
+ "[%{public}@] {%{public}@} removed auto-asset-job from tracking | removals:%{public}@"
+ "[CONTROL_MANAGER_CACHEDELETE_QUEUE] {respondToCacheDelete} performing cache-delete triggered operation for volume %@ at urgency %d ..."
+ "[MAB] \ninfo = %@"
+ "[MAB] %@ does not exist"
+ "[MAB] %s"
+ "[MAB] %sActivity %@ \"%@\" fired."
+ "[MAB] %sActivity %@ \"%@\" will complete asynchronously."
+ "[MAB] AEA extractor will be loaded from the system volume because MobileAsset Brain is built-in."
+ "[MAB] AEA extractor will be loaded from the system volume because loading from the cryptex is unsupported on this OS."
+ "[MAB] Allocating bundle failed for %@"
+ "[MAB] Allocating scheduler object failed"
+ "[MAB] Allocating targetPath failed for target %@"
+ "[MAB] AppleConnect SSO token successfully read"
+ "[MAB] AppleConnect is available in this environment"
+ "[MAB] AppleConnect is not available in this environment"
+ "[MAB] Attempting to copy BuildManifest from %@ to %@"
+ "[MAB] Attempting to copy Cryptex1 ticket for current boot from %@ to %@"
+ "[MAB] Attempting to copy Cryptex1 ticket from %@ to %@"
+ "[MAB] Attempting to copy file from %@ to %@"
+ "[MAB] Attempting to read AppleConnect SSO token with %s interactivity level"
+ "[MAB] Available brain doesn't have any declared features.  Asset requires: %@"
+ "[MAB] Boot session UUID has an invalid length (%zu)"
+ "[MAB] Brain features: %@"
+ "[MAB] Caller canceled enumeration"
+ "[MAB] Canceled device unlock action (token=%d)..."
+ "[MAB] Could not allocate buffer to copy boot session UUID"
+ "[MAB] Could not copy boot session UUID: %d (%s)"
+ "[MAB] Could not create directory enumerator for %@"
+ "[MAB] Could not graft %s to %s"
+ "[MAB] Could not look up boot session UUID: %d (%s)"
+ "[MAB] Could not lstat %s"
+ "[MAB] Could not ungraft %s"
+ "[MAB] Crash loop testing is enabled.  mobileassetd will exit in %d seconds"
+ "[MAB] Cryptex1 nonce management is not available on this host."
+ "[MAB] Device is already unlocked.  Starting action \"%@\""
+ "[MAB] Device is now unlocked.  Starting action \"%@\" (token=%d)"
+ "[MAB] Device is still locked.  Deferring action \"%@\" (token=%d)"
+ "[MAB] Device unlock action \"%@\" is scheduled (token=%d)"
+ "[MAB] Error canceling device unlock action (token=%d). errno=%d (%s)"
+ "[MAB] Error committing MobileAssetBrain bundle %@ as current: %@"
+ "[MAB] Error loading contents of %@: %@"
+ "[MAB] Error removing item %@: %@"
+ "[MAB] Error removing old MobileAssetBrain installation directory: %@"
+ "[MAB] Exiting MA brain before relaunching to use newly installed version"
+ "[MAB] Exiting mobileassetd for crash loop testing..."
+ "[MAB] Exiting mobileassetd for relaunch..."
+ "[MAB] Exiting mobileassetd for release testing..."
+ "[MAB] Exiting mobileassetd to revert to built-in MobileAsset brain..."
+ "[MAB] Failed to copy the PDI MobileAssetBrain nonce: %d"
+ "[MAB] Failed to create directory %@ for UpdateResult.plist: %@"
+ "[MAB] Failed to create directory name from pathname %@"
+ "[MAB] Failed to mark bundle(%@) as current brain."
+ "[MAB] Failed to read AppleConnect SSO token: %@"
+ "[MAB] Failed to remove stale UpdateResult.plist: %@"
+ "[MAB] Failed to write %@ with contents of dictionary:%@\n%@"
+ "[MAB] Failed to write %@: %@"
+ "[MAB] Failed to write stagingName final path component(%@) to proposed path(%@)"
+ "[MAB] Found MA brain ticket: %@"
+ "[MAB] Got a NULL return from IORegistryEntryCreateCFProperty"
+ "[MAB] Got a non-CFData return value from IORegistryEntryCreateCFProperty for property %@"
+ "[MAB] Internal Error - no value for required feature: %@"
+ "[MAB] Invalid ssoToken=%@"
+ "[MAB] Invalid target path at %@"
+ "[MAB] MABrainLoader did not specify compatiblity version"
+ "[MAB] MABrainLoader specified specious compatiblity version: %@"
+ "[MAB] MobileAsset brain download completed successfully"
+ "[MAB] MobileAsset brain download failed: %@"
+ "[MAB] MobileAsset brain scan completed successfully\n MABrain asset: %@"
+ "[MAB] MobileAsset brain scan failed: %@"
+ "[MAB] MobileAssetBrain %s download initiated: %@"
+ "[MAB] MobileAssetBrain (version: %@) install completed successfully"
+ "[MAB] MobileAssetBrain (version: %@) staged for next relaunch"
+ "[MAB] MobileAssetBrain bundle %@ needs to be committed as current"
+ "[MAB] MobileAssetBrain install of asset %@ is starting..."
+ "[MAB] MobileAssetBrain update completed successfully:\n%@"
+ "[MAB] MobileAssetBrain update failed:\n%@"
+ "[MAB] New brain doesn't meet requirements: %@"
+ "[MAB] New brain features: %@"
+ "[MAB] New brain meets asset requirements - going forward with the update"
+ "[MAB] No MobileAssetBrain update found, but no error was reported."
+ "[MAB] No MobileAssetBrain update found."
+ "[MAB] Overriding supported features: %@"
+ "[MAB] Pending MobileAssetBrain version is now %@"
+ "[MAB] Pending MobileAssetBrain version is now nil due to failed download"
+ "[MAB] Pending MobileAssetBrain version is now nil due to failed install"
+ "[MAB] Performing MABrain garbage collection (current=%@)..."
+ "[MAB] Personalizing MobileAssetBrain again, this time with AppleConnect SSO..."
+ "[MAB] Personalizing MobileAssetBrain%s..."
+ "[MAB] Preserving item %@"
+ "[MAB] Preserving item %@ (still grafted)"
+ "[MAB] Proceeding on Tatsu authorization failure because unpersonalized brains are allowed: %@"
+ "[MAB] Release Test Mode is enabled.  Scheduling update on startup..."
+ "[MAB] Removed stale UpdateResult.plist"
+ "[MAB] Required feature '%@' is not a number: %@ [%@]"
+ "[MAB] Starting MABrainUpdater..."
+ "[MAB] Successfully committed MobileAssetBrain bundle %@ as current."
+ "[MAB] Successfully copied the Cryptex1 MobileAssetBrain PDI nonce."
+ "[MAB] Successfully grafted %@ onto %@"
+ "[MAB] Successfully personalized 2nd brain ticket with current-boot-only PDI nonce"
+ "[MAB] Successfully pre-rolled the Cryptex1 MobileAssetBrain nonce."
+ "[MAB] Successfully removed item %@"
+ "[MAB] Successfully removed old MobileAssetBrain installation directory"
+ "[MAB] Successfully rolled the Cryptex1 MobileAssetBrain nonce"
+ "[MAB] Successfully scheduled %@"
+ "[MAB] Successfully ungrafted %@ from the file system using %@"
+ "[MAB] Successfully wrote %@ (using NSData)."
+ "[MAB] Successfully wrote %@."
+ "[MAB] Unable to set SSO token for user authlisting"
+ "[MAB] Unable to set secure TSS URL for user authlisting"
+ "[MAB] User-authlisting enabled."
+ "[MAB] Using GRAFTDMG_CRYPTEX_BOOT"
+ "[MAB] Using GRAFTDMG_CRYPTEX_PDI_NONCE"
+ "[MAB] Waiting for AuthenticationServices completed."
+ "[MAB] Waiting for AuthenticationServices response..."
+ "[MAB] mobileassetd needs to relaunch at next unlock"
+ "[MORE_CLIENT_REQUESTS] {%{public}@} auto-asset-job indicated removal but has more to do | eventInfo:%{public}@"
+ "[SMA] \ndevnodes=%@"
+ "[SMA] %@ manifest for %@"
+ "[SMA] %@ unmount for %@"
+ "[SMA] %s"
+ "[SMA] <%@> has a registered Exclave mapped path [fstag=%d]: %@"
+ "[SMA] AMAuthInstallCreate() failed"
+ "[SMA] AMAuthInstallUpdaterCryptex1CopyTicket() failed: %@"
+ "[SMA] AMAuthInstallUpdaterCryptex1CopyTicket() is unavailable"
+ "[SMA] Activating committed manifest for %@:%@ fstag=%u"
+ "[SMA] Activating committed manifest is not supported on this OS"
+ "[SMA] All specifiers of AssetType %@ are configured to fail personalization"
+ "[SMA] Allow listed for Exclaves: %@:%@ fstag=%u"
+ "[SMA] Attempting to copy BuildManifest from %@ to %@"
+ "[SMA] Attempting to copy file from %@ to %@"
+ "[SMA] Attempting to symlink %@ to %@"
+ "[SMA] Begin access failed for secure asset (%@): %@"
+ "[SMA] Begin access successful for secure asset: %@"
+ "[SMA] Bundle already personalized and personalized manifest staged, skipping: %@"
+ "[SMA] Bundle already personalized, skipping: %@"
+ "[SMA] Cannot map to Exclaves: activate manifest failed"
+ "[SMA] Committing staged exclave manifests for fsTags and specifiers: [%@] [%@]"
+ "[SMA] Committing staged exclave manifests for fsTags: %@"
+ "[SMA] Committing staged manifests for selectors: %@"
+ "[SMA] Conflicting registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
+ "[SMA] Could not determine whether cryptex at %@ is graftable: %s"
+ "[SMA] Could not lstat %s"
+ "[SMA] Could not ungraft %s"
+ "[SMA] Cryptex at %@ is graftable"
+ "[SMA] Cryptex at %@ is not graftable"
+ "[SMA] Crytex is already dmg mounted"
+ "[SMA] Darwin nonce digest: %@"
+ "[SMA] Default %@ invalid. Uneven number of ':' separated elements:[%@]"
+ "[SMA] Depersonalizing %@"
+ "[SMA] Ejected %@ after mount failure"
+ "[SMA] End access failed for secure asset (%@): %@"
+ "[SMA] End access successful for secure asset: %@"
+ "[SMA] Exclave nonce digest: %@"
+ "[SMA] Failed to activate committed manifest because conclave manager instance is nil: %@"
+ "[SMA] Failed to activate committed manifest for %@:%@ fstag=%u %@"
+ "[SMA] Failed to allocate NSNumber for fstag=%d"
+ "[SMA] Failed to attach and mount cryptex disk image: %@"
+ "[SMA] Failed to attach cryptex disk image: %@"
+ "[SMA] Failed to commit staged manifests to Exclaves"
+ "[SMA] Failed to commit staged manifests: %@"
+ "[SMA] Failed to depersonalize: %@"
+ "[SMA] Failed to eject cryptex disk image previously mounted at %@: %@"
+ "[SMA] Failed to generate nonce proposal: %d (%s)"
+ "[SMA] Failed to get nonce dictionary from SecureMobileAssetExclave: %@"
+ "[SMA] Failed to get shared instance of SecureMobileAssetExclave"
+ "[SMA] Failed to get shared instance of SecureMobileAssetExclave: %@"
+ "[SMA] Failed to graft: %@"
+ "[SMA] Failed to personalize asset bundle: %@"
+ "[SMA] Failed to ungraft: %@"
+ "[SMA] Failed to unmount and eject cryptex disk image: %@"
+ "[SMA] Generating nonce proposal for darwin"
+ "[SMA] Generating nonce proposal for exclaves"
+ "[SMA] Img4DecodeGetManifest() failed for %@: %d"
+ "[SMA] Img4DecodeInit() failed for %@: %d"
+ "[SMA] Invalid ssoToken=%@"
+ "[SMA] MASecureManifestStorage isn't available"
+ "[SMA] MASecureMobileAssetTypes is unavailable"
+ "[SMA] Matching registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
+ "[SMA] MobileAssetExclaveServices is not available on this version of the OS"
+ "[SMA] No requestTags found in existing amai object. Creating new object"
+ "[SMA] No selectors specified"
+ "[SMA] Not adding additional requestTags to personalization request"
+ "[SMA] Not allow listed for Exclaves: %@:%@"
+ "[SMA] Nothing to eject!"
+ "[SMA] Obtained nonce (%lu bytes) and digest (%lu bytes)"
+ "[SMA] Operations will be restricted to darwin only"
+ "[SMA] Registering dissenter for volume: %@"
+ "[SMA] Registering unmount approval callback"
+ "[SMA] Removed personalized bundle: %@"
+ "[SMA] SecureMobileAsset did not contain a personalized entry for %@"
+ "[SMA] Setting headers: %@"
+ "[SMA] Signing server is '%@'"
+ "[SMA] Simulating personalization failure of asset(%@) due to default"
+ "[SMA] Successfully activated committed manifest for %@:%@ fstag=%u"
+ "[SMA] Successfully attached %@ with ID: %@"
+ "[SMA] Successfully ejected cryptex disk image previously mounted at %@"
+ "[SMA] Successfully grafted %@ onto %@"
+ "[SMA] Successfully mounted cryptex volume %@ at %@"
+ "[SMA] Successfully registered Exclave mapped path [fstag=%d] %@:%@: %s"
+ "[SMA] Successfully ungrafted %@ from the file system using %@"
+ "[SMA] Successfully unmounted cryptex volume %@ from %@"
+ "[SMA] Successfully unregistered Exclave mapped path [fstag=%d]: %@"
+ "[SMA] The current AssetType(%@) is in the list of those configured to fail personalization but the current specifier(%@) is not"
+ "[SMA] The current specifier(%@) of AssetType %@ is configured to fail personalization"
+ "[SMA] Unable to get SecureMobileAssetExclave instance in this environment"
+ "[SMA] Unable to set SSO token for user authlisting"
+ "[SMA] Unable to set signing server retry count | AMAuthInstallSetSigningServerRetry() failed with error %d (%@)"
+ "[SMA] Unregistering dissenter for volume: %@"
+ "[SMA] User-authlisting enabled."
+ "[SMA] Using overridden value for signing server"
+ "[SMA] WARNING: %@"
+ "[SMA] WARNING: Failed to eject %@ after mount failure: %@"
+ "[SMA] WARNING: Using software coprocessor parameters override:\n%@"
+ "[SMA] Warning: MAExclaveManifestStorageService does not support staging, commit is a no-op"
+ "[SMA] Warning: MAExclaveManifestStorageService does not support staging, storing manifest instead"
+ "[SMA] Warning: MASecureManifestStorage does not support staging, commit is a no-op"
+ "[SMA] Warning: MASecureManifestStorage does not support staging, returning nil"
+ "[SMA] Warning: MASecureManifestStorage does not support staging, storing manifest instead"
+ "[SMA] [Personalization] enqueue %@"
+ "[SMA] [Personalization] finish %@ (success = %i, error = %@)"
+ "[SMA] [Personalization] start %@"
+ "[SMA] [SecureMAHelper]: Creating new graft list for tracking grafted assets"
+ "[SMA] [SecureMAHelper]: Failed to create folder(%@) for grafted list file: %@"
+ "[SMA] [SecureMAHelper]: Failed to delete graft list file at %@ : %@"
+ "[SMA] [SecureMAHelper]: Failed to delete graft list file at path %@. Error: %@"
+ "[SMA] [SecureMAHelper]: Failed to load existing graft list at path %@. Error: %@"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@ to file %@: %@"
+ "[SMA] [SecureMAHelper]: Graft list does not exist at %@"
+ "[SMA] [SecureMAHelper]: Successfully created folder(%@) for grafted list file"
+ "[SMA] [SecureMAHelper]: Successfully recorded graft entry for asset of type %@"
+ "_activateManifestInExclaves:error:"
+ "_autoAssetJobDead:"
+ "_doesSetDescriptorDownloadedMatchLatestToVend:forSetDescriptor:"
+ "_firstLookupError"
+ "_latestDownloadedDescriptor"
+ "_registerWithSpaceAttributionArray"
+ "_requiresLiveExclaveNonce"
+ "_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:isReadOnlyForResumeFromPersisted:"
+ "_shouldUseConclave:"
+ "_storeManifestToExclaves:infoPlist:stage:error:"
+ "_unregisterWithSpaceAttributionArray"
+ "action_CoalesceLateJobScheduled:error:"
+ "action_CoalesceLateJobSetScheduled:error:"
+ "action_FinshedCoalescedClientReply:error:"
+ "action_NowDeadClear:error:"
+ "action_RerouteSchedulerTrigger:error:"
+ "activateCommittedManifestForFSTag:specifier:error:"
+ "autoAssetJobCoalescePostedToFinishedSetSchedulerTrigger:"
+ "autoAssetJobCoalescePostedToFinishedSingletonSchedulerTrigger:"
+ "checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:"
+ "checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:"
+ "com.apple.MobileAsset.UAF.FM.CodeLM"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.Search.ODLA"
+ "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
+ "com.apple.MobileAsset.UAF.VoiceAssistant"
+ "com.apple.mobileassetd.handleEstimateEvictableBytesForSoftwareUpdateRequest"
+ "com.apple.mobileassetd.handleSuspendForSoftwareUpdateRequest-spaceCheck"
+ "com.apple.mobileassetd.handleSuspendForSoftwareUpdateRequest-suspendComplete"
+ "com_apple_mobileassetd_conclave"
+ "commitStagedManifestForFSTags:error:"
+ "commitStagedManifestForFSTags:specifiers:error:"
+ "commitStagedManifestsToExclavesForSelectors:darwinOnly:error:"
+ "d\x1f\x0f\a\x17<+\x14"
+ "digestNonce"
+ "encountered job indicating finished when not a current job | eventInfo:%@"
+ "failed to get integrity catalog path"
+ "failed to read cryptex integrity catalog"
+ "failed to stage manifest in Exclave Secure Storage"
+ "failed to store manifest in Exclave Secure Storage"
+ "finishedAcknowledgeAutoAssetJob"
+ "firstLookupError"
+ "getExclaveManager:"
+ "invalidateManifestForFSTag:error:"
+ "invalidateManifestForFSTag:specifier:error:"
+ "isPersonalizedForExclaves:staged:"
+ "isSetDescriptor:coveredBySetDescriptorStatus"
+ "locateDownloadedNewForSelector"
+ "locateDownloadedNewForSelector:assetSelector:limitedToStaging:"
+ "mappedPath"
+ "persistedEntryIDs:assetSelector:"
+ "proposeNonce:"
+ "rawNonce"
+ "registerWithSpaceAttributionArray"
+ "set-descriptor (to be adopted as just-downloaded) discoveredAtomicInstance matches latest-to-vend [nothing new]"
+ "set-descriptor (to be adopted as just-downloaded) downloadedAtomicInstance matches latest-to-vend [nothing new]"
+ "set-job completed with 0 entries"
+ "setDescriptorKeysForAssetSet"
+ "setDescriptorWalkKeysForClientDomainName:assetSetIdentifier:"
+ "setFirstLookupError:"
+ "setRegisterWithSpaceAttributionArray:"
+ "setUnregisterWithSpaceAttributionArray:"
+ "stageManifest:infoPlist:catalog:error:"
+ "stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:"
+ "storeManifest:infoPlist:catalog:error:"
+ "trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:isReadOnlyForResumeFromPersisted:"
+ "unregisterWithSpaceAttributionArray"
+ "updateSAFRegistrationArrayWithPath:doRegistration:"
+ "v68@0:8@16q24q32B40B44@48B56B60B64"
+ "{%@} no auto-asset-descriptor entry found | entry:%{public}@"
+ "{%@} no persisted-entry found | assetSelector:%{public}@"
+ "{%@} no persisted-entry found | entry:%{public}@"
+ "{%@} unable to locate atomic-instance for set-descriptor | downloadedSetDescriptor:%@"
+ "{%@} unable to locate set-descriptor for locked atomic-instance | setAtomicInstanceUUID:%@"
+ "{%@} unexpected inconsistency for nextDownloadedSetDescriptor expected in staging | nextDownloadedSetDescriptor:%@"
+ "{%{public}@}\n[BECAME-LATEST-TO-VEND] adopted set-descriptor as latest-to-vend\n| persistReason:%{public}@\n| setDescriptor:%{public}@"
+ "{%{public}@}\n[POTENTIAL-LATEST-TO-VEND] not setting latestAtomicInstanceToVend (same as already latest-to-vend) | setJobDescriptor:%{public}@"
+ "{%{public}@}\n[SET_CLIENT_REQUESTS_LATE_COALESCE] | last client-request has completed for set-job that is not active and not being canceled - late-coalesce | eventInfo:%{public}@"
+ "{%{public}@}: atomic-instance considered for adoption | shouldAdoptAsDownloaded:%{public}@ | setAtomicInstance:%{public}@"
+ "{%{public}@}: atomic-instance no longer valid - never adopt | setAtomicInstance:%{public}@"
+ "{FinshedCoalescedClientReply} already another active job-task | eventInfo:%@"
+ "{_autoAssetJobDead} %ld job-tasks when should be none (potentially stranded)"
- "\n[ELIMINATE]{%{public}@:removeCurrentJob} no active job withVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
- "\n[ELIMINATE]{%{public}@:removeCurrentJob} no active job withoutVersionSelector:%{public}@ | autoAssetJobUUID:%{public}@ | eliminateTracker:%{public}@"
- "\ndevnodes=%@"
- "\ninfo = %@"
- "%@ does not exist"
- "%@ manifest for %@"
- "%@ unmount for %@"
- "%sActivity %@ \"%@\" fired."
- "%sActivity %@ \"%@\" will complete asynchronously."
- "'\x14G"
- "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileAssetBrain/ControlManager.m"
- "2.5.9"
- "AEA extractor will be loaded from the system volume because MobileAsset Brain is built-in."
- "AEA extractor will be loaded from the system volume because loading from the cryptex is unsupported on this OS."
- "AMAuthInstallCreate() failed"
- "AMAuthInstallUpdaterCryptex1CopyTicket() failed: %@"
- "AMAuthInstallUpdaterCryptex1CopyTicket() is unavailable"
- "All specifiers of AssetType %@ are configured to fail personalization"
- "Allocating bundle failed for %@"
- "Allocating scheduler object failed"
- "Allocating targetPath failed for target %@"
- "Allow listed for Exclaves: %@:%@ fstag=%u"
- "AppleConnect SSO token successfully read"
- "AppleConnect is available in this environment"
- "AppleConnect is not available in this environment"
- "Attempting to copy BuildManifest from %@ to %@"
- "Attempting to copy Cryptex1 ticket for current boot from %@ to %@"
- "Attempting to copy Cryptex1 ticket from %@ to %@"
- "Attempting to copy file from %@ to %@"
- "Attempting to read AppleConnect SSO token with %s interactivity level"
- "Attempting to symlink %@ to %@"
- "Available brain doesn't have any declared features.  Asset requires: %@"
- "Begin access failed for secure asset (%@): %@"
- "Begin access successful for secure asset: %@"
- "Boot session UUID has an invalid length (%zu)"
- "Brain features: %@"
- "Bundle already personalized and personalized manifest staged, skipping: %@"
- "Bundle already personalized, skipping: %@"
- "Caller canceled enumeration"
- "Canceled device unlock action (token=%d)..."
- "Certificate data is not CFData"
- "Committing staged manifests for selectors: %@"
- "Conflicting registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
- "Could not allocate buffer to copy boot session UUID"
- "Could not copy boot session UUID: %d (%s)"
- "Could not create directory enumerator for %@"
- "Could not determine whether cryptex at %@ is graftable: %s"
- "Could not graft %s to %s"
- "Could not look up boot session UUID: %d (%s)"
- "Could not lstat %s"
- "Could not ungraft %s"
- "Crash loop testing is enabled.  mobileassetd will exit in %d seconds"
- "Cryptex at %@ is graftable"
- "Cryptex at %@ is not graftable"
- "Cryptex1 nonce management is not available on this host."
- "Crytex is already dmg mounted"
- "Darwin nonce digest: %@"
- "Default %@ invalid. Uneven number of ':' separated elements:[%@]"
- "Depersonalizing %@"
- "Device is already unlocked.  Starting action \"%@\""
- "Device is now unlocked.  Starting action \"%@\" (token=%d)"
- "Device is still locked.  Deferring action \"%@\" (token=%d)"
- "Device unlock action \"%@\" is scheduled (token=%d)"
- "Ejected %@ after mount failure"
- "End access failed for secure asset (%@): %@"
- "End access successful for secure asset: %@"
- "Error canceling device unlock action (token=%d). errno=%d (%s)"
- "Error committing MobileAssetBrain bundle %@ as current: %@"
- "Error loading contents of %@: %@"
- "Error removing item %@: %@"
- "Error removing old MobileAssetBrain installation directory: %@"
- "Exclave nonce digest: %@"
- "Exiting MA brain before relaunching to use newly installed version"
- "Exiting mobileassetd for crash loop testing..."
- "Exiting mobileassetd for relaunch..."
- "Exiting mobileassetd for release testing..."
- "Exiting mobileassetd to revert to built-in MobileAsset brain..."
- "Failed to attach and mount cryptex disk image: %@"
- "Failed to attach cryptex disk image: %@"
- "Failed to commit staged manifests: %@"
- "Failed to copy the PDI MobileAssetBrain nonce: %d"
- "Failed to create Apple iPhone CA certificate"
- "Failed to create directory %@ for UpdateResult.plist: %@"
- "Failed to create directory name from pathname %@"
- "Failed to depersonalize: %@"
- "Failed to eject cryptex disk image previously mounted at %@: %@"
- "Failed to generate nonce proposal: %d (%s)"
- "Failed to graft: %@"
- "Failed to mark bundle(%@) as current brain."
- "Failed to personalize asset bundle: %@"
- "Failed to read AppleConnect SSO token: %@"
- "Failed to remove stale UpdateResult.plist: %@"
- "Failed to ungraft: %@"
- "Failed to unmount and eject cryptex disk image: %@"
- "Failed to write %@ with contents of dictionary:%@\n%@"
- "Failed to write %@: %@"
- "Failed to write stagingName final path component(%@) to proposed path(%@)"
- "Found MA brain ticket: %@"
- "Generating nonce proposal for darwin"
- "GlowE"
- "Got a NULL return from IORegistryEntryCreateCFProperty"
- "Got a non-CFData return value from IORegistryEntryCreateCFProperty for property %@"
- "Img4DecodeGetManifest() failed for %@: %d"
- "Img4DecodeInit() failed for %@: %d"
- "Internal Error - no value for required feature: %@"
- "Invalid ssoToken=%@"
- "Invalid target path at %@"
- "MABrainLoader did not specify compatiblity version"
- "MABrainLoader specified specious compatiblity version: %@"
- "MASecureManifestStorage isn't available"
- "MASecureMobileAssetTypes is unavailable"
- "Matching registration found for Exclave mapped path [fstag=%d] %@:%@: %@"
- "MobileAsset brain download completed successfully"
- "MobileAsset brain download failed: %@"
- "MobileAsset brain scan completed successfully\n MABrain asset: %@"
- "MobileAsset brain scan failed: %@"
- "MobileAssetBrain %s download initiated: %@"
- "MobileAssetBrain (version: %@) install completed successfully"
- "MobileAssetBrain (version: %@) staged for next relaunch"
- "MobileAssetBrain bundle %@ needs to be committed as current"
- "MobileAssetBrain install of asset %@ is starting..."
- "MobileAssetBrain update completed successfully:\n%@"
- "MobileAssetBrain update failed:\n%@"
- "New brain doesn't meet requirements: %@"
- "New brain features: %@"
- "New brain meets asset requirements - going forward with the update"
- "No MobileAssetBrain update found, but no error was reported."
- "No MobileAssetBrain update found."
- "No requestTags found in existing amai object. Creating new object"
- "Not adding additional requestTags to personalization request"
- "Not allow listed for Exclaves: %@:%@"
- "Nothing to eject!"
- "Obtained nonce (%lu bytes) and digest (%lu bytes)"
- "Overriding supported features: %@"
- "Pending MobileAssetBrain version is now %@"
- "Pending MobileAssetBrain version is now nil due to failed download"
- "Pending MobileAssetBrain version is now nil due to failed install"
- "Performing MABrain garbage collection (current=%@)..."
- "Personalizing MobileAssetBrain again, this time with AppleConnect SSO..."
- "Personalizing MobileAssetBrain%s..."
- "Preserving item %@"
- "Preserving item %@ (still grafted)"
- "Proceeding on Tatsu authorization failure because unpersonalized brains are allowed: %@"
- "Registering dissenter for volume: %@"
- "Registering unmount approval callback"
- "Release Test Mode is enabled.  Scheduling update on startup..."
- "Removed personalized bundle: %@"
- "Removed stale UpdateResult.plist"
- "SecureMobileAsset did not contain a personalized entry for %@"
- "Setting headers: %@"
- "Should"
- "Should not"
- "Signing server is '%@'"
- "Simulating personalization failure of asset(%@) due to default"
- "Starting MABrainUpdater..."
- "Starting built-in MobileAsset brain built Mar 15 2025 18:00:27"
- "Starting downloaded MobileAsset brain (version: %@) built Mar 15 2025 18:00:27"
- "Successfully attached %@ with ID: %@"
- "Successfully committed MobileAssetBrain bundle %@ as current."
- "Successfully copied the Cryptex1 MobileAssetBrain PDI nonce."
- "Successfully ejected cryptex disk image previously mounted at %@"
- "Successfully grafted %@ onto %@"
- "Successfully mounted cryptex volume %@ at %@"
- "Successfully personalized 2nd brain ticket with current-boot-only PDI nonce"
- "Successfully pre-rolled the Cryptex1 MobileAssetBrain nonce."
- "Successfully registered Exclave mapped path [fstag=%d] %@:%@: %s"
- "Successfully removed item %@"
- "Successfully removed old MobileAssetBrain installation directory"
- "Successfully rolled the Cryptex1 MobileAssetBrain nonce"
- "Successfully scheduled %@"
- "Successfully ungrafted %@ from the file system using %@"
- "Successfully unmounted cryptex volume %@ from %@"
- "Successfully wrote %@ (using NSData)."
- "Successfully wrote %@."
- "The current AssetType(%@) is in the list of those configured to fail personalization but the current specifier(%@) is not"
- "The current specifier(%@) of AssetType %@ is configured to fail personalization"
- "Unable to set SSO token for user authlisting"
- "Unable to set secure TSS URL for user authlisting"
- "Unable to set signing server retry count | AMAuthInstallSetSigningServerRetry() failed with error %d (%@)"
- "Unregistering dissenter for volume: %@"
- "User-authlisting enabled."
- "Using GRAFTDMG_CRYPTEX_BOOT"
- "Using GRAFTDMG_CRYPTEX_PDI_NONCE"
- "Using overridden value for signing server"
- "VendingLatest"
- "WARNING: Failed to eject %@ after mount failure: %@"
- "WARNING: Using software coprocessor parameters override:\n%@"
- "Waiting for AuthenticationServices completed."
- "Waiting for AuthenticationServices response..."
- "Warning: MASecureManifestStorage does not support staging, commit is a no-op"
- "Warning: MASecureManifestStorage does not support staging, returning nil"
- "Warning: MASecureManifestStorage does not support staging, storing manifest instead"
- "[%{public}@] {removeCurrentJob} %{public}@"
- "[CONTROL_MANAGER_CACHEDELETE_QUEUE] {respondToCacheDelete} performing cache-delete triggered operation..."
- "[MORE_CLIENT_REQUESTS] {%{public}@:removeCurrentJob} auto-asset-job indicated removal but has more to do | eventInfo:%{public}@"
- "[Personalization] enqueue %@"
- "[Personalization] finish %@ (success = %i, error = %@)"
- "[Personalization] start %@"
- "[SecureMAHelper]: Creating new graft list for tracking grafted assets"
- "[SecureMAHelper]: Failed to create folder(%@) for grafted list file: %@"
- "[SecureMAHelper]: Failed to delete graft list file at %@ : %@"
- "[SecureMAHelper]: Failed to delete graft list file at path %@. Error: %@"
- "[SecureMAHelper]: Failed to load existing graft list at path %@. Error: %@"
- "[SecureMAHelper]: Failed to record %@ entry for asset of type %@ to file %@: %@"
- "[SecureMAHelper]: Graft list does not exist at %@"
- "[SecureMAHelper]: Successfully created folder(%@) for grafted list file"
- "[SecureMAHelper]: Successfully recorded graft entry for asset of type %@"
- "_scheduleSelector:triggeringAtIntervalSecs:withRemainingSecs:forPushedJob:forSetJob:withSetPolicy:triggeringIfLearned:resettingRemaining:"
- "d\x1f\x0f\a\x16<+\x14"
- "handleSuspendForSoftwareUpdateRequest-spaceCheck"
- "handleSuspendForSoftwareUpdateRequest-suspendComplete"
- "mobileassetd needs to relaunch at next unlock"
- "trackShortTermLockedSetDescriptor:forSpecificAtomicInstance:"
- "v64@0:8@16q24q32B40B44@48B56B60"
- "{%@} set-job decrementing client request count when not an activeSetJob and not a cancelingSetJob | eventInfo:%@"
- "{%{public}@}\n[BECAME-LATEST-TO-VEND] adopted set-descriptor as latest-to-vend | setDescriptor:%{public}@"
- "{%{public}@}: %@ adopt as latest. jobAtomicInstance: %@"

```
