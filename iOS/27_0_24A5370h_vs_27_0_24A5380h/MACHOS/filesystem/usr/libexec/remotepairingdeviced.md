## remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

-  __TEXT.__text: 0x905c0
-  __TEXT.__auth_stubs: 0x42e0
-  __TEXT.__objc_stubs: 0x820
+  __TEXT.__text: 0x971b0
+  __TEXT.__auth_stubs: 0x4380
+  __TEXT.__objc_stubs: 0xa40
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x3798
-  __TEXT.__oslogstring: 0x3dbf
-  __TEXT.__cstring: 0x53ac
+  __TEXT.__const: 0x3968
+  __TEXT.__oslogstring: 0x424f
+  __TEXT.__cstring: 0x565c
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__objc_methname: 0x18d5
-  __TEXT.__objc_classname: 0x9c2
-  __TEXT.__objc_methtype: 0x46b
+  __TEXT.__objc_methname: 0x1c15
+  __TEXT.__objc_classname: 0xa32
+  __TEXT.__objc_methtype: 0x4cb
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1f40
-  __TEXT.__swift5_typeref: 0x256c
+  __TEXT.__constg_swiftt: 0x20f8
+  __TEXT.__swift5_typeref: 0x264c
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0x1b03
-  __TEXT.__swift5_fieldmd: 0x1374
+  __TEXT.__swift5_reflstr: 0x1d93
+  __TEXT.__swift5_fieldmd: 0x14b8
   __TEXT.__swift5_assocty: 0xc8
-  __TEXT.__swift5_proto: 0x134
-  __TEXT.__swift5_types: 0x108
-  __TEXT.__swift5_capture: 0x1dbc
+  __TEXT.__swift5_proto: 0x138
+  __TEXT.__swift5_types: 0x114
+  __TEXT.__swift5_capture: 0x1eb8
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_acfuncs: 0x14
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0x64
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x1ac8
-  __TEXT.__eh_frame: 0x1ee0
-  __DATA_CONST.__const: 0x5910
+  __TEXT.__swift5_acfuncs: 0x14
+  __TEXT.__unwind_info: 0x1bf8
+  __TEXT.__eh_frame: 0x2018
+  __DATA_CONST.__const: 0x5bf0
   __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x2180
