## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x41cbc
+20.4.16.0.0
+  __TEXT.__text: 0x42df0
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x524c
+  __TEXT.__objc_methlist: 0x6968
   __TEXT.__const: 0x1d0
-  __TEXT.__oslogstring: 0x1809
-  __TEXT.__cstring: 0x27fb
-  __TEXT.__gcc_except_tab: 0x720
+  __TEXT.__oslogstring: 0x196d
+  __TEXT.__cstring: 0x28aa
+  __TEXT.__gcc_except_tab: 0x744
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x1230
+  __TEXT.__unwind_info: 0x1258
   __TEXT.__objc_classname: 0x109f
-  __TEXT.__objc_methname: 0x12460
-  __TEXT.__objc_methtype: 0x44cb
-  __TEXT.__objc_stubs: 0xc2a0
-  __DATA_CONST.__got: 0xcf8
-  __DATA_CONST.__const: 0xd38
+  __TEXT.__objc_methname: 0x1293b
+  __TEXT.__objc_methtype: 0x459c
+  __TEXT.__objc_stubs: 0xc5c0
+  __DATA_CONST.__got: 0xd48
+  __DATA_CONST.__const: 0xdf8
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b48
+  __DATA_CONST.__objc_selrefs: 0x4458
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x3e8
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x2ca0
-  __AUTH_CONST.__objc_const: 0x12cf8
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x2c60
+  __AUTH_CONST.__objc_const: 0x103e0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup

   - /System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1885
-  Symbols:   2571
-  CStrings:  3953
+  Functions: 1894
+  Symbols:   2599
+  CStrings:  3998
 
Symbols:
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_MCACMEPayload
+ _OBJC_CLASS_$_RMErSSOStore
+ _OBJC_CLASS_$_UITraitCollection
+ _PSIconUTTypeIdentifierKey
+ _PSLazyIconAppID
+ _PSLazyIconLoading
+ _kISImageDescriptorSpotlight
+ _kISImageDescriptorTableUIName
CStrings:
+ "\a"
+ "@\"NSArray\"24@0:8@\"NSArray\"16"
+ "@48@0:8@16@24@32Q40"
+ "@56@0:8@16@24@32@40@48"
+ "Bundle ID"
+ "DMC Enrollment App Lockup"
+ "DMCReauthSpecifierProvider ignoring reauth presentation because we are already reauthing"
+ "Failed to parse profile data for consent"
+ "Failed to parse profile data for management details"
+ "Missing ErSSO profile: %{public}@"
+ "TB,N,V_isReauthing"
+ "UI_ESSO_REQUIRED_APP_BLURB"
+ "_bundleIDForPluginViewModel:"
+ "_cellDataForESSODeviceDisclosure"
+ "_createLockupRequestAndViewGroupWithITunesItemID:completionHandler:"
+ "_imageForIcon:descriptorName:"
+ "_isReauthing"
+ "_setDismissedCompletionBlockForPresenter:"
+ "_setIcon:forSpecifier:"
+ "_setIconForSpecifier:symbol:viewModel:"
+ "accessibilityContrast"
+ "appIconForBundleID:"
+ "com.apple.application-icon.icloud"
+ "com.apple.graphic-icon.account"
+ "com.apple.graphic-icon.device-management"
+ "com.apple.graphic-icon.mdm"
+ "com.apple.graphic-icon.passcode"
+ "com.apple.mobilenotes"
+ "currentTraitCollection"
+ "enrollmentFlowControllerWithPresenter:managedConfigurationHelper:rmStoreHelper:"
+ "ensureActivationWithCompletionHandler:"
+ "extensionIDsFromESSOProfileIdentifiers:"
+ "iconForTypeID:large:"
+ "imageDescriptorNamed:"
+ "initWithBundleIdentifier:"
+ "initWithDelegate:managedAppleID:profile:requiredAppRequest:requiredAppViewGroup:"
+ "initWithDelegate:username:profile:enrollmentType:"
+ "initiateDEPPushTokenSyncWithCompletionHandler:"
+ "isReauthing"
+ "layoutDirection"
+ "managed restore, conflicting app bundle IDs: [%{public}@]"
+ "managed restore, restoring app bundle IDs: [%{public}@]"
+ "managed restore, snapshot app bundle IDs: [%{public}@]"
+ "monitorDEPPushTokenIfNeededWithCompletion:"
+ "prepareImageForDescriptor:"
+ "q24@?0@\"ACAccount\"8@\"ACAccount\"16"
+ "requestDeviceErasureWithCompletionHandler:"
+ "requestSoftwareUpdateWithInfoDictionary:completionHandler:"
+ "requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:"
+ "setAccountIconForSpecifier:"
+ "setAppIcon:forSpecifier:"
+ "setAppearance:"
+ "setContrast:"
+ "setDrawBorder:"
+ "setGearIconForSpecifier:"
+ "setIsReauthing:"
+ "setLanguageDirection:"
+ "setLanyardIconForSpecifier:"
+ "setPasscodeIconForSpecifier:"
+ "sortedArrayUsingComparator:"
+ "textField:insertInputSuggestion:"
+ "unassignFromDEPWithCompletionHandler:"
+ "updateCloudConfigurationWithRMAccountIdentifier:"
+ "updateLanguage:locale:completionHandler:"
+ "userInterfaceStyle"
+ "v24@?0@\"ASCLockupRequest\"8@\"ASCLockupViewGroup\"16"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v36@0:8@16s24@28"
+ "v48@0:8@\"NSData\"16@\"NSString\"24Q32@?<v@?B>40"
+ "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
+ "v48@0:8@16@24Q32@?40"
+ "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
- "\b"
- "@20@0:8s16"
- "DMC Enrollment SSO App Lockup"
- "Failed to parse profile data"
- "T@\"UIImage\",&,V_icon"
- "_iconForSymbol:"
- "account-icon"
- "accountIcon"
- "app-icon"
- "appIcon"
- "gear-icon"
- "gear-icon-large"
- "graduationCapIcon"
- "graduationcap-icon"
- "icloud-icon"
- "initWithDelegate:managedAppleID:profile:"
- "initWithDelegate:username:profile:"
- "key-icon"
- "keyIcon"
- "lanyard-icon"
- "lanyardCardIcon"
- "lanyardIcon"
- "lanyardcard-icon"
- "manager:didFinishDeviceTransferPreflight:error:"
- "notes-icon"
- "requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:"
- "v40@0:8@\"MBManager\"16@\"MBDeviceTransferPreflight\"24@\"NSError\"32"

```
