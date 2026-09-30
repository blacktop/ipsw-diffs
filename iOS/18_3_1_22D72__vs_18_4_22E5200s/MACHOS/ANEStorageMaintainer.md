## ANEStorageMaintainer

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x23cb4
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_stubs: 0x29c0
-  __TEXT.__objc_methlist: 0x1170
-  __TEXT.__const: 0x1f8
-  __TEXT.__oslogstring: 0x4b5c
-  __TEXT.__cstring: 0x232c
-  __TEXT.__objc_methname: 0x32e7
+370.55.0.0.0
+  __TEXT.__text: 0x23df8
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_stubs: 0x2a80
+  __TEXT.__objc_methlist: 0x134c
+  __TEXT.__const: 0x200
+  __TEXT.__cstring: 0x235b
+  __TEXT.__oslogstring: 0x4a71
+  __TEXT.__objc_methname: 0x343a
   __TEXT.__objc_classname: 0x197
-  __TEXT.__objc_methtype: 0x1bda
-  __TEXT.__gcc_except_tab: 0x3970
-  __TEXT.__unwind_info: 0x938
-  __DATA_CONST.__auth_got: 0x538
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x800
-  __DATA_CONST.__cfstring: 0x2aa0
+  __TEXT.__objc_methtype: 0x1c3c
+  __TEXT.__gcc_except_tab: 0x399c
+  __TEXT.__unwind_info: 0x988
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__cfstring: 0x2900
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x14d0
-  __DATA.__objc_selrefs: 0xea8
+  __DATA.__objc_const: 0x1248
+  __DATA.__objc_selrefs: 0xf78
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x550
-  __DATA.__data: 0x368
+  __DATA.__data: 0x3a8
   __DATA.__bss: 0x220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 678
-  Symbols:   312
-  CStrings:  1373
+  Functions: 708
+  Symbols:   323
+  CStrings:  1380
 
