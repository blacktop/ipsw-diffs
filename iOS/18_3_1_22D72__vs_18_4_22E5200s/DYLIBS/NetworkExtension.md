## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2063.80.10.0.0
-  __TEXT.__text: 0x1c0ea0
-  __TEXT.__auth_stubs: 0x3c40
-  __TEXT.__objc_methlist: 0xd51c
-  __TEXT.__cstring: 0x17350
+2063.100.25.0.0
+  __TEXT.__text: 0x1c1500
+  __TEXT.__auth_stubs: 0x3c00
+  __TEXT.__objc_methlist: 0xe464
+  __TEXT.__const: 0x2538
+  __TEXT.__cstring: 0x174af
   __TEXT.__swift5_typeref: 0x332
-  __TEXT.__const: 0x2418
   __TEXT.__constg_swiftt: 0x540
   __TEXT.__swift5_reflstr: 0xa4
   __TEXT.__swift5_fieldmd: 0x228

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x140
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x5404
-  __TEXT.__oslogstring: 0x1f8b0
-  __TEXT.__unwind_info: 0x4500
+  __TEXT.__gcc_except_tab: 0x5474
+  __TEXT.__oslogstring: 0x1f99b
+  __TEXT.__unwind_info: 0x4400
   __TEXT.__eh_frame: 0x598
-  __TEXT.__objc_classname: 0x23b3
-  __TEXT.__objc_methname: 0x1901e
-  __TEXT.__objc_methtype: 0x34fc
-  __TEXT.__objc_stubs: 0xf3a0
-  __DATA_CONST.__got: 0x1578
-  __DATA_CONST.__const: 0x5458
-  __DATA_CONST.__objc_classlist: 0xa58
+  __TEXT.__objc_classname: 0x23d6
+  __TEXT.__objc_methname: 0x19102
+  __TEXT.__objc_methtype: 0x34f1
+  __TEXT.__objc_stubs: 0xf460
+  __DATA_CONST.__got: 0x1558
+  __DATA_CONST.__const: 0x5590
+  __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b80
+  __DATA_CONST.__objc_selrefs: 0x4c80
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x6e8
+  __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x1e30
-  __AUTH_CONST.__auth_ptr: 0x168
+  __AUTH_CONST.__auth_got: 0x1e10
+  __AUTH_CONST.__auth_ptr: 0x188
   __AUTH_CONST.__const: 0x15a8
-  __AUTH_CONST.__cfstring: 0x16fe0
-  __AUTH_CONST.__objc_const: 0x21f40
+  __AUTH_CONST.__cfstring: 0x17120
+  __AUTH_CONST.__objc_const: 0x206b8
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xda0
+  __AUTH.__objc_data: 0xdf0
   __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x1a50
+  __DATA.__objc_ivar: 0x1a5c
   __DATA.__data: 0x1a50
-  __DATA.__common: 0x168
   __DATA.__bss: 0xad0
+  __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x6040
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0xf0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6587
-  Symbols:   8613
-  CStrings:  11996
+  Functions: 6530
+  Symbols:   8653
+  CStrings:  12022
 
