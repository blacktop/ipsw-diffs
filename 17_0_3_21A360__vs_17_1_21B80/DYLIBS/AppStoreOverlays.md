## AppStoreOverlays

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays`

```diff

-6.0.44.0.0
-  __TEXT.__text: 0x5df8
+6.1.6.0.0
+  __TEXT.__text: 0x6000
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x8a8
+  __TEXT.__objc_methlist: 0x8e0
   __TEXT.__const: 0x90
   __TEXT.__oslogstring: 0x8ec
-  __TEXT.__cstring: 0x5b6
+  __TEXT.__cstring: 0x641
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x216
-  __TEXT.__objc_methname: 0x18d2
-  __TEXT.__objc_methtype: 0x5f4
-  __TEXT.__objc_stubs: 0x1380
+  __TEXT.__unwind_info: 0x24c
+  __TEXT.__objc_classname: 0x212
+  __TEXT.__objc_methname: 0x19c2
+  __TEXT.__objc_methtype: 0x62d
+  __TEXT.__objc_stubs: 0x1460
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12a0
-  __DATA_CONST.__objc_selrefs: 0x658
-  __AUTH_CONST.__cfstring: 0x360
+  __DATA_CONST.__objc_const: 0x12c0
+  __DATA_CONST.__objc_selrefs: 0x6a8
+  __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__auth_got: 0x218
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xd8
+  __DATA.__objc_classrefs: 0xe8
   __DATA.__objc_superrefs: 0x50
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x420

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF5AC572-4757-389F-8214-DD22958C706C
-  Functions: 205
-  Symbols:   917
-  CStrings:  504
+  UUID: 00DFBA80-1907-3EC7-85C0-5A50EDD7FAE0
+  Functions: 210
+  Symbols:   939
+  CStrings:  522
 
Symbols:
+ -[ASOOverlayTransitionContext addAnimationBlockInternal:]
+ -[ASOOverlayTransitionContext endFrameInternal]
+ -[ASOOverlayTransitionContext setEndFrameInternal:]
+ -[ASOOverlayTransitionContext setStartFrameInternal:]
+ -[ASOOverlayTransitionContext startFrameInternal]
+ -[ASOOverlayViewController willStartPresentingOverlay:transitionContext:]
+ _ASOOverlayConfigurationParameterHostBundleID
+ _ASOOverlayConfigurationParameterHostIdiom
+ _ASOOverlayConfigurationParameterHostSceneIdentifier
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_UIDevice
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASORemoteOverlayHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASORemoteOverlayHost
+ __OBJC_$_PROTOCOL_REFS_ASORemoteOverlayHost
+ __OBJC_LABEL_PROTOCOL_$_ASORemoteOverlayHost
+ __OBJC_PROTOCOL_$_ASORemoteOverlayHost
+ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.21
+ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.22
+ ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke.16
+ _objc_msgSend$_scene
+ _objc_msgSend$_sceneIdentifier
+ _objc_msgSend$addAnimationBlock:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$currentDevice
+ _objc_msgSend$endFrameInternal
+ _objc_msgSend$mainBundle
+ _objc_msgSend$startFrameInternal
+ _objc_msgSend$userInterfaceIdiom
+ _objc_msgSend$willStartPresentingOverlay:transitionContext:
- -[ASOOverlayViewController willStartPresentingOverlay:]
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASORemoteContextProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_ASORemoteContextProvider
- __OBJC_$_PROTOCOL_REFS_ASORemoteContextProvider
- __OBJC_LABEL_PROTOCOL_$_ASORemoteContextProvider
- __OBJC_PROTOCOL_$_ASORemoteContextProvider
- ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.19
- ___71-[ASORemoteOverlay remoteStoreOverlayWillStartDismissing:executeBlock:]_block_invoke.20
- ___71-[ASORemoteOverlay remoteStoreOverlayWillStartPresenting:executeBlock:]_block_invoke.12
- _objc_msgSend$endFrame
- _objc_msgSend$startFrame
- _objc_msgSend$willStartPresentingOverlay:
CStrings:
+ "@\"<ASORemoteOverlayHost>\""
+ "ASOOverlayConfigurationParameterHostBundleID"
+ "ASOOverlayConfigurationParameterHostIdiom"
+ "ASOOverlayConfigurationParameterHostSceneIdentifier"
+ "ASORemoteOverlayHost"
+ "T@\"<ASORemoteOverlayHost>\",W,N,V_contextProvider"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
+ "_sceneIdentifier"
+ "addAnimationBlockInternal:"
+ "bundleIdentifier"
+ "currentDevice"
+ "endFrameInternal"
+ "mainBundle"
+ "setEndFrameInternal:"
+ "setStartFrameInternal:"
+ "startFrameInternal"
+ "userInterfaceIdiom"
+ "v32@0:8@\"ASORemoteOverlay\"16@\"ASOOverlayTransitionContext\"24"
+ "willStartPresentingOverlay:transitionContext:"
- "@\"<ASORemoteContextProvider>\""
- "ASORemoteContextProvider"
- "T@\"<ASORemoteContextProvider>\",W,N,V_contextProvider"
- "willStartPresentingOverlay:"

```
