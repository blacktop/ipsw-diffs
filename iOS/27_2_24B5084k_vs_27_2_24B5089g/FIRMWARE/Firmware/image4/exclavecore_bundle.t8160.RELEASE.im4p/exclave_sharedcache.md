## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__PDATA.__auth_ptr`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.40.23.502.2
-  __TEXT.__text: 0xf35478
+1777.40.28.0.2
+  __TEXT.__text: 0xf2c9a4
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0xb52a1
-  __TEXT.__const: 0x207fe4
-  __TEXT.__swift5_typeref: 0x32b54
-  __TEXT.__swift5_reflstr: 0x551c8
-  __TEXT.__swift5_assocty: 0x102b8
-  __TEXT.__swift5_fieldmd: 0x8eea4
-  __TEXT.__constg_swiftt: 0x78dc0
-  __TEXT.__swift5_protos: 0x14c8
-  __TEXT.__swift5_proto: 0xccf0
-  __TEXT.__swift5_types: 0x84a8
+  __TEXT.__cstring: 0xb5041
+  __TEXT.__const: 0x207fc4
+  __TEXT.__swift5_typeref: 0x3292a
+  __TEXT.__swift5_reflstr: 0x55178
+  __TEXT.__swift5_assocty: 0x10270
+  __TEXT.__swift5_fieldmd: 0x8eda8
+  __TEXT.__constg_swiftt: 0x78b08
+  __TEXT.__swift5_protos: 0x14c0
+  __TEXT.__swift5_proto: 0xccd4
+  __TEXT.__swift5_types: 0x8498
   __TEXT.__swift5_types2: 0xc4
   __TEXT.__swift5_builtin: 0x2bc0
   __TEXT.__swift5_capture: 0x3c0c
   __TEXT.__objc_methtype: 0x556
   __TEXT.__swift5_mpenum: 0xdc4
-  __TEXT.__swift_as_entry: 0x1668
-  __TEXT.__swift_as_ret: 0x1870
-  __TEXT.__swift_as_cont: 0x2f28
-  __TEXT.__oslogstring: 0x72f5
+  __TEXT.__swift_as_entry: 0x1688
+  __TEXT.__swift_as_ret: 0x1898
+  __TEXT.__swift_as_cont: 0x2f94
+  __TEXT.__oslogstring: 0x70b5
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x170
-  __TEXT.__eh_frame: 0x83494
+  __TEXT.__eh_frame: 0x83304
   __DATA.__TIGHTBEAM_VT: 0x1530
   __DATA.__TIGHTBEAM: 0x590
-  __DATA.__const: 0x168588
-  __DATA.__data: 0x60320
+  __DATA.__const: 0x168568
+  __DATA.__data: 0x5ff40
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b9c2
-  __DATA.__auth_ptr: 0xb888
+  __DATA.__ENDPOINTS: 0x1bbd0
+  __DATA.__auth_ptr: 0xb868
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x3b8
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__common: 0x5e02
+  __DATA.__common: 0x5dd2
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x6800
+  __PDATA.__const: 0x6810
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xba48
+  __PDATA.__bss: 0xbae8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 1452
+  Functions: 1451
   Symbols:   1
-  CStrings:  16846
+  CStrings:  16807
 
