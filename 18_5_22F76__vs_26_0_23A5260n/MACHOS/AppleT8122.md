## AppleT8122

> `/System/Library/Extensions/AppleT8122.kext/AppleT8122`

```diff

-119.0.0.0.0
+121.0.0.0.0
   __TEXT.__cstring: 0x5d9f
   __TEXT.__const: 0xd0
   __TEXT.__os_log: 0xe18
-  __TEXT_EXEC.__text: 0xf178
+  __TEXT_EXEC.__text: 0xf924
   __TEXT_EXEC.__auth_stubs: 0x3e0
   __DATA.__data: 0x58b4
   __DATA.__common: 0x108

   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x40a0
+  __DATA_CONST.__const: 0x40b8
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 36CC84C6-03D4-38A2-9AF8-D640C45BB19C
+  UUID: 82ADBC67-2E70-3F0B-B084-D8028328DC26
   Functions: 327
-  Symbols:   800
+  Symbols:   803
   CStrings:  930
 
Symbols:
+ __ZN10AppleARMIO15resetPsdServiceEjPc
+ __ZN10AppleARMIO16enablePsdServiceEjjPc
+ __ZN10AppleARMIO18getPsdServiceStateEjPj
Functions:
~ __ZN28AppleH15PlatformErrorHandler23_amccNonPlaneDecodeACTTEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 464 -> 496
~ __ZN28AppleH15PlatformErrorHandler23_amccNonPlaneDecodeSCTTEjjRjPKNS_21AMCCNonPlaneDecoder_tE : 468 -> 500
~ __ZN28AppleH15PlatformErrorHandler24_amccNonPlaneDecodeGCTT0EjjRjPKNS_21AMCCNonPlaneDecoder_tE : 424 -> 456
~ __ZN28AppleH15PlatformErrorHandler24_amccNonPlaneDecodeGCTT1EjjRjPKNS_21AMCCNonPlaneDecoder_tE : 424 -> 456
~ __ZN28AppleH15PlatformErrorHandler5startEP9IOService : 4292 -> 4684
~ __ZN28AppleH15PlatformErrorHandler12_getMetadataERNS_10metadata_tEPKcjb : 1196 -> 1220
~ __ZN28AppleH15PlatformErrorHandler24_afxNiGenerateEnableMaskEv : 112 -> 128
~ __ZN28AppleH15PlatformErrorHandler17_amccEnableErrorsEb : 304 -> 320
~ __ZN28AppleH15PlatformErrorHandler16_dcsEnableErrorsEb : 248 -> 264
~ __ZN28AppleH15PlatformErrorHandler16_ioaEnableErrorsEb : 304 -> 336
~ __ZN28AppleH15PlatformErrorHandler18_afxNiEnableErrorsEb : 276 -> 308
~ __ZN28AppleH15PlatformErrorHandler23_amccPostHibernateCleanEv : 172 -> 188
~ __ZN28AppleH15PlatformErrorHandler15_readRegister32EPKNS_10aperture_tEjj : 80 -> 96
~ __ZN28AppleH15PlatformErrorHandler16_writeRegister32EPKNS_10aperture_tEjjj : 80 -> 96
~ __ZN28AppleH15PlatformErrorHandler14_fabricCommandEj : 48 -> 72
~ __ZN28AppleH15PlatformErrorHandler23amccNoPlaneFetchCeflLogEjPyPj : 372 -> 412
~ __ZN28AppleH15PlatformErrorHandler22_afxNiDecodeInterruptsEiPv : 584 -> 620
~ __ZN28AppleH15PlatformErrorHandler18_afxNsDecodeStatusEjjPKNS_14AfxNsDecoder_tEPKNS_10aperture_tEPKjPKNS_13AfxNsStatus_tE : 440 -> 504
~ __ZN28AppleH15PlatformErrorHandler22_afxNsDecodeInterruptsEiPv : 384 -> 504
~ __ZN28AppleH15PlatformErrorHandler29_amccPlaneDecodeTagPipeParityEjjjRjPKNS_18AMCCPlaneDecoder_tE : 180 -> 196
~ __ZN28AppleH15PlatformErrorHandler27_amccPlaneDecodeDataPipeSBEEjjjRjPKNS_18AMCCPlaneDecoder_tE : 356 -> 368
~ __ZN28AppleH15PlatformErrorHandler27_amccPlaneDecodeDataPipeMBEEjjjRjPKNS_18AMCCPlaneDecoder_tE : 132 -> 148
~ __ZN28AppleH15PlatformErrorHandler31_amccPlaneDecodeDirectoryParityEjjjRjPKNS_18AMCCPlaneDecoder_tE : 344 -> 360
~ __ZN28AppleH15PlatformErrorHandler33_amccPlaneDecodeDirectoryMultiHitEjjjRjPKNS_18AMCCPlaneDecoder_tE : 328 -> 344
~ __ZN28AppleH15PlatformErrorHandler30_amccPlaneDecodeTagPipeAFErrorEjjjRjPKNS_18AMCCPlaneDecoder_tE : 484 -> 524
~ __ZN28AppleH15PlatformErrorHandler37_amccPlaneDecodeDirectoryInconsistentEjjjRjPKNS_18AMCCPlaneDecoder_tE : 340 -> 356
~ __ZN28AppleH15PlatformErrorHandler20_amccPlaneDsidAgeOutEjjjRjPKNS_18AMCCPlaneDecoder_tE : 552 -> 568
~ __ZN28AppleH15PlatformErrorHandler41_amccPlaneDecodeDirectoryUnexpectedVictimEjjjRjPKNS_18AMCCPlaneDecoder_tE : 156 -> 172
~ __ZN28AppleH15PlatformErrorHandler30_amccEnableErrorsForInputTableEPNS_22AMCCNonPlaneDecoders_tEjb : 152 -> 168
~ __ZN28AppleH15PlatformErrorHandler26_amccDumpRegsForInputTableEPNS_22AMCCNonPlaneDecoders_tEjPcPKc : 148 -> 164
~ __ZN28AppleH15PlatformErrorHandler13_amccDumpRegsEj : 520 -> 576
~ __ZN28AppleH15PlatformErrorHandler21_amccDecodeInterruptsEiPv : 600 -> 648
~ __ZN28AppleH15PlatformErrorHandler34_amccDecodeInterruptsForInputTableEPNS_22AMCCNonPlaneDecoders_tEjPb : 336 -> 372
~ __ZN28AppleH15PlatformErrorHandler18_dcsDecodeMCUErrorEjjjRjPKNS_12DCSDecoder_tE : 684 -> 768
~ __ZN28AppleH15PlatformErrorHandler20_dcsDecodeInterruptsEiPv : 752 -> 788
~ __ZN28AppleH15PlatformErrorHandler23_d2dAfxDecodeInterruptsEPKciPvPKNS_10metadata_tEPKNS_10aperture_tEPKNS_15D2DAfxDecoder_tEm : 340 -> 376
~ __ZN28AppleH15PlatformErrorHandler9_ioaPanicEjRjPKNS_12IOADecoder_tE : 576 -> 592
~ __ZN28AppleH15PlatformErrorHandler20_ioaDecodeInterruptsEiPv : 224 -> 240
~ __ZN28AppleH15PlatformErrorHandler20_sepDecodeInterruptsEiPv : 148 -> 172
~ __ZN28AppleH15PlatformErrorHandler23_sepDecodeMonInterruptsEiPv : 464 -> 496
~ __ZN26AppleH15MemCacheController13_mccReadReg32EPKNS_15amcc_aperture_tEjj : 228 -> 244
~ __ZN26AppleH15MemCacheController20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 1200 -> 1196
~ __ZN26AppleH15MemCacheController31_mccRestoreAMCPerfCounterConfigEv : 200 -> 220
~ __ZN26AppleH15MemCacheController23_mccProtectedWriteReg32EPKNS_15amcc_aperture_tEjjj : 256 -> 276
~ __ZN26AppleH15MemCacheController28_mccSelectDynamicDRAMCFGModeEj : 448 -> 472
~ __ZN26AppleH15MemCacheController14_mccWriteReg32EPKNS_15amcc_aperture_tEjjj : 232 -> 248
~ __ZN26AppleH15MemCacheController23getMaxOfDCSODTSReadingsEPb : 904 -> 896
~ __ZN26AppleH15MemCacheController14_mccWriteReg64EPKNS_15amcc_aperture_tEjjy : 228 -> 244
~ __ZN26AppleH15MemCacheController21_setCntrCtrlParmetersEPNS_17AMCCCounterConfigEj : 1252 -> 1268
~ __ZN26AppleH15MemCacheController14_writePerfCtrlEPNS_17AMCCCounterConfigEjj : 552 -> 688
~ __ZN26AppleH15MemCacheController15_enablePerfCtrlEPNS_17AMCCCounterConfigEjb : 912 -> 932
~ __ZN26AppleH15MemCacheController21_mccSamplePerfCounterEPNS_17AMCCCounterConfigEjPy : 160 -> 176
~ __ZN26AppleH15MemCacheController14_readPerfValueEPNS_17AMCCCounterConfigEj : 316 -> 356
~ __ZN26AppleH15MemCacheController13_mccReadReg64EPKNS_15amcc_aperture_tEjj : 228 -> 244
~ __ZN26AppleH15MemCacheController17setDSIDGroupQuotaEjy : 484 -> 536

```
