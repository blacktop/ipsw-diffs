## com.apple.driver.AppleEmbeddedPCIE

> `com.apple.driver.AppleEmbeddedPCIE`

```diff

-936.100.34.0.0
-  __TEXT.__cstring: 0x6a22
-  __TEXT.__os_log: 0x2ef3
+1039.0.0.0.0
+  __TEXT.__cstring: 0x714e
+  __TEXT.__os_log: 0x32d9
   __TEXT.__const: 0x178
-  __TEXT_EXEC.__text: 0x30598
+  __TEXT_EXEC.__text: 0x338bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3d8
   __DATA.__common: 0x188
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x190
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0x2bd0
+  __DATA_CONST.__const: 0x2c98
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 3545F04A-A4CB-33F2-B771-726B4B5E2734
-  Functions: 464
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x190
+  UUID: 0D436127-3DCD-35C4-9070-32424A8770B9
+  Functions: 504
   Symbols:   0
-  CStrings:  767
+  CStrings:  802
 
CStrings:
+ " root_err_status=0x%08x COR source: %u:%u:%u"
+ " root_err_status=0x%08x COR source: %u:%u:%u, UNC source: %u:%u:%u"
+ " root_err_status=0x%08x UNC source: %u:%u:%u"
+ " root_err_status=0x%08x err_src_id: 0x%08x"
+ "\"manual-enable-defer-scan is only supported on manual-enable links\" @%s:%d"
+ "121111121222121211111111112112222222222211122"
+ "121111121222121211111121111221111111111111111111111112122222222111211222221111111222222222222222222222222222222222212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212122222222222222222222222222222222222222222222222222222222222222222211122222121112122122"
+ "121111121222121211111212122222211222112211111112112221111111221122122"
+ "Completion error interrupt"
+ "Completion timeout count"
+ "IOReturn AppleEmbeddedPCIEPort::reenableThreadCall(thread_call_t)_block_invoke"
+ "Link timeout"
+ "Link timeout count"
+ "[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s [%s()] Failed to get device memory for nub %s, skipping mmio timeout increase\n\n"
+ "[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s [%s()] Failed to map IODeviceMemory, skipping mmio timeout increase\n\n"
+ "[PCIe:%u %llu ns] AppleEmbeddedPCIE::%s ml_io_increase_timeouts_phys(0x%lx, %u, %u, %u) %s\n\n"
+ "[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s Invalid error injection type %u\n"
+ "[PCIe:%u %llu ns] AppleEmbeddedPCIEUserClient::%s Invalid timeout injection subtype %u\n"
+ "[PCIe:%u %llu ns] ApplePCIEMSIController::%s Attempting to allocate %u reserved MSI vector(s), starting at vector %u, for port %d\n"
+ "[PCIe:%u %llu ns] ApplePCIEMSIController::%s Warning: the EP driver requested fewer MSIs (%u) than were reserved (%u)\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Reached max allowed timeouts\n"
+ "[PCIe:%u %llu ns] apcie[%u:%s]::%s Using static SID for device %p RID 0x%04x(%d:%d:%d) DART %p\n"
+ "apcie%d+"
+ "apcie%d-"
+ "apcie+"
+ "apcie-"
+ "apcie-plce-sid"
+ "disableRootPort"
+ "enableRootPort"
+ "extInjectError"
+ "handleRootTimeout"
+ "ignoreCorrectableError"
+ "linkDownRecovery"
+ "manual-enable-defer-scan"
+ "msi-reservation-size"
+ "msi-reservation-start"
+ "size >= numVectors"
+ "void AppleEmbeddedPCIE::_waitForLinkUp(uint32_t, uint32_t, bool)"
- " root_err_status=0x%08x"
- "12111112122212121111111111211222222222221112"
- "1211111212221212111111211112211111111111111111111111121222222221112112222111111122222222222222222222222222222222221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221221212222222222222222222222222222222222222222222222222222222222222222221112222212111212212"
- "1211111212221212111112121222222112221122111111121122211111112211221222"
- "AF/Link timeout"
- "CA interrupt debug"
- "Port error interrupt"
- "[%s()] Failed to get device memory for nub %s, skipping mmio timeout increase\n"
- "[%s()] Failed to map IODeviceMemory, skipping mmio timeout increase\n"
- "handleCompletionTimeoutInterrupt"
- "ml_io_increase_timeouts_phys(0x%lx, %u, %u, %u) %s\n"
- "void AppleEmbeddedPCIE::_waitForLinkUp(uint32_t, uint32_t, uint32_t, bool)"

```
