## iCloud

> `/System/Library/CoreServices/iCloud.app/Contents/MacOS/iCloud`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2710.114.0.0.0
-  __TEXT.__text: 0x18da4
+2710.116.0.0.0
+  __TEXT.__text: 0x18e58
   __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_stubs: 0x37e0
   __TEXT.__objc_methlist: 0xf48
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x584
-  __TEXT.__objc_methname: 0x4344
-  __TEXT.__oslogstring: 0x1a55
+  __TEXT.__objc_methname: 0x44c4
+  __TEXT.__oslogstring: 0x1a84
   __TEXT.__cstring: 0x2c54
   __TEXT.__objc_classname: 0xee
   __TEXT.__objc_methtype: 0x93a

   - /usr/lib/libobjc.A.dylib
   Functions: 347
   Symbols:   206
-  CStrings:  1191
+  CStrings:  1192
 
Functions:
~ sub_100009db8 : 280 -> 284
~ sub_10000f988 -> sub_10000f98c : 1888 -> 2036
~ sub_10001583c -> sub_1000158d4 : 780 -> 808
~ sub_10001747c -> sub_100017530 : 8 -> 12
~ sub_10001748c -> sub_100017544 : 12 -> 8
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
