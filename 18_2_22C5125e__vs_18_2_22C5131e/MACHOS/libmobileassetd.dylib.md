## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1329.60.100.502.2
-  __TEXT.__text: 0x2628f4
+1329.60.108.0.0
+  __TEXT.__text: 0x263d24
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_stubs: 0x1fc20
-  __TEXT.__objc_methlist: 0xf010
-  __TEXT.__const: 0x495e
-  __TEXT.__objc_methname: 0x374f8
-  __TEXT.__cstring: 0x4cfcc
+  __TEXT.__objc_stubs: 0x1fd20
+  __TEXT.__objc_methlist: 0xf088
+  __TEXT.__const: 0x494e
+  __TEXT.__objc_methname: 0x37894
+  __TEXT.__cstring: 0x4d42c
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x3588
-  __TEXT.__oslogstring: 0x310d5
+  __TEXT.__objc_methtype: 0x35a2
+  __TEXT.__oslogstring: 0x31303
   __TEXT.__gcc_except_tab: 0x2558
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4

   __DATA_CONST.__auth_got: 0x11d8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6720
-  __DATA_CONST.__cfstring: 0x31aa0
+  __DATA_CONST.__const: 0x6700
+  __DATA_CONST.__cfstring: 0x31c00
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8bb0
+  __DATA_CONST.__objc_selrefs: 0x8c00
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x998
   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x14558
-  __DATA.__objc_classrefs: 0x7a8
+  __DATA.__objc_const: 0x145e8
+  __DATA.__objc_classrefs: 0x7b0
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x1284
+  __DATA.__objc_ivar: 0x1290
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
-  __DATA.__bss: 0x53c0
+  __DATA.__bss: 0x53b0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x1978
   __DATA_DIRTY.__bss: 0x340

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8304
-  Symbols:   14908
-  CStrings:  15831
+  Functions: 8318
+  Symbols:   14928
+  CStrings:  15865
 
