## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-867.3.1.0.0
-  __TEXT.__text: 0x7b128
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x4a10
+867.8.2.0.0
+  __TEXT.__text: 0x7be54
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x4a60
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x9d7b
-  __TEXT.__oslogstring: 0x4a80
+  __TEXT.__cstring: 0x9ddb
+  __TEXT.__oslogstring: 0x4c04
   __TEXT.__gcc_except_tab: 0x924
   __TEXT.__dlopen_cstrs: 0xfa
-  __TEXT.__unwind_info: 0x1b4c
-  __TEXT.__objc_classname: 0x1046
-  __TEXT.__objc_methname: 0xe9e8
+  __TEXT.__unwind_info: 0x1b6c
+  __TEXT.__objc_classname: 0x1049
+  __TEXT.__objc_methname: 0xea3a
   __TEXT.__objc_methtype: 0x3337
-  __TEXT.__objc_stubs: 0xaa40
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x2588
+  __TEXT.__objc_stubs: 0xaa80
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x2568
   __DATA_CONST.__objc_classlist: 0x2b0
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x136c0
-  __DATA_CONST.__objc_selrefs: 0x3350
+  __DATA_CONST.__objc_selrefs: 0x3368
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x7ae0
-  __AUTH_CONST.__objc_const: 0x2458
+  __AUTH_CONST.__cfstring: 0x7b20
+  __AUTH_CONST.__objc_const: 0x2498
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__const: 0x880
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x640
   __DATA.__objc_superrefs: 0x220
   __DATA.__objc_ivar: 0x8c8
   __DATA.__data: 0x1960
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x128
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2896
-  Symbols:   9937
-  CStrings:  4514
+  Functions: 2913
+  Symbols:   9982
+  CStrings:  4528
 
