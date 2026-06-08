## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6805.120.2.0.0
-  __TEXT.__cstring: 0x49f28
-  __TEXT.__os_log: 0x3afb3
+6832.0.0.0.0
+  __TEXT.__cstring: 0x4adb4
+  __TEXT.__os_log: 0x3be20
   __TEXT.__const: 0xb60
-  __TEXT_EXEC.__text: 0x1c4390
+  __TEXT_EXEC.__text: 0x1cb7f0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xb22
-  __DATA.__common: 0x15b0
+  __DATA.__data: 0xc42
+  __DATA.__common: 0x1600
   __DATA.__bss: 0x9
+  __DATA_CONST.__mod_init_func: 0x460
+  __DATA_CONST.__mod_term_func: 0x460
+  __DATA_CONST.__const: 0x24a38
+  __DATA_CONST.__kalloc_type: 0x2340
+  __DATA_CONST.__kalloc_var: 0xcd0
   __DATA_CONST.__auth_got: 0x550
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__mod_init_func: 0x450
-  __DATA_CONST.__mod_term_func: 0x450
-  __DATA_CONST.__const: 0x23e18
-  __DATA_CONST.__kalloc_type: 0x22c0
-  __DATA_CONST.__kalloc_var: 0xbe0
-  UUID: A2A18FA4-061A-374E-A9B0-F76C8834718E
-  Functions: 5586
+  UUID: 0BDFA420-4DDE-33EA-9A17-9A8A3324DCF8
+  Functions: 5698
   Symbols:   0
-  CStrings:  6112
+  CStrings:  6221
 
CStrings:
+ "%lldus IOThunderboltPath<%p>::completeActivation status=0x%llx\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::0setPowerState - state = %ld\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::1setPowerState - state = %ld\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::2setPowerState - return\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::NNNNNfind VSA capability - status=0x%x kVSACapabilityMask=0x%x kVSACapabilityID=0x%x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::NNNNNfind VSA capability - status=0x%x kVSACapabilityMask=0x%x kVSACapabilityID=0x%x cap_offset=0x%x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::destroyPowerManagement\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::finalize\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::finalize - success = %d\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::free\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::init\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x protocol_id=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x protocol_rev=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x protocol_setting=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd0=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd1=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd2=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd3=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rxMask=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x txMask=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%08x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%08x table_config=0x%x num_of_entries_per_protocol=0x%x num_of_entries_in_table=0x%x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%x length_offset=0x%x vsec_length=0x%x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::sleep\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::start\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::start - VSA Port matched port %p adapterType = 0x%x\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::start - fHIPort = %p fVSAPort = %p status=0x%x \n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::start completed - status = 0x%x fHIPort = %p\n"
+ "%lldus IOThunderboltVSA(%x@%llx:%x)::wake\n"
+ "%lldus IOThunderboltVSA::createResources status = 0x%x\n"
+ "%lldus IOThunderboltVSAService(%x@%llx)::finalize\n"
+ "%lldus IOThunderboltVSAService(%x@%llx)::finalize - terminate service: %s\n"
+ "%lldus IOThunderboltVSAService(%x@%llx)::finalize - terminate service: unknown service\n"
+ "%lldus IOThunderboltVSAService<%p>::attach\n"
+ "%lldus IOThunderboltVSAService<%p>::detach\n"
+ "%lldus IOThunderboltVSAService<%p>::free\n"
+ "%lldus IOThunderboltVSAService<%p>::initWithPort\n"
+ "%lldus IOThunderboltVSAService<%p>::initWithPort - ERROR: fPort = NULL\n"
+ "%lldus IOThunderboltVSAService<%p>::publish\n"
+ "%lldus IOThunderboltVSAService<%p>::setProperties\n"
+ "%lldus IOThunderboltVSAService<%p>::terminate\n"
+ "%lldus IOThunderboltVSAService<%p>::unpublish\n"
+ "%s"
+ "%s (%04x:%04x/%04x)"
+ "121111121222121211122211212"
+ "121111211111222222111212112221221"
+ "121112221"
+ "121222212111122"
+ "22:46:39"
+ "IOThunderboltVSA"
+ "IOThunderboltVSAService"
+ "May 27 2026"
+ "Protocol Rev"
+ "Protocol Setting"
+ "Rx Mask"
+ "Tx Mask"
+ "VSA_NOT_FOUND"
+ "Vendor Specific Adapter"
+ "site.IOThunderboltVSA"
+ "site.IOThunderboltVSAService"
+ "vsaaia"
+ "vsasat"
- "%lldus IOThunderboltPath<%p>::completeActivation\n"
- "12111121111122222211121211221"
- "121221"
- "12122212111122"
- "20:24:47"
- "Apr 23 2026"

```
