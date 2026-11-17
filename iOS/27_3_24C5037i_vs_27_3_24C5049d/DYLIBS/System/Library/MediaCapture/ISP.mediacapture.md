## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-20.203.1.0.0
-  __TEXT.__text: 0x1f0d4c
+20.206.0.0.0
+  __TEXT.__text: 0x1f1630
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x5dec
+  __TEXT.__gcc_except_tab: 0x5e38
   __TEXT.__const: 0x2905d
-  __TEXT.__oslogstring: 0x23f09
-  __TEXT.__cstring: 0x1aec0
-  __TEXT.__unwind_info: 0x6910
+  __TEXT.__oslogstring: 0x241bb
+  __TEXT.__cstring: 0x1af22
+  __TEXT.__unwind_info: 0x6920
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x18d8
+  __AUTH_CONST.__auth_got: 0x18e8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x5b0910

   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6179
-  Symbols:   7889
-  CStrings:  7171
+  Functions: 6183
+  Symbols:   7894
+  CStrings:  7185
 
Symbols:
+ GCC_except_table596
+ GCC_except_table601
+ GCC_except_table618
+ GCC_except_table621
+ GCC_except_table627
+ GCC_except_table629
+ GCC_except_table632
+ GCC_except_table639
+ GCC_except_table669
+ GCC_except_table671
+ GCC_except_table695
+ GCC_except_table788
+ GCC_except_table789
+ GCC_except_table794
+ GCC_except_table829
+ GCC_except_table833
+ GCC_except_table835
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table847
+ GCC_except_table853
+ GCC_except_table857
+ GCC_except_table862
+ GCC_except_table866
+ GCC_except_table885
+ GCC_except_table889
+ GCC_except_table914
+ GCC_except_table929
+ _SavageCamInterfaceCheckPersonalizationStatus
+ __ZL21ISPCaptureGroupCreatePK13__CFAllocatorP22OpaqueFigCaptureDevicePN3ISP9ISPDeviceEPK9__CFArrayPP40OpaqueFigCaptureSynchronizedStreamsGroup
+ __ZL27ExclaveSetIsConcurrentStatejb
+ __ZL27SecureAlgoConsumesTileStatsP16ISPCaptureDeviceP16ISPCaptureStream
+ _xpc_dictionary_set_bool
- GCC_except_table595
- GCC_except_table600
- GCC_except_table617
- GCC_except_table620
- GCC_except_table626
- GCC_except_table628
- GCC_except_table631
- GCC_except_table638
- GCC_except_table668
- GCC_except_table670
- GCC_except_table694
- GCC_except_table785
- GCC_except_table786
- GCC_except_table791
- GCC_except_table823
- GCC_except_table830
- GCC_except_table832
- GCC_except_table834
- GCC_except_table838
- GCC_except_table839
- GCC_except_table848
- GCC_except_table850
- GCC_except_table859
- GCC_except_table863
- GCC_except_table882
- GCC_except_table886
- GCC_except_table911
- GCC_except_table926
CStrings:
+ "%s - Failed to set isConcurrent to %{bool}d on ch %u: err=%d\n"
+ "%s - SavageCamInterfaceCheckPersonalizationStatus err 0x%08X\n"
+ "%s - Skipping unpersonalized secure camera channel: %d\n"
+ "%s - Sync group %d has no HW master stream available - not advertising group\n"
+ "%s - Sync group %d has only %d stream - not advertising as a sync group\n"
+ "%s - ch %u concurrentEnabled %{bool}d\n"
+ "%s - chan %d - cameraModuleDescription 0x%08X malformed status entry, stateValue %p typeID %lu (expected %lu), failing closed\n"
+ "%s - chan %d - could not allocate lookup key, failing closed\n"
+ "%s - chan %d - no platform info/statuses dict, info not available, failing closed\n"
+ "%s - chan %d - personalization status unavailable (0x%08X), failing closed\n"
+ "ExclaveSetIsConcurrentState"
+ "IsScanMode"
+ "IsSensorNotPersonalized"
+ "ScanModeResult"
+ "ScanModeTotalLength"
+ "[Exclaves] ISPGraphExclavePCENode::%s ch=%u status=%lld dur=%llums trigger=%llu corr=%llu scanStep=%llu scanMode=%d scanTotal=%llums scanResult=%u isf=%d\n"
- "%s - ISP_EXCLAVEKIT_CMD_RGB_CH_CONCURRENT_FLAG_SET is failure Err: %d\n"
- "[Exclaves] ISPGraphExclavePCENode::%s ch=%u status=%lld dur=%llums trigger=%llu corr=%llu scanStep=%llu isf=%d\n"
```
