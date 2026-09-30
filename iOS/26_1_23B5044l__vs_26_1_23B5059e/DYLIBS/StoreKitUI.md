## StoreKitUI

> `/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI`

```diff

-815.1.6.0.0
-  __TEXT.__text: 0x357390
+815.1.12.0.0
+  __TEXT.__text: 0x357840
   __TEXT.__auth_stubs: 0x24a0
-  __TEXT.__objc_methlist: 0x3399c
+  __TEXT.__objc_methlist: 0x33a84
   __TEXT.__const: 0x23e4
   __TEXT.__gcc_except_tab: 0x5ff8
-  __TEXT.__cstring: 0x2e5da
-  __TEXT.__oslogstring: 0xc01
+  __TEXT.__cstring: 0x2e60a
+  __TEXT.__oslogstring: 0xd21
   __TEXT.__dlopen_cstrs: 0x26d
   __TEXT.__ustring: 0x62
   __TEXT.__constg_swiftt: 0x4b4

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xcf10
+  __TEXT.__unwind_info: 0xcf18
   __TEXT.__eh_frame: 0x358
-  __TEXT.__objc_classname: 0x8e49
-  __TEXT.__objc_methname: 0x5d7e0
-  __TEXT.__objc_methtype: 0x10773
-  __TEXT.__objc_stubs: 0x40ac0
-  __DATA_CONST.__got: 0x1f20
-  __DATA_CONST.__const: 0x90e8
+  __TEXT.__objc_classname: 0x8e75
+  __TEXT.__objc_methname: 0x5dad3
+  __TEXT.__objc_methtype: 0x10af4
+  __TEXT.__objc_stubs: 0x40b00
+  __DATA_CONST.__got: 0x1f28
+  __DATA_CONST.__const: 0x9110
   __DATA_CONST.__objc_classlist: 0x1f60
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x870
+  __DATA_CONST.__objc_protolist: 0x880
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13c68
+  __DATA_CONST.__objc_selrefs: 0x13cf8
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x19c8
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x1268
   __AUTH_CONST.__const: 0x1b18
   __AUTH_CONST.__cfstring: 0x151e0
-  __AUTH_CONST.__objc_const: 0xbdb40
+  __AUTH_CONST.__objc_const: 0xbdf28
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x90

   __AUTH.__objc_data: 0x112d0
   __AUTH.__data: 0x418
   __DATA.__objc_ivar: 0x4a04
-  __DATA.__data: 0x6df8
+  __DATA.__data: 0x6eb8
   __DATA.__bss: 0x1148
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x26c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 285E3BD0-8A36-316F-B1AB-927997CDB459
-  Functions: 20356
-  Symbols:   68057
-  CStrings:  26135
+  UUID: 8B06D8FA-32F9-398F-B4D2-DA6FF93BFAFD
+  Functions: 20365
+  Symbols:   68094
+  CStrings:  26174
 
Symbols:
+ -[SKUIPostRatingOperation AMSURLSession:task:handleAuthenticateRequest:completion:]
+ -[SKUIPostRatingOperation run].cold.1
+ -[SKUIPostRatingOperation run].cold.2
+ -[SKUIPostRatingOperation run].cold.3
+ _OBJC_CLASS_$_AMSUIAuthenticateTask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AMSURLProtocolDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSURLProtocolDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_AMSURLProtocolDelegate
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SKUIPostRatingOperation
+ __OBJC_LABEL_PROTOCOL_$_AMSURLProtocolDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_PROTOCOL_$_AMSURLProtocolDelegate
+ __OBJC_PROTOCOL_$_NSURLSessionDelegate
+ ___30-[SKUIPostRatingOperation run]_block_invoke.30
+ ___30-[SKUIPostRatingOperation run]_block_invoke.30.cold.1
+ ___30-[SKUIPostRatingOperation run]_block_invoke.cold.1
+ ___83-[SKUIPostRatingOperation AMSURLSession:task:handleAuthenticateRequest:completion:]_block_invoke
+ ___83-[SKUIPostRatingOperation AMSURLSession:task:handleAuthenticateRequest:completion:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"AMSAuthenticateResult"8"NSError"16ls40l8s32l8
+ _objc_msgSend$initWithRequest:accountStore:bag:
+ _objc_msgSend$performAuthentication
- ___30-[SKUIPostRatingOperation run]_block_invoke.27
CStrings:
+ "AMSURLProtocolDelegate"
+ "AMSURLSession:handleAuthenticateRequest:completion:"
+ "AMSURLSession:handleDialogRequest:completion:"
+ "AMSURLSession:shouldFailWithServerError:"
+ "AMSURLSession:shouldHandleAuthenticationForAccount:dialogDictionary:"
+ "AMSURLSession:shouldHandleDialogDictionary:"
+ "AMSURLSession:task:handleAuthenticateRequest:completion:"
+ "AMSURLSession:task:handleDialogRequest:completion:"
+ "AMSURLSession:task:handleEngagementRequest:completion:"
+ "AMSURLSession:task:shouldFailWithServerError:"
+ "B32@0:8@\"AMSURLSession\"16@\"NSDictionary\"24"
+ "B32@0:8@\"AMSURLSession\"16@\"NSError\"24"
+ "B40@0:8@\"AMSURLSession\"16@\"ACAccount\"24@\"NSDictionary\"32"
+ "B40@0:8@\"AMSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "NSURLSessionDelegate"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "[SKUIPostRatingOperation] Authentication result: %@"
+ "[SKUIPostRatingOperation] Error: %@"
+ "[SKUIPostRatingOperation] Handling auth request"
+ "[SKUIPostRatingOperation] No active iTunes account found, user not logged in"
+ "[SKUIPostRatingOperation] Successfully retrieved active iTunes account: %{public}@"
+ "initWithRequest:accountStore:bag:"
+ "performAuthentication"
+ "presentingSceneBundleIdentifier"
+ "presentingSceneIdentifier"
+ "presentingWindow"
+ "reportMetricsForContext:"
+ "v24@0:8@\"AMSMetricsLoadURLContext\"16"
+ "v24@0:8@\"NSURLSession\"16"
+ "v24@?0@\"AMSAuthenticateResult\"8@\"NSError\"16"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v40@0:8@\"AMSURLSession\"16@\"AMSAuthenticateRequest\"24@?<v@?@\"AMSAuthenticateResult\"@\"NSError\">32"
+ "v40@0:8@\"AMSURLSession\"16@\"AMSDialogRequest\"24@?<v@?@\"AMSDialogResult\"@\"NSError\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v48@0:8@\"AMSURLSession\"16@\"NSURLSessionTask\"24@\"AMSAuthenticateRequest\"32@?<v@?@\"AMSAuthenticateResult\"@\"NSError\">40"
+ "v48@0:8@\"AMSURLSession\"16@\"NSURLSessionTask\"24@\"AMSDialogRequest\"32@?<v@?@\"AMSDialogResult\"@\"NSError\">40"
+ "v48@0:8@\"AMSURLSession\"16@\"NSURLSessionTask\"24@\"AMSEngagementRequest\"32@?<v@?@\"AMSEngagementResult\"@\"NSError\">40"

```
