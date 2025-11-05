## StoreUI

> `/System/Library/PrivateFrameworks/StoreUI.framework/Versions/A/StoreUI`

```diff

-715.2.3.0.0
-  __TEXT.__text: 0x136c4
+715.4.5.0.0
+  __TEXT.__text: 0x13694
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0xb38
+  __TEXT.__objc_methlist: 0xf60
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x28e4
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x378
   __TEXT.__objc_classname: 0x215
-  __TEXT.__objc_methname: 0x417b
-  __TEXT.__objc_methtype: 0xf3b
+  __TEXT.__objc_methname: 0x41c7
+  __TEXT.__objc_methtype: 0xf8d
   __TEXT.__objc_stubs: 0x44c0
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0xb0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12d8
+  __DATA_CONST.__objc_selrefs: 0x1460
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x2d8
   __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__cfstring: 0x2d20
-  __AUTH_CONST.__objc_const: 0x2dc8
+  __AUTH_CONST.__objc_const: 0x2630
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x438

   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E15C3082-7B46-38A4-BD9C-928EE218EA3C
-  Functions: 296
+  UUID: 80DD24F8-FF9A-32AC-90E7-E75859B055C8
+  Functions: 295
   Symbols:   1356
-  CStrings:  1695
+  CStrings:  1698
 
Functions:
~ -[FRJSStorage callFunction:withArguments:] : 808 -> 780
~ ___24-[FRWKView loadRequest:]_block_invoke_2 : 172 -> 176
~ ___36-[FRWKView sendMessage:messageBody:]_block_invoke : 616 -> 612
~ _getInjectedBundleInitializationUserData : 996 -> 992
~ __38-[FRWKView processStorePlistResponse:]_block_invoke_2.185 : 104 -> 108
- sub_25011c190
~ -[FRWKView webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:] : 444 -> 440
~ -[FRWKView webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:] : 476 -> 472
~ -[FRJSRootObject initWithWebView:storeClient:] : 1436 -> 1432
~ -[FRJSRootObject _cookies] : 232 -> 216
~ ___23-[FRJSRootObject _buy:]_block_invoke : 1652 -> 1644
~ -[FRJSRootObject callFunction:withArguments:] : 5920 -> 5916
~ ___36-[FRJSRootObject _authorizeMachine:]_block_invoke : 180 -> 176
~ ___37-[FRJSRootObject _deauthorizeMachine]_block_invoke : 180 -> 176
~ -[FRJSRootObject _openWindow:] : 2072 -> 2084
~ ___30-[FRJSRootObject _openWindow:]_block_invoke : 572 -> 608
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/FRJSCodeRedeemer.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/FRSharingHelper.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/FRWKView.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/StoreJSInterface/FRJSAccountCreationSecureContext.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/StoreJSInterface/FRJSRootObject.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/StoreJSInterface/FRJSStorage.m"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/FRJSCodeRedeemer.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/FRSharingHelper.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/FRWKView.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/StoreJSInterface/FRJSAccountCreationSecureContext.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/StoreJSInterface/FRJSRootObject.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/Commerce/StoreUI/StoreJSInterface/FRJSStorage.m"

```
