## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0xc23c8
-  __TEXT.__objc_methlist: 0x48fc
-  __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0x93d4
-  __TEXT.__gcc_except_tab: 0x4628
-  __TEXT.__oslogstring: 0xb6fb
-  __TEXT.__unwind_info: 0x2698
+2459.405.0.0.0
+  __TEXT.__text: 0xc7840
+  __TEXT.__objc_methlist: 0x4b4c
+  __TEXT.__const: 0x3e8
+  __TEXT.__cstring: 0x9822
+  __TEXT.__gcc_except_tab: 0x46f8
+  __TEXT.__oslogstring: 0xc063
+  __TEXT.__unwind_info: 0x2750
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__const: 0x618
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a88
+  __DATA_CONST.__objc_selrefs: 0x3be8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__got: 0xb70
-  __AUTH_CONST.__const: 0x56e8
-  __AUTH_CONST.__cfstring: 0x7ca0
-  __AUTH_CONST.__objc_const: 0x5df8
+  __DATA_CONST.__objc_arraydata: 0x2f0
+  __DATA_CONST.__got: 0xba8
+  __AUTH_CONST.__const: 0x57b8
+  __AUTH_CONST.__cfstring: 0x7d80
+  __AUTH_CONST.__objc_const: 0x60d8
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x348
+  __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1008
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4e4
+  __AUTH_CONST.__auth_got: 0x1050
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x520
   __DATA.__data: 0x3f8
-  __DATA.__bss: 0x140
+  __DATA.__bss: 0x1c0
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x158
-  __DATA_DIRTY.__bss: 0x5c0
+  __DATA_DIRTY.__bss: 0x5b8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3319
-  Symbols:   6706
-  CStrings:  2514
+  Functions: 3389
+  Symbols:   6868
+  CStrings:  2573
 
