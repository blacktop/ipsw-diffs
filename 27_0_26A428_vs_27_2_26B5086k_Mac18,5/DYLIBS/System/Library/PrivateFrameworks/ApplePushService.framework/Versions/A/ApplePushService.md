## ApplePushService

> `/System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService`

```diff

-1168.100.1.1.1
-  __TEXT.__text: 0x296e8
-  __TEXT.__objc_methlist: 0x1c4c
-  __TEXT.__cstring: 0x24db
-  __TEXT.__gcc_except_tab: 0x4d8
+1168.200.31.0.0
+  __TEXT.__text: 0x29d74
+  __TEXT.__objc_methlist: 0x1cc4
+  __TEXT.__cstring: 0x25ab
+  __TEXT.__gcc_except_tab: 0x4f0
   __TEXT.__const: 0x136
   __TEXT.__oslogstring: 0x361b
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0xfc0
+  __TEXT.__unwind_info: 0xff0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e0
+  __DATA_CONST.__objc_selrefs: 0x1240
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x288
-  __AUTH_CONST.__const: 0x12c8
-  __AUTH_CONST.__cfstring: 0x22e0
+  __DATA_CONST.__got: 0x290
+  __AUTH_CONST.__const: 0x1318
+  __AUTH_CONST.__cfstring: 0x2380
   __AUTH_CONST.__objc_const: 0x2fe0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x430

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1098
-  Symbols:   2205
-  CStrings:  722
+  Functions: 1113
+  Symbols:   2234
+  CStrings:  729
 
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
+ GCC_except_table227
+ GCC_except_table240
+ GCC_except_table243
+ GCC_except_table310
+ GCC_except_table339
+ GCC_except_table351
+ GCC_except_table357
+ GCC_except_table360
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
+ ___block_descriptor_56_e8_32s40r_e5_v8?0l
+ _objc_msgSend$firstInterfaceSwitchTimestamp
+ _objc_msgSend$firstObject
+ _objc_msgSend$setFirstAttemptTimestamp:
+ _objc_msgSend$setFirstInterfaceSwitchTimestamp:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ courierBagForEnvironmentName:.onceToken
+ courierBagForEnvironmentName:.sQueue
- GCC_except_table235
- GCC_except_table238
- GCC_except_table305
- GCC_except_table334
- GCC_except_table346
- GCC_except_table352
- GCC_except_table355
CStrings:
+ "APSOutgoingMessageAttemptHistory"
+ "APSOutgoingMessageFirstAttemptTimestamp"
+ "APSOutgoingMessageFirstInterfaceSwitchTimestamp"
+ "APSOutgoingMessageSendMetricEmitted"
+ "APSUseBaggerRegion"
+ "courierBagData"
+ "requestCourierBag"
```
