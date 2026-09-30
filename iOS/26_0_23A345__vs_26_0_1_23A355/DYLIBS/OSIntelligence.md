## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-222.2.2.0.0
-  __TEXT.__text: 0x188c0
+222.2.3.0.0
+  __TEXT.__text: 0x185e4
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x2088
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x1755
-  __TEXT.__gcc_except_tab: 0x648
-  __TEXT.__oslogstring: 0x1aaf
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__objc_methlist: 0x2080
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x1770
+  __TEXT.__gcc_except_tab: 0x624
+  __TEXT.__oslogstring: 0x1b1b
+  __TEXT.__unwind_info: 0x8f0
   __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x3f07
+  __TEXT.__objc_methname: 0x3ecc
   __TEXT.__objc_methtype: 0xba9
-  __TEXT.__objc_stubs: 0x2d00
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x828
+  __TEXT.__objc_stubs: 0x2ca0
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b8
+  __DATA_CONST.__objc_selrefs: 0x10a0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x1380
   __AUTH_CONST.__objc_const: 0x2ec0
   __AUTH_CONST.__objc_intobj: 0x90

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2526353D-E9EC-3FD6-8725-1E623CBDF220
-  Functions: 859
-  Symbols:   2898
-  CStrings:  1359
+  UUID: 78C37BEF-7AE5-3911-8AE2-B08FAADCE97B
+  Functions: 856
+  Symbols:   2883
+  CStrings:  1356
 
Symbols:
+ -[_OSIBLManager triggerIBLMNotification]
+ ___21-[_OSIBLManager init]_block_invoke.85
+ ___21-[_OSIBLManager init]_block_invoke_2.87
+ _objc_msgSend$triggerIBLMNotification
- -[_OSINotificationManager notificationRequestWith:content:]
- -[_OSINotificationManager postNotificationWith:content:]
- GCC_except_table4
- GCC_except_table5
- _OBJC_CLASS_$_UNNotificationIcon
- ___21-[_OSIBLManager init]_block_invoke.82
- ___21-[_OSIBLManager init]_block_invoke_2.84
- ___56-[_OSINotificationManager postNotificationWith:content:]_block_invoke
- ___56-[_OSINotificationManager postNotificationWith:content:]_block_invoke.cold.1
- ___block_descriptor_32_e8_v12?0i8l
- ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
- ___block_literal_global.88
- _objc_msgSend$iconNamed:
- _objc_msgSend$notificationRequestWith:content:
- _objc_msgSend$postIBLMFirstTimeNotification
- _objc_msgSend$setIcon:
CStrings:
+ "Console Mode Status is now %{public}llu"
+ "Notified for IBLM Engaged notification"
+ "Prev12Next12Drain Prediction Confidence: %{public}lf Engagement Threshold: %{public}f"
+ "State updated to %{public}ld from %{public}ld"
+ "Trial: %{public}@:%{public}@:%{public}ld"
+ "Trial: %{public}@:%{public}d"
+ "Trial: %{public}@:%{public}f"
+ "Using cached result %{public}@"
+ "com.apple.osi.iblm.engagedNotification"
+ "triggerIBLMNotification"
- "Console Mode Status is now %llu"
- "Posted notification with error: %@"
- "Prev12Next12Drain Prediction Confidence: %lf Engagement Threshold: %f"
- "State updated to %ld from %ld"
- "Trial: %@:%@:%ld"
- "Trial: %@:%d"
- "Trial: %@:%f"
- "Using cached result %@"
- "battery-rcl"
- "iconNamed:"
- "notificationRequestWith:content:"
- "postNotificationWith:content:"
- "setIcon:"

```
