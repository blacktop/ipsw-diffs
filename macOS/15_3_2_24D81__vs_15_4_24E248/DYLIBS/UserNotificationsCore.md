## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Versions/A/UserNotificationsCore`

```diff

-579.4.3.401.0
-  __TEXT.__text: 0x1b9c68
-  __TEXT.__auth_stubs: 0x3150
-  __TEXT.__objc_methlist: 0x6270
-  __TEXT.__const: 0xbf18
-  __TEXT.__cstring: 0xd023
-  __TEXT.__oslogstring: 0xd388
+579.5.24.0.0
+  __TEXT.__text: 0x1bf46c
+  __TEXT.__auth_stubs: 0x3100
+  __TEXT.__objc_methlist: 0x751c
+  __TEXT.__const: 0xc088
+  __TEXT.__cstring: 0xcd43
+  __TEXT.__oslogstring: 0xd428
   __TEXT.__gcc_except_tab: 0x6bc
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__constg_swiftt: 0x5428
-  __TEXT.__swift5_typeref: 0x5030
-  __TEXT.__swift5_reflstr: 0x303a
-  __TEXT.__swift5_fieldmd: 0x3a88
-  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__constg_swiftt: 0x554c
+  __TEXT.__swift5_typeref: 0x50a6
+  __TEXT.__swift5_reflstr: 0x30ca
+  __TEXT.__swift5_fieldmd: 0x3afc
+  __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x480
-  __TEXT.__swift5_capture: 0x1594
+  __TEXT.__swift5_capture: 0x1580
   __TEXT.__swift5_protos: 0xf0
   __TEXT.__swift5_proto: 0x9b0
-  __TEXT.__swift5_types: 0x458
+  __TEXT.__swift5_types: 0x46c
+  __TEXT.__swift_as_entry: 0x118
+  __TEXT.__swift_as_ret: 0x114
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x57b8
-  __TEXT.__eh_frame: 0x5190
+  __TEXT.__unwind_info: 0x54d8
+  __TEXT.__eh_frame: 0x53a0
   __TEXT.__objc_classname: 0xded
-  __TEXT.__objc_methname: 0x155b5
+  __TEXT.__objc_methname: 0x156fd
   __TEXT.__objc_methtype: 0x30f0
   __TEXT.__objc_stubs: 0xc720
-  __DATA_CONST.__got: 0xf38
-  __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__got: 0x1050
+  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fb0
+  __DATA_CONST.__objc_selrefs: 0x4388
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x18b8
-  __AUTH_CONST.__const: 0xa580
+  __AUTH_CONST.__auth_got: 0x1890
+  __AUTH_CONST.__const: 0xa688
   __AUTH_CONST.__cfstring: 0x5560
-  __AUTH_CONST.__objc_const: 0x23c90
+  __AUTH_CONST.__objc_const: 0x21b10
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH.__objc_data: 0x33e8
-  __AUTH.__data: 0x6378
+  __AUTH.__objc_data: 0x33c8
+  __AUTH.__data: 0x6458
   __DATA.__objc_ivar: 0x858
-  __DATA.__data: 0x48b8
+  __DATA.__data: 0x4948
   __DATA.__bss: 0x110f0
-  __DATA.__common: 0x440
+  __DATA.__common: 0x438
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5AE94B45-0E65-3482-8DFD-7BE1FA5A1E2B
-  Functions: 8583
-  Symbols:   9019
+  UUID: CBF29AEB-E7EF-396D-A6EE-504B41175A23
+  Functions: 8434
+  Symbols:   9136
   CStrings:  6668
 
Symbols:
+ +[TLAlert(UserNotificationsCore) unc_toneLibraryAlertTypeForSectionID:].cold.1
+ +[UNCBulletinDefaults standardDefaults].cold.1
+ +[UNCBulletinServerConnection clientInterface].cold.1
+ +[UNCBulletinServerConnection serverInterface].cold.1
+ +[UNCNotificationServiceExtension _extensionIdentifiersCurrentlyAllowedAccessToNotificationCenter].cold.1
+ +[UNCNotificationServiceExtension _extensionIdentifiersToPerExtensionQueues].cold.1
+ +[UNCNotificationSystemService serviceInterface].cold.1
+ +[UNCSettingsRemotePersistenceService _allowedClasses].cold.1
+ +[UNCSettingsRemotePersistenceService clientInterface].cold.1
+ +[UNCSpotlightDaemonClient sharedInstance].cold.1
+ -[UNCLocalNotificationClient _dateFormatter].cold.1
+ -[UNCNotificationSchedule _dateFormatter].cold.1
+ -[UNCNotificationScheduleRepository _dateFormatter].cold.1
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table36
+ GCC_except_table43
+ UNSNotificationRecordDictionaryValidation_block_invoke_4.cold.1
+ _DNDIntelligentInterruptionBehaviorToString
+ _OBJC_CLASS_$_DNDStateService
+ _PROTOCOLS__TtC21UserNotificationsCore35NotificationSourceMonitorLSObserver.39
+ _PROTOCOLS__TtCC21UserNotificationsCore29RemoteNotificationsProperties14DeviceObserver.65
+ _UNCTopicSummaries
+ __DATA__TtC21UserNotificationsCore34UNGenerativeModelAvailabilityCache
+ __IVARS__TtC21UserNotificationsCore34UNGenerativeModelAvailabilityCache
+ __METACLASS_DATA__TtC21UserNotificationsCore34UNGenerativeModelAvailabilityCache
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_2Tm
+ ___swift_project_boxed_opaque_existential_0
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_UserNotificationsCore
+ _symbolic SDySaySSG_____G 16GenerativeModels0aB12AvailabilityV0C0O
+ _symbolic SaySSG______t 16GenerativeModels0aB12AvailabilityV0C0O
+ _symbolic SccyShySo22SFAuthenticationDeviceCG______pG s5ErrorP
+ _symbolic Sccy___________pG So33UNNotificationPresentationOptionsV s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic _____ 21UserNotificationsCore34UNGenerativeModelAvailabilityCacheC
+ _symbolic _____ So11CFStringRefa
+ _symbolic _____ So18CFNotificationNamea
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV0C0O
+ _symbolic _____ySaySSG_____G s18_DictionaryStorageC 16GenerativeModels0cD12AvailabilityV0E0O
+ _symbolic y_____Sg_SvSg_____SgSVSg_____SgtXC So23CFNotificationCenterRefa So0A4Namea So012CFDictionaryC0a
+ block_copy_helper.135
+ block_copy_helper.141
+ block_copy_helper.62
+ block_descriptor.137
+ block_descriptor.143
+ block_descriptor.64
+ block_destroy_helper.136
+ block_destroy_helper.142
+ block_destroy_helper.63
+ objectdestroy.94Tm
- GCC_except_table19
- GCC_except_table37
- GCC_except_table41
- GCC_except_table44
- _PROTOCOLS__TtC21UserNotificationsCore35NotificationSourceMonitorLSObserver.40
- _PROTOCOLS__TtCC21UserNotificationsCore29RemoteNotificationsProperties14DeviceObserver.67
- ___swift_destroy_boxed_opaque_existential_2
- _symbolic SS3key______5valuetSg s11AnyHashableV
- _symbolic Si6offset_______p7elementtSg 21UserNotificationsCore14StateCapturingP
- _symbolic _____Sg 21UserNotificationsCore17ReplicatorManagerC
- _symbolic _____ySSGSg 25UserNotificationsServices7UNSListV
- block_copy_helper.140
- block_copy_helper.146
- block_copy_helper.24
- block_copy_helper.63
- block_copy_helper.92
- block_descriptor.142
- block_descriptor.148
- block_descriptor.26
- block_descriptor.65
- block_descriptor.94
- block_destroy_helper.141
- block_destroy_helper.147
- block_destroy_helper.25
- block_destroy_helper.64
- block_destroy_helper.93
- objectdestroy.96Tm
CStrings:
+ "%s, privacy: .public) Not indexing to spotlight because categorizer doesn't allow."
+ "Could not find group for group summary: %{public}s, %{private}s, %{public}s"
+ "Generative models restricted."
+ "Generative models unavailable."
+ "Processing group summary: %{public}s, %{private}s, %{public}s"
+ "Untool values of summary: %s and isHighlight: %{bool}d, written as %s on a faked forwardingBehavior"
+ "[%{public}s] Could not determine source prioritization setting."
+ "[id=%s] Found observer that's older than %f seconds. Likely abandoned."
+ "_TtC21UserNotificationsCore34UNGenerativeModelAvailabilityCache"
+ "_UNGenerativeModelsAvailabilityDidChange"
+ "_UNGenerativeModelsAvailabilityDidChangeNotificationName"
+ "activeModeConfiguration"
+ "allowIntelligentManagement"
+ "appProtectionActive"
+ "cache"
+ "com.apple.UserNotificationCore.SpotlightIndexer"
+ "com.apple.gms.availability.notification"
+ "configuration"
+ "forwardingBehavior"
+ "initWithEventDetails:interruptionSuppression:intelligentBehavior:resolutionReason:activeModeUUID:"
+ "intelligentBehavior"
+ "isEligibleForIndexing"
+ "languageCode"
+ "prioritizationSetting"
+ "queryCurrentStateWithError:"
+ "replicator"
+ "setForwardingBehavior:"
+ "setUrgencyStatus:"
+ "settingsNotEligible"
- "$__lazy_storage_$_replicator"
- "%s, privacy: .public) Not indexing to spotlight because in newsAndEntertainment"
- "Could not find group for group summary: %{public}s, %{private}s, %{private}s"
- "Division by zero"
- "Division results in an overflow"
- "Generative models restricted. Info: %s"
- "Generative models unavailable. Info: %s"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Processing group summary: %{public}s, %{private}s, %{private}s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "[id=%s] Found observer that's older than %f seconds. Likely abandonded."
- "invalid Collection: less than 'count' elements in collection"

```
