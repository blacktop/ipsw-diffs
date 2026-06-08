## com.apple.iokit.IOPCIFamily

> `com.apple.iokit.IOPCIFamily`

```diff

-726.100.6.0.0
-  __TEXT.__const: 0xe50
-  __TEXT.__cstring: 0x74e1
-  __TEXT.__os_log: 0x4e6f
-  __TEXT_EXEC.__text: 0x3f94c
+762.0.0.0.0
+  __TEXT.__const: 0xf18
+  __TEXT.__cstring: 0x76ed
+  __TEXT.__os_log: 0x5085
+  __TEXT_EXEC.__text: 0x41a84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x430
-  __DATA_CONST.__auth_got: 0x480
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x3d00
+  __DATA_CONST.__const: 0x3d60
   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: C2351448-4D14-3494-B074-FDB498AF9A1B
-  Functions: 712
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x8
+  UUID: 6739D522-092B-3449-A531-8C351CDA6CA7
+  Functions: 723
   Symbols:   0
-  CStrings:  1083
+  CStrings:  1101
 
CStrings:
+ "11111222222111111111111222222222221111122222221112"
+ "12111112122212121112111111111121111221221222121"
+ "22222222222122211121221111111111111111111111111111211221222112111221"
+ "22:46:03"
+ "May 27 2026"
+ "[PCIe:%u %llu ns] %s(0x%qx) is not busy, checking power-plane\n"
+ "[PCIe:%u %llu ns] %s(0x%qx) power children set changed (%u->%u)\n"
+ "[PCIe:%u %llu ns] %s(0x%qx) sleeping for %u ms\n"
+ "[PCIe:%u %llu ns] Limiting the root port's MPS to 0x%x\n"
+ "[PCIe:%u %llu ns] Looking up capability 0x%x\n"
+ "[PCIe:%u %llu ns] No symbol found for capability 0x%x\n"
+ "[PCIe:%u %llu ns] Unexpected error: no offset found for capability 0x%x\n"
+ "[PCIe:%u %llu ns] [ PCI configuration begin (scanning %u:%u:XX) ]\n"
+ "[PCIe:%u %llu ns] [%s()] Unexpected error: nub %s's pause thread is already pending execution\n"
+ "[PCIe:%u %llu ns] waitQuiet() timed out after %llu seconds, attempting pause\n"
+ "__CopyDeviceMemory"
+ "capability"
+ "initiatePause"
+ "offset"
+ "pci-mps-limit"
+ "pci-mps-limit=<domain>,<value>[;<domain>,<value>]"
- "1111122222211111111111122222222222111112222222111"
- "1211111212221212111211111111112111122121222121"
- "20:24:43"
- "222222222212221112122111111111111112112212221121121112"
- "Apr 23 2026"
- "[PCIe:%u %llu ns] %s(0x%qx) still initializing, deferring pause\n"
- "[PCIe:%u %llu ns] IOPCIDevice::%s: offload engine requires using _MemoryAccess()\n"
- "[PCIe:%u %llu ns] [%s()] nub %s(0x%qx) has busy state %u\n"
- "_CopyDeviceMemoryWithIndex_Impl"
- "busyStateChange"

```
