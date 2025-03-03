## terminusd

> `/usr/libexec/terminusd`

```diff

-578.100.23.502.1
-  __TEXT.__text: 0x16d828
+578.100.29.0.0
+  __TEXT.__text: 0x16df6c
   __TEXT.__auth_stubs: 0x2820
-  __TEXT.__objc_stubs: 0x8640
-  __TEXT.__objc_methlist: 0x54e8
+  __TEXT.__objc_stubs: 0x80a0
+  __TEXT.__objc_methlist: 0x5210
   __TEXT.__const: 0x25c
-  __TEXT.__gcc_except_tab: 0x3be8
-  __TEXT.__objc_methname: 0x11376
-  __TEXT.__cstring: 0x3ec2a
+  __TEXT.__gcc_except_tab: 0x3bb8
+  __TEXT.__objc_methname: 0x10e8b
+  __TEXT.__cstring: 0x3ecf0
   __TEXT.__oslogstring: 0x237b
-  __TEXT.__objc_classname: 0xe38
-  __TEXT.__objc_methtype: 0x3520
-  __TEXT.__unwind_info: 0x2248
+  __TEXT.__objc_classname: 0xe3a
+  __TEXT.__objc_methtype: 0x3511
+  __TEXT.__unwind_info: 0x2220
   __DATA_CONST.__auth_got: 0x1420
   __DATA_CONST.__got: 0x9e0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3138
-  __DATA_CONST.__cfstring: 0xb980
+  __DATA_CONST.__const: 0x31f0
+  __DATA_CONST.__cfstring: 0xb9a0
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__objc_intobj: 0x588
-  __DATA_CONST.__objc_arraydata: 0xa0
-  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_intobj: 0x5a0
+  __DATA_CONST.__objc_arraydata: 0xb0
+  __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x148f8
-  __DATA.__objc_selrefs: 0x2cf8
-  __DATA.__objc_ivar: 0x1974
+  __DATA.__objc_const: 0x14808
+  __DATA.__objc_selrefs: 0x2b88
+  __DATA.__objc_ivar: 0x1980
   __DATA.__objc_data: 0x28a0
   __DATA.__data: 0xce8
   __DATA.__bss: 0x6a0

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3027
+  Functions: 2984
   Symbols:   973
-  CStrings:  9829
+  CStrings:  9776
 
CStrings:
+ "\x17\x12\x16"
+ "\x18"
+ "%s%.30s:%-4d Client %@ unpairing %@"
+ "%s%.30s:%-4d Creating only necessary AWDL links due to critical thermal conditions"
+ "%s%.30s:%-4d Deferring creating AWDL links due to critical thermal conditions"
+ "%s%.30s:%-4d deletePairingInfoFromKeychain %@ deleted: %s"
+ "%s%.30s:%-4d localDevice not found"
+ "%s%.30s:%-4d unregisterDeviceWithNRUUID: result %lld error %@"
+ "+[NRDLocalDevice updateHasSavedPairingInfoInKeychain:nrUUID:]"
+ "-[NRDLocalDevice deleteAllKeychainItems]_block_invoke_2"
+ "-[NRLinkManagerBluetooth updatePairingInfoForNRUUID:completionBlock:]"
+ "-[NRLinkManagerBluetooth updatePairingInfoForNRUUID:completionBlock:]_block_invoke"
+ "06:09:13"
+ "578.100.29"
+ "Feb 22 2025"
+ "TB,N,V_hasSavedPairingInfoInKeychain"
+ "_hasSavedPairingInfoInKeychain"
+ "_updatePairingInfoInProgress"
+ "handleUnpairDeviceByNRUUID"
+ "handleUnpairDeviceByNRUUID_block_invoke"
+ "handleUnpairDeviceByNRUUID_block_invoke_2"
+ "hasSavedPairingInfoInKeychain"
+ "setHasSavedPairingInfoInKeychain:"
- "\x17\x12\x15"
- "%s called with null self.parser"
- "%s%.30s:%-4d Deferring creating awdl link due to critical thermal conditions"
- "%s%.30s:%-4d localDevice not found for %@"
- "%s%.30s:%-4d unregisterDeviceWithNRUUID: nruuid %@ result %lld error %@"
- "-[NRDevicePairingDirector handleUnpairRequest:forConnection:]"
- "-[NRDevicePairingDirector handleUnpairRequest:forConnection:]_block_invoke"
- "-[NRDevicePairingDirector handleUnpairRequest:forConnection:]_block_invoke_2"
- "-[NRLinkManagerBluetooth updatePairingInfoForNRUUID:]"
- "-[NRLinkManagerBluetooth updatePairingInfoForNRUUID:]_block_invoke"
- "05:04:18"
- "578.100.23.502.1"
- "Feb 16 2025"
- "T@\"CBCentralManager\",&,N,V_centralManager"
- "T@\"CBPeripheralManager\",&,N,V_peripheralManager"
- "T@\"NRBluetoothPairer\",&,N,V_activePairer"
- "T@\"NRBluetoothPairerParameters\",&,N,V_parameters"
- "T@\"NSMutableArray\",&,N,V_enqueuedPairers"
- "T@\"NSMutableSet\",&,N,V_peripherals"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_completionQueue"
- "T@\"NSUUID\",&,N,V_pairedPeerBluetoothUUID"
- "T@?,C,N,V_completionBlock"
- "TB,N,V_busy"
- "TB,N,V_isPairing"
- "TB,N,V_isPeripheralRole"
- "TB,N,V_isUnpairRequest"
- "TB,N,V_isUnpairing"
- "TI,N,V_peripheralReconnectCounter"
- "Tq,N,V_pairingType"
- "activePairer"
- "busy"
- "centralManager"
- "completionBlock"
- "completionQueue"
- "copySharedManager"
- "disconnectFromPeripherals"
- "disconnectPeripheral:"
- "enqueuePairer:"
- "enqueuedPairers"
- "getPairerForBTUUID:"
- "handlePairerCompletionWithSuccess:peerBTUUID:"
- "hasPairerForNRUUID:"
- "initWithNRUUID:"
- "isPairing"
- "isPeripheralRole"
- "isUnpairRequest"
- "isUnpairing"
- "pair"
- "pairWithParameters:completionQueue:completionBlock:"
- "pairedPeerBluetoothUUID"
- "pairingType"
- "peripheralManager"
- "peripheralReconnectCounter"
- "peripherals"
- "removeAllPairers"
- "removePairerForNRUUID:"
- "resumeUnpairing"
- "setActivePairer:"
- "setBusy:"
- "setCentralManager:"
- "setCompletionBlock:"
- "setCompletionQueue:"
- "setEnqueuedPairers:"
- "setIsPairing:"
- "setIsPeripheralRole:"
- "setIsUnpairRequest:"
- "setIsUnpairing:"
- "setPairedPeerBluetoothUUID:"
- "setPairingType:"
- "setParameters:"
- "setPeripheralManager:"
- "setPeripheralReconnectCounter:"
- "setPeripherals:"
- "startNextPairer"
- "unpair"
- "unpairWithCompletionQueue:completionBlock:"
- "v32@0:8@16@?24"

```
