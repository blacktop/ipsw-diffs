## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

-101.0.0.0.0
-  __TEXT.__text: 0x1a94
+102.0.0.0.0
+  __TEXT.__text: 0x1b94
   __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_methlist: 0x128
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__cstring: 0x1a1
+  __TEXT.__gcc_except_tab: 0xd0
+  __TEXT.__cstring: 0x1aa
   __TEXT.__oslogstring: 0x2e4
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__unwind_info: 0xf4
   __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x48f
+  __TEXT.__objc_methname: 0x491
   __TEXT.__objc_methtype: 0x7e
   __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_classrefs: 0x40
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x198
   __DATA.__data: 0x60
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__const: 0x40
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0x90
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D819E488-0455-3D74-86AC-3B3ACAE7E0D3
-  Functions: 33
-  Symbols:   223
-  CStrings:  106
+  UUID: 6617F2BD-FB5C-3DD9-87CD-CF85F2FE40C7
+  Functions: 34
+  Symbols:   226
+  CStrings:  107
 
Symbols:
+ +[ATTrackingManager _performTCCAccessRequest:]
+ ___46+[ATTrackingManager _performTCCAccessRequest:]_block_invoke
+ ___71+[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32bs_e62_v24?0"NSObject<OS_tcc_authorization_record>"8^{__CFError=}16ls32l8
+ ___block_descriptor_48_e8_32bs_e8_v16?0Q8ls32l8
+ _objc_msgSend$_performTCCAccessRequest:
- +[ATTrackingManager _performTCCAccessRequest]
- GCC_except_table11
- ___45+[ATTrackingManager _performTCCAccessRequest]_block_invoke
- _objc_msgSend$_performTCCAccessRequest
CStrings:
+ "_performTCCAccessRequest:"
+ "v16@?0Q8"
- "_performTCCAccessRequest"

```