-  __DATA_CONST.__got: 0xc98
-  __DATA_CONST.__auth_ptr: 0xa08
-  __DATA.__objc_const: 0x5558
-  __DATA.__objc_selrefs: 0x2b8
+  __DATA_CONST.__auth_got: 0x21d0
+  __DATA_CONST.__got: 0xcd0
+  __DATA_CONST.__auth_ptr: 0xa48
+  __DATA.__objc_const: 0x5908
+  __DATA.__objc_selrefs: 0x340
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0x47a8
-  __DATA.__bss: 0x1f48
+  __DATA.__data: 0x4b68
+  __DATA.__bss: 0x1fd0
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftData.framework/SwiftData
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3518
-  Symbols:   1697
-  CStrings:  949
+  Functions: 3696
+  Symbols:   1718
+  CStrings:  1012
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_acfuncs : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__common : content changed
Symbols:
+ _$s10Foundation14SortDescriptorV_5orderACyxGs7KeyPathCyxqd__SgG_AA0B5OrderOtcSLRd__lufC
+ _$s10Foundation3URLV19_bridgeToObjectiveCSo5NSURLCyF
+ _$s10Foundation3URLV6stringACSgSSh_tcfC
+ _$s19RemotePairingDevice0B15PolicyValidatorMp
+ _$s19RemotePairingDevice0B15PolicyValidatorP08validatebD004hostB7Options0G9Challenge10completionySDySSypGSg_10Foundation4DataVSgyAA0bD17ValidationOutcomeOctFTq
+ _$s19RemotePairingDevice0B23PolicyValidationOutcomeO17challengeRequiredyA2CmFWC
+ _$s19RemotePairingDevice0B23PolicyValidationOutcomeO7allowedyACSb_tcACmFWC
+ _$s19RemotePairingDevice0B23PolicyValidationOutcomeO8rejectedyACs5Error_pcACmFWC
+ _$s19RemotePairingDevice0B23PolicyValidationOutcomeOMa
+ _$s19RemotePairingDevice0B23PolicyValidationOutcomeOMn
+ _$s19RemotePairingDevice0aB5ErrorV21developerModeDisabledACvgZ
+ _$s19RemotePairingDevice19DeveloperModeStatusO23changedNotificationNameSSvgZ
+ _$s19RemotePairingDevice19DeveloperModeStatusO9isEnabledSbvgZ
+ _$s19RemotePairingDevice22AuditActivityAssertionC25NotificationConfigurationV10symbolNameSSvg
+ _$s19RemotePairingDevice22AuditActivityAssertionC25NotificationConfigurationV5titleSSvg
+ _$s19RemotePairingDevice22AuditActivityAssertionC25NotificationConfigurationV8subtitleSSvg
+ _$s19RemotePairingDevice23UserInteractionProviderP024collectConsentForPinlessB013withHostNamed10completionySSSg_yAA0bH17CollectionOutcomeOctFTq
+ _$s19RemotePairingDevice24ControlChannelConnectionC9transport5queue7options23maxReconnectionAttempts26pairingDataStorageProvider0M15PolicyValidator23peerWireProtocolVersionAcA0dE9Transport_p_So012OS_dispatch_H0CAC7OptionsOSiAA0bnoP0_pAA0bqR0_pAA0deftuV0CSgtcfc
+ _$sSaMa
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNNotificationSound
+ _OBJC_CLASS_$_UNTimeIntervalNotificationTrigger
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ _swift_release_x4
- _$s19RemotePairingDevice0B24ConsentCollectionOutcomeO17challengeRequiredyA2CmFWC
- _$s19RemotePairingDevice10AuditEventVSQAAMc
- _$s19RemotePairingDevice23UserInteractionProviderP024collectConsentForPinlessB013withHostNamed04hostB7Options0N9Challenge10completionySSSg_SDySSypGSg10Foundation4DataVSgyAA0bH17CollectionOutcomeOctFTq
- _$s19RemotePairingDevice24ControlChannelConnectionC9transport5queue7options23maxReconnectionAttempts26pairingDataStorageProvider23peerWireProtocolVersionAcA0dE9Transport_p_So012OS_dispatch_H0CAC7OptionsOSiAA0bnoP0_pAA0defrsT0CSgtcfc
- _strerror
- _swift_retain_x10
CStrings:
+ "$__lazy_storage_$_pairingPolicyValidator"
+ "%{public}s: Invalid state to handle pairing initiation request (current state: %{public}s, error: %{public}s)"
+ "%{public}s: Rejecting pair request because developer mode is not enabled"
+ "%{public}s: Unexpectedly received control channel invalidation for %s while in state %{public}s"
+ "Audit banners not supported on this platform"
+ "Collapsing pending banner for activity type: %{public}s"
+ "Current notification authorization status: %s"
+ "Device unlocked — invoking %ld next-unlock handler(s)"
+ "Device unlocked; delivering %ld pending audit banner(s)"
+ "Failed to mark notification presented for activity %{public}s: %{public}s"
+ "Failed to post audit banner for %{public}s: %{public}s"
+ "Failed to recover unpresented notifications: %{public}s"
+ "Failed to request notification authorization: %{public}s"
+ "Ignoring lock status change — device is not unlocked"
+ "Marked notification presented for activity: %{public}s"
+ "No stored record found for activity when marking notification presented: %{public}s"
+ "Notification authorization %s"
+ "Notification center not initialized; invoking completions without posting %ld pending banners"
+ "Pended banner for activity type: %{public}s (total pending: %ld)"
+ "Posted audit banner for activity type: %{public}s"
+ "Received next-unlock XPC event (lock status changed)"
+ "Recovering %ld unpresented notification(s) from previous session"
+ "Registered dynamic XPC event for next unlock detection"
+ "Registered next-unlock handler (total: %ld)"
+ "Started audit banner manager with section identifier: %{public}s"
+ "State dump: RSDService connection count = %ld"
+ "Unregistered dynamic XPC event for next unlock detection"
+ "UserNotifications not available on this platform; audit banners disabled"
+ "_TtC20remotepairingdeviced18AuditBannerManager"
+ "_TtC20remotepairingdeviced29DefaultPairingPolicyValidator"
+ "_completionQueue"
+ "_isDeveloperModeEnabled"
+ "_nextUnlockHandlers"
+ "_notificationCenter"
+ "_notificationPresented"
+ "_pairingPolicyValidator"
+ "_pendingBanners"
+ "_policyValidator"
+ "_registeredForNextUnlock"
+ "addNotificationRequest:withCompletionHandler:"
+ "auditActivityReportCategory"
+ "authorizationStatus"
+ "bannerManager"
+ "com.apple.RemotePairing.AuditActivityNotifications"
+ "com.apple.remotepairingdeviced.next_unlock"
+ "defaultSound"
+ "getNotificationSettingsWithCompletionHandler:"
+ "iconForSystemImageNamed:"
+ "initWithBundleIdentifier:"
+ "markNotificationPresented(id: "
+ "notificationPresented"
+ "notificationsEnabled"
+ "prefs:root=DEVELOPER_SETTINGS"
+ "prefs:root=DEVELOPER_SETTINGS&path=PAIRED_MACS/host/"
+ "recoverUnpresentedNotifications"
+ "remotepairingdeviced/DefaultPairingPolicyValidator.swift"
+ "requestAuthorizationWithOptions:completionHandler:"
+ "requestWithIdentifier:content:trigger:"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setDefaultActionURL:"
+ "setIcon:"
+ "setShouldAuthenticateDefaultAction:"
+ "setSound:"
+ "setTitle:"
+ "setWantsNotificationResponsesDelivered"
+ "triggerWithTimeInterval:repeats:"
+ "v16@?0@\"UNNotificationSettings\"8"
+ "v20@?0B8@\"NSError\"12"
- "%{public}s: Invalid state to handle pairing initiation request: %{public}s"
- "%{public}s: Unexpectedly received control channel invalidation for %s while in state unavailable"
- "Failed to fetch developer mode status: (%{public}s)"
- "State dump: NetworkPairingService connection count = %ld"
- "security.mac.amfi.developer_mode_status"
- "security.mac.amfi.developer_mode_status.changed"

```
