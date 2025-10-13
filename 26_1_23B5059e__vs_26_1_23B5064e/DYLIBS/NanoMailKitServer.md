## NanoMailKitServer

> `/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer`

```diff

-852.0.0.0.0
-  __TEXT.__text: 0x76e8c
+852.1.0.0.0
+  __TEXT.__text: 0x77070
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x942c
+  __TEXT.__objc_methlist: 0x945c
   __TEXT.__const: 0x5b6
   __TEXT.__cstring: 0x4b58
-  __TEXT.__oslogstring: 0x824a
+  __TEXT.__oslogstring: 0x827c
   __TEXT.__gcc_except_tab: 0x3ac
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1800
+  __TEXT.__unwind_info: 0x1808
   __TEXT.__objc_classname: 0xdf1
-  __TEXT.__objc_methname: 0x11a96
-  __TEXT.__objc_methtype: 0x3406
-  __TEXT.__objc_stubs: 0xa9a0
+  __TEXT.__objc_methname: 0x11b01
+  __TEXT.__objc_methtype: 0x3472
+  __TEXT.__objc_stubs: 0xa9e0
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0x1148
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cc0
+  __DATA_CONST.__objc_selrefs: 0x3cd8
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x6540
-  __AUTH_CONST.__objc_const: 0xe450
+  __AUTH_CONST.__objc_const: 0xe460
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 23885B75-5248-3C92-A8CA-CA0686677E43
-  Functions: 3289
-  Symbols:   10193
-  CStrings:  5208
+  UUID: F9ED5C68-C902-373C-A4D9-BFFAA242B9B4
+  Functions: 3292
+  Symbols:   10201
+  CStrings:  5214
 
Symbols:
+ -[NNMKResendScheduler forceRetryingAllPendingIDSMessages].cold.1
+ -[NNMKSyncEndpoint clearResendQueue]
+ -[NNMKSyncProvider resendSchedulerShouldSendRetries:]
+ _objc_msgSend$clearResendQueue
+ _objc_msgSend$resendSchedulerShouldSendRetries:
Functions:
+ -[NNMKSyncEndpoint clearResendQueue]
~ -[NNMKResendScheduler handleIDSMessageFailedWithId:errorCode:] : 452 -> 500
~ -[NNMKResendScheduler forceRetryingAllPendingIDSMessages] : 252 -> 316
~ -[NNMKResendScheduler _scheduleIdsIdentifierForResend:currentResendInterval:newResendInterval:errorCode:] : 216 -> 240
~ ___72-[NNMKSyncProvider initWithDelegate:syncStateManager:directoryProvider:]_block_invoke : 1236 -> 1276
~ -[NNMKSyncProvider messagesSyncServiceServerConnectivityChanged:] : 276 -> 312
+ -[NNMKSyncProvider resendSchedulerShouldSendRetries:]
~ ___59-[NNMKSyncProvider _checkConnectivityBasedSuspensionTimer:]_block_invoke : 368 -> 560
+ -[NNMKResendScheduler forceRetryingAllPendingIDSMessages].cold.1
CStrings:
+ "B24@0:8@\"NNMKResendScheduler\"16"
+ "Message sync suspended, not retrying ids messages"
+ "clearResendQueue"
+ "resendSchedulerShouldSendRetries:"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
