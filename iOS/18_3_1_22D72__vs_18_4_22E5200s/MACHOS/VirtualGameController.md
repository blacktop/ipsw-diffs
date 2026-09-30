## VirtualGameController

> `/System/Library/Frameworks/GameController.framework/VirtualGameController.bundle/VirtualGameController`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x72f8
+12.4.10.0.0
+  __TEXT.__text: 0x74f8
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x3e8
-  __TEXT.__const: 0xd0
-  __TEXT.__objc_methname: 0x1276
+  __TEXT.__objc_methlist: 0x524
+  __TEXT.__const: 0x110
+  __TEXT.__objc_methname: 0x122b
   __TEXT.__cstring: 0x659
   __TEXT.__objc_classname: 0x107
   __TEXT.__objc_methtype: 0x49b
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__gcc_except_tab: 0x128
+  __TEXT.__unwind_info: 0x238
   __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA.__objc_const: 0xe10
-  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_const: 0xbb8
+  __DATA.__objc_selrefs: 0x6d8
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x280
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 124
-  Symbols:   617
+  Functions: 138
+  Symbols:   634
   CStrings:  399
 
Symbols:
+ +[GCControllerViewFeedback sharedInstance].cold.1
+ -[_GCVirtualControllerImpl initWithConfiguration:].cold.1
+ -[_GCVirtualControllerImpl updateConfigurationForElement:configuration:].cold.1
+ GCC_except_table4
+ GCVirtualControllerAdditiveVibrancyEffectView.cold.1
+ GCVirtualControllerSaturationVibrancyEffect.cold.1
+ VirtualControllerBundle.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __52-[_GCVirtualControllerImpl connectWithReplyHandler:]_block_invoke.cold.1
+ __61-[_GCVirtualControllerImpl(Internal) refreshViewForKeyWindow]_block_invoke.cold.1
+ __GCAnalyticsSendVirtualControllerConnectedEvent_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS__GCVirtualControllerImpl
+ _gc_log_virtualcontroller.cold.1
- __OBJC_$_INSTANCE_METHODS__GCVirtualControllerImpl(Internal)

```
