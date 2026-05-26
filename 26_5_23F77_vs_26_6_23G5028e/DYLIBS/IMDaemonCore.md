## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x36c3a0
-  __TEXT.__auth_stubs: 0x55a0
-  __TEXT.__objc_methlist: 0x19c7c
-  __TEXT.__const: 0x6e98
-  __TEXT.__cstring: 0x12dcc
-  __TEXT.__gcc_except_tab: 0x22298
-  __TEXT.__oslogstring: 0x4f447
+1450.700.11.2.3
+  __TEXT.__text: 0x36de90
+  __TEXT.__auth_stubs: 0x55d0
+  __TEXT.__objc_methlist: 0x19d0c
+  __TEXT.__const: 0x6ea8
+  __TEXT.__cstring: 0x12edc
+  __TEXT.__gcc_except_tab: 0x2227c
+  __TEXT.__oslogstring: 0x4f547
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
-  __TEXT.__swift5_typeref: 0x3090
-  __TEXT.__constg_swiftt: 0x2414
+  __TEXT.__swift5_typeref: 0x30a0
+  __TEXT.__constg_swiftt: 0x2434
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x13ef
-  __TEXT.__swift5_fieldmd: 0x1698
+  __TEXT.__swift5_reflstr: 0x13ff
+  __TEXT.__swift5_fieldmd: 0x16a4
   __TEXT.__swift5_assocty: 0x6b8
-  __TEXT.__swift5_capture: 0x1338
+  __TEXT.__swift5_capture: 0x1358
   __TEXT.__swift5_proto: 0x338
   __TEXT.__swift5_types: 0x214
-  __TEXT.__swift_as_entry: 0x334
-  __TEXT.__swift_as_ret: 0x40c
+  __TEXT.__swift_as_entry: 0x338
+  __TEXT.__swift_as_ret: 0x410
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd8c8
-  __TEXT.__eh_frame: 0x781c
+  __TEXT.__unwind_info: 0xd958
+  __TEXT.__eh_frame: 0x79e4
   __TEXT.__objc_classname: 0x44f1
-  __TEXT.__objc_methname: 0x51657
+  __TEXT.__objc_methname: 0x51787
   __TEXT.__objc_methtype: 0xb33f
-  __TEXT.__objc_stubs: 0x32b80
-  __DATA_CONST.__got: 0x3340
-  __DATA_CONST.__const: 0x6680
+  __TEXT.__objc_stubs: 0x32c20
+  __DATA_CONST.__got: 0x3348
+  __DATA_CONST.__const: 0x66a8
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x778
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfeb8
+  __DATA_CONST.__objc_selrefs: 0xfef8
   __DATA_CONST.__objc_protorefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x2ae0
-  __AUTH_CONST.__const: 0x8430
-  __AUTH_CONST.__cfstring: 0xe7e0
-  __AUTH_CONST.__objc_const: 0x21208
-  __AUTH_CONST.__objc_intobj: 0xac8
+  __AUTH_CONST.__auth_got: 0x2af8
+  __AUTH_CONST.__const: 0x84e8
+  __AUTH_CONST.__cfstring: 0xe880
+  __AUTH_CONST.__objc_const: 0x21288
+  __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3428
   __AUTH.__data: 0x5e0
   __DATA.__objc_ivar: 0x123c
   __DATA.__data: 0x5860
-  __DATA.__bss: 0x5200
+  __DATA.__bss: 0x5210
   __DATA.__common: 0x178
   __DATA_DIRTY.__objc_data: 0x31b0
-  __DATA_DIRTY.__data: 0x28d0
+  __DATA_DIRTY.__data: 0x28f0
   __DATA_DIRTY.__bss: 0x19b0
   __DATA_DIRTY.__common: 0x1b8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 97CEAD15-504E-3D15-BE10-F3D681AE3843
-  Functions: 13155
-  Symbols:   3028
-  CStrings:  21679
+  UUID: 392E6CE4-F635-321F-8E14-2B845C686165
+  Functions: 13177
+  Symbols:   3032
+  CStrings:  21709
 
