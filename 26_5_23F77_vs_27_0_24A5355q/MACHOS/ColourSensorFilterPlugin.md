## ColourSensorFilterPlugin

> `/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin`

```diff

-2079.120.10.0.0
-  __TEXT.__text: 0x14690
-  __TEXT.__auth_stubs: 0x930
-  __TEXT.__const: 0x4a0
-  __TEXT.__cstring: 0x12bb
-  __TEXT.__oslogstring: 0x1d2f
-  __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x8c0
+2285.0.0.502.1
+  __TEXT.__text: 0x36f24
+  __TEXT.__auth_stubs: 0x1350
+  __TEXT.__const: 0x1f18
+  __TEXT.__cstring: 0x280b
+  __TEXT.__oslogstring: 0x2144
+  __TEXT.__gcc_except_tab: 0x9c8
+  __TEXT.__constg_swiftt: 0xad8
+  __TEXT.__swift5_typeref: 0x688
+  __TEXT.__swift5_reflstr: 0xd6f
+  __TEXT.__swift5_fieldmd: 0x1168
+  __TEXT.__objc_classname: 0x25c
+  __TEXT.__swift5_types: 0x108
+  __TEXT.__swift5_proto: 0xd0
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__objc_methname: 0x98
+  __TEXT.__objc_methtype: 0x1
+  __TEXT.__swift5_builtin: 0x1f4
+  __TEXT.__swift5_mpenum: 0x24
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0xc80
+  __TEXT.__eh_frame: 0xf88
+  __DATA_CONST.__const: 0x8ab9
+  __DATA_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x80
-  __DATA.__bss: 0xb0
+  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__auth_ptr: 0x1d8
+  __DATA.__objc_const: 0x860
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0xc70
+  __DATA.__bss: 0x1760
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: DD19F44E-FD3D-3D2C-A737-984CC182CDF1
-  Functions: 280
-  Symbols:   315
-  CStrings:  465
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: A3CC9E63-30DB-3483-ABB5-448971FFE6B2
+  Functions: 1145
+  Symbols:   417
+  CStrings:  648
 
Symbols:
+ _CBU_GetCoreBrightnessNode
+ _CBU_IsAABCappingEnabled
+ _CBU_IsCoexTrackerEnabled
+ _CBU_IsVirtualMachine
+ _CFDictionaryGetTypeID
+ _GetCFBooleanValue
+ _IOHIDEventAppendEvent
+ _IOHIDEventCreateVendorDefinedEvent
+ _MGIsDeviceOfType
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Z12rescaleColorPff
+ __ZN10VD6287HmCl11processBlobEhhPKhPjP21VD6287CalibrationBlobP8Matrices
+ __ZN10VD6287HmCl12processColorEhhPK14HmClBlob_colorP21VD6287CalibrationBlob
+ __ZN10VD6287HmCl12processXtalkEhhPK10AlsHtoHmClP21VD6287CalibrationBlob
+ __ZN10VD6287HmCl13processBlobODEhhPKhPjP21VD6287CalibrationBlobP8Matrices
+ __ZN10VD6287HmCl5matchEPK8__CFDataPjS3_
+ __ZN17ColorSensorPlugIn12ackIsEnabledEv
+ __ZN17ColorSensorPlugIn18ackLoadCalibrationEb
+ __ZN17ColorSensorPlugIn18isALSSpikeDetectedE26ColorSensorVendorEventData27eChannelRatioMitigationType9eChipType14eALSSensorType
+ __ZN17ColorSensorPlugIn20loadColorCalibrationEPK8__CFDataPK11t_HmCalDataiPKN24ColourSensorFilterPlugin31ProcessedCalibrationSpectrumCxxEb
+ __ZN17ColorSensorPlugIn20overrideChromaticityEP12__IOHIDEvent
+ __ZN17ColorSensorPlugIn27ackLoadProcessedCalibrationEPN24ColourSensorFilterPlugin29ProcessedCalibrationBundleCxxEb
+ __ZN17ColorSensorPlugIn29ackSideLoadHmSplitCalibrationEPK8__CFDataS2_
+ __ZN17ColorSensorPlugIn32copyDataFromCalibrationInstancesEPK10__CFStringPK9__CFArrayiRjS6_Ry
+ __ZN17ColorSensorPlugIn37ackSetMatricesFromSpectrumCalibrationEPKN24ColourSensorFilterPlugin31ProcessedCalibrationSpectrumCxxEP8Matrices
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
+ __ZNSt3__16ranges5__cpo7find_ifE
+ __ZTISt20bad_array_new_length
+ ___assert_rtn
+ __objc_empty_cache
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_exceptionPersonality
+ _abort
+ _cblas_dgemm$NEWLAPACK$ILP64
+ _clock_gettime_nsec_np
+ _dgesdd$NEWLAPACK$ILP64
+ _log2f
+ _mach_time_to_microseconds
+ _malloc_size
+ _malloc_type_posix_memalign
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retain
+ _objc_retain_x21
+ _objc_retain_x22
+ _pow
+ _sanitize_brightness
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getEnumCaseMultiPayload
+ _swift_getForeignTypeMetadata
+ _swift_getMetatypeMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _swift_willThrowTypedImpl
+ _vDSP_mtransD
- __Z10printUsagev
- __Z25mach_time_to_microsecondsy
- __ZN10VD6287HmCl11processBlobEPK8HmClDataPKhPjP21VD6287CalibrationBlobP8Matrices
- __ZN10VD6287HmCl12processColorEPK8HmClDataPK14HmClBlob_colorP21VD6287CalibrationBlob
- __ZN10VD6287HmCl12processXtalkEPK8HmClDataPK10AlsHtoHmClP21VD6287CalibrationBlob
- __ZN10VD6287HmCl13processBlobODEPK8HmClDataPKhPjP21VD6287CalibrationBlobP8Matrices
- __ZN10VD6287HmCl5matchEPK8__CFData
- __ZN17ColorSensorPlugIn32copyDataFromCalibrationInstancesEPK10__CFStringPK9__CFArrayiRhS6_Ry
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- _dispatch_after
- _dispatch_time
- _exit
- _fclose
- _fopen
- _fread
- _mach_absolute_time
- _main
CStrings:
+ " != bRowsAltered="
+ " => fdrDataArray="
+ " CFSN matching is disallowed! Let's resort to R2R."
+ " Calibration num_blobs="
+ " Calibration source is missing!"
+ " Calibration source is not FDR! Will not proceed!"
+ " Could not create ALSManifest! Bad input: placement="
+ " Did not find any bundle with matching CFSN!"
+ " FDR service is missing!"
+ " Failed to get async blob"
+ " Failed to get sync blob"
+ " Failed to obtain HmCn bundles!"
+ " Failed to obtain HmDt bundles!"
+ " Failed to process async blob"
+ " Failed to process sync blob"
+ " Filtering training data: Kept "
+ " Found dataClass="
+ " HmCA version = "
+ " HmCl version = "
+ " HmCn has only hmCnPtr.count="
+ " HmCn magic not found!"
+ " HmDt has only hmDtPtr.count="
+ " HmDt magic not found!"
+ " Incompatible versions."
+ " Magic not found!"
+ " Matched on CFSN: bundle="
+ " Matched on orientation and placement: bundle="
+ " No FDR service!"
+ " No bundle was matched!"
+ " No bundle was matched! Let's use the first available one: bundle="
+ " No bundles were provided!"
+ " No light sources in the training data fall within the [2400, 7000] K CCT range."
+ " Unexpected calibration blob type "
+ " Unexpected num_channels/num_gains!"
+ " Unexpected num_gains!"
+ " Unexpected number of xtalk nits "
+ " Unexpected orientation!"
+ " Unexpected placement!"
+ " Unexpected size = "
+ " Unexpected size: "
+ " Unexpected version: "
+ " Unrecognized CFSN!"
+ " Unrecognized orientation!"
+ " Unrecognized placement!"
+ " Unrecognized sensor type!"
+ " [FDR] dataClass="
+ " bundlesForDataClass="
+ " calibrationSource="
+ " calibrationTypes="
+ " compatibleBundles="
+ " dataClassSubCCs="
+ " failed for all formats: "
+ " failed with error: "
+ " subCCs is empty!"
+ "%s%s"
+ ", "
+ "ALS orientation mismatch"
+ "ALS placement mismatch"
+ "ALSCalibrationKit/ACKExtensions.swift"
+ "ALSCalibrationKit/ALCl.swift"
+ "ALSCalibrationKit/CalibrationProvider.swift"
+ "ALSCalibrationKit/FDRServiceUserspace.swift"
+ "ALSCalibrationKit/HmCA.swift"
+ "ALSCalibrationKit/HmCl.swift"
+ "ALSCalibrationKit/HmSplit.swift"
+ "ALSCalibrationKit/MatrixOperations.swift"
+ "ALSCalibrationKit/MatrixOperationsUserspace.swift"
+ "ALSCalibrationKit/TrainingLightsProviderUserspace.swift"
+ "ALSCalibrationKit/Utils.swift"
+ "AmbientLightSensorSplitCalibration"
+ "AppleSPUVL628"
+ "BlueLightReductionSupported"
+ "CBUtilities.h"
+ "Calibration contains invalid data"
+ "CalibrationBundle("
+ "ColourSensorFilterPlugin/CalibrationProviderCxx.swift"
+ "Comb"
+ "Comparison failed: delta="
+ "DeriveCCTCoefficients(multipliedSpectrums:trainingLights:outCalBlob:)"
+ "Empty matrix provided."
+ "FDR calibration data length = "
+ "Failed to fetch training spectrum."
+ "Failed to get base address of calibration blob"
+ "Fatal error"
+ "FetchProcessedCalibration(sensorType:placement:orientation:)"
+ "FetchVersion(dataPtr:)"
+ "FetchVersion(hmCnPtr:hmDtPtr:)"
+ "HmCn"
+ "HmD2"
+ "HmD3"
+ "HmDt"
+ "IODeviceTree:/core-brightness"
+ "Initializing channel-wise MA filter with thresholds: %s"
+ "Internal processing error"
+ "Invalid matrix provided: data.count="
+ "Invalid matrix provided: the number of columns is not consistent."
+ "IsVirtualDevice"
+ "Matrix index out of bounds: ("
+ "Mismatched type ("
+ "Moving average thresholds count %zu does not correspond to ALS channel count %d. Possibly a typo in EDT?"
+ "Multiply(a:aTranspose:b:bTranspose:)"
+ "Non matching size in header "
+ "ProbeInternal(_:)"
+ "Process(hmCnData:hmDtData:sensorCal:syncSpectrumCal:)"
+ "ProcessBlob(hmCnBlob:hmDtBlob:trainingLights:outCalBlob:outSpectrum:setOutSpectrum:)"
+ "ProcessCalibration(hmCn:hmDt:)"
+ "ProcessInternal(_:)"
+ "Received nil HID event"
+ "Received non-ALS HID event"
+ "Returned a failure."
+ "SVD failed with code: "
+ "SVD failed: unexpected info="
+ "Some data in calibration blob is incompatible"
+ "Split bundles do not match"
+ "Unexpected calibration size - %lu"
+ "Unexpected channel num."
+ "Unexpected gain num."
+ "Unexpected num nits."
+ "Unexpected size (expected: "
+ "Unexpected size of HmCnData. Expected "
+ "Unexpected size of HmDtData. Expected "
+ "Unexpected spectrum shape!"
+ "Unexpected version: major="
+ "Unrecognized CFSN"
+ "Unrecognized bundle"
+ "Unrecognized sensor orientation: "
+ "Unrecognized sensor placement: "
+ "Unrecognized sensorType="
+ "Unrecognized version"
+ "[%s] Channel num mismatch!"
+ "[%s] Failed to load color calibration!"
+ "[%s] Failed to send calibration to ALS!"
+ "[%s] HmCl placement=%u orientation=%u"
+ "[%s] Processed calibration has been successfully loaded!"
+ "[%s] Spectrum calibration does not contain any samples!"
+ "[%s] Successfully loaded color calibration!"
+ "[%s] [ALSCalibrationKit] forceDBUpdate=%d _sensorType=%u _placement=%u _orientation=%u"
+ "[%s] [ALSCalibrationKit] success=%d"
+ "[%s] [SplitCal]"
+ "[%s] [SplitCal] success=%d"
+ "[%s] _nChannels=%d is unexpected!"
+ "[%s] _nChannelsForColorCalc=%d is unexpected!"
+ "[%s] _service is nullptr!"
+ "[%s] hmCnData is nullptr"
+ "[%s] hmDtData is nullptr"
+ "[%s] luxCoeffs.getCount() = %td != _nChannels = %u"
+ "[%s] spectrumCal/m is nullptr"
+ "[%s] spectrumCalSamples.getCount() = %td != totalSamplesCnt = %zu"
+ "[Callback] Unexpected args."
+ "[Callback] nSamples="
+ "[SplitCalibration]"
+ "[SplitCalibration] Bad input!"
+ "[SplitCalibration] Bad input! Could not find HmCn or HmDt!"
+ "[SplitCalibration] Bad input! hmCnRef/hmDtRef is not CFData!"
+ "] Could not find subCC="
+ "] Failed to copy bundles. Error="
+ "] Probe failed with err="
+ "] Probe succeeded!"
+ "] [SealingManifest] Failed!"
+ "] [SealingManifest] Failed! Error: "
+ "] [SealingManifest] Succeeded! Instances: "
+ "] [SealingMap] Failed!"
+ "] [SealingMap] Failed! Error: "
+ "] [SealingMap] Succeeded! Instances: "
+ "_"
+ "_TtC17ALSCalibrationKit12TimeProfiler"
+ "_TtC17ALSCalibrationKit15CalibrationHmCA"
+ "_TtC17ALSCalibrationKit15CalibrationHmCl"
+ "_TtC17ALSCalibrationKit16MatrixOperations"
+ "_TtC17ALSCalibrationKit19CalibrationProvider"
+ "_TtC17ALSCalibrationKit19FDRServiceUserspace"
+ "_TtC17ALSCalibrationKit22TrainingLightsProvider"
+ "_TtC17ALSCalibrationKit3Log"
+ "_TtC17ALSCalibrationKit3Tag"
+ "_TtC17ALSCalibrationKit5Utils"
+ "_TtC17ALSCalibrationKit7HmSplit"
+ "_TtC17ALSCalibrationKitP33_57B019D70B6B7205195567934E0800755OSLog"
+ "_TtC24ColourSensorFilterPlugin22CalibrationProviderCxx"
+ "ackLoadCalibration"
+ "ackLoadProcessedCalibration"
+ "ackSetMatricesFromSpectrumCalibration"
+ "ackSideLoadHmSplitCalibration"
+ "alsSpectrum - All values are zero!"
+ "calibrationSource"
+ "calibrationTypes"
+ "cctCoefficients - nil"
+ "cctCoefficients - unexpected shape="
+ "com.apple.CoreBrightness.ALSCalibrationKit"
+ "copyDataFromCalibrationInstances"
+ "copyFDR3Data(dataClass:subCCs:)"
+ "copyFDRInstances(dataClass:skipSealingManifestCopy:skipSealingMapCopy:)"
+ "data.size() > 0"
+ "displaySpectrum - All values are zero!"
+ "exbright_log_mask"
+ "fdrService"
+ "fetchCalibrationBundles()"
+ "fetchHmSplitCalibrationBundles()"
+ "fetchStandaloneCalibrationBundles()"
+ "fetchVersion(dataPtr:)"
+ "file"
+ "fileLine"
+ "filtered"
+ "findMatchingBundle(alsManifest:bundles:)"
+ "init(placement:orientation:cfsn:sensorType:)"
+ "loadColorCalibration"
+ "logger"
+ "luxCoeffs - failed"
+ "luxCoeffs - unexpected shape="
+ "lux_coefficient="
+ "ma-channel-thr"
+ "multipliedSpectrums - nil"
+ "multipliedSpectrums - pinv failed"
+ "name"
+ "outCalBlob.cct_coefficient="
+ "percentage - nil"
+ "percentagePinv - failed"
+ "processHmClBlobHeader(header:outputCalibration:)"
+ "processHmClBlobXtalk(versionMajor:versionMinor:xtalk:outputCalibration:)"
+ "r2rPathEnforced"
+ "reconstructedSpectrum - failed"
+ "reconstructedSpectrumT - failed"
+ "startNs"
+ "stopped"
+ "trainingLightsInternal.lux.count="
+ "trainingLightsInternal.samples.count="
+ "trainingSpectrum - nil"
+ "wl_start_nir mismatch"
+ "wl_start_visible mismatch"
+ "wl_step mismatch"
+ "xyz - unexpected shape="
- "\tch%d: "
- "\nCalibration Types: [HmCA10]"
- "\nCurrently only supports HmCA 10.0"
- "\norientation:                      0x%02X\n"
- "\nplacement:                      0x%02X\n"
- "\nsource:           %d\n"
- "%c%c%c%c v%d.%d loaded\n"
- "%d\t"
- "%f\t"
- "%lf\t"
- "--h"
- "--help"
- "-help"
- "-parse"
- "-print"
- "ALSCalibraitonData calibration data length = %ld (nChannels = %d)\n"
- "Bridge OS"
- "F1Xz9g1JORibBS9DYPUPrg"
- "FDR calibration size - %ul"
- "FDRCalibrationTester <calibrationType> <filepath> [-print] [-parse]"
- "HmCA10"
- "HmCM"
- "Plugin is opening on Bridge OS."
- "ProductName"
- "Retrieving FDR calibration data failed in attempt number %d/20. Try again in 5 sec.\n"
- "algo_version:       %d\n"
- "backlightCounts: "
- "cctCoeff: "
- "cfsn:                           %lld\n"
- "darkCounts: "
- "gain_scaling:"
- "luxCoeff: "
- "luxCoeff_gain: %d\n"
- "luxCoeff_itime: %d\n"
- "lux_correction:      %f\n"
- "magic:                          %c%c%c%c\n"
- "numChannels:        %d\n"
- "numGains:           %d\n"
- "r"
- "sensor type:           0x%02X\n"
- "size:                           %d\n"
- "size:               %d\n"
- "spectrum:"
- "spectrum_normalization:      %lf\n"
- "upstreamPassFatpTest:           0x%02X\n"
- "version:                        v%d.%d\n"
- "wavelength_end:                     %d\n"
- "wavelength_start_nir:               %d\n"
- "wavelength_start_visible:           %d\n"
- "wavelength_step:                    %d\n"

```
