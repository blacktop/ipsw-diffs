## iCloud

> `/Applications/iCloud.app/iCloud`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2710.114.0.0.0
-  __TEXT.__text: 0x16c78
+2710.116.0.0.0
+  __TEXT.__text: 0x16d80
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x3320
   __TEXT.__objc_methlist: 0x10b0
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__cstring: 0x2cba
-  __TEXT.__objc_methname: 0x459b
-  __TEXT.__oslogstring: 0x1c7c
+  __TEXT.__cstring: 0x2ccb
+  __TEXT.__objc_methname: 0x471b
+  __TEXT.__oslogstring: 0x1cab
   __TEXT.__objc_classname: 0x122
   __TEXT.__objc_methtype: 0x1069
   __TEXT.__ustring: 0x2a0
   __TEXT.__unwind_info: 0x438
   __DATA_CONST.__const: 0x748
-  __DATA_CONST.__cfstring: 0x2340
+  __DATA_CONST.__cfstring: 0x2360
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   - /usr/lib/libobjc.A.dylib
   Functions: 298
   Symbols:   230
-  CStrings:  1220
+  CStrings:  1222
 
Functions:
~ sub_1000030c8 : 1168 -> 1220
~ sub_100009174 -> sub_1000091a8 : 680 -> 720
~ sub_100009bc0 -> sub_100009c1c : 248 -> 252
~ sub_10000ec30 -> sub_10000ec90 : 1712 -> 1852
~ sub_100014004 -> sub_1000140f0 : 740 -> 768
~ sub_1000159bc -> sub_100015ac4 : 8 -> 12
~ sub_1000159cc -> sub_100015ad8 : 12 -> 8
CStrings:
+ "Error presenting join share alert: %@"
+ "Failed to initialize application record for selected app verification with bundle id %@, error: %@"
+ "TB,N,V_needsLockScreenPresentation"
+ "_alertContentForAppStoreOperationWithApp:shareMetadata:keyPrefix:titleKeySuffix:bodyKeySuffix:needsLockScreenPresentation:"
+ "_alertContentForDropDownSelectionWithShareName:ownerName:currentUserName:currentUserFormattedUsername:dropDownTitles:locKeyPrefix:needsLockScreenPresentation:"
+ "_alertContentForVettingBindingPromptWithBundleID:shareName:ownerName:shareType:isShortcut:needsLockScreenPresentation:"
+ "_handleURL:invitationToken:needsLockScreenPresentation:unitTestOverrides:"
+ "_needsLockScreenPresentation"
+ "acceptShareWithURL:invitationToken:needsLockScreenPresentation:unitTestOverrides:"
+ "alertContentForAppDownload:shareMetadata:needsLockScreenPresentation:"
+ "alertContentForAppSelectionWithShareName:ownerName:currentUserName:currentUserFormattedUsername:dropDownTitles:needsLockScreenPresentation:"
+ "alertContentForAppStoreAppSelectionWithShareName:ownerName:currentUserName:currentUserFormattedUsername:dropDownTitles:needsLockScreenPresentation:"
+ "alertContentForAppUpdate:shareMetadata:needsLockScreenPresentation:"
+ "alertContentForFullVettingBindingPromptWithBundleID:shareName:ownerName:shareType:needsLockScreenPresentation:"
+ "alertContentForShortcutVettingBindingPromptWithBundleID:shareName:ownerName:shareType:needsLockScreenPresentation:"
+ "com.apple.camera"
+ "getAlertOptionsFromOptions:needsLockScreenPresentation:"
+ "getLaunchingOptionsFromOptions:needsLockScreenPresentation:"
+ "initWithCloudKitURL:invitationToken:needsLockScreenPresentation:unitTestOverrides:"
+ "needsLockScreenPresentation"
+ "setNeedsLockScreenPresentation:"
+ "showAlertWithContent:needsLockScreenPresentation:additionalOptions:responseHandler:"
+ "showFailureAlert:needsLockScreenPresentation:"
+ "showFailureAlert:needsLockScreenPresentation:fileRadarAction:"
+ "showICloudAccountSettingAlert:appName:previewRequested:needsLockScreenPresentation:maid:"
+ "showRequestAccessAlert:needsLockScreenPresentation:requestAccessHandler:cancelHandler:"
+ "showRequestAccessResultAlert:needsLockScreenPresentation:"
- "Failed to initialize LSApplicationRecord for selected app verification with bundle id %@."
- "TB,N,V_isSourceICS"
- "_alertContentForAppStoreOperationWithApp:shareMetadata:keyPrefix:titleKeySuffix:bodyKeySuffix:isSourceICS:"
- "_alertContentForDropDownSelectionWithShareName:ownerName:currentUserName:currentUserFormattedUsername:dropDownTitles:locKeyPrefix:isSourceICS:"
- "_alertContentForVettingBindingPromptWithBundleID:shareName:ownerName:shareType:isShortcut:isSourceICS:"
- "_handleURL:invitationToken:isSourceICS:unitTestOverrides:"
- "_isSourceICS"
- "acceptShareWithURL:invitationToken:isSourceICS:unitTestOverrides:"
- "alertContentForAppDownload:shareMetadata:isSourceICS:"
- "alertContentForAppSelectionWithShareName:ownerName:currentUserName:currentUserFormattedUsername:dropDownTitles:isSourceICS:"
- "alertContentForAppStoreAppSelectionWithShareName:ownerName:currentUserName:currentUserFormattedUsername:dropDownTitles:isSourceICS:"
- "alertContentForAppUpdate:shareMetadata:isSourceICS:"
- "alertContentForFullVettingBindingPromptWithBundleID:shareName:ownerName:shareType:isSourceICS:"
- "alertContentForShortcutVettingBindingPromptWithBundleID:shareName:ownerName:shareType:isSourceICS:"
- "getAlertOptionsFromOptions:isSourceICS:"
- "getLaunchingOptionsFromOptions:isSourceICS:"
- "initWithCloudKitURL:invitationToken:isSourceICS:unitTestOverrides:"
- "isSourceICS"
- "setIsSourceICS:"
- "showAlertWithContent:isSourceICS:additionalOptions:responseHandler:"
- "showFailureAlert:isSourceICS:"
- "showFailureAlert:isSourceICS:fileRadarAction:"
- "showICloudAccountSettingAlert:appName:previewRequested:isSourceICS:maid:"
- "showRequestAccessAlert:isSourceICS:requestAccessHandler:cancelHandler:"
- "showRequestAccessResultAlert:isSourceICS:"
```
