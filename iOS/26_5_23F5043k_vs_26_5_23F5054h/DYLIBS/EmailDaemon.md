## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3864.600.1.2.3
-  __TEXT.__text: 0x2802a8
+3864.600.31.2.1
+  __TEXT.__text: 0x2802a4
   __TEXT.__auth_stubs: 0x2750
   __TEXT.__objc_methlist: 0x130fc
   __TEXT.__const: 0x3a2c
   __TEXT.__gcc_except_tab: 0x4eeec
-  __TEXT.__cstring: 0x26c4a
+  __TEXT.__cstring: 0x26c2a
   __TEXT.__oslogstring: 0x1a8c4
   __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x22

   __TEXT.__objc_methtype: 0x7bc7
   __TEXT.__objc_stubs: 0x25800
   __DATA_CONST.__got: 0x1c60
-  __DATA_CONST.__const: 0x9450
+  __DATA_CONST.__const: 0x9448
   __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x3f8

   __DATA_CONST.__objc_arraydata: 0x658
   __AUTH_CONST.__auth_got: 0x13b8
   __AUTH_CONST.__const: 0x5ea3
-  __AUTH_CONST.__cfstring: 0x10060
+  __AUTH_CONST.__cfstring: 0x10020
   __AUTH_CONST.__objc_const: 0x21b98
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x240

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 59FC3F82-F529-3C4C-B084-1C55BDE57CE3
+  UUID: 06B8D533-44D3-39EE-8F1F-7D344F9678E3
   Functions: 10758
-  Symbols:   34790
-  CStrings:  16309
+  Symbols:   34789
+  CStrings:  16305
 
Symbols:
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.398
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.398.cold.1
+ ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.400
+ ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.324
+ ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.262
+ ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.71
+ ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.71.cold.1
+ ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.73
+ ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.238
+ ___block_literal_global.223
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.361
+ ___block_literal_global.384
+ ___block_literal_global.391
+ ___block_literal_global.434
+ ___block_literal_global.438
+ ___block_literal_global.947
+ ___block_literal_global.949
- _EDIconDecorationTyperKey
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.404.cold.1
- ___106-[EDMessageRepository requestRepresentationForMessageWithID:requestID:options:delegate:completionHandler:]_block_invoke.406
- ___125-[EDMessageRepository performOneTimeCodeMessageDeletionWithObjectID:requestID:returnUndoAction:afterDelay:completionHandler:]_block_invoke.327
- ___136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.265
- ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.74
- ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.74.cold.1
- ___60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.76
- ___67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.241
- ___block_literal_global.229
- ___block_literal_global.345
- ___block_literal_global.354
- ___block_literal_global.364
- ___block_literal_global.367
- ___block_literal_global.371
- ___block_literal_global.390
- ___block_literal_global.393
- ___block_literal_global.397
- ___block_literal_global.440
- ___block_literal_global.444
- ___block_literal_global.953
- ___block_literal_global.955
Functions:
~ -[EDMessageRepository mailOnBoardDeleteVerificationCodesMessage:completionHandler:] : 712 -> 732
~ -[EDMessageRepository _dictForPasswordsIcon] : 132 -> 108
CStrings:
- "ISIconDecorationType"
- "otpOnboardingIcon.png"

```
