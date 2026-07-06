## GeneralSettings

> `/System/Library/ExtensionKit/Extensions/GeneralSettings.appex/Contents/MacOS/GeneralSettings`

```diff

-  __TEXT.__text: 0x11684
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0xbc0
-  __TEXT.__objc_classname: 0x220
-  __TEXT.__objc_methname: 0x88f
-  __TEXT.__objc_methtype: 0x4b2
-  __TEXT.__constg_swiftt: 0x5c0
-  __TEXT.__swift5_typeref: 0x110d
-  __TEXT.__swift5_reflstr: 0x376
-  __TEXT.__swift5_fieldmd: 0x334
-  __TEXT.__cstring: 0x922
+  __TEXT.__text: 0x10468
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_stubs: 0x160
+  __TEXT.__objc_methlist: 0x200
+  __TEXT.__const: 0xfb2
+  __TEXT.__constg_swiftt: 0x368
+  __TEXT.__swift5_typeref: 0xfe0
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_reflstr: 0x4de
+  __TEXT.__swift5_fieldmd: 0x364
+  __TEXT.__swift5_assocty: 0x128
+  __TEXT.__swift5_proto: 0x6c
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__objc_classname: 0x1fb
+  __TEXT.__objc_methname: 0x6a7
+  __TEXT.__objc_methtype: 0x482
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0xc5
-  __TEXT.__swift5_capture: 0x88
-  __TEXT.__unwind_info: 0x3a0
-  __TEXT.__eh_frame: 0x180
-  __DATA_CONST.__const: 0x820
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__swift5_capture: 0x130
+  __TEXT.__cstring: 0xd04
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_cont: 0x70
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__oslogstring: 0x36
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x490
+  __TEXT.__eh_frame: 0x6fc
+  __DATA_CONST.__const: 0xa00
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0x6a8
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__auth_ptr: 0x380
-  __DATA.__objc_const: 0x968
-  __DATA.__objc_selrefs: 0x1a0
-  __DATA.__objc_data: 0x218
-  __DATA.__data: 0xb58
+  __DATA_CONST.__auth_got: 0x6e8
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__auth_ptr: 0x508
+  __DATA.__objc_const: 0x728
+  __DATA.__objc_selrefs: 0x148
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x738
+  __DATA.__bss: 0xd60
   __DATA.__common: 0x28
-  __DATA.__bss: 0x9f0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
-  - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
+  - /System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/Versions/A/AsyncAlgorithmsInternal
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/Settings.framework/Versions/A/Settings
+  - /System/Library/PrivateFrameworks/SettingsHost.framework/Versions/A/SettingsHost
+  - /System/Library/PrivateFrameworks/SettingsHostUI.framework/Versions/A/SettingsHostUI
   - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/Versions/A/_IconServices_SwiftUI
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 315
-  Symbols:   115
-  CStrings:  177
+  Functions: 339
+  Symbols:   124
+  CStrings:  173
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __availability_version_check
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _free
+ _fseek
+ _ftell
+ _malloc
+ _rewind
+ _sscanf
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_getObjCClassFromMetadata
+ _swift_initStaticObject
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrowTypedImpl
- _MobileGestalt_get_appleInternalInstallCapability
- _MobileGestalt_get_current_device
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_NSScreen
- _OBJC_CLASS_$_NSTimer
- _OBJC_METACLASS_$_NSObject
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- __swift_stdlib_reportUnimplementedInitializer
- _bzero
- _memcpy
- _objc_msgSendSuper2
- _swift_bridgeObjectRelease_n
- _swift_cvw_initStructMetadataWithLayoutString
- _swift_cvw_initWithTake
- _swift_getAtKeyPath
- _swift_getEnumCaseMultiPayload
- _swift_getEnumTagSinglePayloadGeneric
- _swift_isUniquelyReferenced_nonNull_bridgeObject
- _swift_storeEnumTagMultiPayload
- _swift_storeEnumTagSinglePayloadGeneric
CStrings:
+ "$__lazy_storage_$_selectionState"
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "AirDrop & Continuity"
+ "AppleCare & Warranty"
+ "AutoFill & Passwords"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "Description of the General settings pane shown in the placard."
+ "Device Management"
+ "Language & Region"
+ "Login Items & Extensions"
+ "Managed/badge state changed; rebuilding General list."
+ "Primary Text, Button"
+ "ProductVersion"
+ "Secondary Text, shown on a row that has been disabled via a configuration profile."
+ "These settings are controlled by a profile."
+ "Title of the General settings pane, shown in the placard and titlebar."
+ "Transfer or Reset"
+ "View.task @ GeneralSettings/GeneralSettingsList.swift:"
+ "_$observationRegistrar"
+ "_TtC15GeneralSettings24GeneralSettingsListState"
+ "_TtC15GeneralSettings29GeneralSettingsExtensionModel"
+ "_TtC15GeneralSettings35GeneralSettingsManagedStateProvider"
+ "_currentSnapshot"
+ "com.apple.ExtensionsPreferences"
+ "com.apple.Localization"
+ "com.apple.preference.datetime"
+ "com.apple.preference.startupdisk"
+ "com.apple.preferences.configurationprofiles"
+ "com.apple.preferences.sharing"
+ "com.apple.preferences.softwareupdate"
+ "com.apple.prefs.backup"
+ "com.apple.systempreferences.general.about"
+ "com.apple.systempreferences.general.airDropAndHandoff"
+ "com.apple.systempreferences.general.appleCareAndWarranty"
+ "com.apple.systempreferences.general.dateAndTime"
+ "com.apple.systempreferences.general.deviceManagement"
+ "com.apple.systempreferences.general.featureDescription"
+ "com.apple.systempreferences.general.languageAndRegion"
+ "com.apple.systempreferences.general.loginItems"
+ "com.apple.systempreferences.general.passwords"
+ "com.apple.systempreferences.general.sharing"
+ "com.apple.systempreferences.general.softwareUpdate"
+ "com.apple.systempreferences.general.startupDisk"
+ "com.apple.systempreferences.general.storage"
+ "com.apple.systempreferences.general.timeMachine"
+ "com.apple.systempreferences.general.transferOrReset"
+ "currentListContext"
+ "hasPerformedDeferredSetup"
+ "kCFAllocatorNull"
+ "mainBundle"
+ "managedStateProvider"
+ "navigator"
+ "observationTasks"
+ "r"
+ "sectionProviders"
+ "snapshots"
+ "snapshotsContinuation"
- " handleOpenParameterTarget: "
- "$__lazy_storage_$_legacyBundleIdentifier"
- "$__lazy_storage_$_subPaneIDsFlat"
- "%{public}s"
- "%{public}s:%ld %{public}s %{public}s"
- ".cxx_destruct"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lUQ7p1/Sources/GeneralSettings/GeneralSettings/GeneralSettings.swift"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "AuthenticationExperience"
- "DeviceOSExpert"
- "ExtensionKit"
- "Found General sub-pref extension "
- "GeneralSettings.GeneralSubpane"
- "MDMDisabledSettingsPane"
- "Pantheon"
- "SemanticSearch"
- "Should never be called! "
- "Should never be called! aeDesc: "
- "SystemPrefsApp"
- "UpdatedPrimaryListOrdering"
- "UplevelPasswordManagement"
- "[MDM] Always allowed "
- "[MDM] Disabling "
- "[MDM] Not enabling "
- "_TtC15GeneralSettings6AppLog"
- "_TtC15GeneralSettings8AppError"
- "_TtC15GeneralSettings9FFManager"
- "_TtCV15GeneralSettings15GeneralSettings14GeneralSubpane"
- "_TtCV15GeneralSettings15GeneralSettings5Model"
- "_badgeCount"
- "_isDisabled"
- "_scrollToSubPaneID"
- "_subPanes"
- "addObserverForName:object:queue:usingBlock:"
- "appDomainID"
- "attentionKey"
- "backingScaleFactor"
- "bundleURL"
- "dealloc"
- "description"
- "disabledExtensionIDs"
- "disabledPrefPaneIDs"
- "enabledPrefPaneIDs"
- "ext"
- "extensible_enablement"
- "handleOpenParameter(aeDesc:)"
- "handleOpenParameterTarget"
- "icon"
- "identifier"
- "init"
- "init()"
- "initWithType:"
- "isMDMEnabled(_:)"
- "legacyBundleIDMap"
- "legacyBundleIdentifier"
- "localizedStringForKey:value:table:"
- "mainQueue"
- "mainScreen"
- "map"
- "name"
- "questionmark.square.dashed"
- "revealElement(forKey:)"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "selectedSubPane"
- "signposter"
- "subPaneIDs"
- "v16@?0@\"NSNotification\"8"
- "v16@?0@\"NSTimer\"8"
- "willSelectClosure"

```
