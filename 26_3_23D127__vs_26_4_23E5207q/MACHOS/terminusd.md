## terminusd

> `/usr/libexec/terminusd`

```diff

-676.80.2.0.0
-  __TEXT.__text: 0x184b10
-  __TEXT.__auth_stubs: 0x2bd0
+676.100.19.0.0
+  __TEXT.__text: 0x18665c
+  __TEXT.__auth_stubs: 0x2bb0
   __TEXT.__objc_stubs: 0x84e0
-  __TEXT.__objc_methlist: 0x52b0
-  __TEXT.__const: 0x24c
-  __TEXT.__gcc_except_tab: 0x4314
-  __TEXT.__objc_methname: 0x114c7
-  __TEXT.__cstring: 0x41911
-  __TEXT.__oslogstring: 0x247e
+  __TEXT.__objc_methlist: 0x52b8
+  __TEXT.__const: 0x248
+  __TEXT.__gcc_except_tab: 0x4038
+  __TEXT.__objc_methname: 0x114f1
+  __TEXT.__cstring: 0x41651
+  __TEXT.__oslogstring: 0x2357
   __TEXT.__objc_classname: 0xe92
-  __TEXT.__objc_methtype: 0x386c
-  __TEXT.__unwind_info: 0x24c0
-  __DATA_CONST.__auth_got: 0x15f8
-  __DATA_CONST.__got: 0xa08
+  __TEXT.__objc_methtype: 0x3896
+  __TEXT.__unwind_info: 0x2778
+  __DATA_CONST.__auth_got: 0x15e8
+  __DATA_CONST.__got: 0x9f8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x3418
-  __DATA_CONST.__cfstring: 0xbd60
+  __DATA_CONST.__cfstring: 0xbdc0
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__objc_intobj: 0x5e8
+  __DATA_CONST.__objc_intobj: 0x600
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x15080
-  __DATA.__objc_selrefs: 0x2cd0
+  __DATA.__objc_const: 0x15088
+  __DATA.__objc_selrefs: 0x2cd8
   __DATA.__objc_ivar: 0x1a54
   __DATA.__objc_data: 0x29e0
   __DATA.__data: 0xce8

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33CB4AF2-3C36-3A80-BEE7-216A95101538
-  Functions: 3098
-  Symbols:   1037
-  CStrings:  11562
+  UUID: BF05FAD7-61AC-3191-BC80-32E510929617
+  Functions: 3100
+  Symbols:   1033
+  CStrings:  11548
 
Symbols:
+ _NRCreateLocalIdentityUsingKeys
+ _NRCreateSigningKeyPair
+ _nw_parameters_create_application_service_quic_using_identity
+ _objc_retain_x11
- _SecKeyCopyPublicKey
- _kSecAttrKeySizeInBits
- _kSecAttrKeyTypeECSECPrimeRandom
- _nw_parameters_create_application_service_quic
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%s%.30s:%-4d Listen request %@ for asName %@ not allowed"
+ "%s%.30s:%-4d No devices to scrub"
+ "%s%.30s:%-4d No devices to unregister"
+ "%s%.30s:%-4d Saving %llu local device ClassD configs (changed %s force %s)"
+ "-[NRApplicationServiceManager isListenRequestAllowedForASName:]"
+ "-[NRApplicationServiceManager removeDropPoliciesForDeviceID:]"
+ "-[NRLinkDirector startHTTPConnectProxyServerIfNeeded]_block_invoke_2"
+ "02:19:29"
+ "676.100.19"
+ "Failed to create keypair for local identity"
+ "Jan 28 2026"
+ "local-asquic"
+ "message-tlv-type"
+ "publisher:getKeysBlobForMulticastSession:"
+ "v32@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24"
- "%s called with null block"
- "%s called with null classAUnlockedBlock"
- "%s called with null localDeviceClassCUnlockedBlock"
- "%s called with null messageData"
- "%s called with null resolverProtocolPtr"
- "%s called with null resultPtr"
- "%s called with null serverCertificateDataPtr"
- "%s called with null serverEndpointPtr"
- "%s called with null shouldStartPtr"
- "%s called with null udpInputSourcePtr"
- "%s called with null wifiManagerAvailableBlock"
- "%s%.30s:%-4d %saving %llu local device ClassD configs"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (addrBytes) != ((void*)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (completionBlock) != ((void*)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: (outSockAddrBytes) != ((void*)0)"
- "%s%.30s:%-4d ABORTING: Assertion Failed: lrbIOVecLen > 0; tlvLen=%u filledInLinkReadBufferBytes=%u handledLinkReadBufferBytes=%u"
- "%{public}s Assertion Failed: (addrBytes) != ((void*)0)"
- "%{public}s Assertion Failed: (completionBlock) != ((void*)0)"
- "%{public}s Assertion Failed: (outSockAddrBytes) != ((void*)0)"
- "%{public}s Assertion Failed: lrbIOVecLen > 0; tlvLen=%u filledInLinkReadBufferBytes=%u handledLinkReadBufferBytes=%u"
- "-[NRDLocalDevice fillInClassAKeysWithCompletion:]"
- "-[NRDLocalDevice fillInClassCKeysWithCompletion:]"
- "-[NRDLocalDevice writeLocalClassCInnerAddressBytes:]"
- "-[NRDLocalDevice writeRemoteClassCInnerAddressBytes:]"
- "-[NRLinkDirector startHTTPConnectProxyServerIfNeeded]_block_invoke_3"
- "12:04:58"
- "676.80.2"
- "Force s"
- "Jan 17 2026"
- "NRDTSCreateUDPListeningSocket"
- "unexpected buffer size requirement %u bytes"

```
