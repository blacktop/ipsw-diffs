## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2921.34.7.17.59
-  __TEXT.__text: 0x850a0
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x83d8
-  __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x5fb3
-  __TEXT.__oslogstring: 0x81d6
+2921.35.2.9.18
+  __TEXT.__text: 0x862ec
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x8408
+  __TEXT.__const: 0x2f4
+  __TEXT.__cstring: 0x5fd7
+  __TEXT.__oslogstring: 0x8318
   __TEXT.__gcc_except_tab: 0x1258
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x2178
-  __TEXT.__objc_classname: 0x12bb
-  __TEXT.__objc_methname: 0x11b2c
+  __TEXT.__constg_swiftt: 0x7c
+  __TEXT.__swift5_typeref: 0x38
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x21c8
+  __TEXT.__objc_classname: 0x133b
+  __TEXT.__objc_methname: 0x11b5c
   __TEXT.__objc_methtype: 0x355f
-  __TEXT.__objc_stubs: 0xcee0
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x2f20
-  __DATA_CONST.__objc_classlist: 0x348
+  __TEXT.__objc_stubs: 0xcf20
+  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__const: 0x2f90
+  __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4400
+  __DATA_CONST.__objc_selrefs: 0x4410
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__const: 0xc60
+  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__const: 0xc88
   __AUTH_CONST.__cfstring: 0x4400
-  __AUTH_CONST.__objc_const: 0xd700
+  __AUTH_CONST.__objc_const: 0xd7d8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x14a0
-  __AUTH.__data: 0x10
+  __AUTH.__objc_data: 0x1550
+  __AUTH.__data: 0xd0
   __DATA.__objc_ivar: 0x818
-  __DATA.__data: 0x1ad0
-  __DATA.__bss: 0x1e0
+  __DATA.__data: 0x1ae8
+  __DATA.__bss: 0x1f0
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC0E0F59-BBF5-3937-99A8-104EC641CD2B
-  Functions: 2899
-  Symbols:   10121
-  CStrings:  5421
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 677A6E29-D938-3924-87DD-12A8B5D73795
+  Functions: 2924
+  Symbols:   10205
+  CStrings:  5431
 
