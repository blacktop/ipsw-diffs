## AppleAccountSettings

> `/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings`

```diff

-550.1.1.0.0
-  __TEXT.__text: 0x31d20
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_stubs: 0x7800
-  __TEXT.__objc_methlist: 0x2838
+553.125.1.0.0
+  __TEXT.__text: 0x31bc0
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x7760
+  __TEXT.__objc_methlist: 0x2850
   __TEXT.__const: 0x434
   __TEXT.__cstring: 0x1f97
-  __TEXT.__oslogstring: 0x3976
+  __TEXT.__oslogstring: 0x3aa6
   __TEXT.__objc_classname: 0x649
-  __TEXT.__objc_methname: 0xa385
-  __TEXT.__objc_methtype: 0x283f
-  __TEXT.__gcc_except_tab: 0x5e0
+  __TEXT.__objc_methname: 0xa376
+  __TEXT.__objc_methtype: 0x28db
+  __TEXT.__gcc_except_tab: 0x5ac
   __TEXT.__dlopen_cstrs: 0x1bb
   __TEXT.__constg_swiftt: 0x288
   __TEXT.__swift5_typeref: 0x2f8

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__unwind_info: 0xd08
+  __TEXT.__unwind_info: 0xce0
   __TEXT.__eh_frame: 0xc0
-  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__auth_got: 0x820
   __DATA_CONST.__got: 0x950
   __DATA_CONST.__auth_ptr: 0xc8
-  __DATA_CONST.__const: 0x1370
-  __DATA_CONST.__cfstring: 0x1c80
+  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__cfstring: 0x1ca0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5ea8
-  __DATA.__objc_selrefs: 0x2930
+  __DATA.__objc_const: 0x5ec0
+  __DATA.__objc_selrefs: 0x2928
   __DATA.__objc_ivar: 0x2e8
   __DATA.__objc_data: 0x878
   __DATA.__data: 0xe18

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
+  - /System/Library/PrivateFrameworks/iCloudCalendarUnifiedSettings.framework/iCloudCalendarUnifiedSettings
+  - /System/Library/PrivateFrameworks/iCloudMailUnifiedSettings.framework/iCloudMailUnifiedSettings
   - /System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota
   - /System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI
   - /System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0A6C1653-DF36-3C45-88EE-EB9E33F4B99B
-  Functions: 1117
-  Symbols:   589
-  CStrings:  2767
+  UUID: 91B1F5A2-3D91-3E33-89F2-105821069B05
+  Functions: 1115
+  Symbols:   590
+  CStrings:  2773
 
Symbols:
+ _OBJC_CLASS_$_iCloudCalendarUnifiedSettingsProviderObjc
+ _OBJC_CLASS_$_iCloudMailUnifiedSettingsProviderObjc
+ _protocol_getMethodDescription
- _OBJC_CLASS_$_AAUIEDPStateValidator
- _OBJC_CLASS_$_CDPStateSwiftUIProvider
CStrings:
+ "#40@0:8@\"ACAccount\"16@\"PSSpecifier\"24@\"UIViewController\"32"
+ "#40@0:8@16@24@32"
+ "ACUIAccountViewsProviderProtocol defines viewControllerClassForViewingAccount:specifier:presentingVC. Returning AAUIAppleAccountViewController."
+ "ACUIAccountViewsProviderProtocol does not define viewControllerClassForViewingAccount:specifier:presentingVC."
+ "Account is not primary. Returning AAUIAppleAccountViewController."
+ "Failed to save authKit account with SignOutInProgress = NO. Error: %@"
+ "Failed to save authKit account with SignOutInProgress = YES. Error: %@"
+ "PresentingVC is nil, not presenting Mail settings."
+ "Received specifier with bundleID: %@"
+ "Successfully saved authKit account with SignOutInProgress = NO."
+ "Successfully saved authKit account with SignOutInProgress = YES."
+ "com.apple.mobilecal"
+ "com.apple.mobilemail"
+ "initWithPresenter:"
+ "navigateToiCloudCalendarSettingsWithDeeplink:"
+ "navigateToiCloudMailSettingsWithDeeplink:"
+ "searchController:textViewDidChangeSize:"
+ "searchController:textViewWillChangeSize:"
+ "v40@0:8@\"CNAutocompleteSearchController\"16{CGSize=dd}24"
+ "v40@0:8@16{CGSize=dd}24"
+ "viewControllerClassForViewingAccount:specifier:presentingVC:"
- "%@ - Unable to fetch EDP token after repair. Stopping flow with error %@"
- "%@ - Unable to repair EDP state. Stopping flow with error %@"
- "Attempting to repair EDP state."
- "Handling URL to show edp recovery token settings...."
- "Presenting EDP Token Spyglass Pane"
- "Unable to show EDP token screen because strongCDPController is nil."
- "Unable to show EDP token screen because strongSelf is nil."
- "_handleEDPTokenPane"
- "_showEDPTokenPaneWithToken:onViewController:"
- "cdpContextForPrimaryAccount"
- "edpRecoveryTokenWindow"
- "fetchEDPTokenWithCompletion:"
- "makeSwiftUIViewForEDPTokenInSpyglassWithRecoveryToken:presentingViewController:"
- "repairPrimaryAppleAccountEDPStateWithCompletion:"
- "setPassword:"
- "v24@?0@\"NSArray\"8@\"NSError\"16"

```
