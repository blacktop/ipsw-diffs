## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3774.100.2.2.5
-  __TEXT.__text: 0x96338
+3774.200.91.2.1
+  __TEXT.__text: 0x96e04
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x8714
-  __TEXT.__gcc_except_tab: 0x13654
+  __TEXT.__objc_methlist: 0x8744
+  __TEXT.__gcc_except_tab: 0x13780
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x7aaa
-  __TEXT.__oslogstring: 0x3f21
+  __TEXT.__oslogstring: 0x3f97
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x6108
+  __TEXT.__unwind_info: 0x6134
   __TEXT.__objc_classname: 0x1732
-  __TEXT.__objc_methname: 0x168ee
+  __TEXT.__objc_methname: 0x1697e
   __TEXT.__objc_methtype: 0x3f30
-  __TEXT.__objc_stubs: 0xf120
+  __TEXT.__objc_stubs: 0xf140
   __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x33e8
+  __DATA_CONST.__const: 0x3408
   __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x112f0
-  __DATA_CONST.__objc_selrefs: 0x4e58
+  __DATA_CONST.__objc_selrefs: 0x4e78
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__cfstring: 0x7140
   __AUTH_CONST.__objc_const: 0x4838

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3536
-  Symbols:   14403
-  CStrings:  5861
+  Functions: 3543
+  Symbols:   14423
+  CStrings:  5866
 
Symbols:
+ +[EMMessageListItemPredicates predicateForAccountIdentifier:]
+ -[CNContactStore(EmailContactUtilities) _fetchContactForEmailAddress:keysToFetch:allowMatchOnDisplayName:createIfNeeded:error:].cold.1
+ -[EMBaseMessageListItem arePropertiesEqual:]
+ -[EMOutgoingMessageRepository addOutgoingMessageObserver:]
+ -[EMOutgoingMessageRepository removeOutgoingMessageObserver:]
+ -[EMQuery queryWithTargetClass:predicate:]
+ -[NSArray(EMSmartMailbox) em_containsSmartMailboxType:]
+ GCC_except_table128
+ __OBJC_$_INSTANCE_METHODS_NSArray(EMMessageListItem|EMSender|EMSmartMailbox)
+ ___55-[NSArray(EMSmartMailbox) em_containsSmartMailboxType:]_block_invoke
+ ___58-[EMOutgoingMessageRepository addOutgoingMessageObserver:]_block_invoke
+ ___61-[EMOutgoingMessageRepository removeOutgoingMessageObserver:]_block_invoke
+ ___block_descriptor_40_e19_B16?0"EMMailbox"8l
+ _objc_msgSend$queryWithTargetClass:predicate:
- -[EMOutgoingMessageRepository addObserver:]
- -[EMOutgoingMessageRepository removeObserver:]
- GCC_except_table129
- __OBJC_$_INSTANCE_METHODS_NSArray(EMMessageListItem|EMSender)
- ___43-[EMOutgoingMessageRepository addObserver:]_block_invoke
- ___46-[EMOutgoingMessageRepository removeObserver:]_block_invoke
CStrings:
+ "Failed to fetch contact for email address: %@ using key descriptors: %@ due to EMContactStoreIllegalEmailAddressError"
+ "addOutgoingMessageObserver:"
+ "arePropertiesEqual:"
+ "em_containsSmartMailboxType:"
+ "predicateForAccountIdentifier:"
+ "queryWithTargetClass:predicate:"
+ "removeOutgoingMessageObserver:"
- "addObserver:"
- "removeObserver:"

```