Symbols:
+ -[CSSearchAgent _issueDrainIfRequestedForQueryContext:searchConnection:qos:]
+ -[CSSearchAgent _validatedDrainBundleIDsForQueryContext:searchConnection:]
+ -[MDSearchableIndexService performDrainWithToken:]
+ -[MDSearchableIndexService processDrainResponse:]
+ -[MDSearchableIndexService sp_buildDrainDictionaryForToken:]
+ -[SDConnectionConfiguration allowQueryDrainTrigger]
+ -[SDConnectionConfiguration shouldLogQueryDrainTriggerRejection]
+ -[SDProvenanceResult .cxx_destruct]
+ -[SDProvenanceResult provenance]
+ -[SDProvenanceResult setProvenance:]
+ -[SDProvenanceResult setTeamIdentifier:]
+ -[SDProvenanceResult teamIdentifier]
+ -[SPConcreteCoreSpotlightIndexer _indexUnavailableErrorCodeForFailedOpen]
+ -[SPConcreteCoreSpotlightIndexer _test_setSuspended:]
+ -[SPConcreteCoreSpotlightIndexer evaluateDrainRateLimitForBundleIDs:clientBundleID:]
+ -[SPConcreteCoreSpotlightIndexer issueDrainForBundleID:token:]
+ -[SPConcreteCoreSpotlightIndexer sp_decrementDonorIdentityTokenSlotCountForBundleID:count:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_drainCallerIdentitySlotForBundleID:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_drainDonorIdentitySlotForBundleID:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_drainTokenSweepQueueForTesting]
+ -[SPConcreteCoreSpotlightIndexer sp_drainTokenSweepTimerIsSuspendedForTesting]
+ -[SPConcreteCoreSpotlightIndexer sp_effectiveOccupiedDrainTokenTTLSeconds]
+ -[SPConcreteCoreSpotlightIndexer sp_effectiveQuarantinedDrainTokenTTLSeconds]
+ -[SPConcreteCoreSpotlightIndexer sp_evaluateDrainRateLimitForBundleIDs:clientBundleID:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_evictAllDrainTokensForBundleID:protectionClass:]
+ -[SPConcreteCoreSpotlightIndexer sp_evictAllDrainTokensForBundleID:protectionClass:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_evictDrainTokenAtIndex:expectedToken:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_issueDrainForBundleID:token:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_reconcileDrainTokenSweepTimerSuspension]
+ -[SPConcreteCoreSpotlightIndexer sp_recordedBundleIDForDrainToken:]
+ -[SPConcreteCoreSpotlightIndexer sp_recordedDrainTokenSnapshotForToken:]
+ -[SPConcreteCoreSpotlightIndexer sp_removeDrainTokenEntry:expectingBundleID:]
+ -[SPConcreteCoreSpotlightIndexer sp_removeDrainTokenEntry:expectingBundleID:now:]
+ -[SPConcreteCoreSpotlightIndexer sp_sendDrainToken:toBundleID:]
+ -[SPConcreteCoreSpotlightIndexer sp_startDrainTokenSweepTimer]
+ -[SPConcreteCoreSpotlightIndexer sp_sweepExpiredDrainTokens:]
+ -[SPConcreteCoreSpotlightIndexer sp_tokenAtIndexForTesting:]
+ -[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]
+ -[SPCoreSpotlightIndexer evaluateDrainRateLimitForBundleIDs:clientBundleID:]
+ -[SPCoreSpotlightIndexer evictPendingDrainTokensForBundleID:]
+ -[SPCoreSpotlightIndexer issueDrainForBundleID:token:]
+ -[SPCoreSpotlightIndexer recordedBundleIDForDrainToken:]
+ -[SPCoreSpotlightIndexer removeDrainTokenEntry:bundleID:]
+ GCC_except_table1007
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1046
+ GCC_except_table1062
+ GCC_except_table1063
+ GCC_except_table1111
+ GCC_except_table1116
+ GCC_except_table1180
+ GCC_except_table1221
+ GCC_except_table1227
+ GCC_except_table1228
+ GCC_except_table1235
+ GCC_except_table1236
+ GCC_except_table1246
+ GCC_except_table1248
+ GCC_except_table1266
+ GCC_except_table1272
+ GCC_except_table1276
+ GCC_except_table1307
+ GCC_except_table1314
+ GCC_except_table1321
+ GCC_except_table1328
+ GCC_except_table1335
+ GCC_except_table1353
+ GCC_except_table1428
+ GCC_except_table1429
+ GCC_except_table1431
+ GCC_except_table1438
+ GCC_except_table1498
+ GCC_except_table1505
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table211
+ GCC_except_table234
+ GCC_except_table248
+ GCC_except_table255
+ GCC_except_table268
+ GCC_except_table284
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table296
+ GCC_except_table297
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table343
+ GCC_except_table357
+ GCC_except_table365
+ GCC_except_table371
+ GCC_except_table377
+ GCC_except_table405
+ GCC_except_table415
+ GCC_except_table430
+ GCC_except_table465
+ GCC_except_table470
+ GCC_except_table496
+ GCC_except_table525
+ GCC_except_table546
+ GCC_except_table547
+ GCC_except_table575
+ GCC_except_table602
+ GCC_except_table615
+ GCC_except_table618
+ GCC_except_table671
+ GCC_except_table685
+ GCC_except_table696
+ GCC_except_table722
+ GCC_except_table728
+ GCC_except_table743
+ GCC_except_table744
+ GCC_except_table756
+ GCC_except_table785
+ GCC_except_table811
+ GCC_except_table812
+ GCC_except_table813
+ GCC_except_table839
+ GCC_except_table905
+ GCC_except_table926
+ GCC_except_table947
+ GCC_except_table951
+ GCC_except_table955
+ GCC_except_table984
+ OBJC_IVAR_$_SDConnectionConfiguration._allowQueryDrainTrigger
+ OBJC_IVAR_$_SDConnectionConfiguration._queryDrainTriggerRejectionLogged
+ OBJC_IVAR_$_SDProvenanceResult._provenance
+ OBJC_IVAR_$_SDProvenanceResult._teamIdentifier
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._checkedInClientsLock
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainCallerIdentityEntries
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainCallerIdentityLock
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainDonorIdentityEntries
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainDonorIdentityLock
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenEntries
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenLiveCount
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenLock
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenSweepQueue
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenSweepTimer
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenSweepTimerSuspended
+ _CFURLCreateFromFileSystemRepresentation
+ _LSCopyApplicationURLsForBundleIdentifier
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_PKManager
+ _OBJC_CLASS_$_SDProvenanceResult
+ _OBJC_METACLASS_$_SDProvenanceResult
+ _OUTLINED_FUNCTION_45
+ _PKManagerPlugInBundleIdentifierKey
+ _SecCodeCopyGuestWithAttributes
+ _SecCodeCopyPath
+ _SecCodeCopySigningInformation
+ _SecRequirementCreateWithString
+ _SecStaticCodeCheckValidity
+ _SecStaticCodeCreateWithPath
+ __105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke
+ __105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_2
+ __105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_3
+ __105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_4
+ __105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_5
+ __45-[SPConcreteCoreSpotlightIndexer addClients:]_block_invoke
+ __85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke_2
+ __CFURLGetVolumePropertyFlags
+ __CSCopyContentSchemaContainer
+ __OBJC_$_INSTANCE_METHODS_SDProvenanceResult
+ __OBJC_$_INSTANCE_VARIABLES_SDProvenanceResult
+ __OBJC_$_PROP_LIST_SDProvenanceResult
+ __OBJC_CLASS_RO_$_SDProvenanceResult
+ __OBJC_METACLASS_RO_$_SDProvenanceResult
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_10
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_11
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_12
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_13
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_14
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_15
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_16
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_2
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_3
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_4
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_5
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_6
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_7
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_8
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_9
+ ___41-[SPConcreteCoreSpotlightIndexer dealloc]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer sp_startDrainTokenSweepTimer]_block_invoke
+ ___69-[SPConcreteCoreSpotlightIndexer sp_issueDrainForBundleID:token:now:]_block_invoke
+ ___76-[CSSearchAgent _issueDrainIfRequestedForQueryContext:searchConnection:qos:]_block_invoke
+ ___binaryProvenanceForURL_block_invoke
+ ___block_descriptor_32_e13_v24?0^8^16l
+ ___block_descriptor_40_e8_32s_e5_B8?0l
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e28_v24?0"NSData"8"NSError"16l
+ ___copy_assignment_8_8_s0_s8
+ ___copy_assignment_8_8_s0_t8w8_AB16s8n16_s16_AE_t144w144
+ ___copy_assignment_8_8_t0w16_s16_s24_s32_t40w1
+ ___destructor_8_s0_AB16s8n16_s16_AE
+ ___destructor_8_s16_s24_s32
+ ___dispatchDrainSends_block_invoke
+ ___logForCSLogCategoryDrain_block_invoke
+ ___precompiledRequirement_block_invoke
+ _fsgetpath
+ _getattrlist
+ _kSecCodeInfoCertificates
+ _kSecCodeInfoFlags
+ _kSecCodeInfoTeamIdentifier
+ _kSecEntitlementCSAllowQueryDrainTrigger
+ _kSecGuestAttributeAudit
+ _logForCSLogCategoryDrain
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$_indexUnavailableErrorCodeForFailedOpen
+ _objc_msgSend$_issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:
+ _objc_msgSend$_issueDrainIfRequestedForQueryContext:searchConnection:qos:
+ _objc_msgSend$_validatedDrainBundleIDsForQueryContext:searchConnection:
+ _objc_msgSend$allowQueryDrainTrigger
+ _objc_msgSend$appIdentifierFromTeamAppTuple:
+ _objc_msgSend$containingAppForPlugInConnectedTo:
+ _objc_msgSend$drainBundleIDs
+ _objc_msgSend$drainDonations
+ _objc_msgSend$drainToken
+ _objc_msgSend$evaluateDrainRateLimitForBundleIDs:clientBundleID:
+ _objc_msgSend$evictPendingDrainTokensForBundleID:
+ _objc_msgSend$indexer
+ _objc_msgSend$informationForPlugInWithPid:
+ _objc_msgSend$issueDrainForBundleID:token:
+ _objc_msgSend$performDrainWithToken:
+ _objc_msgSend$processDrainResponse:
+ _objc_msgSend$provenance
+ _objc_msgSend$recordedBundleIDForDrainToken:
+ _objc_msgSend$removeDrainTokenEntry:bundleID:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$setProvenance:
+ _objc_msgSend$setTeamIdentifier:
+ _objc_msgSend$setupHasComplete
+ _objc_msgSend$shouldLogQueryDrainTriggerRejection
+ _objc_msgSend$sp_buildDrainDictionaryForToken:
+ _objc_msgSend$sp_decrementDonorIdentityTokenSlotCountForBundleID:count:now:
+ _objc_msgSend$sp_drainCallerIdentitySlotForBundleID:now:
+ _objc_msgSend$sp_drainDonorIdentitySlotForBundleID:now:
+ _objc_msgSend$sp_effectiveOccupiedDrainTokenTTLSeconds
+ _objc_msgSend$sp_effectiveQuarantinedDrainTokenTTLSeconds
+ _objc_msgSend$sp_evaluateDrainRateLimitForBundleIDs:clientBundleID:now:
+ _objc_msgSend$sp_evictAllDrainTokensForBundleID:protectionClass:
+ _objc_msgSend$sp_evictAllDrainTokensForBundleID:protectionClass:now:
+ _objc_msgSend$sp_evictDrainTokenAtIndex:expectedToken:now:
+ _objc_msgSend$sp_issueDrainForBundleID:token:now:
+ _objc_msgSend$sp_reconcileDrainTokenSweepTimerSuspension
+ _objc_msgSend$sp_recordedBundleIDForDrainToken:
+ _objc_msgSend$sp_removeDrainTokenEntry:expectingBundleID:
+ _objc_msgSend$sp_removeDrainTokenEntry:expectingBundleID:now:
+ _objc_msgSend$sp_sendDrainToken:toBundleID:
+ _objc_msgSend$sp_startDrainTokenSweepTimer
+ _objc_msgSend$sp_sweepExpiredDrainTokens:
+ _objc_msgSend$teamIdentifier
+ _objc_msgSend$trialSpotlightUITreatmentID
+ _precompiledRequirement
+ _provenanceFromSigningInfo
+ _provenanceName
+ _readFileIdentity
+ binaryProvenanceForURL.onceToken
+ binaryProvenanceForURL.provenanceCache
+ logForCSLogCategoryDrain
+ logForCSLogCategoryDrain.onceToken
+ logForCSLogCategoryDrain.sDrainLog
+ provenanceFromSigningInfo
+ sdReqAnchorApple.once
+ sdReqAnchorApple.slot
+ sdReqAnchorAppleGeneric.once
+ sdReqAnchorAppleGeneric.slot
+ sdReqAppStore.once
+ sdReqAppStore.slot
+ sdReqDeveloperID.once
+ sdReqDeveloperID.slot
+ sdReqDevelopmentA.once
+ sdReqDevelopmentA.slot
+ sdReqDevelopmentB.once
+ sdReqDevelopmentB.slot
- -[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]
- GCC_except_table1004
- GCC_except_table1005
- GCC_except_table1014
- GCC_except_table1030
- GCC_except_table1031
- GCC_except_table1079
- GCC_except_table1084
- GCC_except_table1148
- GCC_except_table1189
- GCC_except_table1195
- GCC_except_table1196
- GCC_except_table1202
- GCC_except_table1203
- GCC_except_table1204
- GCC_except_table1214
- GCC_except_table1216
- GCC_except_table1240
- GCC_except_table1244
- GCC_except_table1259
- GCC_except_table1270
- GCC_except_table1277
- GCC_except_table1284
- GCC_except_table1298
- GCC_except_table1316
- GCC_except_table1391
- GCC_except_table1392
- GCC_except_table1394
- GCC_except_table1401
- GCC_except_table1459
- GCC_except_table1466
- GCC_except_table190
- GCC_except_table204
- GCC_except_table218
- GCC_except_table225
- GCC_except_table227
- GCC_except_table228
- GCC_except_table236
- GCC_except_table238
- GCC_except_table249
- GCC_except_table250
- GCC_except_table254
- GCC_except_table261
- GCC_except_table267
- GCC_except_table277
- GCC_except_table306
- GCC_except_table311
- GCC_except_table313
- GCC_except_table327
- GCC_except_table335
- GCC_except_table347
- GCC_except_table375
- GCC_except_table385
- GCC_except_table400
- GCC_except_table435
- GCC_except_table436
- GCC_except_table440
- GCC_except_table495
- GCC_except_table516
- GCC_except_table517
- GCC_except_table545
- GCC_except_table572
- GCC_except_table585
- GCC_except_table588
- GCC_except_table641
- GCC_except_table655
- GCC_except_table666
- GCC_except_table692
- GCC_except_table698
- GCC_except_table713
- GCC_except_table714
- GCC_except_table726
- GCC_except_table755
- GCC_except_table781
- GCC_except_table782
- GCC_except_table783
- GCC_except_table807
- GCC_except_table873
- GCC_except_table894
- GCC_except_table915
- GCC_except_table919
- GCC_except_table923
- GCC_except_table952
- GCC_except_table975
- _OBJC_CLASS_$_LSApplicationExtensionRecord
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4
- __90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5
- __MDPlistContainerCreateWithObject
- ___45-[SPConcreteCoreSpotlightIndexer addClients:]_block_invoke_2
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_14
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_15
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_16
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_3
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_4
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_5
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_6
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_7
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_8
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_9
- ___block_descriptor_32_e9_v16?0^8l
- _gDefaultSchemaPlistBytes
- _mach_vm_allocate
- _mach_vm_deallocate
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$bundleWithIdentifier:
- _objc_msgSend$checkedInClients
- _objc_msgSend$containingBundleRecord
- _objc_msgSend$initWithBundleIdentifier:error:
- _objc_msgSend$initWithContentsOfFile:
- _objc_msgSend$keyEnumerator
CStrings:
+ "%llu|%llu|%u"
+ "%s reindexAllCallToDaemonServer1(%s/excluded:[%s]/%s)"
+ "%s reindexAllCallToDaemonServer2(excluded:[%s]/%s)"
+ "%s reindexAllCallToDaemonServer3([%s]/excluded:[%s]/%s)"
+ "%s reindexAllCallToDelegate(%s/%s)"
+ "(no bundle)"
+ "(no bundles)"
+ "(no reason)"
+ "(no time)"
+ "*warn* Bootstrap - Initial setup assistant not complete, not issuing reindex to clients: %@"
+ "*warn* Bootstrap - setup assistant complete, issuing reindex to clients: %@"
+ "*warn* OpenIndex - Initial setup assistant not complete, not issuing reindex to clients: %@"
+ "*warn* OpenIndex - Initial setup assistant not complete: %@"
+ "Client %@ not allowed to trigger a drain"
+ "Client %@ requested drain for %lu bundles, only the first %lu are considered"
+ "Client %@ requested drain for bundle %@ without having entitlement %@"
+ "Client %@ requested drain with an invalid bundleID entry %@"
+ "Disk commit observed for dataclass:%@"
+ "Donor identity token-slot decrement no-op for bundleID:%@, count:%lu — identity slot absent or already at zero count"
+ "Drain"
+ "Drain response for unknown/expired token:%@ from client:%@ — dropping, no recorded owner to verify against"
+ "Drain response missing token from client %@"
+ "Drain response token:%@ bundleID:%@ outcome:%llu"
+ "Drain response token:%@ bundleID:%@ outcome:%llu queueDepth:%llu"
+ "Drain response token:%@ recorded for bundleID:%@ but presented by client:%@ — dropping, entry left in place"
+ "Drain sent for bundleID:%@, token:%@"
+ "Drain skipped for bundleID:%@, token:%@ — identity already holds kSPMaxDrainTokenSlotsPerIdentity token-table slots, or the identity table is saturated with other live identities"
+ "Drain skipped for bundleID:%@, token:%@ — token already in flight or quarantined, recorded bundleID:%@"
+ "Drain skipped for bundleID:%@, token:%@ — token table full"
+ "Drain token TTL-evicted for bundleID:%@, token:%@"
+ "Drain tokens bulk-quarantined for bundleID:%@, count:%lu"
+ "Mail account delete promoted to full bundle delete for %{private}@"
+ "OpenIndex - Initial setup assistant complete: %@"
+ "Rejecting bundle ID %@ from %s client (pid %d) — a higher-provenance (%s) app on this system also claims it"
+ "Rejecting bundle ID %@ from %s client (pid %d) — cannot rule out a higher-provenance claimant (%s)"
+ "Rejecting bundle ID %@ from %s client (pid %d) — impersonates Apple bundle ID namespace"
+ "Skipping job %ld from %@ (pc: %@) - excluded: %d"
+ "Tier-1 drain rate-limit slot LRU-evicted bundleID:%@ to admit bundleID:%@"
+ "a claimant was unreadable/indeterminate"
+ "ad-hoc"
+ "anchor apple"
+ "anchor apple generic"
+ "anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] and certificate leaf[field.1.2.840.113635.100.6.1.13]"
+ "anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.12]"
+ "anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.2]"
+ "anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.9]"
+ "app-store"
+ "binaryProvenanceForURL: Apple-rooted but unclassified marker for %{public}@"
+ "claimant list may be truncated"
+ "client reindex request from %@"
+ "client reindex request multiple from %@"
+ "com.apple"
+ "com.apple.private.corespotlight.allowquerydraintrigger"
+ "com.apple.spotlight.drainTokenSweep.%p"
+ "developer-id"
+ "development"
+ "drain-declined-queue-depth"
+ "drain-outcome"
+ "drain-queue"
+ "drain-response"
+ "drain-token"
+ "highestClaimantProvenance: %lu claimants for %@ exceeds cap %lu; stopping scan"
+ "performDrainWithToken: called with nil token for client %@, dropping"
+ "platform"
+ "self-signed"
+ "transferDeleteJournalsToDirectory failed: index:%p suspended:%d readOnly:%d code:%ld"
+ "v24@?0^@8^@16"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc1"
- "E"
- "Failed to allocate for schema: %d"
- "client reindex request"
- "issue-command"
- "mdplist"
- "plist"
- "schema"
- "v16@?0^@8"
- "\xf0Q"
```
