## FamilyCircle

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle`

```diff

-254.325.7.0.0
-  __TEXT.__text: 0xc7ae4
-  __TEXT.__auth_stubs: 0x2750
-  __TEXT.__objc_methlist: 0x3e4c
-  __TEXT.__const: 0x8ab8
-  __TEXT.__gcc_except_tab: 0x584
-  __TEXT.__cstring: 0x6956
-  __TEXT.__oslogstring: 0x4df2
+254.475.11.0.0
+  __TEXT.__text: 0xd8c14
+  __TEXT.__auth_stubs: 0x27a0
+  __TEXT.__objc_methlist: 0x3f84
+  __TEXT.__const: 0x9088
+  __TEXT.__gcc_except_tab: 0x50c
+  __TEXT.__cstring: 0x5b84
+  __TEXT.__oslogstring: 0x4f72
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__swift5_typeref: 0x2750
-  __TEXT.__constg_swiftt: 0x27d0
-  __TEXT.__swift5_reflstr: 0x132d
-  __TEXT.__swift5_fieldmd: 0x1d3c
-  __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_assocty: 0x5f0
-  __TEXT.__swift5_proto: 0x688
-  __TEXT.__swift5_types: 0x2c4
+  __TEXT.__swift5_typeref: 0x28ee
+  __TEXT.__constg_swiftt: 0x2a80
+  __TEXT.__swift5_reflstr: 0x154d
+  __TEXT.__swift5_fieldmd: 0x1f6c
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_assocty: 0x620
+  __TEXT.__swift5_proto: 0x6d8
+  __TEXT.__swift5_types: 0x2e8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x7e4
-  __TEXT.__swift_as_entry: 0x1d0
-  __TEXT.__swift_as_ret: 0x220
-  __TEXT.__swift5_protos: 0x70
-  __TEXT.__unwind_info: 0x3e78
-  __TEXT.__eh_frame: 0x6190
-  __TEXT.__objc_classname: 0x98e
-  __TEXT.__objc_methname: 0xac47
-  __TEXT.__objc_methtype: 0x1984
-  __TEXT.__objc_stubs: 0x5160
-  __DATA_CONST.__got: 0xaa8
-  __DATA_CONST.__const: 0x1910
-  __DATA_CONST.__objc_classlist: 0x3a0
+  __TEXT.__swift5_capture: 0x7d4
+  __TEXT.__swift_as_entry: 0x1d8
+  __TEXT.__swift_as_ret: 0x264
+  __TEXT.__swift5_protos: 0x78
+  __TEXT.__unwind_info: 0x4310
+  __TEXT.__eh_frame: 0x6be0
+  __TEXT.__objc_classname: 0x11be
+  __TEXT.__objc_methname: 0xb51d
+  __TEXT.__objc_methtype: 0x1e80
+  __TEXT.__objc_stubs: 0x6e20
+  __DATA_CONST.__got: 0xae0
+  __DATA_CONST.__const: 0x1a20
+  __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a0
+  __DATA_CONST.__objc_selrefs: 0x27e0
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x13b8
-  __AUTH_CONST.__const: 0x6888
-  __AUTH_CONST.__cfstring: 0x3ea0
-  __AUTH_CONST.__objc_const: 0xc890
+  __AUTH_CONST.__auth_got: 0x13e0
+  __AUTH_CONST.__const: 0x6b78
+  __AUTH_CONST.__cfstring: 0x3f00
+  __AUTH_CONST.__objc_const: 0xcc90
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1348
-  __AUTH.__data: 0x1590
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__data: 0x2668
-  __DATA.__bss: 0xc1e0
-  __DATA.__common: 0x70
+  __AUTH.__objc_data: 0x1560
+  __AUTH.__data: 0x1810
+  __DATA.__objc_ivar: 0x444
+  __DATA.__data: 0x2790
+  __DATA.__bss: 0xcae0
+  __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x1340
-  __DATA_DIRTY.__data: 0x700
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__data: 0x6f8
+  __DATA_DIRTY.__bss: 0x250
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2E892673-B844-3132-87E7-F506F52B8535
-  Functions: 5497
-  Symbols:   6840
-  CStrings:  4004
+  UUID: 9BB47927-035D-38ED-A539-498D4385221F
+  Functions: 5784
+  Symbols:   7207
+  CStrings:  4024
 
