## profiled

> `/usr/libexec/profiled`

```diff

-2352.1.3.0.0
-  __TEXT.__text: 0x9d960
-  __TEXT.__auth_stubs: 0x2100
-  __TEXT.__objc_stubs: 0xfa40
+2381.2.4.0.0
+  __TEXT.__text: 0x9da84
+  __TEXT.__auth_stubs: 0x2130
+  __TEXT.__objc_stubs: 0xfa60
   __TEXT.__objc_methlist: 0x4c8c
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x194c
   __TEXT.__oslogstring: 0xcb90
-  __TEXT.__cstring: 0x8b27
-  __TEXT.__objc_methname: 0x1330c
+  __TEXT.__cstring: 0x8b5b
+  __TEXT.__objc_methname: 0x1335a
   __TEXT.__objc_classname: 0xb36
   __TEXT.__objc_methtype: 0x1ff1
   __TEXT.__unwind_info: 0x16a0
-  __DATA_CONST.__auth_got: 0x1090
-  __DATA_CONST.__got: 0x1b80
+  __DATA_CONST.__auth_got: 0x10a8
+  __DATA_CONST.__got: 0x1b90
   __DATA_CONST.__const: 0x1b38
-  __DATA_CONST.__cfstring: 0x8300
+  __DATA_CONST.__cfstring: 0x8320
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x7218
-  __DATA.__objc_selrefs: 0x4340
+  __DATA.__objc_selrefs: 0x4348
   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea

   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1921
-  Symbols:   1454
-  CStrings:  4885
+  Symbols:   1459
+  CStrings:  4887
 
Symbols:
+ _MCFeatureAllowedExternalIntelligenceWorkspaceIDs
+ _MCFeatureDefaultBrowserPromptingAllowed
+ _MCKeybagClearPasscodeGenerationCaches
+ _MCSendClearPasscodeGenerationCachesNotification
+ _MCSendExternalIntelligenceWorkspaceListChangedNotification
CStrings:
+ "MCCleanupMigrator.migrateCleanupMigratorWithContext"
+ "intersectedValuesForFeature:changedBetweenOldRestrictions:andNewRestrictions:"

```
