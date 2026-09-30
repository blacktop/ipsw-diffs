## terminusd

> `/usr/libexec/terminusd`

```diff

-563.40.6.0.0
-  __TEXT.__text: 0x157208
-  __TEXT.__auth_stubs: 0x26d0
-  __TEXT.__objc_stubs: 0x7e00
-  __TEXT.__objc_methlist: 0x45a4
-  __TEXT.__const: 0x268
-  __TEXT.__gcc_except_tab: 0x3824
-  __TEXT.__objc_methname: 0x1041d
-  __TEXT.__cstring: 0x3a93a
+563.60.13.0.0
+  __TEXT.__text: 0x159764
+  __TEXT.__auth_stubs: 0x27c0
+  __TEXT.__objc_stubs: 0x7e60
+  __TEXT.__objc_methlist: 0x460c
+  __TEXT.__const: 0x25c
+  __TEXT.__gcc_except_tab: 0x3864
+  __TEXT.__objc_methname: 0x10517
+  __TEXT.__cstring: 0x3aefa
   __TEXT.__oslogstring: 0x24e1
-  __TEXT.__objc_classname: 0xdbc
+  __TEXT.__objc_classname: 0xdcd
   __TEXT.__objc_methtype: 0x30a5
-  __TEXT.__unwind_info: 0x2150
-  __DATA_CONST.__auth_got: 0x1378
-  __DATA_CONST.__got: 0x958
+  __TEXT.__unwind_info: 0x2168
+  __DATA_CONST.__auth_got: 0x13f0
+  __DATA_CONST.__got: 0x968
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2e88
-  __DATA_CONST.__cfstring: 0xb2e0
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __DATA_CONST.__const: 0x2ea8
+  __DATA_CONST.__cfstring: 0xb3a0
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_intobj: 0x510
-  __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x15218
-  __DATA.__objc_selrefs: 0x26f0
-  __DATA.__objc_ivar: 0x1868
-  __DATA.__objc_data: 0x27b0
+  __DATA.__objc_const: 0x15448
+  __DATA.__objc_selrefs: 0x2718
+  __DATA.__objc_ivar: 0x1898
+  __DATA.__objc_data: 0x2800
   __DATA.__data: 0xbc8
   __DATA.__bss: 0x670
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2944
-  Symbols:   931
-  CStrings:  9314
+  Functions: 2957
+  Symbols:   950
+  CStrings:  9367
 
Symbols:
+ OBJC_IVAR_$_PBDataReader._bytes
+ OBJC_IVAR_$_PBDataReader._error
+ OBJC_IVAR_$_PBDataReader._length
+ OBJC_IVAR_$_PBDataReader._pos
+ _CFDataGetTypeID
+ _OBJC_CLASS_$_PBCodable
+ _OBJC_METACLASS_$_PBCodable
+ _PBDataWriterWriteDataField
+ _PBDataWriterWriteStringField
+ _PBReaderReadData
+ _PBReaderReadString
+ _PBReaderSkipValueWithTag
+ ___NSArray0__struct
+ _kSecAttrLabel
+ _kSecClassIdentity
+ _kSecReturnPersistentRef
+ _nrXPCEntitlementIdentityProxy
+ _nrXPCKeyIdentityProxyReferences
+ _nw_connection_group_copy_parameters
+ _nw_masque_server_copy_connection_group_with_identifier
+ _nw_parameters_copy_protocol_options_for_definition
+ _nw_protocol_copy_quic_stream_definition
+ _nw_proxy_hop_set_client_identity_is_raw_public_key
+ _nw_proxy_hop_set_client_identity_reference
+ _nw_quic_connection_set_sec_protocol_options
+ _nw_quic_copy_sec_protocol_options
+ _nw_quic_stream_copy_shared_connection_options
+ _sec_identity_copy_ref
+ _sec_protocol_options_set_client_raw_public_key_certificates
- _SecCertificateCopyKey
- _kSecCertificateExtensionsEncoded
- _kSecCertificateKeyUsage
- _kSecOidCommonName
- _kSecOidCountryName
- _kSecOidOrganization
- _kSecOidOrganizationalUnit
- _kSecSubjectAltName
- _kSecSubjectAltNameDNSName
- _sec_identity_copy_certificates_ref
CStrings:
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Adding local identity %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) AppVPN agent %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Client %!@(MISSING) trying to resolve identity proxy"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Decoded protobuf: %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Deleting local identity %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Encoded protobuf: %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to add identity to keychain %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to add local identity: keychain locked"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to decode NAN service info protobuf"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to delete local identity: item not found (not an error)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to delete local identity: keychain locked"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to encode NAN service info protobuf %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Failed to start MASQUE server without local identity"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Fetched %!u(MISSING) identities"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Found a device over NAN"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) No auth tag %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) No fetched identities (%!@(MISSING))"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) No service name %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Successfully added identity to keychain %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Successfully added local identity %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) Successfully deleted local identity"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) adding VPN route-rule(s) %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) generated local identity SPKI: %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) no QUIC options"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) no QUIC sec options"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) proxy client connection received (id: %!l(MISSING)lu)"
+ "%!s(MISSING)%!s(MISSING):%!d(MISSING) sending response %!@(MISSING)"
+ "-[NRDKeyManager deleteEphemeralLocalIdentityFromKeychain]"
+ "-[NRDKeyManager saveEphemeralLocalIdentityToKeychain:persistentReference:]"
+ "-[NRLinkDirector generateLocalIdentityIfNeeded:]"
+ "-[NRLinkDirector removeVPNWatcher]"
+ "-[NRLinkDirector updateVPNPolicies]"
+ "13:42:39"
+ "563.60.13"
+ "Availability"
+ "CmpLnkAvailability"
+ "Failed to add local identity: %!d(MISSING)"
+ "Failed to create local identity"
+ "Failed to delete local identity: %!d(MISSING)"
+ "LowLatencyTetheringAvailability"
+ "NRCreateLocalIdentity"
+ "NRNANServiceInfo"
+ "O\r*"
+ "Oct 16 2024"
+ "SecKeyCopySubjectPublicKeyInfo failed"
+ "TLSIdentitySPKI"
+ "TetheringAvailability"
+ "_CFXPCCreateXPCObjectFromCFObject failed"
+ "_advertisingNonce"
+ "_authTag"
+ "_availabilityAgent"
+ "_availabilityAgentPolicyIdentifier"
+ "_availabilityAgentType"
+ "_deviceTypeHash"
+ "_nrUUIDToSPKIs"
+ "_persistentCertificateReference"
+ "_persistentIdentityReference"
+ "_persistentKeyReference"
+ "_spkiForLocalIdentity"
+ "_vpnProviderUUIDs"
+ "advertisingNonce"
+ "authTag"
+ "cert-ref"
+ "com.apple.networkrelay.referencesChanged"
+ "com.apple.terminusd.local-identity"
+ "copyProviderMachOUUIDs"
+ "deviceTypeHash"
+ "dictionaryRepresentation"
+ "excludeVPNClients"
+ "failed to copy connection group (id: %!l(MISSING)lu)"
+ "handleIdentityProxyResolutionRequest"
+ "id-ref"
+ "key-ref"
+ "local-identity"
+ "readFrom:"
+ "sec_identity_copy_ref failed"
+ "setObject:forKey:"
+ "writeTo:"
+ "\xbf\"\x11\x16T%!\(MISSING)x15\x1b*"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) Generated MASQUE TLS identity: %!@(MISSING)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) Generated MASQUE spki: %!@(MISSING)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) adding appVPN route-rule(s) %!@(MISSING)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) detected AppVPN agent %!@(MISSING)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) failed to archive publish dictionary %!@(MISSING)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) found a device over NAN"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) no AppVPN agent found"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) no service name %!@(MISSING)"
- "%!s(MISSING)%!s(MISSING):%!d(MISSING) unarchive error %!@(MISSING)"
- "-[NRLinkDirector copyServerIdentity:publicKey:]"
- "-[NRLinkDirector generateMASQUEProxyServerKeysIfNeeded]"
- "-[NRLinkDirector removeAppVPNWatcher]"
- "-[NRLinkDirector setupAppVPNPolicies]"
- "00:18:43"
- "2.5.29.37"
- "563.40.6"
- "Apple Inc."
- "NetworkRelay.framework"
- "O\v'"
- "Sep 29 2024"
- "US"
- "_spkiMASQUEProxyServer"
- "_tlsIdentityMASQUEProxyServer"
- "arrayWithObject:"
- "nrSN"
- "propertyListWithData:options:format:error:"
- "\xbf\"\x11\x16T%!\(MISSING)x15\x1b'"

```
