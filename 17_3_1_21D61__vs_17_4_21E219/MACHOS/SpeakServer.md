## SpeakServer

> `/System/Library/AccessibilityBundles/SpeakServer.axuiservice/SpeakServer`

```diff

-3093.2.4.4.11
-  __TEXT.__text: 0x3688
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x1c0
+3093.23.0.0.0
+  __TEXT.__text: 0x3a88
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x3e3
-  __TEXT.__objc_classname: 0x27
-  __TEXT.__objc_methname: 0x1075
-  __TEXT.__oslogstring: 0x3b
-  __TEXT.__objc_methtype: 0x302
-  __TEXT.__unwind_info: 0xec
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x130
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__cstring: 0x3c3
+  __TEXT.__objc_classname: 0x28
+  __TEXT.__objc_methname: 0x12c3
+  __TEXT.__oslogstring: 0x153
+  __TEXT.__objc_methtype: 0x3d7
+  __TEXT.__unwind_info: 0x10c
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_classrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x7b0
-  __DATA.__objc_selrefs: 0x3b0
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0x838
+  __DATA.__objc_selrefs: 0x408
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 44
-  Symbols:   112
-  CStrings:  262
+  Functions: 52
+  Symbols:   111
+  CStrings:  287
 
Symbols:
+ __os_log_error_impl
+ _objc_retainBlock
- _AXSpeakTypingPayloadKeyCharacter
- _OBJC_CLASS_$_NSNotificationCenter
- _kAXSApplicationAccessibilityEnabledPreference
CStrings:
+ "\x01\x15\x16"
+ "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
+ "@52@0:8@16Q24@32i40^@44"
+ "Attempted to speak autocorrections from an app that did not own the first responder. Pid: %i, responder element: %@"
+ "Attempted to speak prediction from an app that did not own the first responder. Pid: %i"
+ "B20@0:8i16"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_isLastSpeechActionForResponderElement"
+ "_isAllowedToSpeakForPid:"
+ "_isLastSpeechActionForResponderElement"
+ "_observeSpeechAccessibilityPreferenceChanges"
+ "_speakAction:isForResponderElement:"
+ "_tryObservingNotifications"
+ "com.apple.accessibility.SpeakTypingServices"
+ "isLastSpeechActionForResponderElement"
+ "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
+ "letterFeedbackEnabled"
+ "phoneticFeedbackEnabled"
+ "pid"
+ "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
+ "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
+ "registerUpdateBlock:forRetrieveSelector:withListener:"
+ "remoteParent"
+ "setIsLastSpeechActionForResponderElement:"
+ "speakCorrectionsEnabled"
+ "typingFeedbackEnabled"
+ "v28@0:8@16B24"
+ "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@16Q24@32i40@?44"
+ "wordFeedbackEnabled"
- "\x01\x1b"
- "_handleApplicationAccessibilityEnabledDidChangeNotification:"
- "_speakAction:"
- "addObserver:selector:name:object:"
- "defaultCenter"

```
