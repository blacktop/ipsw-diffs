## NotesUIServices

> `/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices`

```diff

-2654.51.0.0.0
-  __TEXT.__text: 0xe1a8
+2662.0.0.0.0
+  __TEXT.__text: 0xe0d8
   __TEXT.__auth_stubs: 0xcf0
   __TEXT.__objc_methlist: 0x12c
   __TEXT.__const: 0x922

   __TEXT.__objc_methname: 0x691
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_ptr: 0x358
   __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__objc_const: 0x5f0
-  __AUTH.__objc_data: 0x308
-  __AUTH.__data: 0xa8
-  __DATA.__data: 0x3f0
-  __DATA.__bss: 0x348
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__data: 0x210
+  __DATA.__data: 0x1a8
+  __DATA.__bss: 0x248
+  __DATA_DIRTY.__objc_data: 0x4e8
+  __DATA_DIRTY.__data: 0x500
   __DATA_DIRTY.__common: 0x28
-  __DATA_DIRTY.__bss: 0x680
+  __DATA_DIRTY.__bss: 0x780
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 397
-  Symbols:   163
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 396
+  Symbols:   171
+  CStrings:  79
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "$__CDContact"
+ "BJC_METACLASS_$__CDRateLimiter"
+ "LASS_$__DKSearchFeedbackMetadataKey"
+ "_OBJC_CLASS_$_BMComputeSourceClient"
+ "_OBJC_CLASS_$_BMComputeTombstonePropagator"
+ "_OBJC_CLASS_$_BMComputeXPCPublisherStorage"
+ "_OBJC_CLASS_$_BMDaemon"
+ "_OBJC_CLASS_$_BMSQLColumn"
+ "_OBJC_CLASS_$_BMSQLProtoColumn"
+ "_OBJC_CLASS_$_BMSQLSchema"
+ "_OBJC_CLASS_$_BMSource"
+ "_OBJC_CLASS_$_BMStorePublisherManagerProtectedState"
+ "_OBJC_CLASS_$_BMStoreSource"
+ "_OBJC_CLASS_$_BMStoreStreamPruningBridge"
+ "_OBJC_CLASS_$_BMStreamConfiguration"
+ "_OBJC_CLASS_$_BPSBiomeStorePublisher"
+ "_OBJC_CLASS_$__BMLibraryAndInternalLibraryNode"
+ "_OBJC_CLASS_$__CDEntityMetadataKey"
+ "_OBJC_CLASS_$__CDInteraction"
+ "_OBJC_CLASS_$__CDPortraitMetadataKey"
+ "_OBJC_CLASS_$__DKAirPlayPredictionMetadataKey"
+ "_OBJC_CLASS_$__DKAppClipUsageMetadataKey"
+ "_OBJC_CLASS_$__DKAppInstallMetadataKey"
+ "_OBJC_CLASS_$__DKAppIntentsStreamTombstoneRequirement"
+ "_OBJC_CLASS_$__DKAppMediaUsageMetadataKey"
+ "_OBJC_CLASS_$__DKAppUsageTombstoneRequirement"
+ "_OBJC_CLASS_$__DKApplicationActivityMetadataKey"
+ "_OBJC_CLASS_$__DKAudioMetadataKey"
+ "_OBJC_CLASS_$__DKBatterySaverMetadataKey"
+ "_OBJC_CLASS_$__DKBehavioralRuleFeaturesMetadataKey"
+ "_OBJC_CLASS_$__DKBluetoothMetadataKey"
+ "_OBJC_CLASS_$__DKBulletinBoardMetadataKey"
+ "_OBJC_CLASS_$__DKBundleIdentifier"
+ "_OBJC_CLASS_$__DKCalendarMetadataKey"
+ "_OBJC_CLASS_$__DKCallMetadataKey"
+ "_OBJC_CLASS_$__DKDeviceBatteryPercentageMetadataKey"
+ "_OBJC_CLASS_$__DKDeviceIdMetadataKey"
+ "_OBJC_CLASS_$__DKDeviceIsPluggedInMetadataKey"
+ "_OBJC_CLASS_$__DKDeviceStandbyTimerMetadataKey"
+ "_OBJC_CLASS_$__DKDiscoverabilityUsageMetadataKey"
+ "_OBJC_CLASS_$__DKFamilyPredictionMetadataKey"
+ "_OBJC_CLASS_$__DKLocationApplicationActivityMetadataKey"
+ "_OBJC_CLASS_$__DKLocationMetadataKey"
+ "_OBJC_CLASS_$__DKMapsShareEtaFeedbackMetadataKey"
+ "_OBJC_CLASS_$__DKMetadataHomeAppView"
+ "_OBJC_CLASS_$__DKMetadataHomeKitAccessoryControl"
+ "_OBJC_CLASS_$__DKMetadataHomeKitScene"
+ "_OBJC_CLASS_$__DKMetadataPersistenceLookupTable"
+ "_OBJC_CLASS_$__DKMicroLocationMetadataKey"
+ "_OBJC_CLASS_$__DKNotificationUsageMetadataKey"
+ "_OBJC_CLASS_$__DKNowPlayingMetadataKey"
+ "_OBJC_CLASS_$__DKPeopleSuggesterOutputForSiriNLMetadataKey"
+ "_OBJC_CLASS_$__DKPeriodMetadataKey"
+ "_OBJC_CLASS_$__DKPhotosMetadataKeys"
+ "_OBJC_CLASS_$__DKRelevantShortcutMetadataKey"
+ "_OBJC_CLASS_$__DKSafariHistoryMetadataKey"
+ "_OBJC_CLASS_$__DKShareSheetSuggestLessFeedbackMetadataKey"
+ "_OBJC_CLASS_$__DKSiriServiceMetadataKey"
+ "_OBJC_CLASS_$__DKTimerMetadataKey"
+ "_OBJC_METACLASS_$_BMComputeSourceClient"
+ "_OBJC_METACLASS_$_BMComputeTombstonePropagator"
+ "_OBJC_METACLASS_$_BMComputeXPCPublisherStorage"
+ "_OBJC_METACLASS_$_BMDaemon"
+ "_OBJC_METACLASS_$_BMPublisherOptions"
+ "_OBJC_METACLASS_$_BMSQLProtoColumn"
+ "_OBJC_METACLASS_$_BMSQLSchema"
+ "_OBJC_METACLASS_$_BMSource"
+ "_OBJC_METACLASS_$_BMStorePublisherManagerProtectedState"
+ "_OBJC_METACLASS_$_BMStoreSource"
+ "_OBJC_METACLASS_$_BMStoreStreamPruningBridge"
+ "_OBJC_METACLASS_$_BMStream"
+ "_OBJC_METACLASS_$_BMStreamBase"
+ "_OBJC_METACLASS_$_BPSBiomeStorePublisher"
+ "_OBJC_METACLASS_$__BMLibraryAndInternalLibraryNode"
+ "_OBJC_METACLASS_$__CDContact"
+ "_OBJC_METACLASS_$__CDInteraction"
+ "_OBJC_METACLASS_$__DKBundleIdentifier"
+ "ement"
+ "lisherOptions"

```
