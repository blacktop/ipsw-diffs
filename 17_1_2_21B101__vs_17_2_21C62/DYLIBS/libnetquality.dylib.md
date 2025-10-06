## libnetquality.dylib

> `/usr/lib/libnetquality.dylib`

```diff

-113.0.0.0.0
-  __TEXT.__text: 0x14a68
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x1170
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x3d8
-  __TEXT.__cstring: 0x1eff
-  __TEXT.__oslogstring: 0x162a
-  __TEXT.__unwind_info: 0x468
+113.60.5.0.0
+  __TEXT.__text: 0x15698
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x11d0
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__cstring: 0x208b
+  __TEXT.__oslogstring: 0x146d
+  __TEXT.__unwind_info: 0x47c
   __TEXT.__objc_classname: 0x2f2
-  __TEXT.__objc_methname: 0x359f
-  __TEXT.__objc_methtype: 0xc1a
-  __TEXT.__objc_stubs: 0x2ca0
+  __TEXT.__objc_methname: 0x3747
+  __TEXT.__objc_methtype: 0xc28
+  __TEXT.__objc_stubs: 0x2e20
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x4c8
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2cb0
-  __DATA_CONST.__objc_selrefs: 0xc78
-  __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__cfstring: 0x1400
+  __DATA_CONST.__objc_const: 0x2d90
+  __DATA_CONST.__objc_selrefs: 0xcd8
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x798
-  __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_dictobj: 0x190
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__auth_got: 0x540
   __AUTH.__objc_data: 0x730
   __DATA.__objc_classrefs: 0x148
   __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x328
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0x300
   __DATA.__bss: 0x10
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F73C8C4A-0AFD-34EC-AB2E-DF855C35EA71
-  Functions: 497
-  Symbols:   2048
-  CStrings:  1367
+  UUID: BF06EFE2-7A7A-399F-A4FC-8805350378DF
+  Functions: 509
+  Symbols:   2088
+  CStrings:  1430
 
Symbols:
+ -[NetworkQualityExecutions checkTimeout]
+ -[NetworkQualityExecutions isDraining]
+ -[NetworkQualityExecutions setTimeout].cold.1
+ -[NetworkQualityExecutions throughputSaturated]
+ -[NetworkQualityExecutionsResult mutableOtherValues]
+ -[NetworkQualityExecutionsResult setMutableOtherValues:]
+ -[NetworkQualityResult otherValues]
+ -[NetworkQualityResult protocolNames]
+ -[NetworkQualityResult setOtherValues:]
+ -[NetworkQualityResult setProtocolNames:]
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table49
+ _NetworkQualityErrorExecutionTimeout
+ _NetworkQualityStages_to_string
+ _OBJC_IVAR_$_NetworkQualityExecutions._startCapacityTest
+ _OBJC_IVAR_$_NetworkQualityExecutions._throughputSaturated
+ _OBJC_IVAR_$_NetworkQualityExecutionsResult._mutableOtherValues
+ _OBJC_IVAR_$_NetworkQualityResult._otherValues
+ _OBJC_IVAR_$_NetworkQualityResult._protocolNames
+ ___31-[NetworkQualityExecutions run]_block_invoke.103
+ ___31-[NetworkQualityExecutions run]_block_invoke.103.cold.1
+ ___31-[NetworkQualityExecutions run]_block_invoke.104
+ ___31-[NetworkQualityExecutions run]_block_invoke.75
+ ___31-[NetworkQualityExecutions run]_block_invoke.75.cold.1
+ ___31-[NetworkQualityExecutions run]_block_invoke.76
+ ___31-[NetworkQualityExecutions run]_block_invoke.89
+ ___31-[NetworkQualityExecutions run]_block_invoke.89.cold.1
+ ___31-[NetworkQualityExecutions run]_block_invoke.90
+ ___33-[NetworkQualityExecutions drain]_block_invoke.44
+ ___33-[NetworkQualityExecutions drain]_block_invoke.44.cold.1
+ ___33-[NetworkQualityExecutions drain]_block_invoke.48
+ ___33-[NetworkQualityExecutions drain]_block_invoke.48.cold.1
+ ___33-[NetworkQualityExecutions drain]_block_invoke.49
+ ___33-[NetworkQualityExecutions drain]_block_invoke.49.cold.1
+ ___38-[NetworkQualityExecutions setTimeout]_block_invoke
+ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.108
+ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.128
+ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.128.cold.1
+ ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.232
+ ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.159
+ ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.159.cold.1
+ ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.165
+ ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.165.cold.1
+ ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.233
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.172
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.172.cold.1
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.173
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.174
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.174.cold.1
+ ___76-[IdleLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]_block_invoke_2
+ ___79-[WorkingLatencyURLSessionDelegate URLSession:task:didFinishCollectingMetrics:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e54_B28?0"NSObject<OS_nw_protocol_definition>"8i16i20B24ls32l8s40l8
+ __unnamed_array_storage.153
+ __unnamed_array_storage.179
+ __unnamed_array_storage.180
+ _nw_connection_client_accurate_ecn_state_to_string
+ _nw_establishment_report_enumerate_protocol_l4s_state
+ _objc_msgSend$allKeys
+ _objc_msgSend$checkTimeout
+ _objc_msgSend$isDraining
+ _objc_msgSend$mutableOtherValues
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$otherValues
+ _objc_msgSend$protocolNames
+ _objc_msgSend$setMutableOtherValues:
+ _objc_msgSend$setOtherValues:
+ _objc_msgSend$setProtocolNames:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$throughputSaturated
- -[LatencyURLSessionDelegate didFinishCollectingMetrics:task:].cold.3
- -[NetworkQualityExecutions nextStageIs:]
- GCC_except_table31
- GCC_except_table38
- GCC_except_table43
- ___31-[NetworkQualityExecutions run]_block_invoke.66
- ___31-[NetworkQualityExecutions run]_block_invoke.66.cold.1
- ___31-[NetworkQualityExecutions run]_block_invoke.67
- ___31-[NetworkQualityExecutions run]_block_invoke.81
- ___31-[NetworkQualityExecutions run]_block_invoke.81.cold.1
- ___31-[NetworkQualityExecutions run]_block_invoke.82
- ___31-[NetworkQualityExecutions run]_block_invoke.95
- ___31-[NetworkQualityExecutions run]_block_invoke.95.cold.1
- ___31-[NetworkQualityExecutions run]_block_invoke.96
- ___33-[NetworkQualityExecutions drain]_block_invoke.40
- ___33-[NetworkQualityExecutions drain]_block_invoke.40.cold.1
- ___33-[NetworkQualityExecutions drain]_block_invoke.41
- ___33-[NetworkQualityExecutions drain]_block_invoke.41.cold.1
- ___33-[NetworkQualityExecutions drain]_block_invoke.cold.1
- ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.100
- ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.120
- ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke.120.cold.1
- ___55-[WorkingLatencyURLSessionDelegate scheduleNewTaskSelf]_block_invoke.202
- ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.152
- ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.152.cold.1
- ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.158
- ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.158.cold.1
- ___58-[WorkingLatencyURLSessionDelegate scheduleNewTaskForeign]_block_invoke.203
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.165
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.165.cold.1
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.166
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.167
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.167.cold.1
- __unnamed_array_storage.146
- __unnamed_array_storage.172
- __unnamed_array_storage.173
- __unnamed_array_storage.20
- __unnamed_array_storage.27
- __unnamed_array_storage.28
- _objc_msgSend$nextStageIs:
CStrings:
+ "\x06\x1115\x14"
+ "\x11\x1f\x0f"
+ "%s:%u - %s - Didn't yet reach stability with instantaneous val %.2f stddev %.2f (%.2f %%), running for %.2f sec"
+ "%s:%u - Cancelling with %ld"
+ "%s:%u - Current Stage=%s | Next Stage=%s | Cancelled=%d"
+ "%s:%u - Unexpected number of transactionMetrics | cancelled=%d on task %@"
+ "%s:%u - [Staging] In stage %s (%u), setting timeout to %@ - now %@ (divisor: %u, timeLeft %.3f)"
+ "%s:%u - [Staging] not draining until minRuntime expired in %ld seconds"
+ "%s:%u - [Staging] stage %s (%u) ran for too long. Moving on."
+ "-[NetworkQualityExecutions _cancelWithOptionalError:]"
+ "-[NetworkQualityExecutions checkTimeout]"
+ "B28@?0@\"NSObject<OS_nw_protocol_definition>\"8i16i20B24"
+ "CapacityDownlink"
+ "CapacityParallel"
+ "CapacityUplink"
+ "DownlinkDraining"
+ "DownlinkResponsiveness"
+ "IdleDraining"
+ "IdleLatency"
+ "ParallelDraining"
+ "ParallelResponsiveness"
+ "Start"
+ "T@\"NSDictionary\",C,V_otherValues"
+ "T@\"NSDictionary\",C,V_protocolNames"
+ "T@\"NSMutableDictionary\",&,V_mutableOtherValues"
+ "TB,R,V_throughputSaturated"
+ "Unexpected number of transactionMetrics"
+ "UnknownStage"
+ "UplinkDraining"
+ "UplinkResponsiveness"
+ "[self isDraining]"
+ "_mutableOtherValues"
+ "_otherValues"
+ "_protocolNames"
+ "_startCapacityTest"
+ "_throughputSaturated"
+ "allKeys"
+ "canceled"
+ "checkTimeout"
+ "disabled"
+ "divisor > 0"
+ "ecn_ace_bleaching"
+ "ecn_blackholed"
+ "ecn_classic"
+ "ecn_disabled"
+ "ecn_ect_bleaching"
+ "ecn_ect_mangling"
+ "ecn_enabled"
+ "ecn_invalid_state"
+ "ecn_unavailable"
+ "ecn_unknown_state"
+ "ecn_values"
+ "enabled"
+ "i32@0:8@16@24"
+ "isDraining"
+ "l4s"
+ "l4s_enablement"
+ "mutableOtherValues"
+ "not_proxied"
+ "numberWithBool:"
+ "objectForKey:"
+ "otherValues"
+ "protocolNames"
+ "protocolNamesValues"
+ "protocols_seen"
+ "proxy_state"
+ "setMutableOtherValues:"
+ "setOtherValues:"
+ "setProtocolNames:"
+ "setValue:forKey:"
+ "throughputSaturated"
- "\x06\x1115\x13"
- "\x11\x1f\r"
- "%s:%u - %s - Didn't yet reach stability with instantaneous val %.2f stddev %.2f (%.2f %%), running for %.2f sec. out of minimum %ld sec."
- "%s:%u - There's not just 1 transactionMetrics: %lu on task %@"
- "%s:%u - [Staging] In stage %u, setting timeout to %@ - now %@ (divisor: %u, timeLeft %.3f)"
- "%s:%u - [Staging] NetworkQualityStageCapacityDownlink"
- "%s:%u - [Staging] NetworkQualityStageCapacityParallel"
- "%s:%u - [Staging] NetworkQualityStageCapacityUplink"
- "%s:%u - [Staging] NetworkQualityStageDownlinkDraining"
- "%s:%u - [Staging] NetworkQualityStageDownlinkResponsiveness"
- "%s:%u - [Staging] NetworkQualityStageIdleDraining"
- "%s:%u - [Staging] NetworkQualityStageIdleLatency"
- "%s:%u - [Staging] NetworkQualityStageParallelDraining"
- "%s:%u - [Staging] NetworkQualityStageParallelResponsiveness"
- "%s:%u - [Staging] NetworkQualityStageUplinkDraining"
- "%s:%u - [Staging] NetworkQualityStageUplinkResponsiveness"
- "%s:%u - [Staging] stage %u ran for too long. Moving on."
- "-[NetworkQualityExecutions shareProgress]"
- "There are more than just 1 transactionMetrics"
- "[self currentStageIs:NetworkQualityStageIdleDraining] || [self currentStageIs:NetworkQualityStageParallelDraining] || [self currentStageIs:NetworkQualityStageDownlinkDraining] || [self currentStageIs:NetworkQualityStageUplinkDraining]"
- "nextStageIs:"

```
