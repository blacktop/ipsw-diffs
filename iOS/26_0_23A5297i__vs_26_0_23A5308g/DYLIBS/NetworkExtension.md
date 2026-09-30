## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2191.0.0.0.0
-  __TEXT.__text: 0x1f802c
-  __TEXT.__auth_stubs: 0x43b0
-  __TEXT.__objc_methlist: 0xf1c8
-  __TEXT.__const: 0x3200
-  __TEXT.__cstring: 0x1956f
+2204.0.0.0.1
+  __TEXT.__text: 0x1fa210
+  __TEXT.__auth_stubs: 0x43e0
+  __TEXT.__objc_methlist: 0xee50
+  __TEXT.__const: 0x3178
+  __TEXT.__cstring: 0x198c6
   __TEXT.__constg_swiftt: 0xc1c
   __TEXT.__swift5_typeref: 0xdd3
   __TEXT.__swift5_reflstr: 0x465

   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_capture: 0xd58
-  __TEXT.__oslogstring: 0x220a4
+  __TEXT.__oslogstring: 0x232df
   __TEXT.__swift_as_entry: 0xe4
   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__gcc_except_tab: 0x5954
-  __TEXT.__unwind_info: 0x5470
+  __TEXT.__gcc_except_tab: 0x59bc
+  __TEXT.__unwind_info: 0x5440
   __TEXT.__eh_frame: 0x2830
-  __TEXT.__objc_classname: 0x24a2
-  __TEXT.__objc_methname: 0x1a922
-  __TEXT.__objc_methtype: 0x39b4
-  __TEXT.__objc_stubs: 0x10060
-  __DATA_CONST.__got: 0x1748
-  __DATA_CONST.__const: 0x58a0
-  __DATA_CONST.__objc_classlist: 0xb20
+  __TEXT.__objc_classname: 0x24c0
+  __TEXT.__objc_methname: 0x1aa8f
+  __TEXT.__objc_methtype: 0x3a72
+  __TEXT.__objc_stubs: 0x10100
+  __DATA_CONST.__got: 0x1730
+  __DATA_CONST.__const: 0x5908
+  __DATA_CONST.__objc_classlist: 0xb28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5170
+  __DATA_CONST.__objc_selrefs: 0x5180
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x720
+  __DATA_CONST.__objc_superrefs: 0x708
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x21e8
-  __AUTH_CONST.__const: 0x3e88
-  __AUTH_CONST.__cfstring: 0x17ca0
-  __AUTH_CONST.__objc_const: 0x225f0
+  __AUTH_CONST.__auth_got: 0x2200
+  __AUTH_CONST.__const: 0x3ea8
+  __AUTH_CONST.__cfstring: 0x17e20
+  __AUTH_CONST.__objc_const: 0x228a8
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1528
+  __AUTH.__objc_data: 0x1578
   __AUTH.__data: 0xd98
-  __DATA.__objc_ivar: 0x1b38
-  __DATA.__data: 0x1f88
-  __DATA.__bss: 0x1490
+  __DATA.__objc_ivar: 0x1b68
+  __DATA.__data: 0x1f98
+  __DATA.__bss: 0x1488
   __DATA.__common: 0x190
   __DATA_DIRTY.__objc_data: 0x5ff0
   __DATA_DIRTY.__bss: 0xf0

   - /System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0A223F96-CDC5-3C64-9005-A3941FF7C529
-  Functions: 7883
-  Symbols:   22807
-  CStrings:  15673
+  UUID: 568C234B-B355-33F2-A9B4-9667C0D21D19
+  Functions: 7877
+  Symbols:   22775
+  CStrings:  15803
 
