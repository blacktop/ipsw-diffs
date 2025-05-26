## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1262.400.41.2.3
-  __TEXT.__text: 0xfada8
-  __TEXT.__auth_stubs: 0x23d0
-  __TEXT.__objc_methlist: 0x2d74
+1262.500.151.2.4
+  __TEXT.__text: 0xfcf4c
+  __TEXT.__auth_stubs: 0x2430
+  __TEXT.__objc_methlist: 0x2d8c
   __TEXT.__const: 0x6aa
-  __TEXT.__cstring: 0x49eb1
-  __TEXT.__oslogstring: 0x17d6c
-  __TEXT.__gcc_except_tab: 0x9414
+  __TEXT.__cstring: 0x4a681
+  __TEXT.__oslogstring: 0x17f8d
+  __TEXT.__gcc_except_tab: 0x9468
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
-  __TEXT.__swift5_typeref: 0x1b4
+  __TEXT.__swift5_typeref: 0x1ce
   __TEXT.__constg_swiftt: 0x140
   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_reflstr: 0x4f
-  __TEXT.__unwind_info: 0x45a0
-  __TEXT.__eh_frame: 0x78
+  __TEXT.__unwind_info: 0x45d4
+  __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x870
-  __TEXT.__objc_methname: 0xd63d
-  __TEXT.__objc_methtype: 0x1c4a
-  __TEXT.__objc_stubs: 0xb600
-  __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__const: 0xfd00
+  __TEXT.__objc_methname: 0xd63b
+  __TEXT.__objc_methtype: 0x1c1d
+  __TEXT.__objc_stubs: 0xb6c0
+  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__const: 0xfc48
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3f30
-  __DATA_CONST.__objc_selrefs: 0x3190
+  __DATA_CONST.__objc_const: 0x3f20
+  __DATA_CONST.__objc_selrefs: 0x31a8
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_classrefs: 0x628
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__cfstring: 0xfe20
+  __AUTH_CONST.__cfstring: 0xff80
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__const: 0xb80
+  __AUTH_CONST.__const: 0xe58
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x11f8
+  __AUTH_CONST.__auth_got: 0x1228
   __AUTH.__objc_data: 0xc0
   __AUTH.__data: 0x30
-  __DATA.__objc_protorefs: 0x58
-  __DATA.__objc_classrefs: 0x628
-  __DATA.__objc_superrefs: 0xc8
-  __DATA.__objc_ivar: 0x14c
-  __DATA.__data: 0x8b0
-  __DATA.__bss: 0x2f0
+  __DATA.__objc_ivar: 0x148
+  __DATA.__data: 0x8e0
+  __DATA.__bss: 0x2f8
   __DATA.__common: 0x11
-  __DATA_DIRTY.__const: 0x1828
+  __DATA_DIRTY.__const: 0x15e8
   __DATA_DIRTY.__objc_const: 0x1668
   __DATA_DIRTY.__objc_data: 0x15a0
   __DATA_DIRTY.__data: 0x298

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4153
-  Symbols:   2158
-  CStrings:  6677
+  Functions: 4179
+  Symbols:   2173
+  CStrings:  6710
 
