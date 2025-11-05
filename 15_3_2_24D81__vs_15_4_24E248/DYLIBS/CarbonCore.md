## CarbonCore

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/CarbonCore`

```diff

-1366.0.0.0.0
-  __TEXT.__text: 0xef034
-  __TEXT.__auth_stubs: 0x3580
-  __TEXT.__const: 0x1cdac8
-  __TEXT.__cstring: 0x2ac37
+1371.0.0.0.0
+  __TEXT.__text: 0xec0b8
+  __TEXT.__auth_stubs: 0x3570
+  __TEXT.__objc_methlist: 0x68
+  __TEXT.__const: 0x1cdd08
+  __TEXT.__cstring: 0x2ac30
   __TEXT.__oslogstring: 0x5fd5
-  __TEXT.__gcc_except_tab: 0xbb8
-  __TEXT.__unwind_info: 0x2e18
+  __TEXT.__gcc_except_tab: 0x858
+  __TEXT.__unwind_info: 0x2e58
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methname: 0x173
   __TEXT.__objc_methtype: 0x160
   __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__got: 0x348
   __DATA_CONST.__const: 0x152f0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1ad0
+  __AUTH_CONST.__auth_got: 0x1ac8
   __AUTH_CONST.__const: 0x3ad8
   __AUTH_CONST.__cfstring: 0x4f80
-  __AUTH_CONST.__objc_const: 0x108
+  __AUTH_CONST.__objc_const: 0x40
   __AUTH.__data: 0x100
   __DATA.__data: 0x1550
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x348
-  __DATA.__bss: 0x5420
+  __DATA.__bss: 0x5528
   __DATA_DIRTY.__data: 0x7c8
-  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libfakelink.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F74B7C7-7D08-3067-A12E-DD1873D04A2B
-  Functions: 4566
-  Symbols:   7134
-  CStrings:  7335
+  UUID: FB115C6D-9649-3D61-AE71-C7548B808951
+  Functions: 4955
+  Symbols:   7612
+  CStrings:  7333
 
