## terminusd

> `/usr/libexec/terminusd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-914.42.1.0.0
-  __TEXT.__text: 0x1fc1d8
-  __TEXT.__auth_stubs: 0x3f10
-  __TEXT.__objc_stubs: 0x8e00
-  __TEXT.__objc_methlist: 0x5594
+914.60.11.0.0
+  __TEXT.__text: 0x20ddac
+  __TEXT.__auth_stubs: 0x4180
+  __TEXT.__objc_stubs: 0x9680
+  __TEXT.__objc_methlist: 0x5a04
   __TEXT.__const: 0x73c
   __TEXT.__swift5_typeref: 0x4ce
-  __TEXT.__cstring: 0x52bcf
+  __TEXT.__cstring: 0x560c5
   __TEXT.__swift5_capture: 0x4a4
-  __TEXT.__objc_methtype: 0x433b
-  __TEXT.__oslogstring: 0x2dee
+  __TEXT.__objc_methtype: 0x452a
+  __TEXT.__oslogstring: 0x2de8
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_reflstr: 0x8b
   __TEXT.__swift5_fieldmd: 0xf0
-  __TEXT.__objc_classname: 0x14dc
-  __TEXT.__objc_methname: 0x129b5
+  __TEXT.__objc_classname: 0x1659
+  __TEXT.__objc_methname: 0x133b5
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x18

   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__gcc_except_tab: 0x63b4
-  __TEXT.__unwind_info: 0x3ea8
+  __TEXT.__gcc_except_tab: 0x6838
+  __TEXT.__unwind_info: 0x41a8
   __TEXT.__eh_frame: 0xeb8
-  __DATA_CONST.__const: 0x4f40
-  __DATA_CONST.__cfstring: 0xe280
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__const: 0x5478
+  __DATA_CONST.__cfstring: 0xe9a0
+  __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1a0
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x3c8
-  __DATA_CONST.__objc_intobj: 0x7b0
-  __DATA_CONST.__objc_arraydata: 0xd0
-  __DATA_CONST.__objc_arrayobj: 0x120
+  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_intobj: 0x7e0
+  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1f98
-  __DATA_CONST.__got: 0xf08
+  __DATA_CONST.__auth_got: 0x20d0
+  __DATA_CONST.__got: 0xf28
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x19f78
-  __DATA.__objc_selrefs: 0x2b60
-  __DATA.__objc_ivar: 0x208c
-  __DATA.__objc_data: 0x38f0
-  __DATA.__data: 0x1938
+  __DATA.__objc_const: 0x1b0e0
+  __DATA.__objc_selrefs: 0x2d80
+  __DATA.__objc_ivar: 0x2198
+  __DATA.__objc_data: 0x3d00
+  __DATA.__data: 0x19f8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3910
-  Symbols:   1550
-  CStrings:  11633
+  Functions: 4087
+  Symbols:   1592
+  CStrings:  12050
 
Symbols:
+ _OBJC_CLASS_$_NEIKEv2TLSSPI
+ _OBJC_CLASS_$_NRMeshTerminusLinkInfo
+ _OBJC_CLASS_$_TRIClient
+ _SecCertificateCopyKey
+ _nw_agent_add_tls_psk_derivation_context
+ _nw_agent_flush_tls_psk_derivation_contexts
+ _nw_agent_remove_tls_psk_derivation_context
+ _nw_browse_descriptor_create_application_service
+ _nw_browse_descriptor_set_browse_scope
+ _nw_browse_descriptor_set_device_types
+ _nw_connection_copy_protocol_metadata
+ _nw_connection_group_cancel
+ _nw_connection_group_set_new_connection_handler
+ _nw_connection_group_set_queue
+ _nw_connection_group_set_state_changed_handler
+ _nw_connection_group_start
+ _nw_connection_receive_message
+ _nw_content_context_get_is_final
+ _nw_framer_create_definition
+ _nw_framer_create_options
+ _nw_framer_deliver_input_no_copy
+ _nw_framer_mark_failed_with_error
+ _nw_framer_message_create
+ _nw_framer_parse_input
+ _nw_framer_set_input_handler
+ _nw_framer_set_output_handler
+ _nw_framer_write_output
+ _nw_framer_write_output_no_copy
+ _nw_listener_set_new_connection_group_handler
+ _nw_listener_set_state_changed_handler
+ _nw_masque_server_set_tls_epsk_derivation_service_info_with_agent_resolver
+ _nw_parameters_set_preferred_netagent_classes
+ _nw_protocol_copy_quic_definition
+ _nw_proxy_hop_set_tls_epsk_derivation_service_info
+ _nw_proxy_hop_set_use_pqtls
+ _nw_proxy_hop_set_use_x25519
+ _nw_quic_copy_sec_protocol_metadata
+ _nw_swift_tls_create_options
+ _sec_certificate_copy_ref
+ _sec_protocol_metadata_access_peer_certificate_chain
+ _sec_protocol_metadata_copy_peer_public_key
+ _sec_protocol_options_set_tls_early_data_enabled
CStrings:
+ "\n  SPI %@ -> agent %@"
+ "\nCompanion APL allowed: %@"
+ "\nMASQUE RPK port: %u"
+ "\nMASQUE RPK server: %@"
+ "\nMASQUE TLS SA instance ID: %@"
+ "\nMASQUE TLS SA port: %u"
+ "\nMASQUE TLS SA server: %@"
+ "\nTLS SA %@ inbound SPI registry: %lu entries"
+ " cancelled"
+ "%@ %@ (in) %@"
+ "%@ %@ (in) %@ (out) %@"
+ "%@ %@ (out) %@"
+ "%@ Flush %@"
+ "%@ TLS SA service instance ID missing or invalid length"
+ "%@ failed to start with error %@"
+ "%@ link has no TLS SA Class D agent"
+ "%@: No TLS SA agent for %@ at flush - caller must filter by agent presence"
+ "%@: No TLS SA agent for %@ at install - caller must filter by agent presence"
+ "%@: No TLS SA agent for %@ at uninstall - caller must filter by agent presence"
+ "%@: TLS child SA %u install from %@ %@: invalid class"
+ "%@: TLS child SA %u install from %@ has invalid key length inbound=%zu outbound=%zu"
+ "%@: TLS child SA %u install from %@ has no direction"
+ "%@: TLS child SA ID changed for %@ from %u to %u (session %@) - refusing install"
+ "%@: failed to copy connection group (id: %llu)"
+ "%@InboundSPI"
+ "%@OutboundSPI"
+ "%@UUID"
+ "%s (flags %#x, A/B bucket %@, Trial: %@)"
+ "%s called with null group"
+ "%s called with null peerDeviceID"
+ "%s called with null remoteIDSDeviceID"
+ "%s called with null result"
+ "%s%.30s:%-4d %@ Updating usesPSKForMASQUE %d to %d"
+ "%s%.30s:%-4d %@ cancelled"
+ "%s%.30s:%-4d %@ received %lu-byte packet %@ from peer %@ (%@)"
+ "%s%.30s:%-4d %@ resumed, resending hello, routes and pending link requests"
+ "%s%.30s:%-4d %@ started %u"
+ "%s%.30s:%-4d %@: %@ %@ but is endpoint type %u, not ASQUIC"
+ "%s%.30s:%-4d %@: %@ %@ but its IDS device ID is missing or empty"
+ "%s%.30s:%-4d %@: %@ is our own advertisement, ignoring"
+ "%s%.30s:%-4d %@: Not restarting %@ session due to auth failure, waiting for remote unlock"
+ "%s%.30s:%-4d %@: TLS child SA %u install %@ has no agent to receive it on this link - dropping"
+ "%s%.30s:%-4d %@: advertising '%@'"
+ "%s%.30s:%-4d %@: already have an interface for %@, not adding one for peer %@"
+ "%s%.30s:%-4d %@: already have an outbound connection to peer %@"
+ "%s%.30s:%-4d %@: already started"
+ "%s%.30s:%-4d %@: browse change %#llx, batch complete %d"
+ "%s%.30s:%-4d %@: browse result with no endpoint"
+ "%s%.30s:%-4d %@: browser failed, restarting (attempt %u): %@"
+ "%s%.30s:%-4d %@: browser state %u, error %@"
+ "%s%.30s:%-4d %@: browsing '%@'"
+ "%s%.30s:%-4d %@: cancelling browser"
+ "%s%.30s:%-4d %@: cancelling listener"
+ "%s%.30s:%-4d %@: cannot activate mesh link because there is no mesh pairing key"
+ "%s%.30s:%-4d %@: cannot activate mesh link because there is no mesh pairing nonce"
+ "%s%.30s:%-4d %@: cannot activate mesh link because we have no IDS device ID"
+ "%s%.30s:%-4d %@: connection to peer %@ has no interface on its path"
+ "%s%.30s:%-4d %@: connection to peer %@ is on %@, which Babel doesn't use"
+ "%s%.30s:%-4d %@: connection to peer %@ on %@ has no remote address"
+ "%s%.30s:%-4d %@: created %@ for peer %@ from its connection's path, as %@"
+ "%s%.30s:%-4d %@: dropping inbound group %@ (%@)"
+ "%s%.30s:%-4d %@: dropping outbound connection to peer %@"
+ "%s%.30s:%-4d %@: hello names device %@, replacing %@"
+ "%s%.30s:%-4d %@: inbound connection %@ has no interface or remote address, so its group %@ isn't recorded"
+ "%s%.30s:%-4d %@: inbound connection %@ is ready, but its group %@ was dropped"
+ "%s%.30s:%-4d %@: inbound connection group %@"
+ "%s%.30s:%-4d %@: inbound connection state %s, error %@"
+ "%s%.30s:%-4d %@: inbound connection under %@ from peer %@, but we are the initiator"
+ "%s%.30s:%-4d %@: inbound group %@ is ready, connection %@"
+ "%s%.30s:%-4d %@: inbound group %@ replaces group %@ as %@, cancelling the older one"
+ "%s%.30s:%-4d %@: inbound group state %u, error %@"
+ "%s%.30s:%-4d %@: initiating connection to peer %@ (%@)"
+ "%s%.30s:%-4d %@: listener failed, restarting (attempt %u): %@"
+ "%s%.30s:%-4d %@: listener state %u, error %@"
+ "%s%.30s:%-4d %@: mesh pairing key %@"
+ "%s%.30s:%-4d %@: no QUIC options for accepted connection (id: %llu)"
+ "%s%.30s:%-4d %@: no mesh identifier"
+ "%s%.30s:%-4d %@: not connected, dropping packet to peer %@"
+ "%s%.30s:%-4d %@: outbound connection to peer %@ state %s, error %@"
+ "%s%.30s:%-4d %@: peer %@ %@, our IKE role %@"
+ "%s%.30s:%-4d %@: peer %@ reconnected as %@ with a new TLS key, replacing its interface"
+ "%s%.30s:%-4d %@: peer %@ reconnected as %@, removing its interface under %@"
+ "%s%.30s:%-4d %@: peer %@ reconnected as %@, resuming its interface"
+ "%s%.30s:%-4d %@: reconnecting to peer %@ in %lld ms (attempt %u)"
+ "%s%.30s:%-4d %@: recorded inbound group %@ as %@"
+ "%s%.30s:%-4d %@: refused resolve for peer %@: %@"
+ "%s%.30s:%-4d %@: refusing Rapport-key pairing for mesh device %@ (session %@)"
+ "%s%.30s:%-4d %@: refusing Rapport-key pairing for mesh device %@, which has no out of band key"
+ "%s%.30s:%-4d %@: removing %@ (%@)"
+ "%s%.30s:%-4d %@: starting, local device ID %@, advertise scope %#x, browse scope %#x"
+ "%s%.30s:%-4d %@: the connection under %@ ended, pausing its interface for %u s"
+ "%s%.30s:%-4d %@: with device ID %@ in peer's hello"
+ "%s%.30s:%-4d %lu-byte packet is too long to send over ASQUIC"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (self.server) != ((void*)0)"
+ "%s%.30s:%-4d APL negotiation: both sides support APL"
+ "%s%.30s:%-4d APL negotiation: both sides use APL"
+ "%s%.30s:%-4d APL negotiation: disabling local APL"
+ "%s%.30s:%-4d APL negotiation: local doesn't support APL, remote will disable"
+ "%s%.30s:%-4d APL negotiation: local doesn't use APL, enabling"
+ "%s%.30s:%-4d APL negotiation: neither side supports APL"
+ "%s%.30s:%-4d APL negotiation: remote doesn't support APL"
+ "%s%.30s:%-4d APL negotiation: remote doesn't use APL yet, remote will enable"
+ "%s%.30s:%-4d Assigned APL A/B bucket %u"
+ "%s%.30s:%-4d Companion APL Trial configuration changed, APL allowed for this device: %d"
+ "%s%.30s:%-4d Created TLS SA agent %@ (%@)"
+ "%s%.30s:%-4d Deferring APL activation until next Bluetooth reconnection to avoid link churn"
+ "%s%.30s:%-4d Failed to create MASQUE RPK server"
+ "%s%.30s:%-4d Failed to create MASQUE TLS SA server"
+ "%s%.30s:%-4d Failed to create TLS SA agent"
+ "%s%.30s:%-4d Failed to start MASQUE RPK server without local identity"
+ "%s%.30s:%-4d Ignoring mesh link response claiming responder 0x%llx from neighbour %@ (rid 0x%llx)"
+ "%s%.30s:%-4d Ignoring out of range APL A/B bucket %u"
+ "%s%.30s:%-4d Invalidating TLS SA agent %@"
+ "%s%.30s:%-4d Mesh link response for responder 0x%llx with no query in flight (already completed or timed out)"
+ "%s%.30s:%-4d Mesh link response truncated: %lu entries exceeds max %u per TLV"
+ "%s%.30s:%-4d Mesh not registered, returning empty meshInfo for active link query"
+ "%s%.30s:%-4d No TLS SA agent for offered inbound SPI %@ class %@ (%lu registered)"
+ "%s%.30s:%-4d No Trial client, the companion APL A/B cannot be configured remotely"
+ "%s%.30s:%-4d Received mesh active link query from %@"
+ "%s%.30s:%-4d Received mesh link query req=0x%llx from %@"
+ "%s%.30s:%-4d Received mesh link response rsp=0x%llx req=0x%llx entries=%lu from %@"
+ "%s%.30s:%-4d Sending mesh link response responder=0x%llx requester=0x%llx product=%@ build=%@ room=%@ entries=%lu to %@"
+ "%s%.30s:%-4d TLS SA fallback agent %@: installed random outbound SPI %@"
+ "%s%.30s:%-4d Trial companion APL config: active %d aplAllowed %d allowedPercentNonAI %u ids %@"
+ "%s%.30s:%-4d Trial factor '%@' is missing or not a boolean, leaving APL allowed"
+ "%s%.30s:%-4d Trial factor '%@' is missing or not a long, not running the split"
+ "%s%.30s:%-4d Trial factor '%@' is out of range (%lld), not running the split"
+ "%s%.30s:%-4d Trial namespace updated, applying the companion APL change in %us"
+ "%s%.30s:%-4d client connection cancelled (id: %llu)"
+ "%s%.30s:%-4d client connection received (id: %llu)"
+ "%s%.30s:%-4d client connection started (id: %llu)"
+ "%s%.30s:%-4d connection to peer %@ has no remote address"
+ "%s%.30s:%-4d dropping %lu bytes from peer %@ that aren't a Babel packet"
+ "%s%.30s:%-4d failed to receive from peer %@: %@"
+ "%s%.30s:%-4d failed to send %zu bytes to peer %@, cancelling the connection: %@"
+ "%s%.30s:%-4d force sending resolve request for %@ with new public keys, superseding token %@"
+ "%s%.30s:%-4d insufficient data length for %u-byte product type + %u-byte build version + %u-byte room name + %u links (%lu < %lu)"
+ "%s%.30s:%-4d link count %lu exceeds max %zu per TLV; truncating"
+ "%s%.30s:%-4d not using APL due to Trial global switch"
+ "%s%.30s:%-4d peer %@ closed its connection"
+ "%s%.30s:%-4d start MASQUE servers : RPK=%@ TLS-SA=%@"
+ "%s%.30s:%-4d using cached tokens from %@ for %@ (id: %llu)"
+ "%{public}s Assertion Failed: (self.server) != ((void*)0)"
+ "+"
+ "+[NRDLocalDevice updateUsesPSKForMASQUE:nrUUID:]"
+ "+[NRDTrialClient start]_block_invoke"
+ "-[NRBabelASQUICConnectionTransport handleReceivedPacketData:]"
+ "-[NRBabelASQUICConnectionTransport initWithConnection:peerDeviceID:]"
+ "-[NRBabelASQUICConnectionTransport receive]_block_invoke"
+ "-[NRBabelASQUICConnectionTransport sendPacket:]"
+ "-[NRBabelASQUICConnectionTransport sendPacket:]_block_invoke"
+ "-[NRBabelASQUICConnectionTransport updatePeerDevice:]"
+ "-[NRBabelASQUICTransport addInterfaceForPeer:connection:]"
+ "-[NRBabelASQUICTransport addInterfaceForPeer:connection:]_block_invoke"
+ "-[NRBabelASQUICTransport cancel]"
+ "-[NRBabelASQUICTransport connectToPeer:endpoint:]"
+ "-[NRBabelASQUICTransport connectToPeer:endpoint:]_block_invoke"
+ "-[NRBabelASQUICTransport dealloc]"
+ "-[NRBabelASQUICTransport handleBrowseResultChangeFrom:to:batchComplete:]"
+ "-[NRBabelASQUICTransport handleInboundConnectionGroup:]"
+ "-[NRBabelASQUICTransport handleInboundConnectionGroup:]_block_invoke_2"
+ "-[NRBabelASQUICTransport handleInboundConnectionReady:group:]"
+ "-[NRBabelASQUICTransport handleResult:reason:removed:]"
+ "-[NRBabelASQUICTransport init]"
+ "-[NRBabelASQUICTransport pauseInterfaceForNeighbourKey:]"
+ "-[NRBabelASQUICTransport recordInboundGroup:connection:]"
+ "-[NRBabelASQUICTransport removeInboundGroup:]"
+ "-[NRBabelASQUICTransport removeInterfaceForNeighbourKey:]"
+ "-[NRBabelASQUICTransport removeOutboundConnectionForPeer:]"
+ "-[NRBabelASQUICTransport removePausedInterfacesForPeer:exceptNeighbourKey:]"
+ "-[NRBabelASQUICTransport replaceFailedBrowser:]"
+ "-[NRBabelASQUICTransport replaceFailedListener:]"
+ "-[NRBabelASQUICTransport scheduleReconnectToPeer:]"
+ "-[NRBabelASQUICTransport startAdvertising]"
+ "-[NRBabelASQUICTransport startAdvertising]_block_invoke"
+ "-[NRBabelASQUICTransport startBrowsing]"
+ "-[NRBabelASQUICTransport startBrowsing]_block_invoke"
+ "-[NRBabelASQUICTransport startInboundConnection:group:]"
+ "-[NRBabelASQUICTransport startInboundConnection:group:]_block_invoke"
+ "-[NRBabelASQUICTransport startWithLocalIDSDeviceID:meshIdentifier:]"
+ "-[NRBabelInterface initWithInterface:transport:]"
+ "-[NRBabelManager asquicTransport:didResumeInterface:]"
+ "-[NRBabelManager copyBaseDeviceInfoForSource:]"
+ "-[NRBabelManager handleMeshLinkQuery:fromNeighbour:]"
+ "-[NRBabelManager handleMeshLinkResponse:fromNeighbour:]"
+ "-[NRBabelManager sendMeshLinkResponseEntries:requesterRid:responderRid:productType:buildVersion:roomName:toNeighbour:]"
+ "-[NRBabelSubTLVAppleMeshPairingNonce initWithIncomingData:type:]"
+ "-[NRBabelTLVAppleMeshLinkQuery initWithIncomingData:type:]"
+ "-[NRBabelTLVAppleMeshLinkResponse copySendData]"
+ "-[NRBabelTLVAppleMeshLinkResponse initWithIncomingData:type:]"
+ "-[NRBabelTLVDeviceID initWithIncomingData:type:]"
+ "-[NRDDeviceConductor shouldSendResolveRequestForASName:]"
+ "-[NRDMASQUERPKServerContext createServer]"
+ "-[NRDMASQUERPKServerContext handleNewConnectionReceivedWithIdentifier:]"
+ "-[NRDMASQUEServerContext copyAcceptedConnectionQUICOptionsWithIdentifier:]"
+ "-[NRDMASQUEServerContext copyMASQUEServerParameters]"
+ "-[NRDMASQUEServerContext initWithLinkDirector:]"
+ "-[NRDMASQUEServerContext setupHandlers]_block_invoke"
+ "-[NRDMASQUEServerContext setupHandlers]_block_invoke_3"
+ "-[NRDMASQUEServerContext setupHandlers]_block_invoke_4"
+ "-[NRDMASQUEServerContext setupHandlers]_block_invoke_5"
+ "-[NRDMASQUETLSSAServerContext createServer]"
+ "-[NRDeviceEndpoint initWithRemoteIDSDeviceID:]"
+ "-[NRLink handleTLSChildSAInstalled:inbound:outbound:ikeSession:dataProtectionClass:]"
+ "-[NRLinkDirector cancelMASQUERPKServer]"
+ "-[NRLinkDirector cancelMASQUETLSSAServer]"
+ "-[NRLinkDirector negotiateCompanionAPLForNRUUID:localCapabilities:remoteCapabilities:]"
+ "-[NRLinkDirector queryActiveMeshLinksWithCompletionBlock:queue:]"
+ "-[NRLinkDirector registerTLSSAInboundSPI:forLink:dataProtectionClass:]"
+ "-[NRLinkDirector setupAppVPNWatcher]_block_invoke_2"
+ "-[NRLinkDirector tlsSAAgentUUIDForInboundSPI:dataProtectionClass:]"
+ "-[NRLinkDirector unregisterAllTLSSAInboundSPIsForLink:dataProtectionClass:]"
+ "-[NRLinkDirector unregisterTLSSAInboundSPI:forLink:dataProtectionClass:]"
+ "-[NRPairingClient setupInitiator]"
+ "-[NRTLSSAAgent initFallbackAgentWithNRUUID:dataProtectionClass:queue:]"
+ "-[NRTLSSAAgent initWithAgentName:nrUUID:dataProtectionClass:queue:]"
+ "-[NRTLSSAAgent invalidate]"
+ "914.60.11"
+ "<invalidated>"
+ "@\"<NRBabelASQUICTransportDelegate>\""
+ "@\"<NRBabelInterfaceTransport>\""
+ "@\"NEIKEv2TLSSPI\""
+ "@\"NRBabelASQUICTransport\""
+ "@\"NRBabelInterface\""
+ "@\"NRDMASQUERPKServerContext\""
+ "@\"NRDMASQUETLSSAServerContext\""
+ "@\"NRLinkDirector\""
+ "@\"NRTLSSAAgent\""
+ "@\"NSArray\"16@0:8"
+ "AppleMeshLinkQuery"
+ "AppleMeshLinkResponse"
+ "B24@?0Q8[16C]16"
+ "BuildVersion"
+ "Derived out-of-band key for terminus mesh pairing"
+ "DeviceID"
+ "Failed to send packet %@, no interface found for neighbour %@"
+ "Failed to serialize meshInfo for active link query"
+ "L_TLSSAInstall"
+ "L_TLSSAUninstall"
+ "MASQUE"
+ "MASQUE TLS SA service instance ID missing or invalid length"
+ "MASQUE-RPK"
+ "MASQUE-TLS-SA"
+ "MeshASQUIC"
+ "NRBabelASQUICConnectionTransport"
+ "NRBabelASQUICConnectionTransport[%@, %@]"
+ "NRBabelASQUICPeerResponder"
+ "NRBabelASQUICTransport"
+ "NRBabelASQUICTransportDelegate"
+ "NRBabelASQUICTransport[%@]"
+ "NRBabelInterfaceTransport"
+ "NRBabelInterface[%llu, intf: %@[%u], mcast-seqno: %u, %@]"
+ "NRBabelMeshLinkEntry"
+ "NRBabelSubTLVAppleMeshPairingNonce"
+ "NRBabelTLVAppleMeshLinkQuery"
+ "NRBabelTLVAppleMeshLinkQuery[req=0x%llx]"
+ "NRBabelTLVAppleMeshLinkResponse"
+ "NRBabelTLVAppleMeshLinkResponse[rsp=0x%llx req=0x%llx product=%@ build=%@ room=%@ links=%lu]"
+ "NRBabelTLVDeviceID"
+ "NRCreateLocalIdentity failed"
+ "NRDMASQUERPKServerContext"
+ "NRDMASQUEServerContext"
+ "NRDMASQUETLSSAServerContext"
+ "NRDTrialClient"
+ "NRDTrialHandleNamespaceUpdate"
+ "NRDTrialReloadCompanionAPLConfig"
+ "NRTLSSAAgent"
+ "No local IDS device ID available"
+ "No mesh pairing nonce available"
+ "No pairing key available"
+ "PSKForMASQUE"
+ "Peer wired endpoint changed"
+ "ProductType"
+ "Q16@?0@\"NSObject<OS_nw_framer>\"8"
+ "Q28@?0*8Q16B24"
+ "RapportBrowseAgent"
+ "TB,R,N"
+ "TB,R,N,V_needsTLSSAForASQUIC"
+ "TB,R,N,V_needsTLSSAForMASQUE"
+ "TERMINUS_COMPANION_APL"
+ "TLSSA"
+ "Terminus TLS SA \"%@\" %@ %@"
+ "Terminus TLS SA fallback \"%@\" %@"
+ "[%@ port=%u%s]"
+ "_agent"
+ "_agentUUID"
+ "_asquicTransport"
+ "_browserRetryCount"
+ "_buildVersion"
+ "_catchAllTLSSAAgent"
+ "_dataProtectionClass"
+ "_inboundConnections"
+ "_inboundGroups"
+ "_inboundGroupsByNeighbourKey"
+ "_inboundSPICurrent"
+ "_isLinkWithDistributee"
+ "_isLinkWithPrimaryAssistDevice"
+ "_linkDirector"
+ "_listenerRetryCount"
+ "_localCapabilities"
+ "_masqueRPKContext"
+ "_masqueTLSSAContext"
+ "_meshLinkResponseHandler"
+ "_meshPairingNonce"
+ "_needsTLSSAForASQUIC"
+ "_needsTLSSAForMASQUE"
+ "_nonce"
+ "_nr-mesh-control._udp"
+ "_outboundConnections"
+ "_outboundSPICurrent"
+ "_outgoingResolveASNameToPublicKeys"
+ "_pauseTimer"
+ "_peerDeviceHandler"
+ "_peerKey"
+ "_peerResponders"
+ "_peerRid"
+ "_peerSupportsPSKForMASQUE"
+ "_peerTransportsByNeighbourKey"
+ "_productType"
+ "_receivedCapabilities"
+ "_reconnectCount"
+ "_reconnectScheduled"
+ "_requesterRid"
+ "_responderRid"
+ "_roomName"
+ "_rssi"
+ "_tlsSAAgentClassC"
+ "_tlsSAAgentClassD"
+ "_tlsSAChildIDClassC"
+ "_tlsSAChildIDClassD"
+ "_tlsSAInboundSPIRegistryClassC"
+ "_tlsSAInboundSPIRegistryClassD"
+ "_tlsSAServiceInstanceID"
+ "_tokenCache"
+ "_transport"
+ "addUpdateHandlerForNamespaceName:queue:usingBlock:"
+ "allKeysForObject:"
+ "aplAllowed %d allowedPercentNonAI %u %@"
+ "apl_allowed"
+ "apl_allowed_percent_non_ai"
+ "appendTLSSAStatusToString:"
+ "asquicTransport:didAddInterface:"
+ "asquicTransport:didRemoveInterface:"
+ "asquicTransport:didResumeInterface:"
+ "a\x81"
+ "booleanValue"
+ "cacheFactorLevelsWithNamespaceName:"
+ "cancelWithCompletionHandler:"
+ "client unavailable"
+ "com.apple.networkrelay.proxy.masque"
+ "com.apple.rapport.browse"
+ "companionAPLABBucket"
+ "copyBabelASQUICPacketContent"
+ "copyServerTypeLabel"
+ "createServer"
+ "deploymentId"
+ "deviceEndpoints"
+ "experimentId"
+ "experimentIdentifiersWithNamespaceName:"
+ "found"
+ "handleMeshMonitorQueryActiveLinks"
+ "handleNewConnectionReceivedWithIdentifier:"
+ "hasPerDataClassIKESessions"
+ "i16@?0@\"NSObject<OS_nw_framer>\"8"
+ "indexOfObjectIdenticalTo:"
+ "initWithLength:"
+ "initWithProtocol:"
+ "initWithValue:"
+ "interfaces changed"
+ "isSubsetOfSet:"
+ "key"
+ "levelForFactor:withNamespaceName:"
+ "levelOneOfCase"
+ "longValue"
+ "lost"
+ "mesh pairing nonce is %lu bytes, not %d"
+ "meshParticipantInfo"
+ "mutableBytes"
+ "needsChildSA"
+ "needsTLSSA"
+ "needsTLSSAForASQUIC"
+ "needsTLSSAForClassC"
+ "needsTLSSAForClassD"
+ "needsTLSSAForMASQUE"
+ "no active experiment"
+ "nrCF"
+ "numberWithChar:"
+ "nw_browse_descriptor_create_application_service failed"
+ "nw_browser_create failed"
+ "nw_connection_create failed"
+ "nw_listener_create failed"
+ "nw_parameters_create_application_service_quic_using_identity failed"
+ "refresh"
+ "registerTLSSAInboundSPI %@ class=%u: link has no agent for that class"
+ "registerTLSSAInboundSPI:forLink:dataProtectionClass:"
+ "removeObjectIdenticalTo:"
+ "sendMulticastPacket:"
+ "sendUnicastPacket:destinationDevice:"
+ "setActiveMeshLinks:"
+ "setBuildVersion:"
+ "setIsLinkWithDistributee:"
+ "setIsLinkWithPrimaryAssistDevice:"
+ "setLinkSubtype:"
+ "setLinkType:"
+ "setPeerApplicationIdentifier:"
+ "setPeerDeviceIdentifier:"
+ "setPeerName:"
+ "setProductType:"
+ "setRespondedWithinTimeout:"
+ "setRoomName:"
+ "setTlsChildSAInstallBlock:"
+ "setTlsChildSAUninstallBlock:"
+ "setUsesPSKForMASQUE:"
+ "setWifiAwareRSSI:"
+ "setupTLSSACallbacksForIKESession:dataProtectionClass:"
+ "sortedArrayUsingSelector:"
+ "spi"
+ "stringByAppendingString:"
+ "terminusd.trial"
+ "terminusdSettingsCompanionAPLTrialConfigChanged"
+ "terminusdSettingsGetCompanionAPLABBucket"
+ "terminusdSettingsPeekCompanionAPLABBucket"
+ "tlsSAAgent%@"
+ "tlsSAAgentUUIDForDataProtectionClass:"
+ "treatmentId"
+ "trialDeploymentId"
+ "trialExperimentId"
+ "trialTreatmentId"
+ "unassigned"
+ "unregisterAllTLSSAInboundSPIsForLink:dataProtectionClass:"
+ "unregisterTLSSAInboundSPI:forLink:dataProtectionClass:"
+ "updatePeerDevice:"
+ "usesPSKForMASQUE"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
+ "v16@?0@\"NRBabelASQUICTransport\"8"
+ "v16@?0@\"NRBabelTLVAppleMeshLinkResponse\"8"
+ "v16@?0@\"NRMeshInfo\"8"
+ "v16@?0@\"NSObject<OS_nw_connection_group>\"8"
+ "v16@?0@\"NSObject<OS_sec_certificate>\"8"
+ "v24@0:8@\"NRBabelPacket\"16"
+ "v24@0:8@\"NRDeviceEndpoint\"16"
+ "v24@0:8@?<v@?>16"
+ "v28@0:8@\"NRLink\"16C24"
+ "v28@?0I8@\"NEIKEv2TLSSAInstallationRecord\"12@\"NEIKEv2TLSSAInstallationRecord\"20"
+ "v28@?0I8@\"NEIKEv2TLSSPI\"12@\"NEIKEv2TLSSPI\"20"
+ "v32@0:8@\"NRBabelASQUICTransport\"16@\"NRBabelInterface\"24"
+ "v32@0:8@\"NRBabelPacket\"16@\"NRDeviceEndpoint\"24"
+ "v36@0:8@\"NEIKEv2TLSSPI\"16@\"NRLink\"24C32"
+ "v36@0:8@16@24C32"
+ "v36@?0@\"NSObject<OS_nw_framer>\"8@\"NSObject<OS_nw_protocol_metadata>\"16Q24B32"
+ "value"
- "\nCompanion APL allowed: %s"
- "\nMASQUE port: %u"
- "\nMASQUE server: %@"
- "%s%.30s:%-4d %@: Both sides support APL"
- "%s%.30s:%-4d %@: Both sides use APL"
- "%s%.30s:%-4d %@: Local doesn't support APL, but remote does"
- "%s%.30s:%-4d %@: Local doesn't use APL, but remote does"
- "%s%.30s:%-4d %@: Remote doesn't support APL, but local does"
- "%s%.30s:%-4d %@: Remote doesn't use APL, but local does"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (self.masqueServer) != ((void*)0)"
- "%s%.30s:%-4d Failed to create MASQUE server"
- "%s%.30s:%-4d Failed to start MASQUE server without local identity"
- "%s%.30s:%-4d MASQUE server cancelled"
- "%s%.30s:%-4d MASQUE server is already running"
- "%s%.30s:%-4d MASQUE server started %u"
- "%s%.30s:%-4d no QUIC options"
- "%s%.30s:%-4d proxy client connection cancelled (id: %llu)"
- "%s%.30s:%-4d proxy client connection received (id: %llu)"
- "%s%.30s:%-4d proxy client connection started (id: %llu)"
- "%s%.30s:%-4d start MASQUE server : %@"
- "%s%.30s:%-4d using cached tokensfrom %@ for %@ (id: %llu)"
- "%{public}s Assertion Failed: (self.masqueServer) != ((void*)0)"
- "-[NRLinkDirector cancelMASQUEProxyServer]"
- "-[NRLinkDirector setupAppVPNWatcher]_block_invoke"
- "-[NRLinkDirector startMASQUEProxyServerIfNeeded]_block_invoke"
- "-[NRLinkDirector startMASQUEProxyServerIfNeeded]_block_invoke_2"
- "-[NRLinkDirector startMASQUEProxyServerIfNeeded]_block_invoke_3"
- "914.42.1"
- "CompanionLinkMLKEM"
- "_masqueProxyTokenCache"
- "_masqueServer"
- "failed to copy connection group (id: %llu)"
- "setProtocol:"
- "\xf0!"
```
