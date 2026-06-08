## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6805.120.2.0.0
-  __TEXT.__cstring: 0x49f28 sha256:b8fd84f023d473c35be25903865180742c204d2d2e166bcd5dcc5ad1614b56f1
-  __TEXT.__os_log: 0x3afb3 sha256:31f9cbea3e6654716435254c5661620b73d7e266cc9b62b41f34954aa8d9b045
+6832.0.0.0.0
+  __TEXT.__cstring: 0x4adb4 sha256:4057791724cc8146811c8b6e71f24437f381bb61cbd102ee420cee0582167be9
+  __TEXT.__os_log: 0x3be20 sha256:d4d94ed0ebf165b28a7dbd389e484df17a7b50d170134b49272e94041e11f066
   __TEXT.__const: 0xb60 sha256:aa9eaea3e1bf4554c080430db01f7b89090cdc6435b8bd29d7ac7da1b71c8287
-  __TEXT_EXEC.__text: 0x1c4390 sha256:6585d75763b4e19d98d80f22f5606d2a7ab4ee61cbf0855bd20c26468e3b9abb
+  __TEXT_EXEC.__text: 0x1cb7f0 sha256:6e42dfacd865573d2dd60b48e79450767ba9dc7871c556383c71ad8387931666
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xb22 sha256:5ccec3884c75b92c771f68f7522ff1d6c83d4a5cba7ba0b73b6c2fa86f14b6d7
-  __DATA.__common: 0x15b0 sha256:65e830fb3899cb0dbe537dd7894b877587bcd8a7f92f4328018afc112917cd57
+  __DATA.__data: 0xc42 sha256:8f8aeebf8da83e9398d4580c67659fe5bf8663376cca67031b4d742b50e79d7d
+  __DATA.__common: 0x1600 sha256:07fa8a94dd06b17cdd8a23295f9687cd861be80591e8ab912dafabf21117f264
   __DATA.__bss: 0x9 sha256:3e7077fd2f66d689e0cee6a7cf5b37bf2dca7c979af356d0a31cbc5c85605c7d
-  __DATA_CONST.__auth_got: 0x550 sha256:3ff5e5613edf4ee279362394a4c9fc2671d81f0272615460eba217c816359cfb
-  __DATA_CONST.__got: 0x168 sha256:1c253d9684c3939d2eb8aea90b1cd9990768ad1d6e647960d53193c51df4de32
-  __DATA_CONST.__mod_init_func: 0x450 sha256:82ac3b480f87c259f038193d1bc09819923bc33ce960b80aeeaaf501ef956d21
-  __DATA_CONST.__mod_term_func: 0x450 sha256:114b3b0d2ebf85de93445a9e47862010e20633c289ba5ccbc0a85a1b4117b80e
-  __DATA_CONST.__const: 0x23e18 sha256:22b75136118e2aab1ee0156b90c4f3979f4c24a17f6c022e1832f5085d14782b
-  __DATA_CONST.__kalloc_type: 0x22c0 sha256:c9bd42074e2b18b498bb11d6fb68bbfa7f9e82bf19636dee75b6839bf0e36566
-  __DATA_CONST.__kalloc_var: 0xbe0 sha256:b121b31b64d2401d7601f36e20059b3e3df3972956b0e142806fcb3b66bfcc86
-  UUID: A2A18FA4-061A-374E-A9B0-F76C8834718E
-  Functions: 5586
+  __DATA_CONST.__mod_init_func: 0x460 sha256:42b95b722da8909fc690e769bd1d541a9aa5f0736e78ed4021fac73893c91203
+  __DATA_CONST.__mod_term_func: 0x460 sha256:41fcd353e6b427cca1c747cf42e10cb9efab5ec0fa68f52b7bc05a64debd1d79
+  __DATA_CONST.__const: 0x24a38 sha256:6ad9ef76fb3a7ab985f7daacdb23b686aa048a9a393b211e4f3c4418e5429146
+  __DATA_CONST.__kalloc_type: 0x2340 sha256:573c9cc3b58e52264fdc3ed653c0d5a0839b5cecf75c333c25b0e2d646efe178
+  __DATA_CONST.__kalloc_var: 0xcd0 sha256:771f85f3e583bd884c910caeb1cf0c744218b32f8a3f232692fcb88e671e49f5
+  __DATA_CONST.__auth_got: 0x550 sha256:754884fb9c50571f9327901894f60a27c5768caf80230967443b1212b2799743
+  __DATA_CONST.__got: 0x168 sha256:7f32976c896ee7dc877635b7c64852bc1e9663f393a0c905d3978995e4266c2a
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