Symbols:
+ +[FARequestCoalescer sharedInstance]
+ +[FARequestCoalescer sharedInstance].cold.1
+ -[FAAgeRangeController getAgeVerificationInfoForDSID:completion:].cold.1
+ -[FARequestCoalescer .cxx_destruct]
+ -[FARequestCoalescer coalesceQueue]
+ -[FARequestCoalescer inFlightRequests]
+ -[FARequestCoalescer init]
+ -[FARequestCoalescer performBlockForKey:force:block:]
+ -[FARequestCoalescer setCoalesceQueue:]
+ -[FARequestCoalescer setInFlightRequests:]
+ _FAUniversalLinkActionAddMember
+ _FAUniversalLinkActionSetupFamily
+ _OBJC_CLASS_$_FARequestCoalescer
+ _OBJC_CLASS_$__TtC12FamilyCircle20FADeleteFamilyResult
+ _OBJC_IVAR_$_FAAgeRangeController._requestCoalescer
+ _OBJC_IVAR_$_FARequestCoalescer._coalesceQueue
+ _OBJC_IVAR_$_FARequestCoalescer._inFlightRequests
+ _OBJC_METACLASS_$_FARequestCoalescer
+ _OBJC_METACLASS_$__TtC12FamilyCircle20FADeleteFamilyResult
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __DATA__TtC12FamilyCircle20DaemonContainerActor
+ __DATA__TtC12FamilyCircle20FADeleteFamilyResult
+ __DATA__TtC12FamilyCircle36SignificantChangeAckExtensionContext
+ __INSTANCE_METHODS__TtC12FamilyCircle20FADeleteFamilyResult
+ __IVARS__TtC12FamilyCircle20DaemonContainerActor
+ __IVARS__TtC12FamilyCircle20FADeleteFamilyResult
+ __IVARS__TtC12FamilyCircle36SignificantChangeAckExtensionContext
+ __METACLASS_DATA__TtC12FamilyCircle20DaemonContainerActor
+ __METACLASS_DATA__TtC12FamilyCircle20FADeleteFamilyResult
+ __METACLASS_DATA__TtC12FamilyCircle36SignificantChangeAckExtensionContext
+ __OBJC_$_CLASS_METHODS_FARequestCoalescer
+ __OBJC_$_INSTANCE_METHODS_FARequestCoalescer
+ __OBJC_$_INSTANCE_VARIABLES_FARequestCoalescer
+ __OBJC_$_PROP_LIST_FARequestCoalescer
+ __OBJC_CLASS_RO_$_FARequestCoalescer
+ __OBJC_METACLASS_RO_$_FARequestCoalescer
+ __PROPERTIES__TtC12FamilyCircle20FADeleteFamilyResult
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.53
+ ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.53.cold.1
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.33
+ ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.33.cold.1
+ ___36+[FARequestCoalescer sharedInstance]_block_invoke
+ ___52-[FAAgeRangeController saveAgeRangeWith:completion:]_block_invoke.24
+ ___52-[FAAgeRangeController saveAgeRangeWith:completion:]_block_invoke.24.cold.1
+ ___53-[FARequestCoalescer performBlockForKey:force:block:]_block_invoke
+ ___53-[FARequestCoalescer performBlockForKey:force:block:]_block_invoke.26
+ ___53-[FARequestCoalescer performBlockForKey:force:block:]_block_invoke_2
+ ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.18
+ ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.18.cold.1
+ ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.20
+ ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.20.cold.1
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.48
+ ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.48.cold.1
+ ___54-[FAAgeRangeController updateAgeRangeWith:completion:]_block_invoke.26
+ ___54-[FAAgeRangeController updateAgeRangeWith:completion:]_block_invoke.26.cold.1
+ ___55-[FAAgeRangeController deleteAgeRangesWith:completion:]_block_invoke.22
+ ___55-[FAAgeRangeController deleteAgeRangesWith:completion:]_block_invoke.22.cold.1
+ ___55-[FAAgeRangeController fetchDSIDWithCompletionHandler:]_block_invoke.46
+ ___55-[FAAgeRangeController fetchDSIDWithCompletionHandler:]_block_invoke.46.cold.1
+ ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.27
+ ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.27.cold.1
+ ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.43
+ ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.43.cold.1
+ ___59-[FADeleteFamilyRequest startRequestWithCompletionHandler:]_block_invoke.29
+ ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.40
+ ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.40.cold.1
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.50
+ ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.50.cold.1
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.60
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.62
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.63
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.63.cold.1
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.66
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke_2
+ ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke_2.cold.1
+ ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.29
+ ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.29.cold.1
+ ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.37
+ ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.37.cold.1
+ ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.30
+ ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.30.cold.1
+ ___block_descriptor_48_e8_32s40s_e20_v24?08"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e17_"AAFPromise"8?0lw40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e25_v16?0?<v?"NSError">8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___swift_assign_boxed_opaque_existential_1
+ ___swift_memcpy64_8
+ _associated conformance 12FamilyCircle06DeleteA5ErrorOSHAASQ
+ _associated conformance 12FamilyCircle16MemberRegionInfoV10CodingKeys33_51EBD72701D2FB0053076755A1090D02LLOSHAASQ
+ _associated conformance 12FamilyCircle16MemberRegionInfoV10CodingKeys33_51EBD72701D2FB0053076755A1090D02LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 12FamilyCircle16MemberRegionInfoV10CodingKeys33_51EBD72701D2FB0053076755A1090D02LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 12FamilyCircle19DefaultCachedAtDateOAA07CodableC6SourceAA5ValueAaDP_SE
+ _associated conformance 12FamilyCircle19DefaultCachedAtDateOAA07CodableC6SourceAA5ValueAaDP_Se
+ _associated conformance 12FamilyCircle20DaemonContainerActorCs06GlobalE0AA0E4TypesADP_ScA
+ _associated conformance 12FamilyCircle20DefaultCacheDurationOAA07CodableC6SourceAA5ValueAaDP_SE
+ _associated conformance 12FamilyCircle20DefaultCacheDurationOAA07CodableC6SourceAA5ValueAaDP_Se
+ _associated conformance 12FamilyCircle25InternalRegulatoryFeatureOSHAASQ
+ _associated conformance 12FamilyCircle25InternalRegulatoryFeatureOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 12FamilyCircle36SignificantChangeAckExtensionContextC10CodingKeys33_E81F41A99E77DF7B41AE92997F36F657LLOSHAASQ
+ _associated conformance 12FamilyCircle36SignificantChangeAckExtensionContextC10CodingKeys33_E81F41A99E77DF7B41AE92997F36F657LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 12FamilyCircle36SignificantChangeAckExtensionContextC10CodingKeys33_E81F41A99E77DF7B41AE92997F36F657LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper.17
+ _block_copy_helper.20
+ _block_copy_helper.24
+ _block_copy_helper.33
+ _block_copy_helper.36
+ _block_copy_helper.42
+ _block_copy_helper.48
+ _block_copy_helper.53
+ _block_copy_helper.55
+ _block_copy_helper.63
+ _block_copy_helper.69
+ _block_copy_helper.77
+ _block_descriptor.19
+ _block_descriptor.22
+ _block_descriptor.26
+ _block_descriptor.35
+ _block_descriptor.38
+ _block_descriptor.44
+ _block_descriptor.50
+ _block_descriptor.55
+ _block_descriptor.57
+ _block_descriptor.65
+ _block_descriptor.71
+ _block_descriptor.79
+ _block_destroy_helper.18
+ _block_destroy_helper.21
+ _block_destroy_helper.25
+ _block_destroy_helper.34
+ _block_destroy_helper.37
+ _block_destroy_helper.43
+ _block_destroy_helper.49
+ _block_destroy_helper.54
+ _block_destroy_helper.56
+ _block_destroy_helper.64
+ _block_destroy_helper.70
+ _block_destroy_helper.78
+ _keypath_get.4Tm
+ _objc_msgSend$aa_addDeviceProvisioningInfoHeadersWithDSID:
+ _objc_msgSend$aa_isPrimaryEmailVerified
+ _objc_msgSend$aa_isSuspended
+ _objc_msgSend$aa_primaryAppleAccountWithCompletion:
+ _objc_msgSend$aa_suspensionInfo
+ _objc_msgSend$acceptShareInvitationsFromURLs:intoPersistentStore:completion:
+ _objc_msgSend$acceptanceStatus
+ _objc_msgSend$accountStore
+ _objc_msgSend$accounts
+ _objc_msgSend$addListenerID:forService:
+ _objc_msgSend$addParticipant:
+ _objc_msgSend$ageCategory
+ _objc_msgSend$aida_accountForPrimaryiCloudAccount
+ _objc_msgSend$areContactsManagedForDSID:
+ _objc_msgSend$auditToken
+ _objc_msgSend$availabilityForListenerID:forService:
+ _objc_msgSend$badgeAfter
+ _objc_msgSend$broadcastFamilyChangedNotification
+ _objc_msgSend$buildInvite:replyBlock:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$bundleRecordForAuditToken:error:
+ _objc_msgSend$clearPendingFollowUpItemsWithUniqueIdentifiers:error:
+ _objc_msgSend$cloudKitContainer
+ _objc_msgSend$cloudKitContainerOptions
+ _objc_msgSend$coalesceQueue
+ _objc_msgSend$conditions
+ _objc_msgSend$containerIdentifier
+ _objc_msgSend$currentState
+ _objc_msgSend$dataForKey:
+ _objc_msgSend$dataclassActionsForAccountSave:
+ _objc_msgSend$declaredAgeRangeOverrides
+ _objc_msgSend$deregisterTaskWithIdentifier:
+ _objc_msgSend$enabled
+ _objc_msgSend$endowmentNamespaces
+ _objc_msgSend$endpoints
+ _objc_msgSend$environment
+ _objc_msgSend$error
+ _objc_msgSend$errorMessage
+ _objc_msgSend$errorTitle
+ _objc_msgSend$familyChecklistRankingConfigWithCachePolicy:replyBlock:
+ _objc_msgSend$fetchParentalControlBitsForAltDSID:replyBlock:
+ _objc_msgSend$fetchParticipantsMatchingLookupInfos:intoPersistentStore:completion:
+ _objc_msgSend$fetchSharesInPersistentStore:error:
+ _objc_msgSend$handleForIdentifier:error:
+ _objc_msgSend$hours
+ _objc_msgSend$iTunesMetadata
+ _objc_msgSend$idInfoForDestinations:service:infoTypes:options:listenerID:queue:completionBlock:
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$identity
+ _objc_msgSend$idsCache
+ _objc_msgSend$inFlightRequests
+ _objc_msgSend$initWithAccountType:
+ _objc_msgSend$initWithAltDSID:bundleID:lowerbound:upperbound:createdAt:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithConditions:
+ _objc_msgSend$initWithContext:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithEmailAddress:
+ _objc_msgSend$initWithEnabled:strictPolicy:
+ _objc_msgSend$initWithEnabled:strictPolicy:limitType:
+ _objc_msgSend$initWithEntity:insertIntoManagedObjectContext:
+ _objc_msgSend$initWithEntityName:
+ _objc_msgSend$initWithError:
+ _objc_msgSend$initWithHTTPResponse:data:
+ _objc_msgSend$initWithHTTPResponse:data:bodyIsPlist:
+ _objc_msgSend$initWithHTTPResponse:data:mediaType:
+ _objc_msgSend$initWithHeartbeatActivityHandler:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentifier:description:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithLowerbound:upperbound:validationLevel:response:parentalControlsInformation:isSharingNewInformation:verificationMethod:
+ _objc_msgSend$initWithPassword:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithRawValue:
+ _objc_msgSend$initWithRecordZoneID:
+ _objc_msgSend$initWithSourceProperty:operand:result:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithSuccess:errorTitle:errorMessage:learnMoreURL:statusMessage:statusCode:
+ _objc_msgSend$interval
+ _objc_msgSend$invitationDate
+ _objc_msgSend$invitationToken
+ _objc_msgSend$inviteDate
+ _objc_msgSend$inviteType
+ _objc_msgSend$isBeta
+ _objc_msgSend$isCurrentUser
+ _objc_msgSend$isFamilyCircleFresh
+ _objc_msgSend$isFamilySuspended
+ _objc_msgSend$isGuardian
+ _objc_msgSend$isProfileValidated
+ _objc_msgSend$key
+ _objc_msgSend$learnMoreURL
+ _objc_msgSend$limitType
+ _objc_msgSend$localizedName
+ _objc_msgSend$localizedStringFromPersonNameComponents:style:options:
+ _objc_msgSend$lookupInfo
+ _objc_msgSend$mainBundle
+ _objc_msgSend$memberSortOrder
+ _objc_msgSend$milliseconds
+ _objc_msgSend$minDurationBetweenInstances
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$newBackgroundContext
+ _objc_msgSend$normalizedDSID
+ _objc_msgSend$onComplete:onQueue:
+ _objc_msgSend$operand
+ _objc_msgSend$organizerDSID
+ _objc_msgSend$organizerFirstName
+ _objc_msgSend$organizerLastName
+ _objc_msgSend$participants
+ _objc_msgSend$pendingInvitesOnly
+ _objc_msgSend$pendingMembers
+ _objc_msgSend$performBlockForKey:force:block:
+ _objc_msgSend$performRequestWithSession:withHandler:
+ _objc_msgSend$permission
+ _objc_msgSend$persistUpdatedShare:inPersistentStore:completion:
+ _objc_msgSend$persistentStoreDescriptions
+ _objc_msgSend$postFollowUpItem:error:
+ _objc_msgSend$postInstall
+ _objc_msgSend$powerNap
+ _objc_msgSend$priority
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$recordID
+ _objc_msgSend$recordZone
+ _objc_msgSend$refreshIDInfo
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$removeListenerID:forService:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeParticipant:
+ _objc_msgSend$requiresBuddyComplete
+ _objc_msgSend$requiresExternalPower
+ _objc_msgSend$requiresInexpensiveNetworkConnectivity
+ _objc_msgSend$requiresNetworkConnectivity
+ _objc_msgSend$resourceIntensive
+ _objc_msgSend$responseDictionary
+ _objc_msgSend$result
+ _objc_msgSend$role
+ _objc_msgSend$save:
+ _objc_msgSend$saveAccount:withDataclassActions:doVerify:completion:
+ _objc_msgSend$scheduleAfter
+ _objc_msgSend$seconds
+ _objc_msgSend$setAccountProperty:forKey:
+ _objc_msgSend$setBoolValue:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setCloudKitContainer:
+ _objc_msgSend$setCollectionIdentifier:
+ _objc_msgSend$setCommLimitsCollaborationSwitchForAltDSID:enableCollaboration:replyBlock:
+ _objc_msgSend$setCommLimitsMailAppSwitchForAltDSID:enableMailApp:replyBlock:
+ _objc_msgSend$setCreatedAt:
+ _objc_msgSend$setCredential:
+ _objc_msgSend$setDisplayStyle:
+ _objc_msgSend$setDoubleValue:
+ _objc_msgSend$setEnabled:
+ _objc_msgSend$setEnabled:forDataclass:
+ _objc_msgSend$setErrorMessage:
+ _objc_msgSend$setErrorTitle:
+ _objc_msgSend$setExpirationDate:
+ _objc_msgSend$setFetchLimit:
+ _objc_msgSend$setForceRefresh:
+ _objc_msgSend$setGroupIdentifier:
+ _objc_msgSend$setIdsCache:
+ _objc_msgSend$setInformativeText:
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setInvalidatedAt:
+ _objc_msgSend$setKey:
+ _objc_msgSend$setLearnMoreURL:
+ _objc_msgSend$setLimitType:
+ _objc_msgSend$setLowerbound:
+ _objc_msgSend$setMinDurationBetweenInstances:
+ _objc_msgSend$setPermission:
+ _objc_msgSend$setPostInstall:
+ _objc_msgSend$setPowerNap:
+ _objc_msgSend$setPredicate:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRecordZone:
+ _objc_msgSend$setRequiresBuddyComplete:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setRequiresInexpensiveNetworkConnectivity:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$setResourceIntensive:
+ _objc_msgSend$setResponse:
+ _objc_msgSend$setResponseType:
+ _objc_msgSend$setRole:
+ _objc_msgSend$setScheduleAfter:
+ _objc_msgSend$setShouldWakeDevice:
+ _objc_msgSend$setStatusCode:
+ _objc_msgSend$setStatusMessage:
+ _objc_msgSend$setStrictPolicy:
+ _objc_msgSend$setSuccess:
+ _objc_msgSend$setTargetAudience:
+ _objc_msgSend$setTargetBundleIdentifier:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setToken:
+ _objc_msgSend$setTrySchedulingBefore:
+ _objc_msgSend$setUniqueIdentifier:
+ _objc_msgSend$setUpdatedAt:
+ _objc_msgSend$setUpperbound:
+ _objc_msgSend$setUsername:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$share
+ _objc_msgSend$shareManagedObjects:toShare:completion:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$shortName
+ _objc_msgSend$shouldBadgeInvitee
+ _objc_msgSend$shouldBadgeOrganizer
+ _objc_msgSend$shouldWakeDevice
+ _objc_msgSend$signInUsername:onService:waitUntilRegistered:withCompletion:
+ _objc_msgSend$sourceProperty
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$statusCode
+ _objc_msgSend$statusMessage
+ _objc_msgSend$storeItemIdentifier
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$success
+ _objc_msgSend$targetAudience
+ _objc_msgSend$taskRequestForIdentifier:
+ _objc_msgSend$taskState
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$trySchedulingBefore
+ _objc_msgSend$type
+ _objc_msgSend$updateTaskRequest:error:
+ _objc_msgSend$updatedAt
+ _objc_msgSend$urlDestinationTo:params:error:
+ _objc_msgSend$userIdentity
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSend$zoneID
+ _objc_msgSend$zoneName
+ _objectdestroy.24Tm
+ _objectdestroy.66Tm
+ _sharedInstance.sCoalescer
+ _symbolic $s12FamilyCircle20CodableDefaultSourceP
+ _symbolic $s12FamilyCircle28FLFollowUpControllerProtocolP
+ _symbolic $ss11GlobalActorP
+ _symbolic $ss12CaseIterableP
+ _symbolic 5Value_____Qz 12FamilyCircle20CodableDefaultSourceP
+ _symbolic SDyS2SGSg
+ _symbolic SaySSGSg
+ _symbolic Say_____G 12FamilyCircle25InternalRegulatoryFeatureO
+ _symbolic So17NSPersistentStoreCyYaKc
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 12FamilyCircle06DeleteA5ErrorO
+ _symbolic _____ 12FamilyCircle08FADeleteA6ResultC
+ _symbolic _____ 12FamilyCircle14CodableDefaultO
+ _symbolic _____ 12FamilyCircle14CodableDefaultO7WrapperV
+ _symbolic _____ 12FamilyCircle16MemberRegionInfoV10CodingKeys33_51EBD72701D2FB0053076755A1090D02LLO
+ _symbolic _____ 12FamilyCircle19DefaultCachedAtDateO
+ _symbolic _____ 12FamilyCircle20DaemonContainerActorC
+ _symbolic _____ 12FamilyCircle20DefaultCacheDurationO
+ _symbolic _____ 12FamilyCircle25InternalRegulatoryFeatureO
+ _symbolic _____ 12FamilyCircle36SignificantChangeAckExtensionContextC
+ _symbolic _____ 12FamilyCircle36SignificantChangeAckExtensionContextC10CodingKeys33_E81F41A99E77DF7B41AE92997F36F657LLO
+ _symbolic _____Sg 12FamilyCircle16MemberRegionInfoV
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic ______pSg 12FamilyCircle28FLFollowUpControllerProtocolP
+ _symbolic _____y_____G s11_SetStorageC 12FamilyCircle25InternalRegulatoryFeatureO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12FamilyCircle16MemberRegionInfoV10CodingKeys33_51EBD72701D2FB0053076755A1090D02LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12FamilyCircle36SignificantChangeAckExtensionContextC10CodingKeys33_E81F41A99E77DF7B41AE92997F36F657LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12FamilyCircle16MemberRegionInfoV10CodingKeys33_51EBD72701D2FB0053076755A1090D02LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12FamilyCircle36SignificantChangeAckExtensionContextC10CodingKeys33_E81F41A99E77DF7B41AE92997F36F657LLO
+ _symbolic _____y______G 12FamilyCircle14CodableDefaultO7WrapperV AA0D12CachedAtDateO
+ _symbolic _____y______G 12FamilyCircle14CodableDefaultO7WrapperV AA0D13CacheDurationO
+ _symbolic _____y______GSg 12FamilyCircle14CodableDefaultO7WrapperV AA0D12CachedAtDateO
- -[FARequestConfigurator _akSigningController]
- _OBJC_CLASS_$_AKAppleIDSigningController
- _OBJC_IVAR_$_FARequestConfigurator._akSigningController
- ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.51
- ___121-[FAAgeRangeController requestAgeRangeWith:userAgeOverride:altDSID:bundleID:appName:attestedAtOverrideInDays:completion:]_block_invoke.51.cold.1
- ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31
- ___133-[FAAgeRangeController shouldPromptAgeRangeWith:bundleID:appName:privacyVersion:userAgeOverride:attestedAtOverrideInDays:completion:]_block_invoke.31.cold.1
- ___52-[FAAgeRangeController saveAgeRangeWith:completion:]_block_invoke.22
- ___52-[FAAgeRangeController saveAgeRangeWith:completion:]_block_invoke.22.cold.1
- ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.17
- ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.17.cold.1
- ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.19
- ___54-[FAAgeRangeController fetchAgeRangesWith:completion:]_block_invoke.19.cold.1
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.46
- ___54-[FAAgeRangeController fetchAgeWithCompletionHandler:]_block_invoke.46.cold.1
- ___54-[FAAgeRangeController updateAgeRangeWith:completion:]_block_invoke.24
- ___54-[FAAgeRangeController updateAgeRangeWith:completion:]_block_invoke.24.cold.1
- ___55-[FAAgeRangeController deleteAgeRangesWith:completion:]_block_invoke.20
- ___55-[FAAgeRangeController deleteAgeRangesWith:completion:]_block_invoke.20.cold.1
- ___55-[FAAgeRangeController fetchDSIDWithCompletionHandler:]_block_invoke.44
- ___55-[FAAgeRangeController fetchDSIDWithCompletionHandler:]_block_invoke.44.cold.1
- ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.26
- ___57-[FAAgeRangeController globalStateForAltDSID:completion:]_block_invoke.26.cold.1
- ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.41
- ___58-[FAAgeRangeController fetchAltDSIDWithCompletionHandler:]_block_invoke.41.cold.1
- ___59-[FADeleteFamilyRequest startRequestWithCompletionHandler:]_block_invoke.1
- ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.38
- ___63-[FAAgeRangeController fetchFamilyCircleWithCompletionHandler:]_block_invoke.38.cold.1
- ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.48
- ___65-[FAAgeRangeController fetchPrivacyVersionForAltDSID:completion:]_block_invoke.48.cold.1
- ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.54
- ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.54.cold.1
- ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.55
- ___65-[FAAgeRangeController getAgeVerificationInfoForDSID:completion:]_block_invoke.55.cold.1
- ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.28
- ___86-[FAAgeRangeController setGlobalStateForAltDSID:forAltDSID:privacyVersion:completion:]_block_invoke.28.cold.1
- ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.35
- ___92-[FAAgeRangeController postAgeRangeNotificationWith:lowerAgeBound:upperAgeBound:completion:]_block_invoke.35.cold.1
- ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.29
- ___99-[FAAgeRangeController saveAgeRangeGlobalState:forAltDSID:cacheDuration:privacyVersion:completion:]_block_invoke.29.cold.1
- ___swift_memcpy50_8
- _associated conformance So11FLItemGroupaSHSCSQ
- _associated conformance So11FLItemGroupas20_SwiftNewtypeWrapperSCSY
- _associated conformance So11FLItemGroupas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _associated conformance So16FLItemCollectionaSHSCSQ
- _associated conformance So16FLItemCollectionas20_SwiftNewtypeWrapperSCSY
- _associated conformance So16FLItemCollectionas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _block_copy_helper.23
- _block_copy_helper.28
- _block_copy_helper.29
- _block_copy_helper.35
- _block_copy_helper.41
- _block_copy_helper.44
- _block_copy_helper.50
- _block_copy_helper.54
- _block_copy_helper.62
- _block_copy_helper.68
- _block_copy_helper.76
- _block_descriptor.25
- _block_descriptor.30
- _block_descriptor.31
- _block_descriptor.37
- _block_descriptor.43
- _block_descriptor.46
- _block_descriptor.52
- _block_descriptor.56
- _block_descriptor.64
- _block_descriptor.70
- _block_descriptor.78
- _block_destroy_helper.24
- _block_destroy_helper.29
- _block_destroy_helper.30
- _block_destroy_helper.36
- _block_destroy_helper.42
- _block_destroy_helper.45
- _block_destroy_helper.51
- _block_destroy_helper.55
- _block_destroy_helper.63
- _block_destroy_helper.69
- _block_destroy_helper.77
- _keypath_getTm
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objectdestroy.21Tm
- _objectdestroy.65Tm
- _symbolic So17NSPersistentStoreCyKc
- _symbolic _____ So11FLItemGroupa
- _symbolic _____ So16FLItemCollectiona
- _symbolic _____y______SStG s23_ContiguousArrayStorageC So11DestinationV
- _symbolic xyKc
- _type_layout_string 12FamilyCircle16MemberRegionInfoV
CStrings:
+ "/Library/Caches/com.apple.xbs/7F519508-C888-4300-AEAE-060E98B087FC/TemporaryDirectory.HMiDZV/Sources/Family/FamilyCircle/Daemon/Shared/DaemonContainer.swift"
+ "@\"AAFPromise\"8@?0"
+ "@\"FARequestCoalescer\""
+ "@\"NSMutableDictionary\""
+ "@36@0:8@16B24@?28"
+ "AgeRangeEligibilityChecker.%s: eligible features: %s"
+ "AgeRangeEligibilityChecker.%s: failed to get eligibility result: %s"
+ "An unknown error occurred while deleting the family"
+ "Documents/FamilyCircle/AgeVerification_"
+ "FAChildAccountCutOffAgeRequest"
+ "FAChildAccountCutOffAgeResponse"
+ "FACoalescedRequest Queue"
+ "FADeleteFamilyRequest: Error from service - %@"
+ "FAFamilyCFUScheduler"
+ "FAFamilyFetchActivityScheduler"
+ "FAFamilySettings: _launchPrefsUsingDaemonWithOptions"
+ "FAParentalControlsRequest"
+ "FARequestCoalescer"
+ "Failed to decode MemberRegionInfo from dictionary: %@"
+ "FamilyCircle.FADeleteFamilyResult"
+ "RequestCoalescer - Executing block for key %@ force: %@ inFlightPromise: %@"
+ "RequestCoalescer - Returning already in flight promise for key %@ promise: %@"
+ "Sandbox override: %s"
+ "SignificantChangeAckExtensionContext { devDescription: "
+ "T@\"NSMutableDictionary\",&,N,V_inFlightRequests"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_coalesceQueue"
+ "Unable to create delete family request"
+ "_$observationRegistrar"
+ "_TtC12FamilyCircle20DaemonContainerActor"
+ "_TtC12FamilyCircle20FADeleteFamilyResult"
+ "_TtC12FamilyCircle36SignificantChangeAckExtensionContext"
+ "_coalesceQueue"
+ "_inFlightRequests"
+ "_requestCoalescer"
+ "ageAssuranceStringsMap"
+ "clearInviteCFU(followupControllerFactory:)"
+ "clearInviteCFU(followupControllerFactory:) Controller init failed"
+ "coalesceQueue"
+ "com.apple.FamilyExtensionHost.age-attestation"
+ "com.apple.Preferences"
+ "com.apple.family.SignificantChangeAckExtension"
+ "com.apple.family.deletefamily"
+ "com.apple.family.significantchange"
+ "declaredAgeRange"
+ "declaredAgeRangeDetailText"
+ "devDescription"
+ "eligibleRegulatoryFeatures"
+ "enforceRevokeAppAccess"
+ "getAgeVerificationInfo called with nil DSID."
+ "getAgeVerificationInfo-%@"
+ "getEligibleRegulatoryFeatures()"
+ "hostAppName"
+ "hostBundleIdentifier"
+ "inFlightRequests"
+ "initWithError:"
+ "initWithString:"
+ "launchAddMember"
+ "launchSetupFamily"
+ "onComplete:onQueue:"
+ "performBlockForKey:force:block:"
+ "sendInviteCFU(dateFactory:invitationDate:followupControllerFactory:)"
+ "sendInviteCFU(dateFactory:invitationDate:followupControllerFactory:) Controller init failed"
+ "sendInviteCFU(dateFactory:invitationDate:followupControllerFactory:) CoreFollowUp failed: %@"
+ "setCoalesceQueue:"
+ "setInFlightRequests:"
+ "setTargetBundleIdentifier:"
+ "significantAppChangeAdult"
+ "significantAppChangeChildOrTeen"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "/Library/Caches/com.apple.xbs/Sources/Family/FamilyCircle/Daemon/Shared/DaemonContainer.swift"
- "@\"AKAppleIDSigningController\""
- "AgeRangeEligibilityChecker.%s: failed to get eligibility result"
- "Omitting entire region defaults info as it was marked as UNKNOWN or nil"
- "_akSigningController"
- "clearInviteCFU()"
- "clearInviteCFU() Controller init failed"
- "sendInviteCFU(invitationDate:)"
- "sendInviteCFU(invitationDate:) Controller init failed"
- "sendInviteCFU(invitationDate:) CoreFollowUp failed: %@"

```
