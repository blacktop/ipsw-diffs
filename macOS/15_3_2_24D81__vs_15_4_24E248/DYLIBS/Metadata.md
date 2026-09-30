## Metadata

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x71bbc
-  __TEXT.__auth_stubs: 0x2620
-  __TEXT.__objc_methlist: 0x4f4
-  __TEXT.__const: 0x52b8
+2333.22.13.7.0
+  __TEXT.__text: 0x72708
+  __TEXT.__auth_stubs: 0x2630
+  __TEXT.__objc_methlist: 0x50c
+  __TEXT.__const: 0x52a8
   __TEXT.__oslogstring: 0x18bd
-  __TEXT.__cstring: 0x92f9
-  __TEXT.__gcc_except_tab: 0x4b0
+  __TEXT.__cstring: 0x9466
+  __TEXT.__gcc_except_tab: 0x510
   __TEXT.__dof_MetadataF: 0x8b8
-  __TEXT.__unwind_info: 0x11f0
+  __TEXT.__unwind_info: 0x1370
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0xae
   __TEXT.__objc_methname: 0xbbb
   __TEXT.__objc_methtype: 0x830
   __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x3da8
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x3e28
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1320
-  __AUTH_CONST.__const: 0x36a8
-  __AUTH_CONST.__cfstring: 0x7260
-  __AUTH_CONST.__objc_const: 0x17d0
+  __AUTH_CONST.__auth_got: 0x1328
+  __AUTH_CONST.__const: 0x36c8
+  __AUTH_CONST.__cfstring: 0x73c0
+  __AUTH_CONST.__objc_const: 0x17b0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x14d0
-  __DATA.__bss: 0xcb8
-  __DATA.__common: 0x300cc
+  __DATA.__bss: 0xcc8
+  __DATA.__common: 0x300d0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0xca80
   __DATA_DIRTY.__bss: 0x928

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AFBB369-31F2-37B3-AE03-2EDB3E9AD439
-  Functions: 1837
-  Symbols:   4326
-  CStrings:  3148
+  UUID: 5BB3ABA7-BB4C-3DA7-A3FB-DF90D54AE6C7
+  Functions: 2054
+  Symbols:   4585
+  CStrings:  3169
 
