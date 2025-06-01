## MobileTimerSupport

> `/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport`

```diff

-2200.4.3.9.0
-  __TEXT.__text: 0x445e0
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_methlist: 0x55c
-  __TEXT.__const: 0x35d4
+2200.5.5.0.0
+  __TEXT.__text: 0x5f544
+  __TEXT.__auth_stubs: 0x1ab0
+  __TEXT.__objc_methlist: 0xa78
+  __TEXT.__const: 0x4218
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x19af
+  __TEXT.__cstring: 0x255f
   __TEXT.__dlopen_cstrs: 0x91
-  __TEXT.__oslogstring: 0x45e
-  __TEXT.__swift5_typeref: 0x192c
-  __TEXT.__swift5_reflstr: 0x736
-  __TEXT.__swift5_assocty: 0x528
-  __TEXT.__constg_swiftt: 0xf84
-  __TEXT.__swift5_fieldmd: 0x82c
-  __TEXT.__swift5_proto: 0x2d8
-  __TEXT.__swift5_types: 0xbc
-  __TEXT.__swift5_capture: 0x4d0
+  __TEXT.__oslogstring: 0x5c3
+  __TEXT.__swift5_typeref: 0x1d4c
+  __TEXT.__swift5_reflstr: 0xa56
+  __TEXT.__swift5_assocty: 0x540
+  __TEXT.__constg_swiftt: 0x15f4
+  __TEXT.__swift5_fieldmd: 0xb2c
+  __TEXT.__swift5_proto: 0x354
+  __TEXT.__swift5_types: 0xf4
+  __TEXT.__swift5_capture: 0xab0
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x1ab0
-  __TEXT.__eh_frame: 0x1480
-  __TEXT.__objc_classname: 0x8b
-  __TEXT.__objc_methname: 0xc57
-  __TEXT.__objc_methtype: 0x1de
-  __TEXT.__objc_stubs: 0x820
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x2e0
-  __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__unwind_info: 0x25e4
+  __TEXT.__eh_frame: 0x2760
+  __TEXT.__objc_classname: 0x1b8
+  __TEXT.__objc_methname: 0x183e
+  __TEXT.__objc_methtype: 0x606
+  __TEXT.__objc_stubs: 0x1080
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x928
-  __DATA_CONST.__objc_selrefs: 0x430
-  __AUTH_CONST.__objc_const: 0x288
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__const: 0x3740
-  __AUTH_CONST.__auth_got: 0xc48
-  __AUTH.__objc_data: 0x200
-  __AUTH.__data: 0x140
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0x80
-  __DATA.__data: 0x1000
-  __DATA.__bss: 0x4f48
-  __DATA.__common: 0x50
-  __DATA_DIRTY.__objc_data: 0x7c0
-  __DATA_DIRTY.__data: 0x578
+  __DATA_CONST.__objc_const: 0x2658
+  __DATA_CONST.__objc_selrefs: 0x780
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__objc_const: 0x508
+  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__const: 0x4ac0
+  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH.__objc_data: 0x888
+  __AUTH.__data: 0x608
+  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_data: 0x20
+  __DATA.__data: 0x1a30
+  __DATA.__bss: 0x5e48
+  __DATA.__common: 0x60
+  __DATA_DIRTY.__objc_data: 0x7a0
+  __DATA_DIRTY.__data: 0x5a0
   __DATA_DIRTY.__bss: 0xc90
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 35A118EB-A842-38C0-A2DE-4EFC7F94B47F
-  Functions: 2066
-  Symbols:   1279
-  CStrings:  388
+  UUID: 0C4AD72C-4A27-3B85-B1BB-33EB13102D8E
+  Functions: 2985
+  Symbols:   1800
+  CStrings:  697
 
Symbols:
+ +[MTStopwatchUtilities _timeAdjustedFor30fpsDisplay:]
+ +[MTStopwatchUtilities decodeStopwatchesFromDictionary:]
+ +[MTStopwatchUtilities encodedDictionaryForStopwatches:]
+ +[MockDateProvider mockDate]
+ -[DefaultDateProvider date]
+ -[DefaultDateProvider updateDate:]
+ -[MTLegacyStopwatchMigrator .cxx_destruct]
+ -[MTLegacyStopwatchMigrator currentInterval]
+ -[MTLegacyStopwatchMigrator defaults]
+ -[MTLegacyStopwatchMigrator eraseLocalDefaults]
+ -[MTLegacyStopwatchMigrator generateStopwatchFromDefaults]
+ -[MTLegacyStopwatchMigrator initWithDefaults:manager:]
+ -[MTLegacyStopwatchMigrator isTimerRunning]
+ -[MTLegacyStopwatchMigrator loadInitialState]
+ -[MTLegacyStopwatchMigrator manager]
+ -[MTLegacyStopwatchMigrator migrateLegacyStopwatch]
+ -[MTLegacyStopwatchMigrator needsMigration]
+ -[MTLegacyStopwatchMigrator setCurrentInterval:]
+ -[MTLegacyStopwatchMigrator setDefaults:]
+ -[MTLegacyStopwatchMigrator setIsTimerRunning:]
+ -[MTLegacyStopwatchMigrator setManager:]
+ -[MTStopwatchStorage .cxx_destruct]
+ -[MTStopwatchStorage createStopWatch:withCompletion:source:]
+ -[MTStopwatchStorage deleteStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didAddLap:forStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didClearAllLapsForStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didLapLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didPauseLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didResetLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didResumeLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage didStartLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchStorage getStopwatchesWitchCompletion:]
+ -[MTStopwatchStorage init]
+ -[MTStopwatchStorage localSetup]
+ -[MTStopwatchStorage registerObserver:]
+ -[MTStopwatchStorage setStorageProxy:]
+ -[MTStopwatchStorage setSystemReady]
+ -[MTStopwatchStorage storageProxy]
+ -[MTStopwatchStorage unregisterObserver:]
+ -[MTStopwatchStorage updateStopwatch:withCompletion:source:]
+ -[MTStopwatchViewModel .cxx_destruct]
+ -[MTStopwatchViewModel addLap:]
+ -[MTStopwatchViewModel clearAllLaps]
+ -[MTStopwatchViewModel getStopwatch]
+ -[MTStopwatchViewModel initWithStopwatch:manager:delegate:dateProvider:registerForNotifications:broadcastUpdates:]
+ -[MTStopwatchViewModel invalidateDisplayLink]
+ -[MTStopwatchViewModel lapLapTimer]
+ -[MTStopwatchViewModel pauseLapTimer]
+ -[MTStopwatchViewModel resetLapTimer]
+ -[MTStopwatchViewModel resumeLapTimer]
+ -[MTStopwatchViewModel runningTotalForLap:]
+ -[MTStopwatchViewModel setViewModel:]
+ -[MTStopwatchViewModel sourceIdentifier]
+ -[MTStopwatchViewModel startLapTimer]
+ -[MTStopwatchViewModel updateStopwatch:]
+ -[MTStopwatchViewModel updateTime]
+ -[MTStopwatchViewModel updateWithDisplayLink]
+ -[MTStopwatchViewModel viewModel]
+ -[MockDateProvider .cxx_destruct]
+ -[MockDateProvider date]
+ -[MockDateProvider overrideDate]
+ -[MockDateProvider setOverrideDate:]
+ -[MockDateProvider updateDate:]
+ _MTStopwatchManagerDidClearAllLaps
+ _MTStopwatchManagerDidLapLapTimer
+ _MTStopwatchManagerDidPauseLapTimer
+ _MTStopwatchManagerDidResetLapTimer
+ _MTStopwatchManagerDidResumeLapTimer
+ _MTStopwatchManagerDidStartLapTimer
+ _MTStopwatchManagerLapAdded
+ _MTStopwatchManagerModifiedItemKey
+ _MTStopwatchManagerStopwatchKey
+ _MTStopwatchManagerStopwatchUpdated
+ _MTStopwatchSourceIdentifierKey
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_DefaultDateProvider
+ _OBJC_CLASS_$_MTLegacyStopwatchMigrator
+ _OBJC_CLASS_$_MTMutableStopwatch
+ _OBJC_CLASS_$_MTStopwatch
+ _OBJC_CLASS_$_MTStopwatchManager
+ _OBJC_CLASS_$_MTStopwatchStorage
+ _OBJC_CLASS_$_MTStopwatchUtilities
+ _OBJC_CLASS_$_MTStopwatchViewModel
+ _OBJC_CLASS_$_MTStorageReader
+ _OBJC_CLASS_$_MTStorageWriter
+ _OBJC_CLASS_$_MockDateProvider
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$__TtC18MobileTimerSupport18StopwatchViewModel
+ _OBJC_CLASS_$__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ _OBJC_IVAR_$_MTLegacyStopwatchMigrator._currentInterval
+ _OBJC_IVAR_$_MTLegacyStopwatchMigrator._defaults
+ _OBJC_IVAR_$_MTLegacyStopwatchMigrator._isTimerRunning
+ _OBJC_IVAR_$_MTLegacyStopwatchMigrator._manager
+ _OBJC_IVAR_$_MTStopwatchStorage._storageProxy
+ _OBJC_IVAR_$_MTStopwatchViewModel._viewModel
+ _OBJC_IVAR_$_MockDateProvider._overrideDate
+ _OBJC_METACLASS_$_DefaultDateProvider
+ _OBJC_METACLASS_$_MTLegacyStopwatchMigrator
+ _OBJC_METACLASS_$_MTStopwatchStorage
+ _OBJC_METACLASS_$_MTStopwatchUtilities
+ _OBJC_METACLASS_$_MTStopwatchViewModel
+ _OBJC_METACLASS_$_MockDateProvider
+ _OBJC_METACLASS_$__TtC18MobileTimerSupport18StopwatchViewModel
+ _OBJC_METACLASS_$__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ __CATEGORY__TtC18MobileTimerSupport18StopwatchViewModel_$_MobileTimerSupport
+ __DATA__TtC18MobileTimerSupport11SyncManager
+ __DATA__TtC18MobileTimerSupport18StopwatchViewModel
+ __DATA__TtC18MobileTimerSupport21StopwatchStorageActor
+ __DATA__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ __DATA__TtC18MobileTimerSupport25StopwatchSessionsProvider
+ __DATA__TtC18MobileTimerSupport26DefaultsStopwatchDataStore
+ __DATA__TtC18MobileTimerSupport27StopwatchActivityAttributes
+ __IVARS__TtC18MobileTimerSupport11SyncManager
+ __IVARS__TtC18MobileTimerSupport13ObserverStore
+ __IVARS__TtC18MobileTimerSupport18StopwatchViewModel
+ __IVARS__TtC18MobileTimerSupport21StopwatchStorageActor
+ __IVARS__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ __IVARS__TtC18MobileTimerSupport25StopwatchSessionsProvider
+ __IVARS__TtC18MobileTimerSupport26DefaultsStopwatchDataStore
+ __IVARS__TtC18MobileTimerSupport27StopwatchActivityAttributes
+ __METACLASS_DATA__TtC18MobileTimerSupport11SyncManager
+ __METACLASS_DATA__TtC18MobileTimerSupport18StopwatchViewModel
+ __METACLASS_DATA__TtC18MobileTimerSupport21StopwatchStorageActor
+ __METACLASS_DATA__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ __METACLASS_DATA__TtC18MobileTimerSupport25StopwatchSessionsProvider
+ __METACLASS_DATA__TtC18MobileTimerSupport26DefaultsStopwatchDataStore
+ __METACLASS_DATA__TtC18MobileTimerSupport27StopwatchActivityAttributes
+ __OBJC_$_CLASS_METHODS_MTStopwatchUtilities
+ __OBJC_$_CLASS_METHODS_MockDateProvider
+ __OBJC_$_INSTANCE_METHODS_DefaultDateProvider
+ __OBJC_$_INSTANCE_METHODS_MTLegacyStopwatchMigrator
+ __OBJC_$_INSTANCE_METHODS_MTStopwatchStorage
+ __OBJC_$_INSTANCE_METHODS_MTStopwatchViewModel
+ __OBJC_$_INSTANCE_METHODS_MockDateProvider
+ __OBJC_$_INSTANCE_METHODS__TtC18MobileTimerSupport18StopwatchViewModel
+ __OBJC_$_INSTANCE_METHODS__TtC18MobileTimerSupport18StopwatchViewModel(MobileTimerSupport)
+ __OBJC_$_INSTANCE_METHODS__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ __OBJC_$_INSTANCE_METHODS__TtC18MobileTimerSupport25StopwatchSessionsProvider(MobileTimerSupport)
+ __OBJC_$_INSTANCE_VARIABLES_MTLegacyStopwatchMigrator
+ __OBJC_$_INSTANCE_VARIABLES_MTStopwatchStorage
+ __OBJC_$_INSTANCE_VARIABLES_MTStopwatchViewModel
+ __OBJC_$_INSTANCE_VARIABLES_MockDateProvider
+ __OBJC_$_PROP_LIST_MTLegacyStopwatchMigrator
+ __OBJC_$_PROP_LIST_MTStopwatchStorage
+ __OBJC_$_PROP_LIST_MTStopwatchViewModel
+ __OBJC_$_PROP_LIST_MockDateProvider
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchStorageProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchStoreObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchViewModelProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StopwatchDateProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StopwatchViewModelDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchStorageProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchStoreObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchViewModelProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StopwatchDateProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StopwatchViewModelDelegate
+ __OBJC_$_PROTOCOL_REFS_MTSource
+ __OBJC_CLASS_PROTOCOLS_$_DefaultDateProvider
+ __OBJC_CLASS_PROTOCOLS_$_MTStopwatchStorage
+ __OBJC_CLASS_PROTOCOLS_$_MTStopwatchViewModel
+ __OBJC_CLASS_PROTOCOLS_$_MockDateProvider
+ __OBJC_CLASS_PROTOCOLS_$__TtC18MobileTimerSupport18StopwatchViewModel(MobileTimerSupport)
+ __OBJC_CLASS_PROTOCOLS_$__TtC18MobileTimerSupport25StopwatchSessionsProvider(MobileTimerSupport)
+ __OBJC_CLASS_RO_$_DefaultDateProvider
+ __OBJC_CLASS_RO_$_MTLegacyStopwatchMigrator
+ __OBJC_CLASS_RO_$_MTStopwatchStorage
+ __OBJC_CLASS_RO_$_MTStopwatchUtilities
+ __OBJC_CLASS_RO_$_MTStopwatchViewModel
+ __OBJC_CLASS_RO_$_MockDateProvider
+ __OBJC_LABEL_PROTOCOL_$_MTSource
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchStorageProtocol
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchStoreObserver
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchViewModelProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_StopwatchDateProvider
+ __OBJC_LABEL_PROTOCOL_$_StopwatchViewModelDelegate
+ __OBJC_METACLASS_RO_$_DefaultDateProvider
+ __OBJC_METACLASS_RO_$_MTLegacyStopwatchMigrator
+ __OBJC_METACLASS_RO_$_MTStopwatchStorage
+ __OBJC_METACLASS_RO_$_MTStopwatchUtilities
+ __OBJC_METACLASS_RO_$_MTStopwatchViewModel
+ __OBJC_METACLASS_RO_$_MockDateProvider
+ __OBJC_PROTOCOL_$_MTSource
+ __OBJC_PROTOCOL_$_MTStopwatchManagerProtocol
+ __OBJC_PROTOCOL_$_MTStopwatchStorageProtocol
+ __OBJC_PROTOCOL_$_MTStopwatchStoreObserver
+ __OBJC_PROTOCOL_$_MTStopwatchViewModelProtocol
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_StopwatchDateProvider
+ __OBJC_PROTOCOL_$_StopwatchViewModelDelegate
+ __PROTOCOLS__TtC18MobileTimerSupport18StopwatchViewModel
+ __PROTOCOLS__TtC18MobileTimerSupport18StopwatchViewModel.111
+ __PROTOCOLS__TtC18MobileTimerSupport23MTStopwatchStorageProxy
+ __PROTOCOLS__TtC18MobileTimerSupport23MTStopwatchStorageProxy.136
+ ___51-[MTLegacyStopwatchMigrator migrateLegacyStopwatch]_block_invoke
+ ___51-[MTLegacyStopwatchMigrator migrateLegacyStopwatch]_block_invoke.16
+ ___NSArray0__struct
+ ___block_descriptor_48_e8_32s40s_e26_"NAFuture"16?0"NSNull"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e27_"NAFuture"16?0"NSArray"8ls32l8s40l8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___unnamed_1
+ __timeAdjustedFor30fpsDisplay:.leastSignificantDigits
+ _arc4random_uniform
+ _associated conformance 18MobileTimerSupport16StopwatchContextV10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLOSHAASQ
+ _associated conformance 18MobileTimerSupport16StopwatchContextV10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 18MobileTimerSupport16StopwatchContextV10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 18MobileTimerSupport16StopwatchContextVSHAASQ
+ _associated conformance 18MobileTimerSupport21StopwatchSessionErrorOSHAASQ
+ _associated conformance 18MobileTimerSupport21StopwatchStorageActorC0eF5ErrorOSHAASQ
+ _associated conformance 18MobileTimerSupport26DefaultsStopwatchDataStoreC0D5ErrorOSHAASQ
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC0E3Kit0eF0AA12ContentStateAdEP_SE
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC0E3Kit0eF0AA12ContentStateAdEP_SH
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC0E3Kit0eF0AA12ContentStateAdEP_Se
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC0E3Kit0eF0AASE
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC0E3Kit0eF0AASe
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLOSHAASQ
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 18MobileTimerSupport27StopwatchActivityAttributesC10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper.1
+ _block_copy_helper.10
+ _block_copy_helper.12
+ _block_copy_helper.13
+ _block_copy_helper.192
+ _block_copy_helper.235
+ _block_copy_helper.263
+ _block_copy_helper.292
+ _block_copy_helper.303
+ _block_copy_helper.313
+ _block_copy_helper.325
+ _block_copy_helper.4
+ _block_copy_helper.5
+ _block_copy_helper.7
+ _block_descriptor.14
+ _block_descriptor.15
+ _block_descriptor.194
+ _block_descriptor.237
+ _block_descriptor.265
+ _block_descriptor.294
+ _block_descriptor.3
+ _block_descriptor.305
+ _block_descriptor.315
+ _block_descriptor.327
+ _block_descriptor.6
+ _block_descriptor.7
+ _block_descriptor.9
+ _block_destroy_helper.11
+ _block_destroy_helper.13
+ _block_destroy_helper.14
+ _block_destroy_helper.193
+ _block_destroy_helper.2
+ _block_destroy_helper.236
+ _block_destroy_helper.264
+ _block_destroy_helper.293
+ _block_destroy_helper.304
+ _block_destroy_helper.314
+ _block_destroy_helper.326
+ _block_destroy_helper.5
+ _block_destroy_helper.6
+ _block_destroy_helper.8
+ _kMTAStopwatchIndexKey
+ _kMTAStopwatchLapsKey
+ _kMTAStopwatchLastTimeKey
+ _kMTAStopwatchOffsetKey
+ _kMTAStopwatchStartTimeKey
+ _kMTAStopwatchTimerRunningKey
+ _kMTStopwatches
+ _objc_enumerationMutation
+ _objc_msgSend$addLap:
+ _objc_msgSend$addObject:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$clearAllLaps
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createStopWatch:withCompletion:source:
+ _objc_msgSend$createStopwatch:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentInterval
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$defaults
+ _objc_msgSend$deleteStopwatch:withCompletion:source:
+ _objc_msgSend$didAddLap:forStopwatch:withCompletion:source:
+ _objc_msgSend$didClearAllLapsForStopwatch:withCompletion:source:
+ _objc_msgSend$didLapLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didPauseLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didResetLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didResumeLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didStartLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$encodedDictionary
+ _objc_msgSend$firstObject
+ _objc_msgSend$flatMap:
+ _objc_msgSend$generateStopwatchFromDefaults
+ _objc_msgSend$getStopwatch
+ _objc_msgSend$getStopwatches
+ _objc_msgSend$getStopwatchesWitchCompletion:
+ _objc_msgSend$initWithEncodedDictionary:
+ _objc_msgSend$initWithStopwatch:manager:delegate:dateProvider:registerForNotifications:broadcastUpdates:
+ _objc_msgSend$invalidateDisplayLink
+ _objc_msgSend$isTimerRunning
+ _objc_msgSend$lapLapTimer
+ _objc_msgSend$loadInitialState
+ _objc_msgSend$mockDate
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$now
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$overrideDate
+ _objc_msgSend$pauseLapTimer
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeStopwatch:
+ _objc_msgSend$resetLapTimer
+ _objc_msgSend$resumeLapTimer
+ _objc_msgSend$runningTotalForLap:
+ _objc_msgSend$setCurrentInterval:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setDefaults:
+ _objc_msgSend$setIsTimerRunning:
+ _objc_msgSend$setLaps:
+ _objc_msgSend$setMonth:
+ _objc_msgSend$setOffset:
+ _objc_msgSend$setOverrideDate:
+ _objc_msgSend$setPreviousLapsTotalInterval:
+ _objc_msgSend$setStartDate:
+ _objc_msgSend$setState:
+ _objc_msgSend$setStorageProxy:
+ _objc_msgSend$setSystemReady
+ _objc_msgSend$setViewModel:
+ _objc_msgSend$setYear:
+ _objc_msgSend$sourceIdentifier
+ _objc_msgSend$startLapTimer
+ _objc_msgSend$storageProxy
+ _objc_msgSend$unregisterObserver:
+ _objc_msgSend$updateStopwatch:
+ _objc_msgSend$updateStopwatch:withCompletion:source:
+ _objc_msgSend$updateTime
+ _objc_msgSend$updateWithDisplayLink
+ _objc_msgSend$viewModel
+ _objc_opt_isKindOfClass
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x5
+ _objectdestroy.24Tm
+ _objectdestroy.297Tm
+ _objectdestroy.43Tm
+ _objectdestroy.7Tm
+ _objectdestroy.97Tm
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _swift_makeBoxUnique
+ _swift_release_n
+ _swift_unknownObjectRetain_n
+ _symbolic $s18MobileTimerSupport18StopwatchDataStoreP
+ _symbolic BD
+ _symbolic SDySSSo11MTStopwatchCG
+ _symbolic SDySS_____y_____GG 11ActivityKit0A0C 18MobileTimerSupport09StopwatchA10AttributesC
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic SaySo11MTStopwatchCG
+ _symbolic SaySo11MTStopwatchCGSg______pSgIeggg_Sg s5ErrorP
+ _symbolic SaySo8NSNumberCGSg
+ _symbolic ScCySaySo11MTStopwatchCG______pG s5ErrorP
+ _symbolic Sf
+ _symbolic So11MTStopwatchC
+ _symbolic So11MTStopwatchCSg
+ _symbolic So11NSHashTableCyyXlG
+ _symbolic So13CADisplayLinkCSg
+ _symbolic So14NSUserDefaultsC
+ _symbolic So18MTMutableStopwatchC
+ _symbolic So18MTStopwatchManagerC
+ _symbolic So21StopwatchDateProvider_p
+ _symbolic So24MTStopwatchStoreObserver_p
+ _symbolic So26MTStopwatchManagerProtocol_p
+ _symbolic So26StopwatchViewModelDelegate_pSgXw
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
+ _symbolic So8MTSource_p
+ _symbolic So8MTSource_pSg
+ _symbolic So8NSNumberC
+ _symbolic _____ 18MobileTimerSupport11SyncManagerC
+ _symbolic _____ 18MobileTimerSupport13ObserverStoreC
+ _symbolic _____ 18MobileTimerSupport16StopwatchContextV
+ _symbolic _____ 18MobileTimerSupport16StopwatchContextV10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLO
+ _symbolic _____ 18MobileTimerSupport18StopwatchViewModelC
+ _symbolic _____ 18MobileTimerSupport21StopwatchSessionErrorO
+ _symbolic _____ 18MobileTimerSupport21StopwatchStorageActorC
+ _symbolic _____ 18MobileTimerSupport21StopwatchStorageActorC0eF5ErrorO
+ _symbolic _____ 18MobileTimerSupport23MTStopwatchStorageProxyC
+ _symbolic _____ 18MobileTimerSupport25StopwatchSessionsProviderC
+ _symbolic _____ 18MobileTimerSupport26DefaultsStopwatchDataStoreC
+ _symbolic _____ 18MobileTimerSupport26DefaultsStopwatchDataStoreC0D5ErrorO
+ _symbolic _____ 18MobileTimerSupport27StopwatchActivityAttributesC
+ _symbolic _____ 18MobileTimerSupport27StopwatchActivityAttributesC10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLO
+ _symbolic _____SgXw 18MobileTimerSupport18StopwatchViewModelC
+ _symbolic ______p 18MobileTimerSupport18StopwatchDataStoreP
+ _symbolic ______pSg 7Combine11CancellableP
+ _symbolic ______pSgIegg_ s5ErrorP
+ _symbolic ______pSgIegg_Sg s5ErrorP
+ _symbolic _____ySSSo11MTStopwatchCG s18_DictionaryStorageC
+ _symbolic _____ySS_____y_____GG s18_DictionaryStorageC 11ActivityKit0C0C 18MobileTimerSupport09StopwatchC10AttributesC
+ _symbolic _____ySay_____GG s23_ContiguousArrayStorageC 10AppIntents0D8ShortcutV
+ _symbolic _____ySo24MTStopwatchStoreObserver_pG 18MobileTimerSupport13ObserverStoreC
+ _symbolic _____y_____G 11ActivityKit0A0C 18MobileTimerSupport09StopwatchA10AttributesC
+ _symbolic _____y_____G 11ActivityKit0A7ContentV 18MobileTimerSupport16StopwatchContextV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18MobileTimerSupport16StopwatchContextV10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18MobileTimerSupport27StopwatchActivityAttributesC10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18MobileTimerSupport16StopwatchContextV10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18MobileTimerSupport27StopwatchActivityAttributesC10CodingKeys33_3C7AB23F72EF4EBE0D82D1E3F09C518FLLO
+ _symbolic _____y______G 7Combine10PublishersO6FilterV So20NSNotificationCenterC10FoundationE9PublisherV
+ _symbolic ytSg
+ _symbolic ytSgIeghHr_
- -[MTAppIntentsProvider didLapStopwatchWithManager:]
- -[MTAppIntentsProvider didResetStopwatchWithManager:]
- -[MTAppIntentsProvider didStartStopwatchWithManager:]
- -[MTAppIntentsProvider didStopStopwatchWithManager:]
- _block_copy_helper.241
- _block_copy_helper.269
- _block_copy_helper.298
- _block_copy_helper.309
- _block_copy_helper.319
- _block_copy_helper.331
- _block_descriptor.243
- _block_descriptor.271
- _block_descriptor.300
- _block_descriptor.311
- _block_descriptor.321
- _block_descriptor.333
- _block_destroy_helper.242
- _block_destroy_helper.270
- _block_destroy_helper.299
- _block_destroy_helper.310
- _block_destroy_helper.320
- _block_destroy_helper.332
- _objc_msgSend$didLapStopwatchWithProvider:
- _objc_msgSend$didResetStopwatchWithProvider:
- _objc_msgSend$didStartStopwatchWithProvider:
- _objc_msgSend$didStopStopwatchWithProvider:
- _objectdestroy.303Tm
- _swift_setDeallocating
- _symbolic _____y_____G s23_ContiguousArrayStorageC 10AppIntents0D8ShortcutV
CStrings:
+ "\x12"
+ " adding stopwatch lap: "
+ " because it wasn't paused"
+ " because it's already paused"
+ " because it's already running"
+ " because it's already stopped"
+ " because it's not running"
+ " because startDate is nil, aborting"
+ " for stopwatch id: "
+ " for stopwatch with id: "
+ " gettings stopwatch: "
+ " initialized view mode, stopwatch is: "
+ " lapLapTimer called"
+ " lapLapTimer error for stopwatch: "
+ " pauseLapTimer error for stopwatch: "
+ " registerUpdateNotifications called"
+ " registered for clear all laps notification"
+ " resetLapTimer error for stopwatch: "
+ " resumeLapTimer error for stopwatch: "
+ " startLapTimer error for stopwatch: "
+ "#16@0:8"
+ "$defaultActor"
+ "%{public}@ created stopwatch from previous defaults, proceeding to delete default one"
+ "%{public}@ decoding defaults could not generate dictionary"
+ "%{public}@ erasing local defaults"
+ "%{public}@ generated stopwatch from previous defaults: %{public}@"
+ "%{public}@ initialized"
+ "%{public}@ migrating legacy stopwatch"
+ "%{public}@ retrieved default stopwatch: %{public}@"
+ ", broadcast updates: "
+ ", internal stopwatch is: "
+ ", registerUpdateNotifications: "
+ ", stopwatch laps now: "
+ "@\"<MTStopwatchManagerProtocol>\""
+ "@\"NAFuture\"16@0:8"
+ "@\"NAFuture\"16@?0@\"NSArray\"8"
+ "@\"NAFuture\"16@?0@\"NSNull\"8"
+ "@\"NAFuture\"24@0:8@\"MTStopwatch\"16"
+ "@\"NAFuture\"32@0:8@\"MTStopwatch\"16@\"<MTSource>\"24"
+ "@\"NAFuture\"40@0:8@\"NSNumber\"16@\"MTStopwatch\"24@\"<MTSource>\"32"
+ "@\"NSDate\""
+ "@\"NSDate\"16@0:8"
+ "@\"NSString\"16@0:8"
+ "@\"NSUserDefaults\""
+ "@\"_TtC18MobileTimerSupport18StopwatchViewModel\""
+ "@\"_TtC18MobileTimerSupport23MTStopwatchStorageProxy\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24@32"
+ "@56@0:8@\"MTMutableStopwatch\"16@\"<MTStopwatchManagerProtocol>\"24@\"<StopwatchViewModelDelegate>\"32@\"<StopwatchDateProvider>\"40B48B52"
+ "@56@0:8@16@24@32@40B48B52"
+ "ALARM_DEFAULT_TITLE"
+ "AppIntents_Dictionary"
+ "B"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "Can't construct Array with count < 0"
+ "Could not find your alarm."
+ "Creating session for stopwatch id: "
+ "DefaultDateProvider"
+ "Division by zero"
+ "Division results in an overflow"
+ "Error finishing session: "
+ "Fatal error"
+ "LAPS"
+ "LASTTIME"
+ "MTLegacyStopwatchMigrator"
+ "MTSource"
+ "MTStopwatchManagerProtocol"
+ "MTStopwatchStorage"
+ "MTStopwatchStorageProtocol"
+ "MTStopwatchStoreObserver"
+ "MTStopwatchUtilities"
+ "MTStopwatchViewModel"
+ "MTStopwatchViewModelProtocol"
+ "MTStopwatches"
+ "MobileTimerSupport.StopwatchViewModel"
+ "MockDateProvider"
+ "NSObject"
+ "OFFSET"
+ "STARTTIME"
+ "STOPWATCH_INDEX"
+ "Session already exists for stopwatch id: "
+ "StopwatchDateProvider"
+ "StopwatchStorageVersion"
+ "StopwatchViewModelDelegate"
+ "Swift/Array.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/UnsafePointer.swift"
+ "T#,R"
+ "T@\"<MTStopwatchManagerProtocol>\",&,N,V_manager"
+ "T@\"MTStopwatch\",R,N,GgetStopwatch"
+ "T@\"NSDate\",&,N,V_overrideDate"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSUserDefaults\",&,N,V_defaults"
+ "T@\"_TtC18MobileTimerSupport18StopwatchViewModel\",&,N,V_viewModel"
+ "T@\"_TtC18MobileTimerSupport23MTStopwatchStorageProxy\",&,N,V_storageProxy"
+ "TB,N,V_isTimerRunning"
+ "TIMERRUNNING"
+ "TQ,R"
+ "Td,N,V_currentInterval"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_TtC18MobileTimerSupport11SyncManager"
+ "_TtC18MobileTimerSupport18StopwatchViewModel"
+ "_TtC18MobileTimerSupport21StopwatchStorageActor"
+ "_TtC18MobileTimerSupport23MTStopwatchStorageProxy"
+ "_TtC18MobileTimerSupport25StopwatchSessionsProvider"
+ "_TtC18MobileTimerSupport26DefaultsStopwatchDataStore"
+ "_TtC18MobileTimerSupport27StopwatchActivityAttributes"
+ "_currentInterval"
+ "_defaults"
+ "_isTimerRunning"
+ "_overrideDate"
+ "_storageProxy"
+ "_timeAdjustedFor30fpsDisplay:"
+ "_viewModel"
+ "accessQueue"
+ "actor: getting stopwatches"
+ "actor: returning stopwatches "
+ "addLap:"
+ "addObject:"
+ "addToRunLoop:forMode:"
+ "added default stopwatch, now "
+ "allObjects"
+ "autorelease"
+ "boolForKey:"
+ "broadcastUpdates"
+ "class"
+ "clearAllLaps"
+ "clearAllLapsCancellable"
+ "com.apple.mobiletimer.StopwatchViewModelAccess"
+ "conformsToProtocol:"
+ "context"
+ "copy"
+ "countByEnumeratingWithState:objects:count:"
+ "createStopWatch:withCompletion:source:"
+ "createStopwatch:"
+ "currentCalendar"
+ "currentInterval"
+ "currentRunLoop"
+ "currentVersion"
+ "d"
+ "d16@0:8"
+ "d24@0:8d16"
+ "d24@0:8q16"
+ "dataStore"
+ "dateFromComponents:"
+ "dateProvider"
+ "debugDescription"
+ "decodeObjectForKey:"
+ "decodeStopwatchesFromDictionary:"
+ "default alarm title"
+ "defaultCenter"
+ "defaults"
+ "defauts"
+ "deleteStopwatch:withCompletion:source:"
+ "didAddLap:"
+ "didAddLap:forStopwatch:sender:"
+ "didAddLap:forStopwatch:source:"
+ "didAddLap:forStopwatch:withCompletion:source:"
+ "didClearAllLaps"
+ "didClearAllLapsForStopwatch:sender:"
+ "didClearAllLapsForStopwatch:withCompletion:source:"
+ "didCreateStopWatch:source:"
+ "didDeleteStopwatch:source:"
+ "didLapLapTimer"
+ "didLapLapTimerForStopwatch:sender:"
+ "didLapLapTimerForStopwatch:withCompletion:source:"
+ "didPauseLapTimer"
+ "didPauseLapTimerForStopwatch:sender:"
+ "didPauseLapTimerForStopwatch:withCompletion:source:"
+ "didPauseStopwatch"
+ "didResetLapTimer"
+ "didResetLapTimerForStopwatch:sender:"
+ "didResetLapTimerForStopwatch:withCompletion:source:"
+ "didResumeLapTimer"
+ "didResumeLapTimerForStopwatch:sender:"
+ "didResumeLapTimerForStopwatch:withCompletion:source:"
+ "didStartLapTimer"
+ "didStartLapTimerForStopwatch:sender:"
+ "didStartLapTimerForStopwatch:withCompletion:source:"
+ "didUpdateCurrentInterval:adjustedCurrentInterval:totalInterval:adjustedTotalInterval:isStopwatchRunning:"
+ "didUpdateStopwatch:source:"
+ "displayLink"
+ "displayLinkWithTarget:selector:"
+ "donatesIntent"
+ "dontNotify"
+ "doubleValue"
+ "encodeObject:forKey:"
+ "encodedDictionary"
+ "encodedDictionaryForStopwatches:"
+ "eraseLocalDefaults"
+ "error restoring stopwatches "
+ "finishing session for stopwatch id: "
+ "firstObject"
+ "flatMap:"
+ "floatForKey:"
+ "generateStopwatchFromDefaults"
+ "getStopwatch"
+ "getStopwatches"
+ "getStopwatches()"
+ "getStopwatchesWitchCompletion:"
+ "hash"
+ "identifier"
+ "initWithDefaults:manager:"
+ "initWithEncodedDictionary:"
+ "initWithStopwatch:manager:delegate:dateProvider:registerForNotifications:broadcastUpdates:"
+ "initializing StopwatchStorageActor"
+ "internalStopwatch"
+ "invalidate"
+ "invalidateDisplayLink"
+ "isEqual:"
+ "isFromOtherDevice"
+ "isMemberOfClass:"
+ "isProxy"
+ "isTimerRunning"
+ "lapAddedCancellable"
+ "lapLapTimer"
+ "lapLapTimerCancellable"
+ "laps"
+ "loadInitialState"
+ "mainBundle"
+ "migrateLegacyStopwatch"
+ "mockDate"
+ "needsMigration"
+ "now"
+ "objectForKey:"
+ "offset"
+ "overrideDate"
+ "pauseLapTimer"
+ "pauseLapTimerCancellable"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "previousLapsTotalInterval"
+ "registerObserver:"
+ "release"
+ "removeObject:"
+ "removeObjectForKey:"
+ "removeStopwatch:"
+ "resetLapTimer"
+ "resetLapTimerCancellable"
+ "respondsToSelector:"
+ "restored stopwatches "
+ "resumeLapTimer"
+ "resumeLapTimerCancellable"
+ "retain"
+ "retainCount"
+ "runningTotalForLap:"
+ "self"
+ "setCurrentInterval:"
+ "setDay:"
+ "setDefaults:"
+ "setFrameInterval:"
+ "setIsTimerRunning:"
+ "setLaps:"
+ "setMonth:"
+ "setObject:forKey:"
+ "setOffset:"
+ "setOverrideDate:"
+ "setPreviousLapsTotalInterval:"
+ "setStartDate:"
+ "setState:"
+ "setStorageProxy:"
+ "setSystemReady"
+ "setValue:forKey:"
+ "setViewModel:"
+ "setYear:"
+ "sourceIdentifier"
+ "standardUserDefaults"
+ "startDate"
+ "startLapTimer"
+ "startLapTimerCancellable"
+ "stopwatchActor"
+ "stopwatchManager"
+ "stopwatches"
+ "storageProxy"
+ "superclass"
+ "syncManager"
+ "systemReady"
+ "unregisterObserver:"
+ "updateDate:"
+ "updateStopwatch:"
+ "updateStopwatch:withCompletion:source:"
+ "updateTime"
+ "updateWithDisplayLink"
+ "updatedCancellable"
+ "v16@?0@\"NSArray\"8"
+ "v20@0:8B16"
+ "v24@0:8@\"MTMutableStopwatch\"16"
+ "v24@0:8@\"NSDate\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8d16"
+ "v32@0:8@\"MTStopwatch\"16@\"<MTSource>\"24"
+ "v32@0:8@16@24"
+ "v40@0:8@\"MTStopwatch\"16@?<v@?@\"NSError\">24@\"<MTSource>\"32"
+ "v40@0:8@\"NSNumber\"16@\"MTStopwatch\"24@\"<MTSource>\"32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@?24@32"
+ "v48@0:8@\"NSNumber\"16@\"MTStopwatch\"24@?<v@?@\"NSError\">32@\"<MTSource>\"40"
+ "v48@0:8@16@24@?32@40"
+ "v52@0:8d16d24d32d40B48"
+ "viewModel"
+ "weakObjectsHashTable"
+ "zone"
- "Couldn't find your alarm."
- "didLapStopwatch"
- "didLapStopwatch with delegate "
- "didLapStopwatchWithManager:"
- "didLapStopwatchWithProvider:"
- "didResetStopwatch"
- "didResetStopwatch with delegate "
- "didResetStopwatchWithManager:"
- "didResetStopwatchWithProvider:"
- "didStartStopwatch"
- "didStartStopwatch with delegate "
- "didStartStopwatchWithManager:"
- "didStartStopwatchWithProvider:"
- "didStopStopwatch"
- "didStopStopwatch with delegate "
- "didStopStopwatchWithManager:"
- "didStopStopwatchWithProvider:"
- "v24@0:8@\"_TtC18MobileTimerSupport19MTAppIntentsManager\"16"

```
