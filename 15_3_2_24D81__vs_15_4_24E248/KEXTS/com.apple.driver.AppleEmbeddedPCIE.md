## com.apple.driver.AppleEmbeddedPCIE

> `com.apple.driver.AppleEmbeddedPCIE`

```diff

-824.60.9.0.0
-  __TEXT.__cstring: 0x57b3
+824.100.33.0.0
+  __TEXT.__cstring: 0x5bce
   __TEXT.__const: 0x198
-  __TEXT_EXEC.__text: 0x14448
+  __TEXT_EXEC.__text: 0x16e7c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x188
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x46e0
+  __DATA_CONST.__const: 0x4768
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: DC376290-C451-3480-81AA-AABD7BC88560
-  Functions: 491
-  Symbols:   1192
-  CStrings:  587
+  UUID: DF063CA2-9FF3-37A7-AC12-01F45D34902E
+  Functions: 520
+  Symbols:   1232
+  CStrings:  614
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _ZN17AppleEmbeddedPCIE14_waitForLinkUpEjjjb.cold.1
+ _ZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntry.cold.15
+ _ZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntry.cold.16
+ _ZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntry.cold.17
+ _ZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntry.cold.18
+ __ZN11ApplePIODMA9metaClassE
+ __ZN17AppleEmbeddedPCIE14_waitForLinkUpEjjjb
+ __ZN17AppleEmbeddedPCIE16cacheBusApertureE17IOPCIAddressSpacehjj
+ __ZN17AppleEmbeddedPCIE16deviceMemoryReadEP18IOMemoryDescriptoryPvy
+ __ZN17AppleEmbeddedPCIE16deviceMemoryReadEP18IOMemoryDescriptoryS1_yy
+ __ZN18IOMemoryDescriptor18getPhysicalAddressEv
+ __ZN21AppleEmbeddedPCIEPort11configRead8E17IOPCIAddressSpacehPh
+ __ZN21AppleEmbeddedPCIEPort12configRead16E17IOPCIAddressSpacehPt
+ __ZN21AppleEmbeddedPCIEPort12configRead32E17IOPCIAddressSpacehPj
+ __ZN21AppleEmbeddedPCIEPort12configWrite8E17IOPCIAddressSpacehh
+ __ZN21AppleEmbeddedPCIEPort13configWrite16E17IOPCIAddressSpaceht
+ __ZN21AppleEmbeddedPCIEPort13configWrite32E17IOPCIAddressSpacehj
+ __ZN21AppleEmbeddedPCIEPort16deviceMemoryReadEP18IOMemoryDescriptoryPvy
+ __ZN21AppleEmbeddedPCIEPort16deviceMemoryReadEP18IOMemoryDescriptoryS1_yy
+ __ZN21AppleEmbeddedPCIEPort17_setAppclkAutoDisEb
+ __ZN21AppleEmbeddedPCIEPort20_invokeClientHandlerE34AppleEmbeddedPCIEErrorHandlerEventb
+ __ZN21AppleEmbeddedPCIEPort23getLinkRcvryDebugTracerEPvPj
+ __ZN21AppleEmbeddedPCIEPort23getLinkSpeedDebugTracerEPvPj
+ __ZN21AppleEmbeddedPCIEPort26_captureLinkRcvryDebugHistEv
+ __ZN21AppleEmbeddedPCIEPort26_resetLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27_enableLinkRcvryDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27_enableLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27captureLinkRcvryDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort27captureLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort28_captureLinkRcvryDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort28_captureLinkRcvryDebugTracerEv_vfpthunk_
+ __ZN21AppleEmbeddedPCIEPort28_captureLinkSpeedDebugTracerEv
+ __ZN21AppleEmbeddedPCIEPort28_captureLinkSpeedDebugTracerEv_vfpthunk_
+ __ZN27AppleEmbeddedPCIEUserClient21extGetLinkRcvryTracerEP25IOExternalMethodArguments
+ __ZN27AppleEmbeddedPCIEUserClient21extGetLinkSpeedTracerEP25IOExternalMethodArguments
+ __ZN9IOService15serviceMatchingEPKcP12OSDictionary
+ __ZN9IOService9waitQuietEy
+ __ZNK17AppleEmbeddedPCIE29getPortFromConfigSpaceAddressE17IOPCIAddressSpace
+ __ZZN17AppleEmbeddedPCIE18_resetMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1286
+ __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1244
+ __ZZN17AppleEmbeddedPCIE5startEP9IOServiceE20kalloc_type_view_354
+ __ZZN17AppleEmbeddedPCIE9_tearDownEvE20kalloc_type_view_402
+ __ZZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntryE20kalloc_type_view_320
+ _gIOParentMatchKey
+ _gIOPlatformHaltRestartActionKey
+ _ml_at_interrupt_context
+ _ml_get_interrupts_enabled
- _ZN17AppleEmbeddedPCIE9configureEP9IOService.cold.2
- __ZN17AppleEmbeddedPCIE14_waitForLinkUpEjjj
- __ZN21AppleEmbeddedPCIEPort20_invokeClientHandlerE34AppleEmbeddedPCIEErrorHandlerEvent
- __ZZN17AppleEmbeddedPCIE18_resetMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1200
- __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1158
- __ZZN17AppleEmbeddedPCIE5startEP9IOServiceE20kalloc_type_view_353
- __ZZN17AppleEmbeddedPCIE9_tearDownEvE20kalloc_type_view_401
- __ZZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntryE20kalloc_type_view_319
CStrings:
+ "\"[%s()] Internal error: invalid size %u\" @%s:%d"
+ "12111112122212121111112111122111111111111111111111112122222222111211222211111112222222222222222222222222222222222122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122122121222222222222222222222222222222222222222222222222222222222222222222111222121"
+ "AppleEmbeddedPCIE::%s Terminating port's link partner nub\n\n"
+ "ApplePIODMA"
+ "_captureLinkRcvryDebugHist"
+ "_captureLinkRcvryDebugTracer"
+ "_captureLinkSpeedDebugTracer"
+ "_commandGate->commandSleep(&shouldWake, deadline, THREAD_UNINT) == THREAD_TIMED_OUT"
+ "_configBaseDescriptor != nullptr"
+ "_enableLinkRcvryDebugTracer"
+ "_enableLinkSpeedDebugTracer"
+ "_piodma != nullptr"
+ "_resetLinkSpeedDebugTracer"
+ "apcie-piodma"
+ "apcie-piodma-disable"
+ "apcie-piodma-sid"
+ "apcie[%u:%s]::%s %lu nanoseconds elapsed between correctable errors\n"
+ "apcie[%u:%s]::%s AppleEmbeddedPCIEPort::%s %02x:%02x:%02x[%04x] (0x%llx/0x%llx) -> %08x\n"
+ "apcie[%u:%s]::%s Link Recovery Debug Tracer not supported\n\n"
+ "apcie[%u:%s]::%s Link Speed Debug Tracer not supported\n\n"
+ "apcie[%u:%s]::%s no PIODMA engine associated with this port\n\n"
+ "cacheBusAperture"
+ "getLinkRcvryDebugTracer"
+ "getLinkSpeedDebugTracer"
+ "phandleDictionary != nullptr"
+ "pioDmaMatchingDictionary != nullptr"
+ "terminate-missing-endpoint"
+ "void AppleEmbeddedPCIE::_waitForLinkUp(uint32_t, uint32_t, uint32_t, bool)"
- "1211111212221212111111211112211111111111111111111121222222221112112222111111122222222222222222222222222222222221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221212222222222222222222222222222222222222222222222222222222222222222221112"

```
