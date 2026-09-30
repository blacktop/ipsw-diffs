## SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

```diff

-55579.40.2.0.0
-  __TEXT.__text: 0x2c34c
-  __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_stubs: 0x4e60
-  __TEXT.__objc_methlist: 0x1e84
-  __TEXT.__const: 0x149
-  __TEXT.__cstring: 0x2e55
-  __TEXT.__gcc_except_tab: 0x424
-  __TEXT.__oslogstring: 0x287e
-  __TEXT.__objc_methname: 0x52f8
-  __TEXT.__objc_classname: 0x623
-  __TEXT.__objc_methtype: 0x16be
+55579.100.16.0.0
+  __TEXT.__text: 0x2d148
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_stubs: 0x50e0
+  __TEXT.__objc_methlist: 0x27dc
+  __TEXT.__const: 0x169
+  __TEXT.__cstring: 0x2ebb
+  __TEXT.__gcc_except_tab: 0x440
+  __TEXT.__oslogstring: 0x29be
+  __TEXT.__objc_methname: 0x5531
+  __TEXT.__objc_classname: 0x636
+  __TEXT.__objc_methtype: 0x16d4
   __TEXT.__ustring: 0x156e
   __TEXT.__dlopen_cstrs: 0x10d
-  __TEXT.__unwind_info: 0x978
-  __DATA_CONST.__auth_got: 0x928
-  __DATA_CONST.__got: 0x4f0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__cfstring: 0x2880
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __TEXT.__unwind_info: 0x9b0
+  __DATA_CONST.__auth_got: 0x930
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x970
+  __DATA_CONST.__cfstring: 0x28c0
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x1c0
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x5770
-  __DATA.__objc_selrefs: 0x1620
-  __DATA.__objc_ivar: 0x370
-  __DATA.__objc_data: 0x1130
+  __DATA.__objc_const: 0x47e0
+  __DATA.__objc_selrefs: 0x1a50
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_data: 0x1180
   __DATA.__data: 0x492
-  __DATA.__bss: 0x17d
+  __DATA.__bss: 0x195
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
   - /System/Library/PrivateFrameworks/PlatformSSO.framework/Versions/A/PlatformSSO
   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F790510D-72B8-3959-9515-455CF4FDC7D5
-  Functions: 1020
-  Symbols:   711
-  CStrings:  2431
+  UUID: 6CC7F487-276D-3C1D-92DB-56349BD16007
+  Functions: 1058
+  Symbols:   719
+  CStrings:  2470
 
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
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
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
+ "com.apple.SecurityAgent"
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
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "initWithTokenID:serverEndpoint:targetUID:"

```
