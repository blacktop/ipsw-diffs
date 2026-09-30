## demod

> `/usr/libexec/demod`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_data`

```diff

-1871.0.29.0.0
-  __TEXT.__text: 0xf43d4
-  __TEXT.__auth_stubs: 0x20b0
-  __TEXT.__objc_stubs: 0x1b480
-  __TEXT.__objc_methlist: 0xd944
-  __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x10bb2
-  __TEXT.__objc_classname: 0x186a
-  __TEXT.__objc_methtype: 0x3fdb
-  __TEXT.__gcc_except_tab: 0x46bc
-  __TEXT.__oslogstring: 0x1c93c
-  __TEXT.__objc_methname: 0x20de1
+1871.0.42.0.0
+  __TEXT.__text: 0xf66fc
+  __TEXT.__auth_stubs: 0x2110
+  __TEXT.__objc_stubs: 0x1b6c0
+  __TEXT.__objc_methlist: 0xdb24
+  __TEXT.__const: 0x530
+  __TEXT.__cstring: 0x10d22
+  __TEXT.__objc_classname: 0x188a
+  __TEXT.__objc_methtype: 0x409b
+  __TEXT.__gcc_except_tab: 0x4750
+  __TEXT.__oslogstring: 0x1cc3c
+  __TEXT.__objc_methname: 0x21321
   __TEXT.__swift5_typeref: 0x112
-  __TEXT.__swift5_capture: 0x94
+  __TEXT.__swift5_capture: 0xcc
   __TEXT.__constg_swiftt: 0x80
   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift_as_cont: 0x20
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x3a28
-  __TEXT.__eh_frame: 0x310
-  __DATA_CONST.__const: 0x31c0
-  __DATA_CONST.__cfstring: 0xec40
+  __TEXT.__unwind_info: 0x3ab8
+  __TEXT.__eh_frame: 0x3d0
+  __DATA_CONST.__const: 0x3260
+  __DATA_CONST.__cfstring: 0xeca0
   __DATA_CONST.__objc_classlist: 0x720
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x418

   __DATA_CONST.__objc_arrayobj: 0x468
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__auth_got: 0x1068
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__auth_ptr: 0x180
-  __DATA.__objc_const: 0x19710
-  __DATA.__objc_selrefs: 0x80c0
-  __DATA.__objc_ivar: 0xb34
+  __DATA_CONST.__auth_got: 0x1098
+  __DATA_CONST.__got: 0xf20
+  __DATA_CONST.__auth_ptr: 0x190
+  __DATA.__objc_const: 0x19828
+  __DATA.__objc_selrefs: 0x8200
+  __DATA.__objc_ivar: 0xb38
   __DATA.__objc_data: 0x4800
-  __DATA.__data: 0x2990
+  __DATA.__data: 0x29f8
   __DATA.__bss: 0x990
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6048
-  Symbols:   1048
-  CStrings:  10853
+  Functions: 6088
+  Symbols:   1056
+  CStrings:  10924
 
