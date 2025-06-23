## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-622.1.14.10.4
-  __TEXT.__text: 0xb9db4
-  __TEXT.__auth_stubs: 0x24d0
-  __TEXT.__objc_methlist: 0x36f8
+622.1.16.10.3
+  __TEXT.__text: 0xba2d4
+  __TEXT.__auth_stubs: 0x2550
+  __TEXT.__objc_methlist: 0x36e0
   __TEXT.__const: 0xbc98
   __TEXT.__cstring: 0x4f42
-  __TEXT.__oslogstring: 0x3f00
+  __TEXT.__oslogstring: 0x3e90
   __TEXT.__gcc_except_tab: 0x2e0
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__swift5_typeref: 0x2175
+  __TEXT.__swift5_typeref: 0x2177
   __TEXT.__constg_swiftt: 0x2380
   __TEXT.__swift5_reflstr: 0x1601
   __TEXT.__swift5_fieldmd: 0x213c

   __TEXT.__swift5_proto: 0x92c
   __TEXT.__swift5_types: 0x29c
   __TEXT.__swift5_capture: 0x458
-  __TEXT.__swift_as_entry: 0x6c
-  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x31e8
-  __TEXT.__eh_frame: 0x4040
+  __TEXT.__unwind_info: 0x3220
+  __TEXT.__eh_frame: 0x4140
   __TEXT.__objc_classname: 0x7a8
-  __TEXT.__objc_methname: 0xaa7d
-  __TEXT.__objc_methtype: 0x2850
-  __TEXT.__objc_stubs: 0x44c0
-  __DATA_CONST.__got: 0x878
-  __DATA_CONST.__const: 0xb90
+  __TEXT.__objc_methname: 0xaa45
+  __TEXT.__objc_methtype: 0x281c
+  __TEXT.__objc_stubs: 0x4480
+  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ca0
+  __DATA_CONST.__objc_selrefs: 0x1c98
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1278
+  __AUTH_CONST.__auth_got: 0x12b8
   __AUTH_CONST.__const: 0x6110
   __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__objc_const: 0x7678
+  __AUTH_CONST.__objc_const: 0x7670
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x400
-  __DATA.__data: 0x27c0
+  __DATA.__data: 0x27d0
   __DATA.__bss: 0x11450
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x1b70

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E19AF39-183F-3611-98A7-37EAC88BAB40
-  Functions: 4667
-  Symbols:   5279
-  CStrings:  2758
+  UUID: 97E4DF17-9D13-3FE3-8857-143CE32ACC5B
+  Functions: 4666
+  Symbols:   5259
+  CStrings:  2754
 
