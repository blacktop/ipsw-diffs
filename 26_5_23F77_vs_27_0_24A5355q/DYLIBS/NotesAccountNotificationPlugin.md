## NotesAccountNotificationPlugin

> `/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin`

```diff

-2952.120.8.0.0
-  __TEXT.__text: 0x7cdc
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x39c
-  __TEXT.__const: 0x23a
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x344
-  __TEXT.__oslogstring: 0x62f
+2985.0.0.202.2
+  __TEXT.__text: 0x8f70
+  __TEXT.__objc_methlist: 0x3dc
+  __TEXT.__const: 0x24a
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__cstring: 0x484
+  __TEXT.__oslogstring: 0x874
   __TEXT.__swift5_typeref: 0x70
   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x117e
-  __TEXT.__objc_methtype: 0x32f
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x548
+  __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0xd0
-  __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x3e0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xf0
+  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__objc_const: 0x420
+  __AUTH_CONST.__auth_got: 0x3d8
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x4

   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
+  - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF3853C5-1D5C-3D61-8BB9-2FC0CAB7D162
-  Functions: 170
-  Symbols:   174
-  CStrings:  286
+  UUID: A743D8AA-F863-3D2C-AF52-C4C4241DCB05
+  Functions: 188
+  Symbols:   194
+  CStrings:  90
 
Symbols:
+ _ICDynamicCast
+ _NSManagedObjectContextDidSaveObjectIDsNotification
+ _OBJC_CLASS_$_ICAssert
+ _OBJC_CLASS_$_ICAttachment
+ _OBJC_CLASS_$_ICAuthenticationState
+ _OBJC_CLASS_$_ICCloudContext
+ _OBJC_CLASS_$_ICCloudSyncingObject
+ _OBJC_CLASS_$_ICDataPersister
+ _OBJC_CLASS_$_ICNote
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUUID
+ __os_feature_enabled_impl
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x4
+ _swift_release_x19
+ _swift_release_x25
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_retain_x27
CStrings:
+ "%@, account:%@"
+ "%@, account:%@, result %d"
+ "+[ICNote(ICNote_AccountNotification) duplicateNote:intoFolder:]"
+ "+[ICNote(ICNote_AccountNotification) duplicateNote:intoFolder:]_block_invoke"
+ "AppleAccountUI"
+ "Cannot password-protect note {originalNote: %@}"
+ "Deleting modern account %@"
+ "Duplicated note"
+ "Duplicating note… {originalNote: %@, folder: %@}%s:%d"
+ "Error copying values to note %@"
+ "ExtraLargeQuickNoteWidget"
+ "Failed to copy note values — deleting duplicated note {originalNote: %@, duplicatedNote: %@}"
+ "Failed to save after duplicating note {originalNote: %@, duplicatedNote: %@}"
+ "Failed to save note data — deleting duplicated note {originalNote: %@, duplicatedNote: %@}"
+ "Move"
+ "Saved after duplicating note {originalNote: %@, duplicatedNote: %@}"
+ "Saved while duplicating note"
+ "Saving unsynced notes for modern account %@"
+ "SignOutRedesign"
+ "__objc_no"
+ "v16@?0@\"NSNotification\"8"
+ "v24@?0@\"<ICCloudObject>\"8^B16"
- "#16@0:8"
- ".cxx_destruct"
- "?"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@100@0:8q16@24@32{CGSize=dd}40d56Q64B72@76B84B88B92B96"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8^v16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@64@0:8q16@24@32{CGSize=dd}40@56"
- "@72@0:8q16@24@32{CGSize=dd}40d56Q64"
- "ACDAccountNotificationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8i16@20"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "ICThumbnailKey"
- "NSCopying"
- "NSObject"
- "NotesAccountNotificationPlugin"
- "Q16@0:8"
- "T#,R"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",N,R"
- "TQ,R"
- "Tq,N,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_dispatchQueue"
- "acAccount:wasDeletedInStore:"
- "acAccount:wasModifiedInStore:"
- "accessibilityContrast"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountDescription"
- "accountId"
- "accountProperties"
- "accountType"
- "accountWithIdentifier:"
- "accountWithIdentifier:context:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addObserver:selector:name:object:suspensionBehavior:"
- "allAccountsInContext:"
- "applicationDocumentsURL"
- "applicationDocumentsURLForAccountIdentifier:"
- "applicationInstalledOrUninstalled:"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "batchUpdateTopicSubscriptionsAllAccountsInContext:"
- "boolValue"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "childAccountsWithAccountTypeIdentifier:"
- "class"
- "cleanupAdditionalPersistentStores"
- "clearCachedDevicesForAccount:"
- "clearPersistentContainer"
- "conformsToProtocol:"
- "containerUrl"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAdditionalPersistentStoresWithAccountIdentifiers:completionBlock:"
- "crossProcessChangeCoordinator"
- "currentDeviceMigrationStateForAccount:"
- "currentUser"
- "dataclassProperties"
- "date"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "deleteAccount:"
- "deleteAccountForACAccount:"
- "deleteAccountWithBatchDelete:"
- "deleteLegacyAccountForACAccount:"
- "deleteRecentSystemPaperThumbnails"
- "deleteSearchableItemsWithDomainIdentifiers:completionHandler:"
- "deleteSnapshotsForApplicationIdentifier:"
- "deleteSpotlightDomainForAccount:"
- "deleteSpotlightDomainIfNecessaryForAccount:oldAccount:"
- "deleteSpringboardSnapshots"
- "description"
- "descriptionUrl"
- "didChooseToMigrate"
- "didFinishMigration"
- "dirtyAccountProperties"
- "dirtyDataclassProperties"
- "dirtyProperties"
- "disableNotesOnLockScreenIfNecessary"
- "dispatchQueue"
- "displayAccount"
- "displayScale"
- "enabledDataclasses"
- "fetchAndSetMigrationStateForACAccount:inStore:"
- "fetchMigrationStateForAccountID:withCompletionHandler:"
- "hash"
- "ic_hasICloudEmailAddress"
- "ic_isBasicAccountClass"
- "ic_isICloudNotesAccount"
- "ic_isManagedAppleID"
- "ic_isNotesEnabled"
- "ic_isNotesMigrated"
- "ic_isPrimaryAppleAccount"
- "ic_sanitizedFilenameString"
- "ic_shouldCreateSeparatePersistentStore"
- "ic_supportsModernNotes"
- "identifier"
- "imageUrl"
- "init"
- "initWithAccountId:objectId:"
- "initWithAccountId:objectId:thumbnailId:"
- "initWithType:accountId:objectId:preferredSize:scale:appearance:"
- "initWithType:accountId:objectId:preferredSize:scale:appearance:isRTL:contentSizeCategory:hasBoldText:hasButtonShapes:hasDarkerSystemColors:hasBorder:"
- "initWithType:accountId:objectId:preferredSize:traitCollection:"
- "invalidate"
- "isEnabledForDataclass:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "layoutDirection"
- "legibilityWeight"
- "name"
- "newAccountWithIdentifier:type:context:"
- "objectForKeyedSubscript:"
- "objectId"
- "parentAccount"
- "performBlock:"
- "performBlockAndWait:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentStoreCoordinator"
- "persistentStores"
- "persistentStoresByAccountId"
- "postAccountDidChangeNotification"
- "preferredContentSizeCategory"
- "q16@0:8"
- "recentObjectId"
- "release"
- "relevantAccountTypeIdentifiers"
- "reload"
- "reloadTimelinesWithReason:"
- "removeAllTopicSubscriptionsForAccount:"
- "removeItemAtURL:error:"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "save:"
- "saveAccount:withCompletionHandler:"
- "saveDidChooseToMigrate:didFinishMigration:didMigrateOnMac:toACAccount:inStore:completionHandler:"
- "searchableIndex"
- "self"
- "setDidChooseToMigrate:"
- "setDidFinishMigration:"
- "setDidMigrateOnMac:"
- "setDispatchQueue:"
- "setEnabled:forDataclass:"
- "setLegacyNotesDisabled:"
- "setName:"
- "setNeedsToBeFetchedFromCloud:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setState:"
- "setStateModificationDate:"
- "setWithObjects:"
- "sharedContext"
- "sharedController"
- "sharedIndexer"
- "sharedInstance"
- "sharedManager"
- "sharedWidget"
- "shouldProcessChangeType:forACAccount:"
- "startSharedContextWithOptions:"
- "state"
- "superclass"
- "thumbnailId"
- "updateAccountForParentACAccount:inStore:"
- "updateAllLegacyAccountMigrationStatesInContext:"
- "updateChangeCountWithReason:"
- "updateLegacyAccountForParentACAccount:"
- "updateNotesOnLockScreenWhenAccountSupportingLockScreenAdded"
- "userInfo"
- "userInterfaceStyle"
- "userType"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "workerManagedObjectContext"
- "zone"

```
