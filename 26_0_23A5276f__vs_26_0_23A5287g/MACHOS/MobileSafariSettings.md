## MobileSafariSettings

> `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings`

```diff

-7622.1.16.10.3
-  __TEXT.__text: 0x53590
+7622.1.18.10.3
+  __TEXT.__text: 0x5357c
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0xc480
+  __TEXT.__objc_stubs: 0xc4a0
   __TEXT.__objc_methlist: 0x431c
-  __TEXT.__objc_methname: 0x10f68
+  __TEXT.__objc_methname: 0x10f72
   __TEXT.__objc_classname: 0x1070
   __TEXT.__objc_methtype: 0x26b2
   __TEXT.__const: 0x464
-  __TEXT.__cstring: 0x5554
+  __TEXT.__cstring: 0x5564
   __TEXT.__ustring: 0x70a
   __TEXT.__gcc_except_tab: 0x1ea8
   __TEXT.__oslogstring: 0x953

   __DATA_CONST.__auth_got: 0x848
   __DATA_CONST.__got: 0xdd8
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA_CONST.__const: 0x2218
-  __DATA_CONST.__cfstring: 0x4bc0
+  __DATA_CONST.__const: 0x2220
+  __DATA_CONST.__cfstring: 0x4be0
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x138

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8876F648-251B-36AE-853F-F5BDC763FA56
+  UUID: 197BF5A2-F4D7-38AD-AAAA-BFED28B65D79
   Functions: 1550
-  Symbols:   5312
-  CStrings:  4160
+  Symbols:   5314
+  CStrings:  4162
 
Symbols:
+ -[SafariLockdownModePerSitePreferenceSettingsController confirmationPromptStringsForSpecifierChangeIfNeeded:fromValue:toValue:]
+ -[SafariPerSitePreferenceSettingsController confirmationPromptStringsForSpecifierChangeIfNeeded:fromValue:toValue:]
+ _objc_msgSend$_preferenceValueForSpecifier:
+ _objc_msgSend$confirmationPromptStringsForSpecifierChangeIfNeeded:fromValue:toValue:
+ _sidebarWidthDefaultsKey
- -[SafariLockdownModePerSitePreferenceSettingsController confirmationPromptStringsForSpecifierChangeIfNeeded:toValue:]
- -[SafariPerSitePreferenceSettingsController confirmationPromptStringsForSpecifierChangeIfNeeded:toValue:]
- _objc_msgSend$confirmationPromptStringsForSpecifierChangeIfNeeded:toValue:
Functions:
~ -[SafariPerSitePreferenceSettingsController _setPreferenceValue:forSpecifier:] : 584 -> 612
~ -[SafariSettingsController specifiers] : 5040 -> 4944
~ -[SafariLockdownModePerSitePreferenceSettingsController confirmationPromptStringsForSpecifierChangeIfNeeded:toValue:] -> -[SafariLockdownModePerSitePreferenceSettingsController confirmationPromptStringsForSpecifierChangeIfNeeded:fromValue:toValue:] : 448 -> 496
CStrings:
+ "SidebarWidth"
+ "confirmationPromptStringsForSpecifierChangeIfNeeded:fromValue:toValue:"
- "confirmationPromptStringsForSpecifierChangeIfNeeded:toValue:"

```
