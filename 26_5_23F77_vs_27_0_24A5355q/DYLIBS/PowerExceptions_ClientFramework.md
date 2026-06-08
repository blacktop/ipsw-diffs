## PowerExceptions_ClientFramework

> `/System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework`

```diff

-4.100.50.0.0
-  __TEXT.__text: 0xf094
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0xbc0
+145.0.0.0.0
+  __TEXT.__text: 0x10814
+  __TEXT.__objc_methlist: 0xd40
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x528
-  __TEXT.__cstring: 0x463
-  __TEXT.__oslogstring: 0x1576
-  __TEXT.__unwind_info: 0x5f8
-  __TEXT.__objc_classname: 0x145
-  __TEXT.__objc_methname: 0x21c8
-  __TEXT.__objc_methtype: 0xa7d
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x550
+  __TEXT.__gcc_except_tab: 0x5d0
+  __TEXT.__cstring: 0x471
+  __TEXT.__oslogstring: 0x16d5
+  __TEXT.__unwind_info: 0x6a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b0
+  __DATA_CONST.__objc_selrefs: 0x8a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0xed8
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__objc_const: 0xf58
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B544FBB-2F19-3A6B-82AF-61C2A8A12B4F
-  Functions: 372
-  Symbols:   1229
-  CStrings:  617
+  UUID: A4960DD9-C171-3789-AECC-5724AB45DE4B
+  Functions: 423
+  Symbols:   1363
+  CStrings:  205
 
Symbols:
+ -[ComputeSafeguardsManagingClient disableAudioRecognitionTrigger:]
+ -[ComputeSafeguardsManagingClient disableGameModeTrigger:]
+ -[ComputeSafeguardsManagingClient enableAudioRecognitionTrigger:]
+ -[ComputeSafeguardsManagingClient enableGameModeTrigger:]
+ -[ComputeSafeguardsManagingClient forceAudioRecognitionActive:]
+ -[ComputeSafeguardsManagingClient forceAudioRecognitionInactive:]
+ -[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:withIssueType:withRuleID:error:]
+ -[ComputeSafeguardsManagingClient forceGameModeActive:]
+ -[ComputeSafeguardsManagingClient forceGameModeDetection:]
+ -[ComputeSafeguardsManagingClient forceGameModeInactive:]
+ -[ComputeSafeguardsManagingClient forceHighTempActive:]
+ -[ComputeSafeguardsManagingClient forceSysdiagnoseStart:]
+ -[ComputeSafeguardsManagingClient forceSysdiagnoseStop:]
+ -[ComputeSafeguardsManagingClient getAudioRecognitionTriggerStatus:]
+ -[ComputeSafeguardsManagingClient getCombinedPenaltyBoxData:]
+ -[ComputeSafeguardsManagingClient getGameModeTriggerStatus:]
+ -[ComputeSafeguardsManagingClient getSysdiagnoseStatus:]
+ -[ComputeSafeguardsManagingClient setFlushTimeout:error:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table141
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table201
+ GCC_except_table66
+ GCC_except_table78
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table99
+ ___120-[ComputeSafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.69
+ ___39-[ComputeSafeguardsManagingClient init]_block_invoke.46
+ ___39-[ComputeSafeguardsManagingClient init]_block_invoke.46.cold.1
+ ___47-[ComputeSafeguardsManagingClient getDefaults:]_block_invoke.64
+ ___48-[ComputeSafeguardsManagingClient getScenarios:]_block_invoke.49
+ ___48-[PENotificationManager sendMitigationResponse:]_block_invoke.155
+ ___49-[PENotificationManager requestMitigationDetails]_block_invoke.150
+ ___50-[ComputeSafeguardsManagingClient getPenaltyList:]_block_invoke.66
+ ___51-[PEXPCService listener:shouldAcceptNewConnection:]_block_invoke.129
+ ___51-[PEXPCService queueMitigationNotification:forPID:]_block_invoke.147
+ ___51-[PEXPCService queueMitigationNotification:forPID:]_block_invoke.147.cold.1
+ ___52-[ComputeSafeguardsManagingClient getMonitoredList:]_block_invoke.65
+ ___52-[ComputeSafeguardsManagingClient getTargetProcess:]_block_invoke.61
+ ___53-[PENotificationManager registerProcessCapabilities:]_block_invoke.156
+ ___53-[PEXPCService getMitigationDetailsForPID:withReply:]_block_invoke.145
+ ___54-[ComputeSafeguardsManagingClient getActiveScenarios:]_block_invoke.47
+ ___54-[ComputeSafeguardsManagingClient getPollingInterval:]_block_invoke.56
+ ___54-[PENotificationManager unregisterProcessCapabilities]_block_invoke.160
+ ___55-[ComputeSafeguardsManagingClient forceGameModeActive:]_block_invoke
+ ___55-[ComputeSafeguardsManagingClient forceGameModeActive:]_block_invoke.107
+ ___55-[ComputeSafeguardsManagingClient forceGameModeActive:]_block_invoke.cold.1
+ ___55-[ComputeSafeguardsManagingClient forceHighTempActive:]_block_invoke
+ ___55-[ComputeSafeguardsManagingClient forceHighTempActive:]_block_invoke.101
+ ___55-[ComputeSafeguardsManagingClient forceHighTempActive:]_block_invoke.cold.1
+ ___55-[ComputeSafeguardsManagingClient getMitigationPolicy:]_block_invoke.50
+ ___56-[ComputeSafeguardsManagingClient enableThermalTrigger:]_block_invoke.98
+ ___56-[ComputeSafeguardsManagingClient forceSysdiagnoseStop:]_block_invoke
+ ___56-[ComputeSafeguardsManagingClient forceSysdiagnoseStop:]_block_invoke.114
+ ___56-[ComputeSafeguardsManagingClient forceSysdiagnoseStop:]_block_invoke.cold.1
+ ___56-[ComputeSafeguardsManagingClient getSysdiagnoseStatus:]_block_invoke
+ ___56-[ComputeSafeguardsManagingClient getSysdiagnoseStatus:]_block_invoke_2
+ ___56-[ComputeSafeguardsManagingClient getTriggerParameters:]_block_invoke.59
+ ___57-[ComputeSafeguardsManagingClient disableThermalTrigger:]_block_invoke.99
+ ___57-[ComputeSafeguardsManagingClient enableGameModeTrigger:]_block_invoke
+ ___57-[ComputeSafeguardsManagingClient enableGameModeTrigger:]_block_invoke.104
+ ___57-[ComputeSafeguardsManagingClient enableGameModeTrigger:]_block_invoke.cold.1
+ ___57-[ComputeSafeguardsManagingClient forceGameModeInactive:]_block_invoke
+ ___57-[ComputeSafeguardsManagingClient forceGameModeInactive:]_block_invoke.108
+ ___57-[ComputeSafeguardsManagingClient forceGameModeInactive:]_block_invoke.cold.1
+ ___57-[ComputeSafeguardsManagingClient forceSysdiagnoseStart:]_block_invoke
+ ___57-[ComputeSafeguardsManagingClient forceSysdiagnoseStart:]_block_invoke.113
+ ___57-[ComputeSafeguardsManagingClient forceSysdiagnoseStart:]_block_invoke.cold.1
+ ___57-[ComputeSafeguardsManagingClient forceThermalDetection:]_block_invoke.100
+ ___57-[ComputeSafeguardsManagingClient setFlushTimeout:error:]_block_invoke
+ ___57-[ComputeSafeguardsManagingClient setFlushTimeout:error:]_block_invoke.cold.1
+ ___58-[ComputeSafeguardsManagingClient disableGameModeTrigger:]_block_invoke
+ ___58-[ComputeSafeguardsManagingClient disableGameModeTrigger:]_block_invoke.105
+ ___58-[ComputeSafeguardsManagingClient disableGameModeTrigger:]_block_invoke.cold.1
+ ___58-[ComputeSafeguardsManagingClient forceGameModeDetection:]_block_invoke
+ ___58-[ComputeSafeguardsManagingClient forceGameModeDetection:]_block_invoke.106
+ ___58-[ComputeSafeguardsManagingClient forceGameModeDetection:]_block_invoke.cold.1
+ ___59-[ComputeSafeguardsManagingClient getInfoForProcess:error:]_block_invoke.62
+ ___59-[ComputeSafeguardsManagingClient isThermalTriggerEnabled:]_block_invoke.96
+ ___60-[ComputeSafeguardsManagingClient getGameModeTriggerStatus:]_block_invoke
+ ___60-[ComputeSafeguardsManagingClient getGameModeTriggerStatus:]_block_invoke_2
+ ___61-[ComputeSafeguardsManagingClient getCombinedPenaltyBoxData:]_block_invoke
+ ___61-[ComputeSafeguardsManagingClient getCombinedPenaltyBoxData:]_block_invoke.67
+ ___61-[ComputeSafeguardsManagingClient getCombinedPenaltyBoxData:]_block_invoke.cold.1
+ ___61-[ComputeSafeguardsManagingClient getThermalPollingInterval:]_block_invoke.94
+ ___61-[PEXPCService registerProcessCapabilities:forPID:withReply:]_block_invoke.141
+ ___62-[ComputeSafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke.57
+ ___62-[ComputeSafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.60
+ ___63-[ComputeSafeguardsManagingClient forceAudioRecognitionActive:]_block_invoke
+ ___63-[ComputeSafeguardsManagingClient forceAudioRecognitionActive:]_block_invoke.111
+ ___63-[ComputeSafeguardsManagingClient forceAudioRecognitionActive:]_block_invoke.cold.1
+ ___65-[ComputeSafeguardsManagingClient enableAudioRecognitionTrigger:]_block_invoke
+ ___65-[ComputeSafeguardsManagingClient enableAudioRecognitionTrigger:]_block_invoke.109
+ ___65-[ComputeSafeguardsManagingClient enableAudioRecognitionTrigger:]_block_invoke.cold.1
+ ___65-[ComputeSafeguardsManagingClient forceAudioRecognitionInactive:]_block_invoke
+ ___65-[ComputeSafeguardsManagingClient forceAudioRecognitionInactive:]_block_invoke.112
+ ___65-[ComputeSafeguardsManagingClient forceAudioRecognitionInactive:]_block_invoke.cold.1
+ ___65-[ComputeSafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke.58
+ ___66-[ComputeSafeguardsManagingClient disableAudioRecognitionTrigger:]_block_invoke
+ ___66-[ComputeSafeguardsManagingClient disableAudioRecognitionTrigger:]_block_invoke.110
+ ___66-[ComputeSafeguardsManagingClient disableAudioRecognitionTrigger:]_block_invoke.cold.1
+ ___68-[ComputeSafeguardsManagingClient getAudioRecognitionTriggerStatus:]_block_invoke
+ ___68-[ComputeSafeguardsManagingClient getAudioRecognitionTriggerStatus:]_block_invoke_2
+ ___69-[ComputeSafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke.72
+ ___69-[PENotificationManager createTemporaryConnectionAndHandleMitigation]_block_invoke.148
+ ___70-[ComputeSafeguardsManagingClient modifyThermalPollingInterval:error:]_block_invoke.97
+ ___78-[ComputeSafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke.52
+ ___83-[ComputeSafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke.54
+ ___99-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:withIssueType:withRuleID:error:]_block_invoke
+ ___99-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:withIssueType:withRuleID:error:]_block_invoke.83
+ ___99-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:withIssueType:withRuleID:error:]_block_invoke.83.cold.1
+ ___99-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:withIssueType:withRuleID:error:]_block_invoke.cold.1
+ ___block_literal_global.244
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$disableAudioRecognitionTriggerWithHandler:
+ _objc_msgSend$disableGameModeTriggerWithHandler:
+ _objc_msgSend$enableAudioRecognitionTriggerWithHandler:
+ _objc_msgSend$enableGameModeTriggerWithHandler:
+ _objc_msgSend$forceAudioRecognitionActiveWithHandler:
+ _objc_msgSend$forceAudioRecognitionInactiveWithHandler:
+ _objc_msgSend$forceDetectorViolationForProcess:withIssueType:withRuleID:withHandler:
+ _objc_msgSend$forceGameModeActiveWithHandler:
+ _objc_msgSend$forceGameModeDetectionWithHandler:
+ _objc_msgSend$forceGameModeInactiveWithHandler:
+ _objc_msgSend$forceHighTempActiveWithHandler:
+ _objc_msgSend$forceSysdiagnoseStartWithHandler:
+ _objc_msgSend$forceSysdiagnoseStopWithHandler:
+ _objc_msgSend$getAudioRecognitionTriggerStatusWithHandler:
+ _objc_msgSend$getCombinedPenaltyBoxDataWithHandler:
+ _objc_msgSend$getGameModeTriggerStatusWithHandler:
+ _objc_msgSend$getSysdiagnoseStatusWithHandler:
+ _objc_msgSend$modifyFlushTimeout:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- -[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:error:]
- -[ComputeSafeguardsManagingClient getThermalTemperature:]
- -[ComputeSafeguardsManagingClient getThermalTemperature:].cold.1
- -[ComputeSafeguardsManagingClient getThermalTemperature:].cold.2
- GCC_except_table100
- GCC_except_table103
- GCC_except_table106
- GCC_except_table109
- GCC_except_table112
- GCC_except_table115
- GCC_except_table118
- GCC_except_table121
- GCC_except_table124
- GCC_except_table127
- GCC_except_table130
- GCC_except_table133
- GCC_except_table136
- GCC_except_table139
- GCC_except_table142
- GCC_except_table145
- GCC_except_table148
- GCC_except_table151
- GCC_except_table154
- GCC_except_table169
- GCC_except_table173
- GCC_except_table69
- GCC_except_table77
- GCC_except_table79
- GCC_except_table81
- GCC_except_table83
- GCC_except_table85
- GCC_except_table87
- GCC_except_table89
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- ___120-[ComputeSafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.68
- ___39-[ComputeSafeguardsManagingClient init]_block_invoke.47
- ___39-[ComputeSafeguardsManagingClient init]_block_invoke.47.cold.1
- ___47-[ComputeSafeguardsManagingClient getDefaults:]_block_invoke.65
- ___48-[ComputeSafeguardsManagingClient getScenarios:]_block_invoke.50
- ___48-[PENotificationManager sendMitigationResponse:]_block_invoke.156
- ___49-[PENotificationManager requestMitigationDetails]_block_invoke.151
- ___50-[ComputeSafeguardsManagingClient getPenaltyList:]_block_invoke.67
- ___51-[PEXPCService listener:shouldAcceptNewConnection:]_block_invoke.130
- ___51-[PEXPCService queueMitigationNotification:forPID:]_block_invoke.148
- ___51-[PEXPCService queueMitigationNotification:forPID:]_block_invoke.148.cold.1
- ___52-[ComputeSafeguardsManagingClient getMonitoredList:]_block_invoke.66
- ___52-[ComputeSafeguardsManagingClient getTargetProcess:]_block_invoke.62
- ___53-[PENotificationManager registerProcessCapabilities:]_block_invoke.157
- ___53-[PEXPCService getMitigationDetailsForPID:withReply:]_block_invoke.147
- ___54-[ComputeSafeguardsManagingClient getActiveScenarios:]_block_invoke.48
- ___54-[ComputeSafeguardsManagingClient getPollingInterval:]_block_invoke.57
- ___54-[PENotificationManager unregisterProcessCapabilities]_block_invoke.161
- ___55-[ComputeSafeguardsManagingClient getMitigationPolicy:]_block_invoke.51
- ___56-[ComputeSafeguardsManagingClient enableThermalTrigger:]_block_invoke.99
- ___56-[ComputeSafeguardsManagingClient getTriggerParameters:]_block_invoke.60
- ___57-[ComputeSafeguardsManagingClient disableThermalTrigger:]_block_invoke.100
- ___57-[ComputeSafeguardsManagingClient forceThermalDetection:]_block_invoke.101
- ___57-[ComputeSafeguardsManagingClient getThermalTemperature:]_block_invoke
- ___57-[ComputeSafeguardsManagingClient getThermalTemperature:]_block_invoke.94
- ___57-[ComputeSafeguardsManagingClient getThermalTemperature:]_block_invoke.cold.1
- ___59-[ComputeSafeguardsManagingClient getInfoForProcess:error:]_block_invoke.63
- ___59-[ComputeSafeguardsManagingClient isThermalTriggerEnabled:]_block_invoke.97
- ___61-[ComputeSafeguardsManagingClient getThermalPollingInterval:]_block_invoke.96
- ___61-[PEXPCService registerProcessCapabilities:forPID:withReply:]_block_invoke.142
- ___62-[ComputeSafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke.58
- ___62-[ComputeSafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.61
- ___65-[ComputeSafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke.59
- ___69-[ComputeSafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke.71
- ___69-[PENotificationManager createTemporaryConnectionAndHandleMitigation]_block_invoke.149
- ___70-[ComputeSafeguardsManagingClient modifyThermalPollingInterval:error:]_block_invoke.98
- ___74-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke
- ___74-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.83
- ___74-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.83.cold.1
- ___74-[ComputeSafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.cold.1
- ___78-[ComputeSafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke.53
- ___83-[ComputeSafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke.55
- ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSNumber"8"NSError"16ls32l8r40l8r48l8
- ___block_literal_global.217
- _objc_msgSend$code
- _objc_msgSend$domain
- _objc_msgSend$forceDetectorViolationForProcess:withHandler:
- _objc_msgSend$getThermalTemperatureWithHandler:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "Failed to disable audio recognition trigger %@"
+ "Failed to disable game mode trigger %@"
+ "Failed to enable audio recognition trigger %@"
+ "Failed to enable game mode trigger %@"
+ "Failed to force audio recognition active %@"
+ "Failed to force audio recognition inactive %@"
+ "Failed to force detector violation with issue type and rule ID %@"
+ "Failed to force game mode active %@"
+ "Failed to force game mode detection %@"
+ "Failed to force game mode inactive %@"
+ "Failed to force sysdiagnose start %@"
+ "Failed to force sysdiagnose stop %@"
+ "Failed to get combined penalty box data %@"
+ "Failed to set flush timeout %@"
+ "XPC call succeeded, received audio recognition status: %@"
+ "XPC call succeeded, received game mode status: %@"
+ "XPC call succeeded, received sysdiagnose status: %@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PENotificationManagerDelegate>\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"PEMitigationNotification\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@56@0:8Q16d24@32@40@48"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24@32^@40"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8@16@24^B32^d40^@48"
- "B64@0:8@16@24@32@40@48^@56"
- "B72@0:8@16@24@32@40@48@56^@64"
- "B96@0:8@16@24@32@40@48@56@64@72@80^@88"
- "Calling getThermalTemperatureWithHandler via XPC..."
- "ComputeSafeguardsClient"
- "ComputeSafeguardsManagingClient"
- "ComputeSafeguardsScheduledWorkReporting"
- "ComputeSafeguardsViolationReporting"
- "Failed to force detector violation %@"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "PEMitigationNotification"
- "PENotificationManager"
- "PEProcessRegistration"
- "PEXPCConnectionInfo"
- "PEXPCServiceProtocol"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<PENotificationManagerDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",&,N,V_registeredWarningTypes"
- "T@\"NSArray\",&,N,V_warningTypes"
- "T@\"NSDate\",&,N,V_connectionTime"
- "T@\"NSDate\",&,N,V_registrationTime"
- "T@\"NSDictionary\",R,C,N,V_processInfo"
- "T@\"NSMutableArray\",&,N,V_activeConnections"
- "T@\"NSMutableDictionary\",&,N,V_registeredProcesses"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_registryQueue"
- "T@\"NSObject<OS_os_log>\",&,N,V_logger"
- "T@\"NSObject<OS_os_log>\",&,V_logger"
- "T@\"NSString\",&,N,V_currentNotificationID"
- "T@\"NSString\",&,N,V_pendingNotificationID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_notificationID"
- "T@\"NSString\",R,C,N,V_reason"
- "T@\"NSTimer\",&,N,V_cleanupTimer"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCConnection\",&,N,V_temporaryConnection"
- "T@\"NSXPCConnection\",W,N,V_connection"
- "T@\"NSXPCListener\",&,N,V_listener"
- "T@\"PEMitigationNotification\",&,N,V_pendingNotification"
- "TB,N,V_registered"
- "TB,R"
- "TB,R,N"
- "TB,V_featureEnabled"
- "TB,V_interrupted"
- "TQ,R"
- "TQ,R,N,V_warningType"
- "Td,R,N,V_gracePeriod"
- "Ti,N,V_notifyToken"
- "Ti,N,V_pid"
- "Ti,N,V_processPID"
- "UTF8String"
- "Vv16@0:8"
- "XPC call failed for getThermalTemperature - domain: %@, code: %ld, description: %@"
- "^{_NSZone=}16@0:8"
- "_activeConnections"
- "_cleanupTimer"
- "_connection"
- "_connectionTime"
- "_currentNotificationID"
- "_delegate"
- "_featureEnabled"
- "_gracePeriod"
- "_interrupted"
- "_listener"
- "_logger"
- "_notificationID"
- "_notifyToken"
- "_pendingNotification"
- "_pendingNotificationID"
- "_pid"
- "_processInfo"
- "_processPID"
- "_reason"
- "_registered"
- "_registeredProcesses"
- "_registeredWarningTypes"
- "_registrationTime"
- "_registryQueue"
- "_temporaryConnection"
- "_warningType"
- "_warningTypes"
- "_xpcConnection"
- "activeConnections"
- "addObject:"
- "array"
- "autorelease"
- "class"
- "cleanupTemporaryConnection"
- "cleanupTimer"
- "clearMitigationRecordsWithError:"
- "clearMitigationRecordsWithHandler:"
- "clearTargetProcess"
- "clearTargetProcessWithError:"
- "code"
- "conformsToProtocol:"
- "connection"
- "connectionTime"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createTemporaryConnectionAndHandleMitigation"
- "currentNotificationID"
- "d"
- "d16@0:8"
- "date"
- "dealloc"
- "debugDescription"
- "decodeDoubleForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "disableThermalTrigger:"
- "disableThermalTriggerWithHandler:"
- "domain"
- "enableThermalTrigger:"
- "enableThermalTriggerWithHandler:"
- "encodeDouble:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "featureEnabled"
- "forceCPUViolationForProcess:error:"
- "forceCPUViolationForProcess:withHandler:"
- "forceDetectionWithFirstEndDate:lastEndDate:error:"
- "forceDetectionWithFirstEndDate:lastEndDate:withHandler:"
- "forceDetectorViolationForProcess:error:"
- "forceDetectorViolationForProcess:withHandler:"
- "forceMidnightRoutine:"
- "forceMidnightRoutineWithHandler:"
- "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:"
- "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:"
- "forceThermalDetection:"
- "forceThermalDetectionWithHandler:"
- "getActiveScenarios:"
- "getActiveScenariosWithHandler:"
- "getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:"
- "getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:"
- "getDefaults:"
- "getDefaultsWithHandler:"
- "getInfoForProcess:error:"
- "getInfoForProcess:withHandler:"
- "getMaxRelaunchPollingInterval:"
- "getMaxRelaunchPollingIntervalWithHandler:"
- "getMitigationDetailsForPID:withReply:"
- "getMitigationPolicy:"
- "getMitigationPolicyWithHandler:"
- "getMonitoredList:"
- "getMonitoredListWithHandler:"
- "getPenaltyList:"
- "getPenaltyListWithHandler:"
- "getPollingInterval:"
- "getPollingIntervalWithHandler:"
- "getProcessesAffectedByScenarioMapWithError:"
- "getProcessesAffectedByScenarioMapWithHandler:"
- "getRelaunchPollingInterval:"
- "getRelaunchPollingIntervalWithHandler:"
- "getRestrictionsForProcess:forScenario:withError:"
- "getRestrictionsForProcess:forScenario:withHandler:"
- "getScenarioRefreshInterval:"
- "getScenarioRefreshIntervalWithHandler:"
- "getScenarios:"
- "getScenariosWithHandler:"
- "getTargetProcess:"
- "getTargetProcessMitigationRecords:"
- "getTargetProcessMitigationRecordsWithHandler:"
- "getTargetProcessWithHandler:"
- "getThermalPollingInterval:"
- "getThermalPollingIntervalWithHandler:"
- "getThermalSamplingInterval:"
- "getThermalSamplingIntervalWithHandler:"
- "getThermalTemperature XPC call succeeded, received temperature: %@"
- "getThermalTemperature called - featureEnabled: %d, connection: %@"
- "getThermalTemperature:"
- "getThermalTemperature: Feature not enabled"
- "getThermalTemperature: XPC connection is nil!"
- "getThermalTemperatureWithHandler:"
- "getThermalTriggerStatus:"
- "getThermalTriggerStatusWithHandler:"
- "getTriggerParameters:"
- "getTriggerParametersWithHandler:"
- "handleConnectionTermination:"
- "handleMitigationDetails:"
- "handleMitigationNotification"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithWarningType:gracePeriod:notificationID:reason:processInfo:"
- "interfaceWithProtocol:"
- "interrupted"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProcessRegistered:"
- "isProxy"
- "isRegistered"
- "isThermalTriggerEnabled:"
- "isThermalTriggerEnabledWithHandler:"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "localizedDescription"
- "logger"
- "modifyContextForIdentifier:withState:"
- "modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:"
- "modifyMaxRelaunchPollingInterval:"
- "modifyPollingInterval:"
- "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:"
- "modifyRelaunchPollingInterval:"
- "modifyRestrictionsByProcessPerScenario:withHandler:"
- "modifyScenarioRefreshInterval:"
- "modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:"
- "modifyTargetProcessMitigationRecords:withHandler:"
- "modifyThermalPollingInterval:error:"
- "modifyThermalPollingInterval:withHandler:"
- "modifyThermalSamplingInterval:error:"
- "modifyThermalSamplingInterval:withHandler:"
- "modifyTriggerWithInterval:withLookback:withThreshold:"
- "notifyToken"
- "numberWithInt:"
- "objectForKeyedSubscript:"
- "pendingNotification"
- "pendingNotificationID"
- "performMaintenanceCleanup"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "powerExceptionsWillMitigate:completionHandler:"
- "processIdentifier"
- "processPID"
- "queueMitigationNotification:forPID:"
- "registerForNotifications:error:"
- "registerProcessCapabilities:"
- "registerProcessCapabilities:forPID:withReply:"
- "registered"
- "registeredProcesses"
- "registeredWarningTypes"
- "registrationTime"
- "registryQueue"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeObject:"
- "removeObjectForKey:"
- "reportExcessiveCPUUseBy:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:"
- "reportExcessiveCPUUseBy:pid:path:timestamp:observed_cpu_nsecs:observation_nsecs:cpu_nsecs_allowed:limit_window_nsecs:flags:"
- "reportScheduledIntensiveWorkByProcesses:"
- "requestMitigationDetails"
- "resetRuleParameters:error:"
- "resetRuleParameters:withHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "self"
- "sendCoalitionEntries:error:"
- "sendMitigationResponse:"
- "sendMitigationResponse:forNotificationID:"
- "setActiveConnections:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCleanupTimer:"
- "setConnection:"
- "setConnectionTime:"
- "setContextForIdentifier:withState:error:"
- "setCurrentNotificationID:"
- "setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFeatureEnabled:"
- "setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:"
- "setInterrupted:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setListener:"
- "setLogger:"
- "setMaxRelaunchPollingInterval:error:"
- "setNotifyToken:"
- "setObject:forKeyedSubscript:"
- "setPendingNotification:"
- "setPendingNotificationID:"
- "setPid:"
- "setPollingInterval:error:"
- "setProcessPID:"
- "setRegistered:"
- "setRegisteredProcesses:"
- "setRegisteredWarningTypes:"
- "setRegistrationTime:"
- "setRegistryQueue:"
- "setRelaunchPollingInterval:error:"
- "setRemoteObjectInterface:"
- "setRestrictionsByProcessPerScenario:error:"
- "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:"
- "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:"
- "setScenarioRefreshInterval:error:"
- "setTargetProcessMitigationRecords:withError:"
- "setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:"
- "setTemporaryConnection:"
- "setTriggerWithInterval:withLookback:withThreshold:error:"
- "setWarningTypes:"
- "setWithObjects:"
- "sharedManager"
- "sharedService"
- "startListener"
- "stringWithCString:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "temporaryConnection"
- "timeIntervalSinceDate:"
- "unregisterFromNotifications"
- "unregisterProcessCapabilities"
- "unregisterProcessForPID:"
- "unsignedIntegerValue"
- "updateCoalitionEntries:withHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSNumber\">16"
- "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSSet\">16"
- "v24@0:8Q16"
- "v28@0:8@16i24"
- "v28@0:8i16@?20"
- "v28@0:8i16@?<v@?@\"PEMitigationNotification\"@\"NSError\">20"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSNumber\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@\"NSString\"24"
- "v32@0:8Q16@24"
- "v36@0:8@\"NSArray\"16i24@?<v@?B@\"NSError\">28"
- "v36@0:8@16i24@?28"
- "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?Bd@\"NSError\">32"
- "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32"
- "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40"
- "v48@0:8@16@24@32@40"
- "v64@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v72@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@?<v@?@\"NSError\">64"
- "v72@0:8@16@24@32@40@48@56@?64"
- "v84@0:8@\"NSString\"16Q24@\"NSString\"32{mach_timespec=Ii}40q48q56q64q72B80"
- "v84@0:8@16Q24@32{mach_timespec=Ii}40q48q56q64q72B80"
- "v84@0:8[33c]16i24[1024c]28{mach_timespec=Ii}36q44q52q60q68Q76"
- "v96@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80@?<v@?@\"NSError\">88"
- "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
- "warningTypes"
- "zone"

```
