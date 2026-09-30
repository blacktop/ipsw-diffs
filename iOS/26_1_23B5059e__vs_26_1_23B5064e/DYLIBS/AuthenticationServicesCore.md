## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-622.2.9.10.3
-  __TEXT.__text: 0xbe32c
+622.2.10.10.1
+  __TEXT.__text: 0xbe4d0
   __TEXT.__auth_stubs: 0x2580
-  __TEXT.__objc_methlist: 0x3764
+  __TEXT.__objc_methlist: 0x37c4
   __TEXT.__const: 0xbce8
   __TEXT.__cstring: 0x55c2
-  __TEXT.__oslogstring: 0x3fa0
+  __TEXT.__oslogstring: 0x3fd0
   __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48

   __TEXT.__unwind_info: 0x3240
   __TEXT.__eh_frame: 0x4250
   __TEXT.__objc_classname: 0x7a9
-  __TEXT.__objc_methname: 0xabf8
-  __TEXT.__objc_methtype: 0x287b
-  __TEXT.__objc_stubs: 0x4500
+  __TEXT.__objc_methname: 0xac4a
+  __TEXT.__objc_methtype: 0x2854
+  __TEXT.__objc_stubs: 0x4520
   __DATA_CONST.__got: 0x8c0
   __DATA_CONST.__const: 0xc00
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce8
+  __DATA_CONST.__objc_selrefs: 0x1d00
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH_CONST.__const: 0x61b8
+  __AUTH_CONST.__const: 0x61d8
   __AUTH_CONST.__cfstring: 0x1fc0
-  __AUTH_CONST.__objc_const: 0x77f8
+  __AUTH_CONST.__objc_const: 0x7810
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xbb8

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81285BA4-5F0E-3027-BBE4-1B33CC688473
-  Functions: 4725
-  Symbols:   5311
-  CStrings:  2806
+  UUID: 666CD647-3A49-39FC-A64B-16C6EC5A0B0D
+  Functions: 4731
+  Symbols:   5325
+  CStrings:  2810
 
Symbols:
+ -[ASCAgent authorizationPresenterDidIgnorePINRequest:]
+ -[ASCAgent didEnterCorrectPIN]
+ -[ASCAuthorizationPresenter didIgnorePINRequest]
+ -[ASPublicKeyCredentialOperationTestDelegate didEnterCorrectPIN]
+ GCC_except_table175
+ GCC_except_table178
+ ___54-[ASCAgent authorizationPresenterDidIgnorePINRequest:]_block_invoke
+ ___54-[ASCAgent authorizationPresenterDidIgnorePINRequest:]_block_invoke.cold.1
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.464
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.469.cold.1
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.471
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.446
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.446.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.447
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.450.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.451
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.452
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.456
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.456.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.453
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.453.cold.1
+ ___block_literal_global.444
+ ___block_literal_global.449
+ ___block_literal_global.455
+ ___block_literal_global.460
+ ___block_literal_global.466
+ ___block_literal_global.473
+ ___block_literal_global.477
+ ___block_literal_global.699
+ _objc_msgSend$authorizationPresenterDidIgnorePINRequest:
- GCC_except_table173
- GCC_except_table176
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.462
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.467
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.467.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.444
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.444.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.445
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.448
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.448.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.449
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.454
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.454.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.451
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.451.cold.1
- ___block_literal_global.447
- ___block_literal_global.453
- ___block_literal_global.458
- ___block_literal_global.464
- ___block_literal_global.471
- ___block_literal_global.475
- ___block_literal_global.694
CStrings:
+ "Unexpectedly received ignore PIN request callback."
+ "authorizationPresenterDidIgnorePINRequest:"
+ "didEnterCorrectPIN"
+ "didIgnorePINRequest"
+ "v24@0:8@\"<ASCAuthorizationPresenterHostProtocol>\"16"
+ "v40@0:8@\"<ASCAuthorizationPresenterHostProtocol>\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v32@0:8@\"NSString\"16@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">24"
- "v40@0:8@\"<ASCAuthorizationPresenterHostProtocol>\"16@\"NSString\"24@?<v@?@\"<ASCCredentialProtocol>\"@\"NSError\">32"

```
