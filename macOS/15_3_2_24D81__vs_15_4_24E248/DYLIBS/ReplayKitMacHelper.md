## ReplayKitMacHelper

> `/System/Library/PrivateFrameworks/ReplayKitMacHelper.framework/Versions/A/ReplayKitMacHelper`

```diff

-595.11.1.0.0
-  __TEXT.__text: 0x91e0
+610.5.1.5.1
+  __TEXT.__text: 0x9168
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0xa2c
+  __TEXT.__objc_methlist: 0xfac
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0x9a
   __TEXT.__cstring: 0x74b
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x3e7
   __TEXT.__objc_methname: 0x2c55
   __TEXT.__objc_methtype: 0xe38

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_selrefs: 0xc18
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x500
   __AUTH_CONST.__cfstring: 0x400
-  __AUTH_CONST.__objc_const: 0x3c90
+  __AUTH_CONST.__objc_const: 0x3238
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x500

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01C322A3-AF96-3381-9A02-695FF2AB2175
-  Functions: 263
-  Symbols:   959
+  UUID: 464D19E9-53EF-300D-817F-4226721BAF34
+  Functions: 268
+  Symbols:   964
   CStrings:  695
 
Symbols:
+ +[NSXPCInterface(BroadcastActivityViewServiceExtension) __RPBroadcastActivity_viewServiceExtensionInterface].cold.1
+ +[NSXPCInterface(BroadcastActivityViewServiceExtension) __RPBroadcastActivity_viewServiceHostInterface].cold.1
+ +[NSXPCInterface(VideoEditorViewServiceExtension) __RPVideoEditor_viewServiceExtensionInterface].cold.1
+ +[NSXPCInterface(VideoEditorViewServiceExtension) __RPVideoEditor_viewServiceHostInterface].cold.1
+ +[SCCatalystMacOSBridge shared].cold.1
Functions:
~ +[NSXPCInterface(BroadcastActivityViewServiceExtension) __RPBroadcastActivity_viewServiceHostInterface] : 84 -> 68
~ +[NSXPCInterface(BroadcastActivityViewServiceExtension) __RPBroadcastActivity_viewServiceExtensionInterface] : 84 -> 68
~ +[SCCatalystMacOSBridge shared] : 84 -> 68
~ ___86-[RPRemoteWindowController setHostWindowFrame:withClientWindowSync:blurAndShadowSync:]_block_invoke : 220 -> 228
~ -[RPRemoteWindowController dimFrame] : 68 -> 72
~ -[RPDimAndShadowWindow continueTransitionInWithIdentityLayerTransformAfterDelay:animate:currentMediaTime:] : 580 -> 576
~ -[RPDimAndShadowWindow animateLayersToFrame:oldFrame:] : 664 -> 632
~ -[RPBlurWindow continueBlurWithIdentityLayerTransformAfterDelay:animate:currentMediaTime:] : 472 -> 468
~ -[ReplayKitMacHelperClass presentVideoEditorSheetOverUIWindow:withVideoURL:handler:] : 1400 -> 1380
~ ___84-[ReplayKitMacHelperClass presentVideoEditorSheetOverUIWindow:withVideoURL:handler:]_block_invoke : 220 -> 216
~ ___84-[ReplayKitMacHelperClass presentVideoEditorSheetOverUIWindow:withVideoURL:handler:]_block_invoke_2 : 612 -> 600
~ -[ReplayKitMacHelperClass presentBroadcastPickerAsContextMenu:sourceWindowSize:sourceViewFrame:hostInfo:completion:] : 1932 -> 1916
~ __116-[ReplayKitMacHelperClass presentBroadcastPickerAsContextMenu:sourceWindowSize:sourceViewFrame:hostInfo:completion:]_block_invoke.95 : 204 -> 200
~ ___116-[ReplayKitMacHelperClass presentBroadcastPickerAsContextMenu:sourceWindowSize:sourceViewFrame:hostInfo:completion:]_block_invoke_2 : 412 -> 400
~ -[ReplayKitMacHelperClass presentBroadcastActivitySheet] : 172 -> 168
~ ___56-[ReplayKitMacHelperClass presentBroadcastActivitySheet]_block_invoke : 888 -> 884
~ +[NSXPCInterface(VideoEditorViewServiceExtension) __RPVideoEditor_viewServiceHostInterface] : 84 -> 68
~ +[NSXPCInterface(VideoEditorViewServiceExtension) __RPVideoEditor_viewServiceExtensionInterface] : 84 -> 68
~ +[NSString(ReplayKitString) _rpLocalizationNotNeeded:] : 44 -> 8

```
