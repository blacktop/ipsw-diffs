## com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService`

```diff

-1270.80.2.0.0
-  __TEXT.__text: 0x120bc
+1270.102.7.0.0
+  __TEXT.__text: 0x12808
   __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_stubs: 0x1940
   __TEXT.__objc_methlist: 0x5b0
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__cstring: 0x5303
-  __TEXT.__objc_methname: 0x2297
+  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__cstring: 0x557c
+  __TEXT.__objc_methname: 0x22e5
   __TEXT.__objc_classname: 0x129
-  __TEXT.__objc_methtype: 0x6cc
+  __TEXT.__objc_methtype: 0x6d0
   __TEXT.__oslogstring: 0x277
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x3a0
   __DATA_CONST.__auth_got: 0x770
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x3d8
-  __DATA_CONST.__cfstring: 0x2d80
+  __DATA_CONST.__cfstring: 0x2f40
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0xfb8
-  __DATA.__objc_selrefs: 0x760
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_selrefs: 0x778
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
+  - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5514CE5-457F-32E6-A987-63D865C127A2
-  Functions: 244
-  Symbols:   384
-  CStrings:  1258
+  UUID: 59671308-A52E-3CF9-9D9F-53A2B6D66B71
+  Functions: 259
+  Symbols:   401
+  CStrings:  1290
 
Symbols:
+ _MIArrayFilteredToContainOnlyClass
+ _MICopyDataProtectionClassEntitlement
+ _MICopyDataProtectionIfAvailableEntitlement
+ _MICopyMemoryTransferAcceptEntitlement
+ _MICopyMemoryTransferSendEntitlement
+ _MIGetFirstTrueBooleanEntitlement
+ _MIHasAllowJITEntitlement
+ _MIHasBrowserAppInstallationEntitlement
+ _MIHasBrowserEngineContentEntitlement
+ _MIHasBrowserEngineHostEntitlement
+ _MIHasBrowserEngineNetworkingEntitlement
+ _MIHasBrowserEngineRenderingEntitlement
+ _MIHasDefaultBrowserEntitlement
+ _MIHasEmbeddedBrowserEngineEntitlement
+ _MIHasMarketplaceEntitlement
+ _OBJC_CLASS_$_MIInstallOptions
+ _OBJC_CLASS_$_MIStoreMetadata
CStrings:
+ "22:32:33"
+ "DataProtectionClass"
+ "Feb 16 2024"
+ "Options parameter is not an instance of MIInstallOptions; found %@"
+ "T@\"NSString\",?,R,C"
+ "com.apple.developer.browser.app-installation"
+ "com.apple.developer.cs.allow-jit"
+ "com.apple.developer.default-data-protection"
+ "com.apple.developer.default-data-protection-if-available"
+ "com.apple.developer.embedded-web-browser-engine"
+ "com.apple.developer.marketplace.app-installation"
+ "com.apple.developer.memory.transfer-accept"
+ "com.apple.developer.memory.transfer-send"
+ "com.apple.developer.web-browser"
+ "com.apple.developer.web-browser-engine.host"
+ "com.apple.developer.web-browser-engine.networking"
+ "com.apple.developer.web-browser-engine.rendering"
+ "com.apple.developer.web-browser-engine.webcontent"
+ "data-protection-class"
+ "metadataFromPlistAtURL:error:"
+ "performAPFSClone"
+ "propertyListDataWithError:"
+ "setDistributorInfo:"
+ "v40@0:8@\"NSURL\"16@\"MIInstallOptions\"24@?<v@?@\"NSURL\"B@\"NSError\">32"
- "18:41:20"
- "Dec 20 2023"
- "PerformAPFSClone"
- "copyItemIfExistsAtURL:toURL:error:"
- "options parameter is not a valid dictionary"
- "v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSURL\"B@\"NSError\">32"

```