Symbols:
+ _IMDAttachmentRecordMarkAttachmentWithROWIDWithSyncState
+ _IMDMessageRecordCalculateTotalCounts
+ _IMDMessageRecordCloudKitStatisticUnresolvedAttachmentCountKey
+ _IMDMessageRecordCloudKitStatisticUnresolvedChatCountKey
+ _IMDMessageRecordCloudKitStatisticUnresolvedCountKey
+ _IMDMessageRecordCloudKitStatisticUnresolvedMessageCountKey
+ _IMDMessageRecordCloudKitStatisticUnresolvedRecoverableMessageCountKey
+ _IMDMigrateTo17010
+ _IMDRemoveCoreRecentsRecordForMessageGUIDs
+ _IMMessagePropertyGUID
+ _IMMessagePropertyHasDataDetectorResults
+ _OBJC_CLASS_$_IMCoreRecentsMetadataBuilder
+ ___XPCServerIMDAttachmentRecordMarkAttachmentWithROWIDWithSyncState_IPCAction
+ ___XPCServerIMDMessageRecordCalculateTotalCounts_IPCAction
+ ___syncXPCIMDAttachmentRecordMarkAttachmentWithROWIDWithSyncState_IPCAction
+ ___syncXPCIMDMessageRecordCalculateTotalCounts_IPCAction
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _malloc
- _IMDAttachmentRecordMarkAttachmentWithROWIDAsFailedToUploadToCloudKit
- __ConstructMetaDataDictionaryForCoreRecents
- ___XPCServerIMDAttachmentRecordMarkAttachmentWithROWIDAsFailedToUploadToCloudKit_IPCAction
- ___syncXPCIMDAttachmentRecordMarkAttachmentWithROWIDAsFailedToUploadToCloudKit_IPCAction
CStrings:
+ "%K = %@ AND %K IN %@"
+ "'"
+ "******* Notification work done on wrong queue, please file a radar *******"
+ "@40@0:8@16B24B28^B32"
+ "@40@0:8@16q24B32B36"
+ "@56@0:8@16@24@32B40B44^B48"
+ "Attempting to remove messages from CoreRecents. guids={%@}"
+ "Calculated sync stats in %f seconds. All Records: %lld of %lld, %lld remaining, %lld unresolved. Messages : %lld of %lld, %lld remaining, %lld unresolved. Chats : %lld of %lld, %lld remaining, %lld unresolved. Attachments : %lld of %lld, %lld remaining, %lld unresolved."
+ "Calculated total counts in %f seconds. All Records: %lld, Messages: %lld, Chats: %lld, Attachments: %lld, RecoverableMessages: %lld"
+ "Can't construct Array with count < 0"
+ "Coordinated Alerts -- this is not the most active device, suppressing the screen from lighting up and not playing sound for message"
+ "Expected dictionary of record totals is nil"
+ "Expecting statistics dictionary to calculate unresolved counts, but found nil, returning 0"
+ "Fatal error"
+ "IMDAttachmentRecordMarkAttachmentWithROWIDWithSyncState_IPCAction"
+ "IMDCoreRecentsClientQueue"
+ "IMDCoreSpotlight_CoreRecents"
+ "IMDMessageRecordCalculateTotalCounts loaded totals: %@"
+ "IMDNotificationRequestQueue"
+ "IMDSharingActiveDeviceQueue"
+ "Insufficient space allocated to copy string contents"
+ "OFF"
+ "ON"
+ "Populating sound and display sound %@ ignoreDND %@ suppress screen light up %@"
+ "Query: Copy Duplicate Group Chats"
+ "Queuing retraction of all delivered notifications, as we had nothing unread."
+ "Recent messages remove failed with error %@."
+ "Retracting of all delivered notifications, as we had nothing unread."
+ "SELECT COUNT(*) FROM attachment;"
+ "SELECT COUNT(*) FROM chat;"
+ "SELECT COUNT(*) FROM message;"
+ "SELECT ROWID, guid, style, state, account_id, properties, chat_identifier, service_name, room_name, account_login, is_archived, last_addressed_handle, display_name, group_id, is_filtered, successful_query, engram_id, server_change_token, ck_sync_state, original_group_id, last_read_message_timestamp, cloudkit_record_id, last_addressed_sim_id, is_blackholed, syndication_date, syndication_type, is_recovered, is_deleting_incoming_messages    FROM chat c   WHERE style = 43   AND (SELECT count(*) FROM chat cdupe WHERE cdupe.group_id = c.group_id AND cdupe.service_name = c.service_name) > 1   LIMIT ?"
+ "SELECT SUM(total_count) AS total_count FROM ( SELECT COUNT(*) AS total_count FROM chat_recoverable_message_join AS crmj JOIN chat AS c ON c.ROWID = crmj.chat_id JOIN message AS m ON m.ROWID = crmj.message_id UNION ALL SELECT COUNT(1) AS total_count FROM recoverable_message_part AS rmp JOIN chat AS c ON c.ROWID = rmp.chat_id JOIN message AS m ON m.ROWID = rmp.message_id);"
+ "Successfully removed %ld messages from CoreRecents."
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "This method should not be called %@ the notification queue because it may lead to long blocking of other requests."
+ "UPDATE chat SET service_name = substr(guid,1,instr(guid,\";\")-1)  WHERE service_name IS NULL OR service_name == \"\";"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Withdrawing message notifications for message guids %@"
+ "_IMDNotificationRequestQueue"
+ "__postNotificationRequests:isMostActiveDevice:"
+ "__postNotifications"
+ "_generateNotificationRequestForMessageRecord:isUrgentMessageTrigger:isCarouselUITriggered:shouldAdvanceLastAlertedMessageDate:"
+ "_generateNotificationRequestForMessageRecord:messageDictionary:chatDictionary:isUrgentMessageTrigger:isCarouselUITriggered:shouldAdvanceLastAlertedMessageDate:"
+ "_isMostActiveDevice"
+ "_messageShouldBeSpoken:chatDictionary:"
+ "_populateSoundAndDisplayActivationForNotificationContent:chatDictionary:messageDictionary:"
+ "_populateTimeSensitiveOrCriticalForNotificationContent:chatDictionary:messageDictionary:"
+ "_postNotificationRequests:"
+ "_postNotificationRequests:isMostActiveDevice:"
+ "_requestForNonMostActiveDeviceRequest:"
+ "_shouldPostNotificationRequest:withCurrentlyPostedNotifications:"
+ "_userNotificationsForFailedDeliveryMessageRecords:isCarouselUITriggered:"
+ "_userNotificationsForMessageRecords:newerThanDate:isUrgentMessageTrigger:isCarouselUITriggered:"
+ "com.apple.Messages"
+ "copyDuplicateGroupChatRecordsWithLimit:"
+ "corerecents:reference-url"
+ "deliveredNotifications"
+ "handleIMDChatRecordCopyDuplicateGroupChatRecords_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
+ "invalid Collection: less than 'count' elements in collection"
+ "logger"
+ "metadataDictionaryForMessageID:senderID:date:"
+ "referenceURLForMessageGUID:"
+ "syncState"
+ "update attachment set ck_sync_state = ? where rowid=?"
+ "v32@?0@\"NSString\"8@\"UNNotificationContent\"16^B24"
- "7"
- "@44@0:8@16B24B28B32^B36"
- "@60@0:8@16@24@32B40B44B48^B52"
- "Advancing last failed message date to %@ but not posting the notification"
- "B36@0:8@16@24B32"
- "CRAddressKindEmail"
- "CRAddressKindPhoneNumber"
- "CRRecentContactMetadataEventTime"
- "CRRecentContactMetadataFrom"
- "CRRecentContactMetadataFromAddress"
- "CRRecentContactMetadataFromAddressKind"
- "CRRecentContactMetadataReferenceURL"
- "Calculated sync stats in %f seconds. All Records: %lld of %lld, %lld remaining. Messages : %lld of %lld, %lld remaining. Chats : %lld of %lld, %lld remaining. Attachments : %lld of %lld, %lld remaining."
- "Coordinated Alerts -- this is not the most active device, suppressing the screen from lighting up and not playing sound for message %@"
- "CoordinatedAlertQueue"
- "CoreRecents metadata:%@"
- "DataDetectors"
- "Finished adding notification request %@ for failed delivery with error %@"
- "Found last processing date [%lld] later then last alerted date: [%lld]"
- "IMDAttachmentRecordMarkAttachmentWithROWIDAsFailedToUploadToCloudKit_IPCAction"
- "Not posting SharePlay notification because shouldPost was evaluated to NO"
- "Populating sound and display isMostActive %@ sound %@ ignoreDND %@ suppress screen light up %@"
- "__postNotificationsIsMostActiveDevice:"
- "_coalescePostNotifications"
- "_generateNotificationRequestForMessageRecord:isUrgentMessageTrigger:isCarouselUITriggered:isMostActive:shouldAdvanceLastAlertedMessageDate:"
- "_generateNotificationRequestForMessageRecord:messageDictionary:chatDictionary:isUrgentMessageTrigger:isCarouselUITriggered:isMostActive:shouldAdvanceLastAlertedMessageDate:"
- "_isMostActiveDeviceWithCompletionBlock:"
- "_lastProcessingMessageDate"
- "_messageShouldBeSpoken:chatDictionary:isMostActive:"
- "_populateSoundAndDisplayActivationForNotificationContent:chatDictionary:messageDictionary:isMostActive:"
- "_populateTimeSensitiveOrCriticalForNotificationContent:chatDictionary:messageDictionary:isMostActive:"
- "_postNotifications"
- "_proceedMostActiveDevice:isBlockCalled:completionHandler:"
- "_registerUserNotificationsForFailedDeliveryMessageRecords:isCarouselUITriggered:"
- "_registerUserNotificationsForMessageRecords:newerThanDate:isUrgentMessageTrigger:isCarouselUITriggered:isMostActiveDevice:"
- "_shouldPostNotificationRequest:withCompletionHandler:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "getDeliveredNotificationsWithCompletionHandler:"
- "lastProcessingMessageDate"
- "performSelector:withObject:afterDelay:"
- "setLastProcessingMessageDate:"
- "setting last processing message date to %@"
- "sms:/open?message-guid=%@"
- "update attachment set ck_sync_state = 2 where rowid=?"
- "v36@0:8B16^B20@?28"
- "v44@0:8@16q24B32B36B40"

```
