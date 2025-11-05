## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/Versions/A/MetricMeasurement`

```diff

-259.40.2.0.0
-  __TEXT.__text: 0x1b6cc
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x22b8
+261.0.0.0.0
+  __TEXT.__text: 0x1d188
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0x265c
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x1ffd
-  __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__oslogstring: 0x76d
+  __TEXT.__cstring: 0x2196
+  __TEXT.__gcc_except_tab: 0x4b8
+  __TEXT.__oslogstring: 0x7ef
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x56d
   __TEXT.__objc_methname: 0x4493
   __TEXT.__objc_methtype: 0xf6a

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x13e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__cfstring: 0x2280
-  __AUTH_CONST.__objc_const: 0x5b90
+  __AUTH_CONST.__objc_const: 0x5588
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0xd70
   __DATA.__objc_ivar: 0x15c
   __DATA.__data: 0x780
-  __DATA.__bss: 0x2c8
+  __DATA.__bss: 0x2f0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 7C396A62-E4BB-3744-BEE1-BD7D79287A4D
-  Functions: 740
-  Symbols:   2120
-  CStrings:  1713
+  UUID: D0432300-77F9-37D3-AE00-8827478A0D8C
+  Functions: 826
+  Symbols:   2232
+  CStrings:  1732
 
Symbols:
+ +[MXMMachUtils _timebase].cold.1
+ +[MXMOSLogDeviceStore_Internal shared].cold.1
+ -[MXMCPUMetric harvestData:error:].cold.1
+ -[MXMCPUMetric harvestData:error:].cold.2
+ -[MXMCPUMetric harvestData:error:].cold.3
+ -[MXMCPUMetric harvestData:error:].cold.4
+ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.1
+ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.2
+ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.3
+ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.4
+ -[MXMInstrument _setupAndRunWithIteration:spawnThread:attrs:pthread:returnCode:].cold.5
+ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.1
+ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.2
+ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.3
+ -[MXMInstrument _transitionWithState:iteration:instrumentals:].cold.4
+ -[MXMInstrument initWithInstrumentals:].cold.1
+ -[MXMInstrument measureAutomatically:options:block:].cold.1
+ -[MXMInstrument measureAutomatically:options:block:].cold.2
+ -[MXMInstrument measureAutomatically:options:block:].cold.3
+ -[MXMInstrument measureAutomatically:options:block:].cold.4
+ -[MXMInstrument measureAutomatically:options:block:].cold.5
+ -[MXMInstrument measureAutomatically:options:block:].cold.6
+ -[MXMInstrument measureAutomatically:options:block:].cold.7
+ -[MXMInstrument startWithError:].cold.1
+ -[MXMInstrument stopWithError:].cold.1
+ -[MXMInstrument stopWithError:].cold.2
+ -[MXMMetric didStopAtContinuousTime:absoluteTime:stopDate:].cold.1
+ -[MXMMetric didStopAtTime:stopDate:].cold.1
+ -[MXMMetric harvestData:error:].cold.1
+ -[MXMMetric harvestData:error:].cold.2
+ -[MXMMetric harvestData:error:].cold.3
+ -[MXMMetric harvestData:error:].cold.4
+ -[MXMMetric harvestData:error:].cold.5
+ -[MXMMetric willStartAtEstimatedTime:].cold.1
+ -[MXMMutableSampleData appendDoubleValue:tag:timestamp:].cold.1
+ -[MXMMutableSampleData appendFloatValue:tag:timestamp:].cold.1
+ -[MXMMutableSampleData appendIntValue:tag:timestamp:].cold.1
+ -[MXMMutableSampleData appendIntegerValue:tag:timestamp:].cold.1
+ -[MXMMutableSampleData appendUnsignedIntValue:tag:timestamp:].cold.1
+ -[MXMMutableSampleData appendUnsignedIntegerValue:tag:timestamp:].cold.1
+ -[MXMMutableSampleSet appendSample:].cold.1
+ -[MXMMutableSampleSet appendSet:].cold.1
+ -[MXMOSSignpostMetric _constructProbe].cold.1
+ -[MXMOSSignpostMetric _constructProbe].cold.2
+ -[MXMOSSignpostProbe _beginUpdates].cold.1
+ -[MXMProbeDisplay initWithDescriptor:].cold.1
+ -[MXMProbeDisplay initWithDescriptor:].cold.2
+ -[MXMProbeDisplay initWithDescriptor:].cold.3
+ -[MXMProxyMetric _sampleMode].cold.1
+ -[MXMResourceProbe _buildData:timestamp:rusage:].cold.1
+ -[MXMResourceProbe _pollAllProcesses:].cold.1
+ -[MXMResourceProbe _pollBasicTaskInformation:pid:].cold.1
+ -[MXMResourceProbe _pollTaskMachPortInformation:task:].cold.1
+ -[MXMResourceProbe _stopUpdates].cold.1
+ -[MXMSampleAttribute initWithAttributeName:valueType:value:].cold.1
+ -[MXMSampleAttribute initWithAttributeName:valueType:value:].cold.2
+ -[MXMSampleAttribute initWithAttributeName:valueType:value:].cold.3
+ -[MXMSampleAttribute isEqualToAttribute:].cold.1
+ -[MXMSampleSet _appendAttribute:].cold.1
+ -[MXMSampleSet(Stats) distance].cold.1
+ -[MXMSampleTag isEqualToTag:].cold.1
+ -[MXMSampleTimeSeries initWithContinuousTimeSeries:length:].cold.1
+ -[MXMSystemProbe _pollProcessorLoadInformationWithData:].cold.1
+ -[MXMSystemProbe _pollProcessorLoadInformationWithData:].cold.2
+ -[MXMSystemProbe _pollSystemHostProcessorInfoWithData:].cold.1
+ -[MXMSystemProbe _pollSystemLoadInformationWithData:].cold.1
+ _MXMGetInstrumentsLog.cold.1
+ _MXMGetLog.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __60-[MXMProbe updateNowUntilTimeout:updateHandler:stopHandler:]_block_invoke.cold.1
+ __62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.1
+ __62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.2
+ __62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.3
+ __62-[MXMInstrument _transitionWithState:iteration:instrumentals:]_block_invoke.cold.4
+ __MergedGlobals
+ ___assert_rtn
+ ___isOSVersionAtLeast
+ ___isPlatformOrVariantPlatformVersionAtLeast
+ ___isPlatformVersionAtLeast
+ __availability_version_check
+ __initializeAvailabilityCheck
+ __isOSVersionAtLeast.cold.1
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.1
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.2
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.3
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.4
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_once_f
+ _dlsym
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _initializeAvailabilityCheck
+ _malloc
+ _rewind
+ _sscanf
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "MXMTerminateBeforeIteration is not available for this OS version."
+ "MXMUncacheBeforeIteration is not available for this OS version."
+ "Platform2 == PLATFORM_MACOS && \"unexpected platform\""
+ "ProductVersion"
+ "__isPlatformOrVariantPlatformVersionAtLeast"
+ "kCFAllocatorNull"
+ "os_version_check.c"
+ "r"

```