Symbols:
+ ALI_GetHomeDirPath.cold.1
+ AL_copyVolumeAliasForDiskImage.cold.1
+ AL_findByAbsPath.cold.1
+ CCFDisposeComponent.cold.1
+ CSBackupSetItemExcluded.cold.1
+ CSSharedUniverseSegmentMapper.cold.1
+ DeclineVolumeNotification.cold.1
+ DeclineVolumeNotificationWithFlags.cold.1
+ DetachResourceCommon.cold.1
+ DoAsyncFileRequest.cold.1
+ FIDCopyFileIDMapForVolume.cold.1
+ FIDCopyFileIDMapForVolume.cold.2
+ FIDNodeIDFFromFileID.cold.1
+ FSMountGetVolumeUUID.cold.1
+ FSNodeServer_SyncWithSystemUniverseInternal.cold.1
+ FSNode_FillIOKitProperties.cold.1
+ FSReservationUpdate.cold.1
+ FileIDTreePrintNodeTreeInternal.cold.1
+ FileIDTreeServer_FSObjectChangedHook.cold.1
+ FileIDTreeServer_UpdateLatestFModWatchSeed.cold.1
+ FileIDTree_DumpFModWatchSeeds.cold.1
+ FileIDTree_InvalidateChildrenIDs.cold.1
+ FindFolderGuts.cold.1
+ GCC_except_table107
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table21
+ GCC_except_table25
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table89
+ GCC_except_table9
+ GCC_except_table98
+ GetFakelinkDataVolumeMountPoint.cold.1
+ GetFakelinkSystemVolumeMountPoint.cold.1
+ GetFromFolderCache.cold.1
+ GetFromFolderCache.cold.2
+ GetIntlXResource.cold.1
+ GetThreadGlobals.cold.1
+ GetThreadGlobals.cold.2
+ GetThreadGlobals.cold.3
+ INIT_Folders.cold.1
+ InsertOverrideMapCommon.cold.1
+ InsertOverrideMapCommon.cold.2
+ InvalidateFolderDescriptorCacheInternal.cold.1
+ InvalidateFolderDescriptorCacheInternal.cold.2
+ InvalidateFolderDescriptorCacheInternal.cold.3
+ InvalidateFolderDescriptorCacheInternal.cold.4
+ InvalidateFolderDescriptorCacheInternal.cold.5
+ InvalidateFolderDescriptorCacheInternal.cold.6
+ InvalidateFolderTypeInCache.cold.1
+ InvalidateFolderTypeInCache.cold.2
+ InvalidateFolderTypeInCache.cold.3
+ InvalidateFolderTypeInCache.cold.4
+ IsHomeOrLocal.cold.1
+ IsPairedBootVolume.cold.1
+ IsTransactionCompletedButNotVerified.cold.1
+ MPCreateTask.cold.1
+ RMAddResFileToSearchPath.cold.1
+ RMRemoveResFileFromSearchPath.cold.1
+ RegisterForVolumeMountNotifications.cold.1
+ ReleaseResourceCommon.cold.1
+ RequestVolumeNotification.cold.1
+ RequestVolumeNotificationWithFlags.cold.1
+ SCSessionUniverseGetCachedPort.cold.1
+ SCSharedUniverseDestructor.cold.1
+ SaveToFolderCache.cold.1
+ SaveToFolderCache.cold.2
+ SaveToFolderCache.cold.3
+ SaveToFolderCache.cold.4
+ SetThreadGlobalsAreCooperative.cold.1
+ TSCreateThreadCommon.cold.1
+ UTCDateTimeDescription.cold.1
+ _BackupItemXAttrsMatch
+ _CSBackupCopyDestinationMountPointURL.cold.1
+ _CSBackupCopySessionStatus.cold.1
+ _CSBackupDebugLoggingEnabled.cold.1
+ _CSBackupGetSharedServerProxy.cold.1
+ _CSBackupGetSharedStatusProxy.cold.1
+ _CSBackupServerIsActive.cold.1
+ _CSBackupServerProxyCopyMountPointForDestination.cold.1
+ _CSBackupServerSendAdvisoryMessageForPath.cold.1
+ _CSCheckFix.cold.1
+ _CSCheckFix.cold.2
+ _CSCheckFix.cold.3
+ _CSCheckFixWithInfo.cold.1
+ _CSCopyNamedData.cold.1
+ _CSFlushNamedData.cold.1
+ _CSFlushNamedData.cold.2
+ _CSGetNamedData.cold.1
+ _CSGetProcessorArchitecture.cold.1
+ _CSSetNamedData.cold.1
+ _CSSetNamedData.cold.2
+ _FSAddVolumeObserver.cold.1
+ _FSAddVolumeObserverOnQueue.cold.1
+ _FSRemoveVolumeObserver.cold.1
+ _FSRemoveVolumeObserverOnQueue.cold.1
+ _FileIDTreeGetSKServiceDescription.cold.1
+ _GetCachedItlbValue
+ _GetScriptName
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SCDestroyUniverse.cold.1
+ _SCMapSharedSegment.cold.1
+ _SCSessionUniverseByUIDAcquireAndLock.cold.2
+ _SCSessionUniverseByUIDAcquireAndLock.cold.3
+ _SCUniverseAllocateAndInitSegment.cold.1
+ _SCUniverseAllocateEntry.cold.2
+ _SCUniverseAllocateEntry.cold.3
+ _SCUniverseFreeEntry.cold.1
+ _SCUniverseGetEntryAddress.cold.1
+ _SafelyCopyHFSUniStr255
+ _ScriptKeysKindHandler
+ _TSGetMainThread.cold.1
+ _Z10FSMakePathsjPKcjPc.cold.1
+ _Z14FSRefGetNodeIDPK5FSRef.cold.1
+ _Z19FSRefGetParentDirIDPK5FSRef.cold.1
+ _Z19_FileIDMapGetTypeIDv.cold.1
+ _Z20_FSGetDiskArbSessionPP11__DASessionS1_.cold.1
+ _Z21CalculateNewEndOfForkP10FileRecordsxyPy.cold.1
+ _Z21GetMacFilePermissionsjjt.cold.1
+ _Z21UnpackAttributeBufferPK8attrlistPKvP15FSAttributeInfoP18FSVolAttributeInfoPhPjS9_hhhPP4_aclPA16_hSE_.cold.2
+ _Z22VolFSCreatePathFromIDsP7FSMountjPKcjhPc.cold.1
+ _Z22getDataVolumeMountPathv.cold.1
+ _Z9BasicReadP10FileRecordsxPyPvS1_.cold.1
+ _ZL14showCheckFixesv.cold.1
+ _ZL17_CLV_GetCacheablev.cold.1
+ _ZL18_NodeIDFFromFileIDP10_FileIDMapy.cold.1
+ _ZL18_NodeIDFFromFileIDP10_FileIDMapy.cold.2
+ _ZL18getCorrectedDevicej.cold.1
+ _ZL20sVolumeObserverBlock_block_invoke.cold.1
+ _ZL20sVolumeObserverBlock_block_invoke.cold.2
+ _ZL20sVolumeObserverBlock_block_invoke.cold.3
+ _ZL24GetComponentCacheableRefv.cold.1
+ _ZL25GetFSReservationCacheablev.cold.1
+ _ZL28_FN_CreateNotificationObjectPK5FSRef.cold.1
+ _ZL7msgNamei.cold.1
+ _ZN15SCClientSession17checkinWithServerEPj.cold.1
+ _ZN15SCClientSession17checkinWithServerEPj.cold.2
+ _ZN15SCServerSession11noteTaskAddEij.cold.1
+ _ZN15SCServerSession12noteTaskGoneEij.cold.1
+ _ZN15SCServerSession13deleteSessionEv.cold.1
+ _ZN15SCServerSession13forgetSessionEv.cold.1
+ _ZN15SCServerSession17dispatch_mach_msgEP19dispatch_mach_msg_s.cold.1
+ _ZN15SCServerSession23coreServicesClientQueueEv.cold.1
+ _ZN15SCServerSessionC2Ejj.cold.1
+ _ZN15SCServerSessionD2Ev.cold.1
+ _ZN19CSSeedBuiltOnNotify13existingSeedsEb.cold.1
+ _ZN19CSSeedBuiltOnNotify4findEPKcjb.cold.1
+ _ZN19CSSeedBuiltOnNotify4findEPKcjb.cold.2
+ _ZN19CSSeedBuiltOnNotify4findEPKcjb.cold.3
+ __CSBackupRuleTreeEvaluateFolderRules
+ __MergedGlobals
+ __ZL18HexStringToIntegerjPKh
+ __ZNKSt3__16vectorI10FixUpEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI11PrefsBucketNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP11SCCacheableNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP11TFSIteratorNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP9SCServiceNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP9SCSessionNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP9XMLActionNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113__tree_removeB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI10FixUpEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11PrefsBucketEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP11SCCacheableEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP11TFSIteratorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP9SCServiceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP9SCSessionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP9XMLActionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16__treeINS_12__value_typeIP15OpaqueCSSeedRefP19CSSeedBuiltOnNotifyEENS_19__map_value_compareIS3_S6_NS_4lessIS3_EELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS3_JNS_4pairIS3_S5_EEEEENSF_INS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIiPKcEENS_19__map_value_compareIiS4_NS_4lessIiEELb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIiJNS_4pairIiS3_EEEEENSD_INS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIijEENS_19__map_value_compareIiS2_NS_4lessIiEELb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIiJNS_4pairIijEEEEENSB_INS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___FileIDTreeGetSKServiceDescription_block_invoke.cold.1
+ ___TSGetMainThread_block_invoke.cold.2
+ ___TSGetMainThread_block_invoke.cold.3
+ ___Z21UnpackAttributeBufferPK8attrlistPKvP15FSAttributeInfoP18FSVolAttributeInfoPhPjS9_hhhPP4_aclPA16_hSE__block_invoke.cold.1
+ ___Z21UnpackAttributeBufferPK8attrlistPKvP15FSAttributeInfoP18FSVolAttributeInfoPhPjS9_hhhPP4_aclPA16_hSE__block_invoke.cold.2
+ ___Z22getDataVolumeMountPathv_block_invoke.cold.1
+ ___Z22getDataVolumeMountPathv_block_invoke.cold.2
+ ___Z22getDataVolumeMountPathv_block_invoke.cold.3
+ __callAnalyticsSendEventLazyFunc_block_invoke.cold.1
+ __fileMgrShowAllResults.cold.1
+ __fileMgrShowErrorResults.cold.1
+ __fileMgrShowParams.cold.1
+ __threadMgrVerbose.cold.1
+ aliasMgrLog.cold.1
+ callAnalyticsSendEventLazyFunc.cold.1
+ coreServicesDaemonLog.cold.1
+ csSeedLog.cold.1
+ deprecatedFunctionCallsLog.cold.1
+ fileIDTreeMgrLog.cold.1
+ fileMgrLog.cold.1
+ flippersLog.cold.1
+ folderMgrLog.cold.1
+ gestaltLog.cold.1
+ internationalFileCacheLog.cold.1
+ mpTasksLog.cold.1
+ namedDataLog.cold.1
+ pidOfFirstConnectionToCoreServicesd.cold.1
+ resourceMgrLog.cold.1
+ scGetProcessOptions.cold.1
+ scGetServerOptions.cold.1
+ sharedCacheLog.cold.1
+ threadMgrLog.cold.1
+ unicodeInputLog.cold.1
- ALI_GetHomeDirPath.gotIt
- ALI_GetHomeDirPath.homeDirPath
- FileIDTreeAddEnumerationCacheEntryInternal.cold.1
- FileIDTreeUpdateDirCacheInternal.cold.1
- GCC_except_table100
- GCC_except_table109
- GCC_except_table122
- GCC_except_table132
- GCC_except_table23
- GCC_except_table29
- GCC_except_table44
- GCC_except_table45
- GCC_except_table51
- GCC_except_table62
- GCC_except_table69
- GCC_except_table91
- ValidateScriptFontInfo.sFontArray
- ValidateScriptFontInfo.sGotFontFlagsAndArray
- ValidateScriptFontInfo.sScriptFontsValidated
- _MungerSetHandleSize
- _SCUniverseGetAmountOfEntriesForSegment.eEntriesForSegment
- _SCUniverseGetAmountOfEntriesForSegment.onceToken
- _SetCachedItlcValue
- _Z18GetVolFSAttributesP7FSMountjPKcjjP15FSAttributeInfojjP18FSVolAttributeInfoPh.cold.1
- _ZN11XMLKeyboardD2Ev.cold.1
- _ZN9SCSessionD2Ev.cold.1
- __SMgrGetUserDefaultEncoding.inited
- __SMgrGetUserDefaultEncoding.sRegion
- __SMgrGetUserDefaultEncoding.sScript
- __ZL11gHomeDirErr
- __ZL11gHomeDirRef
- __ZL16gHomeDirBasename
- __ZL16gHomeDirParentID
- __ZL17sVNDiskArbSession
- __ZL20gHomeDirIsVolumeRoot
- __ZL25sVNDiskArbApprovalSession
- __ZL29sDefaultDASessionElementArray
- __ZL33sDefaultDASessionScheduleListLock
- __ZNKSt3__16vectorI10FixUpEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI11PrefsBucketNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP11SCCacheableNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP11TFSIteratorNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP9SCServiceNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP9SCSessionNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP9XMLActionNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113__tree_removeB8nn180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI10FixUpEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI11PrefsBucketEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP11SCCacheableEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP11TFSIteratorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP9SCServiceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP9SCSessionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP9XMLActionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__127__tree_balance_after_insertB8nn180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16__treeINS_12__value_typeIP15OpaqueCSSeedRefP19CSSeedBuiltOnNotifyEENS_19__map_value_compareIS3_S6_NS_4lessIS3_EELb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS3_JRKNS_4pairIKS3_S5_EEEEENSF_INS_15__tree_iteratorIS6_PNS_11__tree_nodeIS6_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIiPKcEENS_19__map_value_compareIiS4_NS_4lessIiEELb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIiJRKNS_4pairIKiS3_EEEEENSD_INS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeINS_12__value_typeIijEENS_19__map_value_compareIiS2_NS_4lessIiEELb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIiJRKNS_4pairIKijEEEEENSB_INS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ18FSCopyURLForVolumeE21sHackForRadar53171328
- __ZZ18FSCopyURLForVolumeE9onceToken
- _fmod
- _gIntlCache
- _gIntlCacheInitialized
- _gIntlItlc
- _gIntlItlcSize
- _gKeyCacheInvalidated
- _gSwapKeyboardInited
- _gSwapKeyboardProc
- _gSysDirection
- _sFolderDescList
- _sFolderDescListCount
- _sGetScriptFontFlagsHook
- _sRoutingDescArray
- _sRoutingDescCount
- _sScriptFontValidatorHook
CStrings:
- "._"
- "en_"

```
