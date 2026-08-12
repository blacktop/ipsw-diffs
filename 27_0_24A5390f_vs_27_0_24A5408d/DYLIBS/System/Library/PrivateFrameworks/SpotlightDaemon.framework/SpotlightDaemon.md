## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0xc06f8
-  __TEXT.__objc_methlist: 0x49cc
-  __TEXT.__const: 0x3d8
-  __TEXT.__cstring: 0x96b7
-  __TEXT.__gcc_except_tab: 0x4944
-  __TEXT.__oslogstring: 0xcb64
+2459.102.0.0.0
+  __TEXT.__text: 0xc4514
+  __TEXT.__objc_methlist: 0x4bc4
+  __TEXT.__const: 0x3e8
+  __TEXT.__cstring: 0x98ea
+  __TEXT.__gcc_except_tab: 0x4a1c
+  __TEXT.__oslogstring: 0xd304
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x2800
+  __TEXT.__unwind_info: 0x28f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4730
+  __DATA_CONST.__const: 0x47b0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __DATA_CONST.__objc_selrefs: 0x3d10
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x300
-  __DATA_CONST.__got: 0xbe8
-  __AUTH_CONST.__const: 0x1308
-  __AUTH_CONST.__cfstring: 0x7fe0
-  __AUTH_CONST.__objc_const: 0x5f48
+  __DATA_CONST.__objc_arraydata: 0x310
+  __DATA_CONST.__got: 0xbf8
+  __AUTH_CONST.__const: 0x1328
+  __AUTH_CONST.__cfstring: 0x7fc0
+  __AUTH_CONST.__objc_const: 0x6128
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x390
+  __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1130
+  __AUTH_CONST.__auth_got: 0x1120
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x50c
+  __DATA.__objc_ivar: 0x540
   __DATA.__data: 0x418
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x160
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x158
-  __DATA_DIRTY.__bss: 0x6e0
+  __DATA_DIRTY.__bss: 0x6d8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3320
-  Symbols:   6646
-  CStrings:  2661
+  Functions: 3377
+  Symbols:   6747
+  CStrings:  2699
 