Symbols:
+ -[MSPContainer registerObserver:]
+ -[MSPContainer unregisterObserver:]
+ -[MSPMapsPushDaemonRemoteProxy registerObserver:]
+ -[MSPMapsPushDaemonRemoteProxy unregisterObserver:]
+ _MapsFeature_IsEnabled_RiverNorth
+ _OBJC_CLASS_$_GEOAPUserSessionSnapshot
+ _OBJC_CLASS_$_GEOAPUtils
+ _OBJC_CLASS_$__TtC11MapsSupport15RNGEOLogDiscard
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtC11MapsSupport15RNGEOLogDiscard
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __CLASS_METHODS__TtC11MapsSupport15RNGEOLogDiscard
+ __DATA__TtC11MapsSupport15RNGEOLogDiscard
+ __DATA__TtC11MapsSupportP33_D895F6978ABFA0F06ADE38F52CA15BBD19ResourceBundleClass
+ __INSTANCE_METHODS__TtC11MapsSupport15RNGEOLogDiscard
+ __METACLASS_DATA__TtC11MapsSupport15RNGEOLogDiscard
+ __METACLASS_DATA__TtC11MapsSupportP33_D895F6978ABFA0F06ADE38F52CA15BBD19ResourceBundleClass
+ ___106-[MSPSharedTripIDSCapabilityFetchingQueue batchQueryController:updatedDestinationsStatus:onService:error:]_block_invoke.19
+ ___28-[MSPSharedTripService init]_block_invoke.72
+ ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.197
+ ___49-[MSPFileContainerPersister eraseWithCompletion:]_block_invoke.45
+ ___51-[MSPContainer accessContentsUsingConcurrentBlock:]_block_invoke.56
+ ___54-[MSPSharedTripService _performBlockAfterInitialSync:]_block_invoke.83
+ ___56-[MSPContainer accessStateSnapshotUsingConcurrentBlock:]_block_invoke.61
+ ___58-[MSPSharedTripService _fetchActiveHandlesWithCompletion:]_block_invoke.134
+ ___60-[MSPSharedTripService _performBlockAfterInitialConnection:]_block_invoke.80
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.88
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.89
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.90
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.91
+ ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke.104
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke.105
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_2.106
+ ___62-[MSPFileContainerPersister fetchStateSnapshotWithCompletion:]_block_invoke.37
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke.13
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_2.15
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_3.17
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_4.35
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_5.39
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_6.40
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke.102
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_2.103
+ ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke.103
+ ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke.111
+ ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke.113
+ ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke_2.118
+ ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke_3.122
+ ___70-[MSPSharedTripCapabilityFetchingServer fetchCapabilitiesForContacts:]_block_invoke.101
+ ___76-[MSPSharedTripCapabilityFetchingServer listener:shouldAcceptNewConnection:]_block_invoke.96
+ ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.137
+ ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke.127
+ ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke.130
+ ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke.144
+ ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke_2.137
+ ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke_2.145
+ ___86-[MSPContainer _performInitialLoadNotifyingObservers:kickOffSynchronously:completion:]_block_invoke.65
+ ___86-[MSPContainer _performInitialLoadNotifyingObservers:kickOffSynchronously:completion:]_block_invoke.76
+ ___86-[MSPFileContainerPersister commitByMergingWithStateSnapshot:mergeOptions:completion:]_block_invoke.42
+ ___86-[MSPFileContainerPersister commitByMergingWithStateSnapshot:mergeOptions:completion:]_block_invoke.43
+ ___91-[MSPContainer editByMergingStateSnapshot:mergeOptions:context:completionQueue:completion:]_block_invoke.91
+ ___91-[MSPContainer editByMergingStateSnapshot:mergeOptions:context:completionQueue:completion:]_block_invoke.92
+ ___93-[MSPFileContainerPersister commitEditWithNewContents:edits:appliedToOldContents:completion:]_block_invoke.39
+ ___93-[MSPFileContainerPersister commitEditWithNewContents:edits:appliedToOldContents:completion:]_block_invoke.41
+ ___MSPUGCFetchClientCertificate_block_invoke.24
+ ___UGCFetchLogDiscardCertificatesForSessionWithCompletion_block_invoke.73
+ ___block_literal_global.104
+ ___block_literal_global.105
+ ___block_literal_global.108
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.121
+ ___block_literal_global.124
+ ___block_literal_global.131
+ ___block_literal_global.132
+ ___block_literal_global.140
+ ___block_literal_global.148
+ ___block_literal_global.180
+ ___block_literal_global.188
+ ___block_literal_global.20
+ ___block_literal_global.202
+ ___block_literal_global.210
+ ___block_literal_global.230
+ ___block_literal_global.238
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.262
+ ___block_literal_global.270
+ ___block_literal_global.290
+ ___block_literal_global.304
+ ___block_literal_global.312
+ ___block_literal_global.320
+ ___block_literal_global.328
+ ___block_literal_global.342
+ ___block_literal_global.38
+ ___block_literal_global.48
+ ___block_literal_global.81
+ ___block_literal_global.82
+ ___block_literal_global.83
+ ___block_literal_global.95
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_MapsSupport
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_MapsSupport
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_MapsSupport
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$captureUgcDeleteWithSignature:certificates:sessionSnapshot:trigger:queue:completion:
+ _objc_msgSend$donateLogDiscard:
+ _objc_msgSend$snapshotForType:
+ _objc_msgSend$uuidFrom:
+ _objc_opt_self
+ _pathsAtLocation:.me.38
+ _pathsAtLocation:.me.40
+ _pathsAtLocation:.onceToken.39
+ _pathsAtLocation:.onceToken.41
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 11MapsSupport15RNGEOLogDiscardC
+ _symbolic _____ 11MapsSupport19ResourceBundleClass33_D895F6978ABFA0F06ADE38F52CA15BBDLLC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- -[MSPContainer addObserver:]
- -[MSPContainer removeObserver:]
- -[MSPMapsPushDaemonRemoteProxy addObserver:]
- -[MSPMapsPushDaemonRemoteProxy removeObserver:]
- ___106-[MSPSharedTripIDSCapabilityFetchingQueue batchQueryController:updatedDestinationsStatus:onService:error:]_block_invoke.13
- ___28-[MSPSharedTripService init]_block_invoke.68
- ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.191
- ___49-[MSPFileContainerPersister eraseWithCompletion:]_block_invoke.39
- ___51-[MSPContainer accessContentsUsingConcurrentBlock:]_block_invoke.50
- ___54-[MSPSharedTripService _performBlockAfterInitialSync:]_block_invoke.79
- ___56-[MSPContainer accessStateSnapshotUsingConcurrentBlock:]_block_invoke.55
- ___58-[MSPSharedTripService _fetchActiveHandlesWithCompletion:]_block_invoke.128
- ___60-[MSPSharedTripService _performBlockAfterInitialConnection:]_block_invoke.76
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.82
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.84
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.85
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.87
- ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke.98
- ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke.99
- ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_2.100
- ___62-[MSPFileContainerPersister fetchStateSnapshotWithCompletion:]_block_invoke.31
- ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke.7
- ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_2.9
- ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_3.11
- ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_4.29
- ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_5.33
- ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_6.34
- ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke.96
- ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_2.97
- ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke.105
- ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke.107
- ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke.97
- ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke_2.100
- ___69-[MSPContainer eraseFromStorageTypes:withCompletionQueue:completion:]_block_invoke_3.116
- ___70-[MSPSharedTripCapabilityFetchingServer fetchCapabilitiesForContacts:]_block_invoke.95
- ___76-[MSPSharedTripCapabilityFetchingServer listener:shouldAcceptNewConnection:]_block_invoke.90
- ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.131
- ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke.121
- ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke.124
- ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke.138
- ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke_2.131
- ___81-[MSPContainer editContentsUsingBarrierBlock:context:completionQueue:completion:]_block_invoke_2.139
- ___86-[MSPContainer _performInitialLoadNotifyingObservers:kickOffSynchronously:completion:]_block_invoke.59
- ___86-[MSPContainer _performInitialLoadNotifyingObservers:kickOffSynchronously:completion:]_block_invoke.64
- ___86-[MSPFileContainerPersister commitByMergingWithStateSnapshot:mergeOptions:completion:]_block_invoke.36
- ___86-[MSPFileContainerPersister commitByMergingWithStateSnapshot:mergeOptions:completion:]_block_invoke.37
- ___91-[MSPContainer editByMergingStateSnapshot:mergeOptions:context:completionQueue:completion:]_block_invoke.85
- ___91-[MSPContainer editByMergingStateSnapshot:mergeOptions:context:completionQueue:completion:]_block_invoke.86
- ___93-[MSPFileContainerPersister commitEditWithNewContents:edits:appliedToOldContents:completion:]_block_invoke.33
- ___93-[MSPFileContainerPersister commitEditWithNewContents:edits:appliedToOldContents:completion:]_block_invoke.35
- ___MSPUGCFetchClientCertificate_block_invoke.20
- ___UGCFetchLogDiscardCertificatesForSessionWithCompletion_block_invoke.65
- ___block_literal_global.102
- ___block_literal_global.106
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.110
- ___block_literal_global.12
- ___block_literal_global.125
- ___block_literal_global.126
- ___block_literal_global.134
- ___block_literal_global.14
- ___block_literal_global.142
- ___block_literal_global.150
- ___block_literal_global.182
- ___block_literal_global.190
- ___block_literal_global.204
- ___block_literal_global.212
- ___block_literal_global.232
- ___block_literal_global.240
- ___block_literal_global.248
- ___block_literal_global.256
- ___block_literal_global.264
- ___block_literal_global.272
- ___block_literal_global.292
- ___block_literal_global.306
- ___block_literal_global.314
- ___block_literal_global.32
- ___block_literal_global.322
- ___block_literal_global.330
- ___block_literal_global.50
- ___block_literal_global.75
- ___block_literal_global.77
- ___block_literal_global.78
- ___block_literal_global.91
- ___block_literal_global.99
- _objc_msgSend$addObserver:
- _objc_msgSend$captureUgcDeleteWithSignature:certificates:trigger:queue:completion:
- _pathsAtLocation:.me.32
- _pathsAtLocation:.me.34
- _pathsAtLocation:.onceToken.33
- _pathsAtLocation:.onceToken.35
CStrings:
+ "Assertion failed: completion != ((void*)0)"
+ "Assertion failed: dataToSign != ((void*)0)"
+ "Donating log discard signal with sessionID: %{private}s"
+ "Error donating log discard signal. sessionID: %{private}s Error: %@"
+ "Feature unavailable."
+ "Missing snapshot. Unable to donate Log Discard signal."
+ "Successfully donated log discard signal with sessionID: %{private}s"
+ "_TtC11MapsSupport15RNGEOLogDiscard"
+ "_TtC11MapsSupportP33_D895F6978ABFA0F06ADE38F52CA15BBD19ResourceBundleClass"
+ "captureUgcDeleteWithSignature:certificates:sessionSnapshot:trigger:queue:completion:"
+ "com.apple.GeoAnalytics"
+ "donateLogDiscard:"
+ "snapshotForType:"
+ "uuidFrom:"
- "Assertion failed: completion != ((void *)0)"
- "Assertion failed: dataToSign != ((void *)0)"
- "addObserver:"
- "captureUgcDeleteWithSignature:certificates:trigger:queue:completion:"

```
