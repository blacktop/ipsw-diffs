## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-631.82.1.0.0
-  __TEXT.__text: 0x62d10
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x2ee0
+699.100.7.0.0
+  __TEXT.__text: 0x64918
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x3d50
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xdd70
-  __TEXT.__oslogstring: 0x7697
-  __TEXT.__gcc_except_tab: 0x1ab8
-  __TEXT.__unwind_info: 0x15f0
-  __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0x9d26
-  __TEXT.__objc_methtype: 0x21be
-  __TEXT.__objc_stubs: 0x5980
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x19b8
-  __DATA_CONST.__objc_classlist: 0x180
+  __TEXT.__cstring: 0xe017
+  __TEXT.__oslogstring: 0x76a6
+  __TEXT.__gcc_except_tab: 0x1af4
+  __TEXT.__unwind_info: 0x1660
+  __TEXT.__objc_classname: 0x84f
+  __TEXT.__objc_methname: 0x9ffb
+  __TEXT.__objc_methtype: 0x222d
+  __TEXT.__objc_stubs: 0x5ac0
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__const: 0x1a70
+  __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d78
+  __DATA_CONST.__objc_selrefs: 0x1e90
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x54c0
-  __AUTH_CONST.__objc_const: 0xbc08
+  __AUTH_CONST.__cfstring: 0x5600
+  __AUTH_CONST.__objc_const: 0xa5d8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1b4
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x8a8
   __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0xeb0
+  __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1814
-  Symbols:   2215
-  CStrings:  3244
+  Functions: 1855
+  Symbols:   2248
+  CStrings:  3289
 
Symbols:
+ _OBJC_CLASS_$_IXDefaultAppMetadata
+ _OBJC_METACLASS_$_IXDefaultAppMetadata
+ __kCFBundleShortVersionStringKey
- _strcmp
CStrings:
+ "\x1e"
+ "%s: Failed to find an existing app for delta package with bundle ID %@ : %@"
+ "+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:completion:]_block_invoke"
+ "+[IXAppInstallCoordinator defaultAppMetadataForAppIdentity:error:]_block_invoke"
+ "+[IXAppInstallCoordinator defaultAppMetadataListWithCompletion:]_block_invoke"
+ "+[IXAppInstallCoordinator defaultAppMetadataListWithError:]_block_invoke"
+ "Failed to find an existing app for delta package with bundle ID %@"
+ "Failed to stage background update."
+ "IXAppCoordinationStateReadyForStaging"
+ "IXAppCoordinationStateStagingPending"
+ "IXDefaultAppMetadata"
+ "NSAccentColorName"
+ "T@\"IXApplicationIdentity\",R,N,V_identity"
+ "T@\"NSDictionary\",C,N,V_uiLaunchScreen"
+ "T@\"NSString\",C,N,V_accentColorName"
+ "T@\"NSString\",C,N,V_bundleShortVersionString"
+ "TQ,R,N,V_appType"
+ "TQ,R,N,V_offloadAnswer"
+ "UILaunchScreen"
+ "_accentColorName"
+ "_appType"
+ "_bundleShortVersionString"
+ "_offloadAnswer"
+ "_remote_defaultAppMetadataForAppIdentity:completion:"
+ "_remote_defaultAppMetadataListWithCompletion:"
+ "_uiLaunchScreen"
+ "accentColorName"
+ "appType"
+ "bundleShortVersionString"
+ "com.apple.parallelpatcharchive."
+ "defaultAppMetadataForAppIdentity:completion:"
+ "defaultAppMetadataForAppIdentity:error:"
+ "defaultAppMetadataListWithCompletion:"
+ "defaultAppMetadataListWithError:"
+ "initWithAppIdentity:appType:offloadAnswer:"
+ "offloadAnswer"
+ "setAccentColorName:"
+ "setBundleShortVersionString:"
+ "setUiLaunchScreen:"
+ "uiLaunchScreen"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "v24@?0@\"IXDefaultAppMetadata\"8@\"NSError\"16"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "v32@0:8@\"IXApplicationIdentity\"16@?<v@?@\"IXDefaultAppMetadata\"@\"NSError\">24"
- "\x1b"
- "%s: Skipping incomplete app extension in delta package at %@"
- "Info.plist"
- "PPBundleMetadata"

```
