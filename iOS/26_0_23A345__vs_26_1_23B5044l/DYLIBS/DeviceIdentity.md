## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-1065.0.0.0.0
-  __TEXT.__text: 0x1be48
-  __TEXT.__auth_stubs: 0x860
+1068.40.2.0.0
+  __TEXT.__text: 0x1c1d8
+  __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x49c
-  __TEXT.__cstring: 0x3c7a
+  __TEXT.__cstring: 0x3d4a
   __TEXT.__const: 0xab92
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x69b
-  __TEXT.__gcc_except_tab: 0x890
+  __TEXT.__oslogstring: 0x7be
+  __TEXT.__gcc_except_tab: 0x888
   __TEXT.__dlopen_cstrs: 0x134
   __TEXT.__unwind_info: 0x3d0
   __TEXT.__objc_classname: 0x71

   __TEXT.__objc_methtype: 0x320
   __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x3700
+  __DATA_CONST.__const: 0x3708
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x4a8
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__cfstring: 0x4160
   __AUTH_CONST.__objc_const: 0x710
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AD03E82-FBF5-3D98-BF69-281410536F72
-  Functions: 255
-  Symbols:   1315
-  CStrings:  1424
+  UUID: 22651480-6C5F-3F68-9829-BE7FA384A751
+  Functions: 258
+  Symbols:   1323
+  CStrings:  1436
 
Symbols:
+ GCC_except_table22
+ GCC_except_table5
+ ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.309
+ ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.312
+ ___block_literal_global.328
+ _copyDateUsedForCertificateValidation
+ _kMAOptionsBAAClientProvidedDate
+ _objc_retain_x25
- GCC_except_table13
- GCC_except_table14
- GCC_except_table15
- GCC_except_table25
- ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.321
- ___DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.324
- ___block_literal_global.340
CStrings:
+ "ClientNameSuffix"
+ "ClientProvidedDate"
+ "Existing monotonic time not found (%@/%@): %d"
+ "Existing server timestamp not found (%@/%@): %d"
+ "Failed to copy bytes from existing monotonic time data."
+ "Failed to copy date used for certificate validation."
+ "Failed to copy the date used for certificate validation (treating the cached certificate as expired): %@"
+ "No cached PMU reset count exists (treating the cached certificate as expired)."
+ "PMU reset occurred since the cached certificate was obtained (treating the cached certificate as expired)."
+ "copyDateUsedForCertificateValidation"
+ "iOS Device Activator (MobileActivation-1068.40.2)"
- "BAAClientNameSuffix"
- "SPI not allowed for processes running in recoveryOS."
- "iOS Device Activator (MobileActivation-1065)"

```
