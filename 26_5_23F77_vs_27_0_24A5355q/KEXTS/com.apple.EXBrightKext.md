## com.apple.EXBrightKext

> `com.apple.EXBrightKext`

```diff

-2079.120.10.0.0
+2285.0.0.502.1
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x4180
-  __TEXT_EXEC.__text: 0x13a98
+  __TEXT.__cstring: 0x47c9
+  __TEXT_EXEC.__text: 0x16594
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x130
   __DATA.__bss: 0x2
-  __DATA_CONST.__auth_got: 0x340
-  __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x1e00
+  __DATA_CONST.__const: 0x1f60
   __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: F42C8E30-A477-3D5A-9ABD-586C67AF6651
-  Functions: 519
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x90
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
