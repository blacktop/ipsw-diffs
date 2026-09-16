## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-2003.100.1.2.1
-  __TEXT.__text: 0x1ab9b0
-  __TEXT.__objc_methlist: 0xdc3c
-  __TEXT.__const: 0x5fe8
-  __TEXT.__oslogstring: 0x1b774
-  __TEXT.__cstring: 0x11b26
+2003.200.33.2.5
+  __TEXT.__text: 0x1b31e8
+  __TEXT.__objc_methlist: 0xdc44
+  __TEXT.__const: 0x6108
+  __TEXT.__cstring: 0x11b56
+  __TEXT.__oslogstring: 0x1bdf8
   __TEXT.__gcc_except_tab: 0x3de0
   __TEXT.__ustring: 0xac
   __TEXT.__dlopen_cstrs: 0x102
-  __TEXT.__swift5_typeref: 0x1c5c
-  __TEXT.__swift5_capture: 0x19c
+  __TEXT.__swift5_typeref: 0x1d00
+  __TEXT.__swift5_capture: 0x188
   __TEXT.__swift_as_entry: 0x114
   __TEXT.__swift_as_ret: 0x134
   __TEXT.__swift_as_cont: 0x280
-  __TEXT.__constg_swiftt: 0x1658
-  __TEXT.__swift5_reflstr: 0xe3c
-  __TEXT.__swift5_fieldmd: 0x17d4
-  __TEXT.__swift5_proto: 0x3bc
-  __TEXT.__swift5_types: 0x250
+  __TEXT.__constg_swiftt: 0x16d4
+  __TEXT.__swift5_reflstr: 0xec3
+  __TEXT.__swift5_fieldmd: 0x1894
+  __TEXT.__swift5_proto: 0x3c4
+  __TEXT.__swift5_types: 0x25c
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x8ea0
-  __TEXT.__eh_frame: 0x3180
+  __TEXT.__unwind_info: 0x8f90
+  __TEXT.__eh_frame: 0x33d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5410
+  __DATA_CONST.__const: 0x5420
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d48
+  __DATA_CONST.__objc_selrefs: 0x6d50
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x480
-  __DATA_CONST.__got: 0x1ac8
-  __AUTH_CONST.__const: 0x5540
-  __AUTH_CONST.__cfstring: 0x76e0
+  __DATA_CONST.__got: 0x1ad0
+  __AUTH_CONST.__const: 0x55a8
+  __AUTH_CONST.__cfstring: 0x7740
   __AUTH_CONST.__objc_const: 0x3da18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x588
-  __AUTH_CONST.__auth_got: 0x1ec0
+  __AUTH_CONST.__auth_got: 0x1ec8
   __AUTH.__objc_data: 0x2168
-  __AUTH.__data: 0x1480
+  __AUTH.__data: 0x1598
   __DATA.__objc_ivar: 0xdf4
-  __DATA.__data: 0x2910
+  __DATA.__data: 0x2958
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__bss: 0x3c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9465
-  Symbols:   1874
-  CStrings:  3878
+  Functions: 9514
+  Symbols:   1877
+  CStrings:  3892
 
