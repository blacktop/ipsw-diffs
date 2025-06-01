## MPSBenchmarkLoop

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop`

```diff

-127.1.3.0.0
-  __TEXT.__text: 0xbb18
-  __TEXT.__auth_stubs: 0x600
+127.4.8.0.0
+  __TEXT.__text: 0x9a88
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0x938
-  __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x1da6
-  __TEXT.__gcc_except_tab: 0x244
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x1dc
+  __TEXT.__cstring: 0x1545
   __TEXT.__ustring: 0x48
-  __TEXT.__unwind_info: 0x394
+  __TEXT.__unwind_info: 0x2f0
   __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x7bed
-  __TEXT.__objc_methtype: 0x34ac
-  __TEXT.__objc_stubs: 0x1720
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x320
+  __TEXT.__objc_methname: 0x79e1
+  __TEXT.__objc_methtype: 0x3475
+  __TEXT.__objc_stubs: 0x13e0
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x88f8
-  __DATA_CONST.__objc_selrefs: 0x758
-  __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__cfstring: 0x7e0
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__objc_const: 0x0
+  __DATA_CONST.__objc_const: 0x88b8
+  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x310
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x21c
+  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x300
-  __DATA.__bss: 0x50
   __DATA.__common: 0xc
-  __DATA_DIRTY.__const: 0xf0
+  __DATA.__bss: 0x28
+  __DATA_DIRTY.__const: 0xb0
   __DATA_DIRTY.__objc_const: 0x4c8
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69AB1EE8-F0CB-3ABF-BE6A-0FF4CFC224EF
-  Functions: 297
-  Symbols:   169
-  CStrings:  1747
+  UUID: 39EF7A03-5F72-3207-B71D-6DC69EE907BD
+  Functions: 236
+  Symbols:   153
+  CStrings:  1643
 
