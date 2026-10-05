## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-1219.40.7.0.0
-  __TEXT.__text: 0x428d4
-  __TEXT.__objc_methlist: 0x4a4
+1219.40.10.502.1
+  __TEXT.__text: 0x43138
+  __TEXT.__objc_methlist: 0x4dc
   __TEXT.__const: 0x6de23
-  __TEXT.__cstring: 0x1bba
-  __TEXT.__oslogstring: 0x4eea
+  __TEXT.__cstring: 0x1cb1
+  __TEXT.__oslogstring: 0x5041
   __TEXT.__gcc_except_tab: 0x22c
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xc68
+  __TEXT.__unwind_info: 0xc88
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e8
+  __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x1c50
-  __AUTH_CONST.__cfstring: 0x1c80
+  __AUTH_CONST.__cfstring: 0x1ca0
   __AUTH_CONST.__objc_const: 0x648
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x208
   __DATA.__objc_ivar: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 860
-  Symbols:   1891
-  CStrings:  735
+  Functions: 870
+  Symbols:   1900
+  CStrings:  749
 
Symbols:
+ -[MFAACertificateManager verifyComponentType:forModuleMFi3Certificate:forAuthFlags:]
+ -[MFAACertificateManager verifyComponentType:forModuleMFi4Certificate:]
+ -[MFAACertificateManager verifyIndex:forModuleMFi4Certificate:forModule:]
+ -[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:forIndex:]
+ -[MFAACertificateManager verifyPartNumber:forModuleMFi4Certificate:forModule:]
+ GCC_except_table45
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _SecCertificateCopyComponentAttributes
- GCC_except_table35
CStrings:
+ "%s: !certRef"
+ "%s: !componentAttributes"
+ "%s: !retrievedIndex"
+ "%s: (moduleType=%d) found certPartNumber:%@"
+ "%s: (moduleType=%d) found index:%@"
+ "%s: (moduleType=%d) index:%@"
+ "%s: (moduleType=%d) productTypeString:%@"
+ "(moduleType=%d) Error: missing index"
+ "(moduleType=%d) Failure: cannot find part number"
+ "(moduleType=%d) Failure: part number is too short"
+ "-[MFAACertificateManager verifyIndex:forModuleMFi4Certificate:forModule:]"
+ "-[MFAACertificateManager verifyModuleCertificate:forModule:forAuthFlags:forIndex:]"
+ "-[MFAACertificateManager verifyPartNumber:forModuleMFi4Certificate:forModule:]"
+ "iPhone19,4"
```
