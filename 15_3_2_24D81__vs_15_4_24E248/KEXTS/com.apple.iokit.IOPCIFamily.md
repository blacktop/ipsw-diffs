## com.apple.iokit.IOPCIFamily

> `com.apple.iokit.IOPCIFamily`

```diff

-664.81.2.0.0
+681.101.1.0.0
   __TEXT.__const: 0x710
-  __TEXT.__cstring: 0x5372
-  __TEXT_EXEC.__text: 0x2fe70
+  __TEXT.__cstring: 0x548e
+  __TEXT_EXEC.__text: 0x30f40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x218

   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__kalloc_var: 0x190
   __LINKINFO.__symbolsets: 0x639f
-  UUID: 6634906B-5C27-38EB-95F6-E03B6409AA17
-  Functions: 745
-  Symbols:   1339
-  CStrings:  662
+  UUID: 4710CD1D-B451-35DB-828C-47C9FB39E997
+  Functions: 738
+  Symbols:   1341
+  CStrings:  670
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ __ZN15IOPCI2PCIBridge17detectLinkPartnerEv
+ __ZN19IOPCIHostBridgeData12systemWakingEv
+ __ZZN11IOPCIBridge10publishNubEP11IOPCIDevicejE21kalloc_type_view_2942
+ __ZZN11IOPCIBridge17createEventSourceEP8OSObjectPFvS1_P16IOPCIEventSourcePK10IOPCIEventEjE21kalloc_type_view_5775
+ __ZZN11IOPCIBridge4freeEvE21kalloc_type_view_1219
+ __ZZN11IOPCIBridge4initEP12OSDictionaryE21kalloc_type_view_1205
+ __ZZN15IOPCI2PCIBridge21startBridgeInterruptsEP9IOServiceE21kalloc_type_view_5162
+ __ZZN15IOPCI2PCIBridge4stopEP9IOServiceE21kalloc_type_view_5570
+ __ZZN16IOPCIEventSource4freeEvE21kalloc_type_view_5900
+ __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2301
+ __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2348
+ __ZZN17IOPCIConfigurator17deleteConfigEntryEP16IOPCIConfigEntryE21kalloc_type_view_2068
+ __block_descriptor_tmp.228
+ __block_descriptor_tmp.269
- _ZN17IOPCIConfigurator19constructPropertiesEP16IOPCIConfigEntry.cold.1
- __ZZN11IOPCIBridge10publishNubEP11IOPCIDevicejE21kalloc_type_view_2858
- __ZZN11IOPCIBridge17createEventSourceEP8OSObjectPFvS1_P16IOPCIEventSourcePK10IOPCIEventEjE21kalloc_type_view_5537
- __ZZN11IOPCIBridge4freeEvE21kalloc_type_view_1205
- __ZZN11IOPCIBridge4initEP12OSDictionaryE21kalloc_type_view_1191
- __ZZN15IOPCI2PCIBridge21startBridgeInterruptsEP9IOServiceE21kalloc_type_view_5021
- __ZZN15IOPCI2PCIBridge4stopEP9IOServiceE21kalloc_type_view_5332
- __ZZN16IOPCIEventSource4freeEvE21kalloc_type_view_5662
- __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2289
- __ZZN17IOPCIConfigurator16bridgeProbeChildEP16IOPCIConfigEntry17IOPCIAddressSpaceE21kalloc_type_view_2336
- __ZZN17IOPCIConfigurator17deleteConfigEntryEP16IOPCIConfigEntryE21kalloc_type_view_2056
- __block_descriptor_tmp.227
- __block_descriptor_tmp.264
CStrings:
+ "111111222"
+ "21:11:14"
+ "22222222221222111212211111111111111211222"
+ "Mar 19 2025"
+ "[%s()] BAR%u (0x%x) does not match expected value (0x%x)\n"
+ "[%s()] Done probing\n"
+ "[%s()] Done waiting for %u:%u:%u's busy count to go to zero\n"
+ "[%s()] Requesting rescan of %u:%u:%u\n"
+ "[%s()] nub %s@%u:%u:%u has link depth %u\n"
+ "detectLinkPartner"
+ "probeBusGated"
+ "terminate-on-restore-failure"
- "1111112"
- "20:11:10"
- "2222222222122211121221111111111111121122"
- "Jan  2 2025"

```