Symbols:
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ _strncmp
- _GRCCopyAllCounterSourceGroup
- _GRCReleaseAllCounterSourceGroup
- _MTLCreateSystemDefaultDevice
- _NSClassFromString
- _OBJC_CLASS_$_GPURawCounterSelect
- _OBJC_CLASS_$_GPURawCounterSourceTriggerSelect
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- __ZdaPv
- __ZnamSt19__type_descriptor_t
- ___kCFBooleanTrue
- _bzero
- _exit
- _objc_release
- _objc_release_x28
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "T@\"NSString\",?,R,C"
+ "TB,?"
+ "TB,?,N,GisStatEnabled"
+ "TB,?,R,GisClampToHalfBorderSupported"
+ "TB,?,R,GisCustomBorderColorSupported"
+ "TB,?,R,GisQuadDataSharingSupported"
+ "TB,?,R,GisRGB10A2GammaSupported"
+ "TQ,?,N,GgetStatLocations"
+ "TQ,?,N,GgetStatOptions"
+ "TQ,?,R"
+ "WARNING: MPS_BENCHMARK_LOOP_PSTATE not set. Cycle count will be based on 1GHz. Please use agx_util to set p-state and set MPS_BENCHMARK_LOOP_PSTATE=value env var to let GRC backend know the value you are setting to so that correct cycle count can be computed using timestamp and frequency corresponding to p-state\n"
+ "Workload total Without overhead cycle count standard deviation: %f\n"
+ "Workload total Without overhead cycle count: %f\n"
+ "Workload total with overhead cycle count standard deviation: %f\n"
+ "Workload total with overhead cycle count: %f\n"
+ "_timeStampSampleDouble"
+ "aggregatePerfSamplesForCommandBuffer:firstCommandBuffer:"
+ "encoder: %lu cycle count standard deviation: %f\n"
+ "encoder: %lu cycle count: %f\n"
+ "encoderId"
+ "gblGPUCycles"
+ "gbltimestamp"
+ "getPStateAndFrequency"
+ "sampleType"
+ "supportsArgumentBuffers"
+ "supportsResourceHeaps"
- "\n\nMPS_BENCHMARK_LOOP_GRC_PSTATE set to %llu ... forcing p-state using GRC SPI\n"
- "\nEnd Subtest\n"
- "\nStart Subtest: %s\n\n"
- "%8.3f %s  %s\n"
- "./"
- "/System/Library/Frameworks/ATFMTL.framework/ATFMTL"
- "/System/Library/Frameworks/MetalKit.framework"
- "@\"<GPURawCounterSource>\""
- "@\"<GPURawCounterSourceGroup>\""
- "ATF not present. Skipping leak detection."
- "ATFAnyErrors"
- "ATFExit"
- "ATFGetTestResultsDirectory"
- "ATFLogPerformanceNumber"
- "ATFMTLAnyErrors"
- "ATFMTLCollectCompilePerformanceStatistics"
- "ATFMTLCopyTestDevice"
- "ATFMTLSaveBuffer"
- "ATFMTLSaveTexture"
- "ATFMTLSetCompileLogMode"
- "ATFMTLSetCompileLogType"
- "ATFMTLTestFinish"
- "ATFMTLTestStart"
- "ATFReportLeaks"
- "ATFSubTestFinish"
- "ATFSubTestStart"
- "ATFTestFinish"
- "ATFTestFinish,"
- "ATFTestStart %s\n"
- "ATFTestStartVersion"
- "Cannot find RDE source\n"
- "DisableOverlap"
- "Encoder %llu # of samples %lu > 2 times number of ring buffers\n"
- "Encoder %llu samples missing either start or end sample #samples %lu\n"
- "Error, counter source group is nil!"
- "Error, counter source group list is empty!"
- "Error, fail to get counter source group list!"
- "Error, source has no ring buffer!"
- "Error, there are multiple source group in the list (%u)!"
- "FRG1_COUNT_CYCLES"
- "Fail to start sampling on sourceGroup:%s"
- "Fail, error while enabling source:%s"
- "Fail, error while requesting counterList[%u]=%s for source:%s"
- "Fail, error while requesting triggerList[%u]=%s for source:%s"
- "GBL_GPU_N_CLK_TIMER"
- "GBL_GPU_TIMER"
- "GPURawCounters source group %s\n"
- "GRC_ENCODER_ID"
- "GRC_GPU_CYCLES"
- "GRC_SAMPLE_TYPE"
- "INVALID_ERROR_INDEX"
- "KickBoundary"
- "LockGPUPerfState"
- "MPS_BENCHMARK_LOOP_ENABLE_ENCODER_COALESCING disabled through environment variable\n"
- "MPS_BENCHMARK_LOOP_GRC_PSTATE"
- "MPS_LEGACY_TIMING"
- "MPS_USE_GRC"
- "MPS_USE_GRC environment variable is set to 0. Turning off GRC\n"
- "MTKTextureLoader"
- "No sample for encoder %llu\n"
- "Order of counters returned is not same as requested\n"
- "RDE"
- "Setting pState to %d frequrncy %llu MHz\n"
- "Skipping ATFMTLCopyTestDevice.  ATF not installed."
- "Skipping ATFMTLSaveBuffer.  ATF not installed."
- "Skipping ATFMTLSaveTexture.  ATF not installed."
- "Source list has zero sources!"
- "TB,N,GisStatEnabled"
- "TB,R,GisClampToHalfBorderSupported"
- "TB,R,GisCustomBorderColorSupported"
- "TB,R,GisQuadDataSharingSupported"
- "TB,R,GisRGB10A2GammaSupported"
- "TQ,N,GgetStatLocations"
- "TQ,N,GgetStatOptions"
- "WARNING: MPS_BENCHMARK_LOOP_PSTATE not set. Cycle count will be based on 1GHz. Please use agx_util to set p-state and set MPS_BENCHMARK_LOOP_PSTATE=value env var to let GRC backend know the value you are setting to so that correct cycle count can be computed using timestamp and frequency corresponding to p-state. Alternatively you can set MPS_BENCHMARK_LOOP_GRC_PSTATE=value env var and we will use GRC SPI to set p-state between start and stop sampling of GRC counters\n"
- "Width"
- "Workload total Without overhead cycle count standard deviation: %llu\n"
- "Workload total Without overhead cycle count: %llu\n"
- "Workload total with overhead cycle count standard deviation: %llu\n"
- "Workload total with overhead cycle count: %llu\n"
- "_MPSCommandBufferEncoderIDListKey"
- "_autoTuning"
- "_encoderSamples"
- "_pStatesInitialized"
- "_source"
- "_sourceGroup"
- "_sourceSampleMarker"
- "aggregatePerfSamples:commandBuffer:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "bundleWithURL:"
- "dictionaryWithObjects:forKeys:count:"
- "encoder: %lu cycle count standard deviation: %llu\n"
- "encoder: %lu cycle count: %llu\n"
- "enumerateObjectsUsingBlock:"
- "fileURLWithPath:isDirectory:"
- "i"
- "initWithObjects:count:"
- "isEnabled"
- "load"
- "numberWithUnsignedInt:"
- "objectForKey:"
- "pollCountersAtBufferIndex:withBlock:"
- "removeObjectForKey:"
- "requestCounters:firstErrorIndex:"
- "requestTriggers:firstErrorIndex:"
- "ringBufferNum"
- "sampleMarker"
- "selectWithName:options:"
- "selectedCounters"
- "setEnabled:"
- "setObject:forKey:"
- "setOptions:"
- "setPStateAndFrequency"
- "sourceList"
- "stopSampling"
- "subDivideCounterList:withOptions:"
- "unsignedIntegerValue"
- "userDictionary"
- "v32@?0@8Q16^B24"
- "v32@?0^Q8Q16Q24"

```
