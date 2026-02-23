## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2952.100.21.0.0
-  __TEXT.__text: 0x362958
+2952.100.23.0.0
+  __TEXT.__text: 0x36365c
   __TEXT.__auth_stubs: 0x5240
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x17d84
+  __TEXT.__objc_methlist: 0x17ddc
   __TEXT.__const: 0xdcf8
-  __TEXT.__cstring: 0x1a541
-  __TEXT.__oslogstring: 0x1bc78
-  __TEXT.__gcc_except_tab: 0xf7b8
+  __TEXT.__cstring: 0x1a581
+  __TEXT.__oslogstring: 0x1bd28
+  __TEXT.__gcc_except_tab: 0xf818
   __TEXT.__ustring: 0x38e
   __TEXT.__swift5_typeref: 0x43d4
   __TEXT.__swift5_fieldmd: 0x2d9c

   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf4f0
+  __TEXT.__unwind_info: 0xf518
   __TEXT.__eh_frame: 0x8ce8
   __TEXT.__objc_classname: 0x2ada
-  __TEXT.__objc_methname: 0x3769f
-  __TEXT.__objc_methtype: 0x513f
-  __TEXT.__objc_stubs: 0x285a0
+  __TEXT.__objc_methname: 0x3780f
+  __TEXT.__objc_methtype: 0x514f
+  __TEXT.__objc_stubs: 0x28660
   __DATA_CONST.__got: 0x2130
-  __DATA_CONST.__const: 0x6248
+  __DATA_CONST.__const: 0x62e8
   __DATA_CONST.__objc_classlist: 0xa40
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8f8
+  __DATA_CONST.__objc_selrefs: 0xc930
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6b8
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2980
   __AUTH_CONST.__const: 0xd7b0
-  __AUTH_CONST.__cfstring: 0xf380
-  __AUTH_CONST.__objc_const: 0x21c28
+  __AUTH_CONST.__cfstring: 0xf3a0
+  __AUTH_CONST.__objc_const: 0x21c58
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4FDC1EB9-28DF-3E7C-AEE6-9A539634D346
-  Functions: 18369
-  Symbols:   38806
-  CStrings:  16474
+  UUID: 24577FE7-8A61-3E71-B128-74624FE8B592
+  Functions: 18382
+  Symbols:   38845
+  CStrings:  16487
 
