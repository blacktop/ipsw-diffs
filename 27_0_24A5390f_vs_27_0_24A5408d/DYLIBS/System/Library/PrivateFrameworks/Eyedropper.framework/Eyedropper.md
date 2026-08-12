## Eyedropper

> `/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper`

```diff

-9127.0.53.0.0
-  __TEXT.__text: 0x66c4
-  __TEXT.__objc_methlist: 0xc8c
+9127.0.81.0.0
+  __TEXT.__text: 0x6d5c
+  __TEXT.__objc_methlist: 0xcd4
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x18f
+  __TEXT.__cstring: 0x190
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb40
+  __DATA_CONST.__objc_selrefs: 0xb88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__got: 0x210
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x1140
+  __AUTH_CONST.__objc_const: 0x11a0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_ivar: 0xac
   __DATA.__data: 0x488
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 147
-  Symbols:   701
+  Functions: 153
+  Symbols:   723
   CStrings:  19
 
Symbols:
+ -[EDAppDelegate _attachedSceneDelegatePreferringDisplay:]
+ -[EDAppDelegate _attachedSceneDelegate]
+ -[EDAppDelegate _performFloatEyeDropper]
+ -[EDAppDelegate _performShowEyeDropperForRequestedDisplay:]
+ -[EDAppDelegate _runDeferredEyeDropperOpsIfReady]
+ -[EDAppDelegate _sceneDidActivate:]
+ GCC_except_table18
+ GCC_except_table30
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_IVAR_$_EDAppDelegate._hasPendingFloat
+ _OBJC_IVAR_$_EDAppDelegate._hasPendingShow
+ _OBJC_IVAR_$_EDAppDelegate._pendingShowDisplayHardwareIdentifier
+ _UISceneDidActivateNotification
+ ___59-[EDAppDelegate _performShowEyeDropperForRequestedDisplay:]_block_invoke
+ _objc_msgSend$_attachedSceneDelegate
+ _objc_msgSend$_attachedSceneDelegatePreferringDisplay:
+ _objc_msgSend$_performFloatEyeDropper
+ _objc_msgSend$_performShowEyeDropperForRequestedDisplay:
+ _objc_msgSend$_runDeferredEyeDropperOpsIfReady
+ _objc_msgSend$activationState
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_self
+ _objc_retain_x9
- GCC_except_table14
- GCC_except_table26
- ___49-[EDAppDelegate beginShowingEyeDropper:settings:]_block_invoke_2
```
