## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1636.0.17.0.0
-  __TEXT.__text: 0x8ade4
+1636.40.9.0.0
+  __TEXT.__text: 0x8b51c
   __TEXT.__const: 0x2000
-  __TEXT.__cstring: 0x235d5
+  __TEXT.__cstring: 0x23771
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x3bb8
+  __TEXT.__unwind_info: 0x3bc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x9b8
-  __AUTH_CONST.__cfstring: 0xfba0
+  __AUTH_CONST.__cfstring: 0xfbe0
   __AUTH_CONST.__auth_got: 0xa08
   __DATA.__data: 0x160
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4633
-  Symbols:   1731
-  CStrings:  4198
+  Functions: 4644
+  Symbols:   1734
+  CStrings:  4208
 
Symbols:
+ _AMFDRModuleCertificationWithOptionsAndPermissions
+ __AMFDRModuleCertificationWithOptions
+ __getComponentTypeForInstance
CStrings:
+ "AMFDRModuleCertificationWithOptionsAndPermissions"
+ "AMSupportRsaCreateDataFromPem failed for permission cert"
+ "CFDataCreate failed for permCertDerData"
+ "CertifyPermissionCert"
+ "Failed to allocate infoOptions"
+ "_AMFDRDiagnosticCopyComponentTypesInfoFromSealingManifest"
+ "_AMFDRDiagnosticCopyComponentTypesInfoFromSealingMap"
+ "_AMFDRModuleCertificationWithOptions"
+ "_AMFDRSupportBase64Encode failed for permission cert"
+ "amfdr->cert is not a CFDataRef"
+ "x-fdr-auth-cert"
- "AMFDRModuleCertificationWithOptions"
```
