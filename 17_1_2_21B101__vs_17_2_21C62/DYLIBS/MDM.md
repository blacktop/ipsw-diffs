## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-3.26.2.3.0
-  __TEXT.__text: 0x3a9b0
+3.26.3.6.0
+  __TEXT.__text: 0x3af34
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x2128
+  __TEXT.__objc_methlist: 0x2138
   __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0xa4c
-  __TEXT.__cstring: 0x3bec
-  __TEXT.__oslogstring: 0x42de
+  __TEXT.__cstring: 0x3c33
+  __TEXT.__oslogstring: 0x42f8
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__unwind_info: 0xb68
   __TEXT.__objc_classname: 0x37c
-  __TEXT.__objc_methname: 0x9f9a
+  __TEXT.__objc_methname: 0xa04c
   __TEXT.__objc_methtype: 0x10b8
-  __TEXT.__objc_stubs: 0x8740
-  __DATA_CONST.__got: 0x980
-  __DATA_CONST.__const: 0x1558
+  __TEXT.__objc_stubs: 0x8800
+  __DATA_CONST.__got: 0x988
+  __DATA_CONST.__const: 0x1568
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3758
-  __DATA_CONST.__objc_selrefs: 0x2450
+  __DATA_CONST.__objc_selrefs: 0x2480
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__objc_const: 0xa30
-  __AUTH_CONST.__cfstring: 0x42c0
+  __AUTH_CONST.__cfstring: 0x4320
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0xa8

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: DDBD61F8-E2F4-3775-9419-01D031EAF8F3
-  Functions: 955
-  Symbols:   4386
-  CStrings:  3142
+  UUID: DE077199-AA6F-34E8-8529-94E1197E887C
+  Functions: 956
+  Symbols:   4397
+  CStrings:  3155
 
Symbols:
+ -[MDMParser _installApplicationCouldNotModifyDDMAppsError]
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1507
+ ___block_literal_global.1214
+ ___block_literal_global.1223
+ ___block_literal_global.1387
+ ___block_literal_global.1389
+ ___block_literal_global.1421
+ ___block_literal_global.1426
+ ___block_literal_global.1498
+ _kDMCDeclarativeDeviceManagement
+ _kInstalledApplicationListKeySource
+ _kMCDMDAppPropertyKeySourceIdentifier
+ _objc_msgSend$_installApplicationCouldNotModifyDDMAppsError
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$mdmAppInstallationSourceIdentifierWithDefaultValue:
+ _objc_msgSend$setSourceIdentifier:
+ _objc_msgSend$sourceIdentifier
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1504
- ___block_literal_global.1211
- ___block_literal_global.1220
- ___block_literal_global.1384
- ___block_literal_global.1386
- ___block_literal_global.1418
- ___block_literal_global.1423
- ___block_literal_global.1495
CStrings:
+ "MDM_ERROR_COULD_NOT_MODIFY_APPS_MANAGED_BY_DDM"
+ "No MDM installation found"
+ "Source"
+ "_installApplicationCouldNotModifyDDMAppsError"
+ "array"
+ "arrayByAddingObjectsFromArray:"
+ "mdmAppInstallationSourceIdentifierWithDefaultValue:"
+ "setSourceIdentifier:"
+ "sourceIdentifier"

```