Symbols:
+ GCC_except_table129
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table59
+ GCC_except_table74
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.207
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.210
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.419
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.422
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.425
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.456
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.461
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.461.cold.1
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.463
+ ___64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.347
+ ___64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.350
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.267
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.267.cold.1
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke_2.274
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.278
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.278.cold.1
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.287
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.287.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.198
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.198.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.199
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.199.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.438
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.438.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.439
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.444
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.448.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.445
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.445.cold.1
+ ___87-[ASCAgent _canPerformConditionalRegistrationInICloudKeychainForUsername:relyingParty:]_block_invoke.429
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.354
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.354.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.360
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.363
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.366
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.372
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.372.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.386
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.386.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.393
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.393.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.394.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.400
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.403
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.403.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.409
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.409.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.219
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.219.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.226
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.229
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.229.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.232
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.237
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.242
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.242.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.243
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.255
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.258
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.239
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.252
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_3.240
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_3.240.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_4.241
+ ___block_descriptor_48_e8_32s40bs_e64_v24?0"ASCPlatformPublicKeyCredentialRegistration"8"NSError"16ls32l8s40l8
+ ___block_literal_global.201
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.209
+ ___block_literal_global.212
+ ___block_literal_global.215
+ ___block_literal_global.221
+ ___block_literal_global.228
+ ___block_literal_global.231
+ ___block_literal_global.245
+ ___block_literal_global.254
+ ___block_literal_global.257
+ ___block_literal_global.260
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.276
+ ___block_literal_global.293
+ ___block_literal_global.298
+ ___block_literal_global.310
+ ___block_literal_global.328
+ ___block_literal_global.331
+ ___block_literal_global.349
+ ___block_literal_global.356
+ ___block_literal_global.362
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.382
+ ___block_literal_global.392
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.413
+ ___block_literal_global.416
+ ___block_literal_global.418
+ ___block_literal_global.421
+ ___block_literal_global.424
+ ___block_literal_global.431
+ ___block_literal_global.434
+ ___block_literal_global.436
+ ___block_literal_global.441
+ ___block_literal_global.447
+ ___block_literal_global.452
+ ___block_literal_global.458
+ ___block_literal_global.465
+ ___block_literal_global.685
+ _objectdestroy.23Tm
+ _symbolic _____ s8DurationV
- -[ASCAgent renamePasskeyWithCredentialID:newName:completionHandler:]
- -[ASCAgent renamePasskeyWithCredentialID:newName:completionHandler:].cold.1
- -[ASCAgentProxy renamePasskeyWithCredentialID:newName:completionHandler:]
- GCC_except_table130
- GCC_except_table172
- GCC_except_table175
- GCC_except_table62
- GCC_except_table75
- ___32-[ASCAgent cancelCurrentRequest]_block_invoke.211
- ___32-[ASCAgent cancelCurrentRequest]_block_invoke.214
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.423
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.426
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.429
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.460
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.465
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.465.cold.1
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.467
- ___64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.351
- ___64-[ASCAgent _approvalStateForApplicationIdentifier:relyingParty:]_block_invoke.354
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.271.cold.1
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.275
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke_2.278
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.282
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.282.cold.1
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.291.cold.1
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.295
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.203
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.203.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.206
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.206.cold.1
- ___73-[ASCAgentProxy renamePasskeyWithCredentialID:newName:completionHandler:]_block_invoke
- ___73-[ASCAgentProxy renamePasskeyWithCredentialID:newName:completionHandler:]_block_invoke.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.446
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.446.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.447
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.452
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.452.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.449
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.449.cold.1
- ___87-[ASCAgent _canPerformConditionalRegistrationInICloudKeychainForUsername:relyingParty:]_block_invoke.433
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.358
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.358.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.364
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.367
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.370
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.384
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.384.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.390.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.397
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.397.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.398
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.398.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.404
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.407
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.407.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.413
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.413.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.223
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.223.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.230
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.233
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.233.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.236
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.241
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.246
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.246.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.247
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.259
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.262
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.243
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_2.256
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_3.244
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_3.244.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke_4.245
- ___block_descriptor_40_e8_32bs_e64_v24?0"ASCPlatformPublicKeyCredentialRegistration"8"NSError"16ls32l8
- ___block_literal_global.205
- ___block_literal_global.208
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.216
- ___block_literal_global.219
- ___block_literal_global.225
- ___block_literal_global.232
- ___block_literal_global.235
- ___block_literal_global.249
- ___block_literal_global.258
- ___block_literal_global.261
- ___block_literal_global.264
- ___block_literal_global.270
- ___block_literal_global.273
- ___block_literal_global.284
- ___block_literal_global.297
- ___block_literal_global.302
- ___block_literal_global.314
- ___block_literal_global.332
- ___block_literal_global.335
- ___block_literal_global.357
- ___block_literal_global.360
- ___block_literal_global.366
- ___block_literal_global.369
- ___block_literal_global.372
- ___block_literal_global.386
- ___block_literal_global.400
- ___block_literal_global.406
- ___block_literal_global.409
- ___block_literal_global.417
- ___block_literal_global.420
- ___block_literal_global.422
- ___block_literal_global.425
- ___block_literal_global.432
- ___block_literal_global.435
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.445
- ___block_literal_global.451
- ___block_literal_global.456
- ___block_literal_global.462
- ___block_literal_global.473
- ___block_literal_global.691
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AuthenticationServicesCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AuthenticationServicesCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AuthenticationServicesCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AuthenticationServicesCore
- _objc_msgSend$renamePasskeyWithCredentialID:newName:completionHandler:
- _objc_msgSend$renamePasskeywithIdentifier:newName:error:
- _symbolic Sd
CStrings:
+ "Cooldown for %s aborted."
+ "Cooldown for %s completed."
+ "Scheduling cooldown for %s."
+ "userIsEligibleForPasskeysWithICloudKeychain"
- "Asked to rename passkey %{public}@ to %{private}@."
- "Cooldown for %f aborted."
- "Cooldown for %f completed."
- "Scheduling cooldown for %f."
- "Unentitled client attempted to rename passkey."
- "renamePasskeyWithCredentialID:newName:completionHandler:"
- "renamePasskeywithIdentifier:newName:error:"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B@\"NSError\">32"

```
