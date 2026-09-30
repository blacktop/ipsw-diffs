## CalendarNotification

> `/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification`

```diff

-1529.0.0.0.0
-  __TEXT.__text: 0x57380
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x693c
+1530.0.0.0.0
+  __TEXT.__text: 0x561dc
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x6794
   __TEXT.__const: 0x1d8
-  __TEXT.__oslogstring: 0xdb1c
-  __TEXT.__cstring: 0x3f48
-  __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__unwind_info: 0x1580
-  __TEXT.__objc_classname: 0x1c33
-  __TEXT.__objc_methname: 0x12970
-  __TEXT.__objc_methtype: 0x3088
-  __TEXT.__objc_stubs: 0xbd00
-  __DATA_CONST.__got: 0x948
-  __DATA_CONST.__const: 0xd00
-  __DATA_CONST.__objc_classlist: 0x498
-  __DATA_CONST.__objc_protolist: 0x238
+  __TEXT.__oslogstring: 0xda3a
+  __TEXT.__cstring: 0x3eb5
+  __TEXT.__gcc_except_tab: 0x4fc
+  __TEXT.__unwind_info: 0x1528
+  __TEXT.__objc_classname: 0x1b7c
+  __TEXT.__objc_methname: 0x12595
+  __TEXT.__objc_methtype: 0x2f6f
+  __TEXT.__objc_stubs: 0xbb00
+  __DATA_CONST.__got: 0x928
+  __DATA_CONST.__const: 0xc60
+  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33d8
+  __DATA_CONST.__objc_selrefs: 0x3348
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x2e40
-  __AUTH_CONST.__objc_const: 0xe440
+  __AUTH_CONST.__cfstring: 0x2de0
+  __AUTH_CONST.__objc_const: 0xdf08
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x79c
-  __DATA.__data: 0x1aa0
+  __DATA.__objc_ivar: 0x788
+  __DATA.__data: 0x1920
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x2620
-  __DATA_DIRTY.__bss: 0x3b8
+  __DATA_DIRTY.__objc_data: 0x2530
+  __DATA_DIRTY.__bss: 0x3a8
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69790B8B-DC31-3EE6-BDA7-B1FE9B690231
-  Functions: 2237
-  Symbols:   8621
-  CStrings:  4288
+  UUID: A6224BC2-0308-387C-BD50-77BAB84DAA53
+  Functions: 2214
+  Symbols:   8495
+  CStrings:  4231
 
Symbols:
+ +[CALNNotificationIconUpdater _cleanupLegacyIconCache]
+ +[CALNNotificationIconUpdater _clearIconCacheVersion]
+ +[CALNNotificationIconUpdater _iconCacheDirectory]
+ +[CALNNotificationIconUpdater _needsIconCacheCleanup]
+ +[CALNUNIconProvider _calIconDateFormatTypeFromUNType:]
+ +[CALNUNIconProvider _calIconDateFormatTypeFromUNType:].cold.1
+ +[CALNUNIconProvider _identifierEncodingAllowedCharacters]
+ +[CALNUNIconProvider _identifierEncodingAllowedCharacters].cold.1
+ +[CALNUNIconProvider _parseIconIdentifier:intoDateComponents:calendar:type:]
+ +[CALNUNIconProvider _unDateFormatTypeFromCalIconDateFormatType:]
+ +[CALNUNIconProvider _unDateFormatTypeFromCalIconDateFormatType:].cold.1
+ +[CALNUNIconProvider sharedInstance]
+ -[CALNNotificationIconUpdater initWithProtectedNotificationStorage:iconIdentifierProvider:notificationManager:]
+ -[CALNNotificationIconUpdater updateNotificationIconsIfNeeded]
+ -[CALNUNIconProvider _iconIdentifierForCachedIconPath:]
+ -[CALNUNIconProvider _identifierForIconWithDateComponents:type:inCalendar:]
+ -[CALNUNIconProvider iconIdentifierForIcon:]
+ -[CALNUNIconProvider iconIdentifierForIcon:].cold.1
+ -[CALNUNIconProvider iconIdentifierForIcon:].cold.2
+ -[CALNUNIconProvider iconIdentifierForIcon:].cold.3
+ -[CALNUNIconProvider iconIdentifierForIcon:].cold.4
+ -[CALNUNIconProvider iconWithIdentifier:]
+ -[CALNUNIconProvider identifierForIconWithDate:inCalendar:]
+ -[CALNUNNotificationIconMapper iconProvider]
+ -[CALNUNNotificationIconMapper initWithIconProvider:]
+ -[CALNUNUserNotificationCenter initWithBundleIdentifier:userNotificationCenterFactory:storage:iconProvider:]
+ _OBJC_CLASS_$_CALNUNIconProvider
+ _OBJC_IVAR_$_CALNUNNotificationIconMapper._iconProvider
+ _OBJC_METACLASS_$_CALNUNIconProvider
+ _UNNotificationIconCalendarKey
+ _UNNotificationIconDateComponentsKey
+ _UNNotificationIconDateFormatKey
+ __OBJC_$_CLASS_METHODS_CALNNotificationIconUpdater
+ __OBJC_$_CLASS_METHODS_CALNUNIconProvider
+ __OBJC_$_INSTANCE_METHODS_CALNUNIconProvider
+ __OBJC_$_PROP_LIST_CALNUNIconProvider
+ __OBJC_CLASS_PROTOCOLS_$_CALNUNIconProvider
+ __OBJC_CLASS_RO_$_CALNUNIconProvider
+ __OBJC_METACLASS_RO_$_CALNUNIconProvider
+ ___36+[CALNUNIconProvider sharedInstance]_block_invoke
+ ___58+[CALNUNIconProvider _identifierEncodingAllowedCharacters]_block_invoke
+ _objc_msgSend$_calIconDateFormatTypeFromUNType:
+ _objc_msgSend$_cleanupLegacyIconCache
+ _objc_msgSend$_clearIconCacheVersion
+ _objc_msgSend$_iconIdentifierForCachedIconPath:
+ _objc_msgSend$_identifierForIconWithDateComponents:type:inCalendar:
+ _objc_msgSend$_needsIconCacheCleanup
+ _objc_msgSend$_unDateFormatTypeFromCalIconDateFormatType:
+ _objc_msgSend$dateComponents
+ _objc_msgSend$iconIdentifierForIcon:
+ _objc_msgSend$iconWithDateComponents:calendarIdentifier:format:
+ _objc_msgSend$iconWithIdentifier:
+ _objc_msgSend$initWithBundleIdentifier:userNotificationCenterFactory:storage:iconProvider:
+ _objc_msgSend$initWithProtectedNotificationStorage:iconIdentifierProvider:notificationManager:
+ _objc_msgSend$month
+ _objc_msgSend$updateNotificationIconsIfNeeded
- +[CALNCUIKIconProvider _identifierEncodingAllowedCharacters]
- +[CALNCUIKIconProvider _identifierEncodingAllowedCharacters].cold.1
- +[CALNCUIKIconProvider _parseIconIdentifier:intoDateComponents:calendar:type:]
- +[CALNCUIKIconProvider sharedInstance]
- +[CALNNotificationIconCache _iconCacheDirectory]
- +[CALNNotificationIconCache _pathForCachedIconWithIdentifier:]
- +[CALNNotificationIconCache(UnitTesting) iconCacheDirectory]
- +[CALNNotificationIconCache(UnitTesting) pathForCachedIconWithIdentifier:]
- +[CALNNullIconProvider sharedInstance]
- -[CALNCUIKIconProvider identifierForIconWithDate:inCalendar:]
- -[CALNCUIKIconProvider pngDataForIconWithIdentifier:]
- -[CALNDefaultIconIdentifierVersionProvider iconIdentifierVersion]
- -[CALNDefaultIconIdentifierVersionProvider iconVersionToUpgradeTo]
- -[CALNDefaultIconIdentifierVersionProvider setIconIdentifierVersion:]
- -[CALNNotificationIconCache .cxx_destruct]
- -[CALNNotificationIconCache _addIconWithIdentifier:toCacheAtPath:]
- -[CALNNotificationIconCache _addIconWithIdentifier:toCacheAtPath:].cold.1
- -[CALNNotificationIconCache _createCacheDirectoryIfNeeded]
- -[CALNNotificationIconCache _createCacheDirectoryIfNeeded].cold.1
- -[CALNNotificationIconCache addIconsWithIdentifiers:error:]
- -[CALNNotificationIconCache cachedIconPathForIconIdentifier:]
- -[CALNNotificationIconCache forceRemoveAllCachedIconsWithError:]
- -[CALNNotificationIconCache iconIdentifierForCachedIconPath:]
- -[CALNNotificationIconCache iconProvider]
- -[CALNNotificationIconCache initWithIconProvider:]
- -[CALNNotificationIconCache queue]
- -[CALNNotificationIconCache removeIconWithIdentifier:error:]
- -[CALNNotificationIconUpdater iconCache]
- -[CALNNotificationIconUpdater identifierVersionProvider]
- -[CALNNotificationIconUpdater initWithIconIdentifierVersionProvider:protectedNotificationStorage:iconCache:iconIdentifierProvider:notificationManager:]
- -[CALNNotificationIconUpdater updateIconsToNewVersionIfNeeded]
- -[CALNNotificationServerModule iconCache]
- -[CALNNullIconProvider identifierForIconWithDate:inCalendar:]
- -[CALNNullIconProvider pngDataForIconWithIdentifier:]
- -[CALNUNNotificationIconMapper initWithNotificationIconCache:]
- -[CALNUNNotificationIconMapper notificationIconCache]
- -[CALNUNNotificationIconMapper unNotificationIconFromIconIdentifier:].cold.1
- -[CALNUNUserNotificationCenter initWithBundleIdentifier:userNotificationCenterFactory:storage:notificationIconCache:]
- GCC_except_table10
- GCC_except_table4
- GCC_except_table8
- _NSCocoaErrorDomain
- _OBJC_CLASS_$_CALNCUIKIconProvider
- _OBJC_CLASS_$_CALNDefaultIconIdentifierVersionProvider
- _OBJC_CLASS_$_CALNNotificationIconCache
- _OBJC_CLASS_$_CALNNullIconProvider
- _OBJC_CLASS_$_ISIcon
- _OBJC_CLASS_$_ISImageDescriptor
- _OBJC_CLASS_$_UIImage
- _OBJC_CLASS_$_UIScreen
- _OBJC_IVAR_$_CALNNotificationIconCache._iconProvider
- _OBJC_IVAR_$_CALNNotificationIconCache._queue
- _OBJC_IVAR_$_CALNNotificationIconUpdater._iconCache
- _OBJC_IVAR_$_CALNNotificationIconUpdater._identifierVersionProvider
- _OBJC_IVAR_$_CALNNotificationServerModule._iconCache
- _OBJC_IVAR_$_CALNUNNotificationIconMapper._notificationIconCache
- _OBJC_METACLASS_$_CALNCUIKIconProvider
- _OBJC_METACLASS_$_CALNDefaultIconIdentifierVersionProvider
- _OBJC_METACLASS_$_CALNNotificationIconCache
- _OBJC_METACLASS_$_CALNNullIconProvider
- _UIImagePNGRepresentation
- __OBJC_$_CLASS_METHODS_CALNCUIKIconProvider
- __OBJC_$_CLASS_METHODS_CALNNotificationIconCache(UnitTesting)
- __OBJC_$_CLASS_METHODS_CALNNullIconProvider
- __OBJC_$_CLASS_PROP_LIST_CALNCUIKIconProvider
- __OBJC_$_CLASS_PROP_LIST_CALNNullIconProvider
- __OBJC_$_CLASS_PROP_LIST_CalIconProvider
- __OBJC_$_INSTANCE_METHODS_CALNCUIKIconProvider
- __OBJC_$_INSTANCE_METHODS_CALNDefaultIconIdentifierVersionProvider
- __OBJC_$_INSTANCE_METHODS_CALNNotificationIconCache
- __OBJC_$_INSTANCE_METHODS_CALNNullIconProvider
- __OBJC_$_INSTANCE_VARIABLES_CALNNotificationIconCache
- __OBJC_$_PROP_LIST_CALNCUIKIconProvider
- __OBJC_$_PROP_LIST_CALNDefaultIconIdentifierVersionProvider
- __OBJC_$_PROP_LIST_CALNIconIdentifierVersionProvider
- __OBJC_$_PROP_LIST_CALNNotificationIconCache
- __OBJC_$_PROP_LIST_CALNNullIconProvider
- __OBJC_$_PROTOCOL_CLASS_METHODS_CalIconProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CALNIconCache
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CALNIconIdentifierVersionProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CALNNotificationIconProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CalIconProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CALNIconCache
- __OBJC_$_PROTOCOL_METHOD_TYPES_CALNIconIdentifierVersionProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CALNNotificationIconProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_CalIconProvider
- __OBJC_$_PROTOCOL_REFS_CALNIconCache
- __OBJC_$_PROTOCOL_REFS_CALNIconIdentifierVersionProvider
- __OBJC_$_PROTOCOL_REFS_CALNNotificationIconProvider
- __OBJC_$_PROTOCOL_REFS_CalIconProvider
- __OBJC_CLASS_PROTOCOLS_$_CALNCUIKIconProvider
- __OBJC_CLASS_PROTOCOLS_$_CALNDefaultIconIdentifierVersionProvider
- __OBJC_CLASS_PROTOCOLS_$_CALNNotificationIconCache
- __OBJC_CLASS_PROTOCOLS_$_CALNNullIconProvider
- __OBJC_CLASS_RO_$_CALNCUIKIconProvider
- __OBJC_CLASS_RO_$_CALNDefaultIconIdentifierVersionProvider
- __OBJC_CLASS_RO_$_CALNNotificationIconCache
- __OBJC_CLASS_RO_$_CALNNullIconProvider
- __OBJC_LABEL_PROTOCOL_$_CALNIconCache
- __OBJC_LABEL_PROTOCOL_$_CALNIconIdentifierVersionProvider
- __OBJC_LABEL_PROTOCOL_$_CALNNotificationIconProvider
- __OBJC_LABEL_PROTOCOL_$_CalIconProvider
- __OBJC_METACLASS_RO_$_CALNCUIKIconProvider
- __OBJC_METACLASS_RO_$_CALNDefaultIconIdentifierVersionProvider
- __OBJC_METACLASS_RO_$_CALNNotificationIconCache
- __OBJC_METACLASS_RO_$_CALNNullIconProvider
- __OBJC_PROTOCOL_$_CALNIconCache
- __OBJC_PROTOCOL_$_CALNIconIdentifierVersionProvider
- __OBJC_PROTOCOL_$_CALNNotificationIconProvider
- __OBJC_PROTOCOL_$_CalIconProvider
- ___38+[CALNCUIKIconProvider sharedInstance]_block_invoke
- ___38+[CALNNullIconProvider sharedInstance]_block_invoke
- ___59-[CALNNotificationIconCache addIconsWithIdentifiers:error:]_block_invoke
- ___60+[CALNCUIKIconProvider _identifierEncodingAllowedCharacters]_block_invoke
- ___60-[CALNNotificationIconCache removeIconWithIdentifier:error:]_block_invoke
- ___60-[CALNNotificationIconCache removeIconWithIdentifier:error:]_block_invoke.cold.1
- ___60-[CALNNotificationIconCache removeIconWithIdentifier:error:]_block_invoke.cold.2
- ___61-[CALNNotificationIconCache cachedIconPathForIconIdentifier:]_block_invoke
- ___62-[CALNNotificationIconUpdater updateIconsToNewVersionIfNeeded]_block_invoke
- ___64-[CALNNotificationIconCache forceRemoveAllCachedIconsWithError:]_block_invoke
- ___block_descriptor_40_e8_32s_e39_v32?0"CALNNotificationRecord"8Q16^B24ls32l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- _objc_msgSend$CGImage
- _objc_msgSend$_addIconWithIdentifier:toCacheAtPath:
- _objc_msgSend$_createCacheDirectoryIfNeeded
- _objc_msgSend$_pathForCachedIconWithIdentifier:
- _objc_msgSend$addIconsWithIdentifiers:error:
- _objc_msgSend$cachedIconPathForIconIdentifier:
- _objc_msgSend$forceRemoveAllCachedIconsWithError:
- _objc_msgSend$iconAtPath:
- _objc_msgSend$iconCache
- _objc_msgSend$iconIdentifierForCachedIconPath:
- _objc_msgSend$iconIdentifierVersion
- _objc_msgSend$iconVersionToUpgradeTo
- _objc_msgSend$identifierVersionProvider
- _objc_msgSend$imageWithCGImage:scale:orientation:
- _objc_msgSend$initWithBundleIdentifier:userNotificationCenterFactory:storage:notificationIconCache:
- _objc_msgSend$initWithDateComponents:calendar:format:forceNoTextEffects:
- _objc_msgSend$initWithIconIdentifierVersionProvider:protectedNotificationStorage:iconCache:iconIdentifierProvider:notificationManager:
- _objc_msgSend$initWithNotificationIconCache:
- _objc_msgSend$initWithSize:scale:
- _objc_msgSend$mainScreen
- _objc_msgSend$notificationIconCache
- _objc_msgSend$pathExtension
- _objc_msgSend$pngDataForIconWithIdentifier:
- _objc_msgSend$prepareImageForDescriptor:
- _objc_msgSend$protectedStorage
- _objc_msgSend$queue
- _objc_msgSend$scale
- _objc_msgSend$setIconIdentifierVersion:
- _objc_msgSend$setShouldApplyMask:
- _objc_msgSend$stringByAppendingPathExtension:
- _objc_msgSend$stringByDeletingLastPathComponent
CStrings:
+ "@\"CALNUNIconProvider\""
+ "@40@0:8@16q24@32"
+ "CALNUNIconProvider"
+ "Could not get icon identifier from icon: calendar identifier is nil or not a string"
+ "Could not get icon identifier from icon: date components is nil or not a dictionary"
+ "Could not get icon identifier from icon: missing date components dictionary"
+ "Could not get icon identifier from icon: type is nil or not a number"
+ "Could not get icon identifier from notification icon = %{public}@"
+ "IconUpdater: Deleted legacy icon cache directory."
+ "IconUpdater: Failed to delete legacy icon cache directory: %@"
+ "IconUpdater: Legacy icon cache directory does not exist. Nothing else to do."
+ "IconUpdater: Need to clean up legacy notification icons"
+ "T@\"CALNUNIconProvider\",R,N,V_iconProvider"
+ "Unexpected icon format type: %d"
+ "_calIconDateFormatTypeFromUNType:"
+ "_cleanupLegacyIconCache"
+ "_clearIconCacheVersion"
+ "_iconIdentifierForCachedIconPath:"
+ "_identifierForIconWithDateComponents:type:inCalendar:"
+ "_needsIconCacheCleanup"
+ "_unDateFormatTypeFromCalIconDateFormatType:"
+ "dateComponents"
+ "iconIdentifierForIcon:"
+ "iconWithDateComponents:calendarIdentifier:format:"
+ "iconWithIdentifier:"
+ "initWithBundleIdentifier:userNotificationCenterFactory:storage:iconProvider:"
+ "initWithProtectedNotificationStorage:iconIdentifierProvider:notificationManager:"
+ "month"
+ "q24@0:8q16"
+ "updateNotificationIconsIfNeeded"
- "@\"<CALNIconCache>\""
- "@\"<CALNIconIdentifierVersionProvider>\""
- "@\"<CALNNotificationIconProvider><CALNCalendarIconIdentifierProvider><CalIconProvider>\""
- "@\"<CalIconProvider>\""
- "@\"<CalIconProvider>\"16@0:8"
- "@\"CALNNotificationIconCache\""
- "@\"NSData\"24@0:8@\"NSString\"16"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "B32@0:8@\"NSArray\"16^@24"
- "B32@0:8@\"NSString\"16^@24"
- "CALNCUIKIconProvider"
- "CALNDefaultIconIdentifierVersionProvider"
- "CALNIconCache"
- "CALNIconIdentifierVersionProvider"
- "CALNNotificationIconCache"
- "CALNNotificationIconCacheQueue"
- "CALNNotificationIconProvider"
- "CALNNullIconProvider"
- "CGImage"
- "CalIconProvider"
- "Could not get icon identifier from icon path = %{public}@, notification icon = %{public}@"
- "Could not get icon path for icon identifier = %{public}@"
- "Error trying to create notifications icon cache directory: %{public}@"
- "Failed to add icon to cache."
- "Failed to add icon to cache. IconIdentifier: %{public}@"
- "Failed to generate icon with identifier %{public}@"
- "Failed to remove icon file. Icon Identifier: %{public}@ . Error %{public}@"
- "Failed to save icon with identifier %{public}@ to path %{public}@. error = %{public}@"
- "Icon does not exist and cannot be removed."
- "Icon does not exist and cannot be removed. Icon Identifier: %{public}@"
- "IconUpdater: IconIdentifierVersion out of date, updating all icon identifiers in storage first."
- "IconUpdater: Regenerating icon files that are still in use in protectedStorage"
- "IconUpdater: Wiping icon cache directory to get rid of out dated icon files"
- "IconUpdater: icon update complete, setting icon version to current version"
- "T@\"<CALNIconCache>\",R,N,V_iconCache"
- "T@\"<CALNIconIdentifierVersionProvider>\",R,N,V_identifierVersionProvider"
- "T@\"<CALNNotificationIconProvider><CALNCalendarIconIdentifierProvider><CalIconProvider>\",R,N,V_iconProvider"
- "T@\"<CalIconProvider>\",R,N"
- "T@\"<CalIconProvider>\",R,N,V_iconProvider"
- "T@\"CALNCUIKIconProvider\",R,N"
- "T@\"CALNNotificationIconCache\",R,N,V_iconCache"
- "T@\"CALNNotificationIconCache\",R,N,V_notificationIconCache"
- "T@\"CALNNullIconProvider\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "Tq,N"
- "Tq,R,N"
- "_addIconWithIdentifier:toCacheAtPath:"
- "_createCacheDirectoryIfNeeded"
- "_iconCache"
- "_identifierVersionProvider"
- "_notificationIconCache"
- "_pathForCachedIconWithIdentifier:"
- "_queue"
- "addIconsWithIdentifiers:error:"
- "cachedIconPathForIconIdentifier:"
- "forceRemoveAllCachedIconsWithError:"
- "iconAtPath:"
- "iconCache"
- "iconCacheDirectory"
- "iconIdentifierForCachedIconPath:"
- "iconIdentifierVersion"
- "iconVersionToUpgradeTo"
- "identifierVersionProvider"
- "imageWithCGImage:scale:orientation:"
- "initWithBundleIdentifier:userNotificationCenterFactory:storage:notificationIconCache:"
- "initWithDateComponents:calendar:format:forceNoTextEffects:"
- "initWithIconIdentifierVersionProvider:protectedNotificationStorage:iconCache:iconIdentifierProvider:notificationManager:"
- "initWithNotificationIconCache:"
- "initWithSize:scale:"
- "mainScreen"
- "notificationIconCache"
- "pathExtension"
- "pathForCachedIconWithIdentifier:"
- "png"
- "pngDataForIconWithIdentifier:"
- "prepareImageForDescriptor:"
- "queue"
- "removeIconWithIdentifier:error:"
- "scale"
- "setIconIdentifierVersion:"
- "setShouldApplyMask:"
- "stringByAppendingPathExtension:"
- "stringByDeletingLastPathComponent"
- "v32@?0@\"CALNNotificationRecord\"8Q16^B24"

```
