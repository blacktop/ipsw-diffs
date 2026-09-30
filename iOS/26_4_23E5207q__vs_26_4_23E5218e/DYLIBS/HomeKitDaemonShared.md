## HomeKitDaemonShared

> `/System/Library/PrivateFrameworks/HomeKitDaemonShared.framework/HomeKitDaemonShared`

```diff

-1418.5.4.0.0
-  __TEXT.__text: 0x993c
+1418.5.9.0.1
+  __TEXT.__text: 0x9bfc
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0xa44
+  __TEXT.__objc_methlist: 0xac4
   __TEXT.__const: 0x2a8
   __TEXT.__constg_swiftt: 0x84
   __TEXT.__swift5_typeref: 0x71

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0x33
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__cstring: 0x3d3
+  __TEXT.__cstring: 0x488
   __TEXT.__oslogstring: 0xd4c
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x290
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x19f
-  __TEXT.__objc_methname: 0x1c45
-  __TEXT.__objc_methtype: 0x610
-  __TEXT.__objc_stubs: 0x14a0
+  __TEXT.__objc_classname: 0x1cb
+  __TEXT.__objc_methname: 0x1d67
+  __TEXT.__objc_methtype: 0x639
+  __TEXT.__objc_stubs: 0x1500
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x318
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x6d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x130
-  __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x13e8
+  __AUTH_CONST.__cfstring: 0x4e0
+  __AUTH_CONST.__objc_const: 0x15f0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x1f0
+  __AUTH.__objc_data: 0x240
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x518
   __DATA.__bss: 0x490
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 62C8E632-3D29-3A71-B820-7ECC8A411252
-  Functions: 226
-  Symbols:   836
-  CStrings:  525
+  UUID: 03604547-972F-3F8B-AFE1-4B0155D6DCFE
+  Functions: 236
+  Symbols:   871
+  CStrings:  551
 
Symbols:
+ -[HMDStatusChannelSubscriptionDetailsLogEvent .cxx_destruct]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent channelPrefix]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent coreAnalyticsEventDictionary]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent coreAnalyticsEventName]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent coreAnalyticsEventOptions]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent initWithChannelPrefix:isRetry:timeTakenToSubscribe:]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent isRetry]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent setDurationWaitedForFirstUpdate:receivedUpdateFromChannel:]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent timeTakenToGetFirstUpdate]
+ -[HMDStatusChannelSubscriptionDetailsLogEvent timeTakenToSubscribe]
+ _OBJC_CLASS_$_HMDStatusChannelSubscriptionDetailsLogEvent
+ _OBJC_IVAR_$_HMDStatusChannelSubscriptionDetailsLogEvent._channelPrefix
+ _OBJC_IVAR_$_HMDStatusChannelSubscriptionDetailsLogEvent._isRetry
+ _OBJC_IVAR_$_HMDStatusChannelSubscriptionDetailsLogEvent._timeTakenToGetFirstUpdate
+ _OBJC_IVAR_$_HMDStatusChannelSubscriptionDetailsLogEvent._timeTakenToSubscribe
+ _OBJC_METACLASS_$_HMDStatusChannelSubscriptionDetailsLogEvent
+ __OBJC_$_INSTANCE_METHODS_HMDStatusChannelSubscriptionDetailsLogEvent
+ __OBJC_$_INSTANCE_VARIABLES_HMDStatusChannelSubscriptionDetailsLogEvent
+ __OBJC_$_PROP_LIST_HMDStatusChannelSubscriptionDetailsLogEvent
+ __OBJC_CLASS_PROTOCOLS_$_HMDStatusChannelSubscriptionDetailsLogEvent
+ __OBJC_CLASS_RO_$_HMDStatusChannelSubscriptionDetailsLogEvent
+ __OBJC_METACLASS_RO_$_HMDStatusChannelSubscriptionDetailsLogEvent
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$timeTakenToGetFirstUpdate
+ _objc_msgSend$timeTakenToSubscribe
CStrings:
+ "@36@0:8@16B24d28"
+ "HMDStatusChannelSubscriptionDetailsLogEvent"
+ "Td,R,N,V_timeTakenToGetFirstUpdate"
+ "Td,R,N,V_timeTakenToSubscribe"
+ "_timeTakenToGetFirstUpdate"
+ "_timeTakenToSubscribe"
+ "com.apple.HomeKit.daemon.statuskit.channel.subscriptionDetails"
+ "d"
+ "d16@0:8"
+ "initWithChannelPrefix:isRetry:timeTakenToSubscribe:"
+ "numberWithDouble:"
+ "receivedUpdateFromChannel"
+ "setDurationWaitedForFirstUpdate:receivedUpdateFromChannel:"
+ "subscriptionRetryBool"
+ "subscriptionRetryCount"
+ "timeTakenToGetFirstUpdate"
+ "timeTakenToSubscribe"
+ "v28@0:8d16B24"

```
