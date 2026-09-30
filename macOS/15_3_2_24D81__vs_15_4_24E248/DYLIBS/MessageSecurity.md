## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/Versions/A/MessageSecurity`

```diff

-115.80.1.0.0
-  __TEXT.__text: 0x3fabc
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x1b00
+115.100.9.0.0
+  __TEXT.__text: 0x41460
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x1ce4
   __TEXT.__const: 0xd64
-  __TEXT.__gcc_except_tab: 0x818
-  __TEXT.__cstring: 0x360d
-  __TEXT.__oslogstring: 0xa5c
+  __TEXT.__gcc_except_tab: 0x824
+  __TEXT.__cstring: 0x352d
+  __TEXT.__oslogstring: 0xabc
   __TEXT.__swift5_typeref: 0x2a8
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x3f0

   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x1040
-  __TEXT.__eh_frame: 0x958
+  __TEXT.__unwind_info: 0x10a0
+  __TEXT.__eh_frame: 0x9f0
   __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x3f91
-  __TEXT.__objc_methtype: 0x1726
+  __TEXT.__objc_methname: 0x400f
+  __TEXT.__objc_methtype: 0x1791
   __TEXT.__objc_stubs: 0x2800
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x3fc8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf0
+  __DATA_CONST.__objc_selrefs: 0xe90
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x720
-  __AUTH_CONST.__const: 0x1a60
+  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__const: 0x1a80
   __AUTH_CONST.__cfstring: 0x24a0
-  __AUTH_CONST.__objc_const: 0x4230
+  __AUTH_CONST.__objc_const: 0x3ee8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xb10
   __AUTH.__data: 0xa0
   __DATA.__objc_ivar: 0x1ac
-  __DATA.__data: 0x1168
+  __DATA.__data: 0x1160
   __DATA.__bss: 0x5d0
   __DATA.__common: 0x2721
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AE9B5751-647E-3331-A3D0-6034D16A7B5F
-  Functions: 1948
-  Symbols:   3502
-  CStrings:  1573
+  UUID: DC4177B9-973D-3459-B882-9BEF2F520691
+  Functions: 2060
+  Symbols:   3638
+  CStrings:  1572
 
Symbols:
+ +[MSCMSIdentifier decodeIdentifier:error:].cold.1
+ +[MSCMSIdentifier decodeIdentifier:error:].cold.2
+ +[MSCMSIdentifier decodeIdentifier:error:].cold.3
+ +[MSCMSRecipientInfo decodeKeyAgreeRecipientInfo:certificates:LAContext:error:].cold.1
+ +[MSCMSRecipientInfo decodeKeyAgreeRecipientInfo:certificates:LAContext:error:].cold.2
+ +[MSCMSRecipientInfo decodeKeyAgreeRecipientInfo:certificates:LAContext:error:].cold.3
+ +[MSCMSRecipientInfo decodeKeyAgreeRecipientInfo:certificates:LAContext:error:].cold.4
+ +[MSCMSRecipientInfo decodeKeyTransRecipientInfo:certificates:LAContext:error:].cold.1
+ +[MSCMSRecipientInfo decodeKeyTransRecipientInfo:certificates:LAContext:error:].cold.2
+ +[MSCMSRecipientInfo decodeKeyTransRecipientInfo:certificates:LAContext:error:].cold.3
+ +[MSCMSSignedData decodeMessageSecurityObject:options:error:].cold.1
+ +[MSCMSSignedData decodeMessageSecurityObject:options:error:].cold.2
+ +[MSCMSSignedData decodeMessageSecurityObject:options:error:].cold.3
+ +[MSCMSSignedData decodeMessageSecurityObject:options:error:].cold.4
+ +[MSCMSSignedData decodeMessageSecurityObject:options:error:].cold.5
+ -[MSAlgorithmIdentifier blockSize:].cold.1
+ -[MSAlgorithmIdentifier ccAlgorithm:].cold.1
+ -[MSAlgorithmIdentifier ccMode:].cold.1
+ -[MSAlgorithmIdentifier initWithOID:].cold.1
+ -[MSAlgorithmIdentifier keySize:].cold.1
+ -[MSCMSContentInfo encodeMessageSecurityObject:].cold.1
+ -[MSCMSContentTypeAttribute initWithOID:].cold.1
+ -[MSCMSContentTypeAttribute initWithOID:].cold.2
+ -[MSCMSCounterSignerInfo verifyContentTypeAttribute:].cold.1
+ -[MSCMSEncryptionKeyPreferenceAttribute initWithAttribute:certificates:LAContext:error:].cold.1
+ -[MSCMSEncryptionKeyPreferenceAttribute initWithAttribute:certificates:LAContext:error:].cold.2
+ -[MSCMSEncryptionKeyPreferenceAttribute initWithAttribute:certificates:LAContext:error:].cold.3
+ -[MSCMSEnvelopedData addRecipient:].cold.1
+ -[MSCMSEnvelopedData encodeEncryptionParameters:].cold.1
+ -[MSCMSEnvelopedData encryptDecryptContent:ccOperation:error:].cold.1
+ -[MSCMSEnvelopedData encryptDecryptContent:ccOperation:error:].cold.2
+ -[MSCMSEnvelopedData encryptDecryptContent:ccOperation:error:].cold.3
+ -[MSCMSIdentifier encodeMessageSecurityObject:].cold.1
+ -[MSCMSIdentifier encodeMessageSecurityObject:].cold.2
+ -[MSCMSMessageDigestAttribute initWithDigest:].cold.1
+ -[MSCMSMutableAttributeArray calculateAttributesWithDigest:error:].cold.1
+ -[MSCMSRecipientInfo encodeKeyAgreeRecipientInfo:recipientInfo:error:].cold.1
+ -[MSCMSRecipientInfo encodeKeyTransRecipientInfo:recipientInfo:error:].cold.1
+ -[MSCMSRecipientInfo initWithCertificate:algorithmCapabilities:originator:]
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:].cold.1
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:].cold.2
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:].cold.3
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:].cold.4
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:].cold.5
+ -[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:].cold.6
+ -[MSCMSSignedData addCertificatesForSigner:mode:error:].cold.1
+ -[MSCMSSignedData addCertificatesForSigner:mode:error:].cold.2
+ -[MSCMSSignedData addCertificatesForSigner:mode:error:].cold.3
+ -[MSCMSSignedData addCertificatesForSigner:mode:error:].cold.4
+ -[MSCMSSignedData addCertificatesForSigner:mode:error:].cold.5
+ -[MSCMSSignedData checkSignedPerRFC5652:].cold.1
+ -[MSCMSSignerInfo calculateSignedAttributesDigest:].cold.1
+ -[MSCMSSignerInfo calculateSignedAttributesDigest:].cold.2
+ -[MSCMSSignerInfo createRequiredAttributes:].cold.1
+ -[MSCMSSignerInfo createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:].cold.1
+ -[MSCMSSignerInfo createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:].cold.2
+ -[MSCMSSignerInfo createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:].cold.3
+ -[MSCMSSignerInfo encodeSignerInfo:error:].cold.1
+ -[MSCMSSignerInfo encodeSignerInfo:error:].cold.2
+ -[MSCMSSignerInfo encodeSignerInfo:error:].cold.3
+ -[MSCMSSignerInfo encodeSignerInfo:error:].cold.4
+ -[MSCMSSignerInfo encodeSignerInfo:error:].cold.5
+ -[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:].cold.1
+ -[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:].cold.2
+ -[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:].cold.3
+ -[MSCMSSignerInfo sign:].cold.1
+ -[MSCMSSignerInfo sign:].cold.2
+ -[MSCMSSignerInfo sign:].cold.3
+ -[MSCMSSignerInfo sign:].cold.4
+ -[MSCMSSignerInfo sign:].cold.5
+ -[MSCMSSignerInfo sign:].cold.6
+ -[MSCMSSignerInfo sign:].cold.7
+ -[MSCMSSignerInfo verifyCountersignatures:].cold.1
+ -[MSCMSSignerInfo verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:].cold.1
+ -[MSCMSSignerInfo verifySignature:].cold.1
+ -[MSCMSSignerInfo verifySignature:].cold.2
+ -[MSCMSSignerInfo verifySignature:].cold.3
+ -[MSCMSSignerInfo verifySignature:].cold.4
+ -[MSCMSSignerInfo verifySignature:].cold.5
+ -[MSCMSSignerInfo verifyTimestamps:error:].cold.1
+ -[MSCMSTimestampAttribute initWithTimestampToken:].cold.1
+ -[MSOID initDigestOIDWithSignatureAlgorithm:error:].cold.1
+ -[MSOID initECSignatureOIDWithDigestAlgorithm:error:].cold.1
+ -[MSOID initRSASignatureOIDWithDigestAlgorithm:error:].cold.1
+ -[MSOID initSignatureOIDWithSecKeyAlgorithm:error:].cold.1
+ -[MSOID secKeyAlgorithm].cold.1
+ MSDecryptGCMOneShot.cold.1
+ _MSLog.cold.1
+ _MSLog.cold.2
+ _MSLog.cold.3
+ _MSLog.cold.4
+ _MSLog.cold.5
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __102-[MSCMSCountersignatureAttribute initWithAttribute:certificates:LAContext:containingSignerInfo:error:]_block_invoke.cold.1
+ __133-[MSCMSCountersignatureAttribute verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:signature:error:]_block_invoke.cold.1
+ __41-[MSCMSSignedData checkSignedPerRFC5652:]_block_invoke.cold.1
+ __59-[MSCMSCountersignatureAttribute encodeAttributeWithError:]_block_invoke.cold.1
+ __59-[MSCMSCountersignatureAttribute encodeAttributeWithError:]_block_invoke.cold.2
+ __93-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]_block_invoke.13
+ __93-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]_block_invoke.30
+ __93-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]_block_invoke.9
+ __93-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]_block_invoke_2.16
+ ___93-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]_block_invoke
+ ___93-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]_block_invoke_2
+ __block_literal_global.18
+ __block_literal_global.32
+ _objc_msgSend$initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:
+ dumpNSData.cold.1
+ dumpNSData.cold.2
+ findBestMutuallySupportedEncryptionAlgorithm.cold.1
+ findBestMutuallySupportedKeyEncryptionAlgorithm.cold.1
+ findBestMutuallySupportedSignatureAlgorithm.cold.1
+ findBestMutuallySupportedSignatureAlgorithm.cold.2
+ findCertificateByEmailAddress.cold.1
+ findCertificateByEmailAddress.cold.2
+ findCertificateByEmailAddress.cold.3
+ findCertificateByIssuerAndSerialNumber.cold.1
+ findCertificateByIssuerAndSerialNumber.cold.2
+ findCertificateByIssuerAndSerialNumber.cold.3
+ findCertificateByIssuerAndSerialNumber.cold.4
+ findCertificateBySubjectKeyID.cold.1
+ findCertificateBySubjectKeyID.cold.2
+ initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:.onceToken
+ initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:.onceToken.12
+ initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:.sAllowedECEncAlgs
+ initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:.sAllowedRSAEncAlgs
- __82-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]_block_invoke.10
- __82-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]_block_invoke.27
- __82-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]_block_invoke_2.13
- ___82-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]_block_invoke
- ___82-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]_block_invoke_2
- __block_literal_global.12
- __block_literal_global.29
- _objc_msgSend$initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:
- initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:.onceToken
- initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:.onceToken.9
- initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:.sAllowedECEncAlgs
- initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:.sAllowedRSAEncAlgs
CStrings:
+ "-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]"
+ "@40@0:8^{__SecCertificate=}16@24^{__SecIdentity=}32"
+ "@48@0:8^{__SecCertificate=}16@24@32^{__SecIdentity=}40"
+ "MSCMSRecipientInfo requires an originator identity for an EC recipient. Encode will fail if not set."
+ "initWithCertificate:algorithmCapabilities:originator:"
+ "initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:"
- "-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]"
- "Fatal error"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Integers.swift"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"

```
