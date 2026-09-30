## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-8.1.1.0.0
-  __TEXT.__text: 0xcddb4
-  __TEXT.__auth_stubs: 0x2060
-  __TEXT.__objc_stubs: 0x9340
-  __TEXT.__objc_methlist: 0x34d0
+8.1.6.0.0
+  __TEXT.__text: 0xc41a8
+  __TEXT.__auth_stubs: 0x2070
+  __TEXT.__objc_stubs: 0x93c0
+  __TEXT.__objc_methlist: 0x34e8
   __TEXT.__const: 0x60d0
-  __TEXT.__objc_classname: 0xd6c
-  __TEXT.__objc_methname: 0xd2a8
-  __TEXT.__oslogstring: 0x9842
-  __TEXT.__objc_methtype: 0x3b4c
-  __TEXT.__cstring: 0x6ee8
-  __TEXT.__gcc_except_tab: 0xd7c
+  __TEXT.__objc_classname: 0xd6e
+  __TEXT.__objc_methname: 0xd39e
+  __TEXT.__oslogstring: 0x99f2
+  __TEXT.__objc_methtype: 0x3b80
+  __TEXT.__cstring: 0x6ec8
+  __TEXT.__gcc_except_tab: 0xdd8
   __TEXT.__dlopen_cstrs: 0x2ed
   __TEXT.__constg_swiftt: 0x104c
   __TEXT.__swift5_typeref: 0x132f

   __TEXT.__swift5_types: 0x148
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2c28
+  __TEXT.__unwind_info: 0x2c38
   __TEXT.__eh_frame: 0x3618
-  __DATA_CONST.__auth_got: 0x1040
-  __DATA_CONST.__got: 0x980
-  __DATA_CONST.__auth_ptr: 0x4a0
-  __DATA_CONST.__const: 0x5970
+  __DATA_CONST.__auth_got: 0x1048
+  __DATA_CONST.__got: 0x990
+  __DATA_CONST.__auth_ptr: 0x4b0
+  __DATA_CONST.__const: 0x5a10
   __DATA_CONST.__cfstring: 0x3e80
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x90

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x190
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xba90
-  __DATA.__objc_selrefs: 0x2d70
-  __DATA.__objc_ivar: 0x330
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA.__objc_const: 0xbab0
+  __DATA.__objc_selrefs: 0x2d90
+  __DATA.__objc_ivar: 0x334
   __DATA.__objc_data: 0x1a90
   __DATA.__data: 0x34f8
   __DATA.__bss: 0x7108

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3940
-  Symbols:   937
-  CStrings:  3975
+  Functions: 3949
+  Symbols:   940
+  CStrings:  3986
 
Symbols:
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _AMSErrorIsEqual
+ _AMSErrorUserInfoKeyStatusCode
CStrings:
+ "initWithAccount:bag:initialAuthTokenProvider:authTokenRefreshProvider:odiAssessmentProvider:deviceIdentitySigningProvider:"
+ "v56@0:8@16@24@32@?40@?48"
+ "_initialAuthTokenProvider"
+ "@\"AMSPromise\"24@?0@\"ACAccount\"8@\"NSString\"16"
+ "\x06"
+ "statusCode"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fraud report request failed with error: %!{(MISSING)public}@"
+ "takeKeepAliveTransaction:withQueue:postActionQueue:whilePerformingBlockOnQueue:postAction:"
+ "appendTokenIfNeededToRequest:forAccount:tokenIdentifier:"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Fraud report request failed, server reports authentication token as expired. Attempting silent auth."
+ "_authTokenRefreshProvider"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Failed to retrieve updated authentication token after silent auth, not retrying request. Error: %!{(MISSING)public}@."
+ "@64@0:8@16@24@?32@?40@?48@?56"
+ "@56@0:8@16@24@32@40@48"
+ "handleExpiredAuthenticationTokenErrorWithResult:error:forRequest:account:tokenIdentifier:"
+ "bag, authenticationTokenRefreshProvider, odiAssessmentProvider and deviceIdentitySigningProvider must all be non-nil"
+ "%!{(MISSING)public}@: [%!{(MISSING)public}@] Retrieved new authentication token after silent auth, retrying fraud report request."
+ "response"
- "@\"AMSPromise\"32@?0@\"NSMutableURLRequest\"8@\"ACAccount\"16Q24"
- "bag, tokenDecorationProvider, odiAssessmentProvider and deviceIdentitySigningProvider must all be non-nil"
- "_tokenDecorationProvider"
- "@56@0:8@16@24@?32@?40@?48"
- "initWithAccount:bag:tokenDecorationProvider:odiAssessmentProvider:deviceIdentitySigningProvider:"
- "@\"AMSPromise\"16@?0@\"AMSPair\"8"
- "appendTokenIfNeededToRequest:forAccount:authenticationTokenType:"

```
