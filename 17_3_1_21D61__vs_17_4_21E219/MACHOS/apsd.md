## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-971.400.31.0.0
-  __TEXT.__text: 0xbcf70
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0xfb60
+971.500.141.0.0
+  __TEXT.__text: 0xbd284
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__objc_stubs: 0xfae0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x9b00
-  __TEXT.__objc_methname: 0x1924d
-  __TEXT.__objc_classname: 0xf4e
-  __TEXT.__objc_methtype: 0x4201
-  __TEXT.__cstring: 0x8d82
-  __TEXT.__const: 0x69a
-  __TEXT.__oslogstring: 0x105d4
-  __TEXT.__gcc_except_tab: 0x1bc4
-  __TEXT.__dlopen_cstrs: 0xaa
+  __TEXT.__objc_methlist: 0x9ae8
+  __TEXT.__objc_methname: 0x191f3
+  __TEXT.__objc_classname: 0xf4d
+  __TEXT.__objc_methtype: 0x4212
+  __TEXT.__cstring: 0x8e02
+  __TEXT.__const: 0x6aa
+  __TEXT.__oslogstring: 0x10616
+  __TEXT.__gcc_except_tab: 0x1bf0
+  __TEXT.__dlopen_cstrs: 0x100
   __TEXT.__constg_swiftt: 0x238
   __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_reflstr: 0x199
   __TEXT.__swift5_fieldmd: 0x178
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3014
+  __TEXT.__unwind_info: 0x3010
   __TEXT.__eh_frame: 0x118
-  __DATA_CONST.__auth_got: 0xfa8
-  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__auth_got: 0xfb8
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x3858
-  __DATA_CONST.__cfstring: 0x7d00
+  __DATA_CONST.__const: 0x38d8
+  __DATA_CONST.__cfstring: 0x7d20
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x288
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x600
+  __DATA_CONST.__objc_superrefs: 0x378
+  __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1ccd8
-  __DATA.__objc_selrefs: 0x5128
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x600
-  __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0xca0
+  __DATA.__objc_const: 0x1cd48
+  __DATA.__objc_selrefs: 0x5110
+  __DATA.__objc_ivar: 0xca4
   __DATA.__objc_data: 0x2d38
-  __DATA.__data: 0x1828
-  __DATA.__bss: 0x3c8
+  __DATA.__data: 0x17f8
+  __DATA.__bss: 0x3a8
   __DATA.__common: 0xf8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4603
-  Symbols:   751
-  CStrings:  7053
+  Functions: 4604
+  Symbols:   752
+  CStrings:  7057
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ _objc_getClass
- _APSPrintInternalMessageAppContentsKey
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "\x1a\x14\x12\x11AB\x12\x17!\x11'\x12\x12."
+ "%@: Client device may think its disconnected, sending a note that its connected.  Client %@"
+ "%@: Got presence offline for client %@.  Invalidating and removing any pending proxy presences."
+ "%@: Large Message Size did not change, not sending to client device."
+ "%@: Message Size did not change, not sending to client device."
+ "%@: Received a presence response for a client that's no longer connected.  Dropping..."
+ "%@: We may be an orphaned client, kickstarting proxy connection."
+ "<%p guid: %@; isActive: %@; invalid: %@ stateByInterfaceIdentifier: %@; filterModeByInterfaceIdentifier: %@; enabledTopics: %@, ignoredTopics: %@, opportunisticTopics: %@, nonWakingTopics: %@>"
+ "APSUserCourier.m"
+ "Action"
+ "Class getSafetyAlertsClass(void)_block_invoke"
+ "DidWake"
+ "SafetyAlerts"
+ "T@\"NSString\",?,R,C"
+ "TQ,N,V_environmentType"
+ "Unable to find class %s"
+ "_environmentType"
+ "_handleKeepAliveResponseMessage:onInterface:didWake:"
+ "_reportAPSConnectivity"
+ "environmentType"
+ "isHardwareSupported"
+ "kickstartProxyConnection"
+ "onAPSDConnectionChangeIsOverWiFi:isOverCell:"
+ "setEnvironmentType:"
+ "sharedInterface"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts"
+ "v36@0:8@16q24B32"
+ "void *SafetyAlertsLibrary(void)"
- "\x1a\x14\x12\x11A\x122\x12\x17!\x11'\x12\x12."
- "%@-recreatecourierstate-%@"
- "%@: Filter changed"
- "%@: Finished waiting for user before recreating the courier state"
- "%@: Not starting recreate courier state timer if machine is going to sleep with no connection."
- "%@: Recreating courier state for user %@"
- "%@: Waiting until filter is sent to send queued outgoing message"
- "%@: Will wait %@ for user %@ before recreating the courier state"
- "<%p guid: %@; stateByInterfaceIdentifier: %@; filterModeByInterfaceIdentifier: %@; enabledTopics: %@, ignoredTopics: %@, opportunisticTopics: %@, nonWakingTopics: %@>"
- "_attributesForFilter does not recognize filter name %d"
- "_attributesForFilter:"
- "_clearRecreateCourierStateTimer"
- "_fireRecreateCourierStateTimer"
- "_handleKeepAliveResponseMessage:onInterface:"
- "_hasPendingRecreateCourierStateTimer"
- "_initWithFilter:"
- "_recreateCourierState"
- "_recreateCourierStatePowerAssertion"
- "_recreateCourierStateTimer"
- "_recreateCourierStateTimerFired:"
- "_startRecreateCourierStateTimerBePatient:"
- "a moment"
- "fireDate"
- "initWithFilter:"
- "patiently"

```
