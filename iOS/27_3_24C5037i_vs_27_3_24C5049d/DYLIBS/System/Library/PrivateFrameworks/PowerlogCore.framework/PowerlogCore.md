## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-3486.60.36.0.0
-  __TEXT.__text: 0xe671c
-  __TEXT.__objc_methlist: 0x9848
-  __TEXT.__const: 0x1c88
-  __TEXT.__cstring: 0x43b9d
-  __TEXT.__oslogstring: 0x8d92
+3486.60.47.0.0
+  __TEXT.__text: 0xe8150
+  __TEXT.__objc_methlist: 0x98c8
+  __TEXT.__const: 0x1ca0
+  __TEXT.__cstring: 0x43ef5
+  __TEXT.__oslogstring: 0x93ca
   __TEXT.__gcc_except_tab: 0x2a58
-  __TEXT.__unwind_info: 0x44d0
+  __TEXT.__unwind_info: 0x4578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a00
+  __DATA_CONST.__objc_selrefs: 0x5a68
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x46248
+  __DATA_CONST.__objc_arraydata: 0x46608
   __DATA_CONST.__got: 0x7e8
-  __AUTH_CONST.__const: 0x2540
-  __AUTH_CONST.__cfstring: 0x6d640
-  __AUTH_CONST.__objc_const: 0xaa30
+  __AUTH_CONST.__const: 0x25c0
+  __AUTH_CONST.__cfstring: 0x6dc00
+  __AUTH_CONST.__objc_const: 0xaa60
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x4cc8
+  __AUTH_CONST.__objc_intobj: 0x4ce0
   __AUTH_CONST.__objc_doubleobj: 0x14d0
   __AUTH_CONST.__objc_arrayobj: 0x1230
-  __AUTH_CONST.__objc_dictobj: 0xfe60
-  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH_CONST.__objc_dictobj: 0xff50
+  __AUTH_CONST.__auth_got: 0xe08
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x7d0
+  __DATA.__objc_ivar: 0x7d4
   __DATA.__data: 0x4a0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1e50
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x11f8
+  __DATA_DIRTY.__bss: 0x11e8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4977
-  Symbols:   7284
-  CStrings:  15344
+  Functions: 5022
+  Symbols:   7312
+  CStrings:  15416
 
Symbols:
+ +[PLGestaltUtilities isV68]
+ +[PLUtilities isPlistSafeObject:]
+ +[PLUtilities isPlistSafeObject:atDepth:]
+ +[PLUtilities isValidBatteryUIRequestingService:]
+ +[PLUtilities privilegedCopyFileNamed:fromDirectoryFd:toDirectoryFd:]
+ +[PLUtilities privilegedCopyItemsFromPath:toDirectory:]
+ +[PLUtilities stringContainsControlCharacters:]
+ +[PPSFileUtilities(APFS) markFileDescriptorAsPurgeable:urgency:startDate:]
+ -[PLCoreStorage backgroundProcessingResponder]
+ -[PLCoreStorage setBackgroundProcessingResponder:]
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table136
+ GCC_except_table147
+ GCC_except_table168
+ GCC_except_table177
+ GCC_except_table211
+ GCC_except_table36
+ GCC_except_table99
+ _OBJC_IVAR_$_PLCoreStorage._backgroundProcessingResponder
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _PLCopyPrunedBackgroundProcessingLog
+ ___27+[PLGestaltUtilities isV68]_block_invoke
+ ___47+[PLUtilities stringContainsControlCharacters:]_block_invoke
+ ___49+[PLUtilities isValidBatteryUIRequestingService:]_block_invoke
+ _closedir
+ _dirfd
+ _fcopyfile
+ _fdopendir
+ _fstat
+ _isV68.onceToken
+ _isV68.ret
+ _isValidBatteryUIRequestingService:.disallowedCharacters
+ _isValidBatteryUIRequestingService:.onceToken
+ _openat
+ _readdir
+ _stringContainsControlCharacters:.controlCharacters
+ _stringContainsControlCharacters:.onceToken
+ _unlinkat
- GCC_except_table106
- GCC_except_table125
- GCC_except_table130
- GCC_except_table135
- GCC_except_table138
- GCC_except_table146
- GCC_except_table167
- GCC_except_table169
- GCC_except_table203
- GCC_except_table98
- ___41-[PLCoreStorage initOperatorDependancies]_block_invoke_6
- ___41-[PLCoreStorage initOperatorDependancies]_block_invoke_7
CStrings:
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"
+ "AggAngleCloses"
+ "AggAngleOpens"
+ "AggIntAngleCloses"
+ "AggIntAngleOpens"
+ "AwakeTime"
+ "Background processing log not placed at destination '%{public}@': %{public}@"
+ "BackgroundProcessingLog"
+ "Capacity"
+ "Could not open source directory %@ for privileged copy, errno %d"
+ "DuetDiagnosticExtension"
+ "Error copying files from source path %@ to destination path %@"
+ "Failed to copy background processing log into %@: %@"
+ "Failed to copy background processing log: %@"
+ "Failed to create a scratch directory for the background processing log: %{public}@"
+ "Failed to mark fd %d as purgeable with label: '%@' (error %d = '%s')"
+ "Failed to remove the background processing log scratch directory: %{public}@"
+ "ForegroundApplications"
+ "ForegroundApplicationsX"
+ "HingeMetricsStartTime"
+ "HingeState"
+ "HingeUsage"
+ "Marked fd %d as purgeable with label: '%@'"
+ "MitigationValue"
+ "Object graph has control characters in a key, unsafe to serialize"
+ "Object graph has control characters in a string value, unsafe to serialize"
+ "Object graph has non-string key of class %{public}@, unsafe to serialize"
+ "PLDisplayAgent_EventForward_DisplayX_ALS"
+ "PLDisplayAgent_EventForward_Display_ALS"
+ "PartialCharge"
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
+ "Refusing to copy the background processing log to the destination requested by %@"
+ "Rejecting requestingService containing disallowed characters"
+ "Rejecting requestingService of unexpected class %{public}@"
+ "Rejecting requestingService with invalid length %lu"
+ "ScreenBrightness"
+ "ScreenBrightnessX"
+ "StandbyTime"
+ "TLCMitigation"
+ "TotalCloses"
+ "TotalOpens"
+ "Treating object graph nested deeper than %d levels as unsafe to serialize"
+ "VoltageMV"
+ "colorALSMask"
+ "colorX_1"
+ "colorX_14"
+ "colorY_1"
+ "colorY_14"
+ "colorZ_1"
+ "colorZ_14"
+ "embeddingTableMemoryCostKB"
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
+ "triggers"
+ "trustedALS"
```
