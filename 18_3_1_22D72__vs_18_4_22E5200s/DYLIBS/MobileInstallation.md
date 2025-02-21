## MobileInstallation

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

```diff

-1378.60.22.0.0
-  __TEXT.__text: 0x1f24c
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0xc58
-  __TEXT.__cstring: 0x48d4
-  __TEXT.__gcc_except_tab: 0x9c4
+1378.100.33.0.0
+  __TEXT.__text: 0x201b0
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0xfd4
+  __TEXT.__cstring: 0x49c7
+  __TEXT.__gcc_except_tab: 0xa08
   __TEXT.__const: 0x40
   __TEXT.__oslogstring: 0x43
-  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__unwind_info: 0xa48
   __TEXT.__objc_classname: 0x166
-  __TEXT.__objc_methname: 0x3c1a
-  __TEXT.__objc_methtype: 0x1010
-  __TEXT.__objc_stubs: 0x2a00
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x928
+  __TEXT.__objc_methname: 0x3c35
+  __TEXT.__objc_methtype: 0x1030
+  __TEXT.__objc_stubs: 0x29e0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x930
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba8
+  __DATA_CONST.__objc_selrefs: 0xbf8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x488
+  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x2860
-  __AUTH_CONST.__objc_const: 0x1c10
+  __AUTH_CONST.__objc_const: 0x15c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x30
   __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x240
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x60
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 659
-  Symbols:   869
-  CStrings:  1145
+  Functions: 680
+  Symbols:   892
+  CStrings:  1149
 
Symbols:
+ _MobileInstallationCancelUpdateForStagedIdentifiersWithError
+ _MobileInstallationGetAllStagedUpdateIdentifiers
+ _MobileInstallationInstallParallelPlaceholderForStagedUpdate
+ _MobileInstallationMakeStagedUpdateLiveForIdentifier
+ _objc_retain_x9
- _MobileInstallationCancelStagedUpdateForUUIDWithError
- _MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError
CStrings:
+ "-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_3"
+ "-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]_block_invoke_3"
+ "MobileInstallationCancelUpdateForStagedIdentifiersWithError"
+ "MobileInstallationGetAllStagedUpdateIdentifiers"
+ "MobileInstallationInstallParallelPlaceholderForStagedUpdate"
+ "MobileInstallationMakeStagedUpdateLiveForIdentifier"
+ "Staged Update Placeholder"
+ "allStagedUpdatesWithCompletion:"
+ "cancelUpdateForStagedIdentifiers:completion:"
+ "finalizeStagedInstallForIdentifier:returningResultInfo:completion:"
+ "installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "-[MIInstallerClient finalizeStagedInstallForUUID:returningResultInfo:completion:]_block_invoke_3"
- "MobileInstallationCancelStagedUpdateForUUIDWithError"
- "MobileInstallationMakeStagedApplicationUpdateLiveForIdentityWithError"
- "cancelUpdateForStagedUUID:completion:"
- "dictionaryWithContentsOfURL:"
- "finalizeStagedInstallForUUID:returningResultInfo:completion:"
- "itemDoesNotExistOrIsNotDirectoryAtURL:"
- "itemIsDirectoryAtURL:error:"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