Symbols:
+ _$s16GenerativeModels0aB12AvailabilityV12enhancedSiriAC0C0OvgZ
+ _$s16GenerativeModels0aB12AvailabilityV19enhancedSiriChangesAC08EnhancedE14ChangeSequenceVvgZ
+ _$s16GenerativeModels0aB12AvailabilityV26EnhancedSiriChangeSequenceV17makeAsyncIteratorAE0J0VyF
+ _$s16GenerativeModels0aB12AvailabilityV26EnhancedSiriChangeSequenceV8IteratorVMa
+ _$s16GenerativeModels0aB12AvailabilityV26EnhancedSiriChangeSequenceV8IteratorVScIAAMc
+ _$s16GenerativeModels0aB12AvailabilityV26EnhancedSiriChangeSequenceVMa
+ _OBJC_CLASS_$_AFSiriAvailability
+ _dispatch_group_async
+ _swift_retain_x23
- _swift_retain_x19
CStrings:
+ "%s - %{bool}d"
+ "%s - Error reading availability from AFSiriAvailability"
+ "%s - Start waitForGMAvailability"
+ "%s was called. HS set to '%@'"
+ "+[MSDGreyMatterAvailabilityChecker waitForSiriAIAvailability]"
+ "+[MSDGreyMatterOpter isSiriAIOptedIn]"
+ "+[MSDGreyMatterOpter migrateOptInValue]"
+ "-[MSDHomeManager _handleHeySiriSetting:]"
+ "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata/com.apple.MobileStoreDemo.homekitkeychain"
+ "Device is not eligible for Siri AI."
+ "Failed to load HomeKit pairing keychain info from demo volume."
+ "Failed to save HomeKit pairing keychain info to demo volume."
+ "HMHomeManagerDelegatePrivate"
+ "MSDKeychainSaver"
+ "No need to restore HomeKit pairing record."
+ "Not all Siri support apps downloaded in the given time interval"
+ "Refusing to lock home based on home unlock feature flag"
+ "Restoring HomeKit pairing information to keychain."
+ "Saving HomeKit pairing info stored in keychain."
+ "Siri AI is already available: %s"
+ "Siri AI is not available: %s Waiting for Siri AI availability."
+ "Siri AI is now available."
+ "Siri Support App(s) %@ failed to install"
+ "TB,V_siriOn"
+ "Timed out after %d minutes waiting for Siri AI availability."
+ "Toggled HS/JS for accessory with UUID %{public}@"
+ "_handleHeySiriSetting:"
+ "_siriOn"
+ "checkSiriAIAvailabilityWithCompletion:"
+ "com.apple.SiriApp"
+ "com.apple.hap.pairing"
+ "currentHome"
+ "desiredOrchestrationMode"
+ "fromPreferences"
+ "getAppleIntelligenceAppsToWaitFor"
+ "homeManager:didRemoveHomePermanently:"
+ "homeManager:didUpdateAccessAllowedWhenLocked:"
+ "homeManager:didUpdateDevices:"
+ "homeManager:didUpdateHH2MigrationAvailableState:"
+ "homeManager:didUpdateHH2MigrationInProgressState:"
+ "homeManager:didUpdateHH2State:"
+ "homeManager:didUpdateHomeSafetySecurityEnabled:"
+ "homeManager:didUpdateMultiUserStatus:reason:"
+ "homeManager:didUpdateResidentEnabledForThisDevice:"
+ "homeManager:didUpdateStateForIncomingInvitations:"
+ "homeManager:didUpdateStatus:"
+ "homeManager:didUpdateThisDeviceIsResidentCapable:"
+ "homeManager:residentProvisioningStatusChanged:"
+ "homeManagerDidEndBatchNotifications:"
+ "homeManagerDidRemoveCurrentAccessory:"
+ "homeManagerDidUpdateApplicationData:"
+ "homeManagerDidUpdateAssistantIdentifiers:"
+ "homeManagerDidUpdateCurrentHome:"
+ "homeManagerDidUpdateDataSyncInProgress:"
+ "homeManagerDidUpdateDataSyncState:"
+ "homeManagerWillStartBatchNotifications:"
+ "isEligibleForSiriAI"
+ "isSiriAIOptedIn"
+ "listenForSiri"
+ "preserveHomeKitPairingRecord"
+ "removeHomeKitPairingIfNeeded"
+ "restoreHomeKitPairingRecordIfNeeded"
+ "setAppleIntelligenceFallback:"
+ "setIsSiriAIOptedIn:"
+ "setSiriOn:"
+ "shouldRestoreHomeKitPairingRecord"
+ "siriOn"
+ "v28@0:8@\"HMHomeManager\"16B24"
+ "v32@0:8@\"HMHomeManager\"16@\"NSArray\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"NSSet\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"NSUUID\"24"
+ "v40@0:8@\"HMHomeManager\"16q24@\"NSString\"32"
+ "waitForAppleIntelligenceAvailability"
+ "waitForSiriAIAvailability"
- "Disabled HS/JS for accessory with UUID %{public}@"
- "Image Playground failed to install"
- "MSDContinuityHelper"
```
