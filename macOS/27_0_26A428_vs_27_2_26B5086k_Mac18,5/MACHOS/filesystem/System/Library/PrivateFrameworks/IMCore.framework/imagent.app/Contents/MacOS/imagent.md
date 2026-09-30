## imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/Contents/MacOS/imagent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x63c38
-  __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_stubs: 0x7920
-  __TEXT.__objc_methlist: 0x32e8
-  __TEXT.__const: 0x1a30
-  __TEXT.__gcc_except_tab: 0x3414
-  __TEXT.__cstring: 0x1891
-  __TEXT.__oslogstring: 0x6de9
-  __TEXT.__objc_methname: 0xc7c9
+1491.200.63.0.0
+  __TEXT.__text: 0x65b44
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_stubs: 0x7a60
+  __TEXT.__objc_methlist: 0x3328
+  __TEXT.__const: 0x1a70
+  __TEXT.__gcc_except_tab: 0x3438
+  __TEXT.__cstring: 0x1911
+  __TEXT.__oslogstring: 0x6e49
+  __TEXT.__objc_methname: 0xcb29
   __TEXT.__objc_classname: 0xa31
-  __TEXT.__objc_methtype: 0x350d
-  __TEXT.__swift5_typeref: 0x91e
-  __TEXT.__swift5_capture: 0x7cc
-  __TEXT.__constg_swiftt: 0x904
+  __TEXT.__objc_methtype: 0x35dd
+  __TEXT.__swift5_typeref: 0x92e
+  __TEXT.__swift5_capture: 0x820
+  __TEXT.__constg_swiftt: 0x90c
   __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_reflstr: 0x3be
   __TEXT.__swift5_fieldmd: 0x3cc
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift_as_entry: 0x118
-  __TEXT.__swift_as_ret: 0x104
-  __TEXT.__swift_as_cont: 0x114
+  __TEXT.__swift_as_entry: 0x124
+  __TEXT.__swift_as_ret: 0x110
+  __TEXT.__swift_as_cont: 0x120
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2018
-  __TEXT.__eh_frame: 0x1858
-  __DATA_CONST.__const: 0x2680
+  __TEXT.__unwind_info: 0x2080
+  __TEXT.__eh_frame: 0x19a0
+  __DATA_CONST.__const: 0x2748
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x218

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xb88
-  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__auth_got: 0xbc8
+  __DATA_CONST.__got: 0xb18
   __DATA_CONST.__auth_ptr: 0x318
-  __DATA.__objc_const: 0x32a8
-  __DATA.__objc_selrefs: 0x2b40
+  __DATA.__objc_const: 0x32c0
+  __DATA.__objc_selrefs: 0x2ba0
   __DATA.__objc_ivar: 0x48
-  __DATA.__objc_data: 0x10a0
-  __DATA.__data: 0x17e0
+  __DATA.__objc_data: 0x10a8
+  __DATA.__data: 0x1800
   __DATA.__common: 0x108
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1544
-  Symbols:   566
-  CStrings:  2552
+  Functions: 1565
+  Symbols:   571
+  CStrings:  2571
 
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
