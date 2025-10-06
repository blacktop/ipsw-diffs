## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-1439.40.24.0.0
-  __TEXT.__text: 0x20618
+1439.60.20.0.1
+  __TEXT.__text: 0x2085c
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x22d8
+  __TEXT.__objc_methlist: 0x22e0
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x944
+  __TEXT.__gcc_except_tab: 0x954
   __TEXT.__cstring: 0x1940
-  __TEXT.__oslogstring: 0x19ba
-  __TEXT.__unwind_info: 0x978
+  __TEXT.__oslogstring: 0x19e5
+  __TEXT.__unwind_info: 0x98c
   __TEXT.__objc_classname: 0x4a1
-  __TEXT.__objc_methname: 0x7119
-  __TEXT.__objc_methtype: 0xd5b
-  __TEXT.__objc_stubs: 0x4160
+  __TEXT.__objc_methname: 0x714f
+  __TEXT.__objc_methtype: 0xd8a
+  __TEXT.__objc_stubs: 0x4180
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4578
-  __DATA_CONST.__objc_selrefs: 0x1990
+  __DATA_CONST.__objc_const: 0x45b8
+  __DATA_CONST.__objc_selrefs: 0x19a0
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__cfstring: 0x26c0
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A8BA962-BE7F-3FA5-A8F6-A22707F9987E
-  Functions: 911
-  Symbols:   3316
-  CStrings:  2208
+  UUID: EC82153B-F482-3B74-AB0D-7D09092712A8
+  Functions: 915
+  Symbols:   3327
+  CStrings:  2214
 
Symbols:
+ -[_DASScheduler enableTaskRegistryMode:]
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table128
+ GCC_except_table97
+ ___25-[_DASScheduler policies]_block_invoke.235
+ ___27-[_DASScheduler allBudgets]_block_invoke.232
+ ___27-[_DASScheduler clasStatus]_block_invoke.236
+ ___27-[_DASScheduler statistics]_block_invoke.231
+ ___31-[_DASScheduler runActivities:]_block_invoke.246
+ ___33-[_DASScheduler deferActivities:]_block_invoke.225
+ ___34-[_DASScheduler evaluatePolicies:]_block_invoke.237
+ ___35-[_DASScheduler currentPredictions]_block_invoke.229
+ ___35-[_DASScheduler submitTaskRequest:]_block_invoke.251
+ ___36-[_DASScheduler submittedActivities]_block_invoke.227
+ ___37-[_DASScheduler completeTaskRequest:]_block_invoke.254
+ ___37-[_DASScheduler completeTaskRequest:]_block_invoke.254.cold.1
+ ___37-[_DASScheduler pauseWithParameters:]_block_invoke.243
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.253
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.253.cold.1
+ ___38-[_DASScheduler evaluateAllActivities]_block_invoke.238
+ ___40-[_DASScheduler enableTaskRegistryMode:]_block_invoke
+ ___40-[_DASScheduler enableTaskRegistryMode:]_block_invoke.241
+ ___40-[_DASScheduler enableTaskRegistryMode:]_block_invoke.cold.1
+ ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.244
+ ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.233
+ ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.212
+ ___42-[_DASScheduler runProceedableActivities:]_block_invoke.239
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.242
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.242.cold.1
+ ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.245
+ ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.240
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.252
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.252.cold.1
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.257
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.257.cold.1
+ ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.258
+ ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.258.cold.1
+ ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.255
+ ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.255.cold.1
+ ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.256
+ ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.256.cold.1
+ ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_literal_global.248
+ _objc_msgSend$enableTaskRegistryMode:handler:
- GCC_except_table106
- GCC_except_table114
- GCC_except_table125
- ___25-[_DASScheduler policies]_block_invoke.232
- ___27-[_DASScheduler allBudgets]_block_invoke.229
- ___27-[_DASScheduler clasStatus]_block_invoke.233
- ___27-[_DASScheduler statistics]_block_invoke.228
- ___31-[_DASScheduler runActivities:]_block_invoke.242
- ___33-[_DASScheduler deferActivities:]_block_invoke.222
- ___34-[_DASScheduler evaluatePolicies:]_block_invoke.234
- ___35-[_DASScheduler currentPredictions]_block_invoke.226
- ___35-[_DASScheduler submitTaskRequest:]_block_invoke.247
- ___36-[_DASScheduler submittedActivities]_block_invoke.224
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke.250
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke.250.cold.1
- ___37-[_DASScheduler pauseWithParameters:]_block_invoke.239
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.249
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.249.cold.1
- ___38-[_DASScheduler evaluateAllActivities]_block_invoke.235
- ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.240
- ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.230
- ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.209
- ___42-[_DASScheduler runProceedableActivities:]_block_invoke.236
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.238
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.238.cold.1
- ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.241
- ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.237
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.248
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.248.cold.1
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.253
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.253.cold.1
- ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.254
- ___52-[_DASScheduler unregisterSystemTaskWithIdentifier:]_block_invoke.254.cold.1
- ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.251
- ___59-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:]_block_invoke.251.cold.1
- ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.252
- ___63-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:]_block_invoke.252.cold.1
- ___block_literal_global.244
CStrings:
+ "B20@0:8B16"
+ "Error setting task registry mode to %i: %@"
+ "enableTaskRegistryMode:"
+ "enableTaskRegistryMode:handler:"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B>20"

```
