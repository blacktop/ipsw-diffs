## NotificationsSettings

> `/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings`

```diff

-249.4.3.101.0
-  __TEXT.__text: 0x26e44
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x5340
-  __TEXT.__objc_methlist: 0x1b24
-  __TEXT.__const: 0x254
+249.5.16.0.0
+  __TEXT.__text: 0x294a0
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_stubs: 0x55c0
+  __TEXT.__objc_methlist: 0x2084
+  __TEXT.__const: 0x264
   __TEXT.__gcc_except_tab: 0x1d8
-  __TEXT.__objc_methname: 0x699d
-  __TEXT.__cstring: 0x2ee2
-  __TEXT.__objc_classname: 0x6a5
-  __TEXT.__objc_methtype: 0xd11
+  __TEXT.__objc_methname: 0x6dc6
+  __TEXT.__cstring: 0x2e52
+  __TEXT.__objc_classname: 0x6c7
+  __TEXT.__objc_methtype: 0xd6c
   __TEXT.__oslogstring: 0x252
   __TEXT.__swift5_typeref: 0x1ce
   __TEXT.__swift5_capture: 0xec

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xa00
-  __TEXT.__eh_frame: 0x230
-  __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x518
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0xb40
+  __TEXT.__eh_frame: 0x1f8
+  __DATA_CONST.__auth_got: 0x710
+  __DATA_CONST.__got: 0x520
   __DATA_CONST.__auth_ptr: 0xa8
-  __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__cfstring: 0x2a20
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__cfstring: 0x2c00
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA.__objc_const: 0x5900
-  __DATA.__objc_selrefs: 0x1940
-  __DATA.__objc_ivar: 0x170
-  __DATA.__objc_data: 0x918
+  __DATA.__objc_const: 0x53b8
+  __DATA.__objc_selrefs: 0x1b78
+  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_data: 0x948
   __DATA.__data: 0x8d0
   __DATA.__bss: 0x358
   __DATA.__common: 0x420

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 937
-  Symbols:   436
-  CStrings:  1601
+  Functions: 970
+  Symbols:   441
+  CStrings:  1645
 
Symbols:
+ _NCIsPrioritizationFeatureEnabledForBundleIdentifier
+ _NCOverrideToShowGMSBasedToggles
+ _OBJC_CLASS_$_BSUICAPackageView
+ _OBJC_CLASS_$_NCPriorityNotificationImageCell
+ _OBJC_METACLASS_$_NCPriorityNotificationImageCell
+ _PSValueKey
+ __BSIsInternalInstall
- _swift_arrayDestroy
- _swift_unknownObjectRelease_n
CStrings:
+ "\x06"
+ "-[BulletinBoardController specifiers]"
+ "@\"BSUICAPackageView\""
+ "APPLE_INTELLIGENCE"
+ "APPLE_INTELLIGENCE_FOOTER"
+ "B32@0:8@\"NCPriorityNotificationsDetailController\"16@\"BBSectionInfo\"24"
+ "NCPriorityNotificationImageCell"
+ "NCSettingsShowGMSToggles"
+ "PRIORITIZATION_APP_LIST_DISABLED_APP_DISCLOSURE"
+ "PRIORITIZATION_APP_LIST_GROUP"
+ "PRIORITIZATION_APP_LIST_GROUP_ID"
+ "PRIORITIZATION_EXPLANATION"
+ "PRIORITIZATION_EXPLANATION_VISION"
+ "PRIORITIZATION_ID"
+ "PRIORITY_NOTIFICATION_INFO"
+ "PriorityNotifications~iPad"
+ "PriorityNotifications~iPhone"
+ "SPOKEN_NOTIFICATIONS_APP_OPTIONS_PRIORITY"
+ "T@\"BSUICAPackageView\",&,N,V_packageView"
+ "T@\"UILabel\",&,N,V_captionLabel"
+ "URLForResource:withExtension:"
+ "_captionLabel"
+ "_isPriorityNotificationSupported"
+ "_layoutSubviews"
+ "_packageView"
+ "_prioritizationSpecifierForSectionInfo:"
+ "_sectionInfoHasAnyAnnounceEnabled:"
+ "_setTimeSensitiveAndPriorityEnabled:"
+ "_setupIfNecessary"
+ "_spokenOptionsPriorityNotificationsSpecifier"
+ "_spokenOptionsPrioritySpecifier"
+ "_updateSwitchStates"
+ "_updatesForSpecifiers:withGlobalPrioritizationSetting:animated:"
+ "announcePriorityNotificationsSetting"
+ "bundleIdEligibleForSummarization:"
+ "ca"
+ "captionLabel"
+ "clearColor"
+ "com.apple.notificationsettings"
+ "getMicaFileURL"
+ "imgSizeThatFits:"
+ "initWithURL:"
+ "numberWithInt:"
+ "packageView"
+ "prioritizationSetting"
+ "prioritizationSetting:"
+ "priorityNotificationsDetailController:shouldShowSection:"
+ "setAnnouncePriorityNotificationsSetting:"
+ "setCaptionLabel:"
+ "setPackageView:"
+ "setPrioritizationSetting:"
+ "setPrioritizationSetting:specifier:"
+ "setProritizationSetting:specifier:"
+ "setSectionInfoSettings:"
+ "setSpokenOptionAllNotifications:specifier:"
+ "setSpokenOptionPriority:specifier:"
+ "setSpokenOptionTimeSensitiveDMs:specifier:"
+ "spokenOptionPriority:"
+ "spokenOptionsAllNotifications:"
+ "spokenOptionsTimeSensitiveDMs:"
- "A"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_setSpokenOptionSelectedSpecifier:"
- "categoryOfBundleId:"
- "invalid Collection: less than 'count' elements in collection"
- "setSpokenOption:"

```
