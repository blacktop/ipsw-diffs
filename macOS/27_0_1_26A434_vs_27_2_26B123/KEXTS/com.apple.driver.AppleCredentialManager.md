## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

```diff

-949.0.17.0.0
-  __TEXT.__cstring: 0x1cc97
+949.40.7.0.0
+  __TEXT.__cstring: 0x1cd4a
   __TEXT.__const: 0x4a0
-  __TEXT_EXEC.__text: 0x7eb2c
-  __TEXT_EXEC.__auth_stubs: 0x750
-  __DATA.__data: 0xa501
+  __TEXT_EXEC.__text: 0x7ee04
+  __TEXT_EXEC.__auth_stubs: 0x760
+  __DATA.__data: 0xa6c9
   __DATA.__common: 0x9c8
   __DATA.__bss: 0x26b9
   __DATA_CONST.__mod_init_func: 0x60

   __DATA_CONST.__const: 0x3260
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0x14f0
-  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x30
-  Functions: 1370
-  Symbols:   2072
-  CStrings:  2965
+  Functions: 1371
+  Symbols:   2074
+  CStrings:  2970
 
Symbols:
+ _DataValidation_DeviceInfo
+ __ZN25ACMAnalyticsKernelService19_onMilestoneReachedEP9IOServiceNS_9MilestoneE
+ __ZN25ACMAnalyticsKernelService25_sendEventToCoreAnalyticsEP9IOServiceNS_9MilestoneERKNS_18ResourceUsageEventE
+ __ZN25ACMAnalyticsKernelService27_onResourceUsageInfoHandlerEP9IOServiceNS_9MilestoneE
+ __ZN25ACMAnalyticsKernelService34_milestoneReachedThreadCallHandlerEPvS0_
+ _thread_call_cancel_wait
+ copyCredentials.kalloc_type_view_9375
- __ZN25ACMAnalyticsKernelService14_onActionTimerEP18IOTimerEventSource
- __ZN25ACMAnalyticsKernelService19_onMilestoneReachedENS_9MilestoneE
- __ZN25ACMAnalyticsKernelService25_sendEventToCoreAnalyticsENS_9MilestoneERKNS_18ResourceUsageEventE
- __ZN25ACMAnalyticsKernelService27_onResourceUsageInfoHandlerENS_9MilestoneE
- copyCredentials.kalloc_type_view_9360
CStrings:
+ "%s: %s: giving up waiting for SEP endpoint after %llums (cmd=%u).\n"
+ "121112222222221"
+ "23:03:54"
+ "DataValidation_DeviceInfo"
+ "Oct 14 2026"
+ "Oct 14 2026, 23:04:10"
+ "_milestoneReachedThreadCall"
+ "_milestoneReachedThreadCallHandler"
+ "ioService"
+ "newValue && newValueSize == sizeof(ACMDeviceInfo)"
- "1211122222222212"
- "18:51:20"
- "Aug 30 2026"
- "Aug 30 2026, 18:51:38"
- "_milestoneReachedAction.actionTimer"
```
