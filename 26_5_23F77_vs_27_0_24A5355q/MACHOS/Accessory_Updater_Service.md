## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

-3476.120.8.0.2
-  __TEXT.__text: 0x77844
-  __TEXT.__auth_stubs: 0x1840
+3689.0.0.0.1
+  __TEXT.__text: 0x77fac
+  __TEXT.__auth_stubs: 0x1890
   __TEXT.__objc_stubs: 0x2d00
   __TEXT.__objc_methlist: 0x2e94
-  __TEXT.__const: 0x5cb0
+  __TEXT.__const: 0x5d50
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x176bb
+  __TEXT.__cstring: 0x178ab
   __TEXT.__objc_methname: 0x3682
-  __TEXT.__objc_classname: 0xb12
+  __TEXT.__objc_classname: 0xaf0
   __TEXT.__objc_methtype: 0xd01
   __TEXT.__oslogstring: 0x155e
-  __TEXT.__unwind_info: 0x1888
-  __DATA_CONST.__auth_got: 0xc30
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x2ab0
-  __DATA_CONST.__cfstring: 0x11180
+  __TEXT.__unwind_info: 0x1a10
+  __DATA_CONST.__const: 0x2b08
+  __DATA_CONST.__cfstring: 0x11460
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__auth_got: 0xc58
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0x54a8
   __DATA.__objc_selrefs: 0xf70
   __DATA.__objc_ivar: 0x37c

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2B450263-EF89-3146-BCC4-6FB3B870FAF1
-  Functions: 2715
-  Symbols:   1851
-  CStrings:  6968
+  UUID: 3F6FAAF6-0329-32DA-9CE8-DCF48F0B96D2
+  Functions: 2744
+  Symbols:   1876
+  CStrings:  7012
 
Symbols:
+ _AMAuthInstallCryptoCreateDigestForData_SHA3_384
+ _AMAuthInstallRequestAddRequiredHTTPHeaders
+ _AMSupportCopyDataFromHexString
+ _CFStringInsert
+ _DERImg4CertificateItemSpecs
+ _DERImg4DecodeCertificate
+ _DERImg4DecodeFindProperty
+ _DERImg4DecodeFindPropertyInSequence
+ _DERImg4DecodeParseManifestProperties
+ _DERImg4DecodePropertyWithItem
+ _DERImg4DecodeUnsignedCertificate
+ _DERImg4DecodeUnsignedManifest
+ _DERImg4UnsignedManifestItemSpecs
+ _Img4DecodeGetObjectProperty
+ _Img4DecodeGetObjectPropertyData
+ _Img4DecodeInitManifest
+ __CFDictionaryGetUInt64
+ __CFStringToUInt64
+ _kAMAuthInstallApParameterHardwareModel
+ _kAMAuthInstallApParameterTagPrefix
+ _kAMAuthInstallTagCryptex1KeyAlgorithm
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _parse_raw_server_response
+ _parse_raw_server_response_legacy
- _ASErrorDomain
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x28
CStrings:
+ " epochs:"
+ "%s: AMAuthInstallCryptoCreateDigestForData_SHA3_384 returned %d: %@"
+ "%s: Failed to read file %@"
+ "AMAuthInstallApCreateMeasurementsWithTag"
+ "Ap,TouchASICFW"
+ "ApTagPrefix"
+ "Cryptex1,KeyAlgorithm"
+ "Cryptex1,RosettaOS"
+ "Cryptex1,RosettaTrustCache"
+ "Cryptex1,RosettaVolume"
+ "Current sandcat epochs: %@"
+ "Error: %@\n"
+ "Failed to allocate a buffer large enough to hold the response. Needed %d bytes"
+ "Failed to copy AP parameters"
+ "No epoch string set"
+ "Unable to parse epoch string"
+ "cros"
+ "crsy"
+ "libauthinstall_device-1154"
+ "sha3-384"
+ "tagPrefix is NULL"
+ "tasf"
+ "trcr"
+ "x-intnt-keyalg-certformat"
+ "x-intnt-keyalg-hashmethod"
+ "x-intnt-keyalg-keyscheme"
+ "x-intnt-keyalg-version"
- "CFDataCreate failed"
- "CFDictionaryCreateCopy failed"
- "CFPropertyListCreateFromXMLData failed (%@)"
- "Response too large"
- "libauthinstall_device-1104.120.3.0.1"
- "no data in response"

```
