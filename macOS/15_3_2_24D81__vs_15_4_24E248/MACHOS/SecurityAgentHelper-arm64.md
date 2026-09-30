## SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

```diff

-55579.40.2.0.0
-  __TEXT.__text: 0x1e464
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0x4240
-  __TEXT.__objc_methlist: 0x1528
-  __TEXT.__const: 0x108
-  __TEXT.__objc_methname: 0x470f
-  __TEXT.__oslogstring: 0x1f03
-  __TEXT.__objc_classname: 0x32c
-  __TEXT.__objc_methtype: 0x156c
-  __TEXT.__cstring: 0x1d17
-  __TEXT.__gcc_except_tab: 0x3f0
+55579.100.16.0.0
+  __TEXT.__text: 0x1f460
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_stubs: 0x44c0
+  __TEXT.__objc_methlist: 0x1e7c
+  __TEXT.__const: 0x130
+  __TEXT.__objc_methname: 0x4948
+  __TEXT.__oslogstring: 0x2043
+  __TEXT.__objc_classname: 0x33f
+  __TEXT.__objc_methtype: 0x1582
+  __TEXT.__cstring: 0x1d65
+  __TEXT.__gcc_except_tab: 0x40c
   __TEXT.__ustring: 0x776
   __TEXT.__dlopen_cstrs: 0x10d
-  __TEXT.__unwind_info: 0x6f8
-  __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x780
-  __DATA_CONST.__cfstring: 0x1860
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x760
+  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x7b0
+  __DATA_CONST.__cfstring: 0x1880
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x3e50
-  __DATA.__objc_selrefs: 0x12c0
-  __DATA.__objc_ivar: 0x270
-  __DATA.__objc_data: 0x7d0
+  __DATA.__objc_const: 0x2ec0
+  __DATA.__objc_selrefs: 0x16f8
+  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_data: 0x820
   __DATA.__data: 0x490
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x150
   __DATA.__common: 0x28
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/SecurityInterface.framework/Versions/A/SecurityInterface
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
+  - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2FE9CF9C-D35C-3350-97F8-FD63E0082DF1
-  Functions: 740
-  Symbols:   500
-  CStrings:  1851
+  UUID: 52013AA4-A0EC-3F76-806F-DCFDF2AC7956
+  Functions: 762
+  Symbols:   508
+  CStrings:  1888
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMLocalAuthenticationDialogs
+ _OBJC_CLASS_$_PKInstallHistory
+ _OBJC_CLASS_$_PackageKitHelper
+ _OBJC_METACLASS_$_PackageKitHelper
+ _PKInstallRequestItemDate
+ _PKInstallRequestItemDisplayName
+ _PKInstallRequestItemPackageIdentifiers
CStrings:
+ "@\"BMSource\""
+ "@\"NSDate\""
+ "Checking %d PKInstallHistory items."
+ "Class getTKCTKDConnectionClass(void)_block_invoke"
+ "Dialogs"
+ "Donating to %{public}@: <dialogID: %{public}@, bundleID: %{private}@ timeSinceUpdate: %.0f, mechanisms: %{public}@, successfulMechanism: %d, failedMechanisms: %{public}@, actions: %{public}@, failingAction: %d>)"
+ "Last macOS installation found: %@ (%.0f seconds old)"
+ "LocalAuthentication"
+ "Missing PackageKit"
+ "PackageKitHelper"
+ "TKCTKDConnection"
+ "UI"
+ "_biomeActionFailed"
+ "_biomeActions"
+ "_biomeDonation"
+ "_biomeMechanismSuccessful"
+ "_biomeMechanismsFailed"
+ "_biomeMechanismsStarted"
+ "_biomeSource"
+ "_determineLastSystemUpdateWithHistoryItem:"
+ "_lastSystemUpdate"
+ "action:dismissing:"
+ "authMech:started:"
+ "authMech:succeeded:"
+ "com.apple."
+ "defaultHistory"
+ "initWithCTKDEndpoint:targetUID:"
+ "initWithDialogID:bundleID:timeSinceUpdate:mechanisms:successfulMechanism:failedMechanisms:actions:failingAction:"
+ "initWithTokenID:ctkdConnection:"
+ "installedItems"
+ "isGreaterThan:"
+ "lastObject"
+ "numberWithDouble:"
+ "sharedInstance"
+ "source"
+ "timeIntervalSinceLastSystemUpdate"
+ "timeIntervalSinceNow"
- "initWithTokenID:serverEndpoint:targetUID:"

```
