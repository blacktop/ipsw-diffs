## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-946.3.2.0.0
-  __TEXT.__text: 0x83dd4
-  __TEXT.__auth_stubs: 0x1450
+946.5.3.0.0
+  __TEXT.__text: 0x83a60
+  __TEXT.__auth_stubs: 0x1470
   __TEXT.__objc_methlist: 0x7850
   __TEXT.__const: 0xa44
   __TEXT.__gcc_except_tab: 0x166c

   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__objc_const_ax: 0xcec
-  __TEXT.__unwind_info: 0x2b88
+  __TEXT.__unwind_info: 0x2b74
   __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_classname: 0x1772
-  __TEXT.__objc_methname: 0x1d82f
-  __TEXT.__objc_methtype: 0x684a
-  __TEXT.__objc_stubs: 0x144c0
-  __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x2760
+  __TEXT.__objc_methname: 0x1d8e3
+  __TEXT.__objc_methtype: 0x6882
+  __TEXT.__objc_stubs: 0x144a0
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x2770
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x108b0
+  __DATA_CONST.__objc_const: 0x108f8
   __DATA_CONST.__objc_selrefs: 0x5f68
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0x968
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__objc_const: 0x2f60
   __AUTH_CONST.__cfstring: 0x2fe0

   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH_CONST.__auth_got: 0xa48
   __AUTH.__objc_data: 0x2270
   __AUTH.__data: 0x168
-  __DATA.__objc_protorefs: 0xb0
-  __DATA.__objc_classrefs: 0x968
-  __DATA.__objc_superrefs: 0x288
   __DATA.__objc_ivar: 0xb40
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x2480

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3596
-  Symbols:   12951
-  CStrings:  6218
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 3595
+  Symbols:   12952
+  CStrings:  6225
 
Symbols:
+ ___136-[QLPreviewCollection startTransitionWithSourceViewProvider:transitionController:presenting:useInteractiveTransition:completionHandler:]_block_invoke.177
+ ___44-[QLPreviewController(DocumentMenu) export:]_block_invoke.103
+ ___52-[QLPreviewController(DocumentMenu) _printDocument:]_block_invoke.101
+ ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke.167
+ ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke_2.168
+ ___54-[QLRemoteItemViewController _registerLoadingHandler:]_block_invoke.310
+ ___64-[QLPreviewCollection pageViewController:viewControllerAtIndex:]_block_invoke.200
+ ___73-[QLPreviewCollectionHostContext invalidateServiceWithCompletionHandler:]_block_invoke.28
+ ___73-[QLPreviewController(DocumentMenu) updateTitleMenuAndDocumentProperties]_block_invoke.104
+ ___76+[QLPreviewCollection(Remote) remotePreviewCollectionWithCompletionHandler:]_block_invoke.384
+ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.105
+ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.118
+ ___block_literal_global.151
+ ___block_literal_global.155
+ ___block_literal_global.181
+ ___block_literal_global.217
+ ___block_literal_global.219
+ ___block_literal_global.263
+ ___block_literal_global.265
+ ___block_literal_global.268
+ ___block_literal_global.27
+ ___block_literal_global.299
+ ___block_literal_global.312
+ ___block_literal_global.319
+ ___block_literal_global.323
+ ___block_literal_global.388
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_QuickLook
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_QuickLook
- ___136-[QLPreviewCollection startTransitionWithSourceViewProvider:transitionController:presenting:useInteractiveTransition:completionHandler:]_block_invoke.176
- ___44-[QLPreviewController(DocumentMenu) export:]_block_invoke.102
- ___52-[QLPreviewController(DocumentMenu) _printDocument:]_block_invoke.100
- ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke.166
- ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke_2.167
- ___54-[QLRemoteItemViewController _registerLoadingHandler:]_block_invoke.308
- ___64-[QLPreviewCollection pageViewController:viewControllerAtIndex:]_block_invoke.199
- ___73-[QLPreviewCollectionHostContext invalidateServiceWithCompletionHandler:]_block_invoke.19
- ___73-[QLPreviewController(DocumentMenu) updateTitleMenuAndDocumentProperties]_block_invoke.103
- ___76+[QLPreviewCollection(Remote) remotePreviewCollectionWithCompletionHandler:]_block_invoke.372
- ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.104
- ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.117
- ___block_literal_global.143
- ___block_literal_global.150
- ___block_literal_global.154
- ___block_literal_global.18
- ___block_literal_global.180
- ___block_literal_global.215
- ___block_literal_global.218
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.256
- ___block_literal_global.287
- ___block_literal_global.311
- ___block_literal_global.318
- ___block_literal_global.376
- _keypath_setTm
- _objc_msgSend$viewWillAppear:
CStrings:
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIWindow\",?,&,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R,N"
+ "Td,?,R,N"
+ "Tq,?,N"
+ "Tq,?,R,N"
+ "navigationBarTopOffsetWithCompletionHandler:"
+ "playerViewController:willTransitionToVisibilityOfContextualActions:"
+ "v24@0:8@?<v@?f>16"
+ "v28@0:8@\"AVPlayerViewController\"16B24"
- "T@\"NSDictionary\",R,N"
- "T@\"NSString\",C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@\"UIWindow\",&,N"
- "TB,N"
- "TB,N,GisSecureTextEntry"
- "Tq,N"
- "Tq,R,N"

```
