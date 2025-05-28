## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-971.100.1.2.3
-  __TEXT.__text: 0xbb4b4
+971.200.71.2.2
+  __TEXT.__text: 0xbc848
   __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0xf9e0
+  __TEXT.__objc_stubs: 0xfac0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x9a28
-  __TEXT.__objc_methname: 0x18fed
-  __TEXT.__objc_classname: 0xf4d
-  __TEXT.__objc_methtype: 0x41e1
-  __TEXT.__cstring: 0x8c02
+  __TEXT.__objc_methlist: 0x9aa8
+  __TEXT.__objc_methname: 0x19107
+  __TEXT.__objc_classname: 0xf4e
+  __TEXT.__objc_methtype: 0x4201
+  __TEXT.__cstring: 0x8d72
   __TEXT.__const: 0x69a
-  __TEXT.__oslogstring: 0x103e5
+  __TEXT.__oslogstring: 0x10472
   __TEXT.__gcc_except_tab: 0x1bb0
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__constg_swiftt: 0x230
+  __TEXT.__constg_swiftt: 0x238
   __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_reflstr: 0x199
   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x2fc4
+  __TEXT.__unwind_info: 0x2ffc
   __TEXT.__eh_frame: 0x118
   __DATA_CONST.__auth_got: 0xfa8
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x3880
-  __DATA_CONST.__cfstring: 0x7ca0
+  __DATA_CONST.__cfstring: 0x7ce0
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x208

   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1cb68
-  __DATA.__objc_selrefs: 0x50c8
+  __DATA.__objc_const: 0x1cca8
+  __DATA.__objc_selrefs: 0x50f0
   __DATA.__objc_protorefs: 0x60
   __DATA.__objc_classrefs: 0x600
   __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0xc90
-  __DATA.__objc_data: 0x2d30
+  __DATA.__objc_ivar: 0xc9c
+  __DATA.__objc_data: 0x2d38
   __DATA.__data: 0x1828
   __DATA.__bss: 0x3c8
   __DATA.__common: 0xf8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4582
-  Symbols:   750
-  CStrings:  7016
+  Functions: 4596
+  Symbols:   751
+  CStrings:  7038
 
Symbols:
+ _APSPrintInternalMessageAppContentsKey
CStrings:
+ "\t1\x12"
+ "\x11\x1f\x01"
+ "%@ no change detected between the new and old server filter - cancelling any pending updates"
+ "%@ not downgrading %@, topic is push wake enabled"
+ "%@ noted connections too many times, likely in a loop -- stopping {connectedNotesSentLimiter: %@}"
+ ", alignedMonotonicTimeInNanoSeconds="
+ ", changeInSeconds="
+ ", currentMonotonicTimeInNanoSeconds="
+ ", mostRecentServerTimeInNanoSeconds="
+ "<%p guid: %@; stateByInterfaceIdentifier: %@; filterModeByInterfaceIdentifier: %@; enabledTopics: %@, ignoredTopics: %@, opportunisticTopics: %@, nonWakingTopics: %@>"
+ "<Not currently connected, using current time "
+ "<domain=%@, connectedInterfaces=%lu, info=%@, serverTime=%@>"
+ "<serverTimeInNanoSeconds="
+ "@\"APSFilterVersionStateMachine\""
+ "T@\"APSFilterVersionStateMachine\",&,N,V_filterVersionStateMachine"
+ "T@\"APSRateLimiter\",&,N,V_connectedNotesSentLimiter"
+ "T@\"APSTopicGroup\",&,N,V_serverGroup"
+ "TB,N,V_informingOfWrite"
+ "_connectedNotesSentLimiter"
+ "_informingOfWrite"
+ "_prepareToParseOutgoingDataOnInterface:"
+ "_serverGroup"
+ "com.tinyspeck.chatlyio"
+ "connectedNotesSentLimiter"
+ "courierConnection:aboutToWriteDataOnConnectedInterface:"
+ "iOS Dump State\n%@\nMac OS Dump State\n%@\n"
+ "informingOfWrite"
+ "initWithDictionary:copyItems:"
+ "serverGroup"
+ "setConnectedNotesSentLimiter:"
+ "setInformingOfWrite:"
+ "setServerGroup:"
- "\t1\x11"
- "\x11\x1e"
- "%@ noted connections too many times, likely in a loop -- stopping {countOfConnectedNotesSent: %lld}"
- "<domain=%@, connectedInterfaces=%lu, info=%@>"
- "<guid: %@; stateByInterfaceIdentifier: %@; filterModeByInterfaceIdentifier: %@; enabledTopics: %@, ignoredTopics: %@, opportunisticTopics: %@, nonWakingTopics: %@>"
- "Tq,N,V_countOfConnectedNotesSent"
- "_countOfConnectedNotesSent"
- "_informStateListenerOfOutgoingDataOnInterface:"
- "countOfConnectedNotesSent"
- "noteOutgoingDataOnProtocolConnection:"
- "setCountOfConnectedNotesSent:"

```
