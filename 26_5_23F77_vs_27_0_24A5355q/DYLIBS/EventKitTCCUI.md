## EventKitTCCUI

> `/System/Library/PrivateFrameworks/EventKitTCCUI.framework/EventKitTCCUI`

```diff

-376.4.7.0.0
-  __TEXT.__text: 0x1bec
-  __TEXT.__auth_stubs: 0x2e0
+404.0.0.0.0
+  __TEXT.__text: 0x193c
   __TEXT.__objc_methlist: 0x114
   __TEXT.__const: 0x86
   __TEXT.__cstring: 0x98

   __TEXT.__swift5_reflstr: 0x6
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x676
-  __TEXT.__objc_methtype: 0xb5
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x128
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x298
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH.__objc_data: 0x168
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x18

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9FA0BA0F-3BB0-3C0D-BD57-6F49A23CFAB3
+  UUID: 6CC5F979-A4D9-3E0C-93AE-AF76041BB5B5
   Functions: 37
-  Symbols:   276
-  CStrings:  106
+  Symbols:   273
+  CStrings:  11
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_EventKitTCCUI
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_EventKitTCCUI
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _swift_release_x22
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_EventKitTCCUI
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftMapKit_$_EventKitTCCUI
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftVideoToolbox_$_EventKitTCCUI
- _objc_retain
- _objc_retain_x22
- _objc_retain_x25
- _objc_retain_x26
- _swift_release
Functions:
~ -[EventKitTCCUIFactory initWithBundleIdentifier:] : 420 -> 392
~ _logHandle : 84 -> 68
~ -[EventKitTCCUIFactory countEventsInTheNextYear] : 152 -> 140
~ -[EventKitTCCUIFactory settingsViewSubtitle] : 212 -> 200
~ -[EventKitTCCUIFactory previewTableView] : 84 -> 76
~ +[EventKitTCCTableViewCell reuseIdentifier] : 176 -> 160
~ ___43+[EventKitTCCTableViewCell reuseIdentifier]_block_invoke : 68 -> 64
~ -[EventKitTCCTableViewCell initWithStyle:reuseIdentifier:title:subtitle:symbolName:imageColor:] : 3744 -> 3344
~ -[EventKitTCCTableViewCell symbolImageView] : 16 -> 20
~ -[EventKitTCCTableViewCell setSymbolImageView:] : 80 -> 20
~ -[EventKitTCCTableViewCell titleLabel] : 16 -> 20
~ -[EventKitTCCTableViewCell setTitleLabel:] : 80 -> 20
~ -[EventKitTCCTableViewCell subtitleLabel] : 16 -> 20
~ -[EventKitTCCTableViewCell setSubtitleLabel:] : 80 -> 20
~ sub_251a4bf50 -> sub_25a3cac78 : 536 -> 516
~ sub_251a4c284 -> sub_25a3caf98 : 196 -> 192
CStrings:
- ".cxx_destruct"
- "@\"EKEventStore\""
- "@\"NSArray\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"_TtC13EventKitTCCUI19EventPreviewWrapper\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8@16"
- "@64@0:8q16@24@32@40@48@56"
- "CalDateForBeginningOfToday"
- "EventKitTCCTableViewCell"
- "EventKitTCCUIFactory"
- "T@\"UIImageView\",&,N,V_symbolImageView"
- "T@\"UILabel\",&,N,V_subtitleLabel"
- "T@\"UILabel\",&,N,V_titleLabel"
- "_TtC13EventKitTCCUI19EventPreviewWrapper"
- "_allCalendars"
- "_eventStore"
- "_previewWrapper"
- "_subtitleLabel"
- "_symbolImageView"
- "_titleLabel"
- "activateConstraints:"
- "addSubview:"
- "arrayWithObjects:count:"
- "boldSystemFontOfSize:"
- "bottomAnchor"
- "bundleForClass:"
- "calendarsForEntityType:"
- "centerYAnchor"
- "clearColor"
- "configurationWithTextStyle:scale:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToConstant:"
- "contentView"
- "count"
- "countEventsInTheNextYear"
- "countOfEventsFromStartDate:toEndDate:"
- "currentCalendar"
- "dateByAddingYears:inCalendar:"
- "dealloc"
- "event"
- "firstObject"
- "getPreviewControllerForPrompt:"
- "grayColor"
- "heightAnchor"
- "i16@0:8"
- "init"
- "initWithBundleIdentifier:"
- "initWithEKOptions:"
- "initWithEvent:"
- "initWithFrame:"
- "initWithStyle:reuseIdentifier:"
- "initWithStyle:reuseIdentifier:title:subtitle:symbolName:imageColor:"
- "leadingAnchor"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "nextEventsWithCalendars:limit:exclusionOptions:"
- "pointSize"
- "preferredFontForTextStyle:"
- "previewTableView"
- "previewViewController"
- "reuseIdentifier"
- "setAdjustsFontForContentSizeCategory:"
- "setBackgroundColor:"
- "setContentHuggingPriority:forAxis:"
- "setContentMode:"
- "setFont:"
- "setImage:"
- "setNumberOfLines:"
- "setPriority:"
- "setSeparatorInset:"
- "setSourceAccountManagement:withBundleID:"
- "setSubtitleLabel:"
- "setSymbolImageView:"
- "setText:"
- "setTextColor:"
- "setTintColor:"
- "setTitleLabel:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "settingsPreviewViewController"
- "settingsViewSubtitle"
- "subtitleLabel"
- "symbolImageView"
- "systemImageNamed:withConfiguration:"
- "tertiarySystemFillColor"
- "titleLabel"
- "topAnchor"
- "trailingAnchor"
- "v16@0:8"
- "v24@0:8@16"
- "view"
- "widthAnchor"

```
