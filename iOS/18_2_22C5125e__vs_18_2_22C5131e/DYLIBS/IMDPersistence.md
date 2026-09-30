## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.300.158.2.2
-  __TEXT.__text: 0x1188a0
-  __TEXT.__auth_stubs: 0x26d0
-  __TEXT.__objc_methlist: 0x379c
-  __TEXT.__const: 0xb4a
-  __TEXT.__cstring: 0x39531
-  __TEXT.__oslogstring: 0x19e05
-  __TEXT.__gcc_except_tab: 0xd480
-  __TEXT.__ustring: 0x430
+1402.300.164.2.2
+  __TEXT.__text: 0x11a26c
+  __TEXT.__auth_stubs: 0x2760
+  __TEXT.__objc_methlist: 0x37cc
+  __TEXT.__const: 0xb5a
+  __TEXT.__cstring: 0x395a1
+  __TEXT.__oslogstring: 0x1a065
+  __TEXT.__gcc_except_tab: 0xe488
+  __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x2a4
-  __TEXT.__swift5_typeref: 0x206
+  __TEXT.__swift5_typeref: 0x1fc
   __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_fieldmd: 0xe4
   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4de0
+  __TEXT.__unwind_info: 0x4e10
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xa93
-  __TEXT.__objc_methname: 0x10395
-  __TEXT.__objc_methtype: 0x236d
-  __TEXT.__objc_stubs: 0xd9e0
-  __DATA_CONST.__got: 0xe78
-  __DATA_CONST.__const: 0x10dd0
+  __TEXT.__objc_methname: 0x1056c
+  __TEXT.__objc_methtype: 0x23ae
+  __TEXT.__objc_stubs: 0xdc00
+  __DATA_CONST.__got: 0xe88
+  __DATA_CONST.__const: 0x10f60
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3af0
+  __DATA_CONST.__objc_selrefs: 0x3b58
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x1378
+  __AUTH_CONST.__auth_got: 0x13c0
   __AUTH_CONST.__auth_ptr: 0xd0
   __AUTH_CONST.__const: 0x1a48
-  __AUTH_CONST.__cfstring: 0x10c20
-  __AUTH_CONST.__objc_const: 0x6840
+  __AUTH_CONST.__cfstring: 0x10ca0
+  __AUTH_CONST.__objc_const: 0x6880
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x308
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0xac0
-  __DATA.__bss: 0x490
+  __DATA.__bss: 0x4a0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x17a0
-  __DATA_DIRTY.__data: 0xe98
-  __DATA_DIRTY.__bss: 0x588
+  __DATA_DIRTY.__data: 0xeb8
+  __DATA_DIRTY.__bss: 0x580
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4517
-  Symbols:   2342
-  CStrings:  7402
+  Functions: 4524
+  Symbols:   2354
+  CStrings:  7434
 
