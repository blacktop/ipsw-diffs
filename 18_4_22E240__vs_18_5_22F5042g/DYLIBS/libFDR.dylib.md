## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1300.100.55.0.0
-  __TEXT.__text: 0x81b38
-  __TEXT.__auth_stubs: 0x1370
+1300.120.3.0.0
+  __TEXT.__text: 0x823c4
+  __TEXT.__auth_stubs: 0x1390
   __TEXT.__const: 0x1fe0
-  __TEXT.__cstring: 0x212b9
+  __TEXT.__cstring: 0x2155b
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38

   __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__auth_got: 0x9d8
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__const: 0x910
-  __AUTH_CONST.__cfstring: 0xea40
+  __AUTH_CONST.__cfstring: 0xec60
   __DATA.__data: 0x160
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4003
-  Symbols:   4567
-  CStrings:  3964
+  Functions: 4023
+  Symbols:   4589
+  CStrings:  3983
 
Symbols:
+ _AMFDRDataTrustObjectIsFactorySigned
+ _SecCertificateCopyCommonName
+ _SecCertificateCreateWithData
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