Symbols:
+ +[NEIKEv2AuthenticationProtocol getAlgorithmForRSAPSSParameters:]
+ +[NEIKEv2Crypto appendRandomBytesToData:withSize:]
+ +[NEIKEv2Crypto copyHashForDataVector:hashType:]
+ +[NEIKEv2Crypto validateSignature:hashedData:signatureAlgorithm:publicKey:]
+ +[NEIKEv2Crypto validateSignature:signedDataVector:authProtocol:publicKey:]
+ +[NEIKEv2Session removeItemsFromSet:lowerEdge:]
+ -[NEIKEv2ASN1DNIdentifier typeDescription]
+ -[NEIKEv2AddressAttribute typeDescription]
+ -[NEIKEv2AddressIdentifier typeDescription]
+ -[NEIKEv2AppVersionAttribute typeDescription]
+ -[NEIKEv2AuthPayload copyFullAuthenticationData]
+ -[NEIKEv2AuthPayload parsePayloadData:]
+ -[NEIKEv2AuthPayload typeDescription]
+ -[NEIKEv2AuthenticationProtocol copyHashForDataVector:]
+ -[NEIKEv2AuthenticationProtocol hashType]
+ -[NEIKEv2AuthenticationProtocol signatureAlgorithm]
+ -[NEIKEv2CertificatePayload parsePayloadData:]
+ -[NEIKEv2CertificatePayload typeDescription]
+ -[NEIKEv2CertificateRequestPayload parsePayloadData:]
+ -[NEIKEv2CertificateRequestPayload typeDescription]
+ -[NEIKEv2ChildSAPayload parsePayloadData:]
+ -[NEIKEv2ChildSAPayload typeDescription]
+ -[NEIKEv2ConfigPayload createConfigAttributeFromData:attributeName:attributeType:customType:]
+ -[NEIKEv2ConfigPayload parsePayloadData:]
+ -[NEIKEv2ConfigPayload typeDescription]
+ -[NEIKEv2ConfigurationAttribute typeDescription]
+ -[NEIKEv2CreateChildPacket exchangeType]
+ -[NEIKEv2CreateChildPacket typeDescription]
+ -[NEIKEv2CustomPayload parsePayloadData:]
+ -[NEIKEv2CustomPayload typeDescription]
+ -[NEIKEv2DNSDomainAttribute typeDescription]
+ -[NEIKEv2DeleteChildContext requestType]
+ -[NEIKEv2DeleteIKEContext requestType]
+ -[NEIKEv2DeletePayload parsePayloadData:]
+ -[NEIKEv2DeletePayload typeDescription]
+ -[NEIKEv2EAPPayload parsePayloadData:]
+ -[NEIKEv2EAPPayload typeDescription]
+ -[NEIKEv2EncryptedFragmentPayload isFragment]
+ -[NEIKEv2EncryptedFragmentPayload parsePayloadData:]
+ -[NEIKEv2EncryptedFragmentPayload typeDescription]
+ -[NEIKEv2EncryptedKeyIDIdentifier typeDescription]
+ -[NEIKEv2EncryptedPayload isFragment]
+ -[NEIKEv2EncryptedPayload parsePayloadData:]
+ -[NEIKEv2EncryptedPayload typeDescription]
+ -[NEIKEv2EncryptionProtocol initWithEncryptionWireType:keyLength:]
+ -[NEIKEv2EncryptionProtocol keyMaterialLength]
+ -[NEIKEv2FQDNIdentifier typeDescription]
+ -[NEIKEv2FollowupKEPacket exchangeType]
+ -[NEIKEv2FollowupKEPacket typeDescription]
+ -[NEIKEv2FragmentMap hasFragmentForNumber:]
+ -[NEIKEv2GSPMPayload parsePayloadData:]
+ -[NEIKEv2GSPMPayload typeDescription]
+ -[NEIKEv2IKEAuthPacket exchangeType]
+ -[NEIKEv2IKEAuthPacket typeDescription]
+ -[NEIKEv2IKEAuthPacket validateAuthInitialAsInitiator:beforeEAP:]
+ -[NEIKEv2IKESA copyDeviceIdentityNotifyPayload]
+ -[NEIKEv2IKESA setResponderIdentifierPayload:]
+ -[NEIKEv2IKESAInitPacket encryptPayloads]
+ -[NEIKEv2IKESAInitPacket exchangeType]
+ -[NEIKEv2IKESAInitPacket typeDescription]
+ -[NEIKEv2IKESAPayload parsePayloadData:]
+ -[NEIKEv2IKESAPayload typeDescription]
+ -[NEIKEv2IKESAProposal hash]
+ -[NEIKEv2IKESAProposal isEqual:]
+ -[NEIKEv2IPv4AddressAttribute typeDescription]
+ -[NEIKEv2IPv4DHCPAttribute typeDescription]
+ -[NEIKEv2IPv4DNSAttribute typeDescription]
+ -[NEIKEv2IPv4NetmaskAttribute typeDescription]
+ -[NEIKEv2IPv4PCSCFAttribute typeDescription]
+ -[NEIKEv2IPv4SubnetAttribute typeDescription]
+ -[NEIKEv2IPv6AddressAttribute typeDescription]
+ -[NEIKEv2IPv6DHCPAttribute typeDescription]
+ -[NEIKEv2IPv6DNSAttribute typeDescription]
+ -[NEIKEv2IPv6PCSCFAttribute typeDescription]
+ -[NEIKEv2IPv6SubnetAttribute initEmptyRequest]
+ -[NEIKEv2IPv6SubnetAttribute typeDescription]
+ -[NEIKEv2Identifier initWithIdentifierData:]
+ -[NEIKEv2Identifier typeDescription]
+ -[NEIKEv2IdentifierPayload copyPayloadData]
+ -[NEIKEv2IdentifierPayload parsePayloadData:]
+ -[NEIKEv2IdentifierPayload setPayloadData:]
+ -[NEIKEv2IdentifierPayload typeDescription]
+ -[NEIKEv2InformationalContext requestType]
+ -[NEIKEv2InformationalPacket exchangeType]
+ -[NEIKEv2InformationalPacket typeDescription]
+ -[NEIKEv2InitiatorIdentifierPayload typeDescription]
+ -[NEIKEv2InitiatorTrafficSelectorPayload typeDescription]
+ -[NEIKEv2InitiatorTransportIPv6Address typeDescription]
+ -[NEIKEv2IntermediatePacket constructAuthenticatedDataWithPayloads:payloadsLength:authenticatedHeaders:]
+ -[NEIKEv2IntermediatePacket exchangeType]
+ -[NEIKEv2IntermediatePacket typeDescription]
+ -[NEIKEv2KeyExchangePayload parsePayloadData:]
+ -[NEIKEv2KeyExchangePayload typeDescription]
+ -[NEIKEv2KeyIDIdentifier typeDescription]
+ -[NEIKEv2MOBIKEContext requestType]
+ -[NEIKEv2NULLIdentifier typeDescription]
+ -[NEIKEv2NewChildContext requestType]
+ -[NEIKEv2NoncePayload parsePayloadData:]
+ -[NEIKEv2NoncePayload typeDescription]
+ -[NEIKEv2NotifyPayload copyNotifyTypeDescription]
+ -[NEIKEv2NotifyPayload parsePayloadData:]
+ -[NEIKEv2NotifyPayload typeDescription]
+ -[NEIKEv2Packet decryptReceivedPacketWithIKESA:]
+ -[NEIKEv2Packet encryptPayloads]
+ -[NEIKEv2Packet exchangeType]
+ -[NEIKEv2Packet initInbound]
+ -[NEIKEv2Packet parsePacketData:firstPayloadType:ikeSA:]
+ -[NEIKEv2Packet setRawPayloads:]
+ -[NEIKEv2Packet typeDescription]
+ -[NEIKEv2PacketConstructor .cxx_destruct]
+ -[NEIKEv2PacketConstructor appendPayloadsToPacket:withLength:]
+ -[NEIKEv2Payload description]
+ -[NEIKEv2Payload parsePayloadData:]
+ -[NEIKEv2Payload setPayloadDataVector:]
+ -[NEIKEv2Payload setPayloadSubHeader:]
+ -[NEIKEv2Payload typeDescription]
+ -[NEIKEv2RekeyChildContext requestType]
+ -[NEIKEv2RekeyIKEContext requestType]
+ -[NEIKEv2RequestContext requestType]
+ -[NEIKEv2ResponderIdentifierPayload typeDescription]
+ -[NEIKEv2ResponderTrafficSelectorPayload typeDescription]
+ -[NEIKEv2ResponderTransportIPv6Address typeDescription]
+ -[NEIKEv2ResponseConfigPayload parsePayloadData:]
+ -[NEIKEv2SecurityContext constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]
+ -[NEIKEv2SecurityContextAESGCM constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]
+ -[NEIKEv2SecurityContextAESGCM dealloc]
+ -[NEIKEv2SecurityContextCBCPlusHMAC constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]
+ -[NEIKEv2SecurityContextChaCha20Poly1305 constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]
+ -[NEIKEv2SecurityContextChaCha20Poly1305 dealloc]
+ -[NEIKEv2Session packetsToSave]
+ -[NEIKEv2Session updateReceivedRequestWindow]
+ -[NEIKEv2Session updateSentRequestWindow]
+ -[NEIKEv2StringAttribute typeDescription]
+ -[NEIKEv2SubnetAttribute typeDescription]
+ -[NEIKEv2SupportedAttribute typeDescription]
+ -[NEIKEv2TrafficSelectorPayload parsePayloadData:]
+ -[NEIKEv2TrafficSelectorPayload typeDescription]
+ -[NEIKEv2UserFQDNIdentifier typeDescription]
+ -[NEIKEv2VendorIDPayload parsePayloadData:]
+ -[NEIKEv2VendorIDPayload typeDescription]
+ -[NEPvDFetcher findProxy:proxyToFind:]
+ -[NEPvDFetcher formatExpirationDateFrom:]
+ -[NEPvDFetcher isActive]
+ -[NEPvDFetcher setQueue:]
+ GCC_except_table2819
+ GCC_except_table2829
+ GCC_except_table3062
+ GCC_except_table3067
+ GCC_except_table3073
+ GCC_except_table3076
+ GCC_except_table3091
+ GCC_except_table3092
+ GCC_except_table3093
+ GCC_except_table3108
+ GCC_except_table3122
+ GCC_except_table3123
+ GCC_except_table3165
+ GCC_except_table3169
+ GCC_except_table3215
+ GCC_except_table3266
+ GCC_except_table3327
+ GCC_except_table3346
+ GCC_except_table3355
+ GCC_except_table3376
+ GCC_except_table3377
+ GCC_except_table3389
+ GCC_except_table3396
+ GCC_except_table3435
+ GCC_except_table3441
+ GCC_except_table3478
+ GCC_except_table3481
+ GCC_except_table4604
+ GCC_except_table4606
+ GCC_except_table4641
+ GCC_except_table4651
+ GCC_except_table4655
+ GCC_except_table4667
+ GCC_except_table4687
+ GCC_except_table4689
+ GCC_except_table4695
+ GCC_except_table4697
+ GCC_except_table4789
+ GCC_except_table4858
+ GCC_except_table4879
+ GCC_except_table4892
+ GCC_except_table4989
+ GCC_except_table4994
+ GCC_except_table5035
+ GCC_except_table5081
+ GCC_except_table5083
+ GCC_except_table5147
+ GCC_except_table5150
+ GCC_except_table5186
+ GCC_except_table5206
+ GCC_except_table5208
+ GCC_except_table5210
+ GCC_except_table5218
+ GCC_except_table5257
+ GCC_except_table5258
+ GCC_except_table5260
+ GCC_except_table5262
+ GCC_except_table5265
+ GCC_except_table5309
+ GCC_except_table5331
+ GCC_except_table5334
+ GCC_except_table5410
+ GCC_except_table5739
+ GCC_except_table5775
+ GCC_except_table5776
+ GCC_except_table5833
+ GCC_except_table5839
+ GCC_except_table5840
+ GCC_except_table5848
+ GCC_except_table5851
+ GCC_except_table5861
+ GCC_except_table5876
+ GCC_except_table5877
+ GCC_except_table5878
+ GCC_except_table5879
+ GCC_except_table5888
+ GCC_except_table5895
+ GCC_except_table5904
+ GCC_except_table5907
+ GCC_except_table5988
+ GCC_except_table5989
+ GCC_except_table6118
+ GCC_except_table6119
+ GCC_except_table6120
+ GCC_except_table6121
+ GCC_except_table6122
+ GCC_except_table6147
+ GCC_except_table6153
+ GCC_except_table6154
+ GCC_except_table6185
+ GCC_except_table6262
+ GCC_except_table6263
+ GCC_except_table6264
+ GCC_except_table6265
+ _CCDigestFinal
+ _CCDigestInit
+ _CCDigestUpdate
+ _CFDataIncreaseLength
+ _CFDictionaryApplyFunction
+ _CFURLCopyFileSystemPath
+ _FIVE_MIN_IN_SECONDS
+ _MGCopyAnswer
+ _NEIPSecDBFlushPoliciesHelper
+ _NEIPSecDBFlushSAHelper
+ _NEPFKeyAddSADBAddr
+ _NEPFKeyAddSADBIPSecIF
+ _NEPFKeyAddSADBKey
+ _NEResourcesCopyNetworkPrivacyiOSIconURL
+ _OBJC_CLASS_$_NEIKEv2PacketConstructor
+ _OBJC_IVAR_$_NEIKEv2AddressIdentifier._identifierType
+ _OBJC_IVAR_$_NEIKEv2EncryptedPayload._payloadData
+ _OBJC_IVAR_$_NEIKEv2EncryptionProtocol._keyLength
+ _OBJC_IVAR_$_NEIKEv2FragmentMap._aggregatedPayloadsLength
+ _OBJC_IVAR_$_NEIKEv2FragmentMap._currentCount
+ _OBJC_IVAR_$_NEIKEv2FragmentMap._firstFragment
+ _OBJC_IVAR_$_NEIKEv2IKESA._fallbackLocalIdentifier
+ _OBJC_IVAR_$_NEIKEv2IKESA._responderIdentifierPayload
+ _OBJC_IVAR_$_NEIKEv2IKESAInitPacket._originalPacket
+ _OBJC_IVAR_$_NEIKEv2IdentifierPayload._payloadData
+ _OBJC_IVAR_$_NEIKEv2Packet._originalPacketLength
+ _OBJC_IVAR_$_NEIKEv2PacketConstructor._index
+ _OBJC_IVAR_$_NEIKEv2PacketConstructor._offset
+ _OBJC_IVAR_$_NEIKEv2PacketConstructor._payloadVector
+ _OBJC_IVAR_$_NEIKEv2Payload._payloadDataVector
+ _OBJC_IVAR_$_NEIKEv2Payload._payloadSubHeader
+ _OBJC_IVAR_$_NEIKEv2SecurityContextAESGCM._incomingEncryptionContext
+ _OBJC_IVAR_$_NEIKEv2SecurityContextAESGCM._outgoingEncryptionContext
+ _OBJC_IVAR_$_NEIKEv2SecurityContextAESGCM.incomingEncryptionSalt
+ _OBJC_IVAR_$_NEIKEv2SecurityContextCBCPlusHMAC.incomingHMACBaseContext
+ _OBJC_IVAR_$_NEIKEv2SecurityContextCBCPlusHMAC.outgoingHMACBaseContext
+ _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305.incomingEncryptionContext
+ _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305.incomingEncryptionSalt
+ _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305.outgoingEncryptionContext
+ _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305.outgoingEncryptionSalt
+ _OBJC_IVAR_$_NEIKEv2Session._lastSentRequest
+ _OBJC_IVAR_$_NEIKEv2Session._receivedReplyIDs
+ _OBJC_IVAR_$_NEIKEv2Session._receivedRequestIDs
+ _OBJC_IVAR_$_NEPvDFetcher._fetchTimer
+ _OBJC_METACLASS_$_NEIKEv2PacketConstructor
+ _ONE_DAY_IN_SECONDS
+ _SecPolicyCreateIPSec
+ __OBJC_$_INSTANCE_METHODS_NEIKEv2PacketConstructor
+ __OBJC_$_INSTANCE_VARIABLES_NEIKEv2PacketConstructor
+ __OBJC_$_PROP_LIST_NEIKEv2EncryptedPayload
+ __OBJC_$_PROP_LIST_NEIKEv2Packet
+ __OBJC_$_PROP_LIST_NEIKEv2RequestContext
+ __OBJC_CLASS_RO_$_NEIKEv2PacketConstructor
+ __OBJC_METACLASS_RO_$_NEIKEv2PacketConstructor
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.477
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.481
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.485
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.489
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.493
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.497
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.501
+ ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.505
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.512
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.516
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.520
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.524
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.528
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.532
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.539
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.543
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.547
+ ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.554
+ ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.80
+ ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.85
+ ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.89
+ ___181-[NEIKEv2Session initWithIKEConfig:firstChildConfig:sessionConfig:queue:ipsecInterface:ikeSocketHandler:saSession:shouldOwnSASession:packetDelegate:transport:configurationDelegate:]_block_invoke.45
+ ___25-[NEIKEv2Session connect]_block_invoke.51
+ ___28-[NEIKEv2Session disconnect]_block_invoke.53
+ ___31-[NEIKEv2Session startDPDTimer]_block_invoke.69
+ ___37-[NEIKEv2Session sendCurrentRequest:]_block_invoke.79
+ ___39-[NEIKEv2Session startIKELifetimeTimer]_block_invoke.70
+ ___46+[NEIKEv2Packet createPacketFromReceivedData:]_block_invoke
+ ___46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.292
+ ___46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.299
+ ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.614
+ ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.615
+ ___47+[NEIKEv2Session removeItemsFromSet:lowerEdge:]_block_invoke
+ ___47-[NEIKEv2Session(Exchange) initiateNewChildSA:]_block_invoke.338
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.561
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.565
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.569
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.573
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.577
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.582
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.581
+ ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.586
+ ___48-[NEIKEv2Session(Exchange) initiateMOBIKEInner:]_block_invoke.643
+ ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.442
+ ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.443
+ ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.444
+ ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke_2.447
+ ___53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.354
+ ___53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.355
+ ___54+[NEIKEv2Session removeItemsFromDictionary:lowerEdge:]_block_invoke
+ ___55-[NEIKEv2Session(Exchange) receiveRekeyChildSA:packet:]_block_invoke.466
+ ___55-[NEPvDFetcher initWithDelegate:queue:url:identityRef:]_block_invoke
+ ___56-[NEIKEv2Packet parsePacketData:firstPayloadType:ikeSA:]_block_invoke
+ ___95+[NEUserNotification promptForLocalAuthenticationWithReason:completionQueue:completionHandler:]_block_invoke.47
+ ___95+[NEUserNotification promptForLocalAuthenticationWithReason:completionQueue:completionHandler:]_block_invoke.49
+ ___Block_byref_object_copy_.12500
+ ___Block_byref_object_copy_.14913
+ ___Block_byref_object_copy_.20452
+ ___Block_byref_object_copy_.21709
+ ___Block_byref_object_copy_.22757
+ ___Block_byref_object_copy_.23896
+ ___Block_byref_object_copy_.24604
+ ___Block_byref_object_copy_.27229
+ ___Block_byref_object_copy_.28398
+ ___Block_byref_object_copy_.9417
+ ___Block_byref_object_dispose_.12501
+ ___Block_byref_object_dispose_.14914
+ ___Block_byref_object_dispose_.20453
+ ___Block_byref_object_dispose_.21710
+ ___Block_byref_object_dispose_.22758
+ ___Block_byref_object_dispose_.23897
+ ___Block_byref_object_dispose_.24605
+ ___Block_byref_object_dispose_.27230
+ ___Block_byref_object_dispose_.28399
+ ___Block_byref_object_dispose_.9418
+ ___block_descriptor_36_e22_B24?0"NSNumber"8^B16l
+ ___block_descriptor_36_e25_B32?0"NSNumber"816^B24l
+ ___block_descriptor_40_e8_32s_e12_v24?0^v8Q16ls32l8
+ ___block_descriptor_40_e8_32w_e37_B16?0"NEIKEv2SessionConfiguration"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40r48w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8r40l8w48l8
+ ___block_descriptor_tmp.19500
+ ___block_descriptor_tmp.2
+ ___block_descriptor_tmp.23449
+ ___block_descriptor_tmp.25495
+ ___block_descriptor_tmp.26107
+ ___block_literal_global.10.15519
+ ___block_literal_global.10.9082
+ ___block_literal_global.10061
+ ___block_literal_global.12774
+ ___block_literal_global.13149
+ ___block_literal_global.14.22220
+ ___block_literal_global.14074
+ ___block_literal_global.14239
+ ___block_literal_global.14915
+ ___block_literal_global.15.25725
+ ___block_literal_global.15521
+ ___block_literal_global.16090
+ ___block_literal_global.16333
+ ___block_literal_global.16818
+ ___block_literal_global.17.14087
+ ___block_literal_global.17.17785
+ ___block_literal_global.17660
+ ___block_literal_global.17794
+ ___block_literal_global.18107
+ ___block_literal_global.19409
+ ___block_literal_global.20.17791
+ ___block_literal_global.20266
+ ___block_literal_global.20760
+ ___block_literal_global.21806
+ ___block_literal_global.22225
+ ___block_literal_global.22621
+ ___block_literal_global.23363
+ ___block_literal_global.23447
+ ___block_literal_global.23999
+ ___block_literal_global.24112
+ ___block_literal_global.24146
+ ___block_literal_global.24340
+ ___block_literal_global.24522
+ ___block_literal_global.25442
+ ___block_literal_global.25493
+ ___block_literal_global.25729
+ ___block_literal_global.25833
+ ___block_literal_global.26213
+ ___block_literal_global.26768
+ ___block_literal_global.26957
+ ___block_literal_global.27195
+ ___block_literal_global.27757
+ ___block_literal_global.28.27233
+ ___block_literal_global.28417
+ ___block_literal_global.34
+ ___block_literal_global.4.14077
+ ___block_literal_global.63.20261
+ ___block_literal_global.7.25432
+ ___block_literal_global.73.25828
+ ___block_literal_global.9080
+ ___getDisplayScale_block_invoke
+ __extensionAuxiliaryHostProtocol.protocol.20262
+ __extensionAuxiliaryHostProtocol.protocol.24147
+ __extensionAuxiliaryHostProtocol.protocol.25829
+ __extensionAuxiliaryHostProtocol.protocolInit.20260
+ __extensionAuxiliaryHostProtocol.protocolInit.24145
+ __extensionAuxiliaryHostProtocol.protocolInit.25827
+ __extensionAuxiliaryVendorProtocol.protocol.20267
+ __extensionAuxiliaryVendorProtocol.protocol.25834
+ __extensionAuxiliaryVendorProtocol.protocolInit.20265
+ __extensionAuxiliaryVendorProtocol.protocolInit.25832
+ _convert_error_to_string.24596
+ _driverInterface.driverInterface.10058
+ _driverInterface.driverInterface.16819
+ _driverInterface.driverInterface.20757
+ _driverInterface.driverInterface.22221
+ _driverInterface.onceToken.10057
+ _driverInterface.onceToken.16817
+ _driverInterface.onceToken.20756
+ _driverInterface.onceToken.22219
+ _fcntl
+ _g_noAppFilter.28372
+ _globalConfigurationManager.gChangeQueue.17789
+ _globalConfigurationManager.gConfigurationManager.17786
+ _globalConfigurationManager.onceToken.17784
+ _initGlobals.onceToken.16332
+ _kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA256
+ _kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA384
+ _kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA512
+ _kSecKeyAlgorithmECDSASignatureDigestX962SHA256
+ _kSecKeyAlgorithmECDSASignatureDigestX962SHA384
+ _kSecKeyAlgorithmECDSASignatureDigestX962SHA512
+ _kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA1
+ _kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA256
+ _kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA384
+ _kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA512
+ _kSecKeyAlgorithmRSASignatureDigestPSSSHA256
+ _kSecKeyAlgorithmRSASignatureDigestPSSSHA384
+ _kSecKeyAlgorithmRSASignatureDigestPSSSHA512
+ _loadedManagers.loadedManagers.27193
+ _loadedManagers.loadedManagers.28375
+ _loadedManagers.managers_init.27192
+ _loadedManagers.managers_init.28374
+ _managerInterface.managerInterface.10062
+ _managerInterface.managerInterface.20761
+ _managerInterface.managerInterface.22226
+ _managerInterface.onceToken.10060
+ _managerInterface.onceToken.20759
+ _managerInterface.onceToken.22224
+ _objc_msgSend$constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:
+ _objc_msgSend$floatValue
+ _objc_msgSend$increaseLengthBy:
+ _objc_msgSend$ipv4SubnetMask
+ _objc_msgSend$isFragment
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$nextObject
+ _objc_msgSend$null
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$objectsPassingTest:
+ _objc_msgSend$parsePayloadData:
+ _objc_msgSend$receivePacketData:
+ _objc_msgSend$requestType
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$typeDescription
+ _objc_msgSend$valueForKey:
+ _registerOnce
+ _sMaxDisplayScale
+ _separateDomainsFromFQDNs
+ _sharedManager.onceToken.17793
+ _sharedManager.onceToken.28416
- +[NEIKEv2ASN1DNIdentifier copyTypeDescription]
- +[NEIKEv2AddressAttribute copyTypeDescription]
- +[NEIKEv2AddressIdentifier copyTypeDescription]
- +[NEIKEv2AppVersionAttribute copyTypeDescription]
- +[NEIKEv2AuthPayload copyTypeDescription]
- +[NEIKEv2CertificatePayload copyTypeDescription]
- +[NEIKEv2CertificateRequestPayload copyTypeDescription]
- +[NEIKEv2ChildSAPayload copyTypeDescription]
- +[NEIKEv2ConfigPayload copyTypeDescription]
- +[NEIKEv2ConfigurationAttribute copyTypeDescription]
- +[NEIKEv2CreateChildPacket copyTypeDescription]
- +[NEIKEv2CreateChildPacket exchangeType]
- +[NEIKEv2Crypto copyAuthenticationProtocolForAuthMethod:authData:]
- +[NEIKEv2Crypto signatureAlgorithmTypeForAuthentication:]
- +[NEIKEv2Crypto validateSignature:signedData:authProtocol:publicKey:]
- +[NEIKEv2Crypto validateSignature:signedData:signatureAlgorithm:publicKey:]
- +[NEIKEv2CustomPayload copyTypeDescription]
- +[NEIKEv2DNSDomainAttribute copyTypeDescription]
- +[NEIKEv2DeletePayload copyTypeDescription]
- +[NEIKEv2EAPPayload copyTypeDescription]
- +[NEIKEv2EncryptedFragmentPayload copyTypeDescription]
- +[NEIKEv2EncryptedKeyIDIdentifier copyTypeDescription]
- +[NEIKEv2EncryptedPayload copyTypeDescription]
- +[NEIKEv2FQDNIdentifier copyTypeDescription]
- +[NEIKEv2FollowupKEPacket copyTypeDescription]
- +[NEIKEv2FollowupKEPacket exchangeType]
- +[NEIKEv2GSPMPayload copyTypeDescription]
- +[NEIKEv2IKEAuthPacket copyTypeDescription]
- +[NEIKEv2IKEAuthPacket exchangeType]
- +[NEIKEv2IKEAuthPacket prepareDeviceIdentityNotifyPayload:IMEISV:lastResponderPacket:]
- +[NEIKEv2IKESA createAuthenticationDataForSharedSecret:octetVector:prfProtocol:]
- +[NEIKEv2IKESAInitPacket copyTypeDescription]
- +[NEIKEv2IKESAInitPacket encryptPayloads]
- +[NEIKEv2IKESAInitPacket exchangeType]
- +[NEIKEv2IKESAPayload copyTypeDescription]
- +[NEIKEv2IPv4AddressAttribute copyTypeDescription]
- +[NEIKEv2IPv4DHCPAttribute copyTypeDescription]
- +[NEIKEv2IPv4DNSAttribute copyTypeDescription]
- +[NEIKEv2IPv4NetmaskAttribute copyTypeDescription]
- +[NEIKEv2IPv4PCSCFAttribute copyTypeDescription]
- +[NEIKEv2IPv4SubnetAttribute copyTypeDescription]
- +[NEIKEv2IPv6AddressAttribute copyTypeDescription]
- +[NEIKEv2IPv6DHCPAttribute copyTypeDescription]
- +[NEIKEv2IPv6DNSAttribute copyTypeDescription]
- +[NEIKEv2IPv6PCSCFAttribute copyTypeDescription]
- +[NEIKEv2IPv6SubnetAttribute copyTypeDescription]
- +[NEIKEv2Identifier copyTypeDescription]
- +[NEIKEv2Identifier createIdentifierWithType:data:zone:]
- +[NEIKEv2IdentifierPayload copyTypeDescription]
- +[NEIKEv2InformationalPacket copyTypeDescription]
- +[NEIKEv2InformationalPacket exchangeType]
- +[NEIKEv2InitiatorIdentifierPayload copyTypeDescription]
- +[NEIKEv2InitiatorTrafficSelectorPayload copyTypeDescription]
- +[NEIKEv2InitiatorTransportIPv6Address copyTypeDescription]
- +[NEIKEv2IntermediatePacket copyTypeDescription]
- +[NEIKEv2IntermediatePacket exchangeType]
- +[NEIKEv2KeyExchangePayload copyTypeDescription]
- +[NEIKEv2KeyIDIdentifier copyTypeDescription]
- +[NEIKEv2NULLIdentifier copyTypeDescription]
- +[NEIKEv2NoncePayload copyTypeDescription]
- +[NEIKEv2NotifyPayload copyTypeDescription]
- +[NEIKEv2Packet copyTypeDescription]
- +[NEIKEv2Packet createPacketFromReceivedData:]
- +[NEIKEv2Packet encryptPayloads]
- +[NEIKEv2Packet exchangeType]
- +[NEIKEv2Payload copyTypeDescription]
- +[NEIKEv2Payload createPayloadWithType:fromData:]
- +[NEIKEv2ResponderIdentifierPayload copyTypeDescription]
- +[NEIKEv2ResponderTrafficSelectorPayload copyTypeDescription]
- +[NEIKEv2ResponderTransportIPv6Address copyTypeDescription]
- +[NEIKEv2StringAttribute copyTypeDescription]
- +[NEIKEv2SubnetAttribute copyTypeDescription]
- +[NEIKEv2SupportedAttribute copyTypeDescription]
- +[NEIKEv2TrafficSelectorPayload copyTypeDescription]
- +[NEIKEv2UserFQDNIdentifier copyTypeDescription]
- +[NEIKEv2VendorIDPayload copyTypeDescription]
- +[NEPvDConfiguration separateDomainsFromFQDNs:domains:fqdns:]
- -[NEIKEv2AddressIdentifier identifierData]
- -[NEIKEv2AuthPayload description]
- -[NEIKEv2AuthPayload parsePayloadData]
- -[NEIKEv2CertificatePayload description]
- -[NEIKEv2CertificatePayload parsePayloadData]
- -[NEIKEv2CertificateRequestPayload description]
- -[NEIKEv2CertificateRequestPayload parsePayloadData]
- -[NEIKEv2ChildSAPayload description]
- -[NEIKEv2ChildSAPayload parsePayloadData]
- -[NEIKEv2ConfigPayload createConfigAttributeFromData:attributeName:attributeLen:attributeType:customType:]
- -[NEIKEv2ConfigPayload description]
- -[NEIKEv2ConfigPayload parsePayloadData]
- -[NEIKEv2CreateChildPacket isRekeyIKE]
- -[NEIKEv2CustomPayload parsePayloadData]
- -[NEIKEv2DeletePayload description]
- -[NEIKEv2DeletePayload parsePayloadData]
- -[NEIKEv2EAPPayload description]
- -[NEIKEv2EAPPayload parsePayloadData]
- -[NEIKEv2EncryptedFragmentPayload parsePayloadData]
- -[NEIKEv2EncryptedPayload description]
- -[NEIKEv2EncryptedPayload generatePayloadData]
- -[NEIKEv2EncryptedPayload parsePayloadData]
- -[NEIKEv2EncryptionProtocol initWithEncryptionWireType:is256Bit:]
- -[NEIKEv2EncryptionProtocol keyLength]
- -[NEIKEv2FragmentMap init]
- -[NEIKEv2GSPMPayload description]
- -[NEIKEv2GSPMPayload parsePayloadData]
- -[NEIKEv2IKEAuthPacket validateAuthPart1AsInitiator:beforeEAP:]
- -[NEIKEv2IKESA copyInitiatorIdentifier]
- -[NEIKEv2IKESA copyResponderIdentifier]
- -[NEIKEv2IKESA createLocalSignedOctetVectorUsingPrimeKey:]
- -[NEIKEv2IKESA createRemoteSignedOctetsUsingPrimeKey:]
- -[NEIKEv2IKESAPayload description]
- -[NEIKEv2IKESAPayload parsePayloadData]
- -[NEIKEv2IKESAProposal encryptionProtocol]
- -[NEIKEv2IKESAProposal integrityProtocol]
- -[NEIKEv2Identifier setIdentifierData:]
- -[NEIKEv2IdentifierPayload description]
- -[NEIKEv2IdentifierPayload parsePayloadData]
- -[NEIKEv2IntermediatePacket authenticatedDataVector]
- -[NEIKEv2KeyExchangePayload description]
- -[NEIKEv2KeyExchangePayload parsePayloadData]
- -[NEIKEv2NoncePayload description]
- -[NEIKEv2NoncePayload parsePayloadData]
- -[NEIKEv2NotifyPayload copyServerRedirectNonce]
- -[NEIKEv2NotifyPayload copyTypeDescription]
- -[NEIKEv2NotifyPayload description]
- -[NEIKEv2NotifyPayload parsePayloadData]
- -[NEIKEv2Packet copyUnifiedData]
- -[NEIKEv2Packet processReceivedPacketForIKESA:]
- -[NEIKEv2Payload copyPayloadData]
- -[NEIKEv2Payload parsePayloadData]
- -[NEIKEv2RTT updateRTT:responseMessageID:]
- -[NEIKEv2RequestContext initWithRequestType:]
- -[NEIKEv2ResponseConfigPayload parsePayloadData]
- -[NEIKEv2SecurityContext constructEncryptedPacketFromPayloadData:authenticatedHeaders:]
- -[NEIKEv2SecurityContextAESGCM constructEncryptedPacketFromPayloadData:authenticatedHeaders:]
- -[NEIKEv2SecurityContextCBCPlusHMAC constructEncryptedPacketFromPayloadData:authenticatedHeaders:]
- -[NEIKEv2SecurityContextChaCha20Poly1305 .cxx_destruct]
- -[NEIKEv2SecurityContextChaCha20Poly1305 constructEncryptedPacketFromPayloadData:authenticatedHeaders:]
- -[NEIKEv2Session initiateDeleteChildSA:]
- -[NEIKEv2Session initiateInformational:]
- -[NEIKEv2Session initiateNewChildSA:]
- -[NEIKEv2Session initiateRekeyChildSA:]
- -[NEIKEv2Session initiateRekeyIKESA:]
- -[NEIKEv2Session setReceivedReply:messageID:]
- -[NEIKEv2TrafficSelectorPayload description]
- -[NEIKEv2TrafficSelectorPayload parsePayloadData]
- -[NEIKEv2Transport receivePacket:]
- -[NEIKEv2VendorIDPayload description]
- -[NEIKEv2VendorIDPayload parsePayloadData]
- -[NEPvDFetcher delegate]
- -[NEPvDFetcher refreshConfigForced:]
- GCC_except_table2827
- GCC_except_table2837
- GCC_except_table3075
- GCC_except_table3080
- GCC_except_table3086
- GCC_except_table3089
- GCC_except_table3104
- GCC_except_table3105
- GCC_except_table3106
- GCC_except_table3121
- GCC_except_table3135
- GCC_except_table3136
- GCC_except_table3178
- GCC_except_table3182
- GCC_except_table3228
- GCC_except_table3280
- GCC_except_table3332
- GCC_except_table3348
- GCC_except_table3359
- GCC_except_table3379
- GCC_except_table3380
- GCC_except_table3391
- GCC_except_table3397
- GCC_except_table3437
- GCC_except_table3445
- GCC_except_table3482
- GCC_except_table3483
- GCC_except_table4612
- GCC_except_table4648
- GCC_except_table4658
- GCC_except_table4662
- GCC_except_table4674
- GCC_except_table4694
- GCC_except_table4696
- GCC_except_table4702
- GCC_except_table4704
- GCC_except_table4796
- GCC_except_table4865
- GCC_except_table4886
- GCC_except_table4899
- GCC_except_table4996
- GCC_except_table5001
- GCC_except_table5042
- GCC_except_table5088
- GCC_except_table5090
- GCC_except_table5153
- GCC_except_table5156
- GCC_except_table5192
- GCC_except_table5212
- GCC_except_table5214
- GCC_except_table5216
- GCC_except_table5224
- GCC_except_table5263
- GCC_except_table5264
- GCC_except_table5266
- GCC_except_table5268
- GCC_except_table5271
- GCC_except_table5315
- GCC_except_table5336
- GCC_except_table5339
- GCC_except_table5415
- GCC_except_table5743
- GCC_except_table5780
- GCC_except_table5783
- GCC_except_table5837
- GCC_except_table5843
- GCC_except_table5844
- GCC_except_table5852
- GCC_except_table5855
- GCC_except_table5865
- GCC_except_table5884
- GCC_except_table5885
- GCC_except_table5890
- GCC_except_table5891
- GCC_except_table5892
- GCC_except_table5899
- GCC_except_table5908
- GCC_except_table5915
- GCC_except_table5992
- GCC_except_table5993
- GCC_except_table6139
- GCC_except_table6140
- GCC_except_table6141
- GCC_except_table6142
- GCC_except_table6143
- GCC_except_table6157
- GCC_except_table6158
- GCC_except_table6164
- GCC_except_table6190
- GCC_except_table6267
- GCC_except_table6268
- GCC_except_table6269
- GCC_except_table6270
- _CFDataReplaceBytes
- _NEPFKeySetSADBAddr
- _NEPFKeySetSADBIPSecIF
- _NEPFKeySetSADBKey
- _OBJC_IVAR_$_NEIKEv2EncryptionProtocol._is256Bit
- _OBJC_IVAR_$_NEIKEv2IKESA._internalRemoteIdentifier
- _OBJC_IVAR_$_NEIKEv2Payload._payloadData
- _OBJC_IVAR_$_NEIKEv2RequestContext._requestType
- _OBJC_IVAR_$_NEIKEv2SecurityContextAESGCM._decryptionContext
- _OBJC_IVAR_$_NEIKEv2SecurityContextAESGCM._encryptionContext
- _OBJC_IVAR_$_NEIKEv2SecurityContextAESGCM._incomingEncryptionSalt
- _OBJC_IVAR_$_NEIKEv2SecurityContextCBCPlusHMAC._incomingHMACBaseContext
- _OBJC_IVAR_$_NEIKEv2SecurityContextCBCPlusHMAC._outgoingHMACBaseContext
- _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305._incomingEncryptionContext
- _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305._incomingEncryptionSalt
- _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305._outgoingEncryptionContext
- _OBJC_IVAR_$_NEIKEv2SecurityContextChaCha20Poly1305._outgoingEncryptionSalt
- _OBJC_IVAR_$_NEIKEv2Session._receivedReplies
- _OBJC_IVAR_$_NEIKEv2Session._receivedRequests
- _OBJC_IVAR_$_NEIKEv2Session._sentRequests
- _OBJC_IVAR_$_NEIKEv2SubnetAttribute._ipv4SubnetMask
- _ONE_DAY_SECONDS
- _SecPolicyCreateWithProperties
- __OBJC_$_CLASS_METHODS_NEIKEv2ASN1DNIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2AddressAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2AddressIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2AppVersionAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2AuthPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2CertificatePayload
- __OBJC_$_CLASS_METHODS_NEIKEv2CertificateRequestPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2ChildSAPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2ConfigPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2ConfigurationAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2CreateChildPacket
- __OBJC_$_CLASS_METHODS_NEIKEv2CustomPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2DNSDomainAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2DeletePayload
- __OBJC_$_CLASS_METHODS_NEIKEv2EAPPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2EncryptedFragmentPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2EncryptedKeyIDIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2EncryptedPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2FQDNIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2FollowupKEPacket
- __OBJC_$_CLASS_METHODS_NEIKEv2GSPMPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2IKEAuthPacket
- __OBJC_$_CLASS_METHODS_NEIKEv2IKESAInitPacket
- __OBJC_$_CLASS_METHODS_NEIKEv2IKESAPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv4AddressAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv4DHCPAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv4DNSAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv4NetmaskAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv4PCSCFAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv4SubnetAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv6AddressAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv6DHCPAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv6DNSAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv6PCSCFAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2IPv6SubnetAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2Identifier
- __OBJC_$_CLASS_METHODS_NEIKEv2IdentifierPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2InformationalPacket
- __OBJC_$_CLASS_METHODS_NEIKEv2InitiatorIdentifierPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2InitiatorTrafficSelectorPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2InitiatorTransportIPv6Address
- __OBJC_$_CLASS_METHODS_NEIKEv2IntermediatePacket
- __OBJC_$_CLASS_METHODS_NEIKEv2KeyExchangePayload
- __OBJC_$_CLASS_METHODS_NEIKEv2KeyIDIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2NULLIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2NoncePayload
- __OBJC_$_CLASS_METHODS_NEIKEv2NotifyPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2Packet
- __OBJC_$_CLASS_METHODS_NEIKEv2Payload
- __OBJC_$_CLASS_METHODS_NEIKEv2ResponderIdentifierPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2ResponderTrafficSelectorPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2ResponderTransportIPv6Address
- __OBJC_$_CLASS_METHODS_NEIKEv2StringAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2SubnetAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2SupportedAttribute
- __OBJC_$_CLASS_METHODS_NEIKEv2TrafficSelectorPayload
- __OBJC_$_CLASS_METHODS_NEIKEv2UserFQDNIdentifier
- __OBJC_$_CLASS_METHODS_NEIKEv2VendorIDPayload
- __OBJC_$_CLASS_METHODS_NEPvDConfiguration
- __OBJC_$_PROP_LIST_NEIKEv2KeyExchangeHandler
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.480
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.484
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.488
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.492
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.496
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.500
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.504
- ___101-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAInitiator:rekeyIKEContext:iteration:handler:]_block_invoke.508
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.515
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.519
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.523
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.527
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.531
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.535
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.542
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.546
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.550
- ___120-[NEIKEv2Session(Exchange) handleFollowupKEForRekeyIKESAResponder:iteration:replyPacket:replyPacketDescription:handler:]_block_invoke.557
- ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.72
- ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.73
- ___138-[NEIKEv2Session sendRequest:retryIntervalInMilliseconds:maxRetries:timeoutError:resend:sendMessageID:sendCompletionHandler:replyHandler:]_block_invoke.77
- ___181-[NEIKEv2Session initWithIKEConfig:firstChildConfig:sessionConfig:queue:ipsecInterface:ikeSocketHandler:saSession:shouldOwnSASession:packetDelegate:transport:configurationDelegate:]_block_invoke.40
- ___25-[NEIKEv2Session connect]_block_invoke.45
- ___28-[NEIKEv2Session disconnect]_block_invoke.47
- ___31-[NEIKEv2Session startDPDTimer]_block_invoke.63
- ___37-[NEIKEv2Session sendCurrentRequest:]_block_invoke.71
- ___39-[NEIKEv2Session startIKELifetimeTimer]_block_invoke.64
- ___46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.295
- ___46-[NEIKEv2Session(Exchange) receiveConnection:]_block_invoke.302
- ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.617
- ___46-[NEIKEv2Session(Exchange) receiveRekeyIKESA:]_block_invoke.618
- ___47-[NEIKEv2Session(Exchange) initiateNewChildSA:]_block_invoke.341
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.564
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.568
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.572
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.576
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.580
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke.585
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.584
- ___47-[NEIKEv2Session(Exchange) initiateRekeyIKESA:]_block_invoke_2.589
- ___48-[NEIKEv2Session(Exchange) initiateMOBIKEInner:]_block_invoke.646
- ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.447
- ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.448
- ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke.449
- ___49-[NEIKEv2Session(Exchange) initiateRekeyChildSA:]_block_invoke_2.450
- ___53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.357
- ___53-[NEIKEv2Session(Exchange) receiveNewChildSA:packet:]_block_invoke.358
- ___55-[NEIKEv2Session(Exchange) receiveRekeyChildSA:packet:]_block_invoke.469
- ___95+[NEUserNotification promptForLocalAuthenticationWithReason:completionQueue:completionHandler:]_block_invoke.44
- ___95+[NEUserNotification promptForLocalAuthenticationWithReason:completionQueue:completionHandler:]_block_invoke.46
- ___Block_byref_object_copy_.12486
- ___Block_byref_object_copy_.14925
- ___Block_byref_object_copy_.20384
- ___Block_byref_object_copy_.21611
- ___Block_byref_object_copy_.22661
- ___Block_byref_object_copy_.23794
- ___Block_byref_object_copy_.24496
- ___Block_byref_object_copy_.27077
- ___Block_byref_object_copy_.28258
- ___Block_byref_object_copy_.9531
- ___Block_byref_object_dispose_.12487
- ___Block_byref_object_dispose_.14926
- ___Block_byref_object_dispose_.20385
- ___Block_byref_object_dispose_.21612
- ___Block_byref_object_dispose_.22662
- ___Block_byref_object_dispose_.23795
- ___Block_byref_object_dispose_.24497
- ___Block_byref_object_dispose_.27078
- ___Block_byref_object_dispose_.28259
- ___Block_byref_object_dispose_.9532
- ___block_descriptor_48_e8_32s40w_e37_B16?0"NEIKEv2SessionConfiguration"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48r56w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8r48l8s40l8w56l8
- ___block_descriptor_tmp.19453
- ___block_descriptor_tmp.23347
- ___block_descriptor_tmp.25341
- ___block_descriptor_tmp.25955
- ___block_descriptor_tmp.3
- ___block_literal_global.10.15485
- ___block_literal_global.10.9190
- ___block_literal_global.10123
- ___block_literal_global.12764
- ___block_literal_global.13142
- ___block_literal_global.14.22122
- ___block_literal_global.14057
- ___block_literal_global.14225
- ___block_literal_global.14927
- ___block_literal_global.15.25573
- ___block_literal_global.15487
- ___block_literal_global.16059
- ___block_literal_global.16302
- ___block_literal_global.16787
- ___block_literal_global.17.14070
- ___block_literal_global.17.17754
- ___block_literal_global.17627
- ___block_literal_global.17763
- ___block_literal_global.18075
- ___block_literal_global.19379
- ___block_literal_global.20.17760
- ___block_literal_global.20204
- ___block_literal_global.20663
- ___block_literal_global.21708
- ___block_literal_global.22127
- ___block_literal_global.22524
- ___block_literal_global.23264
- ___block_literal_global.23345
- ___block_literal_global.23898
- ___block_literal_global.24010
- ___block_literal_global.24045
- ___block_literal_global.24239
- ___block_literal_global.25286
- ___block_literal_global.25339
- ___block_literal_global.25577
- ___block_literal_global.25681
- ___block_literal_global.26061
- ___block_literal_global.26615
- ___block_literal_global.26805
- ___block_literal_global.27043
- ___block_literal_global.27598
- ___block_literal_global.28.27081
- ___block_literal_global.28277
- ___block_literal_global.30
- ___block_literal_global.4.14060
- ___block_literal_global.63.20199
- ___block_literal_global.7.25276
- ___block_literal_global.73.25676
- ___block_literal_global.9188
- ___stderrp
- ___strncpy_chk
- __extensionAuxiliaryHostProtocol.protocol.20200
- __extensionAuxiliaryHostProtocol.protocol.24046
- __extensionAuxiliaryHostProtocol.protocol.25677
- __extensionAuxiliaryHostProtocol.protocolInit.20198
- __extensionAuxiliaryHostProtocol.protocolInit.24044
- __extensionAuxiliaryHostProtocol.protocolInit.25675
- __extensionAuxiliaryVendorProtocol.protocol.20205
- __extensionAuxiliaryVendorProtocol.protocol.25682
- __extensionAuxiliaryVendorProtocol.protocolInit.20203
- __extensionAuxiliaryVendorProtocol.protocolInit.25680
- _cc_clear
- _convert_error_to_string.24488
- _driverInterface.driverInterface.10120
- _driverInterface.driverInterface.16788
- _driverInterface.driverInterface.20660
- _driverInterface.driverInterface.22123
- _driverInterface.onceToken.10119
- _driverInterface.onceToken.16786
- _driverInterface.onceToken.20659
- _driverInterface.onceToken.22121
- _findsupportedalg
- _fprintf
- _g_noAppFilter.28232
- _globalConfigurationManager.gChangeQueue.17758
- _globalConfigurationManager.gConfigurationManager.17755
- _globalConfigurationManager.onceToken.17753
- _initGlobals.onceToken.16301
- _ipsec_check_keylen
- _ipsec_check_keylen2
- _ipsec_get_keylen
- _ipsec_supported
- _kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA256
- _kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA384
- _kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA512
- _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
- _kSecKeyAlgorithmECDSASignatureMessageX962SHA384
- _kSecKeyAlgorithmECDSASignatureMessageX962SHA512
- _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA1
- _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA256
- _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA384
- _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA512
- _kSecKeyAlgorithmRSASignatureMessagePSSSHA256
- _kSecKeyAlgorithmRSASignatureMessagePSSSHA384
- _kSecKeyAlgorithmRSASignatureMessagePSSSHA512
- _kSecPolicyAppleIPsec
- _kSecPolicyName
- _loadedManagers.loadedManagers.27041
- _loadedManagers.loadedManagers.28235
- _loadedManagers.managers_init.27040
- _loadedManagers.managers_init.28234
- _managerInterface.managerInterface.10124
- _managerInterface.managerInterface.20664
- _managerInterface.managerInterface.22128
- _managerInterface.onceToken.10122
- _managerInterface.onceToken.20662
- _managerInterface.onceToken.22126
- _memset
- _objc_msgSend$constructEncryptedPacketFromPayloadData:authenticatedHeaders:
- _objc_msgSend$copyShortDescription
- _objc_msgSend$copyTypeDescription
- _objc_msgSend$createIdentifierWithType:data:
- _objc_msgSend$createIdentifierWithType:data:zone:
- _objc_msgSend$dataWithData:
- _objc_msgSend$initWithMethod:keyExchangeData:
- _objc_msgSend$initWithRequestType:
- _objc_msgSend$parsePayloadData
- _objc_msgSend$setIdentifierData:
- _objc_msgSend$timeIntervalSinceNow
- _pfkey_align
- _pfkey_check
- _pfkey_recv
- _pfkey_recv_register
- _pfkey_set_supported
- _sharedManager.onceToken.17762
- _sharedManager.onceToken.28276
- _supported_map
CStrings:
+ "%@ Cannot parse packet, no acceptable payloads found"
+ "%@ Cannot parse packet, no encrypted payload found"
+ "%@ Discarding stale reply"
+ "%@ Discarding undecrypted packet"
+ "%@ Dropping IKE_SA_INIT sent to non-server session"
+ "%@ Dropping IKE_SA_INIT sent to session that already selected proposal"
+ "%@ Dropping IKE_SA_INIT with wrong message ID %d"
+ "%@ Encrypted payload found in already decrypted packet"
+ "%@ Encrypted payload type %zu is not permitted"
+ "%@ Failed to add fragment to map!"
+ "%@ Failed to construct authenticated data vector"
+ "%@ Failed to get device identity payload"
+ "%@ Failed to parse critical payload type %zu"
+ "%@ Failed to parse payload type %zu, ignoring"
+ "%@ Found additional %u bytes after parsing completed"
+ "%@ Ignoring received SA_INIT packet (redirect nonce check failed): %@"
+ "%@ Ignoring request for device identity as peer is not authenticated"
+ "%@ Ignoring unexpected response"
+ "%@ Not enough remaining bytes for payload type %zu (%u > %u)"
+ "%@ Not enough remaining bytes for payload type %zu header (%u < %zu)"
+ "%@ Payload type %zu claimed length too short (%u < %zu)"
+ "%@ Received PFKey Message (type %d) reporting error: [%d] %s"
+ "%@ Received PFKey Message associated with DB (type %d, SAID %u, pid %u, SPI %08X)"
+ "%@ Received all %u fragments for message ID %d"
+ "%@ Received request for device identity"
+ "%@ Responder ID missing"
+ "%@ Sending %u datagrams for reply: %@"
+ "%@ Sending %u datagrams for request %@"
+ "%@ Setting IKE hard lifetime timer for %llu seconds"
+ "%@ Setting IKE soft lifetime timer for %llu seconds"
+ "%@ Unable to handle unsolicited request %@"
+ "%@ Unencrypted critical payload type %zu is not permitted"
+ "%@ Unencrypted payload type %zu is not permitted, ignoring"
+ "%@ Unsupported %@ key length %u"
+ "%@ Using fallback local identifier %@"
+ "%@ ignoring unexpected %@ payload"
+ "%@_%u"
+ "%s called with null ![self hasFragmentForNumber:fragmentNumber]"
+ "%s called with null !self.isInbound"
+ "%s called with null (expectedCount > 0)"
+ "%s called with null (fragmentNumber <= self.expectedCount)"
+ "%s called with null (fragmentNumber >= 1)"
+ "%s called with null addressData"
+ "%s called with null digitalSignatureAlgorithmIdentifier"
+ "%s called with null fragmentMap.readyForReassmebly"
+ "%s called with null incomingEncryptionKey"
+ "%s called with null outgoingEncryptionKey"
+ "%s called with null packetConstructor"
+ "%s called with null payloadVector"
+ "%s called with null payloads"
+ "%s called with null self.isDigitalSignature"
+ "%s called with null self.originalPacket"
+ "%s called with null self.receivedReplyIDs"
+ "%s called with null self.receivedRequestIDs"
+ "%s called with null signedDataVector"
+ "%s:%d: \"%@\" is not a recognized EAP method"
+ "%s:%d: \"%@\" is not a recognized PRF protocol"
+ "%s:%d: \"%@\" is not a recognized authentication method"
+ "%s:%d: \"%@\" is not a recognized encryption method"
+ "%s:%d: \"%@\" is not a recognized integrity method"
+ "%s:%d: can't mix authenticated and unauthenticated encryption protocols in the same proposal"
+ "%s:%d: failed to get DH protocol(s)"
+ "%s:%d: failed to get PRF protocol(s)"
+ "%s:%d: failed to get encryption protocol(s)"
+ "%s:%d: failed to get integrity protocol(s)"
+ "+[NEIKEv2Crypto validateSignature:signedDataVector:authProtocol:publicKey:]"
+ "+[NEIKEv2Packet createPacketFromFragmentMap:ikeSA:]"
+ "+[NEIKEv2Payload createPayloadWithType:fromReceivedData:]"
+ "-[NEIKEv2AddressIdentifier initWithAddressData:identifierType:]"
+ "-[NEIKEv2AuthPayload parsePayloadData:]"
+ "-[NEIKEv2AuthenticationProtocol(Packet) copyDigitalSignatureAlgorithmIdentifier]"
+ "-[NEIKEv2AuthenticationProtocol(Packet) initWithDigitalSignatureAlgorithmIdentifier:]"
+ "-[NEIKEv2CertificatePayload parsePayloadData:]"
+ "-[NEIKEv2CertificateRequestPayload parsePayloadData:]"
+ "-[NEIKEv2ChildSAPayload parsePayloadData:]"
+ "-[NEIKEv2ConfigPayload parsePayloadData:]"
+ "-[NEIKEv2DeletePayload parsePayloadData:]"
+ "-[NEIKEv2EncryptedFragmentPayload parsePayloadData:]"
+ "-[NEIKEv2FragmentMap addFragment:]"
+ "-[NEIKEv2FragmentMap hasFragmentForNumber:]"
+ "-[NEIKEv2FragmentMap initWithExpectedCount:]"
+ "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthFinalAsInitiator:childSA:]"
+ "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthInitialAsInitiator:beforeEAP:]"
+ "-[NEIKEv2IKESA(Crypto) validateAuthenticationForDelegateWithConfiguration:]"
+ "-[NEIKEv2IKESAPayload parsePayloadData:]"
+ "-[NEIKEv2IdentifierPayload parsePayloadData:]"
+ "-[NEIKEv2IntermediatePacket constructAuthenticatedDataWithPayloads:payloadsLength:authenticatedHeaders:]"
+ "-[NEIKEv2KeyExchangePayload parsePayloadData:]"
+ "-[NEIKEv2NotifyPayload parsePayloadData:]"
+ "-[NEIKEv2Packet copyPacketDatagramsForIKESA:]"
+ "-[NEIKEv2PacketConstructor initWithPayloadVector:]"
+ "-[NEIKEv2ResponseConfigPayload initWithResponseConfigPayload:configRequest:]"
+ "-[NEIKEv2ResponseConfigPayload parsePayloadData:]"
+ "-[NEIKEv2SecurityContextAESGCM constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]"
+ "-[NEIKEv2SecurityContextCBCPlusHMAC constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]"
+ "-[NEIKEv2SecurityContextChaCha20Poly1305 constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:]"
+ "-[NEIKEv2TrafficSelectorPayload parsePayloadData:]"
+ ".well-known/masque/udp"
+ "@\"<NEExtensionBaseHostDelegate>\""
+ "@\"OS_dispatch_queue\""
+ "@\"Protocol\""
+ "@\"_TtC16NetworkExtension41NEExtensionBaseProviderHostExportedObject\""
+ "@\"_TtC16NetworkExtension44NEURLFilterControlProviderHostExportedObject\""
+ "@\"_TtC16NetworkExtension45NEHotspotEvaluationProviderHostExportedObject\""
+ "@\"_TtC16NetworkExtension49NEHotspotAuthenticationProviderHostExportedObject\""
+ "@36@0:8@16I24@28"
+ "Auth payload with digital signature method %@ does not have any data"
+ "AuthData too short for AlgorithmIdentifier len %zu, payload %@"
+ "B24@?0@\"NSNumber\"8^B16"
+ "B32@?0@\"NSNumber\"8@16^B24"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_fragment_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_auth_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_cert_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_certreq_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_config_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_delete_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_id_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_ke_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_payload_ts_hdr_t))"
+ "BACKTRACE %s called with null (payloadData.length >= sizeof(ikev2_proposal_t))"
+ "BACKTRACE %s called with null (payloadDataLength >= sizeof(ikev2_payload_notify_hdr_t))"
+ "Can't create address identifier using type %zu"
+ "Cannot copy additional address from notification %@"
+ "Cannot parse packet, header claims to be longer than data (%u > %zu)"
+ "Cannot parse packet, recieved data length %zu is too short"
+ "Child SA proposal mixes authenticated and unauthenticated encryption protocols"
+ "Child SA proposal with authenticated encryption includes integrity options"
+ "Child TLS SA proposal has encryption protocol"
+ "Child TLS SA proposal has integrity protocols"
+ "Construction state after processing fragment %u: Index %zu, Offset %zu"
+ "Could not parse AlgorithmIdentifier parameters, error %d payload %@"
+ "Could not parse AlgorithmIdentifier, error %d payload %@"
+ "DELETE ESP SPI data length too long for %u SPIs, ignoring extra bytes (%u > %u)"
+ "DELETE ESP SPI data length too short for %u SPIs (%u < %u)"
+ "DELETE TLS SPI data length too long for %u SPIs (%u > %u), ignoring extra bytes"
+ "DELETE TLS SPI data length too short for %u SPIs (%u < %u)"
+ "Data is longer than claimed by header (%zu > %u), ignoring extra bytes"
+ "Failed to copy hashed data for %@"
+ "Failed to get construct data vector for IKE_INTERMEDIATE"
+ "Failed to parse SA payload, length %u"
+ "Failed to process all traffic selectors (%zu/%u)"
+ "Failed to sign for %@ with private key: %@"
+ "Fetching new PvD %@ in %lu mins"
+ "Fetching proxy PvD configuration resulted in malformed JSON object: %@ with url: %@"
+ "Fetching proxy PvD configuration resulted in unexpected response: %ld with url: %@"
+ "IKE SA proposal %u has wrong SPI length %u"
+ "IKE SA proposal %u has wrong protocol ID %u"
+ "IKE SA proposal mixes authenticated and unauthenticated encryption protocols"
+ "IKE SA proposal with authenticated encryption includes integrity options"
+ "IPv4 traffic selector end address is wrong family %zu"
+ "IPv4 traffic selector missing end address"
+ "IPv4 traffic selector missing start address"
+ "IPv4 traffic selector start address is wrong family %zu"
+ "IPv6 traffic selector end address is wrong family %zu"
+ "IPv6 traffic selector missing end address"
+ "IPv6 traffic selector missing start address"
+ "IPv6 traffic selector start address is wrong family %zu"
+ "Ignoring %u remaining bytes in Child SA payload"
+ "Ignoring %u remaining bytes in SA payload"
+ "Ignoring %u remaining bytes in configuration payload"
+ "Ignoring %u remaining bytes in proposal %u"
+ "Ignoring %u remaining bytes in response configuration payload"
+ "Ignoring %u remaining bytes in traffic selector payload"
+ "Ignoring %u remaining bytes in transform %u "
+ "Ignoring ESN transform %u found in IKE SA proposal"
+ "Ignoring PvD configuration, no valid proxy-match criteria"
+ "Invalid IMEI string!"
+ "Invalid IMEISV string!"
+ "Invalid Notify %zu ESP SPI length %u"
+ "Invalid Notify %zu IKE SPI length %u"
+ "Invalid Notify %zu TLS SPI length %u"
+ "Invalid Notify payload length %zu too small for SPI length %u"
+ "Invalid PFKey message size: %zd"
+ "Invalid PvD configuration, no valid proxies"
+ "Invalid address length %zu"
+ "Invalid proxy configuration, not a dictionary: %@"
+ "Invalid size 0"
+ "Listener can't handle packet %@"
+ "LocalNetwork icon configuration: device scale is %f"
+ "LocalNetwork icon configuration: icon URL is %@"
+ "LocalNetwork icon configuration: notification dictionay option %@"
+ "LocalNetworkPrivacyiOS@%dx.png"
+ "Must use a subclass of NEIKEv2Packet to create inbound packets"
+ "Must use a subclass of NEIKEv2Packet to create packets"
+ "Must use a subclass of NEIKEv2Payload to create payloads"
+ "NEIKEv2PacketConstructor"
+ "NEPFKeySendDeleteAll: calculated message length (%u) != final message len (%zd)"
+ "NEPFKeySendGetSPI: calculated message length (%u) != final message len (%zd)"
+ "NEPFKeySendGetStats: calculated message length (%u) != final message len (%zd)"
+ "NEPFKeySendMigrate: calculated message length (%u) != final message len (%zd)"
+ "No valid traffic selectors for payload"
+ "NoPPK AuthData too short for AlgorithmIdentifier len %u, payload %@"
+ "Not enough bytes remaining (%u) for transform %u"
+ "Not enough bytes remaining (%u) to process configuration attribute of type %zu length %u"
+ "Not enough bytes remaining (%u) to process response configuration attribute of type %zu length %u"
+ "Not enough bytes remaining (%u) to process traffic selector of type %u length %u"
+ "Not enough bytes remaining (%u) to process transform %u with length %u"
+ "PFKey socket received error: [%d] %s"
+ "Packet construction state not finalized: index %zu, offset %zu"
+ "Parsing configuration attribute of type %zu length %u"
+ "Parsing response configuration attribute of type %zu length %u"
+ "PvD configuration missing mandatory fields"
+ "PvD fetch for %@ fired"
+ "PvD: Ports are not currently supported in proxy-match rules: %@"
+ "PvD: Proxy URL %@ does not contain relay host %@"
+ "PvD: Proxy identifier %@ does not handle both TCP and UDP"
+ "PvD: Referenced proxy %@ did not have 2 entries: %@"
+ "PvD: Two proxies do not have matching ALPN values: %@"
+ "PvD: connect-udp proxy URI path must contain '.well-known/masque/udp/{target_host}/{target_port}': %@"
+ "PvD: ignore fallback proxy identifiers %@"
+ "PvD: invalid \"proxies\" key value: %@"
+ "PvD: match rules refer to different identifiers %@ != %@"
+ "Ran out of payloads with remaining length %u to write"
+ "Refusing to parse packet, length %zu is unreasonable"
+ "Request to write no plaintext with non-empty payload vector"
+ "Request to write plaintext (length %u) with empty payload vector"
+ "Request to write plaintext with finalized construction state"
+ "Resetting kern.ipc.maxsockbuf %u -> %u"
+ "Responder ID missing"
+ "SA proposal %u has wrong SPI length %u for protocol %@"
+ "SBUserNotificationHeaderImagePath"
+ "Sending PFKey add SPI %08X"
+ "Sending PFKey delete SPI %08X"
+ "Sending PFKey get for SPI %08X"
+ "Sending PFKey migrate SPI %08X"
+ "Sending PFKey update SPI %08X"
+ "Setting kern.ipc.maxsockbuf %u -> %u"
+ "Subclasses of NEIKEv2Packet must implement filloutPayloads"
+ "Subclasses of NEIKEv2Packet must implement gatherPayloads"
+ "T@\"NSData\",R,N,V_notifyData"
+ "T@\"NSData\",R,V_identifierData"
+ "T@\"NSString\",R,V_stringValue"
+ "T@\"NWAddressEndpoint\",R,V_address"
+ "TB,R,N,V_isNonStandard"
+ "TC,R,V_prefix"
+ "TQ,R,N,V_digitalSignatureAlgorithm"
+ "TQ,R,N,V_hashType"
+ "TQ,R,N,V_method"
+ "TQ,R,N,V_securePasswordMethod"
+ "TQ,R,V_method"
+ "TQ,R,V_type"
+ "TS,R,N,V_notifyStatus"
+ "Ti,R,N"
+ "Traffic selector length %u is too short"
+ "Transform %u has a key length attribute with length 0"
+ "Transform %u has an unrecognized attribute type %u, ignoring"
+ "Transform %u has invalid key length %u for encryption type %@"
+ "Transform %u length %u is too short"
+ "Transform %u type %u in Child SA proposal is unsupported"
+ "Transform %u type %u in IKE SA proposal is unsupported"
+ "Unable to get RSA-PSS authentication protocol, payload %@"
+ "Unexpected NULL parameters for RSA-PSS, payload %@"
+ "Unexpected non-NULL parameters for signature algorithm %@, payload %@"
+ "Unrecognized digital signature AlgorithmIdentifier OID, payload %@"
+ "Unsupported %@ key length %u"
+ "[4C]"
+ "[NEMutableSensitiveData mutableSensitiveDataWithMaxCapacity:%u] failed"
+ "[NESensitiveData sensitiveDataWithBytes:length:%zu] failed"
+ "[packet addNotification:NEIKEv2NotifyTypeDeviceIdentity] failed"
+ "[responsePacket addNotification:NEIKEv2NotifyTypeDeviceIdentity] failed"
+ "_aggregatedPayloadsLength"
+ "_currentCount"
+ "_fallbackLocalIdentifier"
+ "_fetchTimer"
+ "_firstFragment"
+ "_identifierType"
+ "_index"
+ "_lastSentRequest"
+ "_originalPacket"
+ "_originalPacketLength"
+ "_payloadDataVector"
+ "_payloadSubHeader"
+ "_payloadVector"
+ "_receivedReplyIDs"
+ "_receivedRequestIDs"
+ "_responderIdentifierPayload"
+ "alpn"
+ "com.apple.networkextension.pvdFetch"
+ "connect-udp"
+ "constructEncryptedPacketFromConstructor:plaintextLength:authenticatedHeaders:"
+ "fcntl(%d, F_GETFL) failed: [%d] %s"
+ "fcntl(%d, F_SETFL) failed: [%d] %s"
+ "floatValue"
+ "https-connect"
+ "incomingEncryptionContext"
+ "incomingEncryptionSalt"
+ "incomingHMACBaseContext"
+ "increaseLengthBy:"
+ "isFragment"
+ "keysOfEntriesPassingTest:"
+ "main-screen-scale"
+ "nextObject"
+ "null"
+ "objectEnumerator"
+ "objectsPassingTest:"
+ "outgoingEncryptionContext"
+ "outgoingEncryptionSalt"
+ "outgoingHMACBaseContext"
+ "parsePayloadData:"
+ "pfkey_send_x1: calculated message length (%u) != final message len (%zd)"
+ "pfkey_send_x2: calculated message length (%u) != final message len (%zd)"
+ "pfkey_send_x3: calculated message length (%u) != final message len (%zd)"
+ "pfkey_send_x4: calculated message length (%u) != final message len (%zd)"
+ "pfkey_send_x5: calculated message length (%u) != final message len (%zd)"
+ "ports"
+ "proxy"
+ "proxy-match"
+ "requestType"
+ "setsockopt(%d, SO_RCVBUF, %d) failed: [%d] %s"
+ "setsockopt(%d, SO_SNDBUF, %d) failed: [%d] %s"
+ "sysctlbyname(kern.ipc.maxsockbuf) failed: [%d] %s"
+ "timeIntervalSinceDate:"
+ "typeDescription"
+ "valueForKey:"
+ "{?=\"chacha20_ctx\"{?=\"state\"[16I]\"buffer\"[64C]\"leftover\"Q}\"poly1305_ctx\"{?=\"r0\"I\"r1\"I\"r2\"I\"r3\"I\"r4\"I\"s1\"I\"s2\"I\"s3\"I\"s4\"I\"h0\"I\"h1\"I\"h2\"I\"h3\"I\"h4\"I\"buf\"[16C]\"buf_used\"Q\"key\"[16C]}\"aad_nbytes\"Q\"text_nbytes\"Q\"state\"C}"
+ "{?=\"ctx\"[96I]}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0b"
- "%@ Could not find Device Identity (IMEI) data"
- "%@ Dropping IKE SA Init sent to non-server session"
- "%@ Dropping IKE SA Init with wrong message ID %d"
- "%@ Failed to receive IKE SA Init packet (receive)"
- "%@ Ignoring received packet (nonce check failed): %@"
- "%@ Missing fragment %u/%u, skipping reassembly"
- "%@ Received PFKey Message associated with DB (type %d, SAID %u, pid %u, SPI %08X"
- "%@ Received PFKey Message reporting error: %s (type %d)"
- "%@ Received all %u fragments"
- "%@ Received request for device identity notify payload."
- "%@ Sending %u datagrams for packet (message %u): %@"
- "%@ Sending reply: %@"
- "%@ received sending notify payload request"
- "%@%s"
- "%@: Setting IKE hard lifetime timer for %llu seconds"
- "%@: Setting IKE soft lifetime timer for %llu seconds"
- "%d %d %d\n"
- "%s called with null (data.length >= sizeof(ikev2_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(header))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_cert_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_certreq_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_config_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_delete_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_id_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_ke_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_payload_ts_hdr_t))"
- "%s called with null (self.payloadData.length >= sizeof(ikev2_proposal_t))"
- "%s called with null authData.length"
- "%s called with null data.bytes"
- "%s called with null domains"
- "%s called with null fqdns"
- "%s called with null idPayload"
- "%s called with null ikeSA.copyInitiatorIdentifier"
- "%s called with null ikeSA.copyResponderIdentifier"
- "%s called with null inputData.length"
- "%s called with null primeAuth.isValid"
- "%s called with null receivedFragments"
- "%s called with null remoteSignedOctets"
- "%s called with null self.encryptedPayload"
- "%s called with null self.encryptedPayload.authenticatedHeaders"
- "%s called with null self.fragments"
- "%s called with null self.payloadData"
- "%s called with null self.receivedReplies"
- "%s called with null self.receivedRequests"
- "%s called with null self.sentRequests"
- "%s called with null signedData.length"
- "%s%d: \"%@\" is not a recognized EAP method"
- "%s%d: \"%@\" is not a recognized PRF protocol"
- "%s%d: \"%@\" is not a recognized authentication method"
- "%s%d: \"%@\" is not a recognized encryption method"
- "%s%d: \"%@\" is not a recognized integrity method"
- "%s%d: failed to get DH protocol(s)"
- "%s%d: failed to get PRF protocol(s)"
- "%s%d: failed to get encryption protocol(s)"
- "+[NEIKEv2Crypto copyAuthenticationProtocolForAuthMethod:authData:]"
- "+[NEIKEv2Crypto copySignatureForData:authProtocol:privateKey:]"
- "+[NEIKEv2Crypto validateSignature:signedData:authProtocol:publicKey:]"
- "+[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octetVector:prfProtocol:]"
- "+[NEIKEv2Packet createPacketFromReceivedData:]"
- "+[NEIKEv2Packet createPacketFromReceivedFragments:ikeSA:]"
- "+[NEPvDConfiguration separateDomainsFromFQDNs:domains:fqdns:]"
- "-[NEIKEv2AuthPayload parsePayloadData]"
- "-[NEIKEv2CertificatePayload parsePayloadData]"
- "-[NEIKEv2CertificateRequestPayload parsePayloadData]"
- "-[NEIKEv2ChildSAPayload parsePayloadData]"
- "-[NEIKEv2ConfigPayload parsePayloadData]"
- "-[NEIKEv2CustomPayload parsePayloadData]"
- "-[NEIKEv2DeletePayload parsePayloadData]"
- "-[NEIKEv2EAPPayload parsePayloadData]"
- "-[NEIKEv2EncryptedFragmentPayload parsePayloadData]"
- "-[NEIKEv2EncryptedPayload parsePayloadData]"
- "-[NEIKEv2FragmentMap init]"
- "-[NEIKEv2GSPMPayload parsePayloadData]"
- "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthPart1AsInitiator:beforeEAP:]"
- "-[NEIKEv2IKEAuthPacket(Exchange) validateAuthPart2AsInitiator:childSA:]"
- "-[NEIKEv2IKESA localIdentifier]"
- "-[NEIKEv2IKESA remoteIdentifier]"
- "-[NEIKEv2IKESA(Crypto) copyValidateAuthBlock]_block_invoke"
- "-[NEIKEv2IKESAPayload parsePayloadData]"
- "-[NEIKEv2IdentifierPayload parsePayloadData]"
- "-[NEIKEv2IntermediatePacket authenticatedDataVector]"
- "-[NEIKEv2KeyExchangePayload parsePayloadData]"
- "-[NEIKEv2NoncePayload parsePayloadData]"
- "-[NEIKEv2NotifyPayload parsePayloadData]"
- "-[NEIKEv2ResponseConfigPayload parsePayloadData]"
- "-[NEIKEv2SecurityContextAESGCM constructEncryptedPacketFromPayloadData:authenticatedHeaders:]"
- "-[NEIKEv2SecurityContextCBCPlusHMAC constructEncryptedPacketFromPayloadData:authenticatedHeaders:]"
- "-[NEIKEv2SecurityContextChaCha20Poly1305 constructEncryptedPacketFromPayloadData:authenticatedHeaders:]"
- "-[NEIKEv2TrafficSelectorPayload parsePayloadData]"
- "-[NEIKEv2VendorIDPayload parsePayloadData]"
- "@40@0:8Q16@24^{_NSZone=}32"
- "AUTH payload length %zu is too short for signature algorithm length %u"
- "Attempted to process non-fragment payload"
- "AuthData too short for first byte AlgorithmIdentifier, len %u %@"
- "BACKTRACE %s called with null (self.payloadData.length >= sizeof(ikev2_fragment_hdr_t))"
- "BACKTRACE %s called with null (self.payloadData.length >= sizeof(ikev2_payload_notify_hdr_t))"
- "BACKTRACE %s called with null (self.payloadData.length >= sizeof(ikev2_proposal_t))"
- "Bad payload length too long (%u)"
- "Bad payload length too short (%u)"
- "Cannot parse packet, header claims to be longer than data (%u > %u)"
- "Cannot parse packet, no acceptable payloads found"
- "Could not parse AlgorithmIdentifier parameters, error %d payload len %u payload %@"
- "Could not parse AlgorithmIdentifier, error %d payload len %u payload %@"
- "Encoded signature algorithm data length %zu is too long"
- "Failed to get authenticated data for IKE_INTERMEDIATE"
- "Failed to parse SA, length %u"
- "Failed to parse authentication protocol for method %@"
- "Failed to parse critical payload type %u"
- "Failed to process all traffic selectors (%u/%u)"
- "Failed to receive IKE SA Init packet (receive)"
- "Failed to set socket %d to non-blocking mode"
- "Failed to sign with private key: %@"
- "Fetching proxy configuration resulted in JSON object that is not a dictionary with url: %@"
- "Fetching proxy configuration resulted in malformed JSON object: %@ with url: %@"
- "Fetching proxy configuration resulted in unexpected response: %ld with url: %@"
- "Found unsupported transform type %u in Child SA proposal with protocol %@"
- "Found unsupported transform type %u in IKE SA proposal"
- "Fragment missing decrypted data"
- "Ignoring ESN transform found in IKE SA proposal"
- "Invalid Notify ESP SPI length %u"
- "Invalid Notify IKE SPI length %u"
- "Invalid Notify TLS SPI length %u"
- "Invalid Notify payload length %u cannot hold ESP SPI"
- "Invalid Notify payload length %u cannot hold IKE SPI"
- "Invalid Notify payload length %u cannot hold TLS SPI"
- "Invalid PFKey message size: %zu"
- "Invalid address length %u"
- "Invalid size %u"
- "Invalid traffic selector length (%u)"
- "Key %@ is not NSNumber"
- "Listener received non SA_INIT packet %@"
- "Listener received packet with non-zero responder SPI %@"
- "Listener received responder packet %@"
- "Listener received response packet %@"
- "Must use a subclass of NEIKEv2Payload to init"
- "PFKey socket received error: %s"
- "Packet shorter than header size (size: %u, minimum expected: %u)"
- "Parsing configuration attribute of type %u length %u"
- "Parsing traffic selector of type %u length %u"
- "PvD configuration missing fields"
- "SA proposal %u has wrong length %u"
- "SA proposal %u has wrong length %u for protocol %@"
- "SecPolicyCreateWithProperties failed"
- "Sending PFKey add SPI %04X"
- "Sending PFKey delete SPI %04X"
- "Sending PFKey get for SPI %04X"
- "Sending PFKey migrate SPI %04X"
- "Sending PFKey update SPI %04X"
- "T@\"NSData\",&,N,V_sharedSecret"
- "T@\"NSData\",&,V_identifierData"
- "T@\"NSData\",R,N"
- "TC,R"
- "TS,R,N"
- "The length in the IKE header is too big"
- "Traffic selector missing start address"
- "Unable to get RSA-PSS authentication protocol, payload len %u payload %@"
- "Unencrypted critical payload type %u is not permitted for packet type %u"
- "Unencrypted payload type %u is not permitted for packet type %u"
- "Unexpected NULL parameters for RSA-PSS, payload len %u payload %@"
- "Unexpected non-NULL parameters for %@, payload len %u payload %@"
- "Unrecognized digital signature AlgorithmIdentifier OID, payload len %u payload %@"
- "[NEIKEv2Crypto createRandomWithSize:%u] failed"
- "[NEIKEv2Packet createPacketFromReceivedData] failed"
- "[NESensitiveData sensitiveDataWithBytes:length:IKEv2_CRYPTO_CHACHAPOLY_SALT_LEN] failed"
- "[NESensitiveData sensitiveDataWithBytes:length:IKEv2_CRYPTO_GCM_SALT_LEN] failed"
- "[NSData subdataWithRange:] failed"
- "[self createLocalSignedOctetsUsingPrimeKey:] failed"
- "_256"
- "_decryptionContext"
- "_encryptionContext"
- "_incomingEncryptionSalt"
- "_incomingHMACBaseContext"
- "_internalRemoteIdentifier"
- "_ipv4SubnetMask"
- "_is256Bit"
- "_outgoingEncryptionSalt"
- "_outgoingHMACBaseContext"
- "_receivedReplies"
- "_receivedRequests"
- "_requestType"
- "_sentRequests"
- "a"
- "constructEncryptedPacketFromPayloadData:authenticatedHeaders:"
- "copyShortDescription"
- "copyTypeDescription"
- "createIdentifierWithType:data:"
- "createIdentifierWithType:data:zone:"
- "dataWithData:"
- "initWithRequestType:"
- "parsePayloadData"
- "pfkey_send_x1: calculated message length (%lu) is less than final message len (%lu)"
- "refreshConfigForced:"
- "sensitiveDataWithBytes:length:%zu failed"
- "separateDomainsFromFQDNs:domains:fqdns:"
- "setIdentifierData:"
- "timeIntervalSinceNow"
- "v40@0:8@16^@24^@32"

```
