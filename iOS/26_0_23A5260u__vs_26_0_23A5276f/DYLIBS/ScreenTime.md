## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-571.0.0.0.0
-  __TEXT.__text: 0x4e20
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x72c
+580.0.0.0.0
+  __TEXT.__text: 0x5764
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x242
-  __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__oslogstring: 0x502
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__cstring: 0x306
+  __TEXT.__gcc_except_tab: 0x1cc
+  __TEXT.__oslogstring: 0x548
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x141f
+  __TEXT.__objc_methname: 0x1639
   __TEXT.__objc_methtype: 0x50c
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x2b0
+  __TEXT.__objc_stubs: 0x1000
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x378
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x548
+  __DATA_CONST.__objc_selrefs: 0x5c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1c0
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0xf20
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x2a0
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 506E823B-9CB2-32CB-B90E-35A414673F84
-  Functions: 165
-  Symbols:   736
-  CStrings:  342
+  UUID: ACB46C0C-3945-3E27-94F0-5CC4C4407CFC
+  Functions: 183
+  Symbols:   806
+  CStrings:  368
 
Symbols:
+ +[STWebRemoteViewController cacheWebViewController:]
+ +[STWebRemoteViewController dequeueWebViewController]
+ +[STWebRemoteViewController sharedCache]
+ +[STWebRemoteViewController sharedCache].cold.1
+ -[STWebpageController _changeUsageStateIfNeeded:completionHandler:]
+ -[STWebpageController _installRemoteViewController:]
+ -[STWebpageController _installRemoteViewController:].cold.1
+ -[STWebpageController _installRemoteViewControllerIfNeededWithCompletionHandler:]
+ -[STWebpageController _installRemoteViewControllerOnMainThreadIfNeededWithCompletionHandler:]
+ -[STWebpageController _uninstallRemoteViewControllerIfNeeded]
+ -[STWebpageController _uninstallRemoteViewControllerIfNeeded].cold.1
+ -[STWebpageController _uninstallRemoteViewControllerOnMainThreadIfNeeded]
+ GCC_except_table2
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSThread
+ __OBJC_$_CLASS_PROP_LIST_STWebRemoteViewController
+ ___40+[STWebRemoteViewController sharedCache]_block_invoke
+ ___44-[STWebpageController setCurrentUsageState:]_block_invoke_2
+ ___67-[STWebpageController _changeUsageStateIfNeeded:completionHandler:]_block_invoke
+ ___67-[STWebpageController _changeUsageStateIfNeeded:completionHandler:]_block_invoke.cold.1
+ ___73-[STWebpageController _uninstallRemoteViewControllerOnMainThreadIfNeeded]_block_invoke
+ ___81-[STWebpageController _installRemoteViewControllerIfNeededWithCompletionHandler:]_block_invoke
+ ___81-[STWebpageController _installRemoteViewControllerIfNeededWithCompletionHandler:]_block_invoke.27
+ ___81-[STWebpageController _installRemoteViewControllerIfNeededWithCompletionHandler:]_block_invoke.27.cold.1
+ ___81-[STWebpageController _installRemoteViewControllerIfNeededWithCompletionHandler:]_block_invoke.28
+ ___81-[STWebpageController _installRemoteViewControllerIfNeededWithCompletionHandler:]_block_invoke.cold.1
+ ___93-[STWebpageController _installRemoteViewControllerOnMainThreadIfNeededWithCompletionHandler:]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32bs40w_e47_v24?0"STWebRemoteViewController"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.61
+ ___block_literal_global.63
+ ___block_literal_global.68
+ ___block_literal_global.70
+ _dispatch_once
+ _objc_msgSend$_changeUsageStateIfNeeded:completionHandler:
+ _objc_msgSend$_installRemoteViewController:
+ _objc_msgSend$_installRemoteViewControllerIfNeededWithCompletionHandler:
+ _objc_msgSend$_installRemoteViewControllerOnMainThreadIfNeededWithCompletionHandler:
+ _objc_msgSend$_uninstallRemoteViewControllerIfNeeded
+ _objc_msgSend$_uninstallRemoteViewControllerOnMainThreadIfNeeded
+ _objc_msgSend$addObject:
+ _objc_msgSend$cacheWebViewController:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$dequeueWebViewController
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$removeFromParentViewController
+ _objc_msgSend$removeFromSuperview
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$sharedCache
+ _objc_msgSend$willMoveToParentViewController:
+ _objc_retainAutoreleaseReturnValue
+ _objc_sync_enter
+ _objc_sync_exit
+ _sharedCache.onceToken
+ _sharedCache.sharedCache
- -[STWebpageController _changeUsageState:errorHandler:]
- ___31-[STWebpageController loadView]_block_invoke
- ___31-[STWebpageController loadView]_block_invoke.cold.1
- ___44-[STWebpageController setCurrentUsageState:]_block_invoke.cold.1
- ___54-[STWebpageController _changeUsageState:errorHandler:]_block_invoke
- ___block_descriptor_40_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32w_e47_v24?0"STWebRemoteViewController"8"NSError"16lw32l8
- ___block_literal_global.46
- ___block_literal_global.48
- ___block_literal_global.54
- ___block_literal_global.56
- _objc_msgSend$_changeUsageState:errorHandler:
- _objc_msgSend$removeObserver:forKeyPath:context:
- _objc_release_x27
CStrings:
+ "-_installRemoteViewController: must be called on the main thread"
+ "-_uninstallRemoteViewControllerIfNeeded must be called on the main thread"
+ "Failed to set up cached remote view controller with error: %{public}@"
+ "H:|[remoteView]|"
+ "STWebRemoteViewControllerSharedCacheLock"
+ "STWebpageController.m"
+ "T@\"NSMutableArray\",R"
+ "V:|[remoteView]|"
+ "_changeUsageStateIfNeeded:completionHandler:"
+ "_installRemoteViewController:"
+ "_installRemoteViewControllerIfNeededWithCompletionHandler:"
+ "_installRemoteViewControllerOnMainThreadIfNeededWithCompletionHandler:"
+ "_uninstallRemoteViewControllerIfNeeded"
+ "_uninstallRemoteViewControllerOnMainThreadIfNeeded"
+ "addObject:"
+ "cacheWebViewController:"
+ "currentHandler"
+ "dequeueWebViewController"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "isMainThread"
+ "remoteView"
+ "removeFromParentViewController"
+ "removeFromSuperview"
+ "removeObjectAtIndex:"
+ "removeObserver:forKeyPath:"
+ "sharedCache"
+ "willMoveToParentViewController:"
- "H:|[blockingView]|"
- "V:|[blockingView]|"
- "_changeUsageState:errorHandler:"
- "blockingView"
- "removeObserver:forKeyPath:context:"

```
