## rapportd

> `/usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-751.200.74.0.0
-  __TEXT.__text: 0x19b184
-  __TEXT.__auth_stubs: 0x3a30
-  __TEXT.__objc_stubs: 0x14400
-  __TEXT.__objc_methlist: 0xada8
-  __TEXT.__const: 0x6640
-  __TEXT.__cstring: 0x3d716
+751.200.92.0.0
+  __TEXT.__text: 0x19d7d0
+  __TEXT.__auth_stubs: 0x3a50
+  __TEXT.__objc_stubs: 0x145c0
+  __TEXT.__objc_methlist: 0xae28
+  __TEXT.__const: 0x6700
+  __TEXT.__cstring: 0x3e016
   __TEXT.__objc_classname: 0x11af
   __TEXT.__objc_methtype: 0x4f81
-  __TEXT.__gcc_except_tab: 0x2550
-  __TEXT.__objc_methname: 0x1e7c0
-  __TEXT.__oslogstring: 0x3662
-  __TEXT.__swift5_typeref: 0x17ca
+  __TEXT.__gcc_except_tab: 0x2600
+  __TEXT.__objc_methname: 0x1eac0
+  __TEXT.__oslogstring: 0x3682
+  __TEXT.__swift5_typeref: 0x17d8
   __TEXT.__swift5_capture: 0xb78
-  __TEXT.__swift5_reflstr: 0xfc4
-  __TEXT.__swift5_assocty: 0x190
-  __TEXT.__constg_swiftt: 0xe60
+  __TEXT.__swift5_reflstr: 0xff4
+  __TEXT.__swift5_assocty: 0x1a8
+  __TEXT.__constg_swiftt: 0xe84
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_fieldmd: 0xf3c
-  __TEXT.__swift5_proto: 0x1cc
-  __TEXT.__swift5_types: 0xfc
+  __TEXT.__swift5_fieldmd: 0xf70
+  __TEXT.__swift5_proto: 0x1d8
+  __TEXT.__swift5_types: 0x100
   __TEXT.__swift_as_entry: 0x1fc
   __TEXT.__swift_as_ret: 0x248
   __TEXT.__swift_as_cont: 0x3dc
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7848
-  __TEXT.__eh_frame: 0x4c4c
-  __DATA_CONST.__const: 0x86f8
-  __DATA_CONST.__cfstring: 0xa180
+  __TEXT.__unwind_info: 0x78e0
+  __TEXT.__eh_frame: 0x4c8c
+  __DATA_CONST.__const: 0x88a0
+  __DATA_CONST.__cfstring: 0xa400
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x1d28
+  __DATA_CONST.__auth_got: 0x1d38
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__auth_ptr: 0x670
-  __DATA.__objc_const: 0x12cb0
-  __DATA.__objc_selrefs: 0x6570
-  __DATA.__objc_ivar: 0x11f8
+  __DATA.__objc_const: 0x12d18
+  __DATA.__objc_selrefs: 0x6600
+  __DATA.__objc_ivar: 0x1200
   __DATA.__objc_data: 0x2f70
-  __DATA.__data: 0x3e08
+  __DATA.__data: 0x3e18
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8973
-  Symbols:   1462
-  CStrings:  11868
+  Functions: 9008
+  Symbols:   1464
+  CStrings:  11947
 
Symbols:
+ _nw_parameters_get_advertise_wake_to_peer_to_peer_responder
+ _nw_parameters_get_high_power_peer_to_peer_discovery
CStrings:
+ " homeAccessory"
+ "### Failed to find multi-user device for identifier %@\n"
+ "### Received multi-user device add event without identifier: %@\n"
+ "### Received multi-user device removed event without identifier: %@\n"
+ "### Reject message for multi-user device on unauthenticated connection: %@"
+ "%s unexpected in %s phase"
+ "-[RPCompanionLinkDaemon _multiUserDevice:receivedRequestID:request:options:responseHandler:cnx:]"
+ "-[RPCompanionLinkDaemon _multiUserDeviceAdded:connection:responseHandler:]"
+ "-[RPCompanionLinkDaemon _multiUserDeviceAdded:connection:responseHandler:]_block_invoke"
+ "-[RPCompanionLinkDaemon _multiUserDeviceRemoved:connection:]"
+ "-[RPCompanionLinkDaemon registerForDaemonEvents]_block_invoke_4"
+ "-[RPCompanionLinkXPCConnection _effectiveMultiUserDestinationForDestination:]"
+ "Add multi-user active device: %@ from connection %@ altDSID %@\n"
+ "AudioAccessory11,1"
+ "B525ish"
+ "Connection to %@ is to multi-user destination %@"
+ "DeviceEnclosureColor"
+ "Found better matching multi-user device='%@'\n"
+ "HasHomeAccessoryForce: %d -> %d\n"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "J490Setup"
+ "J491Setup"
+ "Multi-user device identifier missing"
+ "Multi-user device not found"
+ "Received EventID '%@' for multi-user device '%@'\n"
+ "Received requestID '%@' for multi-user device %@"
+ "Remove multi-user active device ( %@ ) from connection ( %@ )\n"
+ "Replacing existing multi-user device ( %@ ) with new ( %@ ) on %@\n"
+ "Unable to map DirectPeer to destination ID"
+ "_aaltDSID"
+ "_destinationID:matchesMultiUserDeviceOnCnx:"
+ "_effectiveMultiUserDestinationForDestination:"
+ "_handleFirstUnlock"
+ "_idHKU"
+ "_idsHasHomeAccessoryCache"
+ "_isAccountCheckedDevice:"
+ "_muDI"
+ "_multiUserDevice:receivedRequestID:request:options:responseHandler:cnx:"
+ "_multiUserDeviceAdded:connection:responseHandler:"
+ "_multiUserDeviceRemoved:connection:"
+ "_multiUserUpdateOptions:withDestination:"
+ "_prefHasHomeAccessoryForce"
+ "_sigHKU"
+ "_sigPD"
+ "_sigRP"
+ "accountOwnerCheckApplies"
+ "com.apple.callservicesd.audioRouteTransfer"
+ "com.apple.callservicesd.requestCallDisplayDetails"
+ "com.apple.callservicesd.requestRingtoneConfiguration"
+ "com.apple.callservicesd.transferActiveConversation"
+ "com.apple.callservicesd.transferContinuityCall"
+ "com.apple.callservicesd.updateBlockedState"
+ "com.apple.nearbyd.perception.generic.data"
+ "exchangePAKEIdentities(clientIdentity:deviceName:givenName:familyName:)"
+ "hasHomeAccessoryForce"
+ "homeAccessoryVariant"
+ "homeDidSetHasOwnerAcknowledgedHomePodSiriOnboarding:"
+ "iPhoneDuo"
+ "idsHasHomeAccessory"
+ "localAccountUpdated"
+ "multiUserDevID"
+ "multiUserDevices"
+ "pairAndReceiveIdentity(pairingData:)"
+ "pairAndReceiveTemporaryIdentities(pairingData:)"
+ "pairing"
+ "phase"
+ "prePairing"
+ "resolveBonjour(clientPublicKey:)"
+ "resolveBonjourCompleted()"
+ "resolveBonjourEncryptedWithSessionID(encryptedRequest:sessionID:)"
+ "setMultiUserDevices:"
+ "shareIdentity(_:)"
+ "shareTemporaryIdentities(_:)"
+ "startPairVerifyWithSessionID(createEncryptionStream:)"
+ "updateMultiUserDeviceWithPeer:"
+ "v16@?0Q8"
+ "verifyIdentityProof:accountAltDSID:"
+ "verifyMUHomeKitIdentityProof:identifier:accountAltDSID:completion:"
- "DeviceColor"
```
