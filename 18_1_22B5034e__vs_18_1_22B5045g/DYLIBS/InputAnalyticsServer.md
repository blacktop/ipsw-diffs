## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.104.0.0.0
-  __TEXT.__text: 0x13510
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0xf64
-  __TEXT.__const: 0x142
-  __TEXT.__oslogstring: 0x1f50
-  __TEXT.__cstring: 0x10f2
+64.106.0.0.0
+  __TEXT.__text: 0x14b74
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x109c
+  __TEXT.__const: 0x152
+  __TEXT.__oslogstring: 0x20a0
+  __TEXT.__cstring: 0x11b2
   __TEXT.__gcc_except_tab: 0x358
   __TEXT.__swift5_typeref: 0x84
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x570
+  __TEXT.__unwind_info: 0x5a8
   __TEXT.__eh_frame: 0x2f8
-  __TEXT.__objc_classname: 0x264
-  __TEXT.__objc_methname: 0x264b
+  __TEXT.__objc_classname: 0x27b
+  __TEXT.__objc_methname: 0x281f
   __TEXT.__objc_methtype: 0x4e5
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x440
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__objc_stubs: 0x1e00
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b8
+  __DATA_CONST.__objc_selrefs: 0x948
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x3d8
-  __AUTH_CONST.__cfstring: 0xce0
-  __AUTH_CONST.__objc_const: 0x23f8
+  __AUTH_CONST.__const: 0x3f8
+  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__objc_const: 0x2640
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x200
+  __AUTH.__objc_data: 0x250
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x168
+  __DATA.__objc_ivar: 0x188
   __DATA.__data: 0x2b0
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 528
-  Symbols:   184
-  CStrings:  812
+  Functions: 568
+  Symbols:   195
+  CStrings:  855
 
Symbols:
+ _OBJC_CLASS_$_IAServerStats
+ _OBJC_CLASS_$_IATextInputActionsSessionKBMenuAppearAction
+ _OBJC_CLASS_$_IATextInputActionsSessionAction
+ _IAPayloadKeySmartRepliesIsCached
+ _objc_retain_x27
+ _objc_retain_x28
+ _OBJC_CLASS_$_IATextInputActionsSessionKBMenuDismissAction
+ _objc_retain_x25
+ _OBJC_CLASS_$_IATextInputActionsSessionGlomojiTapAction
+ _OBJC_CLASS_$_IATextInputActionsSessionKBMenuInteractionAction
+ _OBJC_CLASS_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction
CStrings:
+ "_mergedActionsCount"
+ "com.apple.inputAnalytics.server.IASGlomojiAnalyzer"
+ "com.apple.inputAnalytics.glomojiUsage"
+ "mergeActionIfPossible:"
+ "reportDailyStats"
+ "sequence"
+ "IASGlomojiAnalyzer"
+ "originalInputMode"
+ "sendDismissEvent:"
+ "updatedInputMode"
+ "[IASGlomojiAnalyzer] keyboardDockItemButtonPressAction"
+ "newInputMode"
+ "[IASGlomojiAnalyzer] ignoring unmerged actions of the same class"
+ "removeObjectsInRange:"
+ "objectAtIndex:"
+ "mergedActionsCount"
+ "KBMenuDismissSource"
+ "[IASGlomojiAnalyzer] sequence: %!@(MISSING)"
+ "T@\"NSString\",&,N,V_inputMode"
+ "Tq,N,V_mergedActionsCount"
+ "sendInteractionEvent:"
+ "T@\"NSMutableOrderedSet\",&,N,V_sequence"
+ "[IASGlomojiAnalyzer] error: dismiss without menu appearing"
+ "_inputMode"
+ "Initialized with exceptions: %!{(MISSING)private}@"
+ "[IASGlomojiAnalyzer] class: %!@(MISSING)"
+ "[IASGlomojiAnalyzer] error: interaction without menu appearing"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "actionType"
+ "setMergedActionsCount:"
+ "_sequence"
+ "firstObject"
+ "identifySequence:"
+ "nextEvent"
+ "isCached"
+ "GlomojiAnalytics"
+ "\x02\x12\x11"
+ "numTapCounts"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "insertObject:atIndex:"
+ "setSequence:"
+ "KBMenuSelectedAction"
+ "triggerType"
+ "KBMenuInteractionSource"
- "Failed to cast raw action to TextInputActionsSessionAction and is now nil"
- "Initialized"

```
