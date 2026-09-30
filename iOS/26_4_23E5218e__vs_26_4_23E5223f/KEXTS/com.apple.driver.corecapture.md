## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

```diff

-1325.17.0.0.0
-  __TEXT.__os_log: 0x42dd
+1325.18.0.0.0
+  __TEXT.__os_log: 0x42ec
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x2004
-  __TEXT_EXEC.__text: 0x25fc8
+  __TEXT.__cstring: 0x200e
+  __TEXT_EXEC.__text: 0x2612c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308

   __DATA_CONST.__const: 0x7010
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 7305C4AF-A52D-34F7-A507-EFC96183F71A
+  UUID: 36B271C8-B7B4-30A3-8065-FA682FA9C708
   Functions: 878
   Symbols:   0
-  CStrings:  658
+  CStrings:  660
 
Functions:
~ __ZN15CCFaultReporter19spinDeferredCaptureEP18IOTimerEventSource : 160 -> 188
~ __ZN15CCFaultReporter25SpinDeferredCommonCaptureEv : 500 -> 632
~ __ZN15CCFaultReporter27callCompleteReportCallbacksEv : 640 -> 672
~ __ZN15CCFaultReporter19reportFaultWithInfoEiPKcjS1_S1_jP12OSDictionary : 1248 -> 1336
~ __ZN15CCFaultReporter12processFaultEP13CCFaultReport : 1668 -> 1700
~ sub_fffffe000a61fbd4 -> sub_fffffe000a58420c : 20 -> 64
CStrings:
+ "<unknown>"
+ "Fault reporter is busy - Active: %s - New request: %s\n"
+ "invalid report\n"
- "Fault reporter is busy -  Active: %s - New request: %s\n"

```
