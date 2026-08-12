## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2998.0.0.0.0
-  __TEXT.__text: 0x34a028
+3001.2.1.0.0
+  __TEXT.__text: 0x34ab7c
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x18324
-  __TEXT.__const: 0xdb58
-  __TEXT.__cstring: 0x19344
-  __TEXT.__gcc_except_tab: 0xf0bc
-  __TEXT.__oslogstring: 0x1cc89
+  __TEXT.__objc_methlist: 0x1838c
+  __TEXT.__const: 0xdb68
+  __TEXT.__cstring: 0x193c4
+  __TEXT.__gcc_except_tab: 0xf0e4
+  __TEXT.__oslogstring: 0x1cd19
   __TEXT.__ustring: 0x39a
   __TEXT.__swift5_typeref: 0x4348
   __TEXT.__swift5_fieldmd: 0x2dc8

   __TEXT.__swift_as_ret: 0x1b0
   __TEXT.__swift_as_cont: 0x3e8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf030
+  __TEXT.__unwind_info: 0xf068
   __TEXT.__eh_frame: 0x8710
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6510
+  __DATA_CONST.__const: 0x6568
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xcbf8
+  __DATA_CONST.__objc_selrefs: 0xcc30
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x2138
+  __DATA_CONST.__got: 0x2130
   __AUTH_CONST.__const: 0xdb08
-  __AUTH_CONST.__cfstring: 0xfa00
-  __AUTH_CONST.__objc_const: 0x223e8
+  __AUTH_CONST.__cfstring: 0xfa40
+  __AUTH_CONST.__objc_const: 0x223f8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x258

   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
-  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18532
-  Symbols:   22940
-  CStrings:  5272
+  Functions: 18547
+  Symbols:   22959
+  CStrings:  5277
 
Symbols:
+ +[ICCloudNotificationsController batchUpdateTopicSubscriptionsAllAccountsInBackground]
+ +[ICCloudNotificationsController finishUserNotificationsRegistrationUpdatingSubscriptionsWithAuthorization:]
+ +[ICNote contentInfoAttributedTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:attachmentGraphInfoCount:account:]
+ +[ICNote contentInfoTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:attachmentGraphInfoCount:account:]
+ +[ICNote graphContentInfoTextForCount:]
+ -[ICAttachmentPaperBundleModel paperHasGraph]
+ -[ICAttachmentPaperBundleModel setPaperHasGraph:]
+ -[ICDividerLineTextAttachment imageForBounds:textContainer:characterIndex:]
+ -[ICInlineAttachment cachedlinkedNoteIsPasswordProtected]
+ -[ICInlineAttachment linkedNoteIsPasswordProtected]
+ -[ICInlineAttachment setCachedlinkedNoteIsPasswordProtected:]
+ -[ICNote graphContentInfoCount]
+ GCC_except_table331
+ GCC_except_table354
+ _ICAttachmentPaperHasGraphMetadataKey
+ _OBJC_IVAR_$_ICInlineAttachment._cachedlinkedNoteIsPasswordProtected
+ ___22-[ICNoteData willSave]_block_invoke
+ ___31-[ICNote graphContentInfoCount]_block_invoke
+ ___42-[ICBackgroundTaskScheduler registerTask:]_block_invoke_3
+ ___49-[ICAttachmentPaperBundleModel setPaperHasGraph:]_block_invoke
+ ___51-[ICCloudSyncBackgroundTask runTaskWithCompletion:]_block_invoke_2
+ ___86+[ICCloudNotificationsController batchUpdateTopicSubscriptionsAllAccountsInBackground]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e26_v24?0"ICAttachment"8^B16lr32l8r40l8
+ ___block_descriptor_56_e8_32s40r48w_e8_v12?0B8ls32l8r40l8w48l8
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
- GCC_except_table327
- _OBJC_CLASS_$_CIImage
- _OBJC_IVAR_$_ICInlineAttachment._cachedLinkedNoteIsPasswordProtectedAndLocked
- _objc_msgSend$cachedLinkedNoteIsPasswordProtectedAndLocked
- _objc_msgSend$contentInfoAttributedTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:account:
- _objc_msgSend$contentInfoTextWithSnippet:attachmentContentInfoType:attachmentContentInfoCount:account:
- _objc_msgSend$emptyImage
- _objc_msgSend$imageWithCIImage:
- _objc_msgSend$setCachedLinkedNoteIsPasswordProtectedAndLocked:
CStrings:
+ "NOTE_LIST_GRAPHS_%lu"
+ "Safety mechanism update required. You can see the status in [Settings](chinaai-settings)."
+ "User did not grant authorization for user notifications (via warming sheet)"
+ "User granted authorization for user notifications (via warming sheet)"
+ "hasGraphKey"
```
