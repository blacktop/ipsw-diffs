## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-867.10.0.0.0
-  __TEXT.__text: 0x7be54
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0x4a60
-  __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x9ddb
-  __TEXT.__oslogstring: 0x4c04
-  __TEXT.__gcc_except_tab: 0x924
+867.111.0.0.0
+  __TEXT.__text: 0x7c238
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_methlist: 0x4a70
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0x9ee1
+  __TEXT.__oslogstring: 0x4bc2
+  __TEXT.__gcc_except_tab: 0x920
   __TEXT.__dlopen_cstrs: 0xfa
-  __TEXT.__unwind_info: 0x1b6c
+  __TEXT.__unwind_info: 0x1b88
   __TEXT.__objc_classname: 0x1049
-  __TEXT.__objc_methname: 0xea3a
+  __TEXT.__objc_methname: 0xea7c
   __TEXT.__objc_methtype: 0x3337
   __TEXT.__objc_stubs: 0xaa80
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x2568
+  __DATA_CONST.__const: 0x2570
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x136c0
-  __DATA_CONST.__objc_selrefs: 0x3368
+  __DATA_CONST.__objc_const: 0x136e0
+  __DATA_CONST.__objc_selrefs: 0x3370
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x640
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x7b20
+  __AUTH_CONST.__cfstring: 0x7bc0
   __AUTH_CONST.__objc_const: 0x2498
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__const: 0x880
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH.__objc_data: 0xe60
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x640
-  __DATA.__objc_superrefs: 0x220
-  __DATA.__objc_ivar: 0x8c8
-  __DATA.__data: 0x1960
-  __DATA.__bss: 0x128
+  __DATA.__objc_ivar: 0x8cc
+  __DATA.__data: 0x1978
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2913
-  Symbols:   9982
-  CStrings:  4528
+  Functions: 2916
+  Symbols:   9989
+  CStrings:  4535
 
Symbols:
+ -[FBDisplayManager initWithInitializationCompletion:]
+ -[FBDisplayManager initWithTransformer:]
+ _BSDispatchBlockCreateWithQualityOfService
+ _OBJC_IVAR_$_FBWorkspaceDomain._bgUserInitiatedAttributes
+ ___30-[FBWorkspace _setConnection:]_block_invoke.172
+ ___38-[FBWorkspace _connect:withAssertion:]_block_invoke.181
+ ___38-[FBWorkspace _connect:withAssertion:]_block_invoke_2.182
+ ___38-[FBWorkspace _connect:withAssertion:]_block_invoke_3
+ ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke.141
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.354
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_2.366
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_3.380
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.326
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.332
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.340
+ ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke.305
+ ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2.309
+ ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_3.313
+ ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.244
+ ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.272
+ ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke_2.273
+ ___block_literal_global.123
+ ___block_literal_global.139
+ ___block_literal_global.162
+ ___block_literal_global.189
+ ___block_literal_global.199
+ ___block_literal_global.291
+ ___block_literal_global.348
+ ___block_literal_global.508
+ _objc_msgSend$handleForIdentifier:error:
+ _objc_msgSend$tokenWithHostEndpoint:workspace:identifier:
+ _qos_class_self
- -[FBDisplayManager updateTransformsWithCompletion:]
- ___30-[FBWorkspace _setConnection:]_block_invoke.171
- ___38-[FBWorkspace _connect:withAssertion:]_block_invoke.180
- ___38-[FBWorkspace _connect:withAssertion:]_block_invoke_2.183
- ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke.138
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.353
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_2.365
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_3.379
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.325
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.331
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.339
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke.304
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2.308
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_3.312
- ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.243
- ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.271
- ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke_2.272
- ___block_literal_global.120
- ___block_literal_global.136
- ___block_literal_global.159
- ___block_literal_global.188
- ___block_literal_global.198
- ___block_literal_global.290
- ___block_literal_global.347
- ___block_literal_global.507
- _objc_msgSend$_updateTransformsWithCompletion:
- _objc_msgSend$initWithIdentifier:workspace:endpoint:
CStrings:
+ "\x1f\b"
+ "-initWithInitializationCompletion: is not allowed - call +sharedInstance instead"
+ "-initWithTransformer: is not allowed - call +sharedInstance instead"
+ "Bootstrap-BackgroundUserInitiated"
+ "T@\"NSString\",?,R,C"
+ "_bgUserInitiatedAttributes"
+ "background-user-initiated"
+ "handleForIdentifier:error:"
+ "initWithInitializationCompletion:"
+ "initWithTransformer:"
+ "processIdentity %@ is not equal to handleIdentity %@"
+ "tokenWithHostEndpoint:workspace:identifier:"
- "\x1f\a"
- "%{public}@: RBSProcessHandle has a non-equal identity %{public}@."
- "_updateTransformsWithCompletion:"
- "initWithIdentifier:workspace:endpoint:"
- "updateTransformsWithCompletion:"

```