Symbols:
+ -[CSSearchAgent _issueDrainIfRequestedForQueryContext:searchConnection:qos:]
+ -[CSSearchAgent _validatedDrainBundleIDsForQueryContext:searchConnection:]
+ -[MDSearchableIndexService performDrainWithToken:]
+ -[MDSearchableIndexService processDrainResponse:]
+ -[MDSearchableIndexService sp_buildDrainDictionaryForToken:]
+ -[SDConnectionConfiguration allowQueryDrainTrigger]
+ -[SDConnectionConfiguration shouldLogQueryDrainTriggerRejection]
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
+ GCC_except_table1011
+ GCC_except_table1012
+ GCC_except_table1021
+ GCC_except_table1037
+ GCC_except_table1038
+ GCC_except_table1082
+ GCC_except_table1087
+ GCC_except_table1138
+ GCC_except_table1172
+ GCC_except_table1178
+ GCC_except_table1179
+ GCC_except_table1185
+ GCC_except_table1186
+ GCC_except_table1187
+ GCC_except_table1197
+ GCC_except_table1199
+ GCC_except_table1214
+ GCC_except_table1220
+ GCC_except_table1254
+ GCC_except_table1261
+ GCC_except_table1268
+ GCC_except_table1275
+ GCC_except_table1282
+ GCC_except_table1299
+ GCC_except_table1377
+ GCC_except_table1378
+ GCC_except_table1380
+ GCC_except_table1387
+ GCC_except_table1447
+ GCC_except_table1454
+ GCC_except_table1581
+ GCC_except_table1582
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table190
+ GCC_except_table213
+ GCC_except_table218
+ GCC_except_table238
+ GCC_except_table240
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table267
+ GCC_except_table273
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table293
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table313
+ GCC_except_table321
+ GCC_except_table337
+ GCC_except_table361
+ GCC_except_table371
+ GCC_except_table385
+ GCC_except_table418
+ GCC_except_table419
+ GCC_except_table423
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table491
+ GCC_except_table522
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table574
+ GCC_except_table575
+ GCC_except_table576
+ GCC_except_table614
+ GCC_except_table639
+ GCC_except_table658
+ GCC_except_table683
+ GCC_except_table684
+ GCC_except_table694
+ GCC_except_table722
+ GCC_except_table747
+ GCC_except_table748
+ GCC_except_table749
+ GCC_except_table775
+ GCC_except_table841
+ GCC_except_table865
+ GCC_except_table886
+ GCC_except_table894
+ GCC_except_table922
+ GCC_except_table951
+ GCC_except_table982
+ OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._checkedInClientsLock
+ _CPCopyBundleIdentifierAndTeamFromApplicationIdentifier
+ _OBJC_CLASS_$_PKManager
+ _OBJC_IVAR_$_SDConnectionConfiguration._allowQueryDrainTrigger
+ _OBJC_IVAR_$_SDConnectionConfiguration._queryDrainTriggerRejectionLogged
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainCallerIdentityEntries
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainCallerIdentityLock
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainDonorIdentityEntries
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainDonorIdentityLock
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenEntries
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenLiveCount
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenLock
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenSweepQueue
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenSweepTimer
+ _OBJC_IVAR_$_SPConcreteCoreSpotlightIndexer._drainTokenSweepTimerSuspended
+ _PKManagerPlugInBundleIdentifierKey
+ __CSCopyContentSchemaContainer
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_10
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_11
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_12
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_13
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_14
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_15
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_16
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_17
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_18
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_19
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_2
+ ___105-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:]_block_invoke_20
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
+ ___block_descriptor_32_e13_v24?0^8^16l
+ ___block_descriptor_40_e8_32s_e5_B8?0ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___copy_assignment_8_8_s0_s8
+ ___copy_assignment_8_8_s0_t8w8_AB16s8n16_s16_AE_t144w144
+ ___copy_assignment_8_8_t0w16_s16_s24_s32_t40w1
+ ___destructor_8_s0_AB16s8n16_s16_AE
+ ___destructor_8_s16_s24_s32
+ ___dispatchDrainSends_block_invoke
+ ___logForCSLogCategoryDrain_block_invoke
+ _kSecEntitlementCSAllowQueryDrainTrigger
+ _logForCSLogCategoryDrain
+ _logForCSLogCategoryDrain.onceToken
+ _logForCSLogCategoryDrain.sDrainLog
+ _objc_msgSend$_indexUnavailableErrorCodeForFailedOpen
+ _objc_msgSend$_issueCommand:outFileDescriptor:searchContext:clientBundleID:completionHandler:
+ _objc_msgSend$_issueDrainIfRequestedForQueryContext:searchConnection:qos:
+ _objc_msgSend$_validatedDrainBundleIDsForQueryContext:searchConnection:
+ _objc_msgSend$allowQueryDrainTrigger
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
+ _objc_msgSend$recordedBundleIDForDrainToken:
+ _objc_msgSend$removeDrainTokenEntry:bundleID:
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
+ _objc_msgSend$trialSpotlightUITreatmentID
- -[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]
- GCC_except_table1005
- GCC_except_table1006
- GCC_except_table1050
- GCC_except_table1055
- GCC_except_table1106
- GCC_except_table1140
- GCC_except_table1146
- GCC_except_table1147
- GCC_except_table1153
- GCC_except_table1154
- GCC_except_table1155
- GCC_except_table1156
- GCC_except_table1165
- GCC_except_table1167
- GCC_except_table1182
- GCC_except_table1192
- GCC_except_table1206
- GCC_except_table1217
- GCC_except_table1231
- GCC_except_table1245
- GCC_except_table1262
- GCC_except_table1340
- GCC_except_table1341
- GCC_except_table1343
- GCC_except_table1350
- GCC_except_table1408
- GCC_except_table1415
- GCC_except_table1541
- GCC_except_table1542
- GCC_except_table168
- GCC_except_table169
- GCC_except_table183
- GCC_except_table188
- GCC_except_table201
- GCC_except_table208
- GCC_except_table210
- GCC_except_table221
- GCC_except_table222
- GCC_except_table224
- GCC_except_table227
- GCC_except_table228
- GCC_except_table236
- GCC_except_table237
- GCC_except_table243
- GCC_except_table245
- GCC_except_table246
- GCC_except_table263
- GCC_except_table269
- GCC_except_table283
- GCC_except_table291
- GCC_except_table301
- GCC_except_table307
- GCC_except_table341
- GCC_except_table355
- GCC_except_table388
- GCC_except_table389
- GCC_except_table393
- GCC_except_table416
- GCC_except_table445
- GCC_except_table461
- GCC_except_table462
- GCC_except_table516
- GCC_except_table530
- GCC_except_table533
- GCC_except_table544
- GCC_except_table545
- GCC_except_table584
- GCC_except_table598
- GCC_except_table609
- GCC_except_table634
- GCC_except_table653
- GCC_except_table654
- GCC_except_table692
- GCC_except_table717
- GCC_except_table718
- GCC_except_table719
- GCC_except_table743
- GCC_except_table809
- GCC_except_table833
- GCC_except_table854
- GCC_except_table858
- GCC_except_table862
- GCC_except_table919
- GCC_except_table950
- GCC_except_table979
- GCC_except_table980
- GCC_except_table989
- _SecTaskCopyTeamIdentifier
- _SecTaskGetValidationCategory
- ___45-[SPConcreteCoreSpotlightIndexer addClients:]_block_invoke_2
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_10
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_11
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_12
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_13
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_14
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_15
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_16
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_17
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_18
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_19
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_2
- ___90-[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:]_block_invoke_20
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
- _objc_msgSend$bundleWithIdentifier:
- _objc_msgSend$checkedInClients
- _objc_msgSend$initWithContentsOfFile:
- _objc_msgSend$keyEnumerator
CStrings:
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
+ "Skipping job %ld from %@ (pc: %@) - excluded: %d"
+ "Tier-1 drain rate-limit slot LRU-evicted bundleID:%@ to admit bundleID:%@"
+ "client reindex request from %@"
+ "client reindex request multiple from %@"
+ "com.apple.private.corespotlight.allowquerydraintrigger"
+ "com.apple.spotlight.drainTokenSweep.%p"
+ "drain-declined-queue-depth"
+ "drain-outcome"
+ "drain-queue"
+ "drain-response"
+ "drain-token"
+ "performDrainWithToken: called with nil token for client %@, dropping"
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
