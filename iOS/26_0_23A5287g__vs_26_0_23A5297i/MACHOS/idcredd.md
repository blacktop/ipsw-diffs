## idcredd

> `/usr/libexec/idcredd`

```diff

-8.38.3.0.0
-  __TEXT.__text: 0x1878bc
-  __TEXT.__auth_stubs: 0x3bf0
+8.40.1.0.0
+  __TEXT.__text: 0x18a6e8
+  __TEXT.__auth_stubs: 0x3c30
   __TEXT.__objc_methlist: 0x8b4
-  __TEXT.__const: 0x4700
-  __TEXT.__cstring: 0xd499
+  __TEXT.__const: 0x46f0
+  __TEXT.__cstring: 0xe0d9
   __TEXT.__constg_swiftt: 0x21b4
-  __TEXT.__swift5_typeref: 0x2496
+  __TEXT.__swift5_typeref: 0x2488
   __TEXT.__swift5_reflstr: 0x16e7
   __TEXT.__swift5_fieldmd: 0x1624
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_capture: 0x1e94
   __TEXT.__objc_methname: 0x24e9
-  __TEXT.__oslogstring: 0x9ce8
+  __TEXT.__oslogstring: 0x9d68
   __TEXT.__swift5_proto: 0x144
   __TEXT.__swift5_types: 0x1d8
   __TEXT.__objc_classname: 0x7f
   __TEXT.__objc_methtype: 0xa90
-  __TEXT.__swift_as_entry: 0x5d4
-  __TEXT.__swift_as_ret: 0x6dc
+  __TEXT.__swift_as_entry: 0x5d0
+  __TEXT.__swift_as_ret: 0x6d8
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x5028
-  __TEXT.__eh_frame: 0x12b50
-  __DATA_CONST.__auth_got: 0x1df8
-  __DATA_CONST.__got: 0x13b0
+  __TEXT.__unwind_info: 0x5010
+  __TEXT.__eh_frame: 0x12ab0
+  __DATA_CONST.__auth_got: 0x1e18
+  __DATA_CONST.__got: 0x13b8
   __DATA_CONST.__auth_ptr: 0x9a8
-  __DATA_CONST.__const: 0x5720
+  __DATA_CONST.__const: 0x57a0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x27c8
   __DATA.__objc_selrefs: 0xa50
   __DATA.__objc_data: 0xcb0
-  __DATA.__data: 0x3fe8
+  __DATA.__data: 0x3fe0
   __DATA.__bss: 0x1cc0
   __DATA.__common: 0xf0
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FE963564-BD4E-330B-83F5-A4624E2201F5
-  Functions: 3815
-  Symbols:   1735
-  CStrings:  2048
+  UUID: 2920DFD0-CC71-31DC-85E3-B4CD46874228
+  Functions: 3817
+  Symbols:   1740
+  CStrings:  2055
 
Symbols:
+ _$s11CBORLibrary10COSE_Sign1V13CoreIDVSharedE8isTaggedSbvg
+ _$s13CoreIDVShared0A14IDVAssetBundleV15CertificateTypeO30appleIssuerWebPresentmentRootsyA2EmFWC
+ _$s13CoreIDVShared0A14IDVAssetBundleV30appleIssuerWebPresentmentRootsAA0aC12CertificatesVSgvg
+ _$s13CoreIDVShared13IDCSAnalyticsC26sendPayloadValidationEvent6reason7docType6issuer6result6region19issuingJurisdiction19hasTaggedIssuerAuthyAC0eF6ReasonO_SSSgAnC0eF6ResultOA2NSbtFZ
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
- _$s13CoreIDVShared13IDCSAnalyticsC26sendPayloadValidationEvent6reason7docType6issuer6result6region19issuingJurisdictionyAC0eF6ReasonO_SSSgAmC0eF6ResultOA2MtFZ
CStrings:
+ "All trusted Apple issued reader roots: %s"
+ "All trusted Apple issued web roots: %s"
+ "Internal setting enabled: truncate certificate chains to leaf only"
+ "MIICQzCCAcmgAwIBAgIILcX8iNLFS5UwCgYIKoZIzj0EAwMwZzEbMBkGA1UEAwwS\nQXBwbGUgUm9vdCBDQSAtIEczMSYwJAYDVQQLDB1BcHBsZSBDZXJ0aWZpY2F0aW9u\nIEF1dGhvcml0eTETMBEGA1UECgwKQXBwbGUgSW5jLjELMAkGA1UEBhMCVVMwHhcN\nMTQwNDMwMTgxOTA2WhcNMzkwNDMwMTgxOTA2WjBnMRswGQYDVQQDDBJBcHBsZSBS\nb290IENBIC0gRzMxJjAkBgNVBAsMHUFwcGxlIENlcnRpZmljYXRpb24gQXV0aG9y\naXR5MRMwEQYDVQQKDApBcHBsZSBJbmMuMQswCQYDVQQGEwJVUzB2MBAGByqGSM49\nAgEGBSuBBAAiA2IABJjpLz1AcqTtkyJygRMc3RCV8cWjTnHcFBbZDuWmBSp3ZHtf\nTjjTuxxEtX/1H7YyYl3J6YRbTzBPEVoA/VhYDKX1DyxNB0cTddqXl5dvMVztK517\nIDvYuVTZXpmkOlEKMaNCMEAwHQYDVR0OBBYEFLuw3qFYM4iapIqZ3r6966/ayySr\nMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEGMAoGCCqGSM49BAMDA2gA\nMGUCMQCD6cHEFl4aXTQY2e3v9GwOAEZLuN+yRhHFD/3meoyhpmvOwgPUnPWTxnS4\nat+qIxUCMG1mihDK1A3UT82NQz60imOlM27jbdoXt2QfyFMm+YhidDkLF1vLUagM\n6BgD56KyKA=="
+ "MIIDHDCCAqOgAwIBAgIUCUUHf/NG6IFwesRAtK4Eh4jVlxgwCgYIKoZIzj0EAwMw\nZzEbMBkGA1UEAwwSQXBwbGUgUm9vdCBDQSAtIEczMSYwJAYDVQQLDB1BcHBsZSBD\nZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTETMBEGA1UECgwKQXBwbGUgSW5jLjELMAkG\nA1UEBhMCVVMwHhcNMjMwMzAxMjIxMjA3WhcNMzgwMzAzMDAwMDAwWjB8MTAwLgYD\nVQQDDCdBcHBsZSBBcHBsaWNhdGlvbiBJbnRlZ3JhdGlvbiBDQSA3IC0gRzExJjAk\nBgNVBAsMHUFwcGxlIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MRMwEQYDVQQKDApB\ncHBsZSBJbmMuMQswCQYDVQQGEwJVUzB2MBAGByqGSM49AgEGBSuBBAAiA2IABHQG\nksXbeb0z6osmCAyng85Pvpr+mT1N60KGJwuHdrML8FNeQ+AGdcePn56h2wUE4SQv\n8v2+VIsGCbV6A5wuiVj0BIzNr1kCgVCQpMJwm/Eg+SNP83qDWEKlYzJntdVMIaOB\n+jCB9zASBgNVHRMBAf8ECDAGAQH/AgEAMB8GA1UdIwQYMBaAFLuw3qFYM4iapIqZ\n3r6966/ayySrMEYGCCsGAQUFBwEBBDowODA2BggrBgEFBQcwAYYqaHR0cDovL29j\nc3AuYXBwbGUuY29tL29jc3AwMy1hcHBsZXJvb3RjYWczMDcGA1UdHwQwMC4wLKAq\noCiGJmh0dHA6Ly9jcmwuYXBwbGUuY29tL2FwcGxlcm9vdGNhZzMuY3JsMB0GA1Ud\nDgQWBBQaOP5/gOVtyDcWWR4bEPL6MC2v2DAOBgNVHQ8BAf8EBAMCAQYwEAYKKoZI\nhvdjZAYCHwQCBQAwCgYIKoZIzj0EAwMDZwAwZAIwEmfzZUe6UTPD4wN/ZZRLdmue\nqA8Ip9VJizZsdSOrSz3uLepS60AViSIUxioytqgNAjAp7qKnN64gS1ECerjsprly\n0XSjLUoE0xs0QLxN/Mm95RcmZwkAaMNo9F4vld8jroA="
+ "MIIDNjCCArugAwIBAgIIMjjRxxHADDUwCgYIKoZIzj0EAwMwbDEgMB4GA1UEAwwX\nVGVzdCBBcHBsZSBSb290IENBIC0gRzMxJjAkBgNVBAsMHUFwcGxlIENlcnRpZmlj\nYXRpb24gQXV0aG9yaXR5MRMwEQYDVQQKDApBcHBsZSBJbmMuMQswCQYDVQQGEwJV\nUzAeFw0yMzAyMTAwMDE4NDZaFw0zODAyMDYwMDE4NDVaMIGBMTUwMwYDVQQDDCxU\nZXN0IEFwcGxlIEFwcGxpY2F0aW9uIEludGVncmF0aW9uIENBIDcgLSBHMTEmMCQG\nA1UECwwdQXBwbGUgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkxEzARBgNVBAoMCkFw\ncGxlIEluYy4xCzAJBgNVBAYTAlVTMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEYNnF\nxloB1mKErywkd8kbUVeBNYiWkHqd1oaxUIXSz2N4pLerTnui6U3a83XzGMWapprz\nKiZubK+FgYOsAmgL5lBX8csE30Lb1/XmoTG3j6n5TQHdAQildWSU/nf784clo4IB\nEjCCAQ4wDwYDVR0TAQH/BAUwAwEB/zAfBgNVHSMEGDAWgBT8RtiDbB/m8tzfp5kX\nrgtEZxcbRjBTBggrBgEFBQcBAQRHMEUwQwYIKwYBBQUHMAGGN2h0dHA6Ly9vY3Nw\nLXVhdC5jb3JwLmFwcGxlLmNvbS9vY3NwMDMtdGVzdGFwcGxlcm9vdGNhZzMwRAYD\nVR0fBD0wOzA5oDegNYYzaHR0cDovL2NybC11YXQuY29ycC5hcHBsZS5jb20vdGVz\ndGFwcGxlcm9vdGNhZzMuY3JsMB0GA1UdDgQWBBQHyzKHNVBeiKqiILBS+Ekbz/SV\neDAOBgNVHQ8BAf8EBAMCAQYwEAYKKoZIhvdjZAYCHwQCBQAwCgYIKoZIzj0EAwMD\naQAwZgIxAKeWCUlAJPAxLS/XY+HbSTSUOa4F9IY0w4GQiuhKSNrl5JlyhBhvB8aa\n60xIivYxSQIxAPPLQa/wmiXBADyHLbeQN0VE5sIKL5NiCDlre8CtvT/pXaHFnuvC\n9El6VcDjUPnV0A=="
+ "debug.web-presentment.truncate-certificate-chain-leaf-only"
+ "idcredd/TrustedRootCertificates.swift"
+ "trustedAppleIssuerWebPresentmentRoots()"
- "All trusted apple issued reader roots: %s"
- "idcredd/ReaderRootCertificates.swift"

```
