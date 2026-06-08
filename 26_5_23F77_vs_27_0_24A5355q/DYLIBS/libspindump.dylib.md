## libspindump.dylib

> `/usr/lib/libspindump.dylib`

```diff

-419.10.0.0.0
-  __TEXT.__text: 0x3ab8
-  __TEXT.__auth_stubs: 0x480
+435.0.0.0.0
+  __TEXT.__text: 0x3908
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0xca8
-  __TEXT.__cstring: 0x4a4
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x66
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x70
+  __TEXT.__oslogstring: 0xd3e
+  __TEXT.__cstring: 0x4da
+  __TEXT.__unwind_info: 0x140
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__auth_got: 0x248
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__bss: 0x238

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 453B1833-AF1F-3071-A7ED-213B0CB3BC8E
-  Functions: 84
-  Symbols:   304
-  CStrings:  126
+  UUID: CED35BCA-FF45-3B11-9E3F-03FB42ACFA67
+  Functions: 87
+  Symbols:   309
+  CStrings:  123
 
Symbols:
+ _SPReportIPCMessagesQueuedExhaustion
+ _SPReportIPCMessagesQueuedExhaustion_FatalPort
+ __SPReportIPCMessagesQueuedExhaustion
+ __SPReportIPCMessagesQueuedExhaustion.cold.1
+ __SPReportIPCMessagesQueuedExhaustion.cold.2
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- _OUTLINED_FUNCTION_10
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Reporting %{public}sipc messages queued exhaustion for %{public}s [%d] at %lld ipc messages queued"
+ "Reporting ipc messages queued exhaustion for pid 0"
+ "num_ipc_messages_queued"
+ "num_ipc_messages_queued_limit"
- "UTF8String"
- "bundleIdentifier"
- "infoDictionary"
- "initWithFormat:"
- "length"
- "mainBundle"
- "objectForKeyedSubscript:"

```
