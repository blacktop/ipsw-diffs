## tailspind

> `/usr/libexec/tailspind`

```diff

-250.2.0.0.0
-  __TEXT.__text: 0xd958
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x960
-  __TEXT.__objc_methlist: 0x1f4
+262.0.0.0.0
+  __TEXT.__text: 0xe684
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x134
-  __TEXT.__cstring: 0x10b5
-  __TEXT.__objc_methname: 0xc42
-  __TEXT.__oslogstring: 0x2798
-  __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methtype: 0xfb
-  __TEXT.__gcc_except_tab: 0x238
-  __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__cstring: 0x134a
+  __TEXT.__objc_methname: 0xee2
+  __TEXT.__oslogstring: 0x29cc
+  __TEXT.__objc_classname: 0x14
+  __TEXT.__objc_methtype: 0x119
+  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__unwind_info: 0x438
   __DATA_CONST.__const: 0x448
-  __DATA_CONST.__cfstring: 0x5c0
+  __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x300
-  __DATA.__objc_selrefs: 0x2f0
-  __DATA.__objc_ivar: 0x34
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x3c0
+  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2164
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x598
+  __DATA.__bss: 0x5c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 762A6723-834A-391B-BBF1-6B919ED9B4CD
-  Functions: 262
-  Symbols:   243
-  CStrings:  497
+  UUID: 82989B3C-BCB3-3A49-A4F1-CA7E0A1A1279
+  Functions: 284
+  Symbols:   254
+  CStrings:  586
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSSortDescriptor
+ __os_feature_enabled_impl
+ _ktrace_config_get_owner_name
+ _ktrace_config_kdebug_get_state
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _tailspin_buffer_size_set
- __os_log_fault_impl
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@_DurationSecs"
+ "%llx"
+ "%u,"
+ "0"
+ "<empty>"
+ "<unwedge_161103803>"
+ "@\"NSCountedSet\""
+ "A2!"
+ "BufferSizeConfiguredMB"
+ "BufferSizeUsedMB"
+ "CSC frequency str: %@"
+ "FAILED with error: %{public}@.\nFile path: %{public}@"
+ "Failed to get ktrace config owner name: %{errno}d"
+ "Failed to get ktrace config: %{errno}d"
+ "Failed to unwedge tailspin from bad state 161103803"
+ "FileSizeMB"
+ "Game mode disabled and detected default buffer size. Setting buffer size override"
+ "Game mode enabled and detected non-default buffer size set by tailspin. Resetting buffer size"
+ "IntelligenceFlow"
+ "IsDefaultConfig"
+ "Linwood"
+ "LostTimePeriodAtStartSecs"
+ "NumKdebugEvents"
+ "PercentageBufferSizeUsed"
+ "Phase_"
+ "Phase_Augment"
+ "Phase_Augment_LoggingData"
+ "Phase_Augment_Symbolicate"
+ "Phase_KdebugBufferWriteout"
+ "Phase_PostProcessing_Libktrace"
+ "Phase_PostProcessing_Tailspin"
+ "Phase_SaveStandardChunks"
+ "Phase_SaveStandardChunks_WithoutPostProcessing"
+ "PrevClientKdebugWriteoutDurationSecs"
+ "RequestProcessingLatencySecs"
+ "Successfully unwedge tailspind from bad state 161103803"
+ "T@\"NSCountedSet\",&,N,V_kdebugCSCCounts"
+ "TB,N,V_isDefaultConfig"
+ "TQ,N,V_bufferSizeConfiguredMB"
+ "Td,N,V_prevClientKdebugWriteoutDurationSecs"
+ "TopCSCsAndFreqs"
+ "TotalDurationSecs"
+ "_bufferSizeConfiguredMB"
+ "_isDefaultConfig"
+ "_kdebugCSCCounts"
+ "_prevClientKdebugWriteoutDurationSecs"
+ "appendString:"
+ "arrayWithObjects:count:"
+ "bufferSizeConfiguredMB"
+ "client %s [%d] requested for tailspin data but was rejected by the allowlist"
+ "com.apple.tailspind.saveresult.v3"
+ "countForObject:"
+ "feature enabled: %{bool}d"
+ "hangtracerd"
+ "hasPrefix:"
+ "hwtrace_live_recording_system_options_add_context_target_filtered"
+ "hwtrace_recording_save"
+ "hwtrace_recording_save_options_deinit"
+ "hwtrace_recording_save_options_init"
+ "hwtrace_recording_save_options_set_decode_trace"
+ "hwtrace_recording_save_options_set_ktrace_file"
+ "isDefaultConfig"
+ "kdebugCSCCounts"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedLong:"
+ "object"
+ "objectAtIndexedSubscript:"
+ "prevClientKdebugWriteoutDurationSecs"
+ "setBufferSizeConfiguredMB:"
+ "setIsDefaultConfig:"
+ "setKdebugCSCCounts:"
+ "setPrevClientKdebugWriteoutDurationSecs:"
+ "sortDescriptorWithKey:ascending:"
+ "sortedArrayUsingDescriptors:"
+ "stopRecordingTimeForDumpRequestPhase:errorStr:"
+ "string"
+ "substringFromIndex:"
+ "v20@?0i8@\"NSString\"12"
+ "v28@0:8B16@20"
+ "v32@?0r*8d16Q24"
- "Augment"
- "Augment_LoggingData"
- "Augment_Symbolicate"
- "FAILED due to reason: %{public}@.\nFile path: %{public}@"
- "PostProcessing_Libktrace"
- "PostProcessing_Tailspin"
- "SaveStandardChunks"
- "SaveStandardChunks_WithoutPostProcessing"
- "com.apple.tailspin.saveresult.v1"
- "hwtrace_recording_save_to_ktrace"
- "stopRecordingTimeForDumpRequestPhase:"
- "v12@?0i8"
- "v24@?0r*8Q16"

```
