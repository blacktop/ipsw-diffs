## com.apple.EXBrightKext

> `com.apple.EXBrightKext`

```diff

-2079.120.10.0.0
+2285.0.0.502.1
   __TEXT.__const: 0x118 sha256:e73774659ada8e71f2b77abc51fe5186916125f20a72b2dfdbfb1a33a0dcffac
-  __TEXT.__cstring: 0x4180 sha256:4fb935381ce11d5234526485e21f7c335e1909746d0f3e2d1b8f5967254ed9d6
-  __TEXT_EXEC.__text: 0x13a98 sha256:09da8399c446728005d946dde733e31d7245dedff7d32191532b19da49d16830
+  __TEXT.__cstring: 0x47c9 sha256:e9fefa8b4ec5ea81251884c2d89e6741a2b489bc3f095dddf7aadd5ffe185fcf
+  __TEXT_EXEC.__text: 0x16594 sha256:8d8b9eb0faaf7de7cd28048fc0a894c20458a4eb2502cae2679ba4c4bdda7668
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xd8 sha256:9527b5b3940891ae1acec542204acc9f1e5604bfb6303636706eb8cb52f2f8d4
+  __DATA.__data: 0xd8 sha256:a31a64d70a9e2edafa34b35c7f0907d84f0f8fe934ebfc80b4519c0984110adb
   __DATA.__common: 0x130 sha256:e2fc162ed9124452d23c85e81d60a0c228f414c3214a5de635737e25fbd29ac1
   __DATA.__bss: 0x2 sha256:96a296d224f285c67bee93c30f8a309157f0daa35dc5b87e410b78630a09cfc7
-  __DATA_CONST.__auth_got: 0x340 sha256:ae249fc25d88a5845ee147d8bcfa02f8eaa7a2de8239d6774829caec0a93f317
-  __DATA_CONST.__got: 0x80 sha256:bb52404ab8b219745aadfc34ce768609d205869efe0c87649675a5dbe5d135f0
-  __DATA_CONST.__mod_init_func: 0x30 sha256:87d2dc76af6fbbf84c340dd990902b23f0eda82eb945474aabd826e80f713b78
-  __DATA_CONST.__mod_term_func: 0x30 sha256:b37b63289e1164aa61940a70d5f197b55e30e4aba0c64b72cb1cfe145bba5e24
-  __DATA_CONST.__const: 0x1e00 sha256:d343dd2c660ad322a818f4252766cf3d8c20b2b63c650e2239d700cbd311fbee
-  __DATA_CONST.__kalloc_type: 0x1c0 sha256:fe89a389d8a6cd13bcfd83f13c0f34dd16a5da26f1420dc55802319ddc822c80
-  UUID: F42C8E30-A477-3D5A-9ABD-586C67AF6651
-  Functions: 519
+  __DATA_CONST.__mod_init_func: 0x30 sha256:7cf2208673ef9d1403fd3d6183026966107a10e60c8531a376c538613ce46010
+  __DATA_CONST.__mod_term_func: 0x30 sha256:764cd08d1d8cf5c08f3aaf29032577c1af181df951c92b9306152aff65d3cf30
+  __DATA_CONST.__const: 0x1f60 sha256:7760a215580869be1637e0e65d09ff2d8fce3dfc24a8fb9fb0880fe2935bc81e
+  __DATA_CONST.__kalloc_type: 0x1c0 sha256:784b9de126be6d58a8a625b2e17386873106bfbf401577bc8a00772e1617f3b6
+  __DATA_CONST.__auth_got: 0x378 sha256:9941120952c82ab8b3fc037c3200cc60641757d97d9484bb4921739dad62e6e8
+  __DATA_CONST.__got: 0x90 sha256:fcb0c740e7d202db339f005f908c8bbf883e97645d676f853f80fa40c392115e
+  UUID: E8923727-FC45-3693-8F0A-F8A6310D451C
+  Functions: 572
   Symbols:   0
-  CStrings:  282
+  CStrings:  310
 
CStrings:
+ "\"TB_ASSERT: \" \"(server->getindicatorstates != ((void*)0)) && \\\"implementation for getIndicatorStates is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid tag in `[EXBrightKextInterface.EXBrightIndicatorState]` metadata: 0x%x\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid tag in `[EXBrightKextInterface.EXBrightMIBData]` metadata: 0x%x\" @%s:%d"
+ "\"TB_FATAL: \" \"overflow detected when multiplying\" @%s:%d"
+ "1211111212221212111111121111111211111222212111111112"
+ "121112"
+ "EXBrightMIBOverrideDisplayID"
+ "EXBrightSILStateUntrusted"
+ "EXBrightSILStateUntrustedDisplayID"
+ "EXBrightSILStateUntrustedEnable"
+ "EXBrightToggleFakeMIBStreamingDisplayID"
+ "EXBrightToggleFakeMIBStreamingEnable"
+ "EXBrightUIBrightnessDisplayID"
+ "EXBrightUIBrightnessValue"
+ "I48@?0{exbrightkextinterface_exbrightindicatorstate_v_s=C(?={?=^{exbrightkextinterface_exbrightindicatorstate_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8"
+ "I56@?0{exbrightkextinterface_exbrightmibdata_v__opt_s=B{exbrightkextinterface_exbrightmibdata_v_s=C(?={?=^{exbrightkextinterface_exbrightmibdata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8"
+ "I88@?0{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata__opt_s=B{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata_s=QIffQ{exbrightkextinterfacedebug_exbrightxtalkestimates_s=Q(?={?={exbrightkextinterfacedebug_exbrightalsschannelestimates_s=Q(?={?=[2f]}{?=[5f]})}})}}}8"
+ "[%s] %s %s with value %d for display %d\n"
+ "[%s] Created telemetry dictionary for display %u\n"
+ "[%s] Fake streaming %sabled for display %u\n"
+ "[%s] [ERR] Aggregated telemetry array not initialized!\n"
+ "[%s] [ERR] Display dictionary missing displayID key\n"
+ "[%s] [ERR] Failed to add telemetry data to dictionary for type %s for display %u\n"
+ "[%s] [ERR] Failed to create OSNumber for display id %u\n"
+ "[%s] [ERR] Failed to create iterator for telemetry dump of display %u\n"
+ "[%s] [ERR] Failed to create iterator over telemetry array!\n"
+ "[%s] [ERR] Failed to create telemetry dictionary for display %u\n"
+ "[%s] [ERR] Failed to initialize OSArray with capacity %u\n"
+ "[%s] [ERR] Failed to set telemetry dictionary in array for display id %u\n"
+ "[%s] [ERR] Failed to submit telemetry '%s' for display %u, error: 0x%x\n"
+ "[%s] [ERR] Failed to update telemetry data for type %s for display %u\n"
+ "[%s] [ERR] Fetched MIB data with invalid display id %u\n"
+ "[%s] [ERR] Invalid display id %d for property %s\n"
+ "[%s] [ERR] Invalid display id %u\n"
+ "[%s] [ERR] No telemetry dictionary found for display %u\n"
+ "[%s] [ERR] Unknown channel count for estimates\n"
+ "[%s] [ERR] [%s] Invalid display id %u\n"
+ "[%s] [ERR] [getSILDebug] invalid display id %d\n"
+ "[%s] [INF] = Display %u =\n"
+ "[%s] [INF] Telemetry dump - Total display entries: %u\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "displayID"
+ "fetchIndicatorStates_block_invoke_2"
+ "v24@?0Q8r^{exbrightkextinterface_exbrightindicatorstate_s=BC}16"
+ "v24@?0Q8r^{exbrightkextinterface_exbrightmibdata_s=QfBfC}16"
+ "v48@?0{exbrightkextinterface_exbrightindicatorstate_v_s=C(?={?=^{exbrightkextinterface_exbrightindicatorstate_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8"
+ "v56@?0{exbrightkextinterface_exbrightmibdata_v__opt_s=B{exbrightkextinterface_exbrightmibdata_v_s=C(?={?=^{exbrightkextinterface_exbrightmibdata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8"
+ "v88@?0{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata__opt_s=B{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata_s=QIffQ{exbrightkextinterfacedebug_exbrightxtalkestimates_s=Q(?={?={exbrightkextinterfacedebug_exbrightalsschannelestimates_s=Q(?={?=[2f]}{?=[5f]})}})}}}8"
- "\"TB_ASSERT: \" \"(server->getindicatorstate != ((void*)0)) && \\\"implementation for getIndicatorState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
- "12111"
- "12111112122212121111111211111112111112212111111112"
- "EXBrightSILEnabled"
- "I64@?0{exbrightkextinterface_exbrightbundlealssamplemib__opt_s=B{exbrightkextinterface_exbrightbundlealssamplemib_s={exbrightkextinterface_exbrightluxsample__opt_s=B{exbrightkextinterface_exbrightluxsample_s=Qf}}{exbrightkextinterface_exbrightmibdata_s=QfBf}}}8"
- "I80@?0{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata__opt_s=B{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata_s=QIffQ{exbrightkextinterfacedebug_exbrightxtalkestimates_s=Q(?={?=[5f]})}}}8"
- "[%s] %s %s with value %d\n"
- "[%s] Fake streaming %sabled\n"
- "[%s] [ERR] Aggregated telemetry dictionary not initialized!\n"
- "[%s] [ERR] Failed to add telemetry data to dictionary for type %s\n"
- "[%s] [ERR] Failed to create iterator for telemetry dictionary\n"
- "[%s] [ERR] Failed to initialize OSDictionary with capacity %u\n"
- "[%s] [ERR] Failed to send event to CoreAnalytics for key %s\n"
- "[%s] [ERR] Failed to transform aggregated telemetry to OSDictionary for key %s\n"
- "[%s] [ERR] Failed to update telemetry data for type %s\n"
- "[%s] [ERR] Invalid telemetry data found in dictionary for key %s\n"
- "[%s] [INF] Telemetry dump - Total entries: %u\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "v64@?0{exbrightkextinterface_exbrightbundlealssamplemib__opt_s=B{exbrightkextinterface_exbrightbundlealssamplemib_s={exbrightkextinterface_exbrightluxsample__opt_s=B{exbrightkextinterface_exbrightluxsample_s=Qf}}{exbrightkextinterface_exbrightmibdata_s=QfBf}}}8"
- "v80@?0{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata__opt_s=B{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata_s=QIffQ{exbrightkextinterfacedebug_exbrightxtalkestimates_s=Q(?={?=[5f]})}}}8"

```
