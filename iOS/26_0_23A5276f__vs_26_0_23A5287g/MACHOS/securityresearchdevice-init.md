## securityresearchdevice-init

> `/usr/libexec/securityresearchdevice-init`

```diff

-221.0.14.0.0
-  __TEXT.__text: 0xf08c
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__const: 0x6b8
+221.0.20.0.0
+  __TEXT.__text: 0x17f94
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__const: 0x828
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x316
-  __TEXT.__swift5_typeref: 0x124
-  __TEXT.__cstring: 0x265
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__objc_methname: 0x288
-  __TEXT.__constg_swiftt: 0x1dc
-  __TEXT.__swift5_reflstr: 0x464
-  __TEXT.__swift5_fieldmd: 0x2d8
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_mpenum: 0x20
+  __TEXT.__cstring: 0x55c
+  __TEXT.__swift_as_entry: 0x68
+  __TEXT.__swift_as_ret: 0x98
+  __TEXT.__oslogstring: 0x73c
+  __TEXT.__swift5_typeref: 0x158
+  __TEXT.__constg_swiftt: 0x220
+  __TEXT.__swift5_reflstr: 0x504
+  __TEXT.__swift5_fieldmd: 0x334
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__objc_methname: 0x29a
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x28
-  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x390
-  __TEXT.__eh_frame: 0xab8
-  __DATA_CONST.__auth_got: 0x670
+  __TEXT.__unwind_info: 0x630
+  __TEXT.__eh_frame: 0x1620
+  __DATA_CONST.__auth_got: 0x6c0
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0xd0
-  __DATA_CONST.__const: 0x4d0
+  __DATA_CONST.__const: 0x560
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0xc0
-  __DATA.__data: 0x3b8
-  __DATA.__bss: 0x520
+  __DATA.__objc_selrefs: 0xd0
+  __DATA.__data: 0x4d0
+  __DATA.__bss: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D35CFA6D-B80A-36B7-9A9F-7DF09667022A
-  Functions: 218
-  Symbols:   308
-  CStrings:  66
+  UUID: 88F7A1A9-5BE9-3847-8440-29327FB44F52
+  Functions: 337
+  Symbols:   318
+  CStrings:  112
 
Symbols:
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSiN
+ _$sSis23CustomStringConvertiblesWP
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$ss11_StringGutsV4growyySiF
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss26DefaultStringInterpolationV06appendC0yyxlF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _$ss8DurationV7secondsyABSdFZ
+ _MAStringForMADownloadResult
+ _MAStringForMAPurgeResult
+ _exp2
+ _objc_release_x28
+ _objc_retain_x23
+ _os_transaction_create
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_getEnumCaseMultiPayload
+ _swift_getErrorValue
+ _swift_release_n
- _$s10CryptexKit0A5ErrorO15cryptexNotFoundyA2CmFWC
- _$s10CryptexKit0A5ErrorOMa
- _$s10CryptexKit0A5ErrorOs0C0AAMc
- _$ss16DurationProtocolP1moiyxx_SitFZTj
- _$ss8DurationV1poiyA2B_ABtFZ
- _$ss8DurationVN
- _$ss8DurationVs0A8ProtocolsWP
- _objc_retain_x24
- _objc_retain_x28
- _swift_getExistentialTypeMetadata
- _swift_getTupleTypeMetadata2
CStrings:
+ ") attempt failed: "
+ "AEA decryption with %ld threads"
+ "Acceptable network found"
+ "Breadcrumb created"
+ "Cryptex installed successfully"
+ "Cryptex personalized"
+ "Deleted HTTP download successfully"
+ "Deleted MobileAsset %s successfully"
+ "Error: %@, in %s, line: %ld"
+ "Error: %s, in %s, line: %ld"
+ "Extracted asset path from downloaded MobileAsset"
+ "Extracted local encrypted asset URL"
+ "Failed to delete downloaded asset: %@"
+ "Failed to download asset on iteration "
+ "Failed to download mobile asset catalog on iteration "
+ "Failed to purge MobileAsset "
+ "Forced provisioning: %{bool}d"
+ "Found NVRAM value %s for key %s"
+ "Found variants for %s: %s"
+ "HTTP download attempt iteration: %ld"
+ "HTTP download has correct status code"
+ "HTTP download has response"
+ "HTTP download successful"
+ "Mobile asset catalog download successful"
+ "Mobile asset query download successful"
+ "Mobile asset query result count successful"
+ "Mobile asset query result successful"
+ "Mobile asset query successful"
+ "NVRAM forced provisioning removed"
+ "NVRAM initialization successful"
+ "NVRAM synchronized"
+ "NVRAM variables for cryptex installation are set"
+ "Non acceptable network found"
+ "Removed NVRAM value for key %s"
+ "SecurityResearchDeviceInitCore: "
+ "SecurityResearchDeviceInitMain.run: "
+ "String to hexadecimal data convertion completed"
+ "Temporary directory created"
+ "Temporary directory removed"
+ "Waiting for network"
+ "aea-decrypt"
+ "assetId"
+ "checkShouldInstallCryptex()"
+ "decrypt(sourceURL:destinationURL:recipientPrivateKey:)"
+ "decryptCryptex(encryptedURL:)"
+ "downloadCryptex()"
+ "hexDecodedData()"
+ "httpDownload(url:)"
+ "mobileAssetDownload(audienceId:assetType:compatibilityVersion:)"
+ "personalizeAndInstallBundle(at:)"
+ "purgeSync"
+ "srd-prov-retry-count"
+ "synchronize(forKey:)"
+ "unknown MA error"
+ "unknown MA error "
- "%@"
- "%s"
- "Found variants: %s"
- "Installed cryptex"
- "Personalized cryptex"
- "Request (%s) attempt failed: %@"
- "SecurityResearchDeviceInitMain.run: %@"
- "Will install cryptex"
- "Will personalize cryptex"

```