Symbols:
+ _IDSGroupAgentRemoteAppIntentsAppSvcName
+ _IDSGroupSessionClientSessionExperimentsKey
+ _IDSServiceNameRemoteAppIntents
CStrings:
+ " => Delegate %p responds to: %@, passing along protobuf: %p"
+ " => Delegate %p responds unhandled protobuf passing along protobuf: %p"
+ "-seed"
+ ".clientSessionExperiments(["
+ "<LinkContext %p> linkID %d (UUID:%@, QRSessionID:%@) networkType %u connectionType %s maxMTU %u estimatedConstantOverhead %u RATType %lu maxBitrate %u (remote networkType %u connectionType %s RATType %lu), relay(provider:%d, token:%dB) serverIsDegraded: %@ localLinkFlags 0x%x remoteLinkFlags 0x%x, localDataSoMask: %u, remoteDataSoMask: %u, virtualRelayLink: %@, delegatedLinkID %d, localInterfaceName: %@, relayProtocolStack: %@, isPartialTLEForUPlusOneEnabled: %@, quality metadata: %@, localLinkTechnology: %u, localLinkTransport: %u, connections: %@, featureFlags: %@, qrExperiments: %@"
+ "IDSGroupSession.cryptors: cryptor stream for topic=%s source=%s closed with error: %s"
+ "IDSGroupSession.cryptors: no cryptor backend available for topic=%s; returning an empty stream, session was likely invalidated"
+ "No local key material found. Skip completion handler update."
+ "RealTimeGroupSessionCryptorBackend.invalidate: dropped invalidation of %ld %s key(s), backend is shut down"
+ "RealTimeGroupSessionCryptorBackend.logHandovers: handed cryptor to subscriber=%llu, topic=%s, encryptionKeyID=%s, decryptionKeys=%ld"
+ "RealTimeGroupSessionCryptorBackend.logKeySetChange: %s %ld new %s key(s): %s; rotated=%{bool}d, totalKeys=%ld"
+ "RealTimeGroupSessionCryptorBackend.logKeySetChange: %s %s key(s) but no locally-generated key is available; cannot encrypt, so no cryptor is handed to subscribers"
+ "RealTimeGroupSessionCryptorBackend.logKeySetChange: %s %s key(s): removed=%ld, rotated=%{bool}d, encryptionKeyID=%s, totalKeys=%ld"
+ "RealTimeGroupSessionCryptorBackend.receive: dropped %ld %s key(s), backend is shut down"
+ "RealTimeGroupSessionCryptorBackend.subscribe: subscriber=%llu for topic=%s source=%s finished immediately, backend is shut down"
+ "RealTimeGroupSessionCryptorBackend.subscribe: subscriber=%llu registered for topic=%s source=%s; handed cryptor from cached material, encryptionKeyID=%s, decryptionKeys=%ld"
+ "RealTimeGroupSessionCryptorBackend.subscribe: subscriber=%llu registered for topic=%s source=%s; no locally-generated key yet, no cryptor handed over"
+ "XPC has informed us that a fatal error has occurred, we will not be attempting to reconnect any further"
+ "_IDSRealTimeGroupSessionCryptorBackend.logDropped: %ld of %ld %s key material dict(s) failed to parse and were dropped before reaching the cryptor"
+ "_IDSRealTimeGroupSessionCryptorBackend.shutdown: shutting down cryptor backend, all subscriber streams will finish"
+ "com.apple.private.alloy.remoteappintents"
+ "remoteappintents"
- " => Delgate %p responds to: %@, passing along protobuf: %p"
- " => Delgate %p responds unhandled protobuf passing along protobuf: %p"
- "%s: no cryptor backend available; returning an empty stream (session likely invalidated)"
- "<LinkContext %p> linkID %d (UUID:%@, QRSessionID:%@) networkType %u connectionType %s maxMTU %u estimatedConstantOverhead %u RATType %lu maxBitrate %u (remote networkType %u connectionType %s RATType %lu), relay(provider:%d, token:%dB) serverIsDegraded: %@ localLinkFlags 0x%x remoteLinkFlags 0x%x, localDataSoMask: %u, remoteDataSoMask: %u, virtualRelayLink: %@, delegatedLinkID %d, localInterfaceName: %@, relayProtocolStack: %@, isPartialTLEForUPlusOneEnabled: %@, quality metadata: %@, connections: %@, featureFlags: %@, qrExperiments: %@"
- "No local key material found. Skip completion handler udpate."
- "RealTimeGroupSessionCryptor"
- "XPC has informed us that a fatal error has occured, we will not be attempting to reconnect any further"
- "cryptors(forTopic:keyMaterialSource:strategy:_:)"
```
