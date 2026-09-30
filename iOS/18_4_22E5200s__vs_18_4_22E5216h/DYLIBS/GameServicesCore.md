## GameServicesCore

> `/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore`

```diff

-819.4.25.2.1
-  __TEXT.__text: 0x12a94c
-  __TEXT.__auth_stubs: 0x40e0
-  __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0xc818
-  __TEXT.__swift5_typeref: 0x495c
-  __TEXT.__swift_as_entry: 0x7ac
-  __TEXT.__swift_as_ret: 0x970
-  __TEXT.__cstring: 0x21af
-  __TEXT.__oslogstring: 0x61f
-  __TEXT.__swift5_reflstr: 0x1856
-  __TEXT.__swift5_assocty: 0x700
-  __TEXT.__constg_swiftt: 0x1e78
-  __TEXT.__swift5_fieldmd: 0x1e58
-  __TEXT.__swift5_proto: 0x874
-  __TEXT.__swift5_types: 0x1ec
-  __TEXT.__swift5_acfuncs: 0x76c
-  __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_builtin: 0x3c
+819.4.37.0.0
+  __TEXT.__text: 0x16de50
+  __TEXT.__auth_stubs: 0x4740
+  __TEXT.__const: 0xed20
+  __TEXT.__swift5_typeref: 0x61d4
+  __TEXT.__swift_as_entry: 0x9ac
+  __TEXT.__swift_as_ret: 0xbdc
+  __TEXT.__cstring: 0x2b3f
+  __TEXT.__oslogstring: 0xc06
+  __TEXT.__constg_swiftt: 0x24c4
+  __TEXT.__swift5_reflstr: 0x1dd6
+  __TEXT.__swift5_fieldmd: 0x26f4
+  __TEXT.__swift5_types: 0x258
+  __TEXT.__swift5_assocty: 0x818
+  __TEXT.__swift5_proto: 0xa00
+  __TEXT.__swift5_acfuncs: 0x870
+  __TEXT.__swift5_capture: 0x1b0
+  __TEXT.__swift5_protos: 0x4c
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6870
-  __TEXT.__eh_frame: 0x12150
-  __TEXT.__objc_classname: 0x9
-  __TEXT.__objc_methname: 0x37d
-  __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__unwind_info: 0x80a0
+  __TEXT.__eh_frame: 0x16158
+  __TEXT.__objc_methname: 0x2b5
+  __DATA_CONST.__got: 0x1070
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x188
-  __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2070
-  __AUTH_CONST.__auth_ptr: 0x1428
-  __AUTH_CONST.__const: 0x3f18
-  __AUTH_CONST.__objc_const: 0x1d68
-  __AUTH.__objc_data: 0x5f0
-  __AUTH.__data: 0x20f8
-  __DATA.__data: 0x3f38
-  __DATA.__common: 0x168
-  __DATA.__bss: 0x10880
+  __DATA_CONST.__objc_selrefs: 0x110
+  __AUTH_CONST.__auth_got: 0x23a0
+  __AUTH_CONST.__auth_ptr: 0x1660
+  __AUTH_CONST.__const: 0x4d70
+  __AUTH_CONST.__objc_const: 0x20b0
+  __AUTH.__objc_data: 0x6e0
+  __AUTH.__data: 0x27d0
+  __DATA.__data: 0x4dd8
+  __DATA.__bss: 0x13b10
+  __DATA.__common: 0x1a0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftData.framework/SwiftData
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/GameCenterServerClient.framework/GameCenterServerClient
   - /System/Library/PrivateFrameworks/GameServices.framework/GameServices
   - /System/Library/PrivateFrameworks/HTTPTypesInternal.framework/HTTPTypesInternal

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib

   - /usr/lib/swift/libswift_stdio.dylib
   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7428
-  Symbols:   3197
-  CStrings:  365
+  Functions: 9094
+  Symbols:   3943
+  CStrings:  415
 
Symbols:
+ _AMSErrorDomain
+ _AMSErrorUserInfoKeyServerPayload
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSMediaResult
+ _OBJC_CLASS_$_AMSMediaTask
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_release
+ _objc_retain_x24
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_deletedAsyncMethodErrorTu
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_OS_dispatch_queue
- __Block_copy
- __Block_release
- _objc_release_x26
- _objc_retain_x25
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "$s16GameServicesCore43$DistributedIntegrationTestsServiceProtocolC14listChallenges6player7filters5after0aB04PageVyAH3RefVyAH9Challenge_pGGALyAH6Player_pG_SayAH0P6FilterOGSgAH6CursorVSgtYaKFTE"
+ "$s16GameServicesCore43$DistributedIntegrationTestsServiceProtocolC19listChallengeStates6player10challengesSay0aB00J5StateVSgGAG3RefVyAG6Player_pG_SayAMyAG0J0_pGGtYaKFTE"
+ "$s16GameServicesCore43$DistributedIntegrationTestsServiceProtocolC4load8bulkDataySayAA013BulkChallengeK0VG_tYaKFTE"
+ "$s16GameServicesCore43$DistributedIntegrationTestsServiceProtocolC5purge17challengeIDPrefixySS_tYaKFTE"
+ "$s16GameServicesCore43$DistributedIntegrationTestsServiceProtocolC8describe10challengesSay0aB020ChallengeDescriptionVSgGSayAF3RefVyAF0K0_pGG_tYaKFTE"
+ "%02d:%02d:%02d.%02d"
+ "%02d:%02d:%02d.%03d"
+ "%s failed to get challenge ID: %s, error: %@"
+ "%s failed to purge entries with prefix: %s, error: %@"
+ "%s purged entries before %s"
+ "%s purged entries with prefix: %s"
+ "%s stored %ld bulk data entries"
+ "Can't route ChallengeUpdate notification userInfo: %s to player ID: %s"
+ "Cannot handle deep link opened notification with no authenticated player ID"
+ "Cannot transition from %s to %s"
+ "Challenge ID: %s refers to leaderboard ASC UUID: %s this is unknown to GCS"
+ "ChallengeDescription"
+ "Challenges that don't reference a leaderboard are not supported: %s"
+ "Failed to convert stored challenge instance into: %s id: %s, error: %@"
+ "Failed to create safe data date"
+ "Failed to create trackable for challenge definition ID: "
+ "Failed to delete challenge IDs: %s, error: %@"
+ "Failed to fetch game metadata for bundleID: %s, error: %@"
+ "Failed to refresh challenges from update: %s for player ID: %s, error: %@"
+ "Failed to remove item at: %s, error: %@"
+ "Failed to remove replaced %s for gameBundleIDs: %s, error: %@"
+ "Failed to run: %s: %@"
+ "Failed to sync challenge ID: %s for player ID: %s, error: %@"
+ "GameCenterServerNotification.ChallengeUpdate"
+ "GameCenterServerNotification.GameActivityPartyURLReceivedOrOpened"
+ "GameCenterServerNotification.GameActivityReferralDeepLinkOpened"
+ "GameServicesCore/ChallengeStore.swift"
+ "IDDrivenChallengeSyncOperation("
+ "Ignoring invalid or incomplete challenge definition data: %s"
+ "Ignoring unsupported attempt limit: %s"
+ "Illegal attempt to retrieve a GameActivityPartyURLReceivedOrOpened instance from: "
+ "Illegal attempt to retrieve a GameActivityReferralDeepLinkOpened instance from: "
+ "Invalid challenge status: "
+ "Invalid invitee status: "
+ "Invalid stored platform type: "
+ "No ChallengeSyncOperation for filters: "
+ "No challenge definitions found in MAPI for bundleID: %s"
+ "No game metadata available for bundleID: "
+ "Received a notification that a deep link was opened: %s"
+ "Received a notification with multiple referral types: %s"
+ "Received a notification with no valid referral type: %s"
+ "Refreshing all definitions for bundleID: %s (i.e. ignoring filters: %s"
+ "Removing contents of directory: %s, matching: %s"
+ "Running %s"
+ "StatusDrivenChallengeSyncOperation("
+ "Stored challenge ID: %s"
+ "Successfully handled update notification for challenge ID: %s, player ID: %s"
+ "Unable to retrieve contents of directory: %s, matching: %s, error: %@"
+ "Unexpected challenge filter: "
+ "Unexpected challenge invite filter: "
+ "Updated %ld definitions for bundleID: %s"
+ "_TtC16GameServicesCore23IntegrationTestsService"
+ "_TtC16GameServicesCore43$DistributedIntegrationTestsServiceProtocol"
+ "_TtCV16GameServicesCoreP33_2D441778A4A5881EFABEBF590F5A619422ChallengeStoreSchemaV110Definition"
+ "_artwork"
+ "_associatedInstance"
+ "_attemptLimitOptions"
+ "_consumptionState"
+ "_createCheckedThrowingContinuation(_:)"
+ "_desc"
+ "_groupID"
+ "_isArchived"
+ "_iso8601DurationOptions"
+ "_platformToMinVersion"
+ "_shortGroupID"
+ "_statusMessage"
+ "_title"
+ "alreadyAccepted"
+ "alreadyInvited"
+ "associatedInstance"
+ "attemptLimitOptions"
+ "bagForProfile:profileVersion:"
+ "challengeAlreadyEnded"
+ "challengeIDPrefix"
+ "challengeLimitExceeded"
+ "consumptionState"
+ "describe(challenges:)"
+ "iOS"
+ "initWithType:clientIdentifier:clientVersion:bag:"
+ "invalid"
+ "inviteLimitExceeded"
+ "iso8601DurationOptions"
+ "leaderboardEntryProperties"
+ "listChallengeStates(player:challenges:)"
+ "listChallenges(player:filters:after:)"
+ "macOS"
+ "perform"
+ "platformToMinVersion"
+ "providerReferenceIdentifier"
+ "purge(challengeIDPrefix:)"
+ "relate[challenges]"
+ "responseDataItems"
+ "resultWithCompletion:"
+ "setAdditionalQueryParams:"
+ "setItemIdentifiers:"
+ "tvOS"
+ "unavailable"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
+ "visionOS"
+ "watchOS"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Background fetching challenge IDs: %s"
- "Failed to convert stored challenge instance into description id: %s, error: %@"
- "Failed to read and store challenge detail for id: %s, error: %@"
- "Failed to remove item: %@"
- "GameCenterServerNotification.GameActivityPartyURLOpened"
- "Illegal attempt to fetch GCS type from: "
- "Illegal attempt to retrieve a CacheInvalidation instance from: "
- "Illegal attempt to retrieve a GameActivityPartyURLOpened instance from: "
- "Invalid cursor: "
- "NSObject"
- "No challenge refs providers for filters: "
- "Q16@0:8"
- "Received a cache invalidation notification: %s"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Unable to retrieve contents of directory with error: %@"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "addObserverForName:object:queue:usingBlock:"
- "autorelease"
- "class"
- "com.apple.gameServices.challengeTaskQueue"
- "conformsToProtocol:"
- "debugDescription"
- "description"
- "hash"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "mainQueue"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "superclass"
- "v16@?0@\"NSNotification\"8"
- "zone"

```
