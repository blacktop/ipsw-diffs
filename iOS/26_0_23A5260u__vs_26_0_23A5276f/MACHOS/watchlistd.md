## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-902.0.0.0.0
-  __TEXT.__text: 0x28354
+903.0.0.0.0
+  __TEXT.__text: 0x28658
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x51e0
-  __TEXT.__objc_methlist: 0x265c
-  __TEXT.__cstring: 0x48bf
-  __TEXT.__oslogstring: 0x2602
+  __TEXT.__objc_stubs: 0x52e0
+  __TEXT.__objc_methlist: 0x2664
+  __TEXT.__cstring: 0x48c7
+  __TEXT.__oslogstring: 0x26c9
   __TEXT.__objc_classname: 0x497
   __TEXT.__objc_methtype: 0xf79
-  __TEXT.__objc_methname: 0x5f2a
+  __TEXT.__objc_methname: 0x5fb5
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0xf00
   __TEXT.__unwind_info: 0xb58
   __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__got: 0x540
   __DATA_CONST.__const: 0x1320
   __DATA_CONST.__cfstring: 0x3d00
   __DATA_CONST.__objc_classlist: 0x120

   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x4df0
-  __DATA.__objc_selrefs: 0x1be8
+  __DATA.__objc_selrefs: 0x1c28
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D315DB24-334F-3902-8C67-7097B03BD3D8
-  Functions: 896
-  Symbols:   2684
-  CStrings:  2479
+  UUID: 08D8EE05-94A5-3D0C-A8F6-CC8FB5B209E0
+  Functions: 897
+  Symbols:   2694
+  CStrings:  2490
 
Symbols:
+ -[WLDPushNotificationController pushPayload:withBadgeRequest:]
+ _AMSPushActionTypeBadging
+ __79-[WLDPushNotificationController connection:didReceiveMessageForTopic:userInfo:]_block_invoke.49
+ __79-[WLDPushNotificationController connection:didReceiveMessageForTopic:userInfo:]_block_invoke.54
+ _objc_msgSend$badgeIdentifier
+ _objc_msgSend$enabled
+ _objc_msgSend$enqueueEvent:
+ _objc_msgSend$initWithUnderlyingDictionary:
+ _objc_msgSend$metrics
+ _objc_msgSend$removeBadgeRequest:
+ _objc_msgSend$setEngagementPushTopic:
+ _objc_msgSend$storeBadgeRequest:
- __79-[WLDPushNotificationController connection:didReceiveMessageForTopic:userInfo:]_block_invoke.43
- __79-[WLDPushNotificationController connection:didReceiveMessageForTopic:userInfo:]_block_invoke.48
Functions:
~ ___37-[WLDPushNotificationController init]_block_invoke : 988 -> 1132
+ -[WLDPushNotificationController pushPayload:withBadgeRequest:]
CStrings:
+ "WLDPushNotificationController - WLDPushNotificationController: found empty badge display metrics id %@"
+ "WLDPushNotificationController - WLDPushNotificationController: pushed display metrics for id %@"
+ "badgeIdentifier"
+ "enabled"
+ "enqueueEvent:"
+ "initWithUnderlyingDictionary:"
+ "juniper"
+ "removeBadgeRequest:"
+ "setEngagementPushTopic:"
+ "storeBadgeRequest:"

```
