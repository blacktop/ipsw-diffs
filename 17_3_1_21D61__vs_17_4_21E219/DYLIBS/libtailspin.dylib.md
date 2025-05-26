## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-162.3.0.0.0
-  __TEXT.__text: 0x1bc68
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__const: 0xa9
-  __TEXT.__cstring: 0x1550
-  __TEXT.__oslogstring: 0x1be0
-  __TEXT.__gcc_except_tab: 0xebc
+176.0.0.0.0
+  __TEXT.__text: 0x1e348
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__const: 0x91
+  __TEXT.__cstring: 0x180c
+  __TEXT.__oslogstring: 0x1ecc
+  __TEXT.__gcc_except_tab: 0x1048
   __TEXT.__ustring: 0x6
-  __TEXT.__unwind_info: 0x688
+  __TEXT.__dlopen_cstrs: 0x48
+  __TEXT.__unwind_info: 0x6fc
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x85a
-  __TEXT.__objc_stubs: 0xcc0
+  __TEXT.__objc_methname: 0x980
+  __TEXT.__objc_stubs: 0xe80
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__const: 0x890
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x330
-  __AUTH_CONST.__cfstring: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_classrefs: 0xd0
+  __AUTH_CONST.__cfstring: 0x1820
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x770
-  __DATA.__objc_classrefs: 0xc8
-  __DATA.__data: 0x8
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x798
+  __DATA.__data: 0x38
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x460
-  __DATA_DIRTY.__const: 0x260
+  __DATA.__bss: 0x480
+  __DATA_DIRTY.__const: 0x200
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x2188
+  __DATA_DIRTY.__bss: 0x2180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TailspinSymbolication.framework/TailspinSymbolication
   - /System/Library/PrivateFrameworks/kperfdata.framework/kperfdata
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 520
-  Symbols:   469
-  CStrings:  473
+  Functions: 552
+  Symbols:   488
+  CStrings:  534
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _TSPConfiguration_IsCswitchSamplingEnabledKey
+ _TSPConfiguration_IsSyscallSamplingEnabledKey
+ _TSPConfiguration_SamplingOptionsModifierKey
+ _TSPDumpOptions_CollectTrials
+ _TSPTaskingConfiguration_IsCswitchSamplingEnabledKey
+ _TSPTaskingConfiguration_IsSyscallSamplingEnabledKey
+ ___udivti3
+ __sl_dlopen
+ _mach_continuous_time
+ _objc_getClass
+ _objc_retain_x11
+ _objc_retain_x27
+ _objc_retain_x4
+ _tailspin_augment_output_with_request_id
+ _tailspin_sampling_option_get
+ _tailspin_sampling_option_set
+ _tailspin_sampling_options_clear
+ _tailspin_sampling_options_get_default
+ _tailspin_sampling_options_is_default
+ _tailspin_sampling_options_reset
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- _objc_retain_x26
CStrings:
+ "\t    sampling options               = "
+ "%s"
+ "%s (final size: %{bytes}lld)"
+ "%{public, signpost.description:begin_time}llu\nResult: %{bool}d\nos_signpost: %{bool}d\nos_log: %{bool}d\nscrub_data: %u"
+ "%{public, signpost.description:begin_time}llu\nSave for '%{public}s [%d] %s"
+ "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu numEvents=%{public,name=numEvents}llu enableTelemetry=YES "
+ ","
+ "Augment"
+ "Augment of tailspin for %{public}s [%d]"
+ "Augment_LoggingData"
+ "Augment_Symbolicate"
+ "Class getTRIAllocationStatusClass(void)_block_invoke"
+ "CswitchSamplingEnabledModifier"
+ "FAILED"
+ "Found %lu active trial experiments"
+ "Found %lu active trial rollouts"
+ "IsCswitchSamplingEnabled"
+ "IsSyscallSamplingEnabled"
+ "Min timestamp %.0fs before start of ktrace data, capping signpost/logs to 60s before"
+ "Min timestamp %.0fs before start of ktrace data, including signpost/logs from then"
+ "SUCCEEDED"
+ "SaveStandardChunks"
+ "Saved %{bytes}lld tailspin on behalf of %{public}s [%d]"
+ "Saved %{bytes}lld tailspin on behalf of %{public}s [%d] (augment failed)"
+ "TRIAllocationStatus"
+ "TailspinTaskedIsCswitchSamplingEnabled"
+ "TailspinTaskedIsSyscallSamplingEnabled"
+ "Unable to append trial dict: %{errno}d"
+ "Unable to determine active trial experiments: %@"
+ "Unable to determine active trial rollouts: %@"
+ "Unable to find class %s"
+ "Unable to gather trial info"
+ "Unable to serialize trial dict: %@"
+ "compatibilityVersion"
+ "cswitch-sampling"
+ "currentHandler"
+ "defaultProvider"
+ "deploymentId"
+ "deployment_id"
+ "enumerateActiveExperimentsForEnvironment:error:block:"
+ "enumerateActiveRolloutsWithError:block:"
+ "experimentId"
+ "experiment_id"
+ "experiments"
+ "factorPackIds"
+ "factor_pack_ids"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "libtailspin_client.m"
+ "namespace_ids"
+ "namespaces"
+ "none"
+ "rampId"
+ "ramp_id"
+ "rolloutId"
+ "rollout_id"
+ "rollouts"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Trial.framework/Trial"
+ "string"
+ "syscall-sampling"
+ "tailspin_dump_option_collect_trials"
+ "treatmentId"
+ "treatment_id"
+ "v16@?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}Q{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v}8"
+ "v24@?0@\"TRIExperimentAllocationStatus\"8^B16"
+ "v24@?0@\"TRIRolloutAllocationStatus\"8^B16"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "void *TrialLibrary(void)"
- "%{public, signpost.description:begin_time}llu numEvents=%{public,name=numEvents}llu enableTelemetry=YES "
- "%{public, signpost.description:end_time}llu"
- "KDENABLE sysctl failed"
- "Saved %{bytes}lld tailspin on behalf of %{public}s"
- "Saved %{bytes}lld tailspin on behalf of %{public}s (augment failed)"
- "v16@?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v}8"

```
