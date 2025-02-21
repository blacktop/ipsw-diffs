## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-563.60.14.0.0
-  __TEXT.__text: 0x60a84
+578.100.23.502.1
+  __TEXT.__text: 0x6789c
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x156c
+  __TEXT.__objc_methlist: 0x180c
   __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x850
-  __TEXT.__cstring: 0xd47d
-  __TEXT.__oslogstring: 0x130a
-  __TEXT.__unwind_info: 0x8a8
-  __TEXT.__objc_classname: 0x323
-  __TEXT.__objc_methname: 0x3fad
-  __TEXT.__objc_methtype: 0x742
-  __TEXT.__objc_stubs: 0x25c0
+  __TEXT.__gcc_except_tab: 0x8b8
+  __TEXT.__cstring: 0xdc79
+  __TEXT.__oslogstring: 0x1237
+  __TEXT.__unwind_info: 0x880
+  __TEXT.__objc_classname: 0x325
+  __TEXT.__objc_methname: 0x42df
+  __TEXT.__objc_methtype: 0x74d
+  __TEXT.__objc_stubs: 0x2720
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__const: 0xd98
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc38
+  __DATA_CONST.__objc_selrefs: 0xd78
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x170
+  __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x4280
-  __AUTH_CONST.__objc_const: 0x42c8
-  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__cfstring: 0x4580
+  __AUTH_CONST.__objc_const: 0x41d0
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x450
+  __DATA.__objc_ivar: 0x47c
   __DATA.__data: 0x218
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x248
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 810
-  Symbols:   1228
-  CStrings:  2533
+  Functions: 818
+  Symbols:   1262
+  CStrings:  2642
 