Symbols:
+ __ZN3MIL4Text12ParseProgramENSt3__110shared_ptrINS_10MILContextEEENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_13ParserOptionsE
+ __ZN3MIL4Text9SerializeERKNS_9IRProgramERKNS0_17SerializerOptionsE
+ _fcntl
+ _kANEFHintEnergyEfficientWorkloadKey
+ _kANEFHintReportResidentPagesKey
+ _kANEFHintReportSessionStatusKey
+ _kANEFHintReportTotalPagesKey
+ _kANEFHintSessionAbort
+ _kANEFHintSessionInfo
+ _kANEFHintSessionStart
+ _kANEFHintSessionStop
CStrings:
+ "%@: %@ - 0x%llx"
+ "%@: ANEVirtualClient evaluateWithModel model=%@ options=%@ request=%@ qos=%d"
+ "%@: BAD_ARGUMENT error object is nil"
+ "%@: BAD_ARGUMENT errorIOSurface is nil!"
+ "%@: BAD_ARGUMENT errorLength is 0!"
+ "%@: BAD_ARGUMENT perfStatsIOSurface is NULL!"
+ "%@: Data not found error"
+ "%@: ERROR %@"
+ "%@: ERROR : conditions for precompiled binary support not met! isGuestInternalBuild=%d isHostInternalBuild=%d minimumInterfaceRequirementsMet=%d minimumCapabilityRequirementsMet=%d isPrecompiledBinaryBootArgSet=%d"
+ "%@: ERROR Failed to create errorIOSurface, host-side error reporting will not work"
+ "%@: ERROR Failed to create perfStatsIOSurface"
+ "%@: ERROR Invalid number of completion events"
+ "%@: ERROR failed to get base address for errorIOSurface"
+ "%@: ERROR failed to get string from decoder"
+ "%@: ERROR failed unarchive data:%@"
+ "%@: ERROR optionsArchive length is 0"
+ "%@: FAILED to get dataBaseAddress for perfStatsIOSurfaceRef"
+ "%@: FAILED to get optionsArchive from options dictionary"
+ "%@: FAILED to get perfStatsData object (dataLength=%llu)"
+ "%@: Failed to set session hint %u ret=0x%x"
+ "%@: Not supported"
+ "%@: Set session hint %u success"
+ "%@: Unknown hint %@"
+ "%@: fcntl(F_RDADVISE). errno=%d : %s"
+ "%@: ioSIDPerStats ioSID: %u statsType : %ld"
+ "%@: milTextData is nil! negotiated interface version 0x%x expects a valid milTextData object"
+ "%@: perfStatsLength=0 hwExecutionTime=0, no perfStats to report"
+ "%@: request.inputArray ioSID: %u"
+ "%@: request.inputIndexArray : %llu"
+ "%@: request.outputArray ioSID: %u"
+ "%@: request.outputIndexArray : %llu"
+ "%@: signal events port is %#x and value is %llu\n"
+ "%@: weightsBufferIOSID: %u"
+ "%s:%d Failed to parse MIL::IRProgram"
+ "-[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:]"
+ "@40@0:8^{__IOSurface=}16Q24Q32"
+ "ANEClientEnergyEfficientWorkload"
+ "ANEClientResidentPages"
+ "ANEClientSessionStatus"
+ "ANEClientTotalPages"
+ "ANEHintClientSessionAbort"
+ "ANEHintClientSessionInfo"
+ "ANEHintClientSessionStart"
+ "ANEHintClientSessionStop"
+ "B48@0:8^{__IOSurface=}16Q24q32^@40"
+ "CFDictionaryRef ANEValidateNetworkCreateVMHost(uint64_t, CFStringRef _Nonnull, CFStringRef _Nonnull, CFStringRef _Nonnull, CFDataRef _Nonnull)"
+ "Inferences failed with unknown host error"
+ "Kernel call failed with error=0x%x"
+ "^{__CFDictionary=}64@0:8Q16@24@32@40@48@56"
+ "^{__IOSurface=}32@0:8Q16^I24"
+ "ane_vm_allowPrecompiledBinary"
+ "com.apple.aned.private.ANEAccess.allow"
+ "createIOSurface:ioSID:"
+ "dataNotFoundForMethod:"
+ "notSupportedErrorForMethod:"
+ "privateANEAccessEntitlement"
+ "processSessionHint:options:report:error:"
+ "updateError:errorLength:errorCode:error:"
+ "updatePerformanceStats:performanceStatsLength:hwExecutionTime:"
+ "validateEnvironmentForPrecompiledBinarySupport"
+ "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:"
+ "vm_allowPrecompiledBinaryBootArg"
- "%@: ANEVirtualClient 2 reqQueued=%d\n"
- "%@: ANEVirtualClient _ioSPerformanceStats pointer null\n"
- "%@: ANEVirtualClient evaluateWithModel dictionary call succeeded"
- "%@: ANEVirtualClient evaluateWithModel success=%lld"
- "%@: ANEVirtualClient number of signal shared events=%llu\n"
- "%@: ANEVirtualClient queued the evaluate request. res=%d"
- "%@: ANEVirtualClient signal events port is %#x and value is %llu\n"
- "-[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:]"
- "ANEVirtualClient Connect to driver for kAppleVirtIONeuralEngineDeviceUserClientEvaluateWithModel."
- "ANEVirtualClient Evaluate request1 ioSID: %u"
- "ANEVirtualClient Evaluate request2 ioSID: %llu"
- "ANEVirtualClient Evaluate request3 ioSID: %u"
- "ANEVirtualClient Evaluate request4 ioSID: %llu"
- "ANEVirtualClient Evaluate request5 ioSID: %u"
- "ANEVirtualClient Evaluate request6 ioSID: %u"
- "ANEVirtualClient Evaluate request7 ioSID: %ld"
- "ANEVirtualClient Evaluate request7 ioSID: %u"
- "ANEVirtualClient Evaluate: request.inputArray %lu request.inputIndexArray %lu request.outputArray %lu request.outputIndexArray %lu"
- "ANEVirtualClient Evaluate: virtualANEModel.ioSIDModelNet=%u virtualANEModel.ioSIDModelShape=%u virtualANEModel.ioSIDModelWeight=%u virtualANEModel.ioSIDKey=%u virtualANEModel.string_id=%lld virtualANEModel.programHandle=%lld virtualANEModel.intermediateBufferHandle=%lld virtualANEModel.queueDepth=%d virtualANEModel.ioSIDModelAttributes=%u virtualANEModel.perfStatsMask=%u virtualANEModel.qos=%u virtualANEModel.ioSIDOptions=%u virtualANEModel.ioSIDErrorValue=%u"
- "ANEVirtualClient evaluateWithModel model: %@\n"
- "ANEVirtualClient evaluateWithModel qos: %d\n"
- "ANEVirtualClient evaluateWithModel request: %@\n"
- "ANEVirtualClient evaluateWithmodel options: %@\n"
- "ANEVirtualClient failed to call evaluateWithModel dictionary method with error:%@"
- "Invalid number of completion events"
- "^{__CFDictionary=}56@0:8Q16@24@32@40@48"
- "_ANEVirtualClient calling dictionary doEvaluateWithModel method"
- "errorEventport"
- "inputArray%d"
- "inputArrayCount"
- "inputIndexArray%d"
- "inputIndexArrayCount"
- "ioSIDPerfStats%d"
- "ioSIDPerformanceStatsIndex"
- "ioSIDWeightsBufferIndex"
- "outputArray%d"
- "outputArrayCount"
- "outputIndexArray%d"
- "outputIndexArrayCount"
- "perfStatsCount"
- "perfStatsType%d"
- "signalEvents%dAgentMask"
- "signalEvents%dSymbolIndex"
- "signalEvents%dValue"
- "signalEvents%dport"
- "signalEvents%dtype"
- "signalEventsCount"
- "successEventport"
- "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:"
- "waitEvents%dValue"
- "waitEvents%dport"
- "waitEvents%dtype"
- "waitEventsCount"

```