Symbols:
+ -[FBLocalSynchronousSceneClientProvider dealloc]
+ -[FBProcess _bootstrapAndExec].cold.5
+ -[FBProcess _configureBundleInfo]
+ -[FBProcess _configureBundleInfo].cold.1
+ -[FBProcess _configureIntrinsicsFromHandle:].cold.4
+ -[FBScene _objc_initiateDealloc]
+ -[FBSceneLayerManager _objc_initiateDealloc]
+ -[FBSceneManager dealloc]
+ -[FBSceneManagerObserver delegateReceivesActions]
+ -[FBSceneObserver delegateReceivesActions]
+ -[FBSceneObserver observerHandlesActions]
+ -[FBSceneWorkspace _objc_initiateDealloc]
+ -[NSSet(FBSceneWorkspace) fbs_singleLineDescriptionOfObjects]
+ GCC_except_table89
+ __OBJC_$_CATEGORY_NSSet_$_FBSceneWorkspace
+ __OBJC_$_INSTANCE_METHODS_NSSet(FBSceneWorkspace)
+ ___30-[FBProcess _bootstrapAndExec]_block_invoke.88
+ ___30-[FBProcess _bootstrapAndExec]_block_invoke_2.89
+ ___38-[FBSceneLayerManager _initWithScene:]_block_invoke
+ ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke.138
+ ___47-[FBSceneWorkspace _initWithIdentifier:legacy:]_block_invoke.24
+ ___47-[FBSceneWorkspace _initWithIdentifier:legacy:]_block_invoke.39
+ ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.232
+ ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.239
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.353
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_2.365
+ ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_3.379
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.331
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.339
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.cold.1
+ ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.cold.2
+ ___61-[NSSet(FBSceneWorkspace) fbs_singleLineDescriptionOfObjects]_block_invoke
+ ___62-[FBScene _applyUpdatedSettings:transitionContext:completion:]_block_invoke.258
+ ___62-[FBScene _applyUpdatedSettings:transitionContext:completion:]_block_invoke.274
+ ___62-[FBScene _applyUpdatedSettings:transitionContext:completion:]_block_invoke.275
+ ___66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke.304
+ ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke.304
+ ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2.308
+ ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_3.312
+ ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.243
+ ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.271
+ ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke_2.272
+ ___93-[FBScene initWithDefiniton:remnant:settings:initialClientSettings:clientProvider:workspace:]_block_invoke_4
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8u64l8s48l8s56l8
+ ___block_literal_global.120
+ ___block_literal_global.124
+ ___block_literal_global.134
+ ___block_literal_global.135
+ ___block_literal_global.136
+ ___block_literal_global.159
+ ___block_literal_global.188
+ ___block_literal_global.198
+ ___block_literal_global.231
+ ___block_literal_global.347
+ ___block_literal_global.507
+ ___block_literal_global.53
+ ___block_literal_global.55
+ __class_setCustomDeallocInitiation
+ __initWithIdentifier:legacy:.onceToken
+ __initWithScene:.onceToken
+ __objc_deallocOnMainThreadHelper
+ _dispatch_async_f
+ _initWithDefiniton:remnant:settings:initialClientSettings:clientProvider:workspace:.onceToken
+ _objc_msgSend$_configureBundleInfo
+ _objc_msgSend$_synchronizationQueue
+ _objc_msgSend$delegateReceivesActions
+ _objc_msgSend$fbs_singleLineDescriptionOfObjects
+ _objc_msgSend$observerHandlesActions
+ _pthread_main_np
- -[FBSceneManagerObserver delegateHandlesActions]
- -[FBSceneObserver delegateHandlesActions]
- GCC_except_table88
- ___30-[FBProcess _bootstrapAndExec]_block_invoke.87
- ___30-[FBProcess _bootstrapAndExec]_block_invoke_2.88
- ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke.134
- ___47-[FBSceneWorkspace _initWithIdentifier:legacy:]_block_invoke.36
- ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.229
- ___48-[FBScene _activateWithTransitionContext:error:]_block_invoke.236
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke.367
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_2.379
- ___54-[FBSceneWorkspace didReceiveSceneRequest:fromHandle:]_block_invoke_3.393
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.335
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.341
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke.353
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke_2
- ___57-[FBSceneWorkspace scene:didReceiveActions:forExtension:]_block_invoke_2.345
- ___62-[FBScene _applyUpdatedSettings:transitionContext:completion:]_block_invoke.255
- ___62-[FBScene _applyUpdatedSettings:transitionContext:completion:]_block_invoke.269
- ___62-[FBScene _applyUpdatedSettings:transitionContext:completion:]_block_invoke.271
- ___66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke.301
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke.301
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2.305
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_3.309
- ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.240
- ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke.268
- ___82-[FBSceneWorkspace scene:handleUpdateToSettings:withTransitionContext:completion:]_block_invoke_2.269
- ___block_descriptor_32_e31_24?0"NSString"8"BSAction"16l
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8u56l8s48l8
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.130
- ___block_literal_global.131
- ___block_literal_global.132
- ___block_literal_global.155
- ___block_literal_global.194
- ___block_literal_global.228
- ___block_literal_global.318
- ___block_literal_global.331
- ___block_literal_global.337
- ___block_literal_global.361
- ___block_literal_global.51
- _objc_msgSend$bs_reduce:block:
- _objc_msgSend$delegateHandlesActions
- _objc_msgSend$handleForIdentifier:error:
CStrings:
+ "%{public}@: RBSProcessHandle has a non-equal identity %{public}@."
+ "3`"
+ "Delegate"
+ "Error looking up handle: %{public}@"
+ "FBLocalSynchronousSceneClientProvider should not deallocate"
+ "FBSceneManager should not deallocate"
+ "Observer"
+ "[%{public}@] %{public}s %{public}@ handled action(s): %@"
+ "[%{public}@] %{public}s %{public}@ handled no actions."
+ "[%{public}@] Dropping unhandled action(s): %{public}@"
+ "[%{public}@] Handing all actions to delegate: %@"
+ "[%{public}@] Handing all actions to legacy delegate: %@"
+ "[%{public}@] Legacy scene manager has no delegate; dropping unhandled action(s): %{public}@"
+ "_configureBundleInfo"
+ "_objc_initiateDealloc"
+ "_rbsHandle != nil"
+ "_synchronizationQueue"
+ "delegateReceivesActions"
+ "fbs_singleLineDescriptionOfObjects"
+ "observerHandlesActions"
- ", %@"
- "@24@?0@\"NSString\"8@\"BSAction\"16"
- "Dropping actions since scene delegate does not implement handler: %{public}@"
- "bs_reduce:block:"
- "delegateHandlesActions"
- "handleForIdentifier:error:"

```