Symbols:
+ _NRCreateStringFromPairingAuthMethod
+ _NRDevicePairingErrorOriginalCBUUIDKey
+ _NRDevicePairingErrorOriginalNRUUIDKey
+ _getNRLinkTypeForNRLinkSubtype
+ _nrPacketTo6LoWPAN
+ _nrXPCKeyIsExternalPairing
+ _nrXPCKeyPSM
+ _nrXPCKeyPairedDevice
CStrings:
+ "\x01\x13"
+ "\x02"
+ " NRUUID %@"
+ " migrationPairing %s"
+ " nrDeviceIdentifiers %@"
+ " psm %u"
+ "\""
+ "%s called with null cls"
+ "%s called with null dict"
+ "%s called with null linkType != NRLinkTypeInvalid"
+ "%s%.30s:%-4d %s: wrote %u bytes from nexus (actual: %u)"
+ "%s%.30s:%-4d -- expected %d filledIn %u pending %d received %u"
+ "%s%.30s:%-4d -- filledIn %u numberOfBytesToFill: %u"
+ "%s%.30s:%-4d -- ipv6 payload len %u"
+ "%s%.30s:%-4d -- ipv6 total packet len %u"
+ "%s%.30s:%-4d -- waiting for full header"
+ "%s%.30s:%-4d -- we have full packet"
+ "%s%.30s:%-4d -- we have partial packet"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (dstAddr) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (ioVecs) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (nrXPCQueue) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (outBuffer) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (packetBuffer) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (propertiesCopy.outOfBandKey) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (retNum) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (self.queue) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (srcAddr) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (xpcDict) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (xpcKey) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Invalid PSM for external device registration"
+ "%s%.30s:%-4d ABORTING: strict allocator failed"
+ "%s%.30s:%-4d ABORTING: strict_reallocf called with size 0"
+ "%s%.30s:%-4d ABORTING: strict_reallocf(%zu) failed"
+ "%s%.30s:%-4d Adding BluetoothUUID %@ to cache for nrUUID %@"
+ "%s%.30s:%-4d Auth method request with no XPC connection"
+ "%s%.30s:%-4d Failed to get UUID for key %s"
+ "%s%.30s:%-4d Failed to get XPC data for key %s"
+ "%s%.30s:%-4d Manager state change: %@ -> %@"
+ "%s%.30s:%-4d Register pairing manager request failed to serialize pairing manager info"
+ "%s%.30s:%-4d Register pairing manager request with no XPC connection"
+ "%s%.30s:%-4d Start discovery request with no XPC connection"
+ "%s%.30s:%-4d Start pairing request failed to serialize pairing target"
+ "%s%.30s:%-4d Start pairing request with no XPC connection"
+ "%s%.30s:%-4d Stop discovery request with no XPC connection"
+ "%s%.30s:%-4d Stop pairing request no XPC connection"
+ "%s%.30s:%-4d UUID is null for key %s"
+ "%s%.30s:%-4d Unpair request with no XPC connection"
+ "%s%.30s:%-4d Unregister pairing manager request with no XPC connection"
+ "%s%.30s:%-4d Used 6LowPAN IPHC to compress %u to %u (inline %u, no tlv) - %@ %@ %@"
+ "%s%.30s:%-4d XPC data for key %s is empty"
+ "%s%.30s:%-4d processing incoming data of length %u"
+ "%s%.30s:%-4d processing pending complete packet filledIn %u"
+ "%s%.30s:%-4d re-processing incoming data of length %u at offset %zu"
+ "%s%.30s:%-4d read more than buffer length"
+ "%s%.30s:%-4d unexpected data size %zu"
+ "%{public}s Assertion Failed: (dstAddr) != ((void*)0)"
+ "%{public}s Assertion Failed: (ioVecs) != ((void*)0)"
+ "%{public}s Assertion Failed: (nrXPCQueue) != ((void*)0)"
+ "%{public}s Assertion Failed: (outBuffer) != ((void*)0)"
+ "%{public}s Assertion Failed: (packetBuffer) != ((void*)0)"
+ "%{public}s Assertion Failed: (propertiesCopy.outOfBandKey) != ((void*)0)"
+ "%{public}s Assertion Failed: (retNum) != ((void*)0)"
+ "%{public}s Assertion Failed: (self.queue) != ((void*)0)"
+ "%{public}s Assertion Failed: (srcAddr) != ((void*)0)"
+ "%{public}s Assertion Failed: (xpcDict) != ((void*)0)"
+ "%{public}s Assertion Failed: (xpcKey) != ((void*)0)"
+ "%{public}s BUG IN CLIENT OF NetworkRelay: %s called with Invalid PSM for external device registration"
+ "%{public}s strict allocator failed"
+ "%{public}s strict_reallocf called with size 0"
+ "%{public}s strict_reallocf(%zu) failed"
+ ", EXTERNAL"
+ ", cndSvc %@"
+ ", psm %u"
+ "-[NRBluetoothPacketParser sendXPCCommDictionaryInner:]"
+ "-[NRDeviceIdentifier(InternalDirect) addToCacheForBluetoothUUID:]"
+ "-[NRDeviceOperationalProperties getDefaultLinkSubtypeForLinkType:]"
+ "-[NRPairedDevice initWithDeviceIdentifier:]"
+ "3\x14\xf0\xce!\xf0\xd1"
+ "Activated"
+ "Activating"
+ "BluetoothL2CAP"
+ "BluetoothScalable"
+ "C20@0:8C16"
+ "Discovery"
+ "Failed to archive %@: %@"
+ "Failed to get lost pairing candidate from message"
+ "Failed to get new pairing candidate from message"
+ "Failed to get paired device from message"
+ "Failed to serialize operational properties"
+ "Failed to serialize peer endpoint dictionary"
+ "Failed to unarchive object of type %@: %@"
+ "FailureDeviceAlreadyPaired"
+ "FailureIncorrectAuthenticationData"
+ "FailureTransportPairingFailed"
+ "Initial"
+ "Invalidated"
+ "IsExternalPairing"
+ "L2C"
+ "NRDevicePairingErrorOriginalCBUUIDKey"
+ "NRDevicePairingErrorOriginalNRUUIDKey"
+ "NRDevicePairingTarget[%@"
+ "NRLinkLinkToNexusLoop6LoWPANPacket"
+ "NRLinkLinkToNexusLoopPacket"
+ "NRPairedDevice[%@"
+ "P"
+ "PIN"
+ "PSM"
+ "PairedDevice"
+ "Pairing"
+ "PreSharedKey"
+ "PreviousPairing"
+ "StartingDiscovery"
+ "StartingPairing"
+ "StoppingDiscovery"
+ "StoppingPairing"
+ "T@\"NRDeviceIdentifier\",C,N,V_nrDeviceIdentifier"
+ "T@\"NRDeviceIdentifier\",R,N,V_nrDeviceIdentifier"
+ "T@\"NRDevicePairingTarget\",&,N,V_device"
+ "T@\"NSArray\",&,N,V_nrDeviceIdentifiers"
+ "TB,N,V_controlOnly"
+ "TB,N,V_datagramMode"
+ "TB,N,V_direct"
+ "TB,N,V_isExternalPairing"
+ "TB,N,V_isNotEncapsulated"
+ "TB,N,V_migrationPairing"
+ "TB,N,V_uses6LoWPAN"
+ "TS,N,V_psm"
+ "Unknown(%zu)"
+ "[D(%c%c%c) TF(%c%c) NH(%c) HLIM(%c%c) CID(%c) SAC(%c) SAM(%c%c) M(%c) DAC(%c) DAM(%c%c)"
+ "_NRKeyCreateLogString"
+ "_controlOnly"
+ "_datagramMode"
+ "_direct"
+ "_ipHeaderOffset"
+ "_isExternalPairing"
+ "_isNotEncapsulated"
+ "_migrationPairing"
+ "_newZeroingDataWithBytes:length:"
+ "_nrDeviceIdentifiers"
+ "_psm"
+ "_uses6LoWPAN"
+ "_xpcCommDictionaryCallback"
+ "controlOnly"
+ "createNSDataFromTLVIOVec"
+ "datagramMode"
+ "direct"
+ "getDefaultLinkSubtypeForLinkType:"
+ "initWithCapacity:"
+ "isExternalPairing"
+ "isNotEncapsulated"
+ "migrationPairing"
+ "nrDeviceIdentifiers"
+ "nrPacketTo6LoWPAN"
+ "nr_xpc_dictionary_get_nsobject"
+ "nr_xpc_dictionary_get_nsuuid"
+ "nr_xpc_dictionary_set_nsobject"
+ "nr_xpc_dictionary_set_nsuuid"
+ "numberWithUnsignedChar:"
+ "pending: %d expected: %d filledIn: %u"
+ "psm"
+ "setControlOnly:"
+ "setDatagramMode:"
+ "setDevice:"
+ "setDirect:"
+ "setIsExternalPairing:"
+ "setIsNotEncapsulated:"
+ "setMigrationPairing:"
+ "setNrDeviceIdentifiers:"
+ "setPsm:"
+ "setReceiveXPCCommDictionaryHandler:"
+ "setUses6LoWPAN:"
+ "uses6LoWPAN"
- "\x01\x14"
- "#\x14\xf0\xcd!\xf0\xd1"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (data) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (dstAddr) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (ioVecs) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (nrUUID) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (nrXPCQueue) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (outBuffer) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (packetBuffer) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (pairedDevice) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (pairedDevice.nrDeviceIdentifier) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (propertiesCopy.outOfBandKey) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (retNum) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (self.queue) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (srcAddr) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (targetUUID) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (xpcDict) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (xpcKey) != ((void *)0)"
- "%s%.30s:%-4d ABORTING: _strict_reallocf called with size 0"
- "%s%.30s:%-4d ABORTING: _strict_reallocf(%zu) failed"
- "%s%.30s:%-4d ABORTING: strict_malloc(%zu) failed"
- "%s%.30s:%-4d All-zero nrUUID in response from daemon"
- "%s%.30s:%-4d Failed to archive operational properties %@"
- "%s%.30s:%-4d Manager state change: %zu -> %zu"
- "%s%.30s:%-4d Missing nrUUID in response from daemon"
- "%{public}s Assertion Failed: (data) != ((void *)0)"
- "%{public}s Assertion Failed: (dstAddr) != ((void *)0)"
- "%{public}s Assertion Failed: (ioVecs) != ((void *)0)"
- "%{public}s Assertion Failed: (nrUUID) != ((void *)0)"
- "%{public}s Assertion Failed: (nrXPCQueue) != ((void *)0)"
- "%{public}s Assertion Failed: (outBuffer) != ((void *)0)"
- "%{public}s Assertion Failed: (packetBuffer) != ((void *)0)"
- "%{public}s Assertion Failed: (pairedDevice) != ((void *)0)"
- "%{public}s Assertion Failed: (pairedDevice.nrDeviceIdentifier) != ((void *)0)"
- "%{public}s Assertion Failed: (propertiesCopy.outOfBandKey) != ((void *)0)"
- "%{public}s Assertion Failed: (retNum) != ((void *)0)"
- "%{public}s Assertion Failed: (self.queue) != ((void *)0)"
- "%{public}s Assertion Failed: (srcAddr) != ((void *)0)"
- "%{public}s Assertion Failed: (targetUUID) != ((void *)0)"
- "%{public}s Assertion Failed: (xpcDict) != ((void *)0)"
- "%{public}s Assertion Failed: (xpcKey) != ((void *)0)"
- "%{public}s _strict_reallocf called with size 0"
- "%{public}s _strict_reallocf(%zu) failed"
- "%{public}s strict_malloc(%zu) failed"
- "-[NRBluetoothPacketParser start]_block_invoke_2"
- "-[NRDevicePairingManagerMuxEntry handleStartPairingRequestUpdate:]"
- "-[NRPairedDevice initInternal]"
- "Failed to archive device pairing manager info %@"
- "Failed to archive pairing target %@"
- "Failed to get pairing candidate from message"
- "Failed to unarchive NRDevicePairingCandidate %@"
- "Failed to unarchive NRDevicePairingTarget %@"
- "Invalid operational properties data"
- "Invalid operational properties data %@"
- "Missing or All-zero NRUUID from %@"
- "Start Pairing request result missing pairing target UUID"
- "T@\"NRDevicePairingTarget\",R,N"
- "T@\"NSUUID\",C,N,V_nrDeviceIdentifier"
- "TB,N,V_ephemeral"
- "[D%c%c%cTF%c%cNH%cHLIM%c%cCID%cSAC%cSAM%c%cM%cDAC%cDAM%c%c"
- "_strict_reallocf"
- "isEphemeral"
- "lrbIOVecLen=0 tlvLen=%u filledInLinkReadBufferBytes=%u handledLinkReadBufferBytes=%u"
- "null nrUUID"
- "setEphemeral:"
- "strict_calloc"
- "strict_malloc"

```
