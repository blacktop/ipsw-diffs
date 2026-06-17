## com.apple.driver.AppleEmbeddedPCIE

> `com.apple.driver.AppleEmbeddedPCIE`

```diff

-1039.0.0.0.0
-  __TEXT.__cstring: 0x714e sha256:4f793d0a6b1b2b1cdb4791783825f7147d774b1949b8f4b521386bf420593f4f
-  __TEXT.__os_log: 0x32d9 sha256:59cd6fc8f125b93df65cb11e348dd16093a0bced2869d1623ad5617351045463
+936.100.34.0.0
+  __TEXT.__cstring: 0x6a22 sha256:ec0f9d8bdf8e835a12ece3d137a431840edd835b1aa4ada8930d21626e366fb5
+  __TEXT.__os_log: 0x2ef3 sha256:61f71fd6151f7922edd34e553277f4916a3b0bef3cc1093077a72e46077d8cff
   __TEXT.__const: 0x178 sha256:2647ec82fe57ca85a37a265c8559553ab768dd9574416e30857e1ba7ef8ffe06
-  __TEXT_EXEC.__text: 0x3406c sha256:5d7f13cb677b7246e63f4d3783341c0079979ae859b3ed2066bb62a31b6dad19
+  __TEXT_EXEC.__text: 0x30cdc sha256:fd221dade31b4ca06a48ef1d30cbd91c34d88b9bf71b935a6fd61802f5c77a89
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3d8 sha256:600d081f3935953b0d9eae0c8ceaa212360f97fcc020b83b264fe44f98a3a468
+  __DATA.__data: 0x3d8 sha256:792e67885ebb4ebb7420068e9bc55885069197c3df33e82dbe95dd5ad62ecdf2
   __DATA.__common: 0x188 sha256:3eefc4790b52024832ea4c03c6e7a781f3ef9416866a959b2777fce101ad9d61
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__mod_init_func: 0x40 sha256:429f4bdb4df46eb76edf3b5cf31c94b665b7c545a89959a03ba45ca82c802fa3
-  __DATA_CONST.__mod_term_func: 0x40 sha256:4e61cf98291931a47ea3fb14642e07a51dd396c06169e64e55679d91bf30699f
-  __DATA_CONST.__const: 0x4558 sha256:733a4b9fbf64ad3de1618119314b765d1eae10e01c8f9bb51e4c6dd2907f4ec4
-  __DATA_CONST.__kalloc_type: 0x280 sha256:825c11c70e9e2f115ec178467f2afaa312bf915d2dd3eb7bbf8148e6f059c458
-  __DATA_CONST.__kalloc_var: 0x140 sha256:c8736b88b85871d7cd20d1b7658037c9e4c8a42f71432e6f111888d730ddd6d2
-  __DATA_CONST.__auth_got: 0x498 sha256:3bc25ef2b08e77f453860b98a1bdd9364d7f4d447fa6e739d62305f56b4c97d7
-  __DATA_CONST.__got: 0x190 sha256:d4242dcf0a4c156a3c7b6c4074e74c1bda904970dde5b11e8896cfbc7012051e
-  UUID: CFCEEB95-1C55-3737-B829-BD7CB5F75727
-  Functions: 504
-  Symbols:   1382
-  CStrings:  802
+  __DATA_CONST.__auth_got: 0x470 sha256:5205815acf6fdf9a4f47e6138f3718489ca0cbd9b2a9b9f32d098a4bfb81dcac
+  __DATA_CONST.__got: 0x190 sha256:5fbeed7f3c2b378bdb64c948833f334ea1ad14790c40ccdc8730a6bb7e9b19c2
+  __DATA_CONST.__mod_init_func: 0x40 sha256:dc511d54c826485bed38b6e7335d7e45ff146fcf4ba7bda160c2315565512c17
+  __DATA_CONST.__mod_term_func: 0x40 sha256:5d707698fa0f7cd822f3f5fa28428f8421aa0a3cdf65a56ab0057cc1e42014dc
+  __DATA_CONST.__const: 0x4490 sha256:41108eee6af611a52b103f653ff317846779b43fb8108b1aed71fb15ceefd28d
+  __DATA_CONST.__kalloc_type: 0x280 sha256:69f3e2c1c28745aaace97f041615d04ec6202924ab3c67b3234ef54fcf7c04df
+  __DATA_CONST.__kalloc_var: 0x140 sha256:c2af938761b5a27ae995a0df4916b3b4631ca4a60b398dca8627a2da9b3555d2
+  UUID: 3400CD6A-FA2B-3BE1-A3DC-AFC66CD041A5
+  Functions: 464
+  Symbols:   1324
+  CStrings:  767
 
Symbols:
+ __ZN17AppleEmbeddedPCIE14_waitForLinkUpEjjjb
+ __ZN21AppleEmbeddedPCIEPort32handleCompletionTimeoutInterruptEj
+ __ZNK17AppleEmbeddedPCIE15getLtssmTimeoutEv
+ __ZZN17AppleEmbeddedPCIE14_waitForLinkUpEjjjbE11_os_log_fmt
+ __ZZN17AppleEmbeddedPCIE14_waitForLinkUpEjjjbE11_os_log_fmt_0
+ __ZZN17AppleEmbeddedPCIE14_waitForLinkUpEjjjbE11_os_log_fmt_1
+ __ZZN17AppleEmbeddedPCIE18_resetMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1365
+ __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1323
+ __ZZN17AppleEmbeddedPCIE5startEP9IOServiceE20kalloc_type_view_367
+ __ZZN17AppleEmbeddedPCIE9_tearDownEvE20kalloc_type_view_418
+ __ZZN21AppleEmbeddedPCIEPort15handleInterruptEP22IOInterruptEventSourceiE11_os_log_fmt_1
+ __ZZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntryE20kalloc_type_view_317
- __Z14resolvePHandleP9IOServicePKcS2_y
- __ZL10extractBust
- __ZL10extractDevt
- __ZL10extractFnct
- __ZL23constructAERPanicStringjjPcm
- __ZN15IOPCIHostBridge13probeRootPortE17IOPCIAddressSpace
- __ZN16APCIEPortControl21isBadRequestErrorTypeE36AppleEmbeddedPCIEBadRequestErrorType
- __ZN16AppleARMFunction8DispatchE5IORPC
- __ZN17AppleEmbeddedPCIE12systemActiveEv
- __ZN17AppleEmbeddedPCIE13probeRootPortEj
- __ZN17AppleEmbeddedPCIE13setDebugFlagsEv
- __ZN17AppleEmbeddedPCIE14_waitForLinkUpEjjb
- __ZN17AppleEmbeddedPCIE16logPCITraceEventEtPvmb
- __ZN17AppleEmbeddedPCIE20_prepareForHibernateEv
- __ZN17AppleEmbeddedPCIE20_resumeFromHibernateEv
- __ZN21AppleEmbeddedPCIEPort14enableRootPortEj
- __ZN21AppleEmbeddedPCIEPort15disableRootPortEbbPj
- __ZN21AppleEmbeddedPCIEPort15getLtssmTimeoutEv
- __ZN21AppleEmbeddedPCIEPort15handlePLCEErrorEi
- __ZN21AppleEmbeddedPCIEPort16linkDownRecoveryEv
- __ZN21AppleEmbeddedPCIEPort17handleRootTimeoutE34AppleEmbeddedPCIEErrorHandlerEventbPKcS2_
- __ZN21AppleEmbeddedPCIEPort18enableLinkTrainingEb
- __ZN21AppleEmbeddedPCIEPort18reenableThreadCallEP11thread_call
- __ZN21AppleEmbeddedPCIEPort19isMSIErrorInterruptEj
- __ZN21AppleEmbeddedPCIEPort19lookupPerstFunctionEP15IORegistryEntry
- __ZN21AppleEmbeddedPCIEPort19simulateLinkTimeoutEv
- __ZN21AppleEmbeddedPCIEPort20launchReenableThreadEv
- __ZN21AppleEmbeddedPCIEPort20readAERErrorSourceIDEPj
- __ZN21AppleEmbeddedPCIEPort21allowPanicOnRPCorrErrEv
- __ZN21AppleEmbeddedPCIEPort22_captureDiagnosticDataEv
- __ZN21AppleEmbeddedPCIEPort22allocateMSIVectorRangeEyy
- __ZN21AppleEmbeddedPCIEPort22ignoreCorrectableErrorEv
- __ZN21AppleEmbeddedPCIEPort22ignoreUnexpectedLinkUpEv
- __ZN21AppleEmbeddedPCIEPort22isRdDataErrorInterruptEj
- __ZN21AppleEmbeddedPCIEPort23setLinkTimeoutThresholdEj
- __ZN21AppleEmbeddedPCIEPort24isRIDToSIDErrorInterruptEj
- __ZN21AppleEmbeddedPCIEPort24isRxRequestAddrInterruptEj
- __ZN21AppleEmbeddedPCIEPort25isLTSSMEnClearedInterruptEj
- __ZN21AppleEmbeddedPCIEPort25simulateCompletionTimeoutEv
- __ZN21AppleEmbeddedPCIEPort26handleLinkTimeoutInterruptEv
- __ZN21AppleEmbeddedPCIEPort28isMSIDataMiscompareInterruptEj
- __ZN21AppleEmbeddedPCIEPort30isMalformedMMURequestInterruptEj
- __ZN21AppleEmbeddedPCIEPort32handleCompletionTimeoutInterruptEv
- __ZN21IOPCITraceEventBuffer16logPCITraceEventEtPvmb
- __ZN27AppleEmbeddedPCIEUserClient14extInjectErrorEP25IOExternalMethodArguments
- __ZNK11IOPCIBridge11getWorkLoopEv
- __ZZN17AppleEmbeddedPCIE14_waitForLinkUpEjjbE11_os_log_fmt
- __ZZN17AppleEmbeddedPCIE14_waitForLinkUpEjjbE11_os_log_fmt_0
- __ZZN17AppleEmbeddedPCIE14_waitForLinkUpEjjbE11_os_log_fmt_1
- __ZZN17AppleEmbeddedPCIE18_resetMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1426
- __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE11_os_log_fmt
- __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE11_os_log_fmt_0
- __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE11_os_log_fmt_1
- __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE11_os_log_fmt_2
- __ZZN17AppleEmbeddedPCIE21_increaseMMIOTimeoutsEP21AppleEmbeddedPCIEPortP11IOPCIDeviceE21kalloc_type_view_1384
- __ZZN17AppleEmbeddedPCIE5startEP9IOServiceE20kalloc_type_view_384
- __ZZN17AppleEmbeddedPCIE9_tearDownEvE20kalloc_type_view_435
- __ZZN21AppleEmbeddedPCIEPort12_mapRIDToSIDEP11IOPCIDeviceE11_os_log_fmt__16_
- __ZZN21AppleEmbeddedPCIEPort17handleRootTimeoutE34AppleEmbeddedPCIEErrorHandlerEventbPKcS2_E11_os_log_fmt
- __ZZN21AppleEmbeddedPCIEPort22ignoreCorrectableErrorEvE11_os_log_fmt
- __ZZN21AppleEmbeddedPCIEPort29initWithAPCIeAndRegistryEntryEP17AppleEmbeddedPCIEP15IORegistryEntryE20kalloc_type_view_320
- __ZZN22ApplePCIEMSIController24allocateInterruptVectorsEP9IOServicejPyE11_os_log_fmt_2
- __ZZN22ApplePCIEMSIController24allocateInterruptVectorsEP9IOServicejPyE11_os_log_fmt_3
- __ZZN27AppleEmbeddedPCIEUserClient14extInjectErrorEP25IOExternalMethodArgumentsE11_os_log_fmt
- __ZZN27AppleEmbeddedPCIEUserClient14extInjectErrorEP25IOExternalMethodArgumentsE11_os_log_fmt_0
- ____ZN21AppleEmbeddedPCIEPort18reenableThreadCallEP11thread_call_block_invoke
- _thread_call_allocate
- _thread_call_enter1
- _thread_call_free
CStrings:
+ " root_err_status=0x%08x"
+ "12111112122212121111111111211222222222221112"
+ "1211111212221212111111211112211111111111111111111111121222222221112112222111111122222222222222222222222222222222221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221212222222222222222222222222222222222222222222222222222222222222222221112222212111212212"
+ "1211111212221212111112121222222112221122111111121122211111112211221222"
+ "AF/Link timeout"
+ "CA interrupt debug"
+ "Port error interrupt"
+ "[%s()] Failed to get device memory for nub %s, skipping mmio timeout increase\n"
+ "[%s()] Failed to map IODeviceMemory, skipping mmio timeout increase\n"
+ "handleCompletionTimeoutInterrupt"
+ "ml_io_increase_timeouts_phys(0x%lx, %u, %u, %u) %s\n"
+ "void AppleEmbeddedPCIE::_waitForLinkUp(uint32_t, uint32_t, uint32_t, bool)"
- " root_err_status=0x%08x COR source: %u:%u:%u"
- " root_err_status=0x%08x COR source: %u:%u:%u, UNC source: %u:%u:%u"
- " root_err_status=0x%08x UNC source: %u:%u:%u"
- " root_err_status=0x%08x err_src_id: 0x%08x"
- "\"manual-enable-defer-scan is only supported on manual-enable links\" @%s:%d"
- "121111121222121211111111112112222222222211122"
- "121111121222121211111121111221111111111111111111111112122222222111211222221111111222222222222222222222222222222222212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212122222222222222222222222222222222222222222222222222222222222222222211122222121112122122"
- "121111121222121211111212122222211222112211111112112221111111221122122"
- "Completion error interrupt"
- "Completion timeout count"
- "IOReturn AppleEmbeddedPCIEPort::reenableThreadCall(thread_call_t)_block_invoke"
- "Link timeout"
- "Link timeout count"
- "[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s [%s()] Failed to get device memory for nub %s, skipping mmio timeout increase\n\n"
- "[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s [%s()] Failed to map IODeviceMemory, skipping mmio timeout increase\n\n"
- "[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s ml_io_increase_timeouts_phys(0x%lx, %u, %u, %u) %s\n\n"
- "[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s Invalid error injection type %u\n"
- "[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s Invalid timeout injection subtype %u\n"
- "[PCIe:%u %llu ns] ApplePCIEMSIController::%s Attempting to allocate %u reserved MSI vector(s), starting at vector %u, for port %d\n"
- "[PCIe:%u %llu ns] ApplePCIEMSIController::%s Warning: the EP driver requested fewer MSIs (%u) than were reserved (%u)\n"
- "[PCIe:%u %llu ns] apcie[%u:%s]::%s Reached max allowed timeouts\n"
- "[PCIe:%u %llu ns] apcie[%u:%s]::%s Using static SID for device %p RID 0x%04x(%d:%d:%d) DART %p\n"
- "apcie%d+"
- "apcie%d-"
- "apcie+"
- "apcie-"
- "apcie-plce-sid"
- "disableRootPort"
- "enableRootPort"
- "extInjectError"
- "handleRootTimeout"
- "ignoreCorrectableError"
- "linkDownRecovery"
- "manual-enable-defer-scan"
- "msi-reservation-size"
- "msi-reservation-start"
- "size >= numVectors"
- "void AppleEmbeddedPCIE::_waitForLinkUp(uint32_t, uint32_t, bool)"

```