Symbols:
+ _CCHmacInit
+ _OBJC_CLASS_$_NENetworkAgentSessionFileHandle
+ _OBJC_METACLASS_$_NENetworkAgentSessionFileHandle
+ _cc_clear
+ _kNEExcludedFQDNsPayloadKey
+ _kNEMatchFQDNsPayloadKey
+ _oidQCCompliance
+ _oidQCDisclosures
+ _oidQCEuRetentionPeriod
+ _oidQCLimitValue
+ _oidQCStatements
+ _oidQCSyntaxv1
+ _oidQCSyntaxv2
+ _oidQCType
+ _oidQCTypeEseal
+ _oidQCTypeEsign
+ _oidQCTypeWeb
+ _oidSemanticsIdEidasLegal
+ _oidSemanticsIdEidasNatural
+ _oidSemanticsIdLegal
+ _oidSemanticsIdNatural
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _CCHmac
- _CCHmacClone
- _CCHmacCreate
- _CCHmacDestroy
- _CCHmacOutputSizeFromRef
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "\x01#"
+ "%s called with null dataVector"
+ "%s called with null packet.authenticatedDataVector"
+ "%s called with null remoteSignedOctetVector"
+ "%s called with null self.gspmHandler.sessionKey"
+ "%s%s:%s "
+ "+[NEIKEv2Crypto createHMACFromDataVector:key:prfProtocol:]"
+ "+[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octetVector:prfProtocol:]"
+ "-[NEIKEv2GSPM createLocalSignedOctetVector]"
+ "-[NEIKEv2GSPM createRemoteSignedOctetVector]"
+ "-[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octetVector:]"
+ "-[NEIKEv2IKESA(Crypto) createInitiatorSignedOctetVectorUsingPrimeKey:]"
+ "-[NEIKEv2IKESA(Crypto) createIntAuthOctetVector]"
+ "-[NEIKEv2IKESA(Crypto) createResponderSignedOctetVectorUsingPrimeKey:]"
+ "-[NEIKEv2IntermediatePacket authenticatedDataVector]"
+ "ExcludedFQDNs"
+ "Failed to create responder identifier payload for GSPM"
+ "Failed to get Initiator ID data for %@"
+ "Failed to get Responder ID data for %@"
+ "Invalid DoH hostname"
+ "Invalid excluded FQDN"
+ "Invalid match FQDN"
+ "MatchFQDNs"
+ "NENetworkAgentSessionFileHandle"
+ "Network Agent Session socket (%d) %@"
+ "T@\"NSArray\",C,V_excludedFQDNs"
+ "T@\"NSArray\",C,V_matchFQDNs"
+ "Unnecessary excludes when matching only FQDNs"
+ "[NEIKEv2Crypto createHMACFromDataVector:key:prfProtocol:] failed"
+ "[NEIKEv2Crypto createIntAuthOctetVector] failed"
+ "[self createLocalSignedOctetVectorUsingPrimeKey:] failed"
+ "[self createRemoteSignedOctetVectorUsingPrimeKey:] failed"
+ "_authenticatedDataVector"
+ "_excludedFQDNs"
+ "_matchFQDNs"
+ "createInitiatorSignedOctetVector(GSPM) failed"
+ "createInitiatorSignedOctetVectorUsingPrimeKey failed"
+ "createInitiatorSignedOctetVectorUsingPrimeKey: failed"
+ "createResponderSignedOctetVector(GSPM) failed"
+ "createResponderSignedOctetVectorUsingPrimeKey failed"
+ "createResponderSignedOctetVectorUsingPrimeKey: failed"
+ "dupSessionFileDescriptor"
+ "excludedFQDNs"
+ "fqdn"
+ "initWithNetworkAgentSession:"
+ "initWithNetworkAgentSession:name:"
+ "matchFQDNs"
+ "sensitiveDataWithBytes:length:%zu failed"
+ "setExcludedFQDNs:"
+ "setMatchFQDNs:"
- "%s called with null packet.authenticatedData"
- "%s called with null self.gspmHandler"
- "%sdomain:%s "
- "+[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octets:prfProtocol:]"
- "-[NEIKEv2GSPM createLocalSignedOctets]"
- "-[NEIKEv2GSPM createRemoteSignedOctets]"
- "-[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octets:]"
- "-[NEIKEv2IKESA(Crypto) createInitiatorSignedOctetsUsingPrimeKey:]"
- "-[NEIKEv2IKESA(Crypto) createIntAuthOctets]"
- "-[NEIKEv2IKESA(Crypto) createResponderSignedOctetsUsingPrimeKey:]"
- "-[NEIKEv2IntermediatePacket authenticatedData]"
- "CCHmacClone failed"
- "CCHmacCreate failed"
- "GSPM.sessionKey failed"
- "PRF length %u != HMAC output size %zu"
- "[NEIKEv2Crypto createIntAuthOctets] failed"
- "[NESensitiveData mutableSensitiveDataWithMaxCapacity:%zu] failed"
- "[self createRemoteSignedOctetsUsingPrimeKey:] failed"
- "^{?=[96I]}"
- "_internalAuthenticatedData"
- "creatInitiatorSignedOctets(GSPM) failed"
- "createInitiatorSignedOctets failed"
- "createInitiatorSignedOctetsUsingPrimeKey: failed"
- "createResponderSignedOctets failed"
- "createResponderSignedOctets(GSPM) failed"
- "createResponderSignedOctetsUsingPrimeKey: failed"

```
