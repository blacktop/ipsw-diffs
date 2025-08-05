## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x24b30
-  __TEXT.__auth_stubs: 0x800
+50.0.0.0.0
+  __TEXT.__text: 0x24c58
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0x3958
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x61c
-  __TEXT.__cstring: 0x2ff4
+  __TEXT.__cstring: 0x3062
   __TEXT.__ustring: 0x46
   __TEXT.__unwind_info: 0xc98
   __TEXT.__objc_classname: 0x9c6
-  __TEXT.__objc_methname: 0xac3e
+  __TEXT.__objc_methname: 0xac4d
   __TEXT.__objc_methtype: 0x1f63
-  __TEXT.__objc_stubs: 0x7840
-  __DATA_CONST.__got: 0x738
+  __TEXT.__objc_stubs: 0x7860
+  __DATA_CONST.__got: 0x740
   __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2860
+  __DATA_CONST.__objc_selrefs: 0x2868
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x2620
+  __AUTH_CONST.__cfstring: 0x25e0
   __AUTH_CONST.__objc_const: 0x5660
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E004B65E-166E-351D-9A93-59E666C9DBFF
+  UUID: 9151314F-75B7-36E5-8208-8321166203A5
   Functions: 1112
-  Symbols:   4415
-  CStrings:  2621
+  Symbols:   4418
+  CStrings:  2618
 
Symbols:
+ _DMCSendNavUIUpdatedNotification
+ _kMDMSettingsURLDownloadedProfileComponent
+ _kMDMSettingsURLMDMMigrationComponent
+ _kMDMSettingsURLManagedAccountComponent
+ _kMDMSettingsURLProfilesUIComponent
+ _kMDMSettingsURLResourceID
+ _kMDMSettingsURLVPNComponent
+ _objc_msgSend$setIdentifier:
- _PSIDKey
- _kMCSettingsURLComponentProfilesOverview
- _kMCSettingsURLManagedAppleIDComponent
- _kMCSettingsURLProfilePurgatoryInstallationComponent
- _kMCSettingsURLProfilesOverview
Functions:
~ -[MCInstallationConsentViewController setShowInstall:] : 196 -> 228
~ -[MCInstallProfileViewController initWithInstallableProfileData:fromSource:] : 364 -> 388
~ -[MCInstallProfileViewController setInstallState:animated:] : 260 -> 300
~ -[MCUIAppSignerViewController _appSignersDidChange] : 320 -> 344
~ -[MCUIAppSignerViewController setAppSigner:] : 184 -> 208
~ -[MCUIAppSignerViewController _trust] : 272 -> 276
~ -[MCUIAppSignerViewController _verify] : 272 -> 276
~ -[MCUIAppSignerViewController _removeAppSignerApps] : 348 -> 352
~ -[MCUIBundleController specifier] : 236 -> 224
~ -[MCUIListController handleURL:] : 256 -> 324
~ -[MCUISpecifierProvider _specifierForProfile:profileInstalled:] : 424 -> 456
~ -[UIViewController(MCUI) MCUIShowProgressInNavBar] : 236 -> 260
~ -[UIViewController(MCUI) MCUIHideProgressInNavBarShowBackButton:] : 256 -> 280
~ -[MCURLListenerListController handleURL:] : 360 -> 364
CStrings:
+ "MCUIListController missing username when handling ManagedAccount URL path '%@' from sender: %@ | %@"
+ "MCUIListController presenting '%@' from ManagedAccount URL path '%@' from sender: %@"
+ "MCURLListenerListController handling URL path '%@' from sender: %@"
+ "MCURLListenerListController ignoring URL path '%@' from sender: %@"
+ "setIdentifier:"
- "MCUIListController handling URL path %@ from sender %@"
- "MCURLListenerListController handling URL path %@ from sender %@"
- "MCURLListenerListController ignoring URL path %@ from sender %@"
- "MDMMigration"
- "VPN"
- "username"

```
