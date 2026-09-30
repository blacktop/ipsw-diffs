## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x2f780
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x3540
-  __TEXT.__objc_methlist: 0x16c0
-  __TEXT.__const: 0x208
-  __TEXT.__oslogstring: 0x5894
-  __TEXT.__cstring: 0x2756
-  __TEXT.__objc_methname: 0x4172
+370.55.0.0.0
+  __TEXT.__text: 0x2f884
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_stubs: 0x3600
+  __TEXT.__objc_methlist: 0x18cc
+  __TEXT.__const: 0x210
+  __TEXT.__cstring: 0x2785
+  __TEXT.__gcc_except_tab: 0x4398
+  __TEXT.__objc_methname: 0x42c5
+  __TEXT.__oslogstring: 0x57a9
   __TEXT.__objc_classname: 0x2b4
-  __TEXT.__objc_methtype: 0x1eda
-  __TEXT.__gcc_except_tab: 0x4328
-  __TEXT.__unwind_info: 0xb68
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__cfstring: 0x2fa0
+  __TEXT.__objc_methtype: 0x1f3c
+  __TEXT.__unwind_info: 0xbc8
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1db8
-  __DATA.__objc_selrefs: 0x11f0
+  __DATA.__objc_const: 0x1af0
+  __DATA.__objc_selrefs: 0x12c0
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0x910
-  __DATA.__data: 0x428
+  __DATA.__data: 0x468
   __DATA.__bss: 0x250
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 835
-  Symbols:   393
-  CStrings:  1660
+  Functions: 864
+  Symbols:   403
+  CStrings:  1667
 
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
- _objc_retainAutoreleasedReturnValue
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
