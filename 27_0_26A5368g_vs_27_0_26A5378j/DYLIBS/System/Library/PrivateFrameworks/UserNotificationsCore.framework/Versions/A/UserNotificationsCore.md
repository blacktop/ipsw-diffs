## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Versions/A/UserNotificationsCore`

```diff

-  __TEXT.__text: 0x1e0be0
-  __TEXT.__objc_methlist: 0x5c5c
-  __TEXT.__cstring: 0x8733
-  __TEXT.__const: 0x11248
+  __TEXT.__text: 0x1e09ac
+  __TEXT.__objc_methlist: 0x5c6c
+  __TEXT.__const: 0x1108c
+  __TEXT.__cstring: 0x8751
+  __TEXT.__oslogstring: 0xe84a
   __TEXT.__gcc_except_tab: 0x450
-  __TEXT.__oslogstring: 0xeb98
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__constg_swiftt: 0x65c8
-  __TEXT.__swift5_typeref: 0x6708
-  __TEXT.__swift5_reflstr: 0x3d57
-  __TEXT.__swift5_fieldmd: 0x477c
+  __TEXT.__constg_swiftt: 0x6590
+  __TEXT.__swift5_typeref: 0x66b1
+  __TEXT.__swift5_reflstr: 0x3d1a
+  __TEXT.__swift5_fieldmd: 0x4714
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_assocty: 0x6c0
-  __TEXT.__swift5_protos: 0x140
-  __TEXT.__swift5_proto: 0xc20
-  __TEXT.__swift5_types: 0x538
+  __TEXT.__swift5_assocty: 0x6a8
+  __TEXT.__swift5_proto: 0xc08
+  __TEXT.__swift5_types: 0x530
+  __TEXT.__swift5_capture: 0x1d58
   __TEXT.__swift_as_entry: 0x194
-  __TEXT.__swift_as_cont: 0x260
-  __TEXT.__swift5_capture: 0x1d6c
-  __TEXT.__swift_as_ret: 0x178
+  __TEXT.__swift_as_ret: 0x17c
+  __TEXT.__swift_as_cont: 0x264
+  __TEXT.__swift5_protos: 0x140
   __TEXT.__swift5_mpenum: 0x64
-  __TEXT.__unwind_info: 0x5700
-  __TEXT.__eh_frame: 0x5930
+  __TEXT.__unwind_info: 0x5748
+  __TEXT.__eh_frame: 0x5b4c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a48
+  __DATA_CONST.__objc_selrefs: 0x3aa0
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__got: 0x12a8
-  __AUTH_CONST.__const: 0xd2e0
+  __DATA_CONST.__got: 0x12a0
+  __AUTH_CONST.__const: 0xd100
   __AUTH_CONST.__cfstring: 0x4840
-  __AUTH_CONST.__objc_const: 0x20b40
+  __AUTH_CONST.__objc_const: 0x21228
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1de8
-  __AUTH.__objc_data: 0xb10
-  __AUTH.__data: 0x1bd8
-  __DATA.__objc_ivar: 0x6f4
-  __DATA.__data: 0x3540
-  __DATA.__bss: 0xcb00
+  __AUTH_CONST.__auth_got: 0x1dd8
+  __AUTH.__objc_data: 0xa28
+  __AUTH.__data: 0x1970
+  __DATA.__objc_ivar: 0x6f8
+  __DATA.__data: 0x3258
+  __DATA.__bss: 0xc560
   __DATA.__common: 0x118
-  __DATA_DIRTY.__objc_data: 0x26d8
-  __DATA_DIRTY.__data: 0x78f0
-  __DATA_DIRTY.__bss: 0x8110
+  __DATA_DIRTY.__objc_data: 0x27c0
+  __DATA_DIRTY.__data: 0x7de8
+  __DATA_DIRTY.__bss: 0x83b0
   __DATA_DIRTY.__common: 0x410
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
+  - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8597
-  Symbols:   9346
-  CStrings:  2580
+  Functions: 8592
+  Symbols:   9357
+  CStrings:  2563
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ -[UNCNotificationRecordMapper _categoriesByIdentifier]
+ OBJC_IVAR_$_UNCNotificationRecordMapper._cachedCategoriesByIdentifier
+ _CNContactEmailAddressesKey
+ _CNContactPhoneNumbersKey
+ __OBJC_$_CATEGORY_NSArray_$_UserNotificationsCore
+ __OBJC_$_CLASS_METHODS_UNCNotificationSourceDescription(Testing|Factory)
+ __OBJC_$_INSTANCE_METHODS_NSArray(UserNotificationsCore|UNSNotificationRecord)
+ __OBJC_$_INSTANCE_METHODS_UNCNotificationSourceDescription(Testing|Factory)
+ ___swift_memcpy160_8
+ ___swift_project_boxed_opaque_existential_2Tm
+ ___unnamed_23
+ __swift_closure_destructor.19Tm
+ _objc_msgSend$_categoriesByIdentifier
+ _objc_msgSend$authors
+ _objc_msgSend$contactIdentifier
+ _objc_msgSend$contentCreationDate
+ _objc_msgSend$contentSnippet
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$handleIdentifier
+ _objc_msgSend$handles
+ _objc_msgSend$isCommunicationNotification
+ _objc_msgSend$isGroupThread
+ _objc_msgSend$isTwoFactorCode
+ _objc_msgSend$notificationCritical
+ _objc_msgSend$notificationTimeSensitive
+ _objc_msgSend$primaryRecipients
+ _objc_msgSend$textContent
+ _symbolic _____SgXw 21UserNotificationsCore22AlertCoordinatorClientC
- __OBJC_$_CATEGORY_NSArray_$_UNSNotificationRecord
- __OBJC_$_CLASS_METHODS_UNCNotificationSourceDescription(Factory|Testing)
- __OBJC_$_INSTANCE_METHODS_NSArray(UNSNotificationRecord|UserNotificationsCore)
- __OBJC_$_INSTANCE_METHODS_UNCNotificationSourceDescription(Factory|Testing)
- ___swift_memcpy176_8
- ___unnamed_24
- __swift_closure_destructor.5Tm
- _associated conformance 21UserNotificationsCore0A36NotificationEntityShowPreviewSettingOSHAASQ
- _associated conformance 21UserNotificationsCore16EntityQueryErrorOSHAASQ
- _objc_msgSend$initWithBundle:
- _objc_msgSend$instanceIdentifier
- _objc_msgSend$notificationCategoryForNotificationCategoryRecord:
- _objc_msgSend$notificationSourceWithIdentifier:
- _objc_msgSend$typeIdentifier
- _swift_runtimeSupportsNoncopyableTypes
- _symbolic So28UNNotificationSourceSettingsCSg
- _symbolic _____ 21UserNotificationsCore0A36NotificationEntityShowPreviewSettingO
- _symbolic _____ 21UserNotificationsCore16EntityQueryErrorO
- _symbolic _____ySSSo10BSCFBundleCG s18_DictionaryStorageC
- get_type_metadata 15Synchronization5MutexVySbG noncopyable
CStrings:
+ "CSPerson handles array is empty. %@"
+ "EntityQuery from Spotlight returned %ld results, mapped into %ld entities."
+ "EntityQuery using Spotlight for %{public}ld identifiers"
+ "Failed to query spotlight: %@"
+ "UniqueIdentifier workaround is only valid for notification queries."
+ "_kMDItemAppEntityInstanceIdentifier"
- "Checking settings for identifier: %{private}s"
- "Creating UN object for identifier: %{private}s"
- "Creating entity for identifier: %{private}s"
- "Done with identifier: %{private}s"
- "EntityQuery from repository returned %ld entities from %ld requested."
- "EntityQuery using notification repository for %{public}ld identifiers"
- "Failed to create bundle for %{private}s: %{public}@"
- "Failed to map record to UNNotification for identifier: %{private}s"
- "Failed to parse identifier: %{private}s"
- "Failed to query repository: %@"
- "Mapping notification record for identifier: %{private}s"
- "No notification record found for identifier: %{private}s"
- "No settings for searchable item with bundle %{private}s"
- "Notification repository is not configured properly."
- "Populating group properties for identifier: %{private}s"
- "Querying category for identifier: %{private}s"
- "Querying ls for bundleIdentifier: %{private}s"
- "Querying repository for identifier: %{private}s"
- "Repository accessor not properly configured"
- "Unable to create bundle for identifier: %{private}s"
- "always"
- "never"
- "whenAuthenticated"

```