Symbols:
+ +[ICShareNotifier isDaemonProcess]
+ -[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]
+ -[ICCloudContext enterDispatchGroupIfNeededWithGroup:]
+ -[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]
+ -[ICCloudContext fetchRecordZoneChangesForSession:dispatchGroup:completionHandler:]
+ -[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]
+ -[ICCloudContext fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:dispatchGroup:]
+ -[ICCloudContext fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:dispatchGroup:]
+ -[ICCloudContext fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:dispatchGroup:]
+ -[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:dispatchGroup:]
+ -[ICCloudContext leaveDispatchGroupIfNeededWithGroup:]
+ -[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]
+ -[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:].cold.1
+ -[ICCloudContext operationToFetchRecordZoneChangesForZoneIDs:database:session:dispatchGroup:]
+ -[ICCloudContext operationToFetchRecordZoneChangesForZoneIDs:database:session:dispatchGroup:].cold.1
+ -[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:dispatchGroup:]
+ -[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:dispatchGroup:].cold.1
+ -[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:dispatchGroup:].cold.2
+ -[ICCloudContext useDispatchGroupForDaemonProcessWithGroup:]
+ -[ICNote(SearchIndexableNote) hashtagContentIdentifiers]
+ -[ICSettingsCloudContextDelegate isDaemonProcessForCloudContext:]
+ GCC_except_table129
+ GCC_except_table145
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table184
+ GCC_except_table193
+ GCC_except_table208
+ GCC_except_table231
+ GCC_except_table250
+ GCC_except_table272
+ GCC_except_table303
+ GCC_except_table335
+ GCC_except_table366
+ GCC_except_table384
+ GCC_except_table408
+ GCC_except_table413
+ GCC_except_table418
+ GCC_except_table564
+ GCC_except_table567
+ GCC_except_table568
+ GCC_except_table601
+ GCC_except_table602
+ GCC_except_table603
+ GCC_except_table633
+ GCC_except_table652
+ ___108-[ICCloudContext fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:dispatchGroup:]_block_invoke
+ ___108-[ICCloudContext fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:dispatchGroup:]_block_invoke.cold.1
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_2
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_3
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_4
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_5
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_6
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_7
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_8
+ ___108-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:]_block_invoke_9
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.583
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.cold.1
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2
+ ___113-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2.584
+ ___120-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]_block_invoke
+ ___120-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:]_block_invoke.608
+ ___120-[ICCloudContext fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:dispatchGroup:]_block_invoke
+ ___120-[ICCloudContext fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:dispatchGroup:]_block_invoke_2
+ ___122-[ICCloudContext fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:dispatchGroup:]_block_invoke
+ ___38-[ICCloudContext clearPendingActivity]_block_invoke.205
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.695
+ ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.699
+ ___49+[ICShareNotifier shouldShowNotificationForNote:]_block_invoke.50
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.689
+ ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.691
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.201
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.203
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.202
+ ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.204
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.659
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.663
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.663.cold.1
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.667
+ ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.661
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke.235
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.236
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.236.cold.1
+ ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.236.cold.2
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.631
+ ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.633
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.239
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.239.cold.1
+ ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.239.cold.2
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.643
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.645
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.646
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.646.cold.1
+ ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.646.cold.2
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.638
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.639
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.639.cold.1
+ ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.639.cold.2
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.554
+ ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.555
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.193.cold.1
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.194
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.195
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.195.cold.1
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.196
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke_2
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke_3
+ ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke_3.cold.1
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.668
+ ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.670
+ ___78-[ICCloudContext addOperationToProcessObjectsInSession:withCompletionHandler:]_block_invoke.374
+ ___80-[ICCloudContext deleteSharesForObjects:forSession:accountID:completionHandler:]_block_invoke.287
+ ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.227
+ ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.227.cold.1
+ ___83-[ICCloudContext fetchRecordZoneChangesForSession:dispatchGroup:completionHandler:]_block_invoke
+ ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.677
+ ___89-[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:dispatchGroup:]_block_invoke
+ ___89-[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:dispatchGroup:]_block_invoke.cold.1
+ ___89-[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:dispatchGroup:]_block_invoke.cold.2
+ ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.322
+ ___93-[ICCloudContext operationToFetchRecordZoneChangesForZoneIDs:database:session:dispatchGroup:]_block_invoke
+ ___95-[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:dispatchGroup:]_block_invoke
+ ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.207
+ ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.207.cold.1
+ ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.208
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.579
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.cold.1
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke.cold.2
+ ___98-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:]_block_invoke_2
+ ___99+[ICCloudContext batchRecordsToSave:delete:maxRecordCountPerBatch:maxRecordSizePerBatch:withBlock:]_block_invoke.316
+ ___block_descriptor_56_e8_32s40s48r_e18_v16?0"NSString"8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r64w_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8w64l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0lr64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSError"8ls32l8w64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56r64w_e33_v24?0"CKRecordID"8"NSString"16ls32l8w64l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64w_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24ls32l8w64l8s40l8r56l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72w_e59_v32?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24ls32l8w72l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.210
+ ___block_literal_global.293
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.348
+ ___block_literal_global.356
+ ___block_literal_global.363
+ ___block_literal_global.624
+ ___block_literal_global.672
+ _objc_msgSend$addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:
+ _objc_msgSend$enterDispatchGroupIfNeededWithGroup:
+ _objc_msgSend$fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:
+ _objc_msgSend$fetchRecordZoneChangesForSession:dispatchGroup:completionHandler:
+ _objc_msgSend$fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:
+ _objc_msgSend$fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:dispatchGroup:
+ _objc_msgSend$fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:dispatchGroup:
+ _objc_msgSend$fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:dispatchGroup:
+ _objc_msgSend$fetchRecordZoneChangesOperationDidComplete:session:error:dispatchGroup:
+ _objc_msgSend$isDaemonProcess
+ _objc_msgSend$isDaemonProcessForCloudContext:
+ _objc_msgSend$leaveDispatchGroupIfNeededWithGroup:
+ _objc_msgSend$newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:
+ _objc_msgSend$operationToFetchRecordZoneChangesForZoneIDs:database:session:dispatchGroup:
+ _objc_msgSend$operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:dispatchGroup:
+ _objc_msgSend$processName
+ _objc_msgSend$useDispatchGroupForDaemonProcessWithGroup:
- -[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]
- -[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]
- -[ICCloudContext fetchRecordZoneChangesForSession:completionHandler:]
- -[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]
- -[ICCloudContext fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:]
- -[ICCloudContext fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:]
- -[ICCloudContext fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:]
- -[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:]
- -[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]
- -[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:].cold.1
- -[ICCloudContext operationToFetchRecordZoneChangesForZoneIDs:database:session:]
- -[ICCloudContext operationToFetchRecordZoneChangesForZoneIDs:database:session:].cold.1
- -[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:]
- -[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:].cold.1
- -[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:].cold.2
- GCC_except_table111
- GCC_except_table122
- GCC_except_table166
- GCC_except_table224
- GCC_except_table243
- GCC_except_table252
- GCC_except_table327
- GCC_except_table358
- GCC_except_table376
- GCC_except_table410
- GCC_except_table554
- GCC_except_table557
- GCC_except_table558
- GCC_except_table591
- GCC_except_table592
- GCC_except_table593
- GCC_except_table623
- GCC_except_table642
- ___106-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]_block_invoke
- ___106-[ICCloudContext fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:]_block_invoke.605
- ___106-[ICCloudContext fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:]_block_invoke
- ___106-[ICCloudContext fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:]_block_invoke_2
- ___108-[ICCloudContext fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:]_block_invoke
- ___38-[ICCloudContext clearPendingActivity]_block_invoke.202
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.692
- ___44-[ICCloudContext retryOperationsIfNecessary]_block_invoke.696
- ___49+[ICShareNotifier shouldShowNotificationForNote:]_block_invoke.46
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.686
- ___54-[ICCloudContext startRetryTimerIfNecessaryWithError:]_block_invoke.688
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.198
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke.200
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.199
- ___56-[ICCloudContext cancelEverythingWithCompletionHandler:]_block_invoke_2.201
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.656
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.657
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.660.cold.1
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke.664
- ___56-[ICCloudContext updateCloudContextStateWithCompletion:]_block_invoke_2.658
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke.232
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.233
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.233.cold.1
- ___59-[ICCloudContext updateAccountStatusWithCompletionHandler:]_block_invoke_2.233.cold.2
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.628
- ___59-[ICCloudContext updateSubscriptionsWithCompletionHandler:]_block_invoke.630
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.236
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.236.cold.1
- ___65-[ICCloudContext fetchUserRecordWithContainer:completionHandler:]_block_invoke.236.cold.2
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.640
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke.642
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.643
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.643.cold.1
- ___65-[ICCloudContext saveSubscriptionsForDatabase:completionHandler:]_block_invoke_2.643.cold.2
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke.635
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.636
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.636.cold.1
- ___66-[ICCloudContext fetchSubscriptionsForDatabase:completionHandler:]_block_invoke_2.636.cold.2
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke.551
- ___67-[ICCloudContext _processCloudObjects:inSession:completionHandler:]_block_invoke_2.552
- ___69-[ICCloudContext fetchRecordZoneChangesForSession:completionHandler:]_block_invoke
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.191
- ___74-[ICCloudContext _syncWithReason:uploadUnsyncedChanges:completionHandler:]_block_invoke.191.cold.1
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke.665
- ___74-[ICCloudContext enqueueLongLivedOperationsIfNeededWithCompletionHandler:]_block_invoke_2.667
- ___75-[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:]_block_invoke
- ___75-[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:]_block_invoke.cold.1
- ___75-[ICCloudContext fetchRecordZoneChangesOperationDidComplete:session:error:]_block_invoke.cold.2
- ___78-[ICCloudContext addOperationToProcessObjectsInSession:withCompletionHandler:]_block_invoke.371
- ___79-[ICCloudContext operationToFetchRecordZoneChangesForZoneIDs:database:session:]_block_invoke
- ___80-[ICCloudContext deleteSharesForObjects:forSession:accountID:completionHandler:]_block_invoke.284
- ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.224
- ___81-[ICCloudContext finishOperationsForRecordID:qualityOfService:completionHandler:]_block_invoke.224.cold.1
- ___81-[ICCloudContext operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:]_block_invoke
- ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke
- ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.576
- ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.cold.1
- ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.cold.2
- ___84-[ICCloudContext fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke_2
- ___88-[ICCloudContext enqueueLongLivedOperationsWithIDsIfNeeded:container:completionHandler:]_block_invoke.674
- ___91-[ICCloudContext addCallbackBlocksToModifyRecordsOperation:rootRecordIDsByShareID:session:]_block_invoke.319
- ___94-[ICCloudContext fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:]_block_invoke
- ___94-[ICCloudContext fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:]_block_invoke.cold.1
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_2
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_3
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_4
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_5
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_6
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_7
- ___94-[ICCloudContext newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:]_block_invoke_8
- ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.204
- ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.204.cold.1
- ___97-[ICCloudContext deleteRecordZonesWithZoneIDs:accountID:markZonesAsUserPurged:completionHandler:]_block_invoke.205
- ___99+[ICCloudContext batchRecordsToSave:delete:maxRecordCountPerBatch:maxRecordSizePerBatch:withBlock:]_block_invoke.313
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.580
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke.cold.1
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke_2
- ___99-[ICCloudContext addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:]_block_invoke_2.581
- ___block_descriptor_56_e8_32s40s48s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48r56w_e74_v44?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24B32"NSError"36ls32l8w56l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8ls32l8w56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56w_e33_v24?0"CKRecordID"8"NSString"16ls32l8w56l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48r56w_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24ls32l8w56l8s40l8r48l8
- ___block_descriptor_72_e8_32s40s48bs56r64w_e59_v32?0"CKRecordZoneID"8"CKServerChangeToken"16"NSData"24ls32l8w64l8s40l8r56l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.207
- ___block_literal_global.290
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.345
- ___block_literal_global.353
- ___block_literal_global.360
- ___block_literal_global.621
- ___block_literal_global.669
- _objc_msgSend$addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:
- _objc_msgSend$fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:
- _objc_msgSend$fetchRecordZoneChangesForSession:completionHandler:
- _objc_msgSend$fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:
- _objc_msgSend$fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:
- _objc_msgSend$fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:
- _objc_msgSend$fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:
- _objc_msgSend$fetchRecordZoneChangesOperationDidComplete:session:error:
- _objc_msgSend$newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:
- _objc_msgSend$operationToFetchRecordZoneChangesForZoneIDs:database:session:
- _objc_msgSend$operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJaougBfE_DSJpK9Ne7l4tqOPf93FARi86jFVP0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Ironcade/Shared/CloudKit/ICCloudContext.m"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Ironcade/Shared/CoreData/AttachmentModel/ICAttachmentDrawingModel.m"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Ironcade/Shared/CoreData/ICAccount.m"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/airdrop-document.pb.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/crframework.pb.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/drawing.pb.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/io/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/io/zero_copy_stream.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/io/zero_copy_stream_impl_lite.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/stubs/common.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/wire_format_lite.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/peernetworking.pb.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/topotext.pb.cc"
+ "/Library/Caches/com.apple.xbs/2E9827E3-886C-40A5-A46F-F8F4A4B476C1/TemporaryDirectory.rWE6tF/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/versioned-document.pb.cc"
+ "_syncWithReason :: dispatchGroup failed to notify and completionHandler called after timeout in daemon process"
+ "_syncWithReason :: dispatchGroup notified in daemon process"
+ "addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:"
+ "com.apple.notes.cloud._syncCompletionHandlerCallbackQueue"
+ "enterDispatchGroupIfNeededWithGroup:"
+ "fetchRecordZoneChangesForAccountZoneIDs:session:dispatchGroup:completionHandler:"
+ "fetchRecordZoneChangesForSession:dispatchGroup:completionHandler:"
+ "fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:dispatchGroup:"
+ "fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:dispatchGroup:"
+ "fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:dispatchGroup:"
+ "fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:dispatchGroup:"
+ "fetchRecordZoneChangesOperationDidComplete:session:error:dispatchGroup:"
+ "hashtagContentIdentifiers"
+ "isDaemonProcess"
+ "isDaemonProcessForCloudContext:"
+ "leaveDispatchGroupIfNeededWithGroup:"
+ "newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:dispatchGroup:"
+ "operationToFetchRecordZoneChangesForZoneIDs:database:session:dispatchGroup:"
+ "operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:dispatchGroup:"
+ "processName"
+ "safetycheckd"
+ "useDispatchGroupForDaemonProcessWithGroup:"
+ "v72@0:8@16@24@32@40@48@56@64"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIiCugBzIT_yBzFKCSp7GAZcxi3J0mbHJu1x4qg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Ironcade/Shared/CloudKit/ICCloudContext.m"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Ironcade/Shared/CoreData/AttachmentModel/ICAttachmentDrawingModel.m"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Ironcade/Shared/CoreData/ICAccount.m"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/airdrop-document.pb.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/crframework.pb.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/drawing.pb.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/io/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/io/zero_copy_stream.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/io/zero_copy_stream_impl_lite.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/message_lite.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/repeated_field.h"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/stubs/common.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/google/protobuf/wire_format_lite.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/peernetworking.pb.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/topotext.pb.cc"
- "/Library/Caches/com.apple.xbs/F8A0E85E-68A7-4A41-A996-6ED077ADED03/TemporaryDirectory.W5dBKK/Sources/MobileNotesSupport/Source/Shared/protobuf-lite/versioned-document.pb.cc"
- "addOperationsToFetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:"
- "fetchRecordZoneChangesForAccountZoneIDs:session:completionHandler:"
- "fetchRecordZoneChangesForSession:completionHandler:"
- "fetchRecordZoneChangesOperation:completedFetchForZoneID:serverChangeToken:error:context:"
- "fetchRecordZoneChangesOperation:recordWasChangedWithRecordID:record:error:session:context:"
- "fetchRecordZoneChangesOperation:recordWasDeletedWithRecordID:recordType:session:context:"
- "fetchRecordZoneChangesOperation:zoneID:accountID:changeTokenUpdated:context:"
- "fetchRecordZoneChangesOperationDidComplete:session:error:"
- "newOperationToFetchRecordZoneChangesWithZoneConfigurations:database:session:"
- "operationToFetchRecordZoneChangesForZoneIDs:database:session:"
- "operationsToFetchRecordZoneChangesForZoneIDs:accountID:session:"

```
