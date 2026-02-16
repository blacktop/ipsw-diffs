## Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0xd9c8
-  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__text: 0xe238
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x3000
-  __TEXT.__gcc_except_tab: 0x162c
+  __TEXT.__cstring: 0x303f
+  __TEXT.__gcc_except_tab: 0x1640
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x231
   __TEXT.__objc_methtype: 0xd4
-  __TEXT.__unwind_info: 0x408
-  __DATA_CONST.__auth_got: 0x378
+  __TEXT.__unwind_info: 0x410
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x480
   __DATA_CONST.__cfstring: 0x21c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9E70545-794D-355F-B127-B28D297ABBD2
+  UUID: 034D6AE0-5C05-358B-A503-3DF9E97FA4E9
   Functions: 145
-  Symbols:   324
+  Symbols:   325
   CStrings:  650
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ __Z15Simd4x3ToMatrixR13simd_float4x3PA3_fPf : 84 -> 100
~ __ZN28HxISPCaptureDeviceController9FindGroupEj : 324 -> 316
~ __ZN28HxISPCaptureDeviceController11stopReceiveEj : 404 -> 396
~ __ZN28HxISPCaptureDeviceController10deactivateEv : 404 -> 396
~ __ZN28HxISPCaptureDeviceController8activateEv : 880 -> 864
~ __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArrayPK14__CFDictionary : 208 -> 200
~ __ZN28HxISPCaptureDeviceController17RelinquishStreamsEPK9__CFArray : 192 -> 184
~ __ZN28HxISPCaptureDeviceController12startReceiveEjPFvP20opaqueCMSampleBufferjPvES2_ : 1056 -> 1024
~ __ZN28HxISPCaptureDeviceController33startReceiveWithRealTimeCallbacksEjPFvP10__CVBuffer6CMTimejPvES3_S5_S3_S5_S3_S5_S3_S5_S3_S5_S3_S5_S3_S5_S3_S5_S3_S5_S3_ : 2460 -> 2444
~ __ZN28HxISPCaptureDeviceController17SetStreamPropertyEjPK10__CFStringPKv : 308 -> 304
~ __ZN28HxISPCaptureDeviceController17SetDevicePropertyEPK10__CFStringPKv : 216 -> 208
~ __ZN28HxISPCaptureDeviceController18CopyDevicePropertyEPK10__CFStringPv : 228 -> 220
~ __ZN28HxISPCaptureDeviceController18CopyStreamPropertyEjPK10__CFStringPv : 256 -> 248
~ __ZN28HxISPCaptureDeviceController16SetGroupPropertyEjPK10__CFStringPKv : 512 -> 496
~ __ZN28HxISPCaptureDeviceController17CopyGroupPropertyEjPK10__CFStringPv : 516 -> 500
~ __ZN17DeviceCMInterface38initAndActivateCaptureDeviceControllerEv : 348 -> 360
~ __ZN17DeviceCMInterface19setRgbConfigurationEiRK19RGBCamConfiguration : 3760 -> 3976
~ __ZN17DeviceCMInterface20enableJasperRgbVideoEv : 576 -> 620
~ __ZN17DeviceCMInterface26enableRGBOutputForStreamIdEi : 356 -> 368
~ __ZN17DeviceCMInterface28enableJasperPointCloudOutputEv : 512 -> 540
~ __ZN17DeviceCMInterface26configJasperRgbMultiStreamERK19JasperConfiguration : 1644 -> 1728
~ __ZN17DeviceCMInterface31setJasperMultiOutModeByStreamIdEjb : 624 -> 664
~ __ZN17DeviceCMInterface18configJasperDeviceERK19JasperConfiguration : 3180 -> 3348
~ __ZN17DeviceCMInterface17enableSWRGBOutputEv : 212 -> 224
~ __ZN17DeviceCMInterface23requestControlOfStreamsEbj : 1344 -> 1420
~ __ZN17DeviceCMInterface23releaseControlOfStreamsEv : 384 -> 412
~ __ZN17DeviceCMInterface23enumerateStreamsIndicesEv : 960 -> 992
~ __ZN17DeviceCMInterface30setPearlMultiOutModeByStreamIdEjb : 612 -> 652
~ __ZN17DeviceCMInterface17setStreamPropertyEjPK10__CFStringPK12NSDictionary : 460 -> 488
~ __ZN17DeviceCMInterface19enablePearlIROutputEv : 748 -> 784
~ __ZN17DeviceCMInterface20enablePearlRGBOutputEv : 212 -> 224
~ __ZN17DeviceCMInterface22setPearlIrCofigurationE20PearlProjectorIRType : 1940 -> 2064
~ __ZN17DeviceCMInterface26setPearlDepthConfigurationEyyb18PearlPdeOutputMode : 844 -> 872
~ __ZN17DeviceCMInterface14startRgbStreamEi : 1052 -> 1136
~ __ZN17DeviceCMInterface17startJasperStreamEv : 1688 -> 1808
~ sub_100009528 -> sub_10000995c : 172 -> 164
~ __ZN17DeviceCMInterface16stopJasperStreamEv : 524 -> 560
~ __ZN17DeviceCMInterface18startPearlIrStreamEv : 928 -> 996
~ sub_100009b80 -> sub_10000a014 : 184 -> 176
~ __ZN17DeviceCMInterface17stopPearlIrStreamEv : 524 -> 560
~ __ZN17DeviceCMInterface13stopRgbStreamEi : 516 -> 552
~ __ZN17DeviceCMInterface22validateJasperFwStatusEPj : 344 -> 360
~ __ZN17DeviceCMInterface18validateIrFwStatusEPj : 628 -> 668
~ __ZN17DeviceCMInterface24enableDefaultDepthStreamEv : 224 -> 236
~ __ZN17DeviceCMInterface16setPearlMultiCamEv : 960 -> 1016
~ __ZN17DeviceCMInterface30enableSyncForEnumeratedStreamsEi : 560 -> 588
~ __ZN17DeviceCMInterface17setPearlSyncSlaveEii : 780 -> 820
~ __ZN17DeviceCMInterface20disablePearlSyncModeEi : 316 -> 332
~ __ZN17DeviceCMInterface17configPearlDeviceERK18PearlConfiguration : 2724 -> 2952
~ __ZN17DeviceCMInterface26getPearlProjectorHWVersionEPi : 432 -> 456
~ __ZNK17DeviceCMInterface31getJasperConfigurationStringKeyEPK19JasperConfiguration : 216 -> 224
~ __ZNK17DeviceCMInterface30getPearlConfigurationStringKeyEPK18PearlConfiguration : 476 -> 480
~ __ZN17DeviceCMInterface22isPDECaliobrationValidEPb : 388 -> 412
~ __ZN17DeviceCMInterface23getJasperProjectorFaultEPyPU15__autoreleasingP12NSDictionary : 436 -> 452
~ __ZN17DeviceCMInterface27getJasperProjectorWillFaultEPy : 476 -> 504
~ __ZN17DeviceCMInterface19getJasperResistanceEPy : 476 -> 504
~ __ZN17DeviceCMInterface27getPearlFloodProjectorFaultEPy : 624 -> 664
~ __ZN17DeviceCMInterface27getStructuredProjectorFaultEPy : 492 -> 520
~ __ZN17DeviceCMInterface13releaseDeviceEv : 224 -> 236
~ __ZN17DeviceCMInterface13getRgbjReportERiS0_S0_S0_S0_ : 528 -> 544
~ __ZN17DeviceCMInterface24forceSaveWideJasperCalibEv : 280 -> 296
~ __ZN17DeviceCMInterface20setRgbjConfigurationEjjj : 492 -> 520
~ __ZN17DeviceCMInterface23setWideJasperExtrinsicsEffffff : 668 -> 712
~ __ZN17DeviceCMInterface15getPearlPleUUIDEPh : 436 -> 460
~ __ZN17DeviceCMInterface25getPearlRigelSerialNumberEPU15__autoreleasingP8NSString : 440 -> 468
~ __ZN17DeviceCMInterface23getPearlRigelOtpVersionEPi : 444 -> 468
~ __ZN17DeviceCMInterface18getGuadalupeValuesEPxS0_S0_PiS0_ : 1084 -> 1148
~ sub_10000dce8 -> sub_10000e538 : 1668 -> 1696
~ sub_10000e36c -> sub_10000ebd8 : 184 -> 188
CStrings:
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"

```
