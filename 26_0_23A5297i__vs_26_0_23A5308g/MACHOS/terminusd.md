## terminusd

> `/usr/libexec/terminusd`

```diff

-676.0.3.0.0
-  __TEXT.__text: 0x182d2c
+676.0.13.0.0
+  __TEXT.__text: 0x1846e4
   __TEXT.__auth_stubs: 0x2bd0
-  __TEXT.__objc_stubs: 0x84c0
+  __TEXT.__objc_stubs: 0x84e0
   __TEXT.__objc_methlist: 0x52a0
   __TEXT.__const: 0x24c
-  __TEXT.__gcc_except_tab: 0x420c
-  __TEXT.__objc_methname: 0x11420
-  __TEXT.__cstring: 0x41347
+  __TEXT.__gcc_except_tab: 0x4320
+  __TEXT.__objc_methname: 0x11496
+  __TEXT.__cstring: 0x4191b
   __TEXT.__oslogstring: 0x247e
   __TEXT.__objc_classname: 0xe92
   __TEXT.__objc_methtype: 0x382c
-  __TEXT.__unwind_info: 0x2460
+  __TEXT.__unwind_info: 0x24b8
   __DATA_CONST.__auth_got: 0x15f8
-  __DATA_CONST.__got: 0xa00
+  __DATA_CONST.__got: 0xa08
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x3458
-  __DATA_CONST.__cfstring: 0xbd20
+  __DATA_CONST.__cfstring: 0xbd40
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x15038
-  __DATA.__objc_selrefs: 0x2cc0
-  __DATA.__objc_ivar: 0x1a4c
+  __DATA.__objc_const: 0x15078
+  __DATA.__objc_selrefs: 0x2cc8
+  __DATA.__objc_ivar: 0x1a54
   __DATA.__objc_data: 0x29e0
   __DATA.__data: 0xce8
   __DATA.__bss: 0x6b8

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1FBA3609-AD68-3C89-8D93-A112A9F84CF8
-  Functions: 3085
-  Symbols:   1036
-  CStrings:  11530
+  UUID: 78140C0F-F659-3949-834C-F68D670D5354
+  Functions: 3097
+  Symbols:   1037
+  CStrings:  11558
 
Symbols:
+ _nrXPCKeyUnderlyingError
CStrings:
+ "%s%.30s:%-4d %@: Already has a pending authMethod request for method %zu"
+ "%s%.30s:%-4d %@: Connecting device for %@"
+ "%s%.30s:%-4d %@: Connecting to peripheral"
+ "%s%.30s:%-4d %@: Disconnecting from %@"
+ "%s%.30s:%-4d %@: Failed to get pairing info for %@ migration"
+ "%s%.30s:%-4d %@: Failed to retrieve or create peripheral for %@ migration with addr: %@"
+ "%s%.30s:%-4d %@: Got peripheral for %@ migration: %@"
+ "%s%.30s:%-4d %@: Peripheral already connected"
+ "%s%.30s:%-4d %@: Skipping sending auth method request: pending %zu IKE state %zu"
+ "%s%.30s:%-4d %@: Starting BT pairing to %@"
+ "%s%.30s:%-4d %@: readPairingInfoFromKeychain for %@ migration returned %@"
+ "%s%.30s:%-4d Added %@ to quarantine"
+ "%s%.30s:%-4d Central manager is nil"
+ "%s%.30s:%-4d Invalid pairingManager for %@ migration"
+ "%s%.30s:%-4d No remote %@ address received for %@"
+ "%s%.30s:%-4d Pairing agent is nil"
+ "%s%.30s:%-4d Removing %@ from quarantine after timeout"
+ "%s%.30s:%-4d Skipping pairing info update for %@ - exceeded max retries (%lu)"
+ "%s%.30s:%-4d Started quarantine timer for %lu devices"
+ "%s%.30s:%-4d bluetoothUUID: %@ not found in pairedPeersBTUUIDs:%@"
+ "%s%.30s:%-4d cancelling resolver %@"
+ "%s%.30s:%-4d invalidating quarantine timer"
+ "%s%.30s:%-4d received resolver update for %@ with status %u, endpoints %@"
+ "%s%.30s:%-4d resolver %@ resolving endpoint %@"
+ "%s%.30s:%-4d using alternate device ID, since IDS isn't available"
+ "-[NRDevicePairingCandidateContext disconnectPeripheralAndRemove:]"
+ "-[NRDevicePairingManagerContext performNeededBTConnectionOperations]"
+ "-[NRDevicePairingManagerContext performNeededBTConnectionOperations]_block_invoke_2"
+ "-[NRDiscoveryClient stopResolvingOverLinkType:]"
+ "-[NRLinkDirector copyIDSDeviceIDWithCompletion:]"
+ "-[NRLinkManagerBluetooth addNRUUIDToUpdatePairingInfoQuarantine:completionBlock:]"
+ "-[NRLinkManagerBluetooth invalidateUpdatePairingInfoQuarantineTimer]"
+ "-[NRLinkManagerBluetooth startUpdatePairingInfoQuarantineTimerIfNeeded]"
+ "-[NRLinkManagerBluetooth startUpdatePairingInfoQuarantineTimerIfNeeded]_block_invoke"
+ "-[NRLinkManagerBluetooth updatePairingInfoIfNeeded]"
+ "18:25:56"
+ "676.0.13"
+ "Jul 25 2025"
+ "_authMethodRequestTimer"
+ "_updatePairingInfoQuarantineCompletionBlocks"
+ "_updatePairingInfoQuarantineTimer"
+ "_updatePairingInfoQuarantinedBTNRUUIDs"
+ "_updatePairingInfoRetryCount"
+ "com.apple.private.restrict-post.networkrelay.endpointcache"
+ "com.apple.private.restrict-post.networkrelay.launch"
+ "com.apple.private.restrict-post.networkrelay.referencesChanged"
+ "valueForKey:"
- "%s%.30s:%-4d %@: Already has a pending authMethod request"
- "%s%.30s:%-4d %@: Skipping sending auth method request: pending %zu requested %zu IKE state %zu"
- "%s%.30s:%-4d %@: Starting BT pairing"
- "%s%.30s:%-4d Connecting device for %@"
- "%s%.30s:%-4d Failed to retrieve or create peripheral with addr:%@"
- "%s%.30s:%-4d No remote %@ address recieved for %@"
- "%s%.30s:%-4d invalid pairingManager"
- "%s%.30s:%-4d peripheral already connected: %@"
- "%s%.30s:%-4d readPairingInfoFromKeychain %@"
- "%s%.30s:%-4d resolving endpoint %@"
- "-[NRDevicePairingManagerContext connectToPeersIfNeeded]"
- "-[NRDevicePairingManagerContext connectToPeersIfNeeded]_block_invoke_2"
- "02:12:34"
- "676.0.3"
- "Jul 11 2025"
- "_currentAuthMethod"
- "_pendingClientAuthRequest"
- "_requestedAuthMethod"
- "com.apple.networkrelay.endpointcache"
- "com.apple.networkrelay.launch"
- "com.apple.networkrelay.referencesChanged"

```
