## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-3486.60.36.0.0
-  __TEXT.__text: 0x4eb760
-  __TEXT.__objc_methlist: 0x2f954
-  __TEXT.__const: 0x2cf0
+3486.60.47.0.0
+  __TEXT.__text: 0x4eddb0
+  __TEXT.__objc_methlist: 0x2f9d4
+  __TEXT.__const: 0x2d00
   __TEXT.__swift5_typeref: 0x710
   __TEXT.__constg_swiftt: 0x544
   __TEXT.__swift5_reflstr: 0x4de

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x60e8c
+  __TEXT.__cstring: 0x61217
   __TEXT.__swift5_capture: 0x73c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__oslogstring: 0x172dd
+  __TEXT.__oslogstring: 0x1734e
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x2db0
+  __TEXT.__gcc_except_tab: 0x2dc8
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0xb448
+  __TEXT.__unwind_info: 0xb490
   __TEXT.__eh_frame: 0x16f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9748
+  __DATA_CONST.__const: 0x97b0
   __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_nlclslist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f18
+  __DATA_CONST.__objc_selrefs: 0x14f88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb50
-  __DATA_CONST.__objc_arraydata: 0x16e00
+  __DATA_CONST.__objc_arraydata: 0x16e20
   __DATA_CONST.__got: 0x1b88
-  __AUTH_CONST.__const: 0x2ab8
-  __AUTH_CONST.__cfstring: 0x78920
-  __AUTH_CONST.__objc_const: 0x38d90
+  __AUTH_CONST.__const: 0x2ad8
+  __AUTH_CONST.__cfstring: 0x78fa0
+  __AUTH_CONST.__objc_const: 0x38dc0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x6ea0
   __AUTH_CONST.__objc_arrayobj: 0x3198
-  __AUTH_CONST.__objc_dictobj: 0x5140
+  __AUTH_CONST.__objc_dictobj: 0x5168
   __AUTH_CONST.__objc_doubleobj: 0x1330
   __AUTH_CONST.__auth_got: 0x1960
   __AUTH.__objc_data: 0x2c10

   __DATA.__objc_ivar: 0x1fac
   __DATA.__data: 0x10f8
   __DATA.__common: 0x1f8
-  __DATA_DIRTY.__objc_ivar: 0x13a8
+  __DATA_DIRTY.__objc_ivar: 0x13ac
   __DATA_DIRTY.__objc_data: 0x3f58
   __DATA_DIRTY.__data: 0x728
-  __DATA_DIRTY.__bss: 0x4798
+  __DATA_DIRTY.__bss: 0x47a8
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19930
-  Symbols:   25936
-  CStrings:  19994
+  Functions: 19950
+  Symbols:   25968
+  CStrings:  20048
 
