## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x37724
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x2324
-  __TEXT.__const: 0x260
-  __TEXT.__oslogstring: 0x5c5e
-  __TEXT.__cstring: 0x293c
-  __TEXT.__gcc_except_tab: 0x3e68
-  __TEXT.__unwind_info: 0xf78
-  __TEXT.__objc_classname: 0x2e7
-  __TEXT.__objc_methname: 0x576f
-  __TEXT.__objc_methtype: 0x22df
-  __TEXT.__objc_stubs: 0x3d40
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x6a0
+370.55.0.0.0
+  __TEXT.__text: 0x3a928
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x24b4
+  __TEXT.__const: 0x268
+  __TEXT.__oslogstring: 0x6212
+  __TEXT.__cstring: 0x2b60
+  __TEXT.__gcc_except_tab: 0x3e88
+  __TEXT.__unwind_info: 0x1020
+  __TEXT.__objc_classname: 0x2ef
+  __TEXT.__objc_methname: 0x5977
+  __TEXT.__objc_methtype: 0x2359
+  __TEXT.__objc_stubs: 0x3e80
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1470
+  __DATA_CONST.__objc_selrefs: 0x14e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x5c0
-  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x470
-  __AUTH_CONST.__cfstring: 0x31e0
-  __AUTH_CONST.__objc_const: 0x37e8
+  __AUTH_CONST.__cfstring: 0x33e0
+  __AUTH_CONST.__objc_const: 0x3628
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0xc8
   __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0x358
-  __DATA.__bss: 0x140
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA.__data: 0x398
+  __DATA.__bss: 0x148
+  __DATA_DIRTY.__objc_data: 0x9d8
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1203
-  Symbols:   1647
-  CStrings:  1925
+  Functions: 1280
+  Symbols:   1732
+  CStrings:  1992
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ __ZN3MIL4Text12ParseProgramENSt3__110shared_ptrINS_10MILContextEEENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_13ParserOptionsE
+ __ZN3MIL4Text9SerializeERKNS_9IRProgramERKNS0_17SerializerOptionsE
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
+ "%@: Missing model or hint"
+ "%@: Not supported"
+ "%@: Program not loaded"
+ "%@: Set session hint %u success"
+ "%@: Unknown hint %@"
+ "%@: VM currently not supported for ANE hint"
+ "%@: Yes"
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
+ "-u"
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
+ "B56@0:8@16@24@32@40^@48"
+ "CFDictionaryRef ANEValidateNetworkCreateVMHost(uint64_t, CFStringRef _Nonnull, CFStringRef _Nonnull, CFStringRef _Nonnull, CFDataRef _Nonnull)"
+ "Inferences failed with unknown host error"
+ "Kernel call failed with error=0x%x"
+ "Private"
+ "^{__CFDictionary=}64@0:8Q16@24@32@40@48@56"
+ "^{__IOSurface=}32@0:8Q16^I24"
+ "ane_vm_allowPrecompiledBinary"
+ "arguments"
+ "com.apple.aned.private.ANEAccess.allow"
+ "createIOSurface:ioSID:"
+ "dataNotFoundForMethod:"
+ "doEvaluateWithModelLegacy:options:request:qos:completionEvent:error:"
+ "isAnetoolRootDaemonConnection"
+ "notSupportedErrorForMethod:"
+ "privateANEAccessEntitlement"
+ "processInfo"
+ "processName"
+ "processSessionHint:options:report:error:"
+ "sessionHintWithModel:hint:options:report:error:"
+ "updateError:errorLength:errorCode:error:"
+ "updatePerformanceStats:performanceStatsLength:hwExecutionTime:"
+ "validateEnvironmentForPrecompiledBinarySupport"
+ "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:milTextData:"
+ "vm_allowPrecompiledBinaryBootArg"
- "-[_ANEVirtualClient validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:]"
- "ANEVirtualClient evaluateWithModel model: %@\n"
- "ANEVirtualClient evaluateWithModel qos: %d\n"
- "ANEVirtualClient evaluateWithModel request: %@\n"
- "ANEVirtualClient evaluateWithmodel options: %@\n"
- "^{__CFDictionary=}56@0:8Q16@24@32@40@48"
- "validateNetworkCreate:uuid:function:directoryPath:scratchPadPath:"

```
