## ContextKitExtraction

> `/System/Library/PrivateFrameworks/ContextKitExtraction.framework/Versions/A/ContextKitExtraction`

```diff

-298.0.0.0.0
-  __TEXT.__text: 0x4368
+299.0.0.0.0
+  __TEXT.__text: 0x4358
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x638
-  __TEXT.__const: 0xa8
+  __TEXT.__objc_methlist: 0x684
+  __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x1217
   __TEXT.__ustring: 0x10
   __TEXT.__gcc_except_tab: 0xd8

   __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0xef8
+  __AUTH_CONST.__objc_const: 0xe80
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x78

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 786AD6D2-EDE2-3E68-8989-8C93CF2E8CFB
-  Functions: 149
-  Symbols:   503
+  UUID: 1C2F9682-AB22-3ABF-84F6-2046F8CBF094
+  Functions: 150
+  Symbols:   504
   CStrings:  437
 
Symbols:
+ +[CKContextSharedExtractionHelper blocksFromText:].cold.1
Functions:
~ +[CKContextUIClasses isWKWebView:] : 52 -> 56
~ +[CKContextUIClasses isPDFView:] : 52 -> 56
~ +[CKContextUIClasses isSFSafariView:] : 52 -> 56
~ +[CKContextSharedExtractionHelper blocksFromText:] : 316 -> 300
~ +[CKContextSharedExtractionHelper bestContentStringForWebViewUIElements:andTitle:] : 544 -> 552
~ ___74-[CKContextContentProviderManager _loadContextKitIfNecessaryWithExecutor:]_block_invoke : 216 -> 212
~ -[CKContextContentProviderManager _prepareDonationWithNonce:options:isRecentsCapture:requiringMainQueue:andReply:] : 280 -> 276
~ -[CKContextContentProviderManager _prepareDonationWithNonce:options:isRecentsCapture:andReply:] : 1164 -> 1148
~ -[CKContextExecutor initWithContext:workItemQueue:completionQueue:timeoutAfter:completionHandler:] : 488 -> 480
~ -[CKContextExecutor addWorkItemToQueue:withWorkItem:andContext:] : 336 -> 332
~ ___83+[CKContextContentProvider extractContentFromWebViewPDFData:withCompletionHandler:]_block_invoke : 552 -> 548
+ +[CKContextSharedExtractionHelper blocksFromText:].cold.1
CStrings:
+ "Could not get notification state; error:%u"
- "Could not get notification state; error:%i"

```
