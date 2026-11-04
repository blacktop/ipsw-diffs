## HomeKitEventRouter

> `/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter`

```diff

-1520.2.7.1.3
-  __TEXT.__text: 0x16950
-  __TEXT.__objc_methlist: 0x15dc
-  __TEXT.__const: 0x48
+1535.0.0.0.2
+  __TEXT.__text: 0x171b0
+  __TEXT.__objc_methlist: 0x1624
+  __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x49c
   __TEXT.__cstring: 0xb49
-  __TEXT.__oslogstring: 0x1d1a
-  __TEXT.__unwind_info: 0x728
+  __TEXT.__oslogstring: 0x1dfb
+  __TEXT.__unwind_info: 0x740
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xbe0
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x2568
+  __AUTH_CONST.__objc_const: 0x25a0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 481
-  Symbols:   989
-  CStrings:  252
+  Functions: 488
+  Symbols:   997
+  CStrings:  255
 
Symbols:
+ -[HMEDelegatingEventRouter refreshSubRouterRegistrations]
+ -[HMEMessageDatagramClient _updateWantsConnection]
+ -[HMEMessageDatagramClient dormantFetchTimerInterval]
+ -[HMEMessageDatagramClient setWantsConnection:]
+ -[HMEMessageDatagramClient wantsConnection]
+ -[HMERouterClient registeredTopicFiltersForConsumer:]
+ GCC_except_table100
+ GCC_except_table262
+ GCC_except_table267
+ GCC_except_table271
+ GCC_except_table280
+ GCC_except_table282
+ GCC_except_table284
+ GCC_except_table286
+ GCC_except_table400
+ GCC_except_table402
+ GCC_except_table406
+ GCC_except_table414
+ GCC_except_table431
+ GCC_except_table70
+ GCC_except_table86
+ GCC_except_table94
+ _OBJC_IVAR_$_HMEMessageDatagramClient._dormantFetchTimerInterval
+ _OBJC_IVAR_$_HMEMessageDatagramClient._wantsConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMESynchronousSubscriptionProviding
+ ___57-[HMEDelegatingEventRouter refreshSubRouterRegistrations]_block_invoke
- -[HMEMessageDatagramClient dormatFetchTimerInterval]
- GCC_except_table256
- GCC_except_table260
- GCC_except_table264
- GCC_except_table270
- GCC_except_table273
- GCC_except_table275
- GCC_except_table279
- GCC_except_table393
- GCC_except_table395
- GCC_except_table399
- GCC_except_table407
- GCC_except_table424
- GCC_except_table69
- GCC_except_table85
- GCC_except_table89
- GCC_except_table97
- _OBJC_IVAR_$_HMEMessageDatagramClient._dormatFetchTimerInterval
CStrings:
+ "Delegating registrations to subRouter: %{public}@, topicFilterAdditions: %lu, topicFilterRemovals: %lu"
+ "Failed to change registrations on subRouter: %{public}@, error: %{public}@"
+ "changed registrations on subRouter: %{public}@"
```