Symbols:
+ +[MADAutoAssetControlManager copyCurrentDownloadedDescriptors:unlockedUnreferencedDescriptors:unlockedReferencedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:]
+ +[MADAutoAssetControlManager garbageCollectionOperationComplete:originalUnlockedUnreferencedDescriptors:originalUnlockedReferencedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:]
+ -[ControlManager setUnlockedReferencedDescriptors:]
+ -[ControlManager setUnlockedUnreferencedDescriptors:]
+ -[ControlManager unlockedReferencedDescriptors]
+ -[ControlManager unlockedUnreferencedDescriptors]
+ -[DownloadManager triggerVPN]
+ -[MADAnalyticsCacheDeleteResults initWithReclaimV2AssetSpace:reclaimV2AssetCount:reclaimUnlockedUnreferencedAutoAssetSpace:reclaimUnlockedUnreferencedAutoAssetCount:reclaimUnlockedReferencedAutoAssetSpace:reclaimUnlockedReferencedAutoAssetCount:reclaimLockedOverridableAutoAssetSpace:reclaimLockedOverridableAutoAssetCount:reclaimLockedNeverRemoveAutoAssetSpace:reclaimLockedNeverRemoveAutoAssetCount:reclaimStagedAutoAssetSpace:reclaimStagedAutoAssetCount:reclaimMetadataBlockedSpace:reclaimMetadataBlockedCount:]
+ -[MADAnalyticsCacheDeleteResults reclaimUnlockedReferencedAutoAssetCount]
+ -[MADAnalyticsCacheDeleteResults reclaimUnlockedReferencedAutoAssetSpace]
+ -[MADAnalyticsCacheDeleteResults reclaimUnlockedUnreferencedAutoAssetCount]
+ -[MADAnalyticsCacheDeleteResults reclaimUnlockedUnreferencedAutoAssetSpace]
+ -[MADAnalyticsCacheDeleteResults setReclaimUnlockedReferencedAutoAssetCount:]
+ -[MADAnalyticsCacheDeleteResults setReclaimUnlockedReferencedAutoAssetSpace:]
+ -[MADAnalyticsCacheDeleteResults setReclaimUnlockedUnreferencedAutoAssetCount:]
+ -[MADAnalyticsCacheDeleteResults setReclaimUnlockedUnreferencedAutoAssetSpace:]
+ -[MADAutoAssetControlManager action_ResumeJobs:error:].cold.2
+ -[MADAutoAssetControlManager action_ResumeJobs:error:].cold.3
+ -[MADAutoAssetControlManager doesSelectorArray:coverAssetDescriptor:]
+ -[MADAutoAssetControlManager doesSetConfiguration:coverAssetDescriptor:]
+ -[MADAutoAssetControlManager schedulerReferencesDescriptor:]
+ -[MADAutoAssetControlManager setConfigurationReferencesDescriptor:]
+ -[MADAutoAssetControlManager setConfigurationReferencesDescriptor:].cold.1
+ GCC_except_table542
+ GCC_except_table547
+ GCC_except_table549
+ GCC_except_table563
+ GCC_except_table63
+ GCC_except_table67
+ OBJC_IVAR_$_ControlManager._unlockedReferencedDescriptors
+ OBJC_IVAR_$_ControlManager._unlockedUnreferencedDescriptors
+ OBJC_IVAR_$_MADAnalyticsCacheDeleteResults._reclaimUnlockedReferencedAutoAssetCount
+ OBJC_IVAR_$_MADAnalyticsCacheDeleteResults._reclaimUnlockedReferencedAutoAssetSpace
+ OBJC_IVAR_$_MADAnalyticsCacheDeleteResults._reclaimUnlockedUnreferencedAutoAssetCount
+ OBJC_IVAR_$_MADAnalyticsCacheDeleteResults._reclaimUnlockedUnreferencedAutoAssetSpace
+ _OBJC_CLASS_$_NSCache
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2270
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2271
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2271.cold.1
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2845
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2846
+ ___201+[MADAutoAssetControlManager copyCurrentDownloadedDescriptors:unlockedUnreferencedDescriptors:unlockedReferencedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:]_block_invoke
+ ___271+[MADAutoAssetControlManager garbageCollectionOperationComplete:originalUnlockedUnreferencedDescriptors:originalUnlockedReferencedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:]_block_invoke
+ ___29-[DownloadManager triggerVPN]_block_invoke
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8
+ __block_literal_global.2261
+ __block_literal_global.2310
+ __block_literal_global.2843
+ __block_literal_global.2861
+ __block_literal_global.3180
+ __block_literal_global.3250
+ __block_literal_global.3252
+ __block_literal_global.3370
+ __block_literal_global.3427
+ __block_literal_global.4158
+ __block_literal_global.962
+ _objc_msgSend$brainVersion
+ _objc_msgSend$copyCurrentDownloadedDescriptors:unlockedUnreferencedDescriptors:unlockedReferencedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:
+ _objc_msgSend$garbageCollectionOperationComplete:originalUnlockedUnreferencedDescriptors:originalUnlockedReferencedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:
+ _objc_msgSend$initWithReclaimV2AssetSpace:reclaimV2AssetCount:reclaimUnlockedUnreferencedAutoAssetSpace:reclaimUnlockedUnreferencedAutoAssetCount:reclaimUnlockedReferencedAutoAssetSpace:reclaimUnlockedReferencedAutoAssetCount:reclaimLockedOverridableAutoAssetSpace:reclaimLockedOverridableAutoAssetCount:reclaimLockedNeverRemoveAutoAssetSpace:reclaimLockedNeverRemoveAutoAssetCount:reclaimStagedAutoAssetSpace:reclaimStagedAutoAssetCount:reclaimMetadataBlockedSpace:reclaimMetadataBlockedCount:
+ _objc_msgSend$reclaimUnlockedReferencedAutoAssetCount
+ _objc_msgSend$reclaimUnlockedReferencedAutoAssetSpace
+ _objc_msgSend$reclaimUnlockedUnreferencedAutoAssetCount
+ _objc_msgSend$reclaimUnlockedUnreferencedAutoAssetSpace
+ _objc_msgSend$schedulerReferencesDescriptor:
+ _objc_msgSend$setConfigurationReferencesDescriptor:
+ _objc_msgSend$setReclaimUnlockedReferencedAutoAssetCount:
+ _objc_msgSend$setReclaimUnlockedReferencedAutoAssetSpace:
+ _objc_msgSend$setReclaimUnlockedUnreferencedAutoAssetCount:
+ _objc_msgSend$setReclaimUnlockedUnreferencedAutoAssetSpace:
+ _objc_msgSend$setUnlockedReferencedDescriptors:
+ _objc_msgSend$setUnlockedUnreferencedDescriptors:
+ _objc_msgSend$unlockedReferencedDescriptors
+ _objc_msgSend$unlockedUnreferencedDescriptors
- +[DownloadManager triggerVPN]
- +[MADAutoAssetControlManager copyCurrentDownloadedDescriptors:unlockedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:]
- +[MADAutoAssetControlManager garbageCollectionOperationComplete:originalUnlockedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:]
- -[ControlManager setUnlockedAutoAssetDescriptors:]
- -[ControlManager unlockedAutoAssetDescriptors]
- -[MADAnalyticsCacheDeleteResults initWithReclaimV2AssetSpace:reclaimV2AssetCount:reclaimUnlockedAutoAssetSpace:reclaimUnlockedAutoAssetCount:reclaimLockedOverridableAutoAssetSpace:reclaimLockedOverridableAutoAssetCount:reclaimLockedNeverRemoveAutoAssetSpace:reclaimLockedNeverRemoveAutoAssetCount:reclaimStagedAutoAssetSpace:reclaimStagedAutoAssetCount:reclaimMetadataBlockedSpace:reclaimMetadataBlockedCount:]
- -[MADAnalyticsCacheDeleteResults reclaimUnlockedAutoAssetCount]
- -[MADAnalyticsCacheDeleteResults reclaimUnlockedAutoAssetSpace]
- -[MADAnalyticsCacheDeleteResults setReclaimUnlockedAutoAssetCount:]
- -[MADAnalyticsCacheDeleteResults setReclaimUnlockedAutoAssetSpace:]
- GCC_except_table539
- GCC_except_table541
- GCC_except_table546
- GCC_except_table560
- OBJC_IVAR_$_ControlManager._unlockedAutoAssetDescriptors
- OBJC_IVAR_$_MADAnalyticsCacheDeleteResults._reclaimUnlockedAutoAssetCount
- OBJC_IVAR_$_MADAnalyticsCacheDeleteResults._reclaimUnlockedAutoAssetSpace
- __54-[MADAutoAssetControlManager action_ResumeJobs:error:]_block_invoke.cold.1
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2267
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2268
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2268.cold.1
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2839
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2840
- ___159+[MADAutoAssetControlManager copyCurrentDownloadedDescriptors:unlockedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:]_block_invoke
- ___221+[MADAutoAssetControlManager garbageCollectionOperationComplete:originalUnlockedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:]_block_invoke
- ___29+[DownloadManager triggerVPN]_block_invoke
- ___54-[MADAutoAssetControlManager action_ResumeJobs:error:]_block_invoke
- ___60+[MADAutoAssetSecure ungraft:forDescriptor:ungraftingError:]_block_invoke
- ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
- __block_literal_global.1561
- __block_literal_global.2242
- __block_literal_global.2291
- __block_literal_global.2824
- __block_literal_global.2842
- __block_literal_global.3161
- __block_literal_global.3231
- __block_literal_global.3233
- __block_literal_global.3365
- __block_literal_global.3424
- __block_literal_global.4152
- __block_literal_global.963
- _objc_msgSend$copyCurrentDownloadedDescriptors:unlockedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:
- _objc_msgSend$garbageCollectionOperationComplete:originalUnlockedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:
- _objc_msgSend$initWithReclaimV2AssetSpace:reclaimV2AssetCount:reclaimUnlockedAutoAssetSpace:reclaimUnlockedAutoAssetCount:reclaimLockedOverridableAutoAssetSpace:reclaimLockedOverridableAutoAssetCount:reclaimLockedNeverRemoveAutoAssetSpace:reclaimLockedNeverRemoveAutoAssetCount:reclaimStagedAutoAssetSpace:reclaimStagedAutoAssetCount:reclaimMetadataBlockedSpace:reclaimMetadataBlockedCount:
- _objc_msgSend$reclaimUnlockedAutoAssetCount
- _objc_msgSend$reclaimUnlockedAutoAssetSpace
- _objc_msgSend$secureOperationsFinished:forSetDescriptor:forAutoAssetDescriptors:
- _objc_msgSend$setReclaimUnlockedAutoAssetCount:
- _objc_msgSend$setReclaimUnlockedAutoAssetSpace:
- _objc_msgSend$setUnlockedAutoAssetDescriptors:
- _objc_msgSend$unlockedAutoAssetDescriptors
- action_ResumeJobs:error:.writeStartupActivatedCookieDispatchOnce
CStrings:
+ "'\x14G"
+ "(downloadedAutoAssets) unlocked[unreferenced]:%!l(MISSING)d(%!@(MISSING)), unlocked[referenced]:%!l(MISSING)d(%!@(MISSING)), lockedOverridable:%!l(MISSING)d(%!@(MISSING)), lockedNeverRemove:%!l(MISSING)d(%!@(MISSING)), staged:%!l(MISSING)d(%!@(MISSING))"
+ "(reclaimAssets) v2Assets:%!l(MISSING)d(%!@(MISSING)), unlocked[unreferenced]:%!l(MISSING)d(%!@(MISSING)), unlocked[referenced]:%!l(MISSING)d(%!@(MISSING)), lockedOverridable:%!l(MISSING)d(%!@(MISSING)), lockedNeverRemove:%!l(MISSING)d(%!@(MISSING)), staged:%!l(MISSING)d(%!@(MISSING)), metadataBlocked:%!l(MISSING)d(%!@(MISSING)) | totalAmount(%!@(MISSING)):%!@(MISSING)"
+ "-[DownloadManager triggerVPN]_block_invoke"
+ "/private/var/run/MobileAssetCritialDomainsUpdated.plist"
+ "2.2.22"
+ ">>>\n                      reclaimV2AssetSpace: %!l(MISSING)ld\n                      reclaimV2AssetCount: %!l(MISSING)d\nreclaimUnlockedUnreferencedAutoAssetSpace: %!l(MISSING)ld\nreclaimUnlockedUnreferencedAutoAssetCount: %!l(MISSING)d\n  reclaimUnlockedReferencedAutoAssetSpace: %!l(MISSING)ld\n  reclaimUnlockedReferencedAutoAssetCount: %!l(MISSING)d\n   reclaimLockedOverridableAutoAssetSpace: %!l(MISSING)ld\n   reclaimLockedOverridableAutoAssetCount: %!l(MISSING)d\n   reclaimLockedNeverRemoveAutoAssetSpace: %!l(MISSING)ld\n   reclaimLockedNeverRemoveAutoAssetCount: %!l(MISSING)d\n              reclaimStagedAutoAssetSpace: %!l(MISSING)ld\n              reclaimStagedAutoAssetCount: %!l(MISSING)d\n              reclaimMetadataBlockedSpace: %!l(MISSING)ld\n              reclaimMetadataBlockedCount: %!l(MISSING)d\n<<<]"
+ "@\"NSCache\""
+ "@128@0:8q16q24q32q40q48q56q64q72q80q88q96q104q112q120"
+ "Could not write back CriticalDomainsCookie file: %!@(MISSING)"
+ "Not updating CriticalDomains(already updated since boot)"
+ "STA_STARTUP_COOKIE_EXISTS  "
+ "STA_STARTUP_COOKIE_FAILURE "
+ "STA_STARTUP_COOKIE_SUCCESS "
+ "Starting built-in MobileAsset brain built Nov  4 2024 00:14:39"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Nov  4 2024 00:14:39"
+ "T@\"NSCache\",&,N,V_knownPersistedFiles"
+ "T@\"NSCache\",&,N,V_knownPersistedStates"
+ "T@\"NSDictionary\",&,N,V_unlockedReferencedDescriptors"
+ "T@\"NSDictionary\",&,N,V_unlockedUnreferencedDescriptors"
+ "Tq,N,V_reclaimUnlockedReferencedAutoAssetCount"
+ "Tq,N,V_reclaimUnlockedReferencedAutoAssetSpace"
+ "Tq,N,V_reclaimUnlockedUnreferencedAutoAssetCount"
+ "Tq,N,V_reclaimUnlockedUnreferencedAutoAssetSpace"
+ "Updating CriticalDomains(Brain version changed: Current: %!@(MISSING) previous: %!@(MISSING))"
+ "Updating CriticalDomains(first launch since boot)"
+ "Writing CriticalDomains cookie file : %!@(MISSING)"
+ "_reclaimUnlockedReferencedAutoAssetCount"
+ "_reclaimUnlockedReferencedAutoAssetSpace"
+ "_reclaimUnlockedUnreferencedAutoAssetCount"
+ "_reclaimUnlockedUnreferencedAutoAssetSpace"
+ "_unlockedReferencedDescriptors"
+ "_unlockedUnreferencedDescriptors"
+ "copyCurrentDownloadedDescriptors:unlockedUnreferencedDescriptors:unlockedReferencedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:"
+ "doesSelectorArray:coverAssetDescriptor:"
+ "doesSetConfiguration:coverAssetDescriptor:"
+ "failed post-write existence check after writing STARTUP_ACTIVATED cookie file (even though call to writeToURL was successful)"
+ "garbageCollectionOperationComplete:originalUnlockedUnreferencedDescriptors:originalUnlockedReferencedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:"
+ "initWithReclaimV2AssetSpace:reclaimV2AssetCount:reclaimUnlockedUnreferencedAutoAssetSpace:reclaimUnlockedUnreferencedAutoAssetCount:reclaimUnlockedReferencedAutoAssetSpace:reclaimUnlockedReferencedAutoAssetCount:reclaimLockedOverridableAutoAssetSpace:reclaimLockedOverridableAutoAssetCount:reclaimLockedNeverRemoveAutoAssetSpace:reclaimLockedNeverRemoveAutoAssetCount:reclaimStagedAutoAssetSpace:reclaimStagedAutoAssetCount:reclaimMetadataBlockedSpace:reclaimMetadataBlockedCount:"
+ "reclaimUnlockedReferencedAutoAssetCount"
+ "reclaimUnlockedReferencedAutoAssetSpace"
+ "reclaimUnlockedUnreferencedAutoAssetCount"
+ "reclaimUnlockedUnreferencedAutoAssetSpace"
+ "reclaimV2AssetSpace:%!l(MISSING)ld | reclaimV2AssetCount:%!l(MISSING)d | reclaimAutoAssetSpace:%!l(MISSING)ld | reclaimAutoAssetCount:%!l(MISSING)d | reclaimMetadataBlockedSpace:%!l(MISSING)ld | reclaimMetadataBlockedCount:%!l(MISSING)d"
+ "schedulerReferencesDescriptor:"
+ "setConfigurationReferencesDescriptor:"
+ "setReclaimUnlockedReferencedAutoAssetCount:"
+ "setReclaimUnlockedReferencedAutoAssetSpace:"
+ "setReclaimUnlockedUnreferencedAutoAssetCount:"
+ "setReclaimUnlockedUnreferencedAutoAssetSpace:"
+ "setUnlockedReferencedDescriptors:"
+ "setUnlockedUnreferencedDescriptors:"
+ "unlockedReferencedDescriptors"
+ "unlockedUnreferencedDescriptors"
+ "v60@0:8B16^@20^@28^@36^@44^@52"
+ "v76@0:8B16@20@28@36@44@52q60@68"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job matches latest-to-vend | setJobDescriptor:%!{(MISSING)public}@"
+ "{ResumeJobs} | Failed post-write existence check after writing STARTUP_ACTIVATED cookie file [%!{(MISSING)public}@] | stashError:%!@(MISSING)"
+ "{ResumeJobs} | Failed to write STARTUP_ACTIVATED cookie file [%!{(MISSING)public}@] | stashError:%!@(MISSING)"
+ "{setConfigurationReferencesDescriptor}"
+ "{setConfigurationReferencesDescriptor} unable to load secure-coded set-configuration | entryID:%!{(MISSING)public}@"
+ "{setConfigurationReferencesDescriptor} unable to load set descriptor for latest-to-vend | setConfiguration:%!{(MISSING)public}@"
+ "{setConfigurationReferencesDescriptor} unable to load set-configuration from persisted-state | entryID:%!{(MISSING)public}@"
- "%!@(MISSING) | reclaimUnlockedAutoAssetSpace:%!l(MISSING)ld | reclaimUnlockedAutoAssetCount:%!l(MISSING)d | reclaimLockedOverridableAutoAssetSpace:%!l(MISSING)ld | reclaimLockedOverridableAutoAssetCount:%!l(MISSING)d | reclaimLockedNeverRemoveAutoAssetSpace:%!l(MISSING)ld | reclaimLockedNeverRemoveAutoAssetCount:%!l(MISSING)d | reclaimMetadataBlockedSpace:%!l(MISSING)ld | reclaimMetadataBlockedCount:%!l(MISSING)d"
- "'\x14F"
- "(downloadedAutoAssets) unlocked:%!l(MISSING)d(%!@(MISSING)), lockedOverridable:%!l(MISSING)d(%!@(MISSING)), lockedNeverRemove:%!l(MISSING)d(%!@(MISSING)), staged:%!l(MISSING)d(%!@(MISSING))"
- "(reclaimAssets) v2Assets:%!l(MISSING)d(%!@(MISSING)), unlocked:%!l(MISSING)d(%!@(MISSING)), lockedOverridable:%!l(MISSING)d(%!@(MISSING)), lockedNeverRemove:%!l(MISSING)d(%!@(MISSING)), staged:%!l(MISSING)d(%!@(MISSING)), metadataBlocked:%!l(MISSING)d(%!@(MISSING)) | totalAmount(%!@(MISSING)):%!@(MISSING)"
- "2.2.21"
- "@112@0:8q16q24q32q40q48q56q64q72q80q88q96q104"
- "Starting built-in MobileAsset brain built Oct 28 2024 22:37:01"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct 28 2024 22:37:01"
- "T@\"NSDictionary\",&,N,V_unlockedAutoAssetDescriptors"
- "T@\"NSMutableDictionary\",&,N,V_knownPersistedFiles"
- "T@\"NSMutableDictionary\",&,N,V_knownPersistedStates"
- "Tq,N,V_reclaimUnlockedAutoAssetCount"
- "Tq,N,V_reclaimUnlockedAutoAssetSpace"
- "_reclaimUnlockedAutoAssetCount"
- "_reclaimUnlockedAutoAssetSpace"
- "_unlockedAutoAssetDescriptors"
- "copyCurrentDownloadedDescriptors:unlockedDescriptors:lockedOverridableDescriptors:lockedNeverRemoveDescriptors:stagedDescriptors:"
- "garbageCollectionOperationComplete:originalUnlockedDescriptors:originalLockedOverridableDescriptors:originalLockedNeverRemoveDescriptors:originalStagedDescriptors:totalReclaimedSpace:results:"
- "initWithReclaimV2AssetSpace:reclaimV2AssetCount:reclaimUnlockedAutoAssetSpace:reclaimUnlockedAutoAssetCount:reclaimLockedOverridableAutoAssetSpace:reclaimLockedOverridableAutoAssetCount:reclaimLockedNeverRemoveAutoAssetSpace:reclaimLockedNeverRemoveAutoAssetCount:reclaimStagedAutoAssetSpace:reclaimStagedAutoAssetCount:reclaimMetadataBlockedSpace:reclaimMetadataBlockedCount:"
- "reclaimUnlockedAutoAssetCount"
- "reclaimUnlockedAutoAssetSpace"
- "reclaimV2AssetSpace:%!l(MISSING)ld | reclaimV2AssetCount:%!l(MISSING)d | reclaimStagedAutoAssetSpace:%!l(MISSING)ld | reclaimStagedAutoAssetCount:%!l(MISSING)d"
- "setReclaimUnlockedAutoAssetCount:"
- "setReclaimUnlockedAutoAssetSpace:"
- "setUnlockedAutoAssetDescriptors:"
- "unlockedAutoAssetDescriptors"
- "v52@0:8B16^@20^@28^@36^@44"
- "v68@0:8B16@20@28@36@44q52@60"
- "{ResumeJobs} | Failed to write STARTUP_ACTIVATED cookie file [%!{(MISSING)public}@]| stashError:%!@(MISSING)"

```
