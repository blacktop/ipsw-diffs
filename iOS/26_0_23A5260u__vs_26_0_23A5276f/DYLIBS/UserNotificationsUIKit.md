## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-971.0.3.0.0
-  __TEXT.__text: 0x1a6668
-  __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_methlist: 0x19ecc
-  __TEXT.__const: 0x3c14
+978.0.3.0.0
+  __TEXT.__text: 0x1a72a4
+  __TEXT.__auth_stubs: 0x27e0
+  __TEXT.__objc_methlist: 0x19e84
+  __TEXT.__const: 0x3bf4
   __TEXT.__gcc_except_tab: 0x2e08
-  __TEXT.__cstring: 0xcf96
-  __TEXT.__oslogstring: 0xd50d
+  __TEXT.__cstring: 0xcfc6
+  __TEXT.__oslogstring: 0xd5cd
   __TEXT.__ustring: 0x22
   __TEXT.__swift5_typeref: 0x3ac8
   __TEXT.__swift5_fieldmd: 0x12c0
-  __TEXT.__constg_swiftt: 0x1e80
+  __TEXT.__constg_swiftt: 0x1e88
   __TEXT.__swift5_reflstr: 0x142e
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x258

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x6e70
+  __TEXT.__unwind_info: 0x6e80
   __TEXT.__eh_frame: 0xb80
-  __TEXT.__objc_classname: 0x36b9
-  __TEXT.__objc_methname: 0x44b8e
-  __TEXT.__objc_methtype: 0xbd90
-  __TEXT.__objc_stubs: 0x277a0
-  __DATA_CONST.__got: 0x1840
-  __DATA_CONST.__const: 0x4120
-  __DATA_CONST.__objc_classlist: 0x7c0
+  __TEXT.__objc_classname: 0x36a3
+  __TEXT.__objc_methname: 0x44aa2
+  __TEXT.__objc_methtype: 0xbdb1
+  __TEXT.__objc_stubs: 0x277e0
+  __DATA_CONST.__got: 0x1838
+  __DATA_CONST.__const: 0x40e8
+  __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x5d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc578
+  __DATA_CONST.__objc_selrefs: 0xc588
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0x13f8
-  __AUTH_CONST.__const: 0x5930
-  __AUTH_CONST.__cfstring: 0x7ca0
-  __AUTH_CONST.__objc_const: 0x254c0
+  __AUTH_CONST.__auth_got: 0x1400
+  __AUTH_CONST.__const: 0x5990
+  __AUTH_CONST.__cfstring: 0x7c00
+  __AUTH_CONST.__objc_const: 0x253e0
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2900
   __AUTH.__data: 0x4f8
-  __DATA.__objc_ivar: 0x1674
-  __DATA.__data: 0x5010
+  __DATA.__objc_ivar: 0x1664
+  __DATA.__data: 0x5020
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1be0
+  __DATA.__bss: 0x1c20
   __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x3598
+  __DATA_DIRTY.__objc_data: 0x3548
   __DATA_DIRTY.__data: 0x1648
-  __DATA_DIRTY.__bss: 0x12d0
+  __DATA_DIRTY.__bss: 0x12c0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2AAE2D09-9DCD-35A3-B165-FE351FF290D4
-  Functions: 10650
-  Symbols:   27993
-  CStrings:  13487
+  UUID: 079D97AD-3ECA-3FBB-B3D8-C70B7341B791
+  Functions: 10658
+  Symbols:   27983
+  CStrings:  13482
 
