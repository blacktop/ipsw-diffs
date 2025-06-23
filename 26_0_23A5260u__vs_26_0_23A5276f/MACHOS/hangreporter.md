## hangreporter

> `/usr/libexec/hangreporter`

```diff

-375.0.0.0.0
-  __TEXT.__text: 0x3d060
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xfa4
+378.0.0.0.0
+  __TEXT.__text: 0x3e1a4
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_stubs: 0x2d40
+  __TEXT.__objc_methlist: 0xf74
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x2ea76
-  __TEXT.__oslogstring: 0x484b
+  __TEXT.__cstring: 0x2e80e
+  __TEXT.__oslogstring: 0x4b84
   __TEXT.__objc_classname: 0x147
-  __TEXT.__objc_methname: 0x51a9
-  __TEXT.__objc_methtype: 0x886
-  __TEXT.__gcc_except_tab: 0xcd8
-  __TEXT.__unwind_info: 0x4e8
-  __DATA_CONST.__auth_got: 0x798
+  __TEXT.__objc_methname: 0x5192
+  __TEXT.__objc_methtype: 0x87b
+  __TEXT.__gcc_except_tab: 0xc60
+  __TEXT.__unwind_info: 0x518
+  __DATA_CONST.__auth_got: 0x790
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__cfstring: 0x4b80
+  __DATA_CONST.__const: 0x1470
+  __DATA_CONST.__cfstring: 0x4b40
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x26a0
-  __DATA.__objc_selrefs: 0x1040
-  __DATA.__objc_ivar: 0x260
+  __DATA.__objc_const: 0x2640
+  __DATA.__objc_selrefs: 0x1060
+  __DATA.__objc_ivar: 0x258
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x638
-  __DATA.__bss: 0x1c8
+  __DATA.__bss: 0x1d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
-  - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 85A03444-F747-371E-BDD5-9BC2B1AB0551
-  Functions: 664
-  Symbols:   332
-  CStrings:  5531
+  UUID: 07535DE5-AD93-3C4F-A653-3E97CE638CAA
+  Functions: 673
+  Symbols:   331
+  CStrings:  5537
 
Symbols:
+ ___exp10
- _ADClientAddValueForScalarKey
- _ADClientPushValueForDistributionKey
CStrings:
+ "Failed to parse State info dictionary object from sorted array '%@', object is type of class '%@'"
+ "Failed to parse State info dictionary object of key '%@' from sorted array '%@', object is type of class '%@'"
+ "Found last State Info transition before hang end:%llu at index %lu for array %@"
+ "Found last State Info transition before hang start:%llu at index %lu for array %@."
+ "Invalid object(s) of class '%@' and '%@' passed into StateInfo timestamp comparator."
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary during sorting."
+ "No states were present in the state info array before a hang occurred."
+ "Object in state info array in not a dictioanry. Is kind of class %@"
+ "RBSTaskStateNone"
+ "RBSTaskStateRunningScheduled"
+ "RBSTaskStateRunningSuspended"
+ "RBSTaskStateRunningUnknown"
+ "RBSTaskStateUnknown"
+ "State Info JSON Payload Dict: %@"
+ "StateInfo"
+ "The provided stateInfoArray '%@' only has state objects BEFORE the start (%llu matu) but AFTER then end (%llu matu)."
+ "dictionaryWithDictionary:"
+ "endTaskState"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "floatValue"
+ "indexOfObject:inSortedRange:options:usingComparator:"
+ "intervalsInTaskState"
+ "numberWithUnsignedChar:"
+ "percentInTaskState"
+ "secondsSinceTaskStateTransitionBeforeHangStart"
+ "setValue:forKey:"
+ "startTaskState"
+ "stringValue"
+ "taskEnum"
+ "taskStateBreakdown"
+ "taskStateEnum"
+ "taskStateName"
+ "timeInTaskState"
+ "unsignedCharValue"
+ "v32@?0@8@16^B24"
+ "\xf0\xf0A!V!"
- "HangTracerEnableMemoryLogging"
- "HangTracerMemoryLoggingInterval"
- "TB,R,V_memoryLoggingEnabled"
- "TI,V_memoryLoggingIntervalSec"
- "_memoryLoggingEnabled"
- "_memoryLoggingIntervalSec"
- "com.apple.hangtracer.Fence-hang.%@"
- "com.apple.hangtracer.HTLogsBlownFence.%@"
- "com.apple.hangtracer.HTLogsBlownFence.Total"
- "com.apple.hangtracer.HTLogsConversion.AttemptType.%@"
- "com.apple.hangtracer.HTLogsConversion.Attempted"
- "com.apple.hangtracer.HTLogsConversion.DeletedDueTo3rdPartyFenceBelowHangThreshold"
- "com.apple.hangtracer.HTLogsConversion.DeletedDueToAppAnalyticsDisabled"
- "com.apple.hangtracer.HTLogsConversion.FailedNoSamples"
- "com.apple.hangtracer.HTLogsConversion.FailedReportCrashSubmit"
- "com.apple.hangtracer.HTLogsConversion.FencePidUnknown"
- "com.apple.hangtracer.HTLogsConversion.NoFenceFound"
- "com.apple.hangtracer.HTLogsConversion.NoFenceFound.EmptyTrace"
- "com.apple.hangtracer.HTLogsConversion.NoFenceFound.GoodTrace"
- "com.apple.hangtracer.HTLogsConversion.Succeeded"
- "com.apple.hangtracer.HTLogsFenceHang.PostTailspin"
- "com.apple.hangtracer.HTLogsLongFence.%@"
- "com.apple.hangtracer.HTLogsLongFence.Total"
- "initPropertyMemoryLoggingIntervalSec:"
- "memoryLoggingEnabled"
- "memoryLoggingIntervalSec"
- "setMemoryLoggingIntervalSec:"
- "v20@0:8I16"
- "\xf0\xf0Q!V!"

```
