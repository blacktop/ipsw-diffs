## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-  __TEXT.__text: 0x2661d0
-  __TEXT.__auth_stubs: 0x4f40
-  __TEXT.__objc_methlist: 0x809c
+  __TEXT.__text: 0x267aac
+  __TEXT.__auth_stubs: 0x4f60
+  __TEXT.__objc_methlist: 0x817c
   __TEXT.__const: 0xc848
-  __TEXT.__cstring: 0x490f4
-  __TEXT.__oslogstring: 0x1ea76
-  __TEXT.__gcc_except_tab: 0xb758
+  __TEXT.__cstring: 0x49244
+  __TEXT.__oslogstring: 0x1ebb6
+  __TEXT.__gcc_except_tab: 0xb7e4
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
   __TEXT.__swift5_typeref: 0x3f8a

   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x95e8
-  __TEXT.__eh_frame: 0x8a80
+  __TEXT.__unwind_info: 0x9640
+  __TEXT.__eh_frame: 0x8ab0
   __TEXT.__objc_classname: 0x28fa
-  __TEXT.__objc_methname: 0x1bed5
-  __TEXT.__objc_methtype: 0x4667
-  __TEXT.__objc_stubs: 0x14000
-  __DATA_CONST.__got: 0x1920
-  __DATA_CONST.__const: 0x8278
+  __TEXT.__objc_methname: 0x1c495
+  __TEXT.__objc_methtype: 0x4627
+  __TEXT.__objc_stubs: 0x14240
+  __DATA_CONST.__got: 0x1928
+  __DATA_CONST.__const: 0x82d0
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5908
+  __DATA_CONST.__objc_selrefs: 0x5998
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x300
-  __AUTH_CONST.__auth_got: 0x27b0
-  __AUTH_CONST.__const: 0xad90
-  __AUTH_CONST.__cfstring: 0x124e0
-  __AUTH_CONST.__objc_const: 0x119f0
+  __AUTH_CONST.__auth_got: 0x27c0
+  __AUTH_CONST.__const: 0xadc8
+  __AUTH_CONST.__cfstring: 0x12580
+  __AUTH_CONST.__objc_const: 0x11b48
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x22b0
   __AUTH.__data: 0x4c30
