## HelpData

> `/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/HelpData`

```diff

-  __TEXT.__text: 0x1c7a4
+  __TEXT.__text: 0x1c84c
   __TEXT.__objc_methlist: 0x2014
   __TEXT.__cstring: 0x3394
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x390
+  __TEXT.__gcc_except_tab: 0x398
   __TEXT.__oslogstring: 0x250
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__unwind_info: 0x6f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA.__objc_ivar: 0x298
   __DATA.__data: 0x480
   __DATA.__ddm_mapping: 0x5fa
-  __DATA.__ddm_config: 0x15fb
+  __DATA.__ddm_config: 0x164c
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__data: 0x4
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[DDMObjectManager _authenticateForHost:withCompletionHandler:]
+ -[HPDAuthChallengeHandler authenticateForHost:withCompletionHandler:]
+ _objc_msgSend$_authenticateForHost:withCompletionHandler:
+ _objc_msgSend$authenticateForHost:withCompletionHandler:
- -[DDMObjectManager _authenticateWithCompletionHandler:]
- -[HPDAuthChallengeHandler authenticateWithCompletionHandler:]
- _objc_msgSend$_authenticateWithCompletionHandler:
- _objc_msgSend$authenticateWithCompletionHandler:
Functions:
~ ___72-[DDMObjectManager _executeURLRequest:retryCount:withCompletionHandler:]_block_invoke : 732 -> 780
~ -[DDMObjectManager _authenticateWithCompletionHandler:] -> -[DDMObjectManager _authenticateForHost:withCompletionHandler:] : 96 -> 132
~ -[DDMAssetURLProtocol(Private) handleURLSession:dataTask:didReceiveResponse:completionHandler:] : 852 -> 936

```
