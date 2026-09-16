## ApplePushService

> `/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService`

```diff

-1168.100.1.0.0
-  __TEXT.__text: 0x1f380
-  __TEXT.__objc_methlist: 0x174c
+1168.200.31.0.0
+  __TEXT.__text: 0x1f9d8
+  __TEXT.__objc_methlist: 0x17c4
   __TEXT.__const: 0xae
-  __TEXT.__cstring: 0x1f6b
+  __TEXT.__cstring: 0x203b
   __TEXT.__oslogstring: 0x26e9
-  __TEXT.__gcc_except_tab: 0x100
+  __TEXT.__gcc_except_tab: 0x118
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0xc50
+  __TEXT.__unwind_info: 0xc88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xed0
+  __DATA_CONST.__const: 0xf20
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xee8
+  __DATA_CONST.__objc_selrefs: 0xf48
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__got: 0x240
-  __AUTH_CONST.__const: 0x7a8
-  __AUTH_CONST.__cfstring: 0x20e0
+  __DATA_CONST.__got: 0x248
+  __AUTH_CONST.__const: 0x7c8
+  __AUTH_CONST.__cfstring: 0x2180
   __AUTH_CONST.__objc_const: 0x2a90
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 858
-  Symbols:   1810
-  CStrings:  584
+  Functions: 873
+  Symbols:   1839
+  CStrings:  591
 
Symbols:
+ +[APSConnection courierBagForEnvironmentName:]
+ -[APSOutgoingMessage firstAttemptTimestamp]
+ -[APSOutgoingMessage firstInterfaceSwitchTimestamp]
+ -[APSOutgoingMessage rawCritical]
+ -[APSOutgoingMessage recordSendAttemptOnInterface:]
+ -[APSOutgoingMessage sendAttemptInterfaceHistory]
+ -[APSOutgoingMessage sendMetricEmitted]
+ -[APSOutgoingMessage setFirstAttemptTimestamp:]
+ -[APSOutgoingMessage setFirstInterfaceSwitchTimestamp:]
+ -[APSOutgoingMessage setSendMetricEmitted:]
+ GCC_except_table220
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table305
+ _APSOutgoingMessageAttemptHistoryKey
+ _APSOutgoingMessageFirstAttemptTimestampKey
+ _APSOutgoingMessageFirstInterfaceSwitchTimestampKey
+ _APSOutgoingMessageSendMetricEmittedKey
+ _APSUseBaggerRegion
+ _OBJC_CLASS_$_NSURL
+ ___46+[APSConnection courierBagForEnvironmentName:]_block_invoke
+ ___46+[APSConnection courierBagForEnvironmentName:]_block_invoke_2
+ ___46+[APSConnection courierBagForEnvironmentName:]_block_invoke_3
+ ___46+[APSConnection courierBagForEnvironmentName:]_block_invoke_4
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ _courierBagForEnvironmentName:.onceToken
+ _courierBagForEnvironmentName:.sQueue
+ _objc_msgSend$firstInterfaceSwitchTimestamp
+ _objc_msgSend$firstObject
+ _objc_msgSend$setFirstAttemptTimestamp:
+ _objc_msgSend$setFirstInterfaceSwitchTimestamp:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- GCC_except_table228
- GCC_except_table231
- GCC_except_table300
CStrings:
+ "APSOutgoingMessageAttemptHistory"
+ "APSOutgoingMessageFirstAttemptTimestamp"
+ "APSOutgoingMessageFirstInterfaceSwitchTimestamp"
+ "APSOutgoingMessageSendMetricEmitted"
+ "APSUseBaggerRegion"
+ "courierBagData"
+ "requestCourierBag"
```
