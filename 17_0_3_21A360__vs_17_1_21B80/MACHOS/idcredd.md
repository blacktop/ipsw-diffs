## idcredd

> `/usr/libexec/idcredd`

```diff

-6.46.3.0.0
-  __TEXT.__text: 0xde850
-  __TEXT.__auth_stubs: 0x2fc0
+6.108.0.0.0
+  __TEXT.__text: 0xdef98
+  __TEXT.__auth_stubs: 0x3010
   __TEXT.__objc_methlist: 0x358
   __TEXT.__const: 0x1b50
-  __TEXT.__cstring: 0x10f21
-  __TEXT.__objc_methname: 0x1b6e
+  __TEXT.__cstring: 0x110f1
+  __TEXT.__objc_methname: 0x1b78
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1e80
-  __TEXT.__swift5_typeref: 0x1234
+  __TEXT.__constg_swiftt: 0x1e88
+  __TEXT.__swift5_typeref: 0x1220
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0xd63
   __TEXT.__swift5_assocty: 0x180

   __TEXT.__objc_methtype: 0x9d9
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_capture: 0x764
-  __TEXT.__unwind_info: 0x1a0c
-  __TEXT.__eh_frame: 0x5040
-  __DATA_CONST.__auth_got: 0x17e0
+  __TEXT.__unwind_info: 0x1b88
+  __TEXT.__eh_frame: 0x5190
+  __DATA_CONST.__auth_got: 0x1808
   __DATA_CONST.__got: 0xd20
   __DATA_CONST.__auth_ptr: 0x1a0
-  __DATA_CONST.__const: 0x2250
+  __DATA_CONST.__const: 0x2248
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_protorefs: 0x48
   __DATA.__objc_classrefs: 0x128
   __DATA.__objc_data: 0xa20
-  __DATA.__data: 0x3c98
+  __DATA.__data: 0x3c88
   __DATA.__common: 0xb8
   __DATA.__bss: 0x1510
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D3ED48A5-CEA5-38D7-8159-67829238E801
-  Functions: 1856
-  Symbols:   1329
-  CStrings:  1577
+  UUID: 24EE4E59-8A00-3807-B9A9-326808F92C0A
+  Functions: 1860
+  Symbols:   1334
+  CStrings:  1585
 
Symbols:
+ _$s10Foundation4DateV11distantPastACvgZ
+ _$s10Foundation4DateV13distantFutureACvgZ
+ _$s13CoreIDVShared13IDCSAnalyticsC29sendPayloadIngestionSizeEvent7docType6issuer07overallG5Bytes16numberOfPackages07packagegM0ySS_SSSgS3itFZ
+ _$s13CoreIDVShared15StoredCryptoKeyC12fetchRequestSo07NSFetchG0CyACGyFZ
+ _$s13CoreIDVShared17debugLogFootprintyySSF
+ _$s13CoreIDVShared20ISO18013JumboPackageV7version8packagesACSS_Say10Foundation4DataVGtcfC
+ _$s13CoreIDVShared20ISO18013JumboPackageV8packagesSay10Foundation4DataVGvg
+ _$s13CoreIDVShared30ISO18013_5_1_ElementIdentifierO19issuingJurisdictionyA2CmFWC
- _$s13CoreIDVShared15ISO18013PackageVSEAAMc
- _$s13CoreIDVShared20ISO18013JumboPackageV7version8packagesACSS_SayAA15CBOREncodedCBORVyAA0cE0VGGtcfC
- _$s13CoreIDVShared20ISO18013JumboPackageV8packagesSayAA15CBOREncodedCBORVyAA0cE0VGGvg
CStrings:
+ "Inserting biometric encrypted payload (legacy flow)"
+ "Jumbo package contains %{public}ld payloads of size %{public}ld bytes"
+ "Jumbo package contains no payloads"
+ "credential.credentialIdentifier == %@ AND (usage == %@ OR usage == %@)"
+ "credential.credentialIdentifier == %@ AND usage == %@"
+ "credential.credentialIdentifier == %@ AND usage == %@ AND publicKeyIdentifier == %@"
+ "replacePayload:END"
+ "replacePayload:START"
+ "replacePayload:package loop END"
+ "replacePayload:package loop START"
+ "unable to determine needsPresentmentKeyRefresh, assuming false"
- "Inserting biometric encrypted payload"
- "The count of Payload Protection keys for credential %s is %ld"
- "cryptoKeys"
- "prepareJumboPackage(_:context:credential:decryptionKey:format:)"

```
