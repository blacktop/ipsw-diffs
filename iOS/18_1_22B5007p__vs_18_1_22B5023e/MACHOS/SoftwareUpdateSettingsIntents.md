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
+384.0.0.0.0
+  __TEXT.__text: 0x179f4
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__const: 0x23f4
+  __TEXT.__cstring: 0x1135
+  __TEXT.__constg_swiftt: 0x450
+  __TEXT.__swift5_typeref: 0xc02
+  __TEXT.__swift5_reflstr: 0x473
+  __TEXT.__swift5_fieldmd: 0x2ac
+  __TEXT.__oslogstring: 0x6c0
+  __TEXT.__objc_methname: 0x291
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__oslogstring: 0x590
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_assocty: 0x410
+  __TEXT.__swift5_proto: 0x200
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
+  __TEXT.__unwind_info: 0x890
+  __TEXT.__eh_frame: 0x800
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x4f8
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd8
-  __DATA.__objc_selrefs: 0xc8
-  __DATA.__data: 0x9e8
-  __DATA.__common: 0x230
-  __DATA.__bss: 0x3438
+  __DATA.__objc_const: 0xf8
+  __DATA.__objc_selrefs: 0xe8
+  __DATA.__data: 0xb70
+  __DATA.__common: 0x258
+  __DATA.__bss: 0x4018
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWebKit.dylib
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
+  Functions: 637
+  Symbols:   131
+  CStrings:  132
 
Symbols:
+ _OBJC_CLASS_$_SDBetaManager
+ _OBJC_CLASS_$_SUSettingsStatefulUIManager
+ __swift_FORCE_LOAD_$_swiftWebKit
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
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getMetatypeMetadata
+ _swift_getSingletonMetadata
+ _swift_initStructMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
- __swiftEmptyDictionarySingleton
- __swiftImmortalRefCount
- _objc_release_x27
CStrings:
+ "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_DESC"
+ "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE"
+ "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE to update"
+ "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE to update on APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE"
+ "APP_INTENT_ENTITY_AUTO_INSTALL_SECURITY_RESPONSES_DESC"
+ "APP_INTENT_GET_AUTO_INSTALL_UPDATES_DESC"
+ "APP_INTENT_GET_AUTO_INSTALL_UPDATES_NAME"
+ "APP_INTENT_SET_AUTO_INSTALL_UPDATES_DESC"
+ "APP_INTENT_SET_AUTO_INSTALL_UPDATES_NAME"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_BETA_DESCIPTION"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_BETA_TITLE"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_DESCIPTION"
+ "APP_INTENT_SOFTWARE_UPDATE_PROGRAM_TITLE"
+ "Automatic Install"
+ "AutomaticInstallUpdatesEntity"
+ "Change the APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE value of APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE"
+ "Error message when attempting to show beta updates while user is not enrolled."
+ "Get Automatic Install Updates"
+ "Get Automatically Install Updates"
+ "Not enrolled to the beta updates"
+ "OpenSoftwareUpdateOfRelevantProgramIntent"
+ "Set Automatic Install Updates"
+ "Set Automatically Install Updates"
+ "Unable to check for available updates"
+ "Update APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_TITLE"
+ "beta update, beta updates, developer update, developer updates, seed update, seed updates"
+ "canCurrentDeviceEnrollInBetaUpdates"
+ "initWithManagerClient:"
+ "manager"
+ "no client instance, unable to check for updates"
+ "refreshBetaUpdates()"
+ "refreshBetaUpdates:"
+ "settings-navigation://com.apple.Settings.General/SOFTWARE_UPDATE_LINK"
+ "settings-navigation://com.apple.Settings.General/SOFTWARE_UPDATE_LINK/SUBetaUpdatesButton"
+ "sharedManager"
+ "v24@?0@\"SUSettingsBetaUpdatesScanResults\"8@\"NSError\"16"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Finished to refreshBetaUpdates"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Starting to refreshBetaUpdates"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Unable to create SUManagerClient instance"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Unable to create SUSettingsStatefulUIManager"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => Unable to init SUManagerClient"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => finish to refreshBetaUpdates"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => returning %!s(MISSING)"
+ "🐞 %!s(MISSING) | %!s(MISSING) | line:%!l(MISSING)d => start to refreshBetaUpdates"
- "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME"
- "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME to update"
- "APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME to update on APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME"
- "APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME to update"
- "APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME to update on APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "APP_INTENT_ENTITY_SU_AVAILABLE_NAME to update"
- "APP_INTENT_ENTITY_SU_AVAILABLE_NAME to update on APP_INTENT_ENTITY_SU_AVAILABLE_NAME"
- "APP_INTENT_OPEN_INTENT_UPDATE_DESCRIPTION"
- "APP_INTENT_OPEN_INTENT_UPDATE_TITLE"
- "Automatic Install Update"
- "Change the APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME value of APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME"
- "Change the APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME value of APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "Change the APP_INTENT_ENTITY_SU_AVAILABLE_NAME value of APP_INTENT_ENTITY_SU_AVAILABLE_NAME"
- "Intent getting the value of the OS Automatic Install Updates: %!{(MISSING)bool}d"
- "Scan and check if there is a software update available"
- "The 'Automatically Download Updates' toggle option in the software update settings"
- "The 'Automatically Install Security Responses' toggle option in the software update settings"
- "The 'Automatically Install Updates' toggle option in the software update settings"
- "The set property should not be used by the entity, only by the 'AutomaticInstallUpdatesEntityIntent' perform() call"
- "The set property should not be used by the entity."
- "UnsafeMutablePointer.initialize with negative count"
- "Update APP_INTENT_ENTITY_AUTO_DOWNLOAD_UPDATES_NAME"
- "Update APP_INTENT_ENTITY_AUTO_INSTALL_UPDATES_NAME"
- "Update APP_INTENT_ENTITY_SU_AVAILABLE_NAME"
- "UpdateAutomaticInstallUpdatesEntityBindingvalforgetonlyIntent"
- "UpdateSoftwareUpdateAvailableEntityIntentautovalueIntent"
- "When to run software update"
- "now"
- "tonight"

```