-  __DATA.__objc_ivar: 0x4d0
+  __DATA.__objc_ivar: 0x4ec
   __DATA.__data: 0x34c8
   __DATA.__bss: 0xae98
   __DATA.__common: 0x210

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11769
-  Symbols:   2664
-  CStrings:  12905
+  Functions: 11792
+  Symbols:   2667
+  CStrings:  12951
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __xpc_type_array
+ _xpc_array_get_int64
+ _xpc_int64_create
CStrings:
+ "!$"
+ "@96@0:8B16q20@28Q36B44B48B52B56@60B68@72@80@88"
+ "DELETE FROM unsynced_removed_recoverable_messages WHERE ROWID IN"
+ "INSERT INTO recoverable_message_part (chat_id, message_id, part_index, delete_date, part_text, ck_sync_state)   SELECT cmj.chat_id, cmj.message_id, ?, ?, ?, ?   FROM chat_message_join AS cmj   JOIN message AS m   ON m.ROWID = cmj.message_id AND m.guid = ?;"
+ "INSERT OR REPLACE INTO chat_recoverable_message_join (chat_id, message_id, delete_date) SELECT chat_id, message_id, ? FROM chat_message_join WHERE message_date < ? AND chat_id IN ("
+ "Overriding recently deleted expiration to %lld days based on default com.apple.Messages days-to-deleted-cleanup"
+ "Recently Deleted | Failed to clear tombstones by ROWIDs: %@"
+ "Recently Deleted | Finished clearing %lu specific recoverable message tombstones by ROWID"
+ "Recently Deleted | Will begin clearing %lu specific recoverable message tombstones by ROWID"
+ "Recently Deleted | Will begin permanently deleting recoverable messages for %lu chatGUIDs, beforeDate: %@"
+ "SELECT urrm.chat_guid, urrm.message_guid, urrm.part_index, urrm.ROWID FROM unsynced_removed_recoverable_messages AS urrm LIMIT ?;"
+ "T@\"NSDate\",&,N,V_controllerEntryDate"
+ "T@\"NSDate\",&,N,V_jobStartDate"
+ "T@\"NSDate\",&,N,V_jobSubmissionDate"
+ "T@\"NSDate\",&,N,V_spotlightHeldStartDate"
+ "T@\"NSDictionary\",C,N,V_itemGenerationDurationsByIdentifier"
+ "T@\"NSMutableDictionary\",R,N,V_itemGenerationDurationsByIdentifier"
+ "Td,N,V_spotlightHeldDuration"
+ "UPDATE message SET message_summary_info = NULL, ck_sync_state = 0 WHERE length(message_summary_info) >  ? "
+ "_controllerEntryDate"
+ "_deleteSearchableItemsWithIdentifiers:withContext:completionHandler:"
+ "_detectedClientStateMismatchWithError:spotlightClientState:spotlightClientStateData:completionBlock:"
+ "_initForReindexing:reason:bgstLane:migrationRequirements:preflight:ignoreRejections:ignoreThrottle:forceDeferral:laneOverride:needsTimeSensitiveEvaluation:additionalReasons:chatMetadata:controllerEntryDate:"
+ "_itemGenerationDurationsByIdentifier"
+ "_jobStartDate"
+ "_jobSubmissionDate"
+ "_loadClientStateFromDefaultsWithData:"
+ "_spotlightHeldDuration"
+ "_spotlightHeldStartDate"
+ "_stampControllerEntryDateOnContext:"
+ "_submitIndexingMetricWithError:"
+ "clearRecoverableMessageTombStonesForRowIDs:"
+ "controllerEntryDate"
+ "days-to-deleted-cleanup"
+ "enterScrutiny"
+ "fromSync"
+ "handleIMDMessageRecordClearUnsyncedRemovedRecoverableMessagesForRowIDs_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
+ "itemGenerationDurationsByIdentifier"
+ "jobStartDate"
+ "jobSubmissionDate"
+ "messagesAppDomain"
+ "metadataAttributesInit"
+ "setControllerEntryDate:"
+ "setItemGenerationDurationsByIdentifier:"
+ "setJobStartDate:"
+ "setJobSubmissionDate:"
+ "setSpotlightHeldDuration:"
+ "setSpotlightHeldStartDate:"
+ "spotlightHeldDuration"
+ "spotlightHeldStartDate"
+ "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:fromSync:"
+ "tombstoneRowID"
+ "trackSpotlightClientStateMismatchWithStoredClientState:storedClientStateWasEqual:"
+ "trackSpotlightDonationWithError:durationSeconds:spotlightDonationDuration:itemGenerationDuration:donationDuration:queueDuration:reason:migrationRequirements:runningViaDAS:persistentTaskLane:isPatch:isReindexing:isCritical:attachmentCount:chatCount:messageCount:deletedItemCount:rejectedCount:deferralDepth:"
+ "trackSpotlightIndexRebuildInitiatedWithReason:"
+ "v28@?0@\"IMSpotlightClientState\"8@\"NSData\"16B24"
+ "v32@?0@\"IMSpotlightClientState\"8@\"NSData\"16@\"NSError\"24"
+ "v44@0:8@\"NSAttributedString\"16@\"NSString\"24@\"NSDate\"32B40"
- "!#"
- "@88@0:8B16q20@28Q36B44B48B52B56@60B68@72@80"
- "INSERT INTO recoverable_message_part (chat_id, message_id, part_index, delete_date, part_text, ck_sync_state)   SELECT cmj.chat_id, cmj.message_id, ?, ?, ?, 0   FROM chat_message_join AS cmj   JOIN message AS m   ON m.ROWID = cmj.message_id AND m.guid = ?;"
- "INSERT OR REPLACE INTO chat_recoverable_message_join (chat_id, message_id, delete_date) SELECT chat_id, message_id, message_date FROM chat_message_join WHERE message_date < ? AND chat_id IN ("
- "Recently Deleted | Will begin permanently deleting recoverable messages for %lu chatGUIDs"
- "SELECT urrm.chat_guid, urrm.message_guid, urrm.part_index FROM unsynced_removed_recoverable_messages AS urrm LIMIT ?;"
- "[txn-%@] Failed to fetch serialize client state: %@"
- "_deleteSearchableItemsWithIdentifiers:withReason:completionHandler:"
- "_detectedClientStateMismatchWithError:spotlightClientState:completionBlock:"
- "_initForReindexing:reason:bgstLane:migrationRequirements:preflight:ignoreRejections:ignoreThrottle:forceDeferral:laneOverride:needsTimeSensitiveEvaluation:additionalReasons:chatMetadata:"
- "_loadClientStateFromDefaults"
- "deleteAttachmentGUIDs:reason:completionHandler:"
- "deleteMessageGUIDs:reason:completionHandler:"
- "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:"
- "v20@?0@\"IMSpotlightClientState\"8B16"
- "v40@0:8@\"NSArray\"16q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSAttributedString\"16@\"NSString\"24@\"NSDate\"32"

```
