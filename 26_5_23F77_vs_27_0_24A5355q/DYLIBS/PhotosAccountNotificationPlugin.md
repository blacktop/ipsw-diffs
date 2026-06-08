## PhotosAccountNotificationPlugin

> `/System/Library/Accounts/Notification/PhotosAccountNotificationPlugin.bundle/PhotosAccountNotificationPlugin`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x202c
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0x21c
-  __TEXT.__const: 0x38
+910.14.107.0.0
+  __TEXT.__text: 0x1f2c
+  __TEXT.__objc_methlist: 0x22c
+  __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0xc2
-  __TEXT.__oslogstring: 0x6e7
-  __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0x48
-  __TEXT.__objc_methname: 0x63c
-  __TEXT.__objc_methtype: 0x24d
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0x80
+  __TEXT.__cstring: 0xe9
+  __TEXT.__oslogstring: 0x769
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x238
+  __DATA_CONST.__objc_selrefs: 0x248
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x178
-  __AUTH_CONST.__cfstring: 0x120
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x258
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary
   - /System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 902ADF09-B086-32F8-8BE2-BB107F907A8B
-  Functions: 16
-  Symbols:   69
-  CStrings:  167
+  UUID: A8EBDD68-FB45-3459-8C59-B6A59034F949
+  Functions: 17
+  Symbols:   77
+  CStrings:  62
 
Symbols:
+ _ACAccountDataclassSiri
+ _OBJC_CLASS_$_CPLLibraryManager
+ _PLPhotoLibraryVisualIntelligenceContainerIdentifier
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
CStrings:
+ "Disabling Visual Intelligence iCPL for modified account %@"
+ "Enabling Visual Intelligence iCPL for modified account %@"
+ "Image Playground"
+ "Setting feature dataclasses state to, enabled: %{public}@, disabled: %{public}@ on library bundle: %@"
+ "Unable to %@ shared albums for unsupported platform"
+ "Unable to find default %s library: %@"
+ "Unable to set feature dataclasses state due to missing library bundle, enabled: %{public}@, disabled: %{public}@"
+ "Visual Intelligence"
- "#16@0:8"
- "%{public}@ iCPL in library bundle %@"
- "%{public}@ shared album in library bundle at %@"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "NSObject"
- "PhotosAccountNotificationPlugin"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Unable to %@ iCPL due to missing library bundle"
- "Unable to %@ shared album due to missing library bundle"
- "Unable to %@ shared album for unsupported platform"
- "Unable to find default Image Playground library: %@"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_findPhotoLibraryIdentifiersMatchingSearchCriteria:error:"
- "_isCloudPhotoAutoEnableForAccount:"
- "_isSharedStreamsAutoEnableForAccount:"
- "_isUserDefaultsDisabledDataclass:"
- "_setPhotoStreamEnabled:"
- "_setSharedAlbumEnabled:"
- "_setiCPLEnabled:forBundle:"
- "_unboostingQueue"
- "aa_isAccountClass:"
- "aa_isPrimaryEmailVerified"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "description"
- "enableMultiLibraryMode"
- "findPhotoLibraryIdentifiersMatchingSearchCriteria:error:"
- "firstObject"
- "hash"
- "identifier"
- "init"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProvisionedForDataclass:"
- "isProxy"
- "libraryBundleForGP"
- "libraryBundleForSPL"
- "libraryBundleForURL:"
- "libraryManagementClient"
- "libraryURL"
- "objectForKey:"
- "openBundleAtLibraryURL:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertiesForDataclass:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setCloudPhotoLibraryEnabled:"
- "setContainerIdentifier:"
- "setDomain:"
- "setEnabled:forDataclass:"
- "setPhotoStreamEnabled:"
- "setSharedAlbumEnabled:"
- "setUuid:"
- "sharedBundleController"
- "sharedManager"
- "superclass"
- "systemLibraryURL"
- "userDefaultsDisabledDataclasses"
- "v16@0:8"
- "v20@0:8B16"
- "v28@0:8B16@20"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
