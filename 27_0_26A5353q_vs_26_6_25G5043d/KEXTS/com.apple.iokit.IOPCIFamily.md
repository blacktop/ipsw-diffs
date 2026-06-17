## com.apple.iokit.IOPCIFamily

> `com.apple.iokit.IOPCIFamily`

```diff

-762.0.0.0.0
-  __TEXT.__const: 0xf18 sha256:c73dd6523a1b567aba912a90413b156a1243078cb80db139a67288d62f63360c
-  __TEXT.__cstring: 0x76ed sha256:8519b3282583f11d6a0bc890bed7d87a26a258ed52e0db9573a5113706b644f1
-  __TEXT.__os_log: 0x5085 sha256:1af75e0c25891e4c92d7ea73139f371ab1a9bcbfb5ba2f3ffeac99ff844b465b
-  __TEXT_EXEC.__text: 0x43810 sha256:fc74d160829a8d33fb741b7466d4cdf39b6b29dfa23d6df98a6fafdf8e346fd0
+726.100.6.0.0
+  __TEXT.__const: 0xe50 sha256:c235862187b0f36df327483237b2051533a590e3e1500d5dea0249568a87da19
+  __TEXT.__cstring: 0x74e1 sha256:8088bd73115b975d2cfd0c45e680bbbf765d2657cfb7b656d768a2b7a4c6845b
+  __TEXT.__os_log: 0x4e6f sha256:0d4ec7d04152888d6cad57e7e689b8172f325a6a68d98e9f8a7007b08fa0cb20
+  __TEXT_EXEC.__text: 0x4163c sha256:ae460b0919629d86e9f30edc23a89801f20a086ce4d54854616ad0f7560a1657
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xcc sha256:ac11447ef440d57cf86090ad02806ced56445c031fd9e449c3f286e3e3652acc
+  __DATA.__data: 0xcc sha256:f1a81d34c44ad9b7477fd77374cb8cfd63d97a0c831ce64803887d820741db04
   __DATA.__common: 0x430 sha256:482500ac4ba894ac24dbc1e3e06f5455e570378d55808949294af424208dff4c
-  __DATA_CONST.__mod_init_func: 0x20 sha256:933ac3ca76821bc748e3352ea23c4a62b418fcd79d037d1b51b3fa9607ceea39
-  __DATA_CONST.__mod_term_func: 0x20 sha256:b519c56a0d0b7c35a114b3a40f7d79d2938ad1623c0a6eb21bf81cb2ebc02b6b
-  __DATA_CONST.__const: 0x6088 sha256:efae2c9c3597df165d5ade7f6a52e0320c4fd81a80bd65fffecd8f65ea7f657d
-  __DATA_CONST.__kalloc_type: 0x600 sha256:065f880ba67018051b015f6ebc3a10a165081c0730a44752c112cc015e687456
-  __DATA_CONST.__kalloc_var: 0x190 sha256:ac788ce839598d7fcd25d570b28296d8ae0c9d480494b070ebd6bc5f999cecf1
-  __DATA_CONST.__auth_got: 0x4b0 sha256:63885d08089b1d83f5f6ec5b4b035aeed7ba3cbc6c66b00f79cd8aca836760b4
-  __DATA_CONST.__got: 0x100 sha256:898e5e8a62c5d2af2f1c8f9d087b7230a68c970b7d3039f092352dc3440fd559
-  __DATA_CONST.__auth_ptr: 0x8 sha256:d04454093fc829833baf8aeea5033a2d07c5cf358a839ed15e9357ab5cbdaacf
-  __LINKINFO.__symbolsets: 0x6518 sha256:ea9da37edf7f7aab504853b85225fe95d5e95aafc56236063ed94d7151e49fd2
-  UUID: D6B4606E-0D26-37AB-8867-E2278088BDCF
-  Functions: 785
-  Symbols:   1788
-  CStrings:  1101
+  __DATA_CONST.__auth_got: 0x488 sha256:6d96e99347be52319c854c27a1539462ee1b24cc212259c9ac83e9713f850544
+  __DATA_CONST.__got: 0x108 sha256:9ce80a602dc81618455ea1703ee445c1fb23701c724d7827e8dd03349f11a49b
+  __DATA_CONST.__auth_ptr: 0x8 sha256:69c2762952ef04001cab1e0549e47e6e4d04f2637d7233a28f3ec8041b5b956d
+  __DATA_CONST.__mod_init_func: 0x20 sha256:9cdd1320303f862f1a6035275d0358c310f27aa196c1497d5cbc4d5e878ddc39
+  __DATA_CONST.__mod_term_func: 0x20 sha256:e469d4607132570bbc76f2c06e17ec40db2c2e70cdeacb180016f691fda44d2b
+  __DATA_CONST.__const: 0x6028 sha256:35593eac6d6290ea0f781f7c5d0e44fe59d3bc78d88f473bf8f3a67920e90a19
+  __DATA_CONST.__kalloc_type: 0x600 sha256:c3d71ef17a340c26306e8518561c5ddc9d3a3a0f1b189677ebf6517cbe2c3e2c
+  __DATA_CONST.__kalloc_var: 0x190 sha256:aa2d9b123915fd0f6a8b9b54589689e6618c555561b55d7a7e7b856887a4f0fe
+  __LINKINFO.__symbolsets: 0x639f sha256:c7d38b8583e979da1f1eac9855ba6e3c3b39e5ffaaff48ef60456dffcb50d922
+  UUID: 00C0DA25-0161-3AA0-9DC9-FA8BF2197B8B
+  Functions: 771
+  Symbols:   1760
+  CStrings:  1083
 
Symbols:
+ __ZN11IOPCIDevice14isInitializingEv
+ __ZN11IOPCIDevice15busyStateChangeEPvS0_jP9IOServiceS0_m
+ __ZN11IOPCIDevice17pauseTimerHandlerEP18IOTimerEventSource
+ __ZN14IOPMrootDomain19getPMAssertionLevelEy
+ __ZN21IOPCITraceEventBuffer16logPCITraceEventEtPvm
+ __ZN21IOPCITraceEventBuffer29logPCITraceEventWithTimestampEtPvm
+ __ZZN11IOPCIBridge10publishNubEP11IOPCIDevicejE21kalloc_type_view_3218
+ __ZZN11IOPCIBridge17createEventSourceEP8OSObjectPFvS1_P16IOPCIEventSourcePK10IOPCIEventEjE21kalloc_type_view_6299
+ __ZZN11IOPCIBridge4freeEvE21kalloc_type_view_1431
+ __ZZN11IOPCIBridge4initEP12OSDictionaryE21kalloc_type_view_1417
+ __ZZN11IOPCIDevice12initReservedEvE20kalloc_type_view_466
+ __ZZN11IOPCIDevice13initiatePauseEvE11_os_log_fmt_0
+ __ZZN11IOPCIDevice15busyStateChangeEPvS0_jP9IOServiceS0_mE11_os_log_fmt
+ __ZZN11IOPCIDevice31_CopyDeviceMemoryWithIndex_ImplEyPP18IOMemoryDescriptorP9IOServiceE11_os_log_fmt
+ __ZZN11IOPCIDevice31_CopyDeviceMemoryWithIndex_ImplEyPP18IOMemoryDescriptorP9IOServiceE11_os_log_fmt_0
+ __ZZN11IOPCIDevice31_CopyDeviceMemoryWithIndex_ImplEyPP18IOMemoryDescriptorP9IOServiceE11_os_log_fmt_1
+ __ZZN11IOPCIDevice31_CopyDeviceMemoryWithIndex_ImplEyPP18IOMemoryDescriptorP9IOServiceE11_os_log_fmt_2
+ __ZZN11IOPCIDevice4freeEvE20kalloc_type_view_499
+ __ZZN11IOPCIDevice4freeEvE20kalloc_type_view_517
+ __ZZN15IOPCI2PCIBridge21startBridgeInterruptsEP9IOServiceE21kalloc_type_view_5680
+ __ZZN15IOPCI2PCIBridge4stopEP9IOServiceE21kalloc_type_view_6094
+ __ZZN16IOPCIEventSource4freeEvE21kalloc_type_view_6436
+ __ZZN17IOPCIConfigurator10createRootEvE20kalloc_type_view_561
+ __ZZN17IOPCIConfigurator13addHostBridgeEP15IOPCIHostBridgeE20kalloc_type_view_589
+ __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2338
+ __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2385
+ __ZZN17IOPCIConfigurator17deleteConfigEntryEP16IOPCIConfigEntryE21kalloc_type_view_2105
+ __ZZN32IOPCIMessagedInterruptController19deallocateInterruptEjE20kalloc_type_view_798
+ __block_descriptor_tmp.319
+ __block_descriptor_tmp.361
+ _gIOBusyInterest
- _OUTLINED_FUNCTION_1
- __Block_object_assign
- __Block_object_dispose
- __ZL22addCapOffsetArrayEntryPK8OSSymboljP7OSArray
- __ZN11IOMemoryMap18getPhysicalAddressEv
- __ZN11IOPCIDevice16lookupCapabilityEjPjPt
- __ZN11IOPCIDevice17waitForPauseReadyEPv
- __ZN11IOPCIDevice18__CopyDeviceMemoryEyPP18IOMemoryDescriptorP9IOServiceb
- __ZN11IOPCIDevice28_CopyWCDeviceMemoryWithIndexEyPP18IOMemoryDescriptorP9IOServicePFiP15OSMetaClassBase5IORPCE
- __ZN11IOPCIDevice33_CopyWCDeviceMemoryWithIndex_ImplEyPP18IOMemoryDescriptorP9IOService
- __ZN11IOPCIDevice35_CopyWCDeviceMemoryWithIndex_InvokeE5IORPCP15OSMetaClassBasePFiS2_yPP18IOMemoryDescriptorP9IOServiceE
- __ZN15IOPCIHostBridge13probeRootPortE17IOPCIAddressSpace
- __ZN18IOMemoryDescriptor18getPhysicalAddressEv
- __ZN18IORegistryIterator11iterateOverEP15IORegistryEntryPK15IORegistryPlanej
- __ZNK11IOPCIBridge11getWorkLoopEv
- __ZNK11IOPCIDevice11getWorkLoopEv
- __ZZN11IOPCIBridge10publishNubEP11IOPCIDevicejE21kalloc_type_view_3263
- __ZZN11IOPCIBridge17createEventSourceEP8OSObjectPFvS1_P16IOPCIEventSourcePK10IOPCIEventEjE21kalloc_type_view_6401
- __ZZN11IOPCIBridge4freeEvE21kalloc_type_view_1446
- __ZZN11IOPCIBridge4initEP12OSDictionaryE21kalloc_type_view_1432
- __ZZN11IOPCIDevice12initReservedEvE20kalloc_type_view_472
- __ZZN11IOPCIDevice16lookupCapabilityEjPjPtE11_os_log_fmt
- __ZZN11IOPCIDevice16lookupCapabilityEjPjPtE11_os_log_fmt_0
- __ZZN11IOPCIDevice17waitForPauseReadyEPvE11_os_log_fmt
- __ZZN11IOPCIDevice17waitForPauseReadyEPvE11_os_log_fmt_0
- __ZZN11IOPCIDevice17waitForPauseReadyEPvE11_os_log_fmt_1
- __ZZN11IOPCIDevice17waitForPauseReadyEPvE11_os_log_fmt_2
- __ZZN11IOPCIDevice18__CopyDeviceMemoryEyPP18IOMemoryDescriptorP9IOServicebE11_os_log_fmt
- __ZZN11IOPCIDevice18__CopyDeviceMemoryEyPP18IOMemoryDescriptorP9IOServicebE11_os_log_fmt_0
- __ZZN11IOPCIDevice18__CopyDeviceMemoryEyPP18IOMemoryDescriptorP9IOServicebE11_os_log_fmt_1
- __ZZN11IOPCIDevice4freeEvE20kalloc_type_view_505
- __ZZN11IOPCIDevice4freeEvE20kalloc_type_view_543
- __ZZN15IOPCI2PCIBridge21startBridgeInterruptsEP9IOServiceE21kalloc_type_view_5766
- __ZZN15IOPCI2PCIBridge4stopEP9IOServiceE21kalloc_type_view_6196
- __ZZN16IOPCIEventSource4freeEvE21kalloc_type_view_6538
- __ZZN17IOPCIConfigurator10createRootEvE20kalloc_type_view_588
- __ZZN17IOPCIConfigurator13addHostBridgeEP15IOPCIHostBridgeE20kalloc_type_view_675
- __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE11_os_log_fmt_7
- __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2443
- __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2490
- __ZZN17IOPCIConfigurator17deleteConfigEntryEP16IOPCIConfigEntryE21kalloc_type_view_2210
- __ZZN17IOPCIConfigurator8configOpEP9IOServicemPvS2_E11_os_log_fmt_5
- __ZZN17IOPCIConfigurator8configOpEP9IOServicemPvS2_E11_os_log_fmt_6
- __ZZN32IOPCIMessagedInterruptController19deallocateInterruptEjE20kalloc_type_view_799
- __ZZZN11IOPCIDevice16lookupCapabilityEjPjPtEUb0_E11_os_log_fmt
- __ZZZN11IOPCIDevice17waitForPauseReadyEPvEUb_E11_os_log_fmt
- ____ZN11IOPCIDevice16lookupCapabilityEjPjPt_block_invoke
- ____ZN11IOPCIDevice17waitForPauseReadyEPv_block_invoke
- ___copy_helper_block_8_32r
- ___copy_helper_block_8_32r40r
- ___destroy_helper_block_8_32r
- ___destroy_helper_block_8_32r40r
- __block_descriptor_tmp.151
- __block_descriptor_tmp.318
- __block_descriptor_tmp.360
- __block_descriptor_tmp.65
- _thread_call_cancel_wait
CStrings:
+ "1111122222211111111111122222222222111112222222111"
+ "1211111212221212111211111111112111122121222121"
+ "222222222212221112122111111111111112112212221121121112"
+ "22:44:58"
+ "Jun  9 2026"
+ "[PCIe:%u %llu ns] %s(0x%qx) still initializing, deferring pause\n"
+ "[PCIe:%u %llu ns] IOPCIDevice::%s: offload engine requires using _MemoryAccess()\n"
+ "[PCIe:%u %llu ns] [%s()] nub %s(0x%qx) has busy state %u\n"
+ "_CopyDeviceMemoryWithIndex_Impl"
+ "busyStateChange"
- "01:40:09"
- "11111222222111111111111222222222221111122222221112"
- "12111112122212121112111111111121111221221222121"
- "22222222222122211121221111111111111111111111111111211221222112111221"
- "May 27 2026"
- "[PCIe:%u %llu ns] %s(0x%qx) is not busy, checking power-plane\n"
- "[PCIe:%u %llu ns] %s(0x%qx) power children set changed (%u->%u)\n"
- "[PCIe:%u %llu ns] %s(0x%qx) sleeping for %u ms\n"
- "[PCIe:%u %llu ns] Limiting the root port's MPS to 0x%x\n"
- "[PCIe:%u %llu ns] Looking up capability 0x%x\n"
- "[PCIe:%u %llu ns] No symbol found for capability 0x%x\n"
- "[PCIe:%u %llu ns] Unexpected error: no offset found for capability 0x%x\n"
- "[PCIe:%u %llu ns] [ PCI configuration begin (scanning %u:%u:XX) ]\n"
- "[PCIe:%u %llu ns] [%s()] Unexpected error: nub %s's pause thread is already pending execution\n"
- "[PCIe:%u %llu ns] waitQuiet() timed out after %llu seconds, attempting pause\n"
- "__CopyDeviceMemory"
- "capability"
- "initiatePause"
- "offset"
- "pci-mps-limit"
- "pci-mps-limit=<domain>,<value>[;<domain>,<value>]"

```
