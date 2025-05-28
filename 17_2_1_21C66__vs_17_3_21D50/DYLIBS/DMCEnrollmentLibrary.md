## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-3.26.3.6.0
-  __TEXT.__text: 0x13c30
+3.26.4.1.0
+  __TEXT.__text: 0x1409c
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0xcf4
+  __TEXT.__objc_methlist: 0xd14
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x14aa
-  __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__oslogstring: 0x1de9
-  __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x434
+  __TEXT.__cstring: 0x14df
+  __TEXT.__gcc_except_tab: 0x378
+  __TEXT.__oslogstring: 0x1e50
+  __TEXT.__dlopen_cstrs: 0x10b
+  __TEXT.__unwind_info: 0x450
   __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methname: 0x48a0
+  __TEXT.__objc_methname: 0x491a
   __TEXT.__objc_methtype: 0x4b6
-  __TEXT.__objc_stubs: 0x37a0
+  __TEXT.__objc_stubs: 0x3820
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__const: 0x9e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xb88
-  __DATA_CONST.__objc_selrefs: 0xed0
-  __DATA_CONST.__objc_arraydata: 0x4c8
-  __AUTH_CONST.__cfstring: 0xd60
+  __DATA_CONST.__objc_selrefs: 0xef0
+  __DATA_CONST.__objc_arraydata: 0x4d0
+  __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__auth_got: 0x280
   __AUTH.__objc_data: 0x50
   __DATA.__objc_classrefs: 0x140
   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0xcc
-  __DATA.__bss: 0x68
-  __DATA_DIRTY.__const: 0x80
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0x1b0
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 369
-  Symbols:   1565
-  CStrings:  942
+  Functions: 375
+  Symbols:   1585
+  CStrings:  951
 
Symbols:
+ +[DMCEnrollmentFlowController _createEnrollmentNotAllowedDuringSDPError]
+ -[DMCEnrollmentFlowController _doesDeviceProtectionStateAllowEnrollmentType:]
+ GCC_except_table181
+ _LocalAuthenticationLibraryCore.frameworkLibrary
+ ___LocalAuthenticationLibraryCore_block_invoke
+ ___block_literal_global.402
+ ___block_literal_global.451
+ ___getLARatchetManagerClass_block_invoke
+ ___getLARatchetManagerClass_block_invoke.cold.1
+ __unnamed_array_storage.388
+ __unnamed_array_storage.399
+ _audit_stringLocalAuthentication
+ _getLARatchetManagerClass
+ _getLARatchetManagerClass.softClass
+ _objc_msgSend$_createEnrollmentNotAllowedDuringSDPError
+ _objc_msgSend$_doesDeviceProtectionStateAllowEnrollmentType:
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$sharedInstance
- ___block_literal_global.400
- ___block_literal_global.446
- __unnamed_array_storage.386
- __unnamed_array_storage.397
CStrings:
+ "DMC_ENROLLMENT_NOT_ALLOWED_WITH_SDP"
+ "Failed: %lu feature is not supported when SDP is enabled"
+ "LARatchetManager"
+ "Unable to check SDP with LocalAuthentication!"
+ "_createEnrollmentNotAllowedDuringSDPError"
+ "_doesDeviceProtectionStateAllowEnrollmentType:"
+ "isFeatureEnabled"
+ "sharedInstance"
+ "softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"

```
