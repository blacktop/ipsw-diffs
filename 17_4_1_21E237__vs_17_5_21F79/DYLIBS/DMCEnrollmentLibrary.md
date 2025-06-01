## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-3.26.5.12.0
-  __TEXT.__text: 0x16c48
+3.26.6.4.0
+  __TEXT.__text: 0x16e44
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_methlist: 0xeec
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x1760
-  __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__oslogstring: 0x2197
+  __TEXT.__gcc_except_tab: 0x3f8
+  __TEXT.__oslogstring: 0x219d
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x4bc
+  __TEXT.__unwind_info: 0x4cc
   __TEXT.__objc_classname: 0xe5
-  __TEXT.__objc_methname: 0x552c
-  __TEXT.__objc_methtype: 0x553
+  __TEXT.__objc_methname: 0x5534
+  __TEXT.__objc_methtype: 0x562
   __TEXT.__objc_stubs: 0x4160
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__const: 0xb28
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x1158
   __DATA_CONST.__objc_classrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x598
+  __DATA_CONST.__objc_arraydata: 0x5a0
   __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__objc_intobj: 0x5d0
+  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x330
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xe8
   __DATA.__bss: 0x78
-  __DATA_DIRTY.__const: 0x60
-  __DATA_DIRTY.__objc_const: 0x1b0
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__const: 0x80
+  __DATA_DIRTY.__objc_const: 0x240
+  __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EBF259E-65FE-33A4-8E56-4011366D7A31
-  Functions: 434
-  Symbols:   1823
-  CStrings:  1205
+  UUID: 6B8C3698-9D0E-312B-A130-064F996EAE2E
+  Functions: 435
+  Symbols:   1827
+  CStrings:  1206
 
Symbols:
+ -[DMCEnrollmentFlowController _enrollmentTypeAuthorizedBySDP:completion:]
+ GCC_except_table131
+ GCC_except_table136
+ GCC_except_table26
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table85
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table99
+ ___111-[DMCEnrollmentFlowController _startEnrollmentFlowWithType:anchorCertificates:restartIfFail:completionHandler:]_block_invoke
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.63
+ ___block_descriptor_57_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_literal_global.134
+ ___block_literal_global.81
+ __unnamed_array_storage.78
+ _objc_msgSend$_enrollmentTypeAuthorizedBySDP:completion:
+ _objc_msgSend$isAuthorizedForOperation:completion:
- -[DMCEnrollmentFlowController _doesDeviceProtectionStateAllowEnrollmentType:]
- GCC_except_table130
- GCC_except_table135
- GCC_except_table36
- GCC_except_table39
- GCC_except_table44
- GCC_except_table47
- GCC_except_table50
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table62
- GCC_except_table65
- GCC_except_table68
- GCC_except_table73
- GCC_except_table76
- GCC_except_table79
- GCC_except_table84
- GCC_except_table89
- GCC_except_table92
- GCC_except_table98
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.62
- ___block_literal_global.132
- ___block_literal_global.79
- __unnamed_array_storage.76
- _objc_msgSend$_doesDeviceProtectionStateAllowEnrollmentType:
- _objc_msgSend$isAuthorizedForOperation:
CStrings:
+ "Failed: %lu feature is not supported while SDP is unauthorized"
+ "_enrollmentTypeAuthorizedBySDP:completion:"
+ "isAuthorizedForOperation:completion:"
+ "v32@0:8Q16@?24"
- "Failed: %lu feature is not supported when SDP is enabled"
- "_doesDeviceProtectionStateAllowEnrollmentType:"
- "isAuthorizedForOperation:"

```
