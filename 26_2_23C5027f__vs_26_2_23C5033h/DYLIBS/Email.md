## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.300.11.2.1
-  __TEXT.__text: 0xce6b0
+3864.300.22.2.1
+  __TEXT.__text: 0xce640
   __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0xc9ac
-  __TEXT.__gcc_except_tab: 0x1b1dc
+  __TEXT.__objc_methlist: 0xc9b4
+  __TEXT.__gcc_except_tab: 0x1b1c8
   __TEXT.__const: 0x1238
   __TEXT.__cstring: 0xb62c
   __TEXT.__oslogstring: 0x6123

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7a80
+  __TEXT.__unwind_info: 0x7a78
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_classname: 0x1a44
-  __TEXT.__objc_methname: 0x1b288
+  __TEXT.__objc_methname: 0x1b2cf
   __TEXT.__objc_methtype: 0x4714
-  __TEXT.__objc_stubs: 0x11d40
+  __TEXT.__objc_stubs: 0x11d80
   __DATA_CONST.__got: 0xca0
   __DATA_CONST.__const: 0x4270
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e98
+  __DATA_CONST.__objc_selrefs: 0x5ea8
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x478
-  __DATA_CONST.__objc_arraydata: 0x1d0
+  __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x1848
   __AUTH_CONST.__cfstring: 0x9be0
   __AUTH_CONST.__objc_const: 0x16310
-  __AUTH_CONST.__objc_intobj: 0x348
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x618
   __AUTH.__data: 0x158

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5625AD4D-86A9-3509-836B-54CF6D28CC6E
-  Functions: 4764
-  Symbols:   17725
-  CStrings:  8415
+  UUID: 7CD0FB52-54D2-3D55-8725-0F72C9798FC2
+  Functions: 4765
+  Symbols:   17728
+  CStrings:  8417
 
Symbols:
+ +[EMMessageListItemPredicates _predicateForMessagesWithSearchResultTypes:]
+ ___111+[EMMessageListItemPredicates predicateForMessagesWithActiveFollowUpInAccountsOfMailboxes:mailboxTypeResolver:]_block_invoke.137
+ ___block_literal_global.133
+ ___block_literal_global.136
+ ___block_literal_global.140
+ ___block_literal_global.143
+ ___block_literal_global.155
+ ___block_literal_global.165
+ ___block_literal_global.173
+ ___block_literal_global.189
+ _objc_msgSend$_predicateForMessagesWithSearchResultTypes:
+ _objc_msgSend$setDisableBlockingOnIndex:
- GCC_except_table162
- ___111+[EMMessageListItemPredicates predicateForMessagesWithActiveFollowUpInAccountsOfMailboxes:mailboxTypeResolver:]_block_invoke.132
- ___block_literal_global.128
- ___block_literal_global.131
- ___block_literal_global.135
- ___block_literal_global.138
- ___block_literal_global.150
- ___block_literal_global.163
- ___block_literal_global.179
Functions:
~ +[EMMessageListItemPredicates predicateForTopHitsMessages] : 188 -> 12
~ +[EMMessageListItemPredicates predicateForIndexedMessages] : 188 -> 12
+ +[EMMessageListItemPredicates _predicateForMessagesWithSearchResultTypes:]
~ -[EMSearchableIndexQuery initWithExpression:builder:queryContext:querySetup:] : 3808 -> 3828
~ -[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:] : 2208 -> 2220
CStrings:
+ "_predicateForMessagesWithSearchResultTypes:"
+ "setDisableBlockingOnIndex:"

```
