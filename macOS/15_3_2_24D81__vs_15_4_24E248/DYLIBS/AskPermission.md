## AskPermission

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/AskPermission`

```diff

-128.2.6.0.0
-  __TEXT.__text: 0x6f30
+128.4.5.0.0
+  __TEXT.__text: 0x6f04
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_methlist: 0x79c
+  __TEXT.__objc_methlist: 0xa1c
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x348
   __TEXT.__cstring: 0x5de
   __TEXT.__oslogstring: 0x878
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_classname: 0x192
   __TEXT.__objc_methname: 0x18fb
   __TEXT.__objc_methtype: 0x5fc

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x638
+  __DATA_CONST.__objc_selrefs: 0x6f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x15d8
+  __AUTH_CONST.__objc_const: 0x1168
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7597F873-4B2E-3856-8BDD-2A669254C496
-  Functions: 188
-  Symbols:   649
+  UUID: F5F9AB7F-377B-3FCF-8EBA-3A74B9238922
+  Functions: 190
+  Symbols:   651
   CStrings:  596
 
Symbols:
+ +[APConnectionNotifier sharedNotifier].cold.1
+ +[PRRequestQueue defaultRequestQueue].cold.1
Functions:
~ -[APConnectionNotifier remoteObjectProxy] : 268 -> 264
~ +[APConnectionNotifier sharedNotifier] : 84 -> 68
~ -[APConnectionNotifier _newRemoteConnection] : 864 -> 856
~ -[APLogConfig isEqual:] : 436 -> 432
~ -[APRequestExtension _finish] : 232 -> 228
~ -[APRequestExtension beginRequestWithExtensionContext:] : 1136 -> 1132
~ +[APRequestHandler addRequestWithURL:account:completion:] : 624 -> 620
~ +[APRequestHandler presentApprovalSheetWithRequestIdentifier:completion:] : 580 -> 576
~ +[APRequestHandler getRequestWithIdentifier:completion:] : 580 -> 576
~ +[APRequestHandler getMatchingRequestsWithIdentifier:completion:] : 580 -> 576
~ +[APRequestHandler checkDownloadQueueWithContentType:] : 516 -> 512
~ +[APRequestHandler getCachedRequestsWithCompletion:] : 540 -> 536
~ +[APRequestHandler localApproveRequestWithItemIdentifier:completion:] : 580 -> 576
~ +[APRequestHandler updateRequestWithIdentifier:action:completion:] : 608 -> 604
~ -[APResult initWithDictionary:] : 492 -> 496
~ +[PRRequestQueue defaultRequestQueue] : 84 -> 68

```