CStrings:
+ " bytes for clientCode "
+ " for clientCode "
+ " opted into prefers-waiting-through-sleep; option accepted but not yet implemented"
+ "%s(%zu): failed to delete delta scratch RO span slot"
+ "%s(%zu): failed to delete delta scratch RO temp cap"
+ "%s(%zu): failed to map frame into delta scratch RO span"
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Sep 12 05:10:17 PDT 2026; root:AppleImage4_exclavecore-374~18509/ExclaveImage4/RELEASE_ARM64E"
+ "ANEExclave version: ANEExclave_exclavecore-13.101.1"
+ "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
+ "Build Date: Sat Sep 12 04:43:50 PDT 2026"
+ "Creating new repository for clientCode "
+ "Deferred power on for ANEEngine from "
+ "Detected file size "
+ "ExclaveCameraSISP-20.105.6"
+ "ExclaveOS Image4 Framework Version 7.0.0: Sat Sep 12 05:10:17 PDT 2026; root:AppleImage4_exclavecore-374~18509/ExclaveImage4/RELEASE_ARM64E"
+ "Repository loaded for clientCode "
+ "Resuming ANEEngine to service existing clients from "
+ "Save for clientCode "
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_span_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_temp_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame_readonly(scratch->ro_span, (uintptr_t)ro_words, scratch->ro_temp_slot)'"
+ "[VAS abort in function %s at line %d] [%s] could not allocate fixup span for fault handler\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Could not depopulate temp span (drop): %s (0x%04hx)\n\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] _delta_page_against_original returned unexpected result(%p)\n"
+ "]: OutstandingRequestCount already cleared"
+ "]: OutstandingRequestCount not yet drained"
+ "_delta_page_against_original"
+ "applyFixups: rebase failed for %#lx (region %zd)"
+ "applyFixups: region %zd has NULL fixup_metadata_pointer"
+ "clientSessionHint(client:model:args:) Cycles: "
+ "clientSetPowerHint(client:model:keepPowered:) Cycles: "
+ "com.apple.securepairing.frequent"
+ "delta_output != fault->write_buffer"
+ "resetAndCheckHWCommandQueue(_:)"
+ "resetHWCommandQueueNoWait queueIdx["
+ "resetHWCommandQueueNoWait threw an unexpected error type"
+ "resetHWCommandQueueNoWait(_:)"
+ "resetHWCommandQueueNoWait(source:)"
+ "resetHWCommandQueueNoWait(src:)"
+ "resetHWCommandQueueNoWaitIfPowered(src:)"
+ "skip resetHWCommandQueueNoWait(src: "
+ "vas_return_code(drop_depop) != VAS_SUCCESS"
- ", iopsOverride: "
- ", preferedEncoding: "
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Fri Sep  4 01:28:14 PDT 2026; root:AppleImage4_exclavecore-374~18270/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.100.8"
- "All domain keys are up to date"
- "Attempt to serialize IOPDomainKey without peerPubKey"
- "Attempt to serialize IOPDomainKey without serializedRefKey"
- "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
- "Build Date: Wed Sep  9 20:44:59 PDT 2026"
- "Can't read iop type from stream"
- "Can't read peerPubKey"
- "Can't serialize AKSRefKey: "
- "Could not update a public key for domain: %u"
- "Deferred power on for ANEEngine"
- "Dropping unsoported public key type: %u"
- "ExclaveCameraSISP-20.104.4"
- "ExclaveOS Image4 Framework Version 7.0.0: Fri Sep  4 01:28:14 PDT 2026; root:AppleImage4_exclavecore-374~18270/ExclaveImage4/RELEASE_ARM64E"
- "Failed to read domain key"
- "Failed to read domain key count"
- "Failed to read iop domain keys"
- "Record does not contain domain keys"
- "Requested iop keys: "
- "Resuming ANEEngine to service existing clients"
- "SPR not found for peerId "
- "Saving the client repository failed"
- "SecurePairingCoreComponent/SecurePairingCore+Domain.swift"
- "Skipping unsupported IOP key type: %u"
- "Skipping unsupported IOP type: %u"
- "Stored domain keys contain unknow IOP type: %u"
- "TransferDataStream attempt to receive data in finished state"
- "TransferDataStream attempt to send data in finished state"
- "Unexpected iop type code "
- "Update domain keys, missing keys: "
- "Updating provided keys based on peer response"
- "Will provide keys for IOPs: "
- "cancelDomainPairing threw an unexpected error type"
- "extractPublicKeys(from: "
- "extractPublicKeys(from:)"
- "extracted public keys for domains: "
- "generateDomainKeys()"
- "generateKey(for: "
- "generateKey(for:)"
- "got key material: "
- "handleDomainKeys -> "
- "handleDomainKeys threw an unexpected error type"
- "handleDomainKeys(pairingId: "
- "handleDomainKeys(pairingId:bytes:)"
- "handleDomainKeysAck -> "
- "handleDomainKeysAck threw an unexpected error type"
- "handleDomainKeysAck(pairingId: "
- "handleDomainKeysAck(pairingId:bytes:)"
- "handleMissingKeyTypes(peerIds: "
- "handleMissingKeyTypesAck -> "
- "handleMissingKeyTypesAck(pairingId: "
- "handleMissingKeyTypesAck(pairingId:bytes:)"
- "handleMissingKeyTypesCont -> "
- "handleMissingKeyTypesCont(pairingId: "
- "handleMissingKeyTypesCont(pairingId:bytes:)"
- "handleMissingKeys -> "
- "handleMissingKeys(bytes: "
- "handleMissingKeys(context:bytes:)"
- "handleStartKeyTransfer - no iops set to context before key transfer"
- "handleStartKeyTransfer -> "
- "handleStartKeyTransfer threw an unexpected error type"
- "handleStartKeyTransfer(pairingId: "
- "handleStartKeyTransfer(pairingId:)"
- "invalid rawValue for TransferEncoding: "
- "no payload should be here"
- "setProvidedKeys(_:merge:)"
- "startDomainPairing -> "
- "startDomainPairing(clientClass:peerId:tag:encoding:iopsOverride:bytes:)"
- "startDomainPairing(clientClass:peerId:tag:preferedEncoding:iopsOverride:)"
- "startDomainPairing(peerIds: "
- "storeDomainKeys()"
- "storing new keys for domains: "
- "storing original keys for domains: "
- "unexpected payload size: %ld"
- "updateDomainKeys(iopsOverride: "
- "updateDomainKeys(iopsOverride:)"
- "updatePublicKeys(_:)"
- "updatePublicKeys(from:) count = "
```
