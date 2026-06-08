## ManagedEvent

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent`

```diff

-2169.120.7.0.0
-  __TEXT.__text: 0xa90
-  __TEXT.__auth_stubs: 0x1d0
+2357.0.0.0.2
+  __TEXT.__text: 0xa64
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x184
-  __TEXT.__cstring: 0x776
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0x858
+  __TEXT.__unwind_info: 0x88
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xe0
-  __AUTH_CONST.__auth_got: 0xe8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
-  __DATA.__data: 0x2a0
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x310
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 13649D1B-610E-33F2-BF3C-2407F71E28D4
+  UUID: 5D1E3365-F4BE-31EF-B55A-5242145D4703
   Functions: 17
-  Symbols:   166
-  CStrings:  95
+  Symbols:   178
+  CStrings:  109
 
Symbols:
+ _kSymptomManagedEventKeyBBHAONRNF
+ _kSymptomManagedEventKeyBBHProbeTimeout
+ _kSymptomManagedEventKeyCensusAppsBudgetExhausted
+ _kSymptomManagedEventKeyCensusFlowsIdle
+ _kSymptomManagedEventKeyCensusFlowsNotOurStack
+ _kSymptomManagedEventKeyCensusFlowsQuic
+ _kSymptomManagedEventKeyCensusFlowsQuicMigratable
+ _kSymptomManagedEventKeyCensusFlowsRawUDP
+ _kSymptomManagedEventKeyCensusFlowsRnfEligible
+ _kSymptomManagedEventKeyCensusFlowsRnfIneligible
+ _kSymptomManagedEventKeyCensusFlowsSocketsRawUDP
+ _kSymptomManagedEventKeyCensusFlowsSocketsTCP
+ _kSymptomManagedEventKeyCensusTotalFlows
+ _kSymptomManagedEventKeyTriggerCensusData
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ _managed_event_fetch -> _managed_event_fetch_completion : 172 -> 224
~ _msg_requesting -> ___managed_event_fetch_helper_block_invoke : 136 -> 524
~ _managed_event_send_with_reply -> ___managed_event_compose_from_xpc_object_block_invoke : 168 -> 324
~ ___managed_event_fetch_helper_block_invoke -> _managed_event_fetch : 524 -> 172
~ ___managed_event_compose_from_xpc_object_block_invoke -> _msg_requesting : 324 -> 136
~ _managed_event_fetch_completion -> _managed_event_send_with_reply : 224 -> 168
~ ___managed_event_get_connection_block_invoke : 468 -> 424
CStrings:
+ "aon-rnf"
+ "apps-budget-exhausted"
+ "census-data"
+ "flows-idle"
+ "flows-not-our-stack"
+ "flows-quic"
+ "flows-quic-migratable"
+ "flows-raw-udp"
+ "flows-rnf-eligible"
+ "flows-rnf-ineligible"
+ "flows-sockets-raw-udp"
+ "flows-sockets-tcp"
+ "probe-timeout"
+ "total-flows"

```
