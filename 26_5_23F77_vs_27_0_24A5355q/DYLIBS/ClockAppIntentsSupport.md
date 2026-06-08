## ClockAppIntentsSupport

> `/System/Library/PrivateFrameworks/ClockAppIntentsSupport.framework/ClockAppIntentsSupport`

```diff

-268.5.1.0.0
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x42
-  __DATA_CONST.__const: 0xa8
+299.0.0.0.0
+  __TEXT.__text: 0x18520
+  __TEXT.__objc_methlist: 0x2d4
+  __TEXT.__const: 0xfb8
+  __TEXT.__swift5_typeref: 0x666
+  __TEXT.__swift5_reflstr: 0x10a
+  __TEXT.__swift5_assocty: 0x160
+  __TEXT.__constg_swiftt: 0x224
+  __TEXT.__swift5_fieldmd: 0xf8
+  __TEXT.__swift5_proto: 0x84
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift_as_entry: 0xe8
+  __TEXT.__swift_as_ret: 0xe8
+  __TEXT.__swift_as_cont: 0x15c
+  __TEXT.__swift5_capture: 0x970
+  __TEXT.__oslogstring: 0xa4
+  __TEXT.__cstring: 0x126
+  __TEXT.__unwind_info: 0x850
+  __TEXT.__eh_frame: 0x13dc
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x1f8
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x1748
+  __AUTH_CONST.__objc_const: 0x2a0
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH.__objc_data: 0x90
+  __DATA.__data: 0x150
+  __DATA.__bss: 0xa00
+  __DATA.__common: 0x48
+  __DATA_DIRTY.__objc_data: 0x1c8
+  __DATA_DIRTY.__data: 0x2f8
+  __DATA_DIRTY.__bss: 0x680
+  __DATA_DIRTY.__common: 0x18
+  - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
+  - /System/Library/Frameworks/CoreTransferable.framework/CoreTransferable
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AlarmAppIntents.framework/AlarmAppIntents
+  - /System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/AppIntentsLiveEntitySupport
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport
+  - /System/Library/PrivateFrameworks/StopwatchAppIntents.framework/StopwatchAppIntents
+  - /System/Library/PrivateFrameworks/TimerAppIntents.framework/TimerAppIntents
+  - /System/Library/PrivateFrameworks/WorldClockAppIntents.framework/WorldClockAppIntents
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A34A4009-55C7-37FC-86FE-79BEDABECE70
-  Functions: 0
-  Symbols:   45
-  CStrings:  0
+  UUID: 1C0E2759-A9C2-303F-858B-17D96A5A3787
+  Functions: 656
+  Symbols:   764
+  CStrings:  13
 
Symbols:
+ +[MTAppEntityAssociator addAlarmsToIndex:]
+ +[MTAppEntityAssociator addTimersToIndex:]
+ +[MTAppEntityAssociator alarmDidStartFiring:]
+ +[MTAppEntityAssociator alarmDidStopFiring:]
+ +[MTAppEntityAssociator criticalSearchableIndexWithName:bundleIdentifier:]
+ +[MTAppEntityAssociator deleteAlarmsInIndex:]
+ +[MTAppEntityAssociator deleteTimersInIndex:]
+ +[MTAppEntityAssociator reindexWithAlarms:timers:]
+ +[MTAppEntityAssociator reindexWithTimers:]
+ +[MTAppEntityAssociator timerDidStartCountdown:]
+ +[MTAppEntityAssociator timerDidStartFiring:]
+ +[MTAppEntityAssociator timerDidStopFiring:]
+ +[MTAppEntityAssociator timerWasRemoved:]
+ +[MTAppEntityAssociator updateAlarmsInIndex:]
+ +[MTAppEntityAssociator updateStopwatch:]
+ +[MTAppEntityAssociator updateTimersInIndex:]
+ +[MTIntentDonationWrapper donateCancelIntentWithTimer:]
+ +[MTIntentDonationWrapper donateCreateIntentWithAlarm:]
+ +[MTIntentDonationWrapper donateCreateIntentWithTimer:]
+ +[MTIntentDonationWrapper donateDeleteIntentWithAlarm:]
+ +[MTIntentDonationWrapper donateDismissIntentWithFiringAlarm:dismissedAlarm:]
+ +[MTIntentDonationWrapper donatePauseIntentWithRunningTimer:pausedTimer:]
+ +[MTIntentDonationWrapper donateResumeIntentWithPausedTimer:runningTimer:]
+ +[MTIntentDonationWrapper donateSnoozeIntentWithFiringAlarm:snoozedAlarm:]
+ +[MTIntentDonationWrapper donateUpdateIntentWithOldAlarm:newAlarm:]
+ +[MTIntentDonationWrapper donateUpdateIntentWithOldTimer:newTimer:]
+ <redacted>
+ _OBJC_CLASS_$_CSSearchableIndex
+ _OBJC_CLASS_$_CSSearchableItem
+ _OBJC_CLASS_$_MTAlarm
+ _OBJC_CLASS_$_MTAppEntityAssociator
+ _OBJC_CLASS_$_MTIntentDonationWrapper
+ _OBJC_CLASS_$_MTTimer
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$__TtC22ClockAppIntentsSupport19AppEntityAssociator
+ _OBJC_CLASS_$__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_MTAppEntityAssociator
+ _OBJC_METACLASS_$_MTIntentDonationWrapper
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__TtC22ClockAppIntentsSupport19AppEntityAssociator
+ _OBJC_METACLASS_$__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __CLASS_METHODS__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ __CLASS_PROPERTIES__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ __DATA__TtC22ClockAppIntentsSupport16MTSpotlightIndex
+ __DATA__TtC22ClockAppIntentsSupport19AppEntityAssociator
+ __DATA__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ __INSTANCE_METHODS__TtC22ClockAppIntentsSupport19AppEntityAssociator
+ __INSTANCE_METHODS__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ __IVARS__TtC22ClockAppIntentsSupport16MTSpotlightIndex
+ __METACLASS_DATA__TtC22ClockAppIntentsSupport16MTSpotlightIndex
+ __METACLASS_DATA__TtC22ClockAppIntentsSupport19AppEntityAssociator
+ __METACLASS_DATA__TtC22ClockAppIntentsSupport25IntentDonationCoordinator
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_MTAppEntityAssociator
+ __OBJC_$_CLASS_METHODS_MTIntentDonationWrapper
+ __OBJC_$_CLASS_METHODS__TtC22ClockAppIntentsSupport19AppEntityAssociator(ClockAppIntentsSupport)
+ __OBJC_CLASS_RO_$_MTAppEntityAssociator
+ __OBJC_CLASS_RO_$_MTIntentDonationWrapper
+ __OBJC_METACLASS_RO_$_MTAppEntityAssociator
+ __OBJC_METACLASS_RO_$_MTIntentDonationWrapper
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_allocate_value_buffer
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.100
+ ___swift_closure_destructor.101
+ ___swift_closure_destructor.103
+ ___swift_closure_destructor.105
+ ___swift_closure_destructor.107
+ ___swift_closure_destructor.110
+ ___swift_closure_destructor.112
+ ___swift_closure_destructor.114
+ ___swift_closure_destructor.115
+ ___swift_closure_destructor.118
+ ___swift_closure_destructor.119
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.122
+ ___swift_closure_destructor.123
+ ___swift_closure_destructor.127
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.130
+ ___swift_closure_destructor.133
+ ___swift_closure_destructor.138
+ ___swift_closure_destructor.143
+ ___swift_closure_destructor.145
+ ___swift_closure_destructor.148
+ ___swift_closure_destructor.149
+ ___swift_closure_destructor.153
+ ___swift_closure_destructor.158
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.162
+ ___swift_closure_destructor.163
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.168
+ ___swift_closure_destructor.171
+ ___swift_closure_destructor.173
+ ___swift_closure_destructor.175
+ ___swift_closure_destructor.178
+ ___swift_closure_destructor.180
+ ___swift_closure_destructor.183
+ ___swift_closure_destructor.184
+ ___swift_closure_destructor.188
+ ___swift_closure_destructor.19
+ ___swift_closure_destructor.193
+ ___swift_closure_destructor.197
+ ___swift_closure_destructor.198
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.201
+ ___swift_closure_destructor.203
+ ___swift_closure_destructor.206
+ ___swift_closure_destructor.208
+ ___swift_closure_destructor.21
+ ___swift_closure_destructor.210
+ ___swift_closure_destructor.213
+ ___swift_closure_destructor.214
+ ___swift_closure_destructor.218
+ ___swift_closure_destructor.219
+ ___swift_closure_destructor.223
+ ___swift_closure_destructor.227
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.232
+ ___swift_closure_destructor.236
+ ___swift_closure_destructor.241
+ ___swift_closure_destructor.245
+ ___swift_closure_destructor.249
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.252
+ ___swift_closure_destructor.252Tm
+ ___swift_closure_destructor.254
+ ___swift_closure_destructor.256
+ ___swift_closure_destructor.258
+ ___swift_closure_destructor.260
+ ___swift_closure_destructor.262
+ ___swift_closure_destructor.264
+ ___swift_closure_destructor.277
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.282
+ ___swift_closure_destructor.285
+ ___swift_closure_destructor.289
+ ___swift_closure_destructor.294
+ ___swift_closure_destructor.298
+ ___swift_closure_destructor.3
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.316
+ ___swift_closure_destructor.321
+ ___swift_closure_destructor.326
+ ___swift_closure_destructor.330
+ ___swift_closure_destructor.335
+ ___swift_closure_destructor.339
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.40
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.48
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.57
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.5Tm
+ ___swift_closure_destructor.61
+ ___swift_closure_destructor.65
+ ___swift_closure_destructor.66
+ ___swift_closure_destructor.66Tm
+ ___swift_closure_destructor.7
+ ___swift_closure_destructor.70
+ ___swift_closure_destructor.73
+ ___swift_closure_destructor.74
+ ___swift_closure_destructor.76
+ ___swift_closure_destructor.78
+ ___swift_closure_destructor.80
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.85
+ ___swift_closure_destructor.87
+ ___swift_closure_destructor.88
+ ___swift_closure_destructor.9
+ ___swift_closure_destructor.91
+ ___swift_closure_destructor.92
+ ___swift_closure_destructor.95
+ ___swift_closure_destructor.96
+ ___swift_closure_destructorTm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy1_1
+ ___swift_memcpy32_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _associated conformance 22ClockAppIntentsSupport10EntityTypeOSHAASQ
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0E5QueryV0bC00fG0AA0F0AfGP_AF0bF0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0E5QueryV0bC00fG0AaF22DynamicOptionsProvider
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0E5QueryV0bC00fG0AaF24PersistentlyIdentifiable
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0E5QueryV0bC022DynamicOptionsProviderAA12DefaultValueAfGP_AF07_IntentL0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0E5QueryV0bC022DynamicOptionsProviderAA6ResultAfGP_AF17ResultsCollection
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0E5QueryV0bC022DynamicOptionsProviderAaF09_SupportsB12Dependencies
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC007IndexedF0AaD0bF0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00B5ValueAaD07_IntentG0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00B5ValueAaD24PersistentlyIdentifiable
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00B5ValueAaD24TypeDisplayRepresentable
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00bF0AA12DefaultQueryAdEP_AD0fH0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00bF0AA2IDs12IdentifiableP_AD0F21IdentifierConvertible
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00bF0AAs12Identifiable
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00bF0AaD0B5Value
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC00bF0AaD20DisplayRepresentable
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC012_IntentValueAA0H4TypeAdEP_AdE
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC012_IntentValueAA13SpecificationAdEP_AD08ResolverI0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC012_IntentValueAA13UnwrappedTypeAdEP_AdE
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC020DisplayRepresentableAaD04TypegH0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC020DisplayRepresentableAaD08InstancegH0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV0bC028InstanceDisplayRepresentableAA10Foundation40CustomLocalizedStringResourceConvertible
+ _associated conformance 22ClockAppIntentsSupport10SongEntityV16CoreTransferable0H0AA14RepresentationAdEP_AD08TransferI0
+ _associated conformance 22ClockAppIntentsSupport10SongEntityVs12IdentifiableAA2IDsADP_SH
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV0bC00fG0AA0F0AfGP_AF0bF0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV0bC00fG0AaF22DynamicOptionsProvider
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV0bC00fG0AaF24PersistentlyIdentifiable
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV0bC022DynamicOptionsProviderAA12DefaultValueAfGP_AF07_IntentL0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV0bC022DynamicOptionsProviderAA6ResultAfGP_AF17ResultsCollection
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV0bC022DynamicOptionsProviderAaF09_SupportsB12Dependencies
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC007IndexedF0AaD0bF0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00B5ValueAaD07_IntentG0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00B5ValueAaD24PersistentlyIdentifiable
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00B5ValueAaD24TypeDisplayRepresentable
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00bF0AA12DefaultQueryAdEP_AD0fH0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00bF0AA2IDs12IdentifiableP_AD0F21IdentifierConvertible
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00bF0AAs12Identifiable
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00bF0AaD0B5Value
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC00bF0AaD20DisplayRepresentable
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC012_IntentValueAA0H4TypeAdEP_AdE
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC012_IntentValueAA13SpecificationAdEP_AD08ResolverI0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC012_IntentValueAA13UnwrappedTypeAdEP_AdE
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC020DisplayRepresentableAaD04TypegH0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC020DisplayRepresentableAaD08InstancegH0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV0bC028InstanceDisplayRepresentableAA10Foundation40CustomLocalizedStringResourceConvertible
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityV16CoreTransferable0H0AA14RepresentationAdEP_AD08TransferI0
+ _associated conformance 22ClockAppIntentsSupport14RingtoneEntityVs12IdentifiableAA2IDsADP_SH
+ _block_copy_helper
+ _block_copy_helper.245
+ _block_copy_helper.272
+ _block_copy_helper.278
+ _block_copy_helper.305
+ _block_copy_helper.310
+ _block_copy_helper.345
+ _block_copy_helper.348
+ _block_descriptor
+ _block_descriptor.247
+ _block_descriptor.274
+ _block_descriptor.280
+ _block_descriptor.307
+ _block_descriptor.312
+ _block_descriptor.347
+ _block_descriptor.350
+ _block_destroy_helper
+ _block_destroy_helper.246
+ _block_destroy_helper.273
+ _block_destroy_helper.279
+ _block_destroy_helper.306
+ _block_destroy_helper.311
+ _block_destroy_helper.346
+ _block_destroy_helper.349
+ _bzero
+ _get_witness_table 16CoreTransferable18DataRepresentationVy22ClockAppIntentsSupport10SongEntityVGAA08TransferD0HPyHC.1
+ _get_witness_table 16CoreTransferable18DataRepresentationVy22ClockAppIntentsSupport14RingtoneEntityVGAA08TransferD0HPyHC.1
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_alloc
+ _objc_allocWithZone
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend
+ _objc_msgSend$_initWithName:protectionClass:bundleIdentifier:options:
+ _objc_msgSend$addActiveTimersToIndexWithTimers:
+ _objc_msgSend$addToIndexWithAlarms:
+ _objc_msgSend$alarmDidStartFiringWithAlarm:
+ _objc_msgSend$alarmDidStopFiringWithAlarm:
+ _objc_msgSend$alarmIDString
+ _objc_msgSend$allowsSnooze
+ _objc_msgSend$beginIndexBatch
+ _objc_msgSend$criticalSearchableIndexWithName:bundleIdentifier:
+ _objc_msgSend$deleteAllSearchableItemsWithCompletionHandler:
+ _objc_msgSend$deleteFromIndexWithAlarms:
+ _objc_msgSend$deleteFromIndexWithTimers:
+ _objc_msgSend$deleteSearchableItemsWithIdentifiers:completionHandler:
+ _objc_msgSend$donateCancelIntentWithTimer:
+ _objc_msgSend$donateCreateIntentWithAlarm:
+ _objc_msgSend$donateCreateIntentWithTimer:
+ _objc_msgSend$donateDeleteIntentWithAlarm:
+ _objc_msgSend$donateDismissIntentWithFiringAlarm:dismissedAlarm:
+ _objc_msgSend$donatePauseIntentWithRunningTimer:pausedTimer:
+ _objc_msgSend$donateResumeIntentWithPausedTimer:runningTimer:
+ _objc_msgSend$donateSnoozeIntentWithFiringAlarm:snoozedAlarm:
+ _objc_msgSend$donateUpdateIntentWithOldAlarm:newAlarm:
+ _objc_msgSend$donateUpdateIntentWithOldTimer:newTimer:
+ _objc_msgSend$duration
+ _objc_msgSend$endIndexBatchWithClientState:completionHandler:
+ _objc_msgSend$hour
+ _objc_msgSend$indexSearchableItems:returningItemsSanitizedForSpotlightTo:
+ _objc_msgSend$init
+ _objc_msgSend$interruptAudio
+ _objc_msgSend$isActiveTimer:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isFiring
+ _objc_msgSend$minute
+ _objc_msgSend$reindexWithAlarms:timers:
+ _objc_msgSend$reindexWithTimers:
+ _objc_msgSend$repeatSchedule
+ _objc_msgSend$shared
+ _objc_msgSend$snoozeDuration
+ _objc_msgSend$sound
+ _objc_msgSend$timerDidStartCountdownWithTimer:
+ _objc_msgSend$timerDidStartFiringWithTimer:
+ _objc_msgSend$timerDidStopFiringWithTimer:
+ _objc_msgSend$timerIDString
+ _objc_msgSend$timerWasRemovedWithTimer:
+ _objc_msgSend$title
+ _objc_msgSend$updateIndexWithAlarms:
+ _objc_msgSend$updateIndexWithTimers:
+ _objc_msgSend$updateLiveEntitiesWithStopwatch:
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x10
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _os_log_type_enabled
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getOpaqueTypeConformance2
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x8
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic $s10AppIntents0A6EntityP
+ _symbolic $s10AppIntents11EntityQueryP
+ _symbolic $s10AppIntents12_IntentValueP
+ _symbolic $s10AppIntents22DynamicOptionsProviderP
+ _symbolic $s16CoreTransferable0B0P
+ _symbolic $ss12IdentifiableP
+ _symbolic BD
+ _symbolic SS
+ _symbolic SaySo16CSSearchableItemCG
+ _symbolic SaySo7MTAlarmCG
+ _symbolic SaySo7MTTimerCG
+ _symbolic Say_____G 22ClockAppIntentsSupport10SongEntityV
+ _symbolic Say_____G 22ClockAppIntentsSupport14RingtoneEntityV
+ _symbolic ScA_pSg
+ _symbolic ScGySi_So16CSSearchableItemCtG
+ _symbolic ScPSg
+ _symbolic SccySaySo16CSSearchableItemCG_______pt_____G s5ErrorP s5NeverO
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic Si
+ _symbolic Si_So16CSSearchableItemCt
+ _symbolic Si_So16CSSearchableItemCtIeAgHr_
+ _symbolic So11MTStopwatchC
+ _symbolic So17CSSearchableIndexC
+ _symbolic So7MTAlarmC
+ _symbolic So7MTTimerC
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 10AppIntents16EntityIdentifierV
+ _symbolic _____ 15AlarmAppIntents09AssistantA6EntityV
+ _symbolic _____ 15TimerAppIntents0A6EntityV
+ _symbolic _____ 22ClockAppIntentsSupport0B16EntityAssociatorC
+ _symbolic _____ 22ClockAppIntentsSupport10EntityTypeO
+ _symbolic _____ 22ClockAppIntentsSupport10SongEntityV
+ _symbolic _____ 22ClockAppIntentsSupport10SongEntityV0E5QueryV
+ _symbolic _____ 22ClockAppIntentsSupport14RingtoneEntityV
+ _symbolic _____ 22ClockAppIntentsSupport14RingtoneEntityV0E5QueryV
+ _symbolic _____ 22ClockAppIntentsSupport16MTSpotlightIndexC
+ _symbolic _____ 22ClockAppIntentsSupport25IntentDonationCoordinatorC
+ _symbolic _____ s12StaticStringV
+ _symbolic _____IeghHg_ 22ClockAppIntentsSupport16MTSpotlightIndexC
+ _symbolic _____Iegr_ 15AlarmAppIntents015AssistantCreateA6IntentV
+ _symbolic _____Iegr_ 15AlarmAppIntents015AssistantDeleteA6IntentV
+ _symbolic _____Iegr_ 15AlarmAppIntents06SnoozeA6IntentV
+ _symbolic _____Iegr_ 15AlarmAppIntents06UpdateA6IntentV
+ _symbolic _____Iegr_ 15AlarmAppIntents07DismissA6IntentV
+ _symbolic _____Iegr_ 15TimerAppIntents014AssistantPauseA6IntentV
+ _symbolic _____Iegr_ 15TimerAppIntents015AssistantCancelA6IntentV
+ _symbolic _____Iegr_ 15TimerAppIntents015AssistantCreateA6IntentV
+ _symbolic _____Iegr_ 15TimerAppIntents06UpdateA6IntentV
+ _symbolic _____Sg 10AppIntents16EntityIdentifierV
+ _symbolic _____Sg 10Foundation14DateComponentsV
+ _symbolic _____Sg 10Foundation8CalendarV
+ _symbolic _____Sg 10Foundation8CalendarV14RecurrenceRuleV
+ _symbolic _____Sg 10Foundation8TimeZoneV
+ _symbolic _____So16CSSearchableItemCIegHnr_ 15AlarmAppIntents09AssistantA6EntityV
+ _symbolic _____So16CSSearchableItemCIegHnr_ 15TimerAppIntents0A6EntityV
+ _symbolic _____XMT 22ClockAppIntentsSupport0B16EntityAssociatorC
+ _symbolic ______p s5ErrorP
+ _symbolic ______pIeghHzo_ s5ErrorP
+ _symbolic _____ySSG 10AppIntents14EntityPropertyC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySi_So16CSSearchableItemCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____A3BG 10AppIntents21IntentResultContainerV s5NeverO
+ _symbolic _____y_____A3BGIegr_ 10AppIntents21IntentResultContainerV s5NeverO
+ _symbolic _____y_____G 10AppIntents14EntityPropertyC AA10IntentFileV
+ _symbolic _____y_____G 10AppIntents26EmptyResolverSpecificationV 05ClockaB7Support10SongEntityV
+ _symbolic _____y_____G 10AppIntents26EmptyResolverSpecificationV 05ClockaB7Support14RingtoneEntityV
+ _symbolic _____y_____G 16CoreTransferable18DataRepresentationV 22ClockAppIntentsSupport10SongEntityV
+ _symbolic _____y_____G 16CoreTransferable18DataRepresentationV 22ClockAppIntentsSupport14RingtoneEntityV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation8CalendarV14RecurrenceRuleV7WeekdayO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation6LocaleV7WeekdayO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation8CalendarV14RecurrenceRuleV7WeekdayO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15AlarmAppIntents09AssistantD6EntityV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15TimerAppIntents0D6EntityV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y__________A2CG 10AppIntents21IntentResultContainerV 05AlarmaB009AssistantF6EntityV s5NeverO
+ _symbolic _____y__________A2CG 10AppIntents21IntentResultContainerV 05TimeraB00F6EntityV s5NeverO
+ _symbolic _____y__________A2CGIegr_ 10AppIntents21IntentResultContainerV 05AlarmaB009AssistantF6EntityV s5NeverO
+ _symbolic _____y__________A2CGIegr_ 10AppIntents21IntentResultContainerV 05TimeraB00F6EntityV s5NeverO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 10AppIntents0D6EntityP
+ _symbolic x
+ _symbolic ytIeAgHr_
+ _type_layout_string 22ClockAppIntentsSupport10SongEntityV
+ _type_layout_string 22ClockAppIntentsSupport14RingtoneEntityV
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_ClockAppIntentsSupport
CStrings:
+ "AssistantAlarmEntity/"
+ "ERROR in %s: %@"
+ "Failed to donate intent: %@"
+ "Unable to instantiate EntityIdentifier for alarm %s"
+ "Unable to instantiate EntityIdentifier for timer %s"
+ "alarmDidStartFiring(alarm:)"
+ "alarmDidStopFiring(alarm:)"
+ "com.apple.ClockAppIntentsSupport"
+ "timerDidStartCountdown(timer:)"
+ "timerDidStartFiring(timer:)"
+ "timerDidStopFiring(timer:)"
+ "timerWasRemoved(timer:)"
+ "updateLiveEntities(stopwatch:)"

```
