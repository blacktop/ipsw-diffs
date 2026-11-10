## AudioDSP

> `/System/Library/Components/AudioDSP.component/Contents/MacOS/AudioDSP`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-881.117.10.0.0
-  __TEXT.__text: 0x3b0ebc
-  __TEXT.__realtime: 0x16a690
-  __TEXT.__auth_stubs: 0x4040
-  __TEXT.__objc_stubs: 0x1740
-  __TEXT.__objc_methlist: 0x414
-  __TEXT.__const: 0xa44b0
-  __TEXT.__cstring: 0x359c8
-  __TEXT.__gcc_except_tab: 0x32ae8
-  __TEXT.__oslogstring: 0x342c5
-  __TEXT.__objc_methname: 0x13ce
+881.210.10.1.0
+  __TEXT.__text: 0x3c704c
+  __TEXT.__realtime: 0x17aaa8
+  __TEXT.__auth_stubs: 0x40f0
+  __TEXT.__objc_stubs: 0x1640
+  __TEXT.__objc_methlist: 0x424
+  __TEXT.__const: 0xa3f30
+  __TEXT.__cstring: 0x3618f
+  __TEXT.__gcc_except_tab: 0x33ca8
+  __TEXT.__oslogstring: 0x35482
+  __TEXT.__objc_methname: 0x1341
   __TEXT.__objc_classname: 0xf4
-  __TEXT.__objc_methtype: 0xadf
-  __TEXT.__unwind_info: 0x10620
+  __TEXT.__objc_methtype: 0xae4
+  __TEXT.__unwind_info: 0x10b88
   __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__const: 0x316a8
-  __DATA_CONST.__cfstring: 0x21220
+  __DATA_CONST.__const: 0x32170
+  __DATA_CONST.__cfstring: 0x210e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2030
+  __DATA_CONST.__auth_got: 0x2088
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x890
-  __DATA.__objc_selrefs: 0x6d8
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_const: 0x8b0
+  __DATA.__objc_selrefs: 0x698
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x2fc0
-  __DATA.__bss: 0x2b00
+  __DATA.__data: 0x3208
+  __DATA.__bss: 0x2b20
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11984
-  Symbols:   1325
-  CStrings:  11939
+  Functions: 12187
+  Symbols:   1336
+  CStrings:  12106
 
