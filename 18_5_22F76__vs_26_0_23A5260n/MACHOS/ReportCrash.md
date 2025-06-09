## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

-758.120.5.0.0
-  __TEXT.__text: 0x2a1ec
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x2ea0
-  __TEXT.__objc_methlist: 0xc38
-  __TEXT.__cstring: 0x4e51
-  __TEXT.__const: 0x2f4
-  __TEXT.__objc_methname: 0x34ec
-  __TEXT.__oslogstring: 0x1849
-  __TEXT.__objc_classname: 0x103
-  __TEXT.__objc_methtype: 0x804
-  __TEXT.__gcc_except_tab: 0x3c8
+912.0.0.0.0
+  __TEXT.__text: 0x2c530
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_stubs: 0x3040
+  __TEXT.__objc_methlist: 0xd10
+  __TEXT.__cstring: 0x5341
+  __TEXT.__const: 0x444
+  __TEXT.__objc_methname: 0x37bf
+  __TEXT.__oslogstring: 0x1a49
+  __TEXT.__objc_classname: 0x104
+  __TEXT.__objc_methtype: 0x805
+  __TEXT.__gcc_except_tab: 0x304
   __TEXT.__dlopen_cstrs: 0xa5
-  __TEXT.__constg_swiftt: 0x2d8
-  __TEXT.__swift5_typeref: 0x256
+  __TEXT.__swift5_typeref: 0x268
+  __TEXT.__swift5_capture: 0xe4
+  __TEXT.__constg_swiftt: 0x304
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x80
-  __TEXT.__swift5_fieldmd: 0x108
+  __TEXT.__swift5_fieldmd: 0x118
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__swift5_capture: 0xcc
+  __TEXT.__swift5_types: 0x28
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x680
-  __TEXT.__eh_frame: 0x170
-  __DATA_CONST.__auth_got: 0xc30
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0xc40
-  __DATA_CONST.__cfstring: 0x7200
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__eh_frame: 0x248
+  __DATA_CONST.__auth_got: 0xca0
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__auth_ptr: 0x150
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__cfstring: 0x7500
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x338
-  __DATA_CONST.__objc_dictobj: 0x190
+  __DATA_CONST.__objc_intobj: 0x4e0
+  __DATA_CONST.__objc_arraydata: 0x358
+  __DATA_CONST.__objc_dictobj: 0x1e0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1c70
-  __DATA.__objc_selrefs: 0xe28
-  __DATA.__objc_ivar: 0x230
-  __DATA.__objc_data: 0x6f8
-  __DATA.__data: 0x4f0
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x260
-  __DATA.__common: 0x1
+  __DATA.__objc_const: 0x1e98
+  __DATA.__objc_selrefs: 0xed0
+  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_data: 0x888
+  __DATA.__data: 0x5e8
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x240
+  __DATA.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/GCoreFramework.framework/GCoreFramework
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
-  - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5308177F-549D-3825-903B-8792A9BDCEAA
-  Functions: 571
-  Symbols:   574
-  CStrings:  2839
+  UUID: 17A3EC6F-D4AE-36CA-BBD7-478DA8E21E20
+  Functions: 623
+  Symbols:   587
+  CStrings:  2946
 
