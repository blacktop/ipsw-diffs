## loginwindow

> `/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns/loginwindow.profileDomainPlugin/Contents/MacOS/loginwindow`

```diff

-  __TEXT.__text: 0x5100
+  __TEXT.__text: 0x550c
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x24ee
-  __TEXT.__oslogstring: 0x9e2
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x298f
+  __TEXT.__oslogstring: 0xdb7
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__objc_methname: 0x707
   __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methtype: 0xd4
   __TEXT.__unwind_info: 0x160
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__cfstring: 0x13a0
+  __DATA_CONST.__cfstring: 0x1420
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 83
   Symbols:   159
-  CStrings:  540
+  CStrings:  564
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
Functions:
~ sub_1884 : 844 -> 852
~ sub_2a20 -> sub_2a28 : 2048 -> 2120
~ sub_36b0 -> sub_3700 : 2812 -> 3728
~ sub_43b0 -> sub_4794 : 712 -> 752
CStrings:
+ "ForceCaptivePortalConnectionFromLockScreen"
+ "ForceWifiConfigurationOnLockScreen"
+ "InstallOrRemoveLoginwindowPayload MIG_SetAutoLogin failed for user '%s' err = %d - autologin will NOT occur on next boot"
+ "InstallOrRemoveLoginwindowPayload autologin NOT configured for user '%s': profile is not from a user-approved MDM enrollment (UAMDM required)"
+ "InstallOrRemoveLoginwindowPayload autologin NOT configured: user '%s' does not exist on this device"
+ "InstallOrRemoveLoginwindowPayload autologin configured for user '%s'"
+ "InstallOrRemoveLoginwindowPayload autologin password for user '%s' failed verifyPassword - autologin will NOT be configured (check that the password in the MDM payload matches the local account)"
+ "InstallOrRemoveLoginwindowPayload autologin removal MIG_SetAutoLogin err = %d"
+ "InstallOrRemoveLoginwindowPayload autologin user '%s' has no password in payload - deferring to loginwindow prompt"
+ "InstallOrRemoveLoginwindowPayload autologin user '%s' not found in local node - cannot configure autologin (user must exist locally before profile is installed)"
+ "str_loginwindow_Details_ForceCaptivePortalConnectionFromLockScreen"
+ "str_loginwindow_Details_ForceWifiConfigurationOnLockScreen"

```