Symbols:
+ _CFDictionaryRemoveAllValues
+ _CFStringGetMaximumSizeForEncoding
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
+ __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
+ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj
+ __ZNSt3__127__from_chars_floating_pointIdEENS_19__from_chars_resultIT_EEPKcS5_NS_12chars_formatE
+ __ZNSt3__19to_stringEl
+ __os_log_fault_impl
+ _clock_gettime_nsec_np
+ _dispatch_retain
+ _localtime_r
CStrings:
+ " but AU was created with only "
+ " channels\n"
+ " channels are available"
+ " clamped to "
+ " elements but should have 2\n"
+ " elements, should have 4\n"
+ " filters and assigned them to group "
+ " filters were not imported.\n"
+ " greater than maximum ("
+ " less than minimum ("
+ " of "
+ "%25s:%-5d Requested batch size for NeuralNetCache (%u)."
+ "%25s:%-5d Saved implementation to cache for model %s (batch size %u)."
+ "%25s:%-5d shared mmap of BNNS IR file (%s) failed: %s; retrying MAP_PRIVATE (model pages will be charged to this process)"
+ "%s_%04d%02d%02d.%02d%02d%02d.vpdbg_ecv6.ecvdbg"
+ "' "
+ "' is not a valid 'chN' identifier, where N starts at 1"
+ "(I) CPU cycles per frame"
+ "(I) CPU instructions per frame"
+ "(I) CPU thread ns per frame"
+ "(I) EC last event: 0=none 1=reset 2=backup copy 3=fast init 4=LMS scaledown"
+ "(I) EC output-energy gate active (mic passthrough)"
+ "(I) ms since last EC event (see DualEcLastEvent)"
+ "(I) ms since output-energy gate last active"
+ ", but only "
+ ", but received "
+ ". "
+ "/tmp/AudioCapture/AUEchoCancelerV6"
+ "01:07:51"
+ "01:08:05"
+ "01:08:25"
+ "@28@0:8{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>={?=^{NeuralNetImpl}}}16I24"
+ "AUEchoCancelerV6"
+ "AUEchoCancelerV6::InitializeEC: mic %u init params differ from mic 0 — refChannelsToUse %d/%d multiChanECMode %d/%d blockSize %u/%u filterSize %u/%u ecInitConvergence %u/%u enableFast %u/%u"
+ "AUEchoCancelerV6UI.bundle"
+ "AUEchoCancelerV6_ViewFactory"
+ "AUEchoCancelerV6_cpu_logging"
+ "AUEchoCancelerV6_debug_dir"
+ "AUEchoCancelerV6_debug_dur_sec"
+ "AULoudspeakerSystemIDV2::Initialize failed — algorithm is null"
+ "AUMonopoly"
+ "AUMonopolyViewFactory"
+ "Apple: AUMonopoly"
+ "AudioUnitsUI.bundle"
+ "Ch0MimoPairedDriver"
+ "Ch1MimoPairedDriver"
+ "Ch2MimoPairedDriver"
+ "Ch3MimoPairedDriver"
+ "Ch4MimoPairedDriver"
+ "Ch5MimoPairedDriver"
+ "Ch6MimoPairedDriver"
+ "Ch7MimoPairedDriver"
+ "Crop: Copped filter length for long filter lens"
+ "DualEC epsEcErrorMin"
+ "DualEC minAdaptDoingOk"
+ "DualEC minAdaptInSingletalk"
+ "DualEC minAdaptOverBackup"
+ "DualEC minEchoLevelToCheck"
+ "DualEC minHangTime"
+ "ECv6: partial mic processing nProcMics=%u mNumMics=%u (micChans=%u outChans=%u); higher mics will stale"
+ "ECv6DBG\n"
+ "Error dynamic EQ: missing key '"
+ "Error for filter "
+ "Fast"
+ "FastEC: 0=off,1=initConv,2=reConv,3=+rCal"
+ "FilterSize"
+ "FormatVersion"
+ "Frequency "
+ "Frequency array has "
+ "Frequency of "
+ "Gain of "
+ "HOABuses"
+ "IRs"
+ "Init Convergence"
+ "Linear EC"
+ "MIMOCoupledModel_typeA"
+ "MIMOCoupledModel_typeB"
+ "MIMOCoupledModel_typeC"
+ "Master Volume in dB"
+ "MimoCompensationEnable"
+ "MimoCompensationMaxFcRatio"
+ "MimoCompensationMaxQRatio"
+ "MimoCompensationSd_cm2"
+ "MimoCompensationTargetMode"
+ "MimoCompensationTargetQ"
+ "MimoCompensationVbox_cm3"
+ "MimoEnable"
+ "MimoErrorThreshold"
+ "MimoFitMaxFreqHz"
+ "MimoFitMinFreqHz"
+ "MimoFitNumBins"
+ "MimoPairedDrivers"
+ "MimoSdActiveDriver_cm2"
+ "MimoSmoothingTimeConstant_s"
+ "MimoVboxStatic_cm3"
+ "Missing key: Filters\n"
+ "Multi-Chan + Poly EC"
+ "Multi-Chan EC"
+ "Multi-chan EC mode: 0-LinearEC, 2-MultiChanEC"
+ "NeuralNetImplLoadFromCache: cached batch size (%u) does not match requested batch size (%u) -- discarding stale entry."
+ "NoiseGate registered successfully"
+ "NoiseGate registration failed"
+ "NumMics"
+ "NumParallelSpeakers"
+ "NumRefs"
+ "Oct 10 2026"
+ "Order of "
+ "Poly EC"
+ "Quality of "
+ "RTDebugLogger"
+ "RTDebugLogger.cpp"
+ "RTDebugLogger: ring buffer would be %zu MB (cap 8 MB) — reduce registered slots or filter length"
+ "RdcTolerancePercent"
+ "Re-Convergence"
+ "Re-Convergence + Rate Cal"
+ "Ref"
+ "Register"
+ "Register NoiseGate"
+ "Scotty Center Gain"
+ "Scotty Gain Factor"
+ "SetProperty( kAudioUnitProperty_DspLibDictionary ) Error: data did not decode to a dictionary property list\n"
+ "StaticCreepModelQ"
+ "Successfully imported "
+ "Unknown filter type: "
+ "[%s|%s] AUMonopoly does not support multiple LFEs - Duplicate LFE label"
+ "[%s|%s] AUMonopoly does not support multiple center channels - Duplicate center label"
+ "[%s|%s] AUMonopoly does not support non-symmetric channel layouts as defined by channel labels"
+ "[%s|%s] AUSMListenerPosition: LeftRight: %.4f, BackFront: %.4f, DownUp: %.4f"
+ "[%s|%s] Can not set ACLT when AU is initialized"
+ "[%s|%s] Can not set FFT size when AU is initialized"
+ "[%s|%s] Can not set OutOfPhase when AU is initialized"
+ "[%s|%s] FFT size set to %u"
+ "[%s|%s] Invalid FFT size - must be power of 2"
+ "[%s|%s] No default channel layout for %u input channels"
+ "[%s|%s] Number of input channels inconsistent with number of labels for layout = %u (%s)"
+ "[%s|%s] Only Input ACL can be set - output is always mono"
+ "[%s|%s] Setting input channel layout tag = %u (%s)"
+ "[%s|%s] Setting input channel layout tag = %u (%s) failed - number of channels in layout (%u) is inconsistent with number of input channels (%u)"
+ "[%s|%s] Using default input channel layout tag = %u (%s)"
+ "[ECv6] DrainPendingIRs: mic=%u pending size %zu is not a multiple of refChannelsToUse=%zu; skipping"
+ "[ECv6] DrainPendingIRs: mic=%u per-channel length mismatch: pending=%zu, initialized=%zu; rejecting import"
+ "[ECv6] DrainPendingIRs: mic=%u refChannelsToUse=%d; skipping"
+ "[ECv6] DrainPendingIRs: mic=%u setMainIr rejected a %zu-sample-per-channel import that passed the length check"
+ "[ECv6] DrainPendingIRs: pending mic count (%zu) != initialized mic count (%u); applying overlap only"
+ "[ECv6] GetProperty(CocoaUI): AudioUnitsUI.bundle has no PlugIns URL"
+ "[ECv6] GetProperty(CocoaUI): AudioUnitsUI.bundle not found at expected PlugIns path"
+ "[ECv6] GetProperty(CocoaUI): DSPAudioUnitBundle has no PlugIns URL"
+ "[ECv6] GetProperty(CocoaUI): DSPAudioUnitBundle not found by identifier"
+ "[ECv6] GetProperty(CocoaUI): failed to absolutize the AUEchoCancelerV6UI.bundle URL"
+ "[ECv6] GetProperty(CocoaUI): failed to append AUEchoCancelerV6UI.bundle to inner PlugIns URL"
+ "[ECv6] GetProperty(CocoaUI): failed to append AudioUnitsUI.bundle to PlugIns URL"
+ "[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] (Mic=%u Ref=%u) Coefficients size mismatch: got %ld bytes, expected %zu; skipping"
+ "[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] (Mic=%u Ref=%u) missing/invalid Coefficients; skipping"
+ "[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] Mic=%u Ref=%u out of bounds (NumMics=%u NumRefs=%u); skipping"
+ "[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] is not a dict; skipping"
+ "[ECv6] LoadPendingIRsFromDictionary: IRs[%ld] missing Mic/Ref; skipping"
+ "[ECv6] LoadPendingIRsFromDictionary: header exceeds bounds (NumMics=%u NumRefs=%u FilterSize=%u; max mics=%u, max refs=%u, max filterSize=%u)"
+ "[ECv6] LoadPendingIRsFromDictionary: missing or non-array \"IRs\" key"
+ "[ECv6] LoadPendingIRsFromDictionary: missing/invalid NumMics/NumRefs/FilterSize (got NumMics=%u NumRefs=%u FilterSize=%u)"
+ "[ECv6] LoadPendingIRsFromDictionary: unsupported FormatVersion=%u (expected 1)"
+ "[ECv6] LoadPendingIRsFromDictionary: zero-valued header (NumMics=%u NumRefs=%u FilterSize=%u)"
+ "[ECv6] SetProperty(ECIR) rejected: AU already initialized (mic=%u)"
+ "[ECv6] SetProperty(ECIR) rejected: inData==nullptr (mic=%u)"
+ "[ECv6] SetProperty(ECIR) rejected: inDataSize=%u not a positive multiple of sizeof(float) (mic=%u)"
+ "[ECv6] SetProperty(ECIR) rejected: inElement=%u exceeds kAUEchoCancelerV6_MaxMics=%u"
+ "[ECv6] SetProperty(InitializeIR) rejected: AU already initialized"
+ "[ECv6] SetProperty(InitializeIR) rejected: inData=%p inDataSize=%u (expected >=%zu)"
+ "[ECv6] SetProperty(InitializeIR) rejected: value is not a CFDictionaryRef"
+ "[ECv6_CPU] cycles=%llu instructions=%llu ns=%llu"
+ "_batchSize"
+ "adapted"
+ "attempting to assign a filter to channel: "
+ "attempting to assign a global parameter to channel "
+ "batchSize"
+ "blockIREnergies"
+ "blockProp"
+ "ch"
+ "channel key '"
+ "constrainedIREnergies"
+ "could not find key :Channels"
+ "cropEndIndex"
+ "cropStartIndex"
+ "deltaIR"
+ "echoEstMagImag"
+ "echoEstMagReal"
+ "false && \"RTDebugLogger::Register called after Allocate; frame layout is frozen\""
+ "filter entry is not a dictionary"
+ "filterImagSum"
+ "filterRealSum"
+ "getDefaultInputACL"
+ "initWithImpl:batchSize:"
+ "irEnergy"
+ "key '0' not found"
+ "leakEst"
+ "maskDictionary is empty"
+ "maskDictionary is invalid"
+ "micEchoEstXcorr"
+ "missing key Channels"
+ "missing key: Frequency\n"
+ "missing key: Gain\n"
+ "missing key: GainRange\n"
+ "missing key: Order\n"
+ "missing key: Quality\n"
+ "parseDictionary() Error: mainCurve element %u is not numeric"
+ "parseDictionary() Error: value for key '%@' is not an array"
+ "parseTwoPointCurve() Error: expected two numeric values"
+ "pey"
+ "pyy"
+ "refEnergy"
+ "replacedBackup"
+ "report geometry for this bus to the GUI"
+ "rer"
+ "samplerate key not found"
+ "samplerate mismatch"
+ "scaleDown"
+ "sdd"
+ "see"
+ "smoothWeight2"
+ "smoothWeight3"
+ "stepSize"
+ "string_view::substr"
+ "syy"
+ "unspecified error"
+ "wrong mask size. expected "
- "%25s:%-5d Saved implementation to cache for model %s."
- "%25s:%-5d mlock of BNNS IR file (%s) failed: %s; page faults may occur on IO thread"
- "%d filters were not imported.\n"
- "%lu"
- "17:54:42"
- "17:54:54"
- "17:55:16"
- "@24@0:8{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>={?=^{NeuralNetImpl}}}16"
- "AULoudspeakerSystemIDV2::Initialize failed — algorithm is null (gInstanceCounter=%u)"
- "Aug  8 2026"
- "Error dynamic EQ: missing key '%@' "
- "Error for filter %d: %@"
- "Frequency 0 of %f greater than maximum (%f)\n"
- "Frequency 0 of %f less than minimum (%f)\n"
- "Frequency 1 of %f greater than maximum (%f)\n"
- "Frequency 1 of %f less than minimum (%f)\n"
- "Frequency 2 of %f greater than maximum (%f)\n"
- "Frequency 2 of %f less than minimum (%f)\n"
- "Frequency 3 of %f greater than maximum (%f)\n"
- "Frequency 3 of %f less than minimum (%f)\n"
- "Frequency array has %lu elements but should have 2\n"
- "Frequency array has %lu elements, should have 4\n"
- "Frequency of %f greater than maximum (%f)\n"
- "Frequency of %f less than minimum (%f)\n"
- "Gain of %f greater than maximum (%f)\n"
- "Gain of %f less than minimum (%f)\n"
- "Missing key: %@\n"
- "Order of %f greater than maximum (%f)\n"
- "Order of %f less than minimum (%f)\n"
- "Quality of %f clamped to %f."
- "Successfully imported %lu filters and assigned them to group %d. "
- "Unknown filter type: %@\n"
- "attempting to assign a global parameter to channel %ld but AU was created with only %u channels\n"
- "attempting to assing a filter to channel: %ld, but only %d channels are available"
- "cStringUsingEncoding:"
- "channel number = 0, but channel enumeration starts with channel 1"
- "could not find key :%@"
- "indexOfObject:"
- "initWithImpl:"
- "integerValue"
- "key 'mask' not found\n"
- "maskDictionary is NULL"
- "maskDictionary is empty\n"
- "maskDictionary is not a dictionary"
- "missing key %@"
- "missing key: %@\n"
- "nil message"
- "numberWithInteger:"
- "numberWithUnsignedLong:"
- "parseDictionary() Error: array expected"
- "removeAllObjects"
- "samplerate key not found\n"
- "samplerate mismatch\n"
- "setValue:forKey:"
- "stringByAppendingString:"
- "substringFromIndex:"
- "wrong mask size. expected %lu, but received %lu."
```
