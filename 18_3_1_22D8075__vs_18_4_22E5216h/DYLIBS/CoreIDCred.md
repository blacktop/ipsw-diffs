## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-7.300.0.0.0
-  __TEXT.__text: 0x1b418
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x19d4
+7.418.0.0.0
+  __TEXT.__text: 0x1c934
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x1fa4
   __TEXT.__const: 0x8a
-  __TEXT.__cstring: 0x18d2
-  __TEXT.__oslogstring: 0x3994
+  __TEXT.__cstring: 0x1972
+  __TEXT.__oslogstring: 0x3b81
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x818
-  __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methname: 0x390a
-  __TEXT.__objc_methtype: 0xf4e
-  __TEXT.__objc_stubs: 0x1920
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x9c0
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__unwind_info: 0x820
+  __TEXT.__objc_classname: 0x336
+  __TEXT.__objc_methname: 0x3ca4
+  __TEXT.__objc_methtype: 0xfca
+  __TEXT.__objc_stubs: 0x1a00
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x9f0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa40
+  __DATA_CONST.__objc_selrefs: 0xb40
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1940
-  __AUTH_CONST.__objc_const: 0x3db0
-  __DATA.__objc_ivar: 0x258
+  __AUTH_CONST.__cfstring: 0x1a00
+  __AUTH_CONST.__objc_const: 0x37d0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x27c
   __DATA.__data: 0x300
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 981
-  Symbols:   1136
-  CStrings:  1181
+  Functions: 1028
+  Symbols:   1186
+  CStrings:  1228
 
Symbols:
+ _DCCredentialDeviceEncryptionKeyTypeToString
+ _OBJC_CLASS_$_DCCredentialRevocationInfo
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_METACLASS_$_DCCredentialRevocationInfo
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x03"
+ "\r"
+ "\x12\x1b\x14"
+ "+"
+ "<%@ %p; credentialIdentifier = %@; presentmentKeyIdentifier = %@; partition = %@; docType = %@; elements = %@; readerMetadata = %@; readerAnalytics = %@; region = %@; issuingJurisdiction = %@, credentialRevocationInfo = %@>"
+ "@\"DCCredentialRevocationInfo\""
+ "@\"NSDateComponents\""
+ "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
+ "@88@0:8@16@24@32@40@48@56@64@72Q80"
+ "DCCredentialElement identifier = %@; birthDate value = %@"
+ "DCCredentialRevocationInfo"
+ "DCCredentialStore generateDeviceEncryptionKeyForCredential keyType = %@"
+ "DCPresentmentClient buildGenericDataResponse"
+ "DCPresentmentClient buildGenericDataResponse returned successfully"
+ "DCPresentmentClient buildGenericDataResponse returned with error %{public}@"
+ "DCPresentmentClient interpretGenericDataRequest"
+ "DCPresentmentClient interpretGenericDataRequest returned successfully"
+ "DCPresentmentClient interpretGenericDataRequest returned with error %{public}@"
+ "DCPresentmentSession buildGenericDataResponse"
+ "DCPresentmentSession interpretGenericDataRequest"
+ "T@\"DCCredentialRevocationInfo\",&,N"
+ "T@\"DCCredentialRevocationInfo\",&,N,V_credentialRevocationInfo"
+ "T@\"DCCredentialRevocationInfo\",R,N,V_credentialRevocationInfo"
+ "T@\"NSData\",R,N,V_certificate"
+ "T@\"NSData\",R,N,V_identifier"
+ "T@\"NSDate\",&,N,V_signedAt"
+ "T@\"NSDateComponents\",R,N,V_birthDateValue"
+ "T@\"NSURL\",R,N,V_URL"
+ "URL"
+ "_URL"
+ "_birthDateValue"
+ "_certificate"
+ "_credentialRevocationInfo"
+ "_payloadSignedAt"
+ "_signedAt"
+ "birthDateValue"
+ "buildGenericDataResponse:completion:"
+ "certificate"
+ "credentialRevocationInfo"
+ "generateDeviceEncryptionKeyForCredential:keyType:completion:"
+ "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:"
+ "initWithElementIdentifier:birthDateValue:"
+ "initWithElementIdentifier:stringValue:dataValue:dateValue:birthDateValue:numberValue:arrayValue:dictionaryValue:numericTypeHint:"
+ "initWithIdentifier:certificate:URL:"
+ "initWithIdentifier:publicKey:publicKeyIdentifier:publicKeyCOSEKey:keyType:keyUsage:casdAttestation:keyAuthorization:kskAttestation:"
+ "interpretGenericDataRequest:completion:"
+ "payloadSignedAt"
+ "setCredentialRevocationInfo:"
+ "setPayloadSignedAt:"
+ "setSignedAt:"
+ "signedAt"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"DCCredentialCryptoKey\"@\"NSError\">32"
- "\a"
- "\f"
- "\x12\x1a\x13"
- ")"
- "<%@ %p; credentialIdentifier = %@; presentmentKeyIdentifier = %@; partition = %@; docType = %@; elements = %@; readerMetadata = %@; readerAnalytics = %@; region = %@; issuingJurisdiction = %@>"
- "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "@80@0:8@16@24@32@40@48@56@64Q72"
- "DCCredentialStore generateDeviceEncryptionKeyForCredential"
- "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:"
- "initWithElementIdentifier:stringValue:dataValue:dateValue:numberValue:arrayValue:dictionaryValue:numericTypeHint:"
- "kElementIdentifiersByNamespace"
- "kValidFrom"
- "kValidUntil"

```
