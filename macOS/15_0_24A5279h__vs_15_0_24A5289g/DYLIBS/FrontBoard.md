## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/Versions/A/FrontBoard`

```diff

-935.0.0.0.0
-  __TEXT.__text: 0x83754
+939.0.0.0.0
+  __TEXT.__text: 0x83e64
   __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x46dc
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x9db7
+  __TEXT.__objc_methlist: 0x479c
+  __TEXT.__const: 0x338
+  __TEXT.__cstring: 0x9e19
   __TEXT.__oslogstring: 0x5277
   __TEXT.__gcc_except_tab: 0x10e0
-  __TEXT.__unwind_info: 0x1b88
+  __TEXT.__unwind_info: 0x1b90
   __TEXT.__objc_classname: 0xfea
-  __TEXT.__objc_methname: 0xe6a1
-  __TEXT.__objc_methtype: 0x349d
-  __TEXT.__objc_stubs: 0xa780
+  __TEXT.__objc_methname: 0xe71b
+  __TEXT.__objc_methtype: 0x3533
+  __TEXT.__objc_stubs: 0xa800
   __DATA_CONST.__got: 0x868
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32c8
+  __DATA_CONST.__objc_selrefs: 0x3300
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x668
-  __AUTH_CONST.__const: 0x29f0
-  __AUTH_CONST.__cfstring: 0x7f40
-  __AUTH_CONST.__objc_const: 0xc648
+  __AUTH_CONST.__const: 0x2a20
+  __AUTH_CONST.__cfstring: 0x7f80
+  __AUTH_CONST.__objc_const: 0xc6e8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xbe0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2650
-  Symbols:   6701
-  CStrings:  1190
+  Functions: 2666
+  Symbols:   6722
+  CStrings:  1193
 
Symbols:
+ -[FBApplicationProcessLaunchTransaction add:]
+ -[FBApplicationProcessLaunchTransaction remove:]
+ -[FBProcess add:]
+ -[FBProcess remove:]
+ -[FBProcessManager add:]
+ -[FBProcessManager remove:]
+ -[FBScene _deactivateAndInvalidate:transitionContext:]
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.1
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.2
+ -[FBScene _deactivateAndInvalidate:transitionContext:].cold.3
+ -[FBScene add:]
+ -[FBScene invalidate:]
+ -[FBScene remove:]
+ -[FBSceneLayerManager add:]
+ -[FBSceneLayerManager remove:]
+ -[FBSceneManager add:]
+ -[FBSceneManager remove:]
+ -[FBSceneObserver sceneDidDeactivate:withContext:]
+ -[FBSceneObserver sceneDidInvalidate:withContext:]
+ -[FBSceneObserver sceneWillDeactivate:withContext:]
+ -[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]
+ -[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:].cold.1
+ -[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:].cold.2
+ GCC_except_table107
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table17
+ GCC_except_table40
+ __35-[FBSceneMonitorBehaviors isEqual:]_block_invoke.213
+ __50-[FBSceneObserver descriptionWithMultilinePrefix:]_block_invoke.83
+ __54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.362
+ __54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.cold.1
+ __54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.cold.2
+ __54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke.cold.3
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.334
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke.347
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_2.338
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_2.351
+ __68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3.355
+ ___54-[FBScene _deactivateAndInvalidate:transitionContext:]_block_invoke
+ ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke
+ ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_2
+ ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_3
+ ___68-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]_block_invoke_4
+ ___NSStringFromFBSceneLayerTypeMask_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v28?0Q8i16^B20l
+ ___block_descriptor_66_e8_32s40s_e5_v8?0l
+ _objc_msgSend$scene:deactivateAndInvalidate:withContext:block:
+ _objc_msgSend$sceneDidDeactivate:withContext:
+ _objc_msgSend$sceneDidInvalidate:withContext:
+ _objc_msgSend$sceneWillDeactivate:withContext:
+ _objc_msgSend$setError:
- -[FBScene _deactivateAndInvalidate:clientError:transitionContext:]
- -[FBScene _deactivateAndInvalidate:clientError:transitionContext:].cold.1
- -[FBScene _deactivateAndInvalidate:clientError:transitionContext:].cold.2
- -[FBScene _deactivateAndInvalidate:clientError:transitionContext:].cold.3
- -[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]
- -[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:].cold.1
- -[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:].cold.2
- GCC_except_table143
- GCC_except_table144
- GCC_except_table145
- GCC_except_table38
- _OUTLINED_FUNCTION_17
- __35-[FBSceneMonitorBehaviors isEqual:]_block_invoke.210
- __50-[FBSceneObserver descriptionWithMultilinePrefix:]_block_invoke.68
- __66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke.362
- __66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke.cold.1
- __66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke.cold.2
- __66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke.cold.3
- __66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke.334
- __66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke.347
- __66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2.338
- __66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2.351
- __66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_3.355
- ___66-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]_block_invoke
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_2
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_3
- ___66-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]_block_invoke_4
- ___block_descriptor_73_e8_32s40s48s_e5_v8?0l
- _objc_msgSend$scene:deactivateAndInvalidate:withError:block:
CStrings:
+ "-[FBScene _deactivateAndInvalidate:transitionContext:]"
+ "-[FBSceneWorkspace scene:deactivateAndInvalidate:withContext:block:]"
+ "call sceneDidDeactivate:withContext:"
+ "call sceneDidInvalidate:withContext:"
+ "call sceneWillDeactivate:withContext:"
+ "error != nil"
+ "v28@?0Q8i16^B20"
- "-[FBScene _deactivateAndInvalidate:clientError:transitionContext:]"
- "-[FBSceneWorkspace scene:deactivateAndInvalidate:withError:block:]"
- "clientError != nil"
- "externalScene"

```
