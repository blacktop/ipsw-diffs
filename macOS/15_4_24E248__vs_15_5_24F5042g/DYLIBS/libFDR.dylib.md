## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1300.100.55.0.0
-  __TEXT.__text: 0x81644
-  __TEXT.__auth_stubs: 0x1380
+1300.120.3.0.0
+  __TEXT.__text: 0x81ed0
+  __TEXT.__auth_stubs: 0x13a0
   __TEXT.__const: 0x1fe8
-  __TEXT.__cstring: 0x213b1
+  __TEXT.__cstring: 0x21653
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38

   __DATA_CONST.__const: 0x708
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH_CONST.__auth_got: 0x9e0
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x9d0
-  __AUTH_CONST.__cfstring: 0xea60
+  __AUTH_CONST.__cfstring: 0xec80
   __DATA.__objc_classrefs: 0x10
   __DATA.__data: 0x180
   __DATA.__bss: 0x1b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4004
-  Symbols:   4874
-  CStrings:  3967
+  Functions: 4024
+  Symbols:   4896
+  CStrings:  3986
 
Symbols:
+ AMFDRDataTrustObjectIsFactorySigned.cold.1
+ AMFDRDataTrustObjectIsFactorySigned.cold.10
+ AMFDRDataTrustObjectIsFactorySigned.cold.2
+ AMFDRDataTrustObjectIsFactorySigned.cold.3
+ AMFDRDataTrustObjectIsFactorySigned.cold.4
+ AMFDRDataTrustObjectIsFactorySigned.cold.5
+ AMFDRDataTrustObjectIsFactorySigned.cold.6
+ AMFDRDataTrustObjectIsFactorySigned.cold.7
+ AMFDRDataTrustObjectIsFactorySigned.cold.8
+ AMFDRDataTrustObjectIsFactorySigned.cold.9
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.27
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.28
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.29
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.30
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.31
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.32
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.33
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.34
+ AMFDRSealingMapVerifyAsidMetadataForDevice.cold.35
+ _AMFDRDataTrustObjectIsFactorySigned
+ _SecCertificateCopyCommonName
+ _SecCertificateCreateWithData
+ __block_descriptor_tmp.1236
+ __block_descriptor_tmp.1241
+ __block_descriptor_tmp.1245
+ __block_descriptor_tmp.1253
+ __block_descriptor_tmp.1342
+ __block_descriptor_tmp.1407
+ __block_descriptor_tmp.1410
+ __block_descriptor_tmp.1565
+ __block_literal_global.1238
+ __block_literal_global.1255
+ __block_literal_global.1409
+ __block_literal_global.1412
- __block_descriptor_tmp.1211
- __block_descriptor_tmp.1215
- __block_descriptor_tmp.1220
- __block_descriptor_tmp.1224
- __block_descriptor_tmp.1321
- __block_descriptor_tmp.1386
- __block_descriptor_tmp.1389
- __block_descriptor_tmp.1544
- __block_literal_global.1213
- __block_literal_global.1217
- __block_literal_global.1388
- __block_literal_global.1391
CStrings:
+ "AMFDRDataAppendPermissionsString failed for seal"
+ "AMFDRDataCopySealingManifestProperty failed for supm"
+ "AMFDRDataTrustObjectIsFactorySigned"
+ "Could not get sealDataInstance"
+ "FDR CA issuer is: %@"
+ "FDR-CM-SSL-ROOT"
+ "Failed to allocate trustObject digest data"
+ "Failed to copy common name from certificate"
+ "Failed to create certificate reference"
+ "Failed to get cert data from SSL root"
+ "Failed to get digest sha256 from trustObject data"
+ "Failed to verify trustObject Digest"
+ "No FDR SSL root found"
+ "Unable to copy FDR SSL root"
+ "Unable to load FDR trustObject data"
+ "currentDevice has wrong type %@"
+ "supm data mismatched"
+ "supmSealingManifestData has wrong type %@"
+ "supmSealingMapData has wrong type %@"

```
