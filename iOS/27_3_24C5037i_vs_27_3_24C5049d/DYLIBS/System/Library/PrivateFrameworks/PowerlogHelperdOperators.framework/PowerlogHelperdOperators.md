## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-3486.60.36.0.0
-  __TEXT.__text: 0x1e6df4
-  __TEXT.__objc_methlist: 0x11568
-  __TEXT.__const: 0x720
-  __TEXT.__cstring: 0x26f68
-  __TEXT.__oslogstring: 0x16688
-  __TEXT.__gcc_except_tab: 0x25a4
+3486.60.47.0.0
+  __TEXT.__text: 0x1ea794
+  __TEXT.__objc_methlist: 0x11648
+  __TEXT.__const: 0x730
+  __TEXT.__cstring: 0x27336
+  __TEXT.__oslogstring: 0x16bd2
+  __TEXT.__gcc_except_tab: 0x25bc
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x6120
+  __TEXT.__unwind_info: 0x6200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x45c8
+  __DATA_CONST.__const: 0x4630
   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb3e0
+  __DATA_CONST.__objc_selrefs: 0xb498
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e0
-  __DATA_CONST.__objc_arraydata: 0x165c0
+  __DATA_CONST.__objc_arraydata: 0x165e0
   __DATA_CONST.__got: 0xf98
-  __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0x346c0
-  __AUTH_CONST.__objc_const: 0x16f90
+  __AUTH_CONST.__const: 0x1b40
+  __AUTH_CONST.__cfstring: 0x34d80
+  __AUTH_CONST.__objc_const: 0x16fc0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x29d0
-  __AUTH_CONST.__objc_dictobj: 0x3bd8
+  __AUTH_CONST.__objc_dictobj: 0x3c00
   __AUTH_CONST.__objc_doubleobj: 0xc10
   __AUTH_CONST.__objc_arrayobj: 0x30c0
-  __AUTH_CONST.__auth_got: 0xe10
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH.__objc_data: 0xca8
-  __DATA.__objc_ivar: 0x1724
+  __DATA.__objc_ivar: 0x1728
   __DATA.__data: 0x580
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1888

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8925
-  Symbols:   12081
-  CStrings:  9187
+  Functions: 8984
+  Symbols:   12138
+  CStrings:  9264
 
