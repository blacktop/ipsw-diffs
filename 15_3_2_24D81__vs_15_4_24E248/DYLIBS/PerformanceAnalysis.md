## PerformanceAnalysis

> `/System/Library/PrivateFrameworks/PerformanceAnalysis.framework/Versions/A/PerformanceAnalysis`

```diff

-382.1.0.0.0
-  __TEXT.__text: 0x4e4c
+385.13.0.0.0
+  __TEXT.__text: 0x4d38
   __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x5f8
+  __TEXT.__objc_methlist: 0x6d8
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x833
   __TEXT.__oslogstring: 0x20c
-  __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__gcc_except_tab: 0x1d0
+  __TEXT.__unwind_info: 0x270
   __TEXT.__objc_classname: 0xf2
   __TEXT.__objc_methname: 0x18fa
   __TEXT.__objc_methtype: 0x25a
   __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8

   __AUTH_CONST.__auth_got: 0x1c8
   __AUTH_CONST.__const: 0x130
   __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0x1230
+  __AUTH_CONST.__objc_const: 0x1078
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0xa8

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 660BF352-26D9-342D-A944-CE2651F3B2F9
-  Functions: 173
-  Symbols:   518
+  UUID: BB502995-D113-30C0-8291-094E9225BB48
+  Functions: 179
+  Symbols:   534
   CStrings:  433
 
Symbols:
+ +[PAPerfLoggingClientOperation existingOperationWithOperationCategory:operationName:].cold.1
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.1
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.2
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.3
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.4
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.5
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.6
+ -[PAPerfLoggingClientOperation endWithType:truncateDurationInSeconds:].cold.7
+ -[PAPerfLoggingClientOperation initAndStartWithOperationCategory:andOperationName:andPid:shouldMonitorWSUpdates:].cold.1
+ -[PAPerfLoggingClientOperation markOperationStart].cold.2
+ -[PAPerfLoggingIntervalData _logPAPerfLoggingDataValue:uom:doLocalLogging:].cold.1
+ PACurrentRealTimeInSeconds.cold.1
+ PAPerfLoggingGetLogHandle.cold.1
+ PAPerfLoggingIntervalPrintHeader.cold.1
+ _intervalTimestampForNSNumberTimestamp.cold.1
+ gWSUpdateHandler_block_invoke_2.cold.1

```