Symbols:
+ _IMBalloonBundleIdentifierPolls
+ _IMDCreateIMItemFromIMDMessageRecordRefWithAccountLookup
+ _IMSharedBalloonPreviewSummaryForCustomAcknowledgementMessage
+ _IMSharedBalloonPreviewSummaryForPollAddChoiceMessage
CStrings:
+ "@\"NSArray\"16@?0@\"NSString\"8"
+ "Attempted to purge an unsafe path for guid: %@ path: %@"
+ "Converting item into previous ack: %@ (a:%@, t:%lld, s: %@) %@"
+ "Creating Poll Add Choice summary for sent message; sender: '%@':'%@'"
+ "Deleting formerly oldest ack %@"
+ "Failed to encode outgoing relay dictionary for message GUID %@. Data will be incomplete."
+ "Failed to purge file for guid: %@ error: %@"
+ "Found prior vote across session breadcrumbs: %@ (a:%@, t:%lld) for summary generation"
+ "Guids to delete: %lu"
+ "MiC.DASCheckpointBalancedVersion"
+ "MiC.SyncResumeBatchProgress"
+ "MiC.SyncResumeCompletedStepIndex"
+ "MiC.SyncResumePhase"
+ "Preparing relay send dictionary"
+ "Will NOT delete ack %@ (a:%@, t:%lld, s: %@) %@"
+ "Will delete old ack %@ (a:%@, t:%lld, s: %@) %@"
+ "Will delete old prior ack %@ (a:%@, t:%lld, s: %@) %@"
+ "[%{public}s] Failed to resume task scheduling: %@"
+ "[%{public}s] Finished submitting metrics for batch"
+ "[%{public}s] Resuming task scheduling to clear client offset"
+ "[%{public}s] Submitting metrics for batch"
+ "[%{public}s] Task is not eligible to run because it has higher priority work"
+ "[%{public}s] Task is not eligible to run because it is blocked by low power mode"
+ "[%{public}s] Task is not eligible to run because it is throttled"
+ "[%{public}s] Task is not eligible to run because it was cancelled"
+ "[%{public}s] Task is still allowed to proceed"
+ "[%{public}s] Task was cancelled, skipping remaining work"
+ "[%{public}s] Updating task request with reason: %s"
+ "[%{public}s] blocked due to %{public}s, deferral status: %{public}s, expiring with infinite delay: %{bool,public}d"
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchContext:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:isBIAMessage:biaReferenceID:completionBlock:"
+ "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchID:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:isBIAMessage:biaReferenceID:completionBlock:"
+ "_canAttemptNextWriteBatchWithRecurseCount:"
+ "_priorDefinitionForMessageItem:"
+ "_singleBatchOfRecordsToWriteWithFilter:limit:error:"
+ "cancellingTask"
+ "clientInitiatedDeferral"
+ "deferralStatus"
+ "definitionItemForCustomAcknowledgement:"
+ "md-attachment-upload-recurse-limit"
+ "mostRecentPriorCustomAcknowledgementForItem:definitionItem:fetchAssociatedItemsBlock:"
+ "notDeferred"
+ "priorItemForCustomAcknowledgement:"
+ "purgeFileTransferFromDisk:reply:"
+ "purgeTransfer:"
+ "q24@?0@\"IMItem\"8@\"IMItem\"16"
+ "resumeScheduling:error:"
+ "scheduleAfter"
+ "schedulerInitiatedDeferral"
+ "v268@0:8@\"IMMessageItem\"16@\"IMDChat\"24@\"IMDAccount\"32@\"NSData\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSArray\"72@\"NSString\"80@\"NSString\"88B96B100B104@\"NSDictionary\"108B116B120@\"NSNumber\"124@\"NSDictionary\"132@\"NSDictionary\"140@\"NSArray\"148@\"NSDictionary\"156@\"NSString\"164@\"NSString\"172@\"NSString\"180@\"NSString\"188@\"IDSService\"196@204B212B216B220B224B228q232q240B248@\"NSString\"252@?<v@?>260"
+ "v268@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104@108B116B120@124@132@140@148@156@164@172@180@188@196@204B212B216B220B224B228q232q240B248@252@?260"
+ "writeAddChoiceSummaryForMessage:sender:"
- "@44@0:8Q16q24i32^@36"
- "Deleting previous custom acknowledgments failed with error: %@"
- "The transfer we want to remove does not exist at its local path -- transfer (%@) local path (%@)"
- "There was an error trying to remove the file: %@"
- "We are removing the file at path: %@ for transfer: %@"
- "We attempted to delete a path that was not safe to delete for guid: %@ path: %@"
- "We successfully removed the file - setting the transfer state to waiting for accept"
- "[%{public}s] Failed to expire: %@"
- "[%{public}s] Ignoring request to resume task because it has higher priority work"
- "[%{public}s] Ignoring request to resume task because it is blocked by low power mode"
- "[%{public}s] Ignoring request to resume task because it is throttled"
- "[%{public}s] Resume request for persistent task is allowed to proceed"
- "[%{public}s] Updating task request"
- "[%{public}s] blocked due to %{public}s, expiring with infinite delay"
- "[%{public}s] finished batch, has more work to do, but blocked by low power mode"
- "[%{public}s] finished batch, has more work to do, but has higher priority work"
- "[%{public}s] finished batch, has more work to do, but is cancelled"
- "[%{public}s] setting expired with retry after 300s"
- "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchContext:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:completionBlock:"
- "_blastDoorProcessingWithIMMessageItem:chat:account:fromToken:fromIDSID:fromIdentifier:toIdentifier:participants:groupName:groupID:isFromMe:isLastFromStorage:isFromStorage:batchID:hideLockScreenNotification:wantsCheckpointing:needsDeliveryReceipt:messageBalloonPayloadAttachmentDictionary:inlineAttachments:attributionInfoArray:nicknameDictionary:availabilityVerificationRecipientChannelIDPrefix:availabilityVerificationRecipientEncryptionValidationToken:availabilityOffGridRecipientSubscriptionValidationToken:availabilityOffGridRecipientEncryptionValidationToken:idsService:messageContext:isFromTrustedSender:isFromSnapTrustedSender:wasContextUsed:isBlackholed:shouldTrackForRequery:isFiltered:spamDetectionSource:completionBlock:"
- "batchOfRecordsToWriteWithFilter:limit:recurseCount:error:"
- "chat:groupIDUpdated:"
- "chat:originalGroupIDUpdated:"
- "v256@0:8@\"IMMessageItem\"16@\"IMDChat\"24@\"IMDAccount\"32@\"NSData\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSArray\"72@\"NSString\"80@\"NSString\"88B96B100B104@\"NSDictionary\"108B116B120@\"NSNumber\"124@\"NSDictionary\"132@\"NSDictionary\"140@\"NSArray\"148@\"NSDictionary\"156@\"NSString\"164@\"NSString\"172@\"NSString\"180@\"NSString\"188@\"IDSService\"196@204B212B216B220B224B228q232q240@?<v@?>248"
- "v256@0:8@16@24@32@40@48@56@64@72@80@88B96B100B104@108B116B120@124@132@140@148@156@164@172@180@188@196@204B212B216B220B224B228q232q240@?248"
- "wasManuallySuspended"

```
