## backboardd

> `/usr/libexec/backboardd`

```diff

-668.2.3.1.0
-  __TEXT.__text: 0xa41d4
-  __TEXT.__auth_stubs: 0x1c90
-  __TEXT.__objc_stubs: 0xeae0
-  __TEXT.__objc_methlist: 0x68c0
+668.3.7.0.0
+  __TEXT.__text: 0xa40fc
+  __TEXT.__auth_stubs: 0x1c60
+  __TEXT.__objc_stubs: 0xec80
+  __TEXT.__objc_methlist: 0x6930
   __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0x50e8
-  __TEXT.__objc_methname: 0x14cfc
-  __TEXT.__cstring: 0x7394
-  __TEXT.__objc_classname: 0x1d3a
-  __TEXT.__objc_methtype: 0x4022
-  __TEXT.__oslogstring: 0xa256
+  __TEXT.__gcc_except_tab: 0x5020
+  __TEXT.__objc_methname: 0x14ee2
+  __TEXT.__cstring: 0x7421
+  __TEXT.__objc_classname: 0x1c87
+  __TEXT.__objc_methtype: 0x4016
+  __TEXT.__oslogstring: 0xa25c
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2a40
-  __DATA_CONST.__auth_got: 0xe60
+  __TEXT.__unwind_info: 0x2a60
+  __DATA_CONST.__auth_got: 0xe48
   __DATA_CONST.__got: 0xa28
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4bb0
-  __DATA_CONST.__cfstring: 0x8160
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __DATA_CONST.__const: 0x4c50
+  __DATA_CONST.__cfstring: 0x8200
+  __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x14778
-  __DATA.__objc_selrefs: 0x4558
-  __DATA.__objc_ivar: 0xf6c
-  __DATA.__objc_data: 0x3ac0
-  __DATA.__data: 0x1bb0
+  __DATA.__objc_const: 0x14370
+  __DATA.__objc_selrefs: 0x4598
+  __DATA.__objc_ivar: 0xf60
+  __DATA.__objc_data: 0x3930
+  __DATA.__data: 0x1b50
   __DATA.__bss: 0x418
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3180
-  Symbols:   790
-  CStrings:  6323
+  Functions: 3199
+  Symbols:   785
+  CStrings:  6340
 
Symbols:
+ _BKSHIDEventGetRemoteTimestamp
+ _BKSHIDEventSetRemoteTimestamp
- _CFStringAppend
- _CFStringAppendFormat
- _CFStringAppendFormatAndArguments
- _CFStringCreateWithFormatAndArguments
- _IOHIDEventCreateVendorDefinedEvent
- _OBJC_CLASS_$_BKHIDEventClient
- _OBJC_METACLASS_$_BKHIDEventClient
CStrings:
+ "0x%!x(MISSING)"
+ "3\xf0A\xf0Q\xf1\xb1\xb1!A\x11"
+ "<%!@(MISSING): (pid: %!d(MISSING)) %!p(MISSING)>"
+ "@\"<BKHIDEventClientDelegate>\""
+ "@\"BSMachPortSendRight\""
+ "@\"BSPortDeathSentinel\""
+ "@28@0:8i16@20"
+ "@44@0:8i16@20@28@36"
+ "BKHIDEventClient"
+ "BKHIDEventClient died (pid): %!{(MISSING)public}@"
+ "BKHIDEventClient died (port): %!{(MISSING)public}@"
+ "BKHIDEventClient.m"
+ "ProxClearedAfterOccludedWake"
+ "T@\"<BKHIDEventClientDelegate>\",W,N"
+ "T@\"BSMachPortSendRight\",R,N,V_queue_sendRight"
+ "TB,N,GisTerminating,V_terminating"
+ "TQ,R,N,V_lastRemoteEventTimestamp"
+ "Ti,R,N,V_queue_pid"
+ "_BKHIDXXProximityDidUnoccludeAfterScreenWake"
+ "_lastRemoteEventTimestamp"
+ "_queue_delegate"
+ "_queue_invalidated"
+ "_queue_performDelegateCallout:"
+ "_queue_pid"
+ "_queue_pidWatcher"
+ "_queue_portSentinel"
+ "_queue_procName"
+ "_queue_sendRight"
+ "_terminating"
+ "activateWithHandler:"
+ "addTopLevelScaleEvent:fromSender:"
+ "addTopLevelScrollEvent:fromSender:"
+ "delegate"
+ "initWithPid:sendRight:queue:processName:"
+ "initWithSendRight:"
+ "isTerminating"
+ "lastRemoteEventTimestamp"
+ "port"
+ "proximityDidUnoccludeAfterScreenWake"
+ "proximityHostStateKeys"
+ "setTerminating:"
+ "terminating"
+ "use initWithPid:..."
+ "v16@?0@\"<BKHIDEventClientDelegate>\"8"
- "\n"
- "%!{(MISSING)public}@%!{(MISSING)public}@"
- "3\xf0A\xf0Q\xf1\xb1\xb1!B"
- "@\"<BKTranscriptTarget>\""
- "@\"NSMutableString\""
- "@\"_BKGraphStructureNode\""
- "BKEventGraphDescriptionAccumulator"
- "BKGraphDescription"
- "BKHIDVendorDefinedTouchSensitiveButtonEventProcessor"
- "BKHIDVendorDefinedTouchSensitiveButtonEventProcessor.m"
- "BKOSLogTranscriptTarget"
- "BKStringTranscriptTarget"
- "BKTranscriptTarget"
- "_BKGraphStructureNode"
- "_current"
- "_itemCountStack"
- "_itemRemainingStack"
- "_stackIndexesHighlighted"
- "_supernode"
- "_topLevel"
- "incoming %!{(MISSING)public}@"
- "initWithOSLog:"
- "outgoing %!{(MISSING)public}@ -> %!{(MISSING)public}@"
- "popSection:"
- "v40@0:8@\"NSString\"16@\"NSString\"24*32"
- "v40@0:8@16@24*32"
- "writePrefix:label:args:"
- "writeString:"

```
