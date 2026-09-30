## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS`

```diff

-2003.100.1.0.0
-  __TEXT.__text: 0x1bb8a4
-  __TEXT.__objc_methlist: 0xdbcc
-  __TEXT.__const: 0x5fd8
-  __TEXT.__oslogstring: 0x1b584
-  __TEXT.__cstring: 0x10b06
+2003.200.33.1.5
+  __TEXT.__text: 0x1c3150
+  __TEXT.__objc_methlist: 0xdbd4
+  __TEXT.__const: 0x60f8
+  __TEXT.__cstring: 0x10b36
+  __TEXT.__oslogstring: 0x1bc18
   __TEXT.__gcc_except_tab: 0x3e04
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
-  __TEXT.__unwind_info: 0x8e88
-  __TEXT.__eh_frame: 0x3180
+  __TEXT.__unwind_info: 0x8f78
+  __TEXT.__eh_frame: 0x33d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd08
+  __DATA_CONST.__const: 0xd18
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ce8
+  __DATA_CONST.__objc_selrefs: 0x6cf0
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x478
-  __DATA_CONST.__got: 0x1ab0
-  __AUTH_CONST.__const: 0xa280
-  __AUTH_CONST.__cfstring: 0x7580
+  __DATA_CONST.__got: 0x1ab8
+  __AUTH_CONST.__const: 0xa2e8
+  __AUTH_CONST.__cfstring: 0x75e0
   __AUTH_CONST.__objc_const: 0x3d690
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x588
-  __AUTH_CONST.__auth_got: 0x1cb8
+  __AUTH_CONST.__auth_got: 0x1cc0
   __AUTH.__objc_data: 0x2118
-  __AUTH.__data: 0x1468
+  __AUTH.__data: 0x1580
   __DATA.__objc_ivar: 0xdf0
-  __DATA.__data: 0x2870
+  __DATA.__data: 0x28b8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1bd0
   __DATA_DIRTY.__bss: 0x3ca

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9479
-  Symbols:   1785
-  CStrings:  3807
+  Functions: 9528
+  Symbols:   1788
+  CStrings:  3821
 
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
