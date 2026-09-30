## MSMessageExtensionBalloonPlugin

> `/System/iOSSupport/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/Contents/MacOS/MSMessageExtensionBalloonPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x27800
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0x63a0
-  __TEXT.__objc_methlist: 0x2d04
+1491.200.63.0.0
+  __TEXT.__text: 0x280e4
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_stubs: 0x64c0
+  __TEXT.__objc_methlist: 0x2d7c
   __TEXT.__const: 0x494
-  __TEXT.__objc_methname: 0x835d
+  __TEXT.__objc_methname: 0x84cd
   __TEXT.__objc_classname: 0x63f
   __TEXT.__cstring: 0x142e
-  __TEXT.__objc_methtype: 0x1dae
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__oslogstring: 0x2874
+  __TEXT.__objc_methtype: 0x1dfe
+  __TEXT.__gcc_except_tab: 0x73c
+  __TEXT.__oslogstring: 0x29d4
   __TEXT.__swift5_typeref: 0x2c6
   __TEXT.__swift5_capture: 0x128
   __TEXT.__constg_swiftt: 0x2e4

   __TEXT.__swift_as_cont: 0x34
   __TEXT.__swift5_assocty: 0x28
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0xdf0
+  __TEXT.__unwind_info: 0xe20
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__const: 0xfe0
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x758
-  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__auth_got: 0x760
+  __DATA_CONST.__got: 0x610
   __DATA_CONST.__auth_ptr: 0xf8
-  __DATA.__objc_const: 0x3620
-  __DATA.__objc_selrefs: 0x2198
-  __DATA.__objc_ivar: 0x1e4
+  __DATA.__objc_const: 0x3658
+  __DATA.__objc_selrefs: 0x21f8
+  __DATA.__objc_ivar: 0x1e8
   __DATA.__objc_data: 0x998
   __DATA.__data: 0xb08
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1031
-  Symbols:   464
-  CStrings:  1833
+  Functions: 1039
+  Symbols:   467
+  CStrings:  1852
 
Symbols:
+ _IMBalloonBundleIdentifierLegacyAskToBuy
+ _IMBalloonPluginIdentifierIsReplyable
+ _OBJC_CLASS_$_IMFeatureFlags
CStrings:
+ "LiveBubble. Deferring remote view creation until on window. messageGUID: %@"
+ "LiveBubble. On window; retrying deferred remote view creation. messageGUID: %@"
+ "LiveBubble. Requesting remote view controller from extension for messageGUID: %@"
+ "LiveBubble. remoteProxy nil breakdown — remoteVC: %@ requestUUID: %@ hostContext: %@ auxConnection: %@"
+ "_addRemoteViewControllerAndConfigureExtension %@ firstResponder: %@"
+ "_needsRemoteViewCreationOnWindow"
+ "_shouldApplyMoveToWindowDeferral"
+ "_stageAppItem:replyingToMessage:skipShelf:completionHandler:"
+ "_stagePayload:skipShelf:completion:"
+ "_substituteNamesInAppItem:"
+ "balloonTailInsets"
+ "didMoveToWindow"
+ "firstResponder"
+ "isAppleCashRepliesEnabled"
+ "liveViewDidMoveToWindow:"
+ "setThreadReferenceBalloonBundleID:"
+ "setThreadReferenceMessageGUID:"
+ "sharedFeatureFlags"
+ "stageAppItem:replyingToMessage:skipShelf:completionHandler:"
+ "v44@0:8@\"MSMessage\"16@\"MSMessage\"24B32@?<v@?B@\"NSError\">36"
+ "v44@0:8@16@24B32@?36"
- "_addRemoteViewControllerAndConfigureExtension %@"
- "pluginBalloonInsetsForMessageFromMe:"
```
