## SpokenNotificationsModule

> `/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule`

```diff

-3525.5.11.11.1
-  __TEXT.__text: 0x1bec
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x27c
+3600.49.31.1.6
+  __TEXT.__text: 0x1aec
+  __TEXT.__objc_methlist: 0x294
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0x33e
+  __TEXT.__cstring: 0x342
   __TEXT.__oslogstring: 0x132
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x9e6
-  __TEXT.__objc_methtype: 0x30d
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d8
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x440
+  __AUTH_CONST.__objc_const: 0x448
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63CBE0E2-D8A5-3954-AEB7-6912B0C35347
+  UUID: 062E4A6F-A2FA-309B-972A-7112BC9DDDFE
   Functions: 33
-  Symbols:   56
-  CStrings:  191
+  Symbols:   57
+  CStrings:  44
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ sub_2a7084e70 -> sub_23c0d1e70 : 184 -> 192
~ sub_2a7085038 -> sub_23c0d2040 : 180 -> 184
~ sub_2a708513c -> sub_23c0d2148 : 560 -> 544
~ sub_2a708536c -> sub_23c0d2368 : 932 -> 924
~ sub_2a70857dc -> sub_23c0d27d0 : 364 -> 308
~ sub_2a7085948 -> sub_23c0d2904 : 408 -> 348
~ sub_2a7085ae0 -> sub_23c0d2a60 : 460 -> 392
~ sub_2a7085d18 -> sub_23c0d2c54 : 528 -> 532
~ sub_2a7085f28 -> sub_23c0d2e68 : 148 -> 144
~ sub_2a7086104 -> sub_23c0d3040 : 404 -> 364
~ sub_2a70863a0 -> sub_23c0d32b4 : 428 -> 420
~ sub_2a70865c8 -> sub_23c0d34d4 : 232 -> 240
~ sub_2a708670c -> sub_23c0d3620 : 116 -> 108
~ sub_2a7086784 -> sub_23c0d3690 : 268 -> 252
~ sub_2a7086890 -> sub_23c0d378c : 200 -> 204
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"BBSettingsGateway\""
- "@\"CCUIContentModuleContext\""
- "@\"CCUIMenuModuleItem\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8I16I20"
- "CCUIContentModule"
- "NSObject"
- "Q16@0:8"
- "SiriUISpokenNotificationsModule"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
- "TB,?,R,N"
- "TQ,?,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_builtInSpeakerAnnounceEnabled"
- "_canShowWhileLocked"
- "_contentModuleContext"
- "_createMenuItems"
- "_fetchAnnounceSettingsAndRefreshState"
- "_headphonesAnnounceEnabled"
- "_hearingAidsAnnounceEnabled"
- "_isEligibleForAnnounceNotificationsWithVendorID:productID:"
- "_menuItemMute"
- "_menuItemOffForTheDay"
- "_menuItemOn"
- "_menuItems"
- "_muteSpokenMessages"
- "_refreshState"
- "_refreshStateWithSelected:expanded:"
- "_selectedOnExpansion"
- "_settingsGateway"
- "_spokenNotificationsModuleQueue"
- "_turnOffSpokenMessagesForTheDay"
- "_turnOnSpokenMessages"
- "_updateMenuItems"
- "_updateMenuItemsWithDate:"
- "addObject:"
- "announceNotificationsOnBuiltInSpeakerEnabled"
- "announceNotificationsOnHearingAidsEnabled"
- "announceNotificationsOnHearingAidsSupported"
- "autorelease"
- "available"
- "backgroundViewController"
- "backgroundViewControllerForContext:"
- "bundleForClass:"
- "buttonTapped:forEvent:"
- "class"
- "component:fromDate:"
- "conformsToProtocol:"
- "connectedDevices"
- "contentRenderingMode"
- "contentViewController"
- "contentViewControllerForContext:"
- "countByEnumeratingWithState:objects:count:"
- "currentCalendar"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "debugDescription"
- "description"
- "descriptionForPackageNamed:inBundle:"
- "didTransitionToExpandedContentMode:"
- "effectiveGlobalAnnounceHeadphonesSetting"
- "enqueueStatusUpdate:"
- "expandsGridSizeClassesForAccessibility"
- "getSpokenNotificationTemporarilyDisabledEndDateWithCompletion:"
- "getSpokenNotificationTemporarilyDisabledStatusWithCompletion:"
- "hash"
- "initWithNibName:bundle:"
- "initWithQueue:"
- "initWithTitle:identifier:handler:"
- "isDate:inSameDayAsDate:"
- "isDeviceInEligibleAnnounceNotificationsConfiguration"
- "isEqual:"
- "isExpanded"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSelected"
- "localizedStringForKey:value:table:"
- "moduleDescription"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "productId"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setContentModuleContext:"
- "setDateStyle:"
- "setGlyphPackageDescription:"
- "setGlyphState:"
- "setIndentation:"
- "setMenuItems:"
- "setSelected:"
- "setSpokenNotificationTemporarilyDisabledUntil:"
- "setSubtitle:"
- "setTimeStyle:"
- "setTitle:"
- "sharedInstance"
- "sharedPreferences"
- "shouldBeginTransitionToExpandedContentModule"
- "startOfDayForDate:"
- "statusUpdateWithMessage:type:"
- "stringFromDate:"
- "stringWithFormat:"
- "superclass"
- "supportedGridSizeClasses"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CCUIContentModuleContext\"16"
- "v24@0:8@16"
- "v24@0:8B16B20"
- "v32@0:8@16@24"
- "vendorId"
- "viewDidLoad"
- "viewWillAppear:"
- "willTransitionToExpandedContentMode:"
- "zone"

```
