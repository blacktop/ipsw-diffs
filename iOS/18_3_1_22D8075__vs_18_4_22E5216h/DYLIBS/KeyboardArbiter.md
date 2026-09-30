## KeyboardArbiter

> `/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`

```diff

-8306.0.0.0.0
-  __TEXT.__text: 0x17058
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0xd18
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0xdbd
-  __TEXT.__oslogstring: 0x128a
-  __TEXT.__gcc_except_tab: 0x888
+8440.1.102.0.0
+  __TEXT.__text: 0x18ad0
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x11fc
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0xf01
+  __TEXT.__oslogstring: 0x19a2
+  __TEXT.__gcc_except_tab: 0x8f8
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x5a0
-  __TEXT.__objc_classname: 0x2f1
-  __TEXT.__objc_methname: 0x3504
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__objc_classname: 0x2f2
+  __TEXT.__objc_methname: 0x364f
   __TEXT.__objc_methtype: 0xbec
-  __TEXT.__objc_stubs: 0x2e20
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x830
+  __TEXT.__objc_stubs: 0x2f60
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd28
+  __DATA_CONST.__objc_selrefs: 0xe08
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x2568
+  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__objc_const: 0x1d48
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x420
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_ivar: 0x18
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 360
-  Symbols:   536
-  CStrings:  952
+  Functions: 374
+  Symbols:   557
+  CStrings:  1014
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_NSMutableString
+ __UIArbiterClientHandleLog
+ __UIArbiterEventsLog
+ __UIKeyboardTransitionStageToString
+ __UIKeyboardWindowStateToString
+ __UISceneIdentityToLogString
+ __UITextInputSourceToString
+ _objc_retain_x26
+ _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "\x0311#\x11\x11\x13\x11!!"
+ "%s%lu"
+ "%{public}@(%d) lostConnection (invalidation)"
+ "("
+ "(self)"
+ ")"
+ ","
+ "-[_UIKeyboardArbiterClientHandle userFirstTapOnKeyboard]"
+ "<%@ focus:%@ run:%s hosting:%@ level:%.0f active:%s wantedState:%@ #suppr:%d iavHeight:%.0f onScreen:%s>"
+ "================ Last detected blank keyboard at %@ ===================="
+ "Events"
+ "Handle"
+ "N"
+ "RX %@(%d) notifyHostedPIDsOfSuppression:%s active:%s"
+ "RX %{public}@(%d) applicationShouldFocusWithBundle:%{public}@"
+ "RX %{public}@(%d) focusApplicationWithPID:%d stealKeyboard:%s\n    context:%{public}@"
+ "RX %{public}@(%d) notifyIAVHeight:%.1f (was %.1f)"
+ "RX %{public}@(%d) retrieveDebugInfo"
+ "RX %{public}@(%d) retrieveMoreDebugInfo"
+ "RX %{public}@(%d) setClientFocusContext\n    focusContext:%{public}@"
+ "RX %{public}@(%d) setDeactivating:%s"
+ "RX %{public}@(%d) setKeyboardTotalDisable:%s fence:%s"
+ "RX %{public}@(%d) setWantsFencing:%s"
+ "RX %{public}@(%d) setWindowContextID:%u windowState:%{public}@ level:%.1f\n    focusContext:%{public}@"
+ "RX %{public}@(%d) setWindowHostingPID:%d active:%s"
+ "RX %{public}@(%d) signalAutofillUIBringup"
+ "RX %{public}@(%d) signalEventSourceChanged:%{public}@"
+ "RX %{public}@(%d) signalKeyboardChangeComplete"
+ "RX %{public}@(%d) signalKeyboardChanged\n    keyboardChanges:%{public}@"
+ "RX %{public}@(%d) startArbitration\n    expectedState:%{public}@\n    focusContext:%{private}@\n    hostingPIDs:%@ usingFence:%s withSuppression:%d"
+ "RX %{public}@(%d) transition:%{public}@ eventStage:%{public}@"
+ "T@\"NSArray\",&,N,V_blankKeyboardLogs"
+ "Td,N,V_blankKeyboardRecordTime"
+ "Trying to restore previouslyActiveHandle: %{public}@"
+ "Y"
+ "[%@] do not steal keyboard from Spotlight for pid %ld"
+ "_blankKeyboardLogs"
+ "_blankKeyboardRecordTime"
+ "active input destination is now %{public}@; information: %{public}@"
+ "allObjects"
+ "applySceneFocusChange:%{public}@ forRequest:%{public}@"
+ "blankKeyboardLogs"
+ "blankKeyboardRecordTime"
+ "com.apple.KeyboardArbiter"
+ "descriptionForLog"
+ "enumerateObjectsUsingBlock:"
+ "initWithString:"
+ "integerValue"
+ "request:%{public}@ sceneFocusChange:%{public}@"
+ "sceneFocusDeliberation(pid:%d) = %{public}@"
+ "set activeInputDestination:%{public}@"
+ "set activeInputDestination:(null) (unexpectedDeallocForHandler)"
+ "set currentFocus PID:%d sceneIdentity:%{public}@"
+ "set focusRequestedHandle:%{public}@"
+ "set focusRequestedHandle:(null) (connectionInvalidated)"
+ "set focusRequestedHandle:(null) (processSuspended)"
+ "set focusRequestedHandle:(null) (unexpectedDeallocForHandler)"
+ "setBlankKeyboardLogs:"
+ "setBlankKeyboardRecordTime:"
+ "steal keyboard for %{public}@"
+ "subarrayWithRange:"
+ "updateSuppression:%s pid:%d active:%s"
+ "userFirstTapOnKeyboard"
+ "v32@?0@\"NSNumber\"8Q16^B24"
- "\x0311#\x11\x11\x13\x11!"
- "active input destination is now %{private}@; information: %{private}@"

```