Symbols:
+ _$s11OSAnalytics11DeviceStateC15isCustomerFusedSbvgZ
+ _$s11OSAnalytics11DeviceStateCMa
+ _$s11OSAnalytics24WatchdogExitReasonHelperC19descriptionFromCodeySSSgs5Int32VFZ
+ _$s11OSAnalytics24WatchdogExitReasonHelperCMa
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s8Dispatch0A13TimeoutResultO2eeoiySbAC_ACtFZ
+ _$s8Dispatch0A4TimeV3nowACyFZ
+ _$s8Dispatch0A4TimeVMa
+ _$sSS10describingSSx_tclufC
+ _$sSiN
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$sSo21OS_dispatch_semaphoreC8DispatchE4wait7timeoutAC0D13TimeoutResultOAC0D4TimeV_tF
+ _$sSo21OS_dispatch_semaphoreC8DispatchE6signalSiyF
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss38_bridgeAnythingNonVerbatimToObjectiveCyyXlxnlF
+ _$ss6UInt32VN
+ ___kCFBooleanFalse
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _create_gcore_with_options
+ _os_variant_has_internal_diagnostics
+ _os_variant_is_darwinos
+ _swift_setDeallocating
+ _usleep
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- _$ss4Int8VMn
- _OBJC_CLASS_$_LockdownModeManager
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _kOSALogOptionPriority
- _objc_retain_x28
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_release_n
CStrings:
+ " (Limit %u MB) Crossed Conclave Memory Limit"
+ " Page Domain Fault"
+ " Section Domain Fault"
+ " Sync External abort translation table walk"
+ " Sync External abort, not translation table walk"
+ " Sync parity or ECC error translation table walk"
+ " Sync parity or ECC error, not translation table walk"
+ " TLB conflict abort"
+ " Unsupported atomic hardware update fault"
+ "%hhd"
+ "%hhu"
+ "(Syscall)"
+ "*52@0:8I16Q20Q28^B36^B44"
+ "@\"KcdataParser\""
+ "@\"TaskOperator\""
+ "@48@0:8Q16Q24^B32^B40"
+ "B40@0:8Q16{_VMURange=QQ}24"
+ "B40@0:8{kcdata_iter=^{kcdata_item}^v}16q32"
+ "Core file creation result: %d"
+ "Core file not requested with max size = %s and process name = %s"
+ "Creating a core file from ReportCrash is not available"
+ "Failed to create OSAOsLogPackParser"
+ "Failed to parse os_log_pack data"
+ "INVALID_MPO_ENTITLEMENT"
+ "INVALID_NOTIFICATION_REQ"
+ "KOBJECT_REPLY_PORT_SEMANTICS"
+ "KcdataParser"
+ "OOL_PORT_ARRAY_CREATION"
+ "REALITYKIT"
+ "RealityKit scene is too complex: (Directional + Spot + Point) LightComponent limit exceeded"
+ "RealityKit scene is too complex: AudioPlaybackController limit exceeded"
+ "RealityKit scene is too complex: GroundingShadowComponent limit exceeded"
+ "RealityKit scene is too complex: ModelComponent limit exceeded"
+ "RealityKit scene is too complex: SynchronizationComponent limit exceeded"
+ "ReportCrash6"
+ "ReportCrash7"
+ "Requesting a core file for %s"
+ "Skipping core file request as the current number of concurrent requests exceeds the max of %ld"
+ "Skipping core file request for gcore"
+ "T@\"KcdataParser\",R,N,V_kcdataParser"
+ "T@\"TaskOperator\",R,N,V_taskOperator"
+ "TB,R,N,V_is_full_corpse"
+ "TaskOperator"
+ "Unable to get virtual address size: %s (%d)"
+ "Unexpected kcdata item size for type %u: %u < %ld"
+ "_TtC11ReportCrash25WatchdogTerminationReason"
+ "__swift_setObject:forKeyedSubscript:"
+ "_applicationSpecificInfoRedacted"
+ "_asiFormattedFiltered"
+ "_asiFormattedInternal"
+ "_asiFormattedSafe"
+ "_copyStringFromTask:atAddress:maxLength:immutableCheck:isInSharedCache:"
+ "_isMemorySafeAtAddress:"
+ "_kcdataParser"
+ "_mergeFormattedASI"
+ "_readIndirectSafeStringFromSymbol:symbolOwner:"
+ "_readStringAtTaskAddress:maxLength:immutableCheck:isInSharedCache:"
+ "_regionAtAddress:immutableCheck:isInSharedCache:"
+ "_taskOperator"
+ "addFieldsToCrashEvent:"
+ "addFieldsToHeader:"
+ "addJITImage:size:"
+ "asiRedacted"
+ "bootProgressRegister"
+ "com.apple.ReportCrash.coreFileWriter"
+ "coreFileProcessList"
+ "customerFused"
+ "decode_reasonRealityKit"
+ "decode_syndrome:"
+ "descriptionFromCode:"
+ "developerMode"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "extraction"
+ "filterOutSensitiveParts:withFormats:"
+ "gcore is not available"
+ "heap(1) and vmmap(1) outputs have been replaced by ReportMemoryException diagnostics and a limited number of memory graphs. You can find them in a sysdiagnose under 'crashes_and_spins/MemoryExceptions' and on device by running `ReportMemoryExceptionTool -l`. Memory graphs can be opened with Xcode and provided as inputs to most memory tools, including footprint(1), heap(1), leaks(1), and vmmap(1). ReportMemoryException diagnostics can be read with `ReportMemoryExceptionTool -f <path>`. You can learn more by visiting at.apple.com/MemoryLimitDebugging."
+ "hwModel"
+ "initAlertDelegate"
+ "initWithMaxNumAruments:"
+ "isAddress:inRange:"
+ "isCustomerFused"
+ "isDeveloperMode"
+ "isFullCorpse"
+ "isSecurityResearchDeviceERM"
+ "kcdataParser"
+ "machdep.virtual_address_size"
+ "parseElement:from:"
+ "parsed"
+ "processCrashReporterAnnotations:"
+ "requestedNoReport"
+ "requested_no_report"
+ "set"
+ "setModulePathForMemoryPointer:"
+ "setPointerPointsToSafeMemory:"
+ "setWithObjects:"
+ "stringArrayForKey:"
+ "taskOperator"
+ "v24@0:8@?16"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v344@0:8{crashreporter_annotations_t=QQQQQQQQ[256c]C}16"
+ "v36@0:8I16{kcdata_iter=^{kcdata_item}^v}20"
+ "writeReportBodyWithSectionWriter:"
+ "x86 process execution is disabled via nox86exec boot-arg"
+ "{_VMURange=QQ}40@0:8Q16^B24^B32"
- "*44@0:8I16Q20Q28^B36"
- "@40@0:8Q16Q24^B32"
- "B40@0:8{kcdata_iter=^{kcdata_item}^v}16Q32"
- "ExcResourceDiagInfo_%@"
- "HWModelStr"
- "The process footprint was too large for running vmmap and heap, instead a memgraph generation was potentially attempted via a process core dump. You can find this in a sysdiagnose under 'crashes_and_spins/MemoryExceptions' and on device by running `ReportMemoryExceptionTool -l`. Memory graphs can be opened with Xcode and provided as inputs to most memory tools, including footprint(1), heap(1), leaks(1), and vmmap(1). ReportMemoryException diagnostics can be read with `ReportMemoryExceptionTool -f <path>`. You can learn more by visiting at.apple.com/MemoryLimitDebugging."
- "To mitigate the CPU impact of repeated ExcResource events for this process, vmmap and heap were excluded. Please check an older report within the hour for those diagnostics."
- "Unexpected kcdata item size for type 0x%x: %lu < %lu "
- "_copyStringFromTask:atAddress:maxLength:immutableCheck:"
- "_isMemoryImmutableAtAddress:"
- "_readIndirectImmutableStringFromSymbol:symbolOwner:"
- "_readStringAtTaskAddress:maxLength:immutableCheck:"
- "_regionAtAddress:immutableCheck:"
- "com.apple.osanalytics.diagnosticInfo"
- "date"
- "enabled"
- "filterOutSensitiveStrings:"
- "isComputeNode"
- "kern.max_task_pmem"
- "monitoring timed out for service"
- "setModulePathForImmutableMemoryPointer:"
- "setPointerPointsToImmutableMemory:"
- "shared"
- "timeIntervalSinceDate:"
- "{_VMURange=QQ}32@0:8Q16^B24"

```
