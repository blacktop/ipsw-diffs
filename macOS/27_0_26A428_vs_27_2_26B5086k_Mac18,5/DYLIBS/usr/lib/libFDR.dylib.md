## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1636.0.17.0.0
-  __TEXT.__text: 0x8a9e0
+1636.40.9.0.0
+  __TEXT.__text: 0x8b108
   __TEXT.__const: 0x2008
-  __TEXT.__cstring: 0x236cd
+  __TEXT.__cstring: 0x23869
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x3bb8
+  __TEXT.__unwind_info: 0x3bd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xad8
-  __AUTH_CONST.__cfstring: 0xfbc0
+  __AUTH_CONST.__cfstring: 0xfc00
   __AUTH_CONST.__auth_got: 0xa10
   __DATA.__objc_classrefs: 0x10
   __DATA.__data: 0x160
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4632
-  Symbols:   2191
-  CStrings:  4201
+  Functions: 4643
+  Symbols:   2194
+  CStrings:  4211
 
Symbols:
+ AMFDRModuleCertificationWithOptionsAndPermissions
+ _AMFDRModuleCertificationWithOptionsAndPermissions
+ __AMFDRModuleCertificationWithOptions
+ __getComponentTypeForInstance
- AMFDRModuleCertificationWithOptions
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
