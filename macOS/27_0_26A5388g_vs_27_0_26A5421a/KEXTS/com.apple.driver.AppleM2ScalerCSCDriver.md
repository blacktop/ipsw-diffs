## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-200.57.0.0.0
-  __TEXT.__const: 0xc3020
-  __TEXT.__cstring: 0x25520
-  __TEXT_EXEC.__text: 0x146028
+200.62.3.0.0
+  __TEXT.__const: 0xc30c0
+  __TEXT.__cstring: 0x25869
+  __TEXT_EXEC.__text: 0x146004
   __TEXT_EXEC.__auth_stubs: 0xba0
   __DATA.__data: 0x22388
-  __DATA.__common: 0x2760
-  __DATA.__bss: 0x2184
-  __DATA_CONST.__mod_init_func: 0x6a8
-  __DATA_CONST.__mod_term_func: 0x678
-  __DATA_CONST.__const: 0x3de88
-  __DATA_CONST.__kalloc_type: 0x4ec0
-  __DATA_CONST.__kalloc_var: 0x1310
+  __DATA.__common: 0x2710
+  __DATA.__bss: 0x2134
+  __DATA_CONST.__mod_init_func: 0x698
+  __DATA_CONST.__mod_term_func: 0x668
+  __DATA_CONST.__const: 0x3d9c8
+  __DATA_CONST.__kalloc_type: 0x4e40
+  __DATA_CONST.__kalloc_var: 0x13b0
   __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10215
-  Symbols:   10288
-  CStrings:  3650
+  Functions: 10194
+  Symbols:   10252
+  CStrings:  3664
 
