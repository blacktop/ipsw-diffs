## ClockComplications

> `/System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications`

```diff

-2483.340.80.1.0
-  __TEXT.__text: 0xe38
-  __TEXT.__auth_stubs: 0x1b0
+2483.480.0.4.0
+  __TEXT.__text: 0xe28
   __TEXT.__objc_methlist: 0x40c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0xad
+  __TEXT.__cstring: 0xb4
   __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0xd9
-  __TEXT.__objc_methname: 0x96e
-  __TEXT.__objc_methtype: 0x1cf
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x6d8
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x120
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 614D5984-CEFF-3879-8125-BFF399038DEF
+  UUID: A4CF81E0-85B3-3853-BC0B-9A936AF95811
   Functions: 75
-  Symbols:   278
-  CStrings:  151
+  Symbols:   280
+  CStrings:  11
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
- _objc_release_x23
- _objc_retain
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[CLKCComplicationBundleDataSource bundleIdentifier] : 96 -> 88
~ -[CLKCComplicationBundleDataSource complicationDescriptor] : 172 -> 160
~ -[CLKCComplicationBundleDataSource getLaunchURLForTimelineEntryDate:timeTravelDate:withHandler:] : 256 -> 240
~ +[CLKCBundleComplication complicationWithBundleIdentifier:appBundleIdentifier:complicationDescriptor:] : 124 -> 132
~ +[CLKCBundleComplication complicationWithBundleIdentifier:appBundleIdentifier:] : 112 -> 116
~ -[CLKCBundleComplication initWithBundleIdentifier:appBundleIdentifier:complicationDescriptor:] : 212 -> 224
~ -[CLKCBundleComplication description] : 204 -> 188
~ -[CLKCBundleComplication isEqual:] : 268 -> 264
~ -[CLKCBundleComplication hash] : 104 -> 96
~ -[CLKCBundleComplication encodeWithCoder:] : 160 -> 164
~ -[CLKCBundleComplication bundleIdentifier] : 16 -> 20
~ -[CLKCBundleComplication appBundleIdentifier] : 16 -> 20
~ -[CLKCBundleComplication complicationDescriptor] : 16 -> 20
~ -[CLKCComplicationDataSource initWithComplication:family:forDevice:] : 176 -> 184
CStrings:
- ".cxx_destruct"
- "@\"<CLKCComplicationDataSourceDelegate>\""
- "@\"CLKCComplication\""
- "@\"CLKCComplicationDataSourceContext\""
- "@\"CLKComplicationDescriptor\""
- "@\"CLKDevice\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@40@0:8@16q24@32"
- "@48@0:8@16q24@32@40"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8q16@24"
- "CLKCBundleComplication"
- "CLKCComplication"
- "CLKCComplicationBundleDataSource"
- "CLKCComplicationBundleDataSourceContainer"
- "CLKCComplicationDataSource"
- "CLKCComplicationDataSourceContext"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q16@0:8"
- "T@\"<CLKCComplicationDataSourceDelegate>\",W,N,V_delegate"
- "T@\"CLKCComplication\",R,N,V_complication"
- "T@\"CLKCComplicationDataSourceContext\",R,N,V_context"
- "T@\"CLKComplicationDescriptor\",R,C,N,V_complicationDescriptor"
- "T@\"CLKComplicationDescriptor\",R,N"
- "T@\"CLKDevice\",R,N,V_device"
- "T@\"NSArray\",R,C,N"
- "T@\"NSOrderedSet\",R,N"
- "T@\"NSString\",R,C,N,V_appBundleIdentifier"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,N"
- "TB,N,V_showsBackground"
- "TB,R"
- "TB,R,N"
- "TQ,R,N"
- "Tq,R"
- "Tq,R,N,V_family"
- "URLWithString:"
- "_appBundleIdentifier"
- "_bundleIdentifier"
- "_complication"
- "_complicationDescriptor"
- "_context"
- "_delegate"
- "_device"
- "_family"
- "_showsBackground"
- "acceptsComplicationFamily:forDevice:"
- "alwaysOnTemplate"
- "alwaysShowIdealizedTemplateInSwitcher"
- "appBundleIdentifier"
- "appGroupIdentifier"
- "appIdentifier"
- "becomeActive"
- "becomeInactive"
- "bundleForClass:"
- "bundleIdentifier"
- "complication"
- "complicationApplicationIdentifier"
- "complicationBundleDataSources"
- "complicationDescriptor"
- "complicationDescriptors"
- "complicationWithBundleIdentifier:appBundleIdentifier:"
- "complicationWithBundleIdentifier:appBundleIdentifier:complicationDescriptor:"
- "context"
- "copy"
- "copyWithZone:"
- "currentSwitcherTemplate"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "description"
- "device"
- "didTouchDownInView:"
- "didTouchUpInsideView:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "family"
- "fetchWidgetMigrationForDescriptor:completion:"
- "fetchWidgetMigrationForDescriptor:family:completion:"
- "getCurrentTimelineEntryWithHandler:"
- "getDesiredUpdateIntervalWithHandler:"
- "getLaunchURLForTimelineEntryDate:timeTravelDate:withHandler:"
- "getSupportedTimeTravelDirectionsWithHandler:"
- "getTimelineEndDateWithHandler:"
- "getTimelineEntriesAfterDate:limit:withHandler:"
- "getTimelineEntriesBeforeDate:limit:withHandler:"
- "getTimelineStartDateWithHandler:"
- "hasMigratedToWidgetForFamily:device:"
- "hasSensitiveUI"
- "hash"
- "init"
- "initPrivate"
- "initWithBundleIdentifier:appBundleIdentifier:complicationDescriptor:"
- "initWithCoder:"
- "initWithComplication:family:forDevice:"
- "initWithComplication:family:forDevice:context:"
- "isEqual:"
- "legacyComplicationDescriptor"
- "legacyNTKComplicationType"
- "length"
- "localizedAppName"
- "localizedComplicationName"
- "lockedTemplate"
- "pause"
- "pauseAnimations"
- "privacyTemplate"
- "q"
- "q16@0:8"
- "resume"
- "resumeAnimations"
- "sampleTemplate"
- "sectionIdentifier"
- "setDelegate:"
- "setShowsBackground:"
- "showsBackground"
- "stringWithFormat:"
- "supportsSecureCoding"
- "supportsTapAction"
- "timelineAnimationBehavior"
- "tritiumUpdatePriority"
- "useComplicationDescriptorsOnCompanion"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@?32"
- "wantsToSkipPauseWhenEnteringTritium"

```
