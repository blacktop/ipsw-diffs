## imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`

```diff

-1491.100.1.2.25
-  __TEXT.__text: 0x5f590
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_stubs: 0x7b60
-  __TEXT.__objc_methlist: 0x3360
-  __TEXT.__const: 0x1a40
-  __TEXT.__gcc_except_tab: 0x3474
-  __TEXT.__cstring: 0x180c
-  __TEXT.__oslogstring: 0x6d7b
-  __TEXT.__objc_methname: 0xca79
+1491.200.63.2.1
+  __TEXT.__text: 0x61324
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_stubs: 0x7ca0
+  __TEXT.__objc_methlist: 0x33a0
+  __TEXT.__const: 0x1a80
+  __TEXT.__gcc_except_tab: 0x3498
+  __TEXT.__cstring: 0x188c
+  __TEXT.__oslogstring: 0x6ddb
+  __TEXT.__objc_methname: 0xcdb9
   __TEXT.__objc_classname: 0xa15
-  __TEXT.__objc_methtype: 0x349b
-  __TEXT.__swift5_typeref: 0x92e
+  __TEXT.__objc_methtype: 0x3573
+  __TEXT.__swift5_typeref: 0x93e
   __TEXT.__swift5_fieldmd: 0x3d8
-  __TEXT.__constg_swiftt: 0x91c
+  __TEXT.__constg_swiftt: 0x924
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_capture: 0x7dc
+  __TEXT.__swift5_capture: 0x830
   __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift_as_entry: 0x118
-  __TEXT.__swift_as_ret: 0x104
-  __TEXT.__swift_as_cont: 0x114
+  __TEXT.__swift_as_entry: 0x124
+  __TEXT.__swift_as_ret: 0x110
+  __TEXT.__swift_as_cont: 0x120
   __TEXT.__swift5_reflstr: 0x3ee
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2030
-  __TEXT.__eh_frame: 0x1858
-  __DATA_CONST.__const: 0x25a8
+  __TEXT.__unwind_info: 0x2098
+  __TEXT.__eh_frame: 0x19a0
+  __DATA_CONST.__const: 0x2670
   __DATA_CONST.__cfstring: 0x920
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x218

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xd70
-  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__auth_got: 0xdb0
+  __DATA_CONST.__got: 0xb20
   __DATA_CONST.__auth_ptr: 0x318
-  __DATA.__objc_const: 0x32f8
-  __DATA.__objc_selrefs: 0x2be0
+  __DATA.__objc_const: 0x3310
+  __DATA.__objc_selrefs: 0x2c40
   __DATA.__objc_ivar: 0x48
-  __DATA.__objc_data: 0x10a0
-  __DATA.__data: 0x1810
+  __DATA.__objc_data: 0x10a8
+  __DATA.__data: 0x1828
   __DATA.__common: 0x108
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1529
-  Symbols:   621
-  CStrings:  2563
+  Functions: 1549
+  Symbols:   626
+  CStrings:  2582
 
Symbols:
+ _IMCopyAnyServiceGUIDForChat
+ _IMServiceBundleFromNSBundle
+ _IMServiceNameAny
+ _OBJC_CLASS_$_IMDBulkChatHistoryQueryHandler
+ _OBJC_CLASS_$_IMDChatForkMerger
+ _OBJC_CLASS_$_IMMessageItem
- _IMDCreateIMMessageItemFromIMDMessageRecordLoadAttachmentIfNeededRef
CStrings:
+ "Could not find message with GUID %s in %s."
+ "Request from %@ to perform %d bulk history queries"
+ "createIMMessageItemFromIMDMessageRecordRef:inputHandleString:useAttachmentCache:shouldLoadAttachments:"
+ "editedMessageItemWithOriginalMessageItem:editedPartIndex:newPartText:newPartTranslation:"
+ "editedMessageItemWithOriginalMessageItem:retractedPartIndex:shouldRetractSubject:"
+ "fetchItemsWithBulkHistoryQueryRequests:urgent:completionHandler:"
+ "fetchSerializedItemsWithBulkHistoryQueryRequests:urgent:completionHandler:"
+ "initWithString:"
+ "mergeChatForks(intoLeadChatIdentifier:forkChatIdentifiers:)"
+ "mergeChatForksIntoLeadChatIdentifier:forkChatIdentifiers:completionHandler:"
+ "mergeChatsIntoLeadChatGUID:forkChatGUIDs:completionHandler:"
+ "moveMessagesWithGUIDsToRecentlyDeleted:deleteDate:fromSync:"
+ "reconcileForksToLeadChatIdentifier:forkChatIdentifiers:"
+ "simulateEditMessage(withGUID:replacementText:part:completion:)"
+ "simulateEditMessageWithGUID:replacementText:partIndex:completion:"
+ "storeEditedMessage:editedPartIndex:editType:previousMessage:chat:updatedAssociatedMessageItems:"
+ "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:fromSync:"
+ "synchronousDatabaseQueryProvider"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSArray\">28"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24q32@?<v@?B>40"
- "moveMessagesWithGUIDsToRecentlyDeleted:deleteDate:"
- "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:"
```
