## idcredd

> `/usr/libexec/idcredd`

```diff

-8.36.2.0.0
-  __TEXT.__text: 0x185d14
-  __TEXT.__auth_stubs: 0x3bd0
+8.38.3.0.0
+  __TEXT.__text: 0x1878bc
+  __TEXT.__auth_stubs: 0x3bf0
   __TEXT.__objc_methlist: 0x8b4
-  __TEXT.__const: 0x46c4
-  __TEXT.__cstring: 0xd412
-  __TEXT.__constg_swiftt: 0x2184
-  __TEXT.__swift5_typeref: 0x245c
+  __TEXT.__const: 0x4700
+  __TEXT.__cstring: 0xd499
+  __TEXT.__constg_swiftt: 0x21b4
+  __TEXT.__swift5_typeref: 0x2496
+  __TEXT.__swift5_reflstr: 0x16e7
+  __TEXT.__swift5_fieldmd: 0x1624
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x16ad
-  __TEXT.__swift5_fieldmd: 0x15d8
   __TEXT.__swift5_assocty: 0x1c8
+  __TEXT.__swift5_capture: 0x1e94
+  __TEXT.__objc_methname: 0x24e9
+  __TEXT.__oslogstring: 0x9ce8
   __TEXT.__swift5_proto: 0x144
-  __TEXT.__swift5_types: 0x1d4
+  __TEXT.__swift5_types: 0x1d8
   __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0x24cf
   __TEXT.__objc_methtype: 0xa90
-  __TEXT.__swift5_capture: 0x1e94
-  __TEXT.__oslogstring: 0x9c55
-  __TEXT.__swift_as_entry: 0x5d0
-  __TEXT.__swift_as_ret: 0x6d8
+  __TEXT.__swift_as_entry: 0x5d4
+  __TEXT.__swift_as_ret: 0x6dc
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x5018
-  __TEXT.__eh_frame: 0x12a88
-  __DATA_CONST.__auth_got: 0x1de8
-  __DATA_CONST.__got: 0x13a8
-  __DATA_CONST.__auth_ptr: 0x9b8
-  __DATA_CONST.__const: 0x56f8
+  __TEXT.__unwind_info: 0x5028
+  __TEXT.__eh_frame: 0x12b50
+  __DATA_CONST.__auth_got: 0x1df8
+  __DATA_CONST.__got: 0x13b0
+  __DATA_CONST.__auth_ptr: 0x9a8
+  __DATA_CONST.__const: 0x5720
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x27c8
   __DATA.__objc_selrefs: 0xa50
   __DATA.__objc_data: 0xcb0
-  __DATA.__data: 0x3f20
+  __DATA.__data: 0x3fe8
   __DATA.__bss: 0x1cc0
   __DATA.__common: 0xf0
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5CBC9AEC-4049-30E0-80D5-43EB57B08773
-  Functions: 3806
-  Symbols:   1732
-  CStrings:  2044
+  UUID: FE963564-BD4E-330B-83F5-A4624E2201F5
+  Functions: 3815
+  Symbols:   1735
+  CStrings:  2048
 
Symbols:
+ _$s13CoreIDVShared12DIPCertUsageO14webPresentmentyACSS_tcACmFWC
+ _$s13CoreIDVShared12DIPCertUsageO23webPresentmentNoNetworkyACSS_tcACmFWC
+ _$s13CoreIDVShared16AppleIDVManagingP19validatePrearmTrust14baaCertificate18protectedPublicKeyy10Foundation4DataV_AISgtKFTj
+ _$s13CoreIDVShared21ISO18013KnownDocTypesO8allCasesSayACGvgZ
+ _$s13CoreIDVShared28ISO18013MobileSecurityObjectV14IdentifierListV11certificate10Foundation4DataVSgvg
+ _$s13CoreIDVShared28ISO18013MobileSecurityObjectV14IdentifierListV2id11certificate3uriAE10Foundation4DataV_AKSgSStcfC
+ _$s13CoreIDVShared8DIPErrorV4CodeO30hostNameMismatchForCertificateyA2EmFWC
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
- _$s13CoreIDVShared12DIPCertUsageO14webPresentmentyA2CmFWC
- _$s13CoreIDVShared12DIPCertUsageO23webPresentmentNoNetworkyA2CmFWC
- _$s13CoreIDVShared28ISO18013MobileSecurityObjectV14IdentifierListV11certificate10Foundation4DataVvg
- _$s13CoreIDVShared28ISO18013MobileSecurityObjectV14IdentifierListV2id11certificate3uriAE10Foundation4DataV_AKSStcfC
- _objc_release_x9
CStrings:
+ "CredentialStorage foring presentment key generation failure"
+ "Failed presentment key due to internal setting"
+ "Overriding relying party identifier %s with %s"
+ "Request origin host validation log only, allowing invalid certificate chain %s"
+ "Request origin host validation log only, permitting host name mismatch for readerCerts %s"
+ "certUsages(documentTypes:requestType:)"
+ "debug.force-presentment-key-generation-error"
+ "debug.web-presentment.override-originating-url"
+ "debug.web-presentment.request-origin-host-validation-log-only"
+ "establishPrearmTrust -\n\nexisting trust       : %s\n\nexisting attestation : %s\n\naccessibilityEnabled : %{bool}d"
+ "establishPrearmTrust - returning attestations %s"
+ "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:issuerSignerCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:"
+ "interpretCredentialRequest(useCases:readerAuthResult:requiredPublicKeyIdentifier:sessionTranscript:)"
+ "issuerCertificateChain"
+ "setIssuerCertificateChain:"
- "StoredPayload missing identifier revocation list certificate; excluding from payload contents"
- "Unexpected presentmentType "
- "authorityKeyIdentifiers"
- "certUsages(documentTypes:presentmentType:)"
- "establishPrearmTrust - AX returning attestation of existing progenitor key"
- "establishPrearmTrust - existing public key = %s"
- "establishPrearmTrust - returning attestation of existing trust and progenitor key"
- "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:"
- "interpretCredentialRequest(useCases:readerAuthResult:readerAuthError:requiredPublicKeyIdentifier:sessionTranscript:)"
- "missing stored certificate"
- "setAuthorityKeyIdentifiers:"

```
