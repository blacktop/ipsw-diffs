## DistributedSensing

> `/System/Library/PrivateFrameworks/DistributedSensing.framework/Versions/A/DistributedSensing`

```diff

 1.12.0.0.0
-  __TEXT.__text: 0xe05c
+  __TEXT.__text: 0xe074
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x9a8
+  __TEXT.__objc_methlist: 0xb54
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x6a0
   __TEXT.__cstring: 0x587
   __TEXT.__oslogstring: 0x1d59
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_classname: 0x147
   __TEXT.__objc_methname: 0x1b33
   __TEXT.__objc_methtype: 0x451

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x708
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x2140
+  __AUTH_CONST.__objc_const: 0x1e20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x15c

   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4BF45123-5C76-3198-A635-FE62FBD36538
-  Functions: 253
-  Symbols:   767
+  UUID: AC3F1C1C-75B4-3A85-B1B2-0EA1117716C3
+  Functions: 257
+  Symbols:   772
   CStrings:  660
 
Symbols:
+ +[DSMotionStateListenerProxy sharedInstance].cold.1
+ -[DSCoreAnalyticsEventHandler dsSessionCompletedWithStopReason:numHeartbeats:numMotionStateMessages:activeProviderLostCount:dataLinkType:maxListenerClients:avgListenerStartInterval:].cold.1
+ -[DSCoreAnalyticsEventHandler dsSessionCompletedWithStopReason:numHeartbeats:numMotionStateMessages:activeProviderLostCount:dataLinkType:maxListenerClients:avgListenerStartInterval:].cold.2
+ -[DSProvider _receivedDataRequest:options:responseHandler:].cold.1
+ _OUTLINED_FUNCTION_0

```
