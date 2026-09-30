## SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

```diff

-55579.40.2.0.0
-  __TEXT.__text: 0x206d7
-  __TEXT.__stubs: 0x58e
-  __TEXT.__const: 0xb0
-  __TEXT.__objc_methname: 0x4866
-  __TEXT.__oslogstring: 0x24d7
-  __TEXT.__objc_classname: 0x32c
-  __TEXT.__objc_methtype: 0x1577
-  __TEXT.__cstring: 0x1d16
-  __TEXT.__gcc_except_tab: 0x3f4
+55579.100.16.0.0
+  __TEXT.__text: 0x216e7
+  __TEXT.__stubs: 0x594
+  __TEXT.__const: 0xe0
+  __TEXT.__objc_methname: 0x4a9f
+  __TEXT.__oslogstring: 0x2647
+  __TEXT.__objc_classname: 0x33f
+  __TEXT.__objc_methtype: 0x158d
+  __TEXT.__cstring: 0x1d65
+  __TEXT.__gcc_except_tab: 0x40c
   __TEXT.__ustring: 0x776
   __TEXT.__dlopen_cstrs: 0x11d
-  __TEXT.__unwind_info: 0x6c0
-  __DATA_CONST.__got: 0xb48
-  __DATA_CONST.__const: 0x760
-  __DATA_CONST.__cfstring: 0x1860
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x6f0
+  __DATA_CONST.__got: 0xb78
+  __DATA_CONST.__const: 0x790
+  __DATA_CONST.__cfstring: 0x1880
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x6388
-  __DATA.__objc_selrefs: 0x11a0
-  __DATA.__objc_ivar: 0x4e0
-  __DATA.__objc_data: 0xb40
+  __DATA.__objc_const: 0x65e8
+  __DATA.__objc_selrefs: 0x1238
+  __DATA.__objc_ivar: 0x518
+  __DATA.__objc_data: 0xba8
   __DATA.__data: 0x490
-  __DATA.__bss: 0x140
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
-  UUID: 9C383BF0-6DAC-3E74-9B6A-2723D874396F
-  Functions: 711
-  Symbols:   500
-  CStrings:  1870
+  UUID: C3E8E7EA-6038-35FD-A07E-C8169251E831
+  Functions: 739
+  Symbols:   508
+  CStrings:  1907
 
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
