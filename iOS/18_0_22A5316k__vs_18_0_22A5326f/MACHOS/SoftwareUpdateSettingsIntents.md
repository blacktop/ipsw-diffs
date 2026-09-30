## SoftwareUpdateSettingsIntents

> `/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents`

```diff

-362.0.0.0.0
-  __TEXT.__text: 0x13bbc
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__const: 0x1dd4
-  __TEXT.__cstring: 0x1174
-  __TEXT.__constg_swiftt: 0x380
-  __TEXT.__swift5_typeref: 0xc7e
-  __TEXT.__swift5_reflstr: 0x413
-  __TEXT.__swift5_fieldmd: 0x26c
-  __TEXT.__objc_methname: 0x234
+371.0.0.0.0
+  __TEXT.__text: 0x15508
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__const: 0x1ef4
+  __TEXT.__cstring: 0x1204
+  __TEXT.__constg_swiftt: 0x3f4
+  __TEXT.__swift5_typeref: 0xaee
+  __TEXT.__swift5_reflstr: 0x3e3
+  __TEXT.__swift5_fieldmd: 0x278
+  __TEXT.__oslogstring: 0x6f0
+  __TEXT.__objc_methname: 0x291
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__oslogstring: 0x590
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_types: 0x50
+  __TEXT.__swift5_assocty: 0x3d0
+  __TEXT.__swift5_proto: 0x1b0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_assocty: 0x3c8
-  __TEXT.__swift5_proto: 0x1a0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x838
-  __TEXT.__eh_frame: 0x820
-  __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__auth_ptr: 0x618
-  __DATA_CONST.__const: 0x8f0
+  __TEXT.__unwind_info: 0x820
+  __TEXT.__eh_frame: 0x8a0
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_ptr: 0x5f0
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd8
-  __DATA.__objc_selrefs: 0xc8
-  __DATA.__data: 0x9e8
-  __DATA.__common: 0x230
-  __DATA.__bss: 0x3438
+  __DATA.__objc_const: 0xf8
+  __DATA.__objc_selrefs: 0xe8
+  __DATA.__data: 0x968
+  __DATA.__common: 0x198
+  __DATA.__bss: 0x3618
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 611
-  Symbols:   113
-  CStrings:  118
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 593
+  Symbols:   128
+  CStrings:  140
 
Symbols:
+ _OBJC_CLASS_$_SDBetaManager
+ _OBJC_CLASS_$_SUSettingsStatefulUIManager
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x24
+ _objc_retain_x1
+ _objc_retain_x28
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_getMetatypeMetadata
- __swiftEmptyDictionarySingleton
- _objc_release_x27
CStrings:
+ "APP_INTENT_GET_AUTO_INSTALL_UPDATES_NAME"
+ "APP_INTENT_SET_AUTO_INSTALL_UPDATES_NAME"
+ "APP_INTENT_SOFTWARE_UPDATE_CUSTOMER_UPDATE_PROGRAM"
+ "APP_INTENT_SOFTWARE_UPDATE_CUSTOMER_UPDATE_PROGRAM_DESCIPTION"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_BETA"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_BETA_DESCIPTION"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_DEEPLINK"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_INTENT"
+ "Automatic Install"
+ "AutomaticInstallUpdatesEntity"
+ "Automatically Install Updates"
+ "Check if there is software update available"
+ "Get Automatic Install Updates"
+ "Get Automatically Install Updates"
+ "Get the 'Automatically Install Updates' status"
+ "SOFTWARE_UPDATE_LINK"
+ "SOFTWARE_UPDATE_LINK/SUBetaUpdatesButton"
+ "SOFTWARE_UPDATE_LINK?PerformAction=SUSUIUpdateNowAction"
+ "SOFTWARE_UPDATE_LINK?PerformAction=SUSUIUpdateTonightAction"
+ "Set Automatic Install Updates"
+ "Set Automatically Install Updates"
+ "Set the 'Automatically Install Updates' status"
+ "The timing when to run software update"
+ "Unable to check for available updates"
+ "Which program to run software update"
+ "beta update, beta updates, developer update, developer updates, seed update, seed updates"
+ "canCurrentDeviceEnrollInBetaUpdates"
+ "initWithManagerClient:"
+ "manager"
+ "no client instance, unable to check for updates"
+ "refreshBetaUpdates()"
+ "refreshBetaUpdates:"
+ "settings-navigation://com.apple.Settings.General/"
+ "sharedManager"
+ "suggestedEntities()"
+ "v24@?0@\"SUSettingsBetaUpdatesScanResults\"8@\"NSError\"16"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Finished to refreshBetaUpdates"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Starting to refreshBetaUpdates"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Unable to create SUManagerClient instance"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Unable to create SUSettingsStatefulUIManager"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Unable to init SUManagerClient"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => filter results: %!s(MISSING)"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => finish to refreshBetaUpdates"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => returning %!s(MISSING)"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => start to refreshBetaUpdates"
- "APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME to update"
- "APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME to update on APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "APP_INTENT_ENTITY_SU_AVAILABLE_NAME to update"
- "APP_INTENT_ENTITY_SU_AVAILABLE_NAME to update on APP_INTENT_ENTITY_SU_AVAILABLE_NAME"
- "Automatic Install Update"
- "Change the APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME value of APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "Change the APP_INTENT_ENTITY_SU_AVAILABLE_NAME value of APP_INTENT_ENTITY_SU_AVAILABLE_NAME"
- "Intent getting the value of the OS Automatic Install Updates: %!{(MISSING)bool}d"
- "Scan and check if there is a software update available"
- "The 'Automatically Install Updates' toggle option in the software update settings"
- "The set property should not be used by the entity, only by the 'AutomaticInstallUpdatesEntityIntent' perform() call"
- "The set property should not be used by the entity."
- "UnsafeMutablePointer.initialize with negative count"
- "Update APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "Update APP_INTENT_ENTITY_SU_AVAILABLE_NAME"
- "UpdateAutomaticInstallUpdatesEntityBindingvalforgetonlyIntent"
- "UpdateSoftwareUpdateAvailableEntityIntentautovalueIntent"
- "When to run software update"
- "now"
- "settings-navigation://com.apple.Settings.General/SOFTWARE_UPDATE_LINK?PerformAction=SUSUIUpdateNowAction"
- "settings-navigation://com.apple.Settings.General/SOFTWARE_UPDATE_LINK?PerformAction=SUSUIUpdateTonightAction"
- "tonight"

```