Symbols:
+ +[PLDisplayAgent entryEventForwardDefinitionDisplayALS]
+ +[PLDisplayAgent entryEventForwardDefinitionDisplayXALS]
+ +[PPSFileUtilities(APFS) markFileDescriptorAsPurgeable:urgency:startDate:]
+ -[PLBatteryAgent parsedAlertKeysFromLowBatteryLogString:]
+ -[PLBatteryAgent parsedCPMSKeysFromLowBatteryLogString:]
+ -[PLDisplayAgent displayALSEntryFromTelemetry:isDisplayX:]
+ -[PLDisplayAgent logEventForwardDisplayALSWithDate:isDisplayX:]
+ -[PLDisplayAgent logEventForwardDisplayALSWithOcclusionTrigger:]
+ -[PLXPCAgent handleHingeUsageNotificationWithPayload:]
+ -[PLXPCAgent hingeUsageXPCListener]
+ -[PLXPCAgent logHingeUsageToCA:]
+ -[PLXPCAgent setHingeUsageXPCListener:]
+ GCC_except_table172
+ GCC_except_table190
+ GCC_except_table202
+ GCC_except_table264
+ GCC_except_table273
+ GCC_except_table281
+ GCC_except_table287
+ GCC_except_table289
+ GCC_except_table293
+ GCC_except_table301
+ GCC_except_table336
+ GCC_except_table340
+ GCC_except_table344
+ GCC_except_table437
+ _PLBatteryAgentIntegerFromLowBatteryLogValue
+ _PLBatteryAgentRealFromLowBatteryLogValue
+ _PLBatteryAgentSecondsFromLowBatteryLogDuration
+ _PLBatteryAgentSplitPerDisplayValue
+ ___32-[PLXPCAgent logHingeUsageToCA:]_block_invoke
+ ___56-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLogString:]_block_invoke
+ ___56-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLogString:]_block_invoke_2
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_3
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke_3
+ ___PLBatteryAgentSplitPerDisplayValue_block_invoke
+ _kPLBatteryAgentStringAwakeTime
+ _kPLBatteryAgentStringCapacity
+ _kPLBatteryAgentStringForegroundApplications
+ _kPLBatteryAgentStringForegroundApplicationsX
+ _kPLBatteryAgentStringHingeState
+ _kPLBatteryAgentStringPartialCharge
+ _kPLBatteryAgentStringPowerAssertions
+ _kPLBatteryAgentStringScreenBrightness
+ _kPLBatteryAgentStringScreenBrightnessX
+ _kPLBatteryAgentStringStandbyTime
+ _kPLBatteryAgentStringVoltageMV
+ _kPLDisplayAgentEventForwardNameDisplayALS
+ _kPLDisplayAgentEventForwardNameDisplayXALS
- -[PLBatteryAgent parsedCPMSKeysFromLowBatteryLog]
- GCC_except_table170
- GCC_except_table188
- GCC_except_table200
- GCC_except_table261
- GCC_except_table270
- GCC_except_table276
- GCC_except_table277
- GCC_except_table283
- GCC_except_table284
- GCC_except_table298
- GCC_except_table331
- GCC_except_table334
- GCC_except_table338
- GCC_except_table433
- ___49-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLog]_block_invoke
- ___49-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLog]_block_invoke_2
CStrings:
+ ": "
+ "Awake Time"
+ "AwakeTime"
+ "CBDisplayTelemetrySnapshot"
+ "CBOcclusionTelemetrySample"
+ "CBOcclusionTelemetryTrigger"
+ "Capacity"
+ "CoreMotion"
+ "CoreMotion::HingeUsage"
+ "DisplayX_ALS"
+ "Display_ALS"
+ "Failed to mark fd %d as purgeable with label: '%@' (error %d = '%s')"
+ "Foreground Applications"
+ "ForegroundApplications"
+ "ForegroundApplicationsX"
+ "Hinge State"
+ "HingeMetricsStartTime"
+ "HingeState"
+ "HingeUsage"
+ "HingeUsage payload: %@"
+ "HingeUsage: logging data to CA: %@"
+ "HingeUsage: logging entry: %@"
+ "HingeUsage: received nil payload"
+ "Marked fd %d as purgeable with label: '%@'"
+ "Partial Charge"
+ "PartialCharge"
+ "Power Assertions"
+ "PowerAssertions"
+ "Screen Brightness"
+ "ScreenBrightness"
+ "ScreenBrightnessX"
+ "Standby Time"
+ "StandbyTime"
+ "TotalCloses"
+ "TotalOpens"
+ "VoltageMV"
+ "\\.inner:\\s*(\\{[^}]*\\}|[^,}]+?)\\s*,\\s*\\.cover:\\s*(\\{[^}]*\\}|[^,}]+?)\\s*\\}"
+ "colorALSMask"
+ "colorX_1"
+ "colorX_14"
+ "colorY_1"
+ "colorY_14"
+ "colorZ_1"
+ "colorZ_14"
+ "com.apple.power.hingeUsage"
+ "embeddingTableResidentRatio"
+ "expertsLoadedDuringPromptCount"
+ "expertsLoadedFromCacheDuringPromptCount"
+ "expertsNeedingNANDLoadDuringPromptCount"
+ "expertsSwappedDuringPromptCount"
+ "harmonyStrength"
+ "lux_1"
+ "lux_11"
+ "lux_14"
+ "totalExpertsLoadedCount"
+ "triggerTime"
+ "triggers"
+ "trustedALS"
- "Checking %@ with flags %u"
- "Could not get eachFlags"
- "Could not get flags"
- "Skip %@ with flags %u - not a full AP wake reason"
```
