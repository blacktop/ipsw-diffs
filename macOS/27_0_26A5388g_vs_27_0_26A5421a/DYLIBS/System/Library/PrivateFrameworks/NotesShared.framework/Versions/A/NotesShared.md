## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/Versions/A/NotesShared`

```diff

-3192.0.0.0.0
-  __TEXT.__text: 0x36d65c
+3195.0.0.0.0
+  __TEXT.__text: 0x36e11c
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x6b0
-  __TEXT.__objc_methlist: 0x1822c
+  __TEXT.__objc_methlist: 0x1829c
   __TEXT.__const: 0xdb70
-  __TEXT.__cstring: 0x19386
-  __TEXT.__gcc_except_tab: 0xf1e0
-  __TEXT.__oslogstring: 0x1c889
+  __TEXT.__cstring: 0x19406
+  __TEXT.__gcc_except_tab: 0xf20c
+  __TEXT.__oslogstring: 0x1c919
   __TEXT.__ustring: 0x39a
   __TEXT.__swift5_typeref: 0x4376
   __TEXT.__constg_swiftt: 0x363c

   __TEXT.__swift_as_ret: 0x1b4
   __TEXT.__swift_as_cont: 0x3f0
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf100
+  __TEXT.__unwind_info: 0xf138
   __TEXT.__eh_frame: 0x8680
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e60
+  __DATA_CONST.__const: 0x1e68
   __DATA_CONST.__objc_classlist: 0xa58
   __DATA_CONST.__objc_catlist: 0x130
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xcb08
+  __DATA_CONST.__objc_selrefs: 0xcb48
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6d0
   __DATA_CONST.__objc_arraydata: 0x228
   __DATA_CONST.__got: 0x2178
-  __AUTH_CONST.__const: 0x127f8
-  __AUTH_CONST.__cfstring: 0xfaa0
-  __AUTH_CONST.__objc_const: 0x22380
+  __AUTH_CONST.__const: 0x12828
+  __AUTH_CONST.__cfstring: 0xfae0
+  __AUTH_CONST.__objc_const: 0x22390
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x258

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18632
-  Symbols:   23342
-  CStrings:  5244
+  Functions: 18647
+  Symbols:   23361
+  CStrings:  5249
 
Symbols:
+ +[ICCloudNotificationsController batchUpdateTopicSubscriptionsAllAccountsInBackground]
+ +[ICCloudNotificationsController finishUserNotificationsRegistrationUpdatingSubscriptionsWithAuthorization:]
+ +[ICNote contentInfoAttributedTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:attachmentGraphInfoCount:account:]
+ +[ICNote contentInfoTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:attachmentGraphInfoCount:account:]
+ +[ICNote graphContentInfoTextForCount:]
+ -[ICAttachmentPaperBundleModel paperHasGraph]
+ -[ICAttachmentPaperBundleModel setPaperHasGraph:]
+ -[ICDividerLineTextAttachment attachmentCell]
+ -[ICDividerLineTextAttachment imageForBounds:textContainer:characterIndex:]
+ -[ICInlineAttachment cachedlinkedNoteIsPasswordProtected]
+ -[ICInlineAttachment linkedNoteIsPasswordProtected]
+ -[ICInlineAttachment setCachedlinkedNoteIsPasswordProtected:]
+ -[ICNote graphContentInfoCount]
+ GCC_except_table202
+ GCC_except_table347
+ OBJC_IVAR_$_ICInlineAttachment._cachedlinkedNoteIsPasswordProtected
+ _ICAttachmentPaperHasGraphMetadataKey
+ ___22-[ICNoteData willSave]_block_invoke
+ ___31-[ICNote graphContentInfoCount]_block_invoke
+ ___49-[ICAttachmentPaperBundleModel setPaperHasGraph:]_block_invoke
+ ___51-[ICCloudSyncBackgroundTask runTaskWithCompletion:]_block_invoke_2
+ ___86+[ICCloudNotificationsController batchUpdateTopicSubscriptionsAllAccountsInBackground]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e26_v24?0"ICAttachment"8^B16l
+ _objc_msgSend$batchUpdateTopicSubscriptionsAllAccountsInBackground
+ _objc_msgSend$cachedlinkedNoteIsPasswordProtected
+ _objc_msgSend$contentInfoAttributedTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:attachmentGraphInfoCount:account:
+ _objc_msgSend$contentInfoTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:attachmentGraphInfoCount:account:
+ _objc_msgSend$graphContentInfoCount
+ _objc_msgSend$graphContentInfoTextForCount:
+ _objc_msgSend$requestSaveWhenUnblockedWithBlock:
+ _objc_msgSend$setCachedlinkedNoteIsPasswordProtected:
- +[ICNote contentInfoAttributedTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:account:]
- -[ICInlineAttachment cachedLinkedNoteIsPasswordProtectedAndLocked]
- -[ICInlineAttachment linkedNoteIsPasswordProtectedAndLocked]
- -[ICInlineAttachment setCachedLinkedNoteIsPasswordProtectedAndLocked:]
- GCC_except_table341
- GCC_except_table364
- OBJC_IVAR_$_ICInlineAttachment._cachedLinkedNoteIsPasswordProtectedAndLocked
- _objc_msgSend$cachedLinkedNoteIsPasswordProtectedAndLocked
- _objc_msgSend$contentInfoAttributedTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:account:
- _objc_msgSend$contentInfoTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:account:
- _objc_msgSend$initWithSize:
- _objc_msgSend$setCachedLinkedNoteIsPasswordProtectedAndLocked:
CStrings:
+ "NOTE_LIST_GRAPHS_%lu"
+ "Safety mechanism update required. You can see the status in [Settings](chinaai-settings)."
+ "User did not grant authorization for user notifications (via warming sheet)"
+ "User granted authorization for user notifications (via warming sheet)"
+ "hasGraphKey"
```
