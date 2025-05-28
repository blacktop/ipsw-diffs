## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-3.26.0.0.0
-  __TEXT.__text: 0x24a64
+3.26.2.3.0
+  __TEXT.__text: 0x24c38
   __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0x2d2c
+  __TEXT.__objc_methlist: 0x2d54
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__cstring: 0x2c35
-  __TEXT.__ustring: 0xa0
-  __TEXT.__unwind_info: 0xc4c
+  __TEXT.__gcc_except_tab: 0x61c
+  __TEXT.__cstring: 0x2c8f
+  __TEXT.__ustring: 0x46
+  __TEXT.__unwind_info: 0xc5c
   __TEXT.__objc_classname: 0xa02
-  __TEXT.__objc_methname: 0xa702
+  __TEXT.__objc_methname: 0xa75c
   __TEXT.__objc_methtype: 0x1eea
-  __TEXT.__objc_stubs: 0x73e0
+  __TEXT.__objc_stubs: 0x7420
   __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x59d8
-  __DATA_CONST.__objc_selrefs: 0x22f8
+  __DATA_CONST.__objc_selrefs: 0x2308
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__objc_const: 0x1408
-  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__cfstring: 0x2440
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1090
-  Symbols:   4358
-  CStrings:  2265
+  Functions: 1095
+  Symbols:   4371
+  CStrings:  2269
 
Symbols:
+ -[MCInstallProfileViewController _removeProfileWithIdentifier:completionHandler:]
+ -[MCUITableViewController initWithStyle:]
+ -[MCUITableViewController init]
+ -[MCUIViewController init]
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table79
+ ___63-[MCRemoveProfileViewController _leaveRemoteManagementAndErase]_block_invoke_3
+ ___81-[MCInstallProfileViewController _removeProfileWithIdentifier:completionHandler:]_block_invoke
+ ___81-[MCInstallProfileViewController _removeProfileWithIdentifier:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ _objc_msgSend$_removeProfileWithIdentifier:completionHandler:
+ _objc_msgSend$setCellLayoutMarginsFollowReadableWidth:
- GCC_except_table73
- GCC_except_table76
- GCC_except_table78
- ___69-[MCInstallProfileViewController performRemoveAfterFinalVerification]_block_invoke_3
- ___69-[MCInstallProfileViewController performRemoveAfterFinalVerification]_block_invoke_4
CStrings:
+ "Profile removal finished. Error: %@"
+ "Unenrolled from DEP. Removing existing MDM profile..."
+ "_removeProfileWithIdentifier:completionHandler:"
+ "setCellLayoutMarginsFollowReadableWidth:"

```
