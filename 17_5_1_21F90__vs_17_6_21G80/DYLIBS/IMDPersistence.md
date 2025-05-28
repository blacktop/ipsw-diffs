## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1262.600.61.2.9
-  __TEXT.__text: 0xfe6a0
-  __TEXT.__auth_stubs: 0x24f0
-  __TEXT.__objc_methlist: 0x2dfc
+1262.700.71.2.1
+  __TEXT.__text: 0x100d10
+  __TEXT.__auth_stubs: 0x2530
+  __TEXT.__objc_methlist: 0x2f1c
   __TEXT.__const: 0x6ea
-  __TEXT.__cstring: 0x4aa61
-  __TEXT.__oslogstring: 0x17fae
-  __TEXT.__gcc_except_tab: 0x9468
+  __TEXT.__cstring: 0x4ad11
+  __TEXT.__oslogstring: 0x1813b
+  __TEXT.__gcc_except_tab: 0x95ec
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
   __TEXT.__swift5_typeref: 0x1fa

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4634
+  __TEXT.__unwind_info: 0x46d4
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x870
-  __TEXT.__objc_methname: 0xd691
-  __TEXT.__objc_methtype: 0x1c1d
-  __TEXT.__objc_stubs: 0xb740
-  __DATA_CONST.__got: 0x640
-  __DATA_CONST.__const: 0xfc48
-  __DATA_CONST.__objc_classlist: 0x210
+  __TEXT.__objc_classname: 0x88d
+  __TEXT.__objc_methname: 0xda25
+  __TEXT.__objc_methtype: 0x1c4e
+  __TEXT.__objc_stubs: 0xb900
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__const: 0xfe28
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3fc0
-  __DATA_CONST.__objc_selrefs: 0x31d0
+  __DATA_CONST.__objc_const: 0x40c8
+  __DATA_CONST.__objc_selrefs: 0x3248
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_classrefs: 0x630
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_classrefs: 0x638
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__cfstring: 0x10000
-  __AUTH_CONST.__objc_const: 0x110
+  __AUTH_CONST.__cfstring: 0x10160
+  __AUTH_CONST.__objc_const: 0x158
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__const: 0xe38
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x1288
-  __AUTH.__objc_data: 0x170
+  __AUTH_CONST.__auth_got: 0x12a8
+  __AUTH.__objc_data: 0x1c0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x148
+  __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0x950
   __DATA.__bss: 0x2e8
   __DATA.__common: 0x28
-  __DATA_DIRTY.__const: 0xc40
+  __DATA_DIRTY.__const: 0xc60
   __DATA_DIRTY.__objc_const: 0x15e8
   __DATA_DIRTY.__objc_data: 0x15c8
-  __DATA_DIRTY.__data: 0xd18
-  __DATA_DIRTY.__bss: 0x5b8
+  __DATA_DIRTY.__data: 0xd28
+  __DATA_DIRTY.__bss: 0x5c8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4215
-  Symbols:   2184
-  CStrings:  6733
+  Functions: 4261
+  Symbols:   2201
+  CStrings:  6776
 
Symbols:
+ _IMAttachmentPropertyOriginalGUID
+ _IMDHandleRecordCopyHandlesFilteredUsingPredicateQuery
+ _IMDHandleRecordCopySortedHandlesFilteredUsingPredicateWithLimitQuery
+ _IMDMigrateTo17014
+ _IMHandlePropertyCanonicalizedURIKey
+ _IMHandlePropertyCountryCodeKey
+ _IMHandlePropertyServiceNameKey
+ _IMHandlePropertyUncanonicalizedURIKey
+ _OBJC_CLASS_$_IMDOrphanedAttachmentHandler
+ _OBJC_METACLASS_$_IMDOrphanedAttachmentHandler
+ __IMDHandleRecordCopyHandlesFromRecords
+ __IMDHandleRecordCopyHandlesFromXPCArray
+ ___XPCServerIMDChatRecordCopyChatRecordForIdentifier_IPCAction
+ ___syncXPCIMDChatRecordCopyChatRecordForIdentifier_IPCAction
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeak
- _IMDCleanseOrphanedAttachments
CStrings:
+ "%{public}s: Unknown record type %lld"
+ "-[IMDDatabase(Database) fetchCountOfRecordType:completionHandler:]"
+ "-[IMDDatabase(Handles) fetchHandleRecordsFilteredUsingPredicate:sortedUsingDescriptors:limit:completionHandler:]"
+ "-[IMDDatabase(Handles) handleRecordsFilteredByPredicate:]"
+ "@\"<IMDFileManager>\""
+ "Deleting previews at %@"
+ "Failed to create XPC dictionary"
+ "Failed to get total row count for table %{public}@: %@"
+ "Fetching handles filtered by predicate: %@"
+ "Fetching handles filtered by predicate: %@ sortDescriptors: %llu limit: %llu"
+ "I16@0:8"
+ "IMDMessageRecordCountAllUnreadMessages"
+ "IMDMessageRecordCountAllUnreadMessages timing: %@"
+ "IMDOrphanedAttachmentHandler"
+ "Query: Copy Chat Record for Identifier"
+ "Query: Copy Handles Filtered Using Predicate"
+ "Query: Copy Sorted Handles Filtered Using Predicate With Limit"
+ "Query: Copy the total number of records for a given type"
+ "SELECT ROWID, id, country, service, uncanonicalized_id, person_centric_id FROM handle "
+ "T@\"<IMDFileManager>\",&,N,V_fileManager"
+ "TI,R,N"
+ "Total row count for table %{public}@: %@"
+ "_cleanseOrphanedAttachmentsWithEnumerator:atPath:"
+ "_copyHandleRecordsFromCoreSDBResults:"
+ "_handleRecordsCopiedFromXPCArray:"
+ "_respondWithHandleRecords:responseMessage:completionHandler:"
+ "_xpcArrayWithHandleRecords:"
+ "chat_recoverable_message_join(message_id)"
+ "chat_recoverable_message_join_message_id_idx"
+ "cleanseOrphanedAttachments"
+ "cleanseOrphanedAttachmentsInDirectoryAtPath:"
+ "fetchCountOfRecordType:completionHandler:"
+ "fetchHandleRecordsFilteredUsingPredicate:sortedUsingDescriptors:limit:completionHandler:"
+ "handleIMDCountOfRecordType_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
+ "handleIMDHandleRecordCopyHandlesFilteredUsingPredicate_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
+ "handleIMDHandleRecordCopySortedHandlesFilteredUsingPredicateWithLimit_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
+ "handleRecordsFilteredByPredicate:"
+ "initWithFileManager:"
+ "maxCleanseIterations"
+ "recordType"
+ "v32@0:8Q16@?<v@?q>24"

```