Symbols:
+ -[NCNotificationGroupList notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:notificationVC:]
+ -[NCNotificationListView updateOverridedUserInterfaceStyleTo:]
+ -[NCNotificationRootList layoutForRootListSizeChange]
+ -[NCNotificationStructuredListViewController _notificationListViewEdgeInsetsForSize:]
+ GCC_except_table129
+ GCC_except_table173
+ GCC_except_table179
+ GCC_except_table198
+ GCC_except_table224
+ GCC_except_table259
+ GCC_except_table265
+ GCC_except_table291
+ GCC_except_table59
+ GCC_except_table61
+ _NCIconImageForUTIWithFormat
+ _NCIconImageForUTIWithFormat.__utiIconCache
+ _NCIconImageForUTIWithFormat.cold.1
+ _NCIconImageForUTIWithFormat.cold.2
+ _NCIconImageForUTIWithFormat.onceToken
+ _OBJC_CLASS_$_UNSAvatarImageRenderer
+ _UNNotificationIconCalendarKey
+ _UNNotificationIconDateComponentsKey
+ _UNNotificationIconDateFormatKey
+ __NCDateIconImageForDateComponentsWithFormat
+ __NCDateIconImageForDateComponentsWithFormat.__componentsIconCache
+ __NCDateIconImageForDateComponentsWithFormat.cold.1
+ __NCDateIconImageForDateComponentsWithFormat.cold.2
+ __NCDateIconImageForDateComponentsWithFormat.onceToken
+ __NCDateIconImageForDateWithFormat
+ __NCDateIconImageForDateWithFormat.__dateIconCache
+ __NCDateIconImageForDateWithFormat.cold.1
+ __NCDateIconImageForDateWithFormat.cold.2
+ __NCDateIconImageForDateWithFormat.onceToken
+ ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.184
+ ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.185
+ ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.186
+ ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke_2.187
+ ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.189
+ ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.190
+ ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.191
+ ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke_2.192
+ ___43-[NCNotificationRootList _digestTestRecipe]_block_invoke.298
+ ___62-[NCNotificationListView updateOverridedUserInterfaceStyleTo:]_block_invoke
+ ___66-[NCNotificationRootList _notificationMigrationOverrideTestRecipe]_block_invoke.305
+ ___84-[NCNotificationRootList _elevateGroupInOtherSectionsIfNeededWithRequest:toSection:]_block_invoke.193
+ ___99-[NCNotificationRootList notificationListMigrationScheduler:requestsMigratingNotificationRequests:]_block_invoke.126
+ ___NCIconImageForUTIWithFormat_block_invoke
+ ____NCDateIconImageForDateComponentsWithFormat_block_invoke
+ ____NCDateIconImageForDateWithFormat_block_invoke
+ ____identifierEncodingAllowedCharacters_block_invoke
+ ___block_descriptor_48_e8_32s_e23_v32?0"UIView"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e82_v24?0"NCNotificationViewController"8"<NCNotificationViewControllerObserving>"16ls32l8
+ ___block_literal_global.1099
+ ___block_literal_global.117
+ ___block_literal_global.119
+ ___block_literal_global.131
+ ___block_literal_global.172
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.20
+ ___block_literal_global.31
+ ___block_literal_global.9
+ __identifierEncodingAllowedCharacters
+ __identifierEncodingAllowedCharacters.characterSet
+ __identifierEncodingAllowedCharacters.cold.1
+ __identifierEncodingAllowedCharacters.onceToken
+ __identifierForIconWithDate
+ __identifierForIconWithDateComponents
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_UserNotificationsUIKit
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_UserNotificationsUIKit
+ _block_copy_helper.11
+ _block_copy_helper.17
+ _block_copy_helper.23
+ _block_copy_helper.29
+ _block_copy_helper.35
+ _block_copy_helper.41
+ _block_copy_helper.56
+ _block_copy_helper.67
+ _block_copy_helper.89
+ _block_descriptor.13
+ _block_descriptor.19
+ _block_descriptor.25
+ _block_descriptor.31
+ _block_descriptor.37
+ _block_descriptor.43
+ _block_descriptor.58
+ _block_descriptor.69
+ _block_descriptor.91
+ _block_destroy_helper.12
+ _block_destroy_helper.18
+ _block_destroy_helper.24
+ _block_destroy_helper.30
+ _block_destroy_helper.36
+ _block_destroy_helper.42
+ _block_destroy_helper.57
+ _block_destroy_helper.68
+ _block_destroy_helper.90
+ _keypath_get_selector_glassTintColor
+ _objc_msgSend$_notificationListViewEdgeInsetsForSize:
+ _objc_msgSend$calendarIdentifier
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$dateComponentDetails
+ _objc_msgSend$day
+ _objc_msgSend$initWithType:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$layoutForRootListSizeChange
+ _objc_msgSend$locale
+ _objc_msgSend$month
+ _objc_msgSend$notificationStructuredListViewControllerRequestsEdgeInsetsForFooterView:forOrientation:
+ _objc_msgSend$notificationStructuredListViewControllerRequestsEdgeInsetsForNotificationListView:forOrientation:
+ _objc_msgSend$notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:notificationVC:
+ _objc_msgSend$setGlassTintColor:
+ _objc_msgSend$stringByAddingPercentEncodingWithAllowedCharacters:
+ _objc_msgSend$updateOverridedUserInterfaceStyleTo:
+ _objc_msgSend$uti
+ _objc_msgSend$weekday
- +[NCAvatarImageRenderer sharedInstanceForPointSize:]
- +[NCAvatarImageRenderer sharedInstanceForPointSize:].cold.1
- -[NCAvatarImageRenderer .cxx_destruct]
- -[NCAvatarImageRenderer _decrementAvatarImageGenerationQueueUsageCountAndInvalidateIfNeeded]
- -[NCAvatarImageRenderer _getAvatarImageGenerationQueueAndIncrementUsageCount]
- -[NCAvatarImageRenderer _imageNamed:inBundleIdentifier:traitCollection:]
- -[NCAvatarImageRenderer _imageNamed:inBundleIdentifier:traitCollection:].cold.1
- -[NCAvatarImageRenderer _initWithPointSize:]
- -[NCAvatarImageRenderer _queue_imageForContacts:compatibleWithTraitCollection:circular:]
- -[NCAvatarImageRenderer _silhouetteFallbackImageNameForContacts:]
- -[NCAvatarImageRenderer _systemImageNamed:traitCollection:]
- -[NCAvatarImageRenderer renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:]
- -[NCNotificationGroupList notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:]
- GCC_except_table124
- GCC_except_table127
- GCC_except_table171
- GCC_except_table178
- GCC_except_table197
- GCC_except_table222
- GCC_except_table255
- GCC_except_table263
- GCC_except_table290
- _BSDispatchQueueCreateSerialWithQoS
- _NCUILogCommunicationNotifications
- _OBJC_CLASS_$_CNAvatarImageRenderer
- _OBJC_CLASS_$_CNAvatarImageRendererSettings
- _OBJC_CLASS_$_CNAvatarImageRenderingScope
- _OBJC_CLASS_$_NCAvatarImageRenderer
- _OBJC_IVAR_$_NCAvatarImageRenderer._avatarImageGenerationQueue
- _OBJC_IVAR_$_NCAvatarImageRenderer._avatarImageGenerationQueueUsageCount
- _OBJC_IVAR_$_NCAvatarImageRenderer._avatarRenderer
- _OBJC_IVAR_$_NCAvatarImageRenderer._pointSize
- _OBJC_METACLASS_$_NCAvatarImageRenderer
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __OBJC_$_CLASS_METHODS_NCAvatarImageRenderer
- __OBJC_$_INSTANCE_METHODS_NCAvatarImageRenderer
- __OBJC_$_INSTANCE_VARIABLES_NCAvatarImageRenderer
- __OBJC_CLASS_RO_$_NCAvatarImageRenderer
- __OBJC_METACLASS_RO_$_NCAvatarImageRenderer
- ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.180
- ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.181
- ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke.182
- ___103-[NCNotificationRootList _migrateNonActiveHighlightNotificationRequestsFromHighlightToIncomingSection:]_block_invoke_2.184
- ___119-[NCAvatarImageRenderer renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:]_block_invoke
- ___119-[NCAvatarImageRenderer renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:]_block_invoke.3
- ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.185
- ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.186
- ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke.187
- ___137-[NCNotificationRootList _migrateOnScheduleNotificationRequests:fromSection:toSection:clearRequests:filterForDestination:animateRemoval:]_block_invoke_2.189
- ___43-[NCNotificationRootList _digestTestRecipe]_block_invoke.295
- ___52+[NCAvatarImageRenderer sharedInstanceForPointSize:]_block_invoke
- ___66-[NCNotificationRootList _notificationMigrationOverrideTestRecipe]_block_invoke.302
- ___84-[NCNotificationRootList _elevateGroupInOtherSectionsIfNeededWithRequest:toSection:]_block_invoke.190
- ___99-[NCNotificationRootList notificationListMigrationScheduler:requestsMigratingNotificationRequests:]_block_invoke.123
- ___NCDateIconImageForDateIconIdentifierWithFormat_block_invoke.cold.3
- ___NCDateIconImageForDateWithFormat_block_invoke.cold.1
- ___block_descriptor_40_e82_v24?0"NCNotificationViewController"8"<NCNotificationViewControllerObserving>"16l
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_91_e8_32s40s48s56s64bs72r80r_e5_v8?0ls64l8r72l8s32l8s40l8s48l8r80l8s56l8
- ___block_literal_global.1095
- ___block_literal_global.114
- ___block_literal_global.116
- ___block_literal_global.122
- ___block_literal_global.130
- ___block_literal_global.15
- ___block_literal_global.169
- ___block_literal_global.177
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_UserNotificationsUIKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_UserNotificationsUIKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_UserNotificationsUIKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_UserNotificationsUIKit
- _block_copy_helper.108
- _block_copy_helper.15
- _block_copy_helper.39
- _block_copy_helper.76
- _block_copy_helper.9
- _block_copy_helper.97
- _block_descriptor.11
- _block_descriptor.110
- _block_descriptor.17
- _block_descriptor.41
- _block_descriptor.78
- _block_descriptor.99
- _block_destroy_helper.10
- _block_destroy_helper.109
- _block_destroy_helper.16
- _block_destroy_helper.40
- _block_destroy_helper.77
- _block_destroy_helper.98
- _objc_msgSend$_decrementAvatarImageGenerationQueueUsageCountAndInvalidateIfNeeded
- _objc_msgSend$_getAvatarImageGenerationQueueAndIncrementUsageCount
- _objc_msgSend$_imageNamed:inBundleIdentifier:traitCollection:
- _objc_msgSend$_initWithPointSize:
- _objc_msgSend$_queue_imageForContacts:compatibleWithTraitCollection:circular:
- _objc_msgSend$_silhouetteFallbackImageNameForContacts:
- _objc_msgSend$_systemImageNamed:traitCollection:
- _objc_msgSend$allContacts
- _objc_msgSend$avatarImageForContacts:scope:
- _objc_msgSend$configurationWithTraitCollection:
- _objc_msgSend$descriptorForRequiredKeys
- _objc_msgSend$generateEphemeralContactsForImageRenderingWithContext:bundleIdentifier:descriptorForRequiredKeys:
- _objc_msgSend$isSystemImage
- _objc_msgSend$notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:
- _objc_msgSend$offMainThreadSynchronousRenderingOnlySettingsWithCacheSize:
- _objc_msgSend$scopeWithPointSize:scale:rightToLeft:style:backgroundStyle:
- _sharedInstanceForPointSize:.__pointSizesToRenderers
- _sharedInstanceForPointSize:.onceToken
CStrings:
+ "%d"
+ "%{public}@ reject glassInterfaceStyle change for non leading group %{public}@; userInterfaceStyle: %ld"
+ "%{public}@ reject glassInterfaceStyle change for non leading request %{public}@; userInterfaceStyle: %ld"
+ "%{public}@ reject glassInterfaceStyle change to %ld for expanded group, glass auto luma tracking is incorrect."
+ "%{public}@ reject glassInterfaceStyle change with nonGroupList; userInterfaceStyle: %ld"
+ "%{public}@ update glassInterfaceStyle change from request %{public}@"
+ "%{public}@ update glassInterfaceStyle to %ld; currentOverrideUserInterfaceStyle: %ld"
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "Failed to obtain ISImage for Calendar date components '%{public}@'"
+ "Failed to obtain ISImage for UTI '%{public}@'"
+ "T@\"UIColor\",N,&,VglassTintColor"
+ "Update glassInterfaceStyle change from section %{public}@; userInterfaceStyle: %ld"
+ "_notificationListViewEdgeInsetsForSize:"
+ "calendarIdentifier"
+ "characterSetWithCharactersInString:"
+ "dateComponentDetails"
+ "day"
+ "glassTintColor"
+ "invertedSet"
+ "layoutForRootListSizeChange"
+ "locale"
+ "month"
+ "notificationStructuredListViewControllerRequestsEdgeInsetsForFooterView:forOrientation:"
+ "notificationStructuredListViewControllerRequestsEdgeInsetsForNotificationListView:forOrientation:"
+ "notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:notificationVC:"
+ "setGlassTintColor:"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "updateOverridedUserInterfaceStyleTo:"
+ "uti"
+ "v32@0:8q16@\"NCNotificationViewController\"24"
+ "v32@0:8q16@24"
+ "weekday"
- "%{public}@ update glassInterfaceStyle to %ld"
- ".%@.avatarGeneration"
- "@\"CNAvatarImageRenderer\""
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "Error loading image named '%{public}@' in bundle '%{public}@'. Error: %@"
- "Failed to obtain ISImage for Calendar date icon identifier '%{public}@'"
- "NCAvatarImageRenderer"
- "NO"
- "NotificationListLayoutValidator"
- "YES"
- "YES with count of '%lu'"
- "[%{public}@]: Context identifier:%{public}@ - Rendered avatar image: %{public}@. Tried System Image: %{public}@, Tried Bundle Image: %{public}@, Tried Ephemeral Contacts: %{public}@, Tried Silhouette Fallback of Name: %{public}@"
- "_avatarImageGenerationQueue"
- "_avatarImageGenerationQueueUsageCount"
- "_avatarRenderer"
- "_decrementAvatarImageGenerationQueueUsageCountAndInvalidateIfNeeded"
- "_getAvatarImageGenerationQueueAndIncrementUsageCount"
- "_imageNamed:inBundleIdentifier:traitCollection:"
- "_initWithPointSize:"
- "_queue_imageForContacts:compatibleWithTraitCollection:circular:"
- "_silhouetteFallbackImageNameForContacts:"
- "_systemImageNamed:traitCollection:"
- "allContacts"
- "avatarImageForContacts:scope:"
- "configurationWithTraitCollection:"
- "descriptorForRequiredKeys"
- "generateEphemeralContactsForImageRenderingWithContext:bundleIdentifier:descriptorForRequiredKeys:"
- "isSystemImage"
- "notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:"
- "offMainThreadSynchronousRenderingOnlySettingsWithCacheSize:"
- "person.2.circle.fill"
- "person.3.fill"
- "person.crop.circle.fill"
- "scopeWithPointSize:scale:rightToLeft:style:backgroundStyle:"

```
