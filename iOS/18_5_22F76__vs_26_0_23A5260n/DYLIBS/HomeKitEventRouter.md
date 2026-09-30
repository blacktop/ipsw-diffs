## HomeKitEventRouter

> `/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter`

```diff

-1278.6.31.1.1
-  __TEXT.__text: 0x17114
+1323.0.6.0.1
+  __TEXT.__text: 0x173d4
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x157c
+  __TEXT.__objc_methlist: 0x1594
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x594
-  __TEXT.__cstring: 0xb2f
-  __TEXT.__oslogstring: 0x1d6b
+  __TEXT.__cstring: 0xb22
+  __TEXT.__oslogstring: 0x1d3a
   __TEXT.__unwind_info: 0x618
   __TEXT.__objc_classname: 0x2d1
-  __TEXT.__objc_methname: 0x3474
+  __TEXT.__objc_methname: 0x34db
   __TEXT.__objc_methtype: 0xa99
-  __TEXT.__objc_stubs: 0x23e0
-  __DATA_CONST.__got: 0x118
+  __TEXT.__objc_stubs: 0x24c0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb70
+  __DATA_CONST.__objc_selrefs: 0xba8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x24f0
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0x2520
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E6275017-A8E8-3FEE-9A1F-1AE7DEC673D6
-  Functions: 477
-  Symbols:   1751
-  CStrings:  973
+  UUID: E95DB60A-270C-37BD-84AB-64C11FF9CF30
+  Functions: 480
+  Symbols:   1761
+  CStrings:  984
 
Symbols:
+ -[HMEMessageDatagramClient _enableRetryTimer]
+ -[HMEMessageDatagramClient _performKeepAliveRequest]
+ -[HMEMessageDatagramClient _removeRetryTimerAndResetInterval]
+ -[HMEMessageDatagramClient _removeRetryTimer]
+ -[HMEMessageDatagramClient hasPendingKeepAliveRequest]
+ -[HMEMessageDatagramClient resetRetryTimerToInitialState]
+ -[HMEMessageDatagramClient retryIntervalProvider]
+ -[HMEMessageDatagramClient retryTimer]
+ -[HMEMessageDatagramClient setHasPendingKeepAliveRequest:]
+ -[HMEMessageDatagramClient setRetryTimer:]
+ GCC_except_table256
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table275
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table397
+ GCC_except_table406
+ GCC_except_table423
+ _OBJC_IVAR_$_HMEMessageDatagramClient._hasPendingKeepAliveRequest
+ _OBJC_IVAR_$_HMEMessageDatagramClient._retryIntervalProvider
+ _OBJC_IVAR_$_HMEMessageDatagramClient._retryTimer
+ ___45-[HMEMessageDatagramClient _enableRetryTimer]_block_invoke
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hasPendingKeepAliveRequest
+ _objc_msgSend$position
+ _objc_msgSend$retryIntervalProvider
+ _objc_msgSend$retryTimer
+ _objc_msgSend$setHasPendingKeepAliveRequest:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setRetryTimer:
- -[HMEMessageDatagramClient _enableReconnectTimer]
- -[HMEMessageDatagramClient _removeReconnectTimer]
- -[HMEMessageDatagramClient _removeReconnectionTimerAndResetInterval]
- -[HMEMessageDatagramClient connectionRetryIntervalProvider]
- -[HMEMessageDatagramClient connectionRetryTimer]
- -[HMEMessageDatagramClient resetReconnectTimerToInitialState]
- -[HMEMessageDatagramClient setConnectionRetryTimer:]
- GCC_except_table254
- GCC_except_table257
- GCC_except_table261
- GCC_except_table267
- GCC_except_table269
- GCC_except_table272
- GCC_except_table274
- GCC_except_table276
- GCC_except_table388
- GCC_except_table390
- GCC_except_table394
- GCC_except_table403
- GCC_except_table420
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBJC_IVAR_$_HMEMessageDatagramClient._connectionRetryIntervalProvider
- _OBJC_IVAR_$_HMEMessageDatagramClient._connectionRetryTimer
- ___49-[HMEMessageDatagramClient _enableReconnectTimer]_block_invoke
- _objc_msgSend$connectionRetryIntervalProvider
- _objc_msgSend$connectionRetryTimer
- _objc_msgSend$setConnectionRetryTimer:
CStrings:
+ "Keep alive request responded"
+ "Keep alive request responded with %@ error: %@"
+ "Removing retry timer"
+ "Retry timer fired: %f"
+ "Server identifier changed and removing retry timer"
+ "Starting retry timer with interval: %f"
+ "T@\"<HMETimer>\",&,N,V_retryTimer"
+ "T@\"<HMETimerIntervalProvider>\",R,V_retryIntervalProvider"
+ "TB,N,V_hasPendingKeepAliveRequest"
+ "[HMEMessageDatagramClient connection mode: %ld, connected: %d, connected server UUID: %@, retry timer interval: %f, dormant fetch conditions met: %d, \n\t event router client: %@]"
+ "_hasPendingKeepAliveRequest"
+ "_retryIntervalProvider"
+ "_retryTimer"
+ "_setError"
+ "getBytes:range:"
+ "hasError"
+ "hasPendingKeepAliveRequest"
+ "non-terminating"
+ "position"
+ "resetRetryTimerToInitialState"
+ "retryIntervalProvider"
+ "retryTimer"
+ "setHasPendingKeepAliveRequest:"
+ "setPosition:"
+ "setRetryTimer:"
+ "terminating"
- " with non-terminating error: "
- "Connection retry timer fired: %f"
- "Keep alive request responded with terminating error: %@"
- "Keep alive request responded%@%@"
- "Removing reconnection timer"
- "Server identifier changed and removing reconnection timer"
- "Starting connection retry timer with interval: %f"
- "T@\"<HMETimer>\",&,N,V_connectionRetryTimer"
- "T@\"<HMETimerIntervalProvider>\",R,V_connectionRetryIntervalProvider"
- "[HMEMessageDatagramClient connection mode: %ld, connected: %d, connected server UUID: %@, connection retry timer interval: %f, dormant fetch conditions met: %d, \n\t event router client: %@]"
- "_connectionRetryIntervalProvider"
- "_connectionRetryTimer"
- "connectionRetryIntervalProvider"
- "connectionRetryTimer"
- "resetReconnectTimerToInitialState"
- "setConnectionRetryTimer:"

```
