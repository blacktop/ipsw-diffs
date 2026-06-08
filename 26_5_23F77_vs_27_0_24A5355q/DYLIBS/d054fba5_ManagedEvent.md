## ManagedEvent

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent`

```diff

-2169.120.7.0.0
-  __TEXT.__text: 0xa90 sha256:874cd7511f2a314caec81eca11b34ca11d885ca5ed8b589b8efc528f85707b7a
-  __TEXT.__auth_stubs: 0x1d0 sha256:68b373b473739a228c9bf75455e3cc4bcb205a48f227555b14d4bc33bc7893bb
+2357.0.0.0.2
+  __TEXT.__text: 0xa64 sha256:1e6041dd5eecdd51c80821e4349ec61c820e89a584e9975c3dee8303ad29f80b
   __TEXT.__const: 0x18 sha256:97d6c6ba80894cc6faffb874e0966524a9825921997bb75ddd81bec11be4cd0c
   __TEXT.__oslogstring: 0x184 sha256:692985ddaba61134e971e24fb67a016eb4ef0976bba0e93200002ae7236647c1
-  __TEXT.__cstring: 0x776 sha256:4dda0797886705474335092f41ee337ad9037f81651b809fbf26ac85b6c26d8c
-  __TEXT.__unwind_info: 0x90 sha256:025084e75e5b89d25fb10a9b3c872f11d111756d3d667c1afb507818d7af6d33
-  __DATA_CONST.__got: 0x58 sha256:10eef285deef7a4b7c82b22aa53589b7833df29de3814649c772bbd5c832f365
-  __DATA_CONST.__const: 0xe0 sha256:139041fe60ab0317465f27eebd3c3db0ffe56995b90a4f80635cba166b31d005
-  __AUTH_CONST.__auth_got: 0xe8 sha256:c4fcd50d9f0c893c46288b57d8e62b18523145956b249b6ecd6c21718be49065
-  __AUTH_CONST.__const: 0x40 sha256:19ee057d6d3bd20ac8e4b8664a3d8d0d6938baac158f0491f4bf4fb4670b1ec8
-  __DATA.__data: 0x2a0 sha256:f3373a5e11ccef1ee1cf8075cc45ec599da9d4d7490099e0a5fc491cf4dc04d9
+  __TEXT.__cstring: 0x858 sha256:a5e258cb4780ae4a45d3c1d6cbd17e414b50feabc40abd5980290dc1b2340d73
+  __TEXT.__unwind_info: 0x88 sha256:51b9540733c0932c058a135f27cfd28f84cbf0956bd137cd234e40f8659e5ebc
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xe0 sha256:59b8db687dabe2718d71f2e326d075ca1beda0607f6303a3780985a495b38174
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x40 sha256:e13cc1cce32fb49b38dedb94105624685ace4d31f81a926cd7e83360e2c27972
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x310 sha256:6a5cba22b65e7a0f4749cec6ef6d0477792ab760a103add68e3c6ade82521db1
   __DATA_DIRTY.__bss: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
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
~ ___managed_event_send_with_reply_block_invoke : sha256 530a6cb4b235ec2df50fa26240acfc84d7cbd128f1314191208a348fbec4de9a -> 85db15bca2d167604f4796904443765e1fb49dcec0271405a17d3c80594c3d8c
~ _managed_event_fetch_series : sha256 81a6dc1a671475bb840c770d318727549d9e92884180d20efb04fcefa2e892c7 -> 814a8be0877cef9e29d8ca8015c5731e514a2128b9d24238c6f94c663b203301
~ ___managed_event_get_queue_block_invoke : sha256 7d40efaf7c4cc4c928bea8b6a9a7c477632dc34f0f41844b0c15511a2688ec3f -> b2695e2361531e4bc941b48639095bb6ac5b055517b2ef409109172e8cf211fc
~ ___managed_event_get_connection_block_invoke : 468 -> 424
~ _OUTLINED_FUNCTION_0 : sha256 d2ab6a011acc7054d313002a3f3566d25d57796ef1e6c54b1bf0caeca0a8dc5d -> 902a28da609d5e09e803be22da6be77255745fe6489e0fd9d9e916a5eb755e0c
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