Symbols:
+ +[_MDItem initialize].cold.1
+ +[__MDQuery initialize].cold.1
+ -[RecvList remove:].cold.1
+ -[_MDItemWithPath _cfTypeID].cold.1
+ -[_MDLabel _cfTypeID].cold.1
+ -[_MDLabel initWithUUID:attributes:forUserUUID:].cold.2
+ -[_MDLabelRegistry synchronize].cold.2
+ -[_MDServiceConnection _cfTypeID].cold.1
+ -[_MDServiceConnection connect].cold.2
+ -[_MDServiceConnection sendGreeting].cold.1
+ -[_MDServiceConnection unconnect:].cold.1
+ CopyAppleLanguages.cold.1
+ GCC_except_table114
+ GCC_except_table161
+ GCC_except_table244
+ MDBackupBegin.cold.3
+ MDBackupBegin.cold.4
+ MDBackupCancel.cold.2
+ MDBackupEnd.cold.3
+ MDBackupIndexFile.cold.3
+ MDBackupResume.cold.3
+ MDBackupResume.cold.4
+ MDCopySessionBegin.cold.3
+ MDCopySessionBegin.cold.4
+ MDCopySessionBegin.cold.5
+ MDCopySessionCancel.cold.2
+ MDCopySessionEnd.cold.3
+ MDExtendedAttributeBlockList.cold.1
+ MDExtendedAttributeBlockList.onceToken
+ MDExtendedAttributeBlockList.sBlockList
+ MDItemCopyAttribute.cold.1
+ MDItemCopyAttributeNames.cold.1
+ MDItemCopyAttributeNames.cold.2
+ MDItemCopyAttributes.cold.1
+ MDItemCopyAttributes.cold.2
+ MDItemCopyAttributes.cold.3
+ MDItemCreate.cold.3
+ MDItemCreate.cold.4
+ MDItemCreate.cold.5
+ MDItemCreate.cold.6
+ MDItemCreateForAbsolutePaths.cold.1
+ MDItemGetCacheFileDescriptors.cold.1
+ MDItemRemoveAttribute.cold.1
+ MDItemRemoveAttributes.cold.1
+ MDItemSetAttribute.cold.1
+ MDItemSetAttributes.cold.1
+ MDItemSetLocalizedAttribute.cold.1
+ MDItemWithPathGetTypeID.cold.1
+ MDItemsCreateWithURLs.cold.1
+ MDLabelGetTypeID.cold.1
+ MDQueryEnableUpdates.cold.3
+ MDQueryExecute.cold.10
+ MDQueryExecute.cold.11
+ MDQueryExecute.cold.12
+ MDQueryExecute.cold.13
+ MDQueryExecute.cold.14
+ MDQueryExecute.cold.15
+ MDQueryExecute.cold.16
+ MDQueryExecute.cold.17
+ MDQueryExecute.cold.18
+ MDQueryExecute.cold.19
+ MDQueryExecute.cold.20
+ MDQueryExecute.cold.21
+ MDQueryExecute.cold.22
+ MDQueryExecute.cold.23
+ MDQueryExecute.cold.24
+ MDQueryExecute.cold.25
+ MDQueryExecute.cold.26
+ MDQueryExecute.cold.27
+ MDQueryExecute.cold.28
+ MDQueryExecute.cold.29
+ MDQueryExecute.cold.30
+ MDQueryExecute.cold.31
+ MDQueryExecute.cold.4
+ MDQueryExecute.cold.5
+ MDQueryExecute.cold.6
+ MDQueryExecute.cold.7
+ MDQueryExecute.cold.8
+ MDQueryExecute.cold.9
+ MDServiceConnectionGetConnection.cold.1
+ MDServiceConnectionGetTypeID.cold.1
+ MDUnicodeConverterCreate.cold.1
+ MDUnicodeConverterGetTypeID.cold.1
+ _DeviceForStoreToken.cold.3
+ _DeviceForStoreToken.cold.4
+ _DeviceForStoreToken.cold.5
+ _MDAccessCopyClientPort.cold.2
+ _MDAccessCopyServerConnectionWithExit.cold.1
+ _MDAccessIsAllowed.cold.1
+ _MDBackupCatchup.cold.3
+ _MDBackupCatchup.cold.4
+ _MDConfigCopyImporterInformation.cold.2
+ _MDConfigCopyImporterUIDs.cold.2
+ _MDConfigCopyIndexingStorePaths.cold.2
+ _MDConfigCopyStoreAttributes.cold.2
+ _MDConfigCopyStoreInformation.cold.2
+ _MDConfigCopyStorePaths.cold.2
+ _MDConfigRegisterMountPoint.cold.2
+ _MDConfigRemoveStore.cold.2
+ _MDConfigSetStoreAttributes.cold.1
+ _MDConfigUnregisterMountPoint.cold.2
+ _MDCopyExclusionList.cold.2
+ _MDCopyLabelUserUUID.cold.2
+ _MDCopyPathSpotlightInternal.cold.1
+ _MDCopyVolumeFilter.cold.2
+ _MDExtendedAttributeBlockList
+ _MDFastPath.cold.1
+ _MDGetAllowedTaskCount.cold.1
+ _MDGetCurrentTaskCount.cold.1
+ _MDGetLastUsedDate.cold.1
+ _MDImportPrivateXattrsFromItems.cold.2
+ _MDIssueStoreCommand.cold.1
+ _MDItemAttributeAllowlisted.cold.1
+ _MDItemCopyAttributesBulkHelper.cold.1
+ _MDItemCopyAttributesBulkHelper.cold.2
+ _MDItemCopyAttributesBulkHelper.cold.3
+ _MDItemCopyCFURL_Interal.cold.1
+ _MDItemCopyStoreOIDArrayForPaths_Internal.cold.1
+ _MDItemCreate.cold.1
+ _MDItemCreateFSRef.cold.1
+ _MDItemDoMarkAs.cold.1
+ _MDItemGetTextSnippets.cold.1
+ _MDItemMarkAsUsedForPathAndTime.cold.4
+ _MDItemMarkAsUsedForPathAndTime.cold.5
+ _MDItemMarkAsUsedForPathAndTime.cold.6
+ _MDItemMarkAsUsedForPathAndTime.cold.7
+ _MDItemMarkAsUsedWithAbsoluteTime.cold.1
+ _MDItemMarkAsUsedWithAbsoluteTime.cold.2
+ _MDItemSetFinderColor.cold.3
+ _MDItemSetPrivateAttributes.cold.1
+ _MDItemWithPathCreate.cold.1
+ _MDItemsCreateWithFileIdsAndAbsolutePathsOnDevice.cold.1
+ _MDItemsWritePrivateXattrUpdatesWithKeysAndValuesAndFlags.cold.2
+ _MDItemsWritePublicXattrUpdatesWithKeysAndValues.cold.2
+ _MDMatchKeyCreate.cold.1
+ _MDOpenUserFile.cold.1
+ _MDPerfCopyStoreLifeCycleInfo.cold.2
+ _MDPerfSetAuditLevel.cold.2
+ _MDPerfWaitFileIndexingMarkerProcessed.cold.1
+ _MDPrepareForSnapshotTimeout.cold.1
+ _MDPrivateXattrUUIDsGetter.cold.1
+ _MDQueryCloseQuery.cold.1
+ _MDQueryCloseQuery.cold.2
+ _MDQueryCopyParams.cold.1
+ _MDQueryCopyParams.cold.2
+ _MDQueryCopyParams.cold.3
+ _MDQueryCopyRealPathsInArray.cold.1
+ _MDQueryCopyRealPathsInArray.cold.2
+ _MDQueryCreate_Internal.cold.1
+ _MDQueryCreate_Internal.cold.2
+ _MDQueryExecuteLocked.cold.2
+ _MDQueryExecuteLocked.cold.3
+ _MDQueryExecuteLocked.cold.4
+ _MDQueryExecuteLocked.cold.5
+ _MDQueryExecuteLocked.cold.6
+ _MDQueryGetAttributeValueOfResultAtIndexForGroup.cold.1
+ _MDQueryGetIndexAndGroupOfResultWithStoreAndOid.cold.3
+ _MDQueryGetIndexOfResultInRangeOfGroupWithStoreAndOid.cold.2
+ _MDQueryRestart.cold.1
+ _MDQuerySetGroupComparator.cold.7
+ _MDRegisterFileProviderPaths.cold.3
+ _MDRegisterFileProviderPaths.cold.4
+ _MDSetMailMessageAttributesAtTime.cold.2
+ _MDSetMailMessageAttributesAtTime.cold.3
+ _MDSetMailMessageAttributesAtTime.cold.4
+ _MDStringCompareLocalized.cold.1
+ _MDStringCopyCollationData.cold.1
+ _MDStringPrefixOfString.cold.1
+ _MDStringPrefixOfString.cold.2
+ _MDUpdateResultInQuery.cold.1
+ _MDValidateAttributeName.cold.1
+ _MDWaitForServerDeath.cold.1
+ _MDWriteCopyLabelUpdateData.cold.2
+ __31-[_MDServiceConnection connect]_block_invoke.43.cold.2
+ __MDItemCopyAttributesEllipsis1.cold.1
+ __MDQueryGetStringCollator.cold.1
+ __MDQuerySetAttributedUserQuery
+ __MDQuerySetClientBundleID
+ __MDQuerySetPommesRanking
+ __MDQuerySetQueryUnderstanding
+ __MDQuerySetTokenRewrites
+ __MDStoreOIDArrayIsMutable
+ __MergedGlobals
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8nn190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8nn190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8nn190102EPKcm
+ __ZNSt3__130__uninitialized_allocator_copyB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
+ __ZNSt3__130__uninitialized_allocator_copyB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIS6_NS4_IS6_EEEEEC2B8nn190102ERKSB_
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIS6_NS4_IS6_EEEEEC2B8nn190102ILb1ELi0EEERS7_RKSA_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8nn190102IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8nn190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC1B8nn190102ESt16initializer_listIS6_E
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ ___MDAccessCopyServerConnectionWithExit_block_invoke.9.cold.3
+ ___MDAccessCopyServerConnectionWithExit_block_invoke.9.cold.4
+ ___MDAccessCopyServerConnectionWithExit_block_invoke_2.cold.1
+ ___MDCreateCopyValueNoExt_block_invoke.cold.1
+ ___MDExtendedAttributeBlockList_block_invoke
+ ___MDQueryExecuteLocked_block_invoke.473.cold.10
+ ___MDQueryExecuteLocked_block_invoke.473.cold.11
+ ___MDQueryExecuteLocked_block_invoke.473.cold.12
+ ___MDQueryExecuteLocked_block_invoke.473.cold.13
+ ___MDQueryExecuteLocked_block_invoke.473.cold.14
+ ___MDQueryExecuteLocked_block_invoke.473.cold.15
+ ___MDQueryExecuteLocked_block_invoke.484.cold.6
+ ___MDQueryExecuteLocked_block_invoke.484.cold.7
+ ___MDQueryExecuteLocked_block_invoke.484.cold.8
+ ___MDQueryHandleConnection_block_invoke.533.cold.10
+ ___MDQueryHandleConnection_block_invoke.533.cold.11
+ ___MDQueryHandleConnection_block_invoke.533.cold.12
+ ___MDQueryHandleConnection_block_invoke.533.cold.13
+ ___MDQueryHandleConnection_block_invoke.533.cold.14
+ ___MDQueryHandleConnection_block_invoke.533.cold.15
+ ___MDQueryHandleConnection_block_invoke.533.cold.16
+ ___MDQueryHandleConnection_block_invoke.533.cold.17
+ ___MDQueryMakeClientPortLocked_block_invoke.508.cold.4
+ ___MDQueryMakeClientPortLocked_block_invoke.508.cold.5
+ ___MDQueryRestart_block_invoke_2.cold.5
+ ___MDQueryRestart_block_invoke_2.cold.6
+ ___pushAsyncNotification_block_invoke.cold.1
+ __block_descriptor_tmp.128
+ __block_descriptor_tmp.135
+ __block_descriptor_tmp.137
+ __block_descriptor_tmp.16
+ __block_descriptor_tmp.191
+ __block_descriptor_tmp.194
+ __block_descriptor_tmp.57
+ __block_literal_global.130
+ __block_literal_global.139
+ __block_literal_global.18
+ __ensureInitialized_block_invoke_4.cold.1
+ __getCurrentLocale_block_invoke.cold.1
+ __getCurrentLocale_block_invoke.cold.2
+ __get_proximities_block_invoke.186
+ __kMDAttributedUserQuery
+ __kMDQueryClientBundleID
+ __kMDQueryPommesRanking
+ __kMDQueryTokenRewrites
+ __kMDQueryUnderstanding
+ __md_create_expr_block_invoke.cold.1
+ __md_create_expr_block_invoke.cold.2
+ __md_create_expr_block_invoke.cold.3
+ __newAttr.cold.1
+ __newAttr.cold.2
+ __queryOIDArrayApplier_block_invoke.680.cold.1
+ __queryOIDArrayParallelApplier_block_invoke.671.cold.1
+ __query_node_expand_block_invoke.136
+ __receiveSync_block_invoke.146.cold.1
+ __receiveSync_block_invoke.cold.1
+ __receiveSync_block_invoke.cold.2
+ __receiveSync_block_invoke.cold.3
+ _bulkFetchUnpackerApplier.cold.2
+ _expandFunctions.cold.1
+ _postQueryNotification.cold.1
+ _query_init.cold.1
+ _setAttributesBulk.cold.1
+ _shouldShowExtensions.cold.1
+ _statfs_ext
+ copyExtendedAttributes.cold.1
+ copyTextShortcutsSet.cold.1
+ deferProcessUpdates.cold.1
+ ensureInitialized.cold.1
+ fetchAttributesForItems.cold.1
+ getPublicPort.cold.1
+ getPublicPort.cold.2
+ hybridSearch.cold.1
+ invalidatePublicPort.cold.1
+ invalidateServerPort.cold.2
+ itemAtIndexForGroup.cold.1
+ md_fsgetpath_ext.cold.1
+ mdwrite_send_message.cold.1
+ mdwrite_send_message.cold.2
+ multikey_qsortmain.cold.1
+ path_bundle_index.cold.1
+ processUpdatesLocked.cold.10
+ processUpdatesLocked.cold.11
+ processUpdatesLocked.cold.12
+ processUpdatesLocked.cold.13
+ processUpdatesLocked.cold.14
+ queryOIDArrayApplier.cold.1
+ queryOIDArrayApplier.cold.2
+ queryOIDArrayParallelApplier.cold.1
+ queryOIDArrayParallelApplier.cold.2
+ sendNotificationLocked.cold.1
+ sendNotificationLocked.cold.2
+ sendNotificationLocked.cold.3
+ sendNotificationLocked.cold.4
+ sendNotificationLocked.cold.5
+ si_calendar_retain.cold.1
+ writeTombsone.cold.1
+ writeTombsone.cold.2
- GCC_except_table113
- GCC_except_table156
- GCC_except_table239
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn180100EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn180100ERKS6_S9_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIS8_NS6_IS8_EEEEEEPvEENS_22__hash_node_destructorINS6_ISE_EEEEE5resetB8nn180100EPSE_
- __ZNSt3__112__destroy_atB8nn180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIS7_NS5_IS7_EEEEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn180100ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8nn180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8nn180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8nn180100EPKcm
- __ZNSt3__130__uninitialized_allocator_copyB8nn180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
- __ZNSt3__130__uninitialized_allocator_copyB8nn180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIS6_NS4_IS6_EEEEEC2B8nn180100ERKSB_
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIS6_NS4_IS6_EEEEEC2B8nn180100ILb1ELi0EEERS7_RKSA_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn180100Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8nn180100IPS6_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8nn180100Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC1B8nn180100ESt16initializer_listIS6_E
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- ___MDQueryGetPerThreadCache
- __block_descriptor_tmp.120
- __block_descriptor_tmp.127
- __block_descriptor_tmp.178
- __block_descriptor_tmp.180
- __block_descriptor_tmp.184
- __block_descriptor_tmp.188
- __block_descriptor_tmp.56
- __block_descriptor_tmp.60
- __block_literal_global.190
- __block_literal_global.58
- __get_proximities_block_invoke.179
- __query_node_expand_block_invoke.128
- _fmod
- _utf8_encodelen
- si_calendar_retain.once
- si_calendar_retain.s_gmt_tz
- si_calendar_retain.s_local_tz
CStrings:
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDIndexing.c"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDItem.c"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDLabel.c"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDQuery.c"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDServiceConnection.c"
+ "_MDQueryGetAttributeValueOfResultAtIndexForGroupLocked"
+ "_kMDAttributedUserQuery"
+ "_kMDItemMediaEmbeddingVersion"
+ "_kMDItemPrimaryTextEmbedding"
+ "_kMDItemTextChunkTokenLength"
+ "_kMDQueryClientBundleID"
+ "_kMDQueryPommesRanking"
+ "_kMDQueryTokenRewrites"
+ "_kMDQueryUnderstanding"
+ "itemAtIndexForGroup"
+ "kMDItemEmbeddingVersion"
+ "kMDItemKeyphraseLabels"
+ "kMDItemKeyphraseVersion"
+ "kMDItemTextContentLanguage"
- "**"
- ".."
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDIndexing.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDItem.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDLabel.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDQuery.c"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/framework/MDServiceConnection.c"
- "ja"
- "now"

```