Symbols:
+ +[PLDisplayAgent entryEventForwardDefinitionDisplayALS]
+ +[PLDisplayAgent entryEventForwardDefinitionDisplayXALS]
+ +[PLUtilities isPlistSafeObject:]
+ +[PLUtilities isPlistSafeObject:atDepth:]
+ +[PLUtilities isValidBatteryUIRequestingService:]
+ +[PLUtilities privilegedCopyFileNamed:fromDirectoryFd:toDirectoryFd:]
+ +[PLUtilities privilegedCopyItemsFromPath:toDirectory:]
+ +[PLUtilities stringContainsControlCharacters:]
+ +[PPSFileUtilities(APFS) markFileDescriptorAsPurgeable:urgency:startDate:]
+ -[PLBatteryAgent parsedAlertKeysFromLowBatteryLogString:]
+ -[PLBatteryAgent parsedCPMSKeysFromLowBatteryLogString:]
+ -[PLBatteryUIResponderService plistSafeResultDictionary]
+ -[PLDisplayAgent displayALSEntryFromTelemetry:isDisplayX:]
+ -[PLDisplayAgent logEventForwardDisplayALSWithDate:isDisplayX:]
+ -[PLDisplayAgent logEventForwardDisplayALSWithOcclusionTrigger:]
+ -[PLXPCAgent handleHingeUsageNotificationWithPayload:]
+ -[PLXPCAgent hingeUsageXPCListener]
+ -[PLXPCAgent logHingeUsageToCA:]
+ -[PLXPCAgent setHingeUsageXPCListener:]
+ GCC_except_table172
+ GCC_except_table177
+ GCC_except_table190
+ GCC_except_table202
+ GCC_except_table211
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
+ GCC_except_table36
+ GCC_except_table437
+ _OBJC_IVAR_$_PLXPCAgent._hingeUsageXPCListener
+ _PLBatteryAgentIntegerFromLowBatteryLogValue
+ _PLBatteryAgentRealFromLowBatteryLogValue
+ _PLBatteryAgentSecondsFromLowBatteryLogDuration
+ _PLBatteryAgentSplitPerDisplayValue
+ _PLBatteryAgentSplitPerDisplayValue.once
+ _PLBatteryAgentSplitPerDisplayValue.regex
+ _PLBatteryUsageUIKeyForRequest
+ ___32-[PLXPCAgent logHingeUsageToCA:]_block_invoke
+ ___47+[PLUtilities stringContainsControlCharacters:]_block_invoke
+ ___49+[PLUtilities isValidBatteryUIRequestingService:]_block_invoke
+ ___56-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLogString:]_block_invoke
+ ___56-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLogString:]_block_invoke_2
+ ___56-[PLBatteryUIResponderService plistSafeResultDictionary]_block_invoke
+ ___56-[PLBatteryUIResponderService plistSafeResultDictionary]_block_invoke_2
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_3
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke_3
+ ___PLBatteryAgentSplitPerDisplayValue_block_invoke
+ _closedir
+ _dirfd
+ _fcopyfile
+ _fdopendir
+ _fstat
+ _isValidBatteryUIRequestingService:.disallowedCharacters
+ _isValidBatteryUIRequestingService:.onceToken
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
+ _openat
+ _parsedCPMSKeysFromLowBatteryLogString:.kvRegex
+ _parsedCPMSKeysFromLowBatteryLogString:.once
+ _readdir
+ _stringContainsControlCharacters:.controlCharacters
+ _stringContainsControlCharacters:.onceToken
+ _unlinkat
- -[PLBatteryAgent parsedCPMSKeysFromLowBatteryLog]
- GCC_except_table169
- GCC_except_table170
- GCC_except_table18
- GCC_except_table188
- GCC_except_table200
- GCC_except_table203
- GCC_except_table25
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
- _CFDataGetTypeID
- ___49-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLog]_block_invoke
- ___49-[PLBatteryAgent parsedCPMSKeysFromLowBatteryLog]_block_invoke_2
- _parsedCPMSKeysFromLowBatteryLog.kvRegex
- _parsedCPMSKeysFromLowBatteryLog.once
CStrings:
+ ":"
+ ": "
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"
+ "Awake Time"
+ "AwakeTime"
+ "CBDisplayTelemetrySnapshot"
+ "CBOcclusionTelemetrySample"
+ "CBOcclusionTelemetryTrigger"
+ "Capacity"
+ "CoreMotion"
+ "CoreMotion::HingeUsage"
+ "Could not open source directory %@ for privileged copy, errno %d"
+ "DisplayX_ALS"
+ "Display_ALS"
+ "Error copying files from source path %@ to destination path %@"
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
+ "Object graph has control characters in a key, unsafe to serialize"
+ "Object graph has control characters in a string value, unsafe to serialize"
+ "Object graph has non-string key of class %{public}@, unsafe to serialize"
+ "Partial Charge"
+ "PartialCharge"
+ "Power Assertions"
+ "PowerAssertions"
+ "Privileged copy could not create destination %s, errno %d"
+ "Privileged copy could not open source %s, errno %d"
+ "Privileged copy could not remove partial destination %s, errno %d"
+ "Privileged copy could not stat source %s, errno %d"
+ "Privileged copy of %s failed, errno %d"
+ "Privileged copy refusing non-regular source %s"
+ "Refusing privileged copy to %@, errno %d"
+ "Refusing privileged copy to destination of unexpected class %{public}@"
+ "Refusing privileged copy to empty destination path"
+ "Rejecting requestingService containing disallowed characters"
+ "Rejecting requestingService of unexpected class %{public}@"
+ "Rejecting requestingService with invalid length %lu"
+ "Responder Service: omitting entry with unsafe key from plist"
+ "Responder Service: omitting entry with unsafe value from plist"
+ "Responder Service: omitting non-string key from plist"
+ "Screen Brightness"
+ "ScreenBrightness"
+ "ScreenBrightnessX"
+ "Standby Time"
+ "StandbyTime"
+ "TotalCloses"
+ "TotalOpens"
+ "Treating object graph nested deeper than %d levels as unsafe to serialize"
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
