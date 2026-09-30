## MSMessageExtensionBalloonPlugin

> `/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin`

### Sections with Same Size but Changed Content

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

-1491.100.1.2.25
-  __TEXT.__text: 0x29d5c
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_stubs: 0x6b60
-  __TEXT.__objc_methlist: 0x2eec
-  __TEXT.__const: 0x494
-  __TEXT.__objc_methname: 0x8b3d
+1491.200.63.2.1
+  __TEXT.__text: 0x2a640
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_stubs: 0x6c80
+  __TEXT.__objc_methlist: 0x2f5c
+  __TEXT.__const: 0x4a4
+  __TEXT.__objc_methname: 0x8ccd
   __TEXT.__objc_classname: 0x6af
   __TEXT.__cstring: 0x14ae
-  __TEXT.__objc_methtype: 0x1ede
-  __TEXT.__gcc_except_tab: 0x794
-  __TEXT.__oslogstring: 0x2cf4
+  __TEXT.__objc_methtype: 0x1f2e
+  __TEXT.__gcc_except_tab: 0x7ec
+  __TEXT.__oslogstring: 0x2e64
   __TEXT.__swift5_typeref: 0x2c6
   __TEXT.__swift5_capture: 0x128
   __TEXT.__constg_swiftt: 0x2e4

   __TEXT.__swift_as_cont: 0x34
   __TEXT.__swift5_assocty: 0x28
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0xea8
+  __TEXT.__unwind_info: 0xed8
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__const: 0x1120
+  __DATA_CONST.__const: 0x1170
   __DATA_CONST.__cfstring: 0x9e0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x778
-  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__got: 0x678
   __DATA_CONST.__auth_ptr: 0xf8
-  __DATA.__objc_const: 0x3718
-  __DATA.__objc_selrefs: 0x23a8
-  __DATA.__objc_ivar: 0x1e4
+  __DATA.__objc_const: 0x3750
+  __DATA.__objc_selrefs: 0x2408
+  __DATA.__objc_ivar: 0x1e8
   __DATA.__objc_data: 0x998
   __DATA.__data: 0xc88
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1074
-  Symbols:   483
-  CStrings:  1934
+  Functions: 1082
+  Symbols:   486
+  CStrings:  1953
 
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