Symbols:
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _ZN12MailBoxMSR2619drainOutboxMessagesEv
+ _ZN19IosaDPEControlMSR237stopDPEEv
+ _ZN24AppleM2ScalerCSCHalMSR2739tearDownMsrMessageBoxLinks_gatedContextEv
+ _ZN27IosaFirmwareControlMSR27Rtk23runColdBootInitSequenceEv
+ _ZZN22AppleM2ScalerCSCDriver20checkCustomFilterBinEP18M2ScalerCSCRequestENK3$_0clEv
+ __ZN12MailBoxMSR2619drainOutboxMessagesEv
+ __ZN12MailBoxMSR2622hwCheckCreditReturnIncEv
+ __ZN22AppleM2ScalerCSCDriver44findCustomFilterCoefficientsAtNeighboringBinEP18M2ScalerCSCRequest20VerticalOrHorizontal17ChromaLumaOrAlphadjPjPd
+ __ZN24AppleM2ScalerCSCHalMSR2339tearDownMsrMessageBoxLinks_gatedContextEv
+ __ZN24AppleM2ScalerCSCHalMSR2739tearDownMsrMessageBoxLinks_gatedContextEv
+ __ZN27IosaFirmwareControlMSR27Rtk23runColdBootInitSequenceEv
+ __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_3137
+ __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEjE22kalloc_type_view_11043
+ __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10973
+ __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10979
+ __ZZN19AppleM2ScalerCSCHal32updateShadowMapperCacheTTL_gatedEjyE22kalloc_type_view_11027
+ __ZZN22AppleM2ScalerCSCDriver20checkCustomFilterBinEP18M2ScalerCSCRequestENK3$_0clEv
+ __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6424
+ __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6403
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1727
+ __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1734
+ __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_627
+ __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_688
+ __ZZN26IOSurfaceAcceleratorClient40asynchronousUserClientCompletionCallbackEPvS0_E20kalloc_type_view_595
+ __ZZN29BlockDescriptorRegStreamMSR2325prepareClientForTransformEP4taskbE20kalloc_type_view_851
+ __ZZN29BlockDescriptorRegStreamMSR2325prepareClientForTransformEP4taskbE20kalloc_type_view_877
+ _kernel_task
- _GLOBAL__sub_I_IosaDPEControlMSR26.cpp
- _GLOBAL__sub_I_IosaDPEControlMSR27.cpp
- _ZN19IosaDPEControlMSR267stopDPEEv
- _ZN19IosaDPEControlMSR268startDPEEv
- _ZN19IosaDPEControlMSR278startDPEEv
- _ZN22AppleM2ScalerCSCDriver40activateAndExecuteTransform_gatedContextEP18M2ScalerCSCRequestj
- _ZZN19IosaDPEControlMSR277stopDPEEvENK3$_0clE15registerGroup_t
- __ZL23IosaDPEControlMSR26_ktv
- __ZL23IosaDPEControlMSR27_ktv
- __ZN19IosaDPEControlMSR2610gMetaClassE
- __ZN19IosaDPEControlMSR2610superClassE
- __ZN19IosaDPEControlMSR267stopDPEEv
- __ZN19IosaDPEControlMSR268startDPEEv
- __ZN19IosaDPEControlMSR269MetaClassC1Ev
- __ZN19IosaDPEControlMSR269MetaClassC2Ev
- __ZN19IosaDPEControlMSR269MetaClassD0Ev
- __ZN19IosaDPEControlMSR269MetaClassD1Ev
- __ZN19IosaDPEControlMSR269metaClassE
- __ZN19IosaDPEControlMSR26C1EPK11OSMetaClass
- __ZN19IosaDPEControlMSR26C1Ev
- __ZN19IosaDPEControlMSR26C2EPK11OSMetaClass
- __ZN19IosaDPEControlMSR26C2Ev
- __ZN19IosaDPEControlMSR26D0Ev
- __ZN19IosaDPEControlMSR26D1Ev
- __ZN19IosaDPEControlMSR26D2Ev
- __ZN19IosaDPEControlMSR26dlEPvm
- __ZN19IosaDPEControlMSR26nwEm
- __ZN19IosaDPEControlMSR2710gMetaClassE
- __ZN19IosaDPEControlMSR2710superClassE
- __ZN19IosaDPEControlMSR277stopDPEEv
- __ZN19IosaDPEControlMSR278startDPEEv
- __ZN19IosaDPEControlMSR279MetaClassC1Ev
- __ZN19IosaDPEControlMSR279MetaClassC2Ev
- __ZN19IosaDPEControlMSR279MetaClassD0Ev
- __ZN19IosaDPEControlMSR279MetaClassD1Ev
- __ZN19IosaDPEControlMSR279metaClassE
- __ZN19IosaDPEControlMSR27C1EPK11OSMetaClass
- __ZN19IosaDPEControlMSR27C1Ev
- __ZN19IosaDPEControlMSR27C2EPK11OSMetaClass
- __ZN19IosaDPEControlMSR27C2Ev
- __ZN19IosaDPEControlMSR27D0Ev
- __ZN19IosaDPEControlMSR27D1Ev
- __ZN19IosaDPEControlMSR27D2Ev
- __ZN19IosaDPEControlMSR27dlEPvm
- __ZN19IosaDPEControlMSR27nwEm
- __ZNK19IosaDPEControlMSR2612getMetaClassEv
- __ZNK19IosaDPEControlMSR269MetaClass5allocEv
- __ZNK19IosaDPEControlMSR2712getMetaClassEv
- __ZNK19IosaDPEControlMSR279MetaClass5allocEv
- __ZTV19IosaDPEControlMSR26
- __ZTV19IosaDPEControlMSR27
- __ZTVN19IosaDPEControlMSR269MetaClassE
- __ZTVN19IosaDPEControlMSR279MetaClassE
- __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_3135
- __ZZN19AppleM2ScalerCSCHal22clearShadowMapperCacheEjE22kalloc_type_view_11042
- __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10972
- __ZZN19AppleM2ScalerCSCHal31mapShadowMapperCacheEntry_gatedE16ScalerMapperTypeP18IOMemoryDescriptorjE22kalloc_type_view_10978
- __ZZN19AppleM2ScalerCSCHal32updateShadowMapperCacheTTL_gatedEjyE22kalloc_type_view_11026
- __ZZN19IosaDPEControlMSR277stopDPEEvENK3$_0clE15registerGroup_t
- __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6292
- __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6271
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1726
- __ZZN22AppleM2ScalerCSCDriver4stopEP9IOServiceE21kalloc_type_view_1733
- __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_623
- __ZZN26IOSurfaceAcceleratorClient29transformSurface_asynchronousEP20TransformSurfaceDataE20kalloc_type_view_684
- __ZZN26IOSurfaceAcceleratorClient40asynchronousUserClientCompletionCallbackEPvS0_E20kalloc_type_view_591
CStrings:
+ " >>>> Client %d (%p) (%s) filters %p, Scaling filters %p\n"
+ "\"[%s] \" \"MailBox[%d] credit return_inc check failed on wake\\n\" @%s:%d"
+ "\"[%s] \" \"MailBox[6] credit return_inc check failed on transform completion (req: %d)\\n\" @%s:%d"
+ "%s %s, src to dst ratio index=%d%s:      %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator/FirmwareControl/IosaFirmwareControlMSR27Rtk.cpp"
+ "1111222"
+ "121111121222121211111111111221221121121212212222"
+ "12122121221212212122121221212212122121221212212122121221212212122120000020000000122112221200000020000000211112112222211222221122222112222211222221122222112222211222221122222111122211112221111222111122211112221111222111122211112222211212000020000000"
+ "ActiveWindow partiton %dx%d (src %dx%d dst %dx%d rot %d): Dest AW dimension %dx%d\n"
+ "Allocated MailBox: %p (instance id: %d)\n"
+ "Custom Chroma Filter :\n"
+ "Custom Filter :\n"
+ "Failed to allocate ta_pool\n"
+ "MSR Message Box link bring up!\n"
+ "MSR Message Box teardown - STATIC_IDLE_STATUS.static_gate_ready timed out\n"
+ "MSRCPU: IMEM verified against embedded image (%zu words)\n"
+ "MSRCPU: IMEM verify failed: %zu/%zu words mismatched\n"
+ "MSRCPU: IMEM verify mismatch at word %zu: wrote %08X, read %08X\n"
+ "MailBox[%u] outbox drain did not complete\n"
+ "No"
+ "Scaler[%d] startDPE() done\n"
+ "Scaler[%d] stopDPE() done\n"
+ "Yes"
+ "drainOutboxMessages"
+ "findCustomFilterCoefficientsAtNeighboringBin"
+ "site.TileArray"
+ "tearDownMsrMessageBoxLinks_gatedContext"
+ "transform (%dx%d)->(%dx%d): A dimension has src to dst ratio %s%d.%s%u (bin %d) for %s %s has set a custom filter flag without custom coefficients; falling back to default filter for this axis\n"
+ "transform (%dx%d)->(%dx%d): src to dst ratio %s%d.%s%u for %s %s landed on bin %d with no coefficients; using neighboring bin %d instead to absorb client ratio quantization noise\n"
+ "updateWithAllCoefficientsCopy: client=%d (%p) %s: raw hDstToSrcRatio=0x%x vDstToSrcRatio=0x%x (diff=%d) -> hSrcToDstRatioIndex=%d vSrcToDstRatioIndex=%d\n"
- "%s %s, src to dst ratio index=%d%s:\n"
- "%s: TODO\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR26.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator/DPEControl/IosaDPEControlMSR27.cpp"
- "12111112122212121111111111122122112112112212222"
- "12122121221212212122121221212212122121221212212122121221212212122120000020000000122112221200000020000000211112112222211222221122222112222211222221122222112222211222221122222111122211112221111222111122211112221111222111122211112222211200000020000000"
- "ActiveWindow partiton on (%s) %dx%d: Dest AW dimension %dx%d\n"
- "Allocated MailBox: %p\n"
- "IosaDPEControlMSR26"
- "IosaDPEControlMSR27"
- "No filter coefficients!\n"
- "site.IosaDPEControlMSR26"
- "site.IosaDPEControlMSR27"
- "transform (%dx%d)->(%dx%d): A dimension has src to dst ratio %s%d.%s%u (bin %d) for %s %s has set a custom filter flag without custom coefficients\n"
- "virtual void IosaDPEControlMSR26::startDPE()"
- "virtual void IosaDPEControlMSR26::stopDPE()"
```