Symbols:
+ _CFAutorelease
+ _IMDCoreSpotlightReindexAttachment
+ _IMDMigrateTo18017
+ _IMFileTransferAttributionInfoHasLegacyState
+ _IMFileTransferPreviewGenerationStateWithStoredState
+ _IMIsSupportedUTIType
+ _IMShouldAllowInteractionlessUsageOfUTITypeWithPreviewGenerationState
+ _OBJC_CLASS_$_IMCoreSpotlightRejectedItem
+ __os_activity_create
+ __os_activity_current
+ _os_activity_scope_enter
+ _os_activity_scope_leave
CStrings:
+ "-[IMDCoreSpotlightManager _indexSearchableItems:rejectedItems:clientState:lastIndexedRowID:messagesInBatch:messagesWithItemsGeneratedCount:batchSize:lastBatch:withIndex:reason:]"
+ "@\"NSArray\"60@0:8@\"CSSearchableItemAttributeSet\"16@\"NSDictionary\"24@\"NSDictionary\"32B40@\"IMDSpotlightIndexerTimingProfiler\"44@\"NSMutableArray\"52"
+ "@36@0:8@16B24@28"
+ "@44@0:8@16@24B32@36"
+ "@60@0:8@16@24@32B40@44@52"
+ "@64@0:8^Q16^Q24^Q32Q40@48@56"
+ "Handled message %!l(MISSING)d/%!@(MISSING) from (%!d(MISSING): %!@(MISSING)) wantsReply %!@(MISSING)"
+ "Handling message %!l(MISSING)d/%!@(MISSING) from (%!d(MISSING): %!@(MISSING)) wantsReply %!@(MISSING)"
+ "IMDCoreSpotlightIndexSearchableItems: failed to delete %!l(MISSING)d items for reason %!@(MISSING) due to %!@(MISSING)"
+ "Migrating attachment GUID %!@(MISSING) to new preview generation state"
+ "Not donating attachment to CoreSpotlight because %!{(MISSING)public}@. attachmentGUID: %!@(MISSING) UTI: %!@(MISSING)"
+ "ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description, preview_generation_state "
+ "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description, preview_generation_state FROM attachment "
+ "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description, preview_generation_state FROM attachment WHERE ck_sync_state == 1 AND transfer_state == 5 AND ck_server_change_token_blob != '' AND ck_server_change_token_blob NOT NULL ORDER BY created_date ASC LIMIT ? OFFSET ?;"
+ "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description, preview_generation_state FROM attachment WHERE filename LIKE ?;"
+ "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description, preview_generation_state FROM attachment WHERE guid = ? ORDER BY ROWID DESC;"
+ "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description, preview_generation_state FROM attachment WHERE original_guid = ? ORDER BY ROWID DESC;"
+ "TB,R,N,GisHidden"
+ "Timed out indexing %!@(MISSING), but an override is set, not exiting!"
+ "UPDATE attachment SET preview_generation_state = 3;"
+ "_copyNewSearchableIndexesForMessagesWithLastRowID:messageRecordCount:messagesWithItemsGeneratedCount:batchSize:timingCollection:rejectedItems:"
+ "_indexSearchableItems:rejectedItems:clientState:lastIndexedRowID:messagesInBatch:messagesWithItemsGeneratedCount:batchSize:lastBatch:withIndex:reason:"
+ "_write"
+ "_writeIfNeededForPreviewGenerationStateMigration"
+ "auxiliaryItemsForPrimaryAttributes:withItem:chat:isReindexing:timingProfiler:rejectedItems:"
+ "com.apple.messages.IMDPCommandDispatcher"
+ "deleted %!l(MISSING)d items for reason %!@(MISSING)"
+ "exitOnIndexingTimeout"
+ "extendedSpotlightTimeoutSeconds"
+ "hidden"
+ "history query %!l(MISSING)u / %!l(MISSING)u - %!@(MISSING)"
+ "history query %!l(MISSING)u / %!l(MISSING)u - %!@(MISSING) - in operation"
+ "history query %!l(MISSING)u / %!l(MISSING)u - %!@(MISSING) - in operation bind"
+ "history query %!l(MISSING)u / %!l(MISSING)u - %!@(MISSING) - in operation results"
+ "initWithDomain:identifier:reason:"
+ "isHidden"
+ "newSearchableItemsForMessage:reindexing:rejectedItems:"
+ "newSearchableItemsForMessageGUID:reindexing:rejectedItems:"
+ "newSearchableItemsForMessageItemDictionary:chatDictionary:reindexing:rejectedItems:"
+ "not deleting %!l(MISSING)d items from Spotlight due to override"
+ "previewAttributedStringWithMessageSummaryInfo:isAdaptiveImageGlyphProvider:isCommSafetySensitiveProvider:adaptiveImageGlyphProvider:senderDisplayName:isFromMe:effectString:"
+ "previewGenerationState"
+ "preview_generation_state"
+ "proposedIdentifier"
+ "replaceCharactersInRange:withAttributedString:"
+ "spotlightTimeoutSeconds"
+ "v32@?0@\"NSNumber\"8@\"NSMutableArray\"16^B24"
+ "v92@0:8@16@24@32Q40Q48Q56Q64B72@76q84"
+ "void IMDAttachmentRecordBulkUpdate(IMDAttachmentRecordRef, CFStringRef, int64_t, int64_t, CFStringRef, CFStringRef, CFStringRef, CFStringRef, int64_t, Boolean, int64_t, CFDictionaryRef, Boolean, CFDictionaryRef, CFDictionaryRef, Boolean, int64_t, CFDataRef, CFStringRef, CFStringRef, int64_t, CFStringRef, CFStringRef, int64_t)"
+ "withdrawDonationsForFailedPreviewGenerations"
- "-[IMDCoreSpotlightManager _indexSearchableItems:clientState:lastIndexedRowID:messagesInBatch:messagesWithItemsGeneratedCount:batchSize:lastBatch:withIndex:reason:]"
- "@\"NSArray\"52@0:8@\"CSSearchableItemAttributeSet\"16@\"NSDictionary\"24@\"NSDictionary\"32B40@\"IMDSpotlightIndexerTimingProfiler\"44"
- "@52@0:8@16@24@32B40@44"
- "@56@0:8^Q16^Q24^Q32Q40@48"
- "CFArrayRef IMDMessageRecordCopyMessagesWithChatIdentifiersOnServicesUpToGUIDOrLimitWithOptionalThreadIdentifier(CFArrayRef, CFArrayRef, CFStringRef, CFStringRef, Boolean, Boolean, int64_t)_block_invoke_2"
- "Not donating attachment to CoreSpotlight because preview generation failed. attachmentGUID: %!@(MISSING)"
- "ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description "
- "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description FROM attachment "
- "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description FROM attachment WHERE ck_sync_state == 1 AND transfer_state == 5 AND ck_server_change_token_blob != '' AND ck_server_change_token_blob NOT NULL ORDER BY created_date ASC LIMIT ? OFFSET ?;"
- "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description FROM attachment WHERE filename LIKE ?;"
- "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description FROM attachment WHERE guid = ? ORDER BY ROWID DESC;"
- "SELECT ROWID, guid, created_date, start_date, filename, uti, mime_type, transfer_state, is_outgoing, user_info, transfer_name, total_bytes, is_sticker, sticker_user_info, attribution_info, hide_attachment, ck_sync_state, ck_server_change_token_blob, ck_record_id, original_guid, is_commsafety_sensitive, emoji_image_content_identifier, emoji_image_short_description FROM attachment WHERE original_guid = ? ORDER BY ROWID DESC;"
- "_copyNewSearchableIndexesForMessagesWithLastRowID:messageRecordCount:messagesWithItemsGeneratedCount:batchSize:timingCollection:"
- "_indexSearchableItems:clientState:lastIndexedRowID:messagesInBatch:messagesWithItemsGeneratedCount:batchSize:lastBatch:withIndex:reason:"
- "auxiliaryItemsForPrimaryAttributes:withItem:chat:isReindexing:timingProfiler:"
- "newSearchableItemsForMessage:reindexing:"
- "newSearchableItemsForMessageGUID:reindexing:"
- "newSearchableItemsForMessageItemDictionary:chatDictionary:reindexing:"
- "previewAttributedStringWithMessageSummaryInfo:isAdaptiveImageGlyphProvider:adaptiveImageGlyphProvider:senderDisplayName:isFromMe:effectString:"
- "v84@0:8@16@24Q32Q40Q48Q56B64@68q76"
- "void IMDAttachmentRecordBulkUpdate(IMDAttachmentRecordRef, CFStringRef, int64_t, int64_t, CFStringRef, CFStringRef, CFStringRef, CFStringRef, int64_t, Boolean, int64_t, CFDictionaryRef, Boolean, CFDictionaryRef, CFDictionaryRef, Boolean, int64_t, CFDataRef, CFStringRef, CFStringRef, int64_t, CFStringRef, CFStringRef)"

```
