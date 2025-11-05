## UIRecording

> `/System/Library/PrivateFrameworks/UIRecording.framework/Versions/A/UIRecording`

```diff

 33.1.0.0.0
-  __TEXT.__text: 0xbffc
+  __TEXT.__text: 0xbfd8
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0xd30
+  __TEXT.__objc_methlist: 0xd7c
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x1bc4
   __TEXT.__gcc_except_tab: 0x3a0
-  __TEXT.__unwind_info: 0x468
+  __TEXT.__unwind_info: 0x458
   __TEXT.__objc_classname: 0x18c
   __TEXT.__objc_methname: 0x227a
   __TEXT.__objc_methtype: 0xa27

   __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0x2940
-  __AUTH_CONST.__objc_const: 0x1718
+  __AUTH_CONST.__objc_const: 0x16a0
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0xec
   __DATA.__data: 0x128

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C41E9684-8227-3C23-A642-80C6BF5280DD
-  Functions: 289
-  Symbols:   1027
+  UUID: 352105A6-D7B0-3FF9-9DD7-9BE4156C9C05
+  Functions: 287
+  Symbols:   1028
   CStrings:  1282
 
Symbols:
+ _UIRecordingFrameworkBundle.cold.1
Functions:
~ -[UIRAccessibilityElement actionNames] : 68 -> 72
~ -[UIRAccessibilityElement attributeNames] : 68 -> 72
~ -[UIRAccessibilityElement descriptionForAction:] : 72 -> 76
~ -[UIRAccessibilityElement valueForAttribute:] : 72 -> 76
~ -[UIRAccessibilityElement valuesForAttribute:] : 80 -> 84
~ -[UIRRecord _glideCursorToLocation:withEvent:withEventSource:] : 220 -> 224
~ -[UIRRecord _raiseMouseButtons:withEventSource:] : 268 -> 292
~ -[UIRRecord _indexOfFirstElementInStack:afterIndex:withAnyAccessibilityRole:] : 324 -> 320
~ -[UIRRecord _playbackRecording] : 1708 -> 1704
~ -[UIRRecord _runCheckForCancelCommandThread] : 432 -> 436
~ -[UIRRemoteRecorder stopRecording] : 136 -> 132
~ -[UIRRemoteRecorder didStopRecording:] : 260 -> 264
~ -[UIREvent initWithCoder:] : 512 -> 508
~ _print_event : 1880 -> 1948
- sub_254b944d8
~ -[UIRAccessibilityElementRecord objectForAXValue:] : 628 -> 632
- sub_254b95488
~ -[UIRAccessibilityElementRecord initWithCoder:] : 512 -> 508
~ -[UIRTDrawFocusView drawRect:] : 1232 -> 1236
~ -[UIRTDrawFocus selectNextAction] : 492 -> 488
~ -[UIRTDrawFocus _createActionsWindowForUIElement:] : 636 -> 632
~ -[UIRLocalRecorder setCurrentUIElement:] : 140 -> 144
~ -[UIRLocalRecorder _recordEventsOnPrivateThread] : 888 -> 892
~ -[UIRLocalRecorder performTimerBasedUIElementUpdate] : 96 -> 100
~ -[UIRLocalRecorder _eventTapProxyCallback:withEventType:withEvent:] : 828 -> 860
- sub_254b98cf0
~ __UIRecordingFrameworkBundle : 272 -> 220

```
