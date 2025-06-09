## AppleH15MCD

> `/System/Library/Extensions/AppleH15MCD.kext/AppleH15MCD`

```diff

-119.0.0.0.0
-  __TEXT.__cstring: 0x8893
+121.0.0.0.0
+  __TEXT.__cstring: 0x88d9
   __TEXT.__const: 0x1a0
-  __TEXT.__os_log: 0x111c
-  __TEXT_EXEC.__text: 0x13ad4
+  __TEXT.__os_log: 0x1198
+  __TEXT_EXEC.__text: 0x145f0
   __TEXT_EXEC.__auth_stubs: 0x490
   __DATA.__data: 0x12f68
   __DATA.__common: 0x108

   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x6d30
+  __DATA_CONST.__const: 0x6d48
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: FFE6C615-FED3-3359-B3CF-2CC27D70174E
+  UUID: C39DB0F2-1CE6-35EE-89B2-EAA071B71716
   Functions: 406
-  Symbols:   928
-  CStrings:  1413
+  Symbols:   933
+  CStrings:  1415
 
Symbols:
+ __ZN10AppleARMIO15resetPsdServiceEjPc
+ __ZN10AppleARMIO16enablePsdServiceEjjPc
+ __ZN10AppleARMIO18getPsdServiceStateEjPj
+ __ZZN26AppleH15MemCacheController10getBankValEyPjS0_S0_E11_os_log_fmt
+ __ZZN26AppleH15MemCacheController15getAmccInstanceEyPjS0_E11_os_log_fmt
Functions:
~ __ZN28AppleH15PlatformErrorHandler23_amccNonPlaneDecodeACTTEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 464 -> 496
~ __ZN28AppleH15PlatformErrorHandler23_amccNonPlaneDecodeSCTTEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 468 -> 500
~ __ZN28AppleH15PlatformErrorHandler24_amccNonPlaneDecodeGCTT0EjjRjPKNS_21AMCCNonPlaneDecoder_tE : 424 -> 456
~ __ZN28AppleH15PlatformErrorHandler24_amccNonPlaneDecodeGCTT1EjjRjPKNS_21AMCCNonPlaneDecoder_tE : 424 -> 456
~ __ZN28AppleH15PlatformErrorHandler30_amccNoPlaneDecodeUeflOverflowEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 340 -> 356
~ __ZN28AppleH15PlatformErrorHandler30_amccNoPlaneDecodeCeflOverflowEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 204 -> 216
~ __ZN28AppleH15PlatformErrorHandler38_amccNoPlaneDecodeCeflErrCountExceededEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 84 -> 100
~ __ZN28AppleH15PlatformErrorHandler18_afxNsDecodeStatusEjjPKNS_14AfxNsDecoder_tEPKNS_10aperture_tEPKjPKNS_13AfxNsStatus_tE : 440 -> 504
~ __ZN28AppleH15PlatformErrorHandler5startEP9IOService : 5512 -> 5904
~ __ZN28AppleH15PlatformErrorHandler15eccEventHandlerEP8OSObjectP22IOInterruptEventSourcei : 1012 -> 1060
~ __ZN28AppleH15PlatformErrorHandler30amccNoPlaneDelayedFetchUeflLogEP8OSObjectP22IOInterruptEventSourcei : 388 -> 420
~ __ZN28AppleH15PlatformErrorHandler12_getMetadataERNS_10metadata_tEPKcjb : 1196 -> 1220
~ __ZN28AppleH15PlatformErrorHandler22_d2dAfcHandleInterruptEP8OSObjectPvP9IOServicei : 104 -> 120
~ __ZN28AppleH15PlatformErrorHandler22_d2dAfiHandleInterruptEP8OSObjectPvP9IOServicei : 104 -> 120
~ __ZN28AppleH15PlatformErrorHandler22_d2dAfrHandleInterruptEP8OSObjectPvP9IOServicei : 104 -> 120
~ __ZN28AppleH15PlatformErrorHandler24_afxNiGenerateEnableMaskEv : 112 -> 128
~ __ZN28AppleH15PlatformErrorHandler26_d2dAfcGenerateDisableMaskEv : 116 -> 156
~ __ZN28AppleH15PlatformErrorHandler26_d2dAfiGenerateDisableMaskEv : 128 -> 168
~ __ZN28AppleH15PlatformErrorHandler26_d2dAfrGenerateDisableMaskEv : 148 -> 192
~ __ZN28AppleH15PlatformErrorHandler17_amccEnableErrorsEb : 320 -> 336
~ __ZN28AppleH15PlatformErrorHandler16_dcsEnableErrorsEb : 400 -> 436
~ __ZN28AppleH15PlatformErrorHandler16_ioaEnableErrorsEb : 484 -> 552
~ __ZN28AppleH15PlatformErrorHandler18_afxNiEnableErrorsEb : 292 -> 308
~ __ZN28AppleH15PlatformErrorHandler20_d2dAfcDisableErrorsEv : 152 -> 184
~ __ZN28AppleH15PlatformErrorHandler20_d2dAfiDisableErrorsEv : 144 -> 176
~ __ZN28AppleH15PlatformErrorHandler20_d2dAfrDisableErrorsEv : 188 -> 220
~ __ZN28AppleH15PlatformErrorHandler23_amccPostHibernateCleanEv : 168 -> 184
~ __ZN28AppleH15PlatformErrorHandler15_readRegister32EPKNS_10aperture_tEjj : 80 -> 96
~ __ZN28AppleH15PlatformErrorHandler16_writeRegister32EPKNS_10aperture_tEjjj : 80 -> 96
~ __ZN28AppleH15PlatformErrorHandler14_fabricCommandEj : 48 -> 72
~ __ZN28AppleH15PlatformErrorHandler23amccNoPlaneFetchCeflLogEjPyPj : 372 -> 412
~ __ZN28AppleH15PlatformErrorHandler22_afxNiDecodeInterruptsEiPv : 1140 -> 1176
~ __ZN28AppleH15PlatformErrorHandler22_afxNsDecodeInterruptsEiPv : 384 -> 504
~ __ZN28AppleH15PlatformErrorHandler32_amccNoPlaneDecodeOverflowGetEFLENS_12EFLErrorTypeEjjj : 332 -> 468
~ __ZN28AppleH15PlatformErrorHandler31_amccNoPlaneDecodeCeflReportLogEjNS_12EFLErrorTypeE : 228 -> 244
~ __ZN28AppleH15PlatformErrorHandler29_amccPlaneDecodeTagPipeParityEjjjRjPKNS_18AMCCPlaneDecoder_tE : 180 -> 196
~ __ZN28AppleH15PlatformErrorHandler27_amccPlaneDecodeDataPipeSBEEjjjRjPKNS_18AMCCPlaneDecoder_tE : 356 -> 368
~ __ZN28AppleH15PlatformErrorHandler27_amccPlaneDecodeDataPipeMBEEjjjRjPKNS_18AMCCPlaneDecoder_tE : 132 -> 148
~ __ZN28AppleH15PlatformErrorHandler31_amccPlaneDecodeDirectoryParityEjjjRjPKNS_18AMCCPlaneDecoder_tE : 344 -> 360
~ __ZN28AppleH15PlatformErrorHandler33_amccPlaneDecodeDirectoryMultiHitEjjjRjPKNS_18AMCCPlaneDecoder_tE : 332 -> 348
~ __ZN28AppleH15PlatformErrorHandler30_amccPlaneDecodeTagPipeAFErrorEjjjRjPKNS_18AMCCPlaneDecoder_tE : 484 -> 524
~ __ZN28AppleH15PlatformErrorHandler37_amccPlaneDecodeDirectoryInconsistentEjjjRjPKNS_18AMCCPlaneDecoder_tE : 340 -> 356
~ __ZN28AppleH15PlatformErrorHandler20_amccPlaneDsidAgeOutEjjjRjPKNS_18AMCCPlaneDecoder_tE : 552 -> 568
~ __ZN28AppleH15PlatformErrorHandler41_amccPlaneDecodeDirectoryUnexpectedVictimEjjjRjPKNS_18AMCCPlaneDecoder_tE : 156 -> 172
~ __ZN28AppleH15PlatformErrorHandler30_amccEnableErrorsForInputTableEPNS_22AMCCNonPlaneDecoders_tEjb : 152 -> 168
~ __ZN28AppleH15PlatformErrorHandler26_amccDumpRegsForInputTableEPNS_22AMCCNonPlaneDecoders_tEjPcPKc : 148 -> 164
~ __ZN28AppleH15PlatformErrorHandler13_amccDumpRegsEj : 532 -> 588
~ __ZN28AppleH15PlatformErrorHandler21_amccDecodeInterruptsEiPv : 592 -> 640
~ __ZN28AppleH15PlatformErrorHandler34_amccDecodeInterruptsForInputTableEPNS_22AMCCNonPlaneDecoders_tEjPb : 336 -> 372
~ __ZN28AppleH15PlatformErrorHandler17writePoisonEnableEb : 136 -> 152
~ __ZN28AppleH15PlatformErrorHandler18_dcsDecodeMCUErrorEjjjRjPKNS_12DCSDecoder_tE : 712 -> 796
~ __ZN28AppleH15PlatformErrorHandler20_dcsDecodeInterruptsEiPv : 796 -> 832
~ __ZN28AppleH15PlatformErrorHandler23_gibIoaDecodeInterruptsEiPv : 248 -> 264
~ __ZN28AppleH15PlatformErrorHandler23_gibD2dDecodeInterruptsEiPv : 240 -> 256
~ __ZN28AppleH15PlatformErrorHandler24_gibAmccDecodeInterruptsEiPv : 240 -> 256
~ __ZN28AppleH15PlatformErrorHandler23_d2dAfxDecodeInterruptsEPKciPvPKNS_10metadata_tEPKNS_10aperture_tEPKNS_15D2DAfxDecoder_tEm : 340 -> 376
~ __ZN28AppleH15PlatformErrorHandler23_d2dAfrDecodeInterruptsEPKciPvPKNS_10metadata_tEPKNS_10aperture_tEPKNS_15D2DAfxDecoder_tEm : 420 -> 456
~ __ZN28AppleH15PlatformErrorHandler9_ioaPanicEjRjPKNS_12IOADecoder_tE : 576 -> 592
~ __ZN28AppleH15PlatformErrorHandler20_ioaDecodeInterruptsEiPv : 312 -> 328
~ __ZN28AppleH15PlatformErrorHandler20_sepDecodeInterruptsEiPv : 148 -> 172
~ __ZN28AppleH15PlatformErrorHandler23_sepDecodeMonInterruptsEiPv : 460 -> 492
~ __ZN28AppleH15PlatformErrorHandler21_sramDecodeInterruptsEiPv : 344 -> 360
~ __ZN26AppleH15MemCacheController13_mccReadReg32EPKNS_15amcc_aperture_tEjj : 228 -> 244
~ __ZL16dcs_error_injectPvmyj : 72 -> 68
~ __ZN26AppleH15MemCacheController20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 1200 -> 1196
~ __ZN26AppleH15MemCacheController31_mccRestoreAMCPerfCounterConfigEv : 200 -> 220
~ __ZN26AppleH15MemCacheController23_mccProtectedWriteReg32EPKNS_15amcc_aperture_tEjjj : 256 -> 276
~ __ZN26AppleH15MemCacheController28_mccSelectDynamicDRAMCFGModeEj : 448 -> 472
~ __ZN26AppleH15MemCacheController14_mccWriteReg32EPKNS_15amcc_aperture_tEjjj : 232 -> 248
~ __ZN26AppleH15MemCacheController18handleDCSOdtsEventEP18IOTimerEventSource : 296 -> 292
~ __ZN26AppleH15MemCacheController23getMaxOfDCSODTSReadingsEPb : 836 -> 828
~ __ZN26AppleH15MemCacheController14_mccWriteReg64EPKNS_15amcc_aperture_tEjjy : 228 -> 244
~ __ZN26AppleH15MemCacheController21_setCntrCtrlParmetersEPNS_17AMCCCounterConfigEj : 1264 -> 1280
~ __ZN26AppleH15MemCacheController14_writePerfCtrlEPNS_17AMCCCounterConfigEjj : 552 -> 688
~ __ZN26AppleH15MemCacheController15_enablePerfCtrlEPNS_17AMCCCounterConfigEjb : 912 -> 932
~ __ZN26AppleH15MemCacheController21_mccSamplePerfCounterEPNS_17AMCCCounterConfigEjPy : 160 -> 176
~ __ZN26AppleH15MemCacheController14_readPerfValueEPNS_17AMCCCounterConfigEj : 316 -> 356
~ __ZN26AppleH15MemCacheController13_mccReadReg64EPKNS_15amcc_aperture_tEjj : 228 -> 244
~ __ZN26AppleH15MemCacheController17setDSIDGroupQuotaEjy : 484 -> 536
~ __ZN26AppleH15MemCacheController16getHashBitValuesEPjyPNS_14DcsHashingUnitEj : 132 -> 156
~ __ZN26AppleH15MemCacheController15restoreDropBitsEPyPNS_14DcsHashingUnitEPjj : 288 -> 312
~ __ZN26AppleH15MemCacheController15getAmccInstanceEyPjS0_ : 448 -> 468
~ __ZN26AppleH15MemCacheController10getBankValEyPjS0_S0_ : 360 -> 368
~ __ZN26AppleH15MemCacheController20setErrorInjectionDCSEPNS_8errorInjE : 740 -> 852
CStrings:
+ "%s:%d: Not able to get dcs hashing result. Aborting error injection\n\n"
+ "Not able to get dcs hashing result. Aborting error injection\n"

```
