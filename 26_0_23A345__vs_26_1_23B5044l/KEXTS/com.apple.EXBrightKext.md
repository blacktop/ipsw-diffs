## com.apple.EXBrightKext

> `com.apple.EXBrightKext`

```diff

-2079.2.2.0.0
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x2eda
-  __TEXT_EXEC.__text: 0xf42c
+2079.40.16.0.0
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x3e5f
+  __TEXT_EXEC.__text: 0x13b6c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
-  __DATA.__common: 0x90
+  __DATA.__common: 0x108
   __DATA.__bss: 0x2
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__mod_init_func: 0x18
-  __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1840
-  __DATA_CONST.__kalloc_type: 0xc0
-  UUID: B0DF04B1-E8F6-3A9A-801C-9BAABC530370
-  Functions: 368
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__mod_init_func: 0x28
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x1d58
+  __DATA_CONST.__kalloc_type: 0x180
+  UUID: DBAB7F84-7E1B-33E9-B31C-06CBA69134DF
+  Functions: 465
   Symbols:   0
-  CStrings:  180
+  CStrings:  266
 
CStrings:
+ "\"TB_ASSERT: \" \"(server->fetchtelemetryhealthdata != ((void*)0)) && \\\"implementation for fetchTelemetryHealthData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->getindicatorstate != ((void*)0)) && \\\"implementation for getIndicatorState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "\"TB_ASSERT: \" \"(server->sethealththresholdtohwmonitor != ((void*)0)) && \\\"implementation for setHealthThresholdToHWMonitor is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d"
+ "12"
+ "12111"
+ "12111112122212121111111211111112111112212111111112"
+ "122222"
+ "CoreAnalyticsHub"
+ "EXBrightKextInterface_c.c"
+ "EXBrightSILEnabledTrusted"
+ "HealthCounters"
+ "I12@?0I8"
+ "I48@?0{exbrightkextinterface_exbrighttelemetryhealthdata__opt_s=B{exbrightkextinterface_exbrighttelemetryhealthdata_s={exbrightkextinterface_exbrighttelemetryhealthcounters_s=I[4I][4I]}}}8"
+ "TelemetryData"
+ "TelemetryManager"
+ "Unknown"
+ "[%s] TelemetryManager ready to send events!\n"
+ "[%s] [DEB] Dumping aggregated telemetry...\n"
+ "[%s] [ERR] Aggregated telemetry dictionary not initialized!\n"
+ "[%s] [ERR] Could not add timer for submitting telemetry to the workloop, res: %d\n"
+ "[%s] [ERR] Could not create TelemetryManager\n"
+ "[%s] [ERR] Could not create timer for submitting telemetry\n"
+ "[%s] [ERR] Empty telemetry array, nothing to update\n"
+ "[%s] [ERR] Failed to add telemetry data to dictionary for type %s\n"
+ "[%s] [ERR] Failed to alloc HealthCounters\n"
+ "[%s] [ERR] Failed to alloc TelemetryManager!\n"
+ "[%s] [ERR] Failed to allocate telemetry IOLock\n"
+ "[%s] [ERR] Failed to cast CoreAnalyticsHub\n"
+ "[%s] [ERR] Failed to cast TelemetryData to HealthCounters\n"
+ "[%s] [ERR] Failed to create OSString eventName %s\n"
+ "[%s] [ERR] Failed to create iterator for telemetry dictionary\n"
+ "[%s] [ERR] Failed to create iterator for telemetry dump\n"
+ "[%s] [ERR] Failed to get indicator state\n"
+ "[%s] [ERR] Failed to initalize HealthCounters\n"
+ "[%s] [ERR] Failed to initialize OSDictionary with capacity %u\n"
+ "[%s] [ERR] Failed to initialize TelemetryManager\n"
+ "[%s] [ERR] Failed to send event to CoreAnalytics for key %s\n"
+ "[%s] [ERR] Failed to send event to CoreAnalytics for type %s\n"
+ "[%s] [ERR] Failed to send event!\n"
+ "[%s] [ERR] Failed to set CoreAnalytics service\n"
+ "[%s] [ERR] Failed to setup TelemetryManager!\n"
+ "[%s] [ERR] Failed to transform aggregated telemetry to OSDictionary for key %s\n"
+ "[%s] [ERR] Failed to transform aggregated telemetry to OSDictionary for type %s\n"
+ "[%s] [ERR] Failed to update telemetry data for type %s\n"
+ "[%s] [ERR] Invalid eventName!\n"
+ "[%s] [ERR] Invalid eventPayload!\n"
+ "[%s] [ERR] Invalid telemetry data for key: %s\n"
+ "[%s] [ERR] Invalid telemetry data found in dictionary for key %s\n"
+ "[%s] [ERR] No CoreAnalytics Service set, cannot send events!\n"
+ "[%s] [ERR] No telemetry data found for type %s\n"
+ "[%s] [ERR] No telemetry to dump!\n"
+ "[%s] [INF] \t=== Brightness Failures ===\n"
+ "[%s] [INF] \t=== Contrast Failures ===\n"
+ "[%s] [INF] \tRampDown State = %u%% (%u)\n"
+ "[%s] [INF] \tRampUp State = %u%% (%u)\n"
+ "[%s] [INF] \tSession Start = %u%% (%u)\n"
+ "[%s] [INF] \tSteady State = %u%% (%u)\n"
+ "[%s] [INF] \tTotal = %u%% (%u)\n"
+ "[%s] [INF] == HealthCounters Summary ==\n"
+ "[%s] [INF] Telemetry dump - Total entries: %u\n"
+ "[%s] [INF] Total Frames Checked = %u\n"
+ "com.apple.EXBright.HealthCounters"
+ "coreAnalyticsMatchNotificationHandler"
+ "percentBrightnessFailures"
+ "percentBrightnessFailuresRampDown"
+ "percentBrightnessFailuresRampUp"
+ "percentBrightnessFailuresSessionStart"
+ "percentBrightnessFailuresSteady"
+ "percentContrastFailures"
+ "percentContrastFailuresRampDown"
+ "percentContrastFailuresRampUp"
+ "percentContrastFailuresSessionStart"
+ "percentContrastFailuresSteady"
+ "site.HealthCounters"
+ "site.TelemetryData"
+ "site.TelemetryManager"
+ "totalBrightnessFailures"
+ "totalBrightnessFailuresRampDown"
+ "totalBrightnessFailuresRampUp"
+ "totalBrightnessFailuresSessionStart"
+ "totalBrightnessFailuresSteady"
+ "totalCheckedFrames"
+ "totalContrastFailures"
+ "totalContrastFailuresRampDown"
+ "totalContrastFailuresRampUp"
+ "totalContrastFailuresSessionStart"
+ "totalContrastFailuresSteady"
+ "v12@?0I8"
+ "v48@?0{exbrightkextinterface_exbrighttelemetryhealthdata__opt_s=B{exbrightkextinterface_exbrighttelemetryhealthdata_s={exbrightkextinterface_exbrighttelemetryhealthcounters_s=I[4I][4I]}}}8"
- "12111112122212121111111211111112112212111111112"
- "EXBrightKextInterfaceDebug_C.c"
- "EXBrightKextInterface_C.c"

```
