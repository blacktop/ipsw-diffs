## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1450.600.53.2.3
-  __TEXT.__text: 0x366518
-  __TEXT.__auth_stubs: 0x5530
-  __TEXT.__objc_methlist: 0x19c44
-  __TEXT.__const: 0x6c78
-  __TEXT.__cstring: 0x12d8c
-  __TEXT.__gcc_except_tab: 0x22158
-  __TEXT.__oslogstring: 0x4f1f7
+1450.600.61.2.7
+  __TEXT.__text: 0x36c290
+  __TEXT.__auth_stubs: 0x55a0
+  __TEXT.__objc_methlist: 0x19c7c
+  __TEXT.__const: 0x6e98
+  __TEXT.__cstring: 0x12dcc
+  __TEXT.__gcc_except_tab: 0x22298
+  __TEXT.__oslogstring: 0x4f447
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
-  __TEXT.__swift5_typeref: 0x2f5c
-  __TEXT.__constg_swiftt: 0x2388
-  __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x136f
-  __TEXT.__swift5_fieldmd: 0x15d4
+  __TEXT.__swift5_typeref: 0x3090
+  __TEXT.__constg_swiftt: 0x2414
+  __TEXT.__swift5_builtin: 0x1cc
+  __TEXT.__swift5_reflstr: 0x13ef
+  __TEXT.__swift5_fieldmd: 0x1698
   __TEXT.__swift5_assocty: 0x6b8
-  __TEXT.__swift5_capture: 0x12f8
-  __TEXT.__swift5_proto: 0x328
-  __TEXT.__swift5_types: 0x204
+  __TEXT.__swift5_capture: 0x1338
+  __TEXT.__swift5_proto: 0x338
+  __TEXT.__swift5_types: 0x214
   __TEXT.__swift_as_entry: 0x334
   __TEXT.__swift_as_ret: 0x40c
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd7e0
-  __TEXT.__eh_frame: 0x773c
+  __TEXT.__unwind_info: 0xd8c8
+  __TEXT.__eh_frame: 0x781c
   __TEXT.__objc_classname: 0x44f1
-  __TEXT.__objc_methname: 0x514e7
-  __TEXT.__objc_methtype: 0xb30f
-  __TEXT.__objc_stubs: 0x32ac0
-  __DATA_CONST.__got: 0x3330
-  __DATA_CONST.__const: 0x65b8
+  __TEXT.__objc_methname: 0x51617
+  __TEXT.__objc_methtype: 0xb33f
+  __TEXT.__objc_stubs: 0x32b40
+  __DATA_CONST.__got: 0x3340
+  __DATA_CONST.__const: 0x6680
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x778
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfe80
+  __DATA_CONST.__objc_selrefs: 0xfea8
   __DATA_CONST.__objc_protorefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x2aa8
-  __AUTH_CONST.__const: 0x81b0
-  __AUTH_CONST.__cfstring: 0xe780
-  __AUTH_CONST.__objc_const: 0x211b8
+  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__const: 0x8430
+  __AUTH_CONST.__cfstring: 0xe7e0
+  __AUTH_CONST.__objc_const: 0x21208
   __AUTH_CONST.__objc_intobj: 0xac8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x3418
+  __AUTH.__objc_data: 0x3428
   __AUTH.__data: 0x5e0
   __DATA.__objc_ivar: 0x123c
-  __DATA.__data: 0x57c0
-  __DATA.__bss: 0x5000
+  __DATA.__data: 0x5860
+  __DATA.__bss: 0x5200
   __DATA.__common: 0x178
   __DATA_DIRTY.__objc_data: 0x31b0
   __DATA_DIRTY.__data: 0x28d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A98BE943-8C38-3C26-9743-F316CCF92F8F
-  Functions: 13074
-  Symbols:   3025
-  CStrings:  21654
+  UUID: 8FBCD3C3-B8C3-3C79-BA86-AE07751E3A16
+  Functions: 13155
+  Symbols:   3028
+  CStrings:  21677
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _IMChatPropertyNeedsFreshGroupCreation
+ _IMServerBagValueForKnownSender
CStrings:
+ "Did not find transfer for GUID %@, calling provider with nil"
+ "Dropping command %ld from %@ via server bag"
+ "IMDiMessageIDSDelegate-unsupported-commands"
+ "Not routing message (%@) because it has been delivered, not a candidate for routing"
+ "Not sending message %@ because encryption was downgraded"
+ "Still couldn't find a real receiver URI: %@"
+ "_createGroupActionItemDictionaryForItem:senderURI:chat:conversationID:receiverURI:notifyInternalSecurity:completionBlock:"
+ "_populateAttachmentInfo:fromFileTransferGUIDs:transferInfoProvider:completionBlock:"
+ "_receiverURIWithChat:"
+ "coalescingQueue"
+ "com.apple.imagent.SpotlightCoalescingQueue"
+ "flushPendingFileURLRequests: %{public}ld requests coalesced into %{public}ld unique identifiers"
+ "flushPendingFileURLRequests: batch completed in %{public}.*fs — %{public}ld results for %{public}ld identifiers"
+ "flushPendingFileURLRequests: batch failed in %{public}.*fs — error: %@"
+ "groupAction"
+ "message-type"
+ "mmcsInfo"
+ "needsFreshGroupCreation"
+ "pendingFileURLRequests"
+ "provideFileURL enqueued itemIdentifier: %s typeIdentifier: %s options: %ld pendingKeys: %{public}ld"
+ "setNeedsFreshGroupCreation:"
+ "v24@?0@\"IMFileTransfer\"8@?<v@?@\"NSDictionary\">16"
+ "v48@0:8@16@24@?32@?40"
+ "v68@0:8@16@24@32@40@48B56@?60"
- "Did not find transfer for Message, unable to include it in ReportSpam"
- "Still couldn't fine a real receiver URI: %@"
- "fileURLForSearchableIndex:itemIdentifier:typeIdentifier:options:error:"
- "provideFileURL(forBundleID:protectionClass:itemIdentifier:typeIdentifier:options:completionHandler:)"

```
