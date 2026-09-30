## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.3.10.0.0
-  __TEXT.__text: 0x16b524
-  __TEXT.__auth_stubs: 0x2920
-  __TEXT.__objc_methlist: 0x12384
-  __TEXT.__cstring: 0x19b53
-  __TEXT.__const: 0x6548
-  __TEXT.__gcc_except_tab: 0x149c
-  __TEXT.__oslogstring: 0xda7b
+820.4.13.0.0
+  __TEXT.__text: 0x17f494
+  __TEXT.__auth_stubs: 0x28d0
+  __TEXT.__objc_methlist: 0x123fc
+  __TEXT.__cstring: 0x18900
+  __TEXT.__const: 0x6588
+  __TEXT.__gcc_except_tab: 0x1410
+  __TEXT.__oslogstring: 0xdb3b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__swift5_typeref: 0x1f7e
+  __TEXT.__swift5_typeref: 0x1f96
   __TEXT.__swift5_capture: 0x8c0
   __TEXT.__swift5_fieldmd: 0x171c
   __TEXT.__constg_swiftt: 0x18b4

   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_proto: 0x43c
+  __TEXT.__swift5_proto: 0x444
   __TEXT.__swift5_types: 0x1b0
   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x6590
-  __TEXT.__eh_frame: 0x5508
-  __TEXT.__objc_classname: 0x1ef7
-  __TEXT.__objc_methname: 0x273a1
-  __TEXT.__objc_methtype: 0x644a
-  __TEXT.__objc_stubs: 0x14f80
-  __DATA_CONST.__got: 0x1100
-  __DATA_CONST.__const: 0x60e0
+  __TEXT.__unwind_info: 0x7398
+  __TEXT.__eh_frame: 0x59f8
+  __TEXT.__objc_classname: 0x259d
+  __TEXT.__objc_methname: 0x286f5
+  __TEXT.__objc_methtype: 0x6b62
+  __TEXT.__objc_stubs: 0x15820
+  __DATA_CONST.__got: 0x1130
+  __DATA_CONST.__const: 0x6090
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8598
+  __DATA_CONST.__objc_selrefs: 0x85d8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x14a0
+  __AUTH_CONST.__auth_got: 0x1478
   __AUTH_CONST.__const: 0x59a0
-  __AUTH_CONST.__cfstring: 0x114a0
-  __AUTH_CONST.__objc_const: 0x24d40
+  __AUTH_CONST.__cfstring: 0x11520
+  __AUTH_CONST.__objc_const: 0x24e38
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x2cf8
-  __AUTH.__data: 0x1150
-  __DATA.__objc_ivar: 0x1058
-  __DATA.__data: 0x3b18
-  __DATA.__bss: 0x8490
+  __AUTH.__objc_data: 0x2c80
+  __AUTH.__data: 0x1128
+  __DATA.__objc_ivar: 0x105c
+  __DATA.__data: 0x3a80
+  __DATA.__bss: 0x8510
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x2b28
-  __DATA_DIRTY.__data: 0x520
-  __DATA_DIRTY.__bss: 0xb68
+  __DATA_DIRTY.__objc_data: 0x2ba0
+  __DATA_DIRTY.__data: 0x5f8
+  __DATA_DIRTY.__bss: 0xbf0
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FDF0C3A1-3693-32FE-A3E7-E18D13DFF603
-  Functions: 10872
-  Symbols:   24733
-  CStrings:  13674
+  UUID: 39837C50-3D7D-33A8-AF89-0ED5CA197CEA
+  Functions: 11011
+  Symbols:   25418
+  CStrings:  13652
 
Symbols:
+ -[ACAccountStore(GameCenter) _gkSaveCredential:completionHandler:].cold.4
+ -[GKDaemonProxy handleAMSRequest:selector:completion:delegateAction:]
+ -[GKDaemonProxy handleAMSRequest:selector:completion:delegateAction:].cold.1
+ -[GKDaemonProxy handleAMSRequest:selector:completion:delegateAction:].cold.2
+ -[GKDaemonProxy handleAMSRequest:selector:completion:delegateAction:].cold.3
+ -[GKDaemonProxy handleAMSRequest:selector:completion:delegateAction:].cold.4
+ -[GKDaemonProxy handleAuthenticationRequest:completion:]
+ -[GKDaemonProxy handleDialogRequest:completion:]
+ -[GKDaemonProxy handleEngagementRequest:completion:]
+ -[GKDispatchGroup .cxx_destruct]
+ -[GKInstallMetadata hasOptedOutOfKnowledgeGraph]
+ -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:hasOptedOutOfKnowledgeGraph:persistentRecordID:]
+ -[GKPlayerCredential(Nullability) nullableDSID]
+ GCC_except_table218
+ GCC_except_table267
+ _OBJC_CLASS_$_AMSAuthenticateRequest
+ _OBJC_CLASS_$_AMSAuthenticateResult
+ _OBJC_CLASS_$_AMSDialogRequest
+ _OBJC_CLASS_$_AMSDialogResult
+ _OBJC_CLASS_$_AMSEngagementRequest
+ _OBJC_CLASS_$_AMSEngagementResult
+ _OBJC_IVAR_$_GKInstallMetadata._hasOptedOutOfKnowledgeGraph
+ _OUTLINED_FUNCTION_183
+ _OUTLINED_FUNCTION_184
+ _OUTLINED_FUNCTION_185
+ _OUTLINED_FUNCTION_186
+ _OUTLINED_FUNCTION_187
+ _OUTLINED_FUNCTION_188
+ _OUTLINED_FUNCTION_189
+ _OUTLINED_FUNCTION_190
+ _OUTLINED_FUNCTION_191
+ _OUTLINED_FUNCTION_192
+ _OUTLINED_FUNCTION_193
+ _OUTLINED_FUNCTION_194
+ _OUTLINED_FUNCTION_195
+ _OUTLINED_FUNCTION_196
+ _OUTLINED_FUNCTION_197
+ _OUTLINED_FUNCTION_198
+ _OUTLINED_FUNCTION_199
+ _OUTLINED_FUNCTION_200
+ _OUTLINED_FUNCTION_201
+ _OUTLINED_FUNCTION_202
+ _OUTLINED_FUNCTION_203
+ _OUTLINED_FUNCTION_204
+ _OUTLINED_FUNCTION_205
+ _OUTLINED_FUNCTION_206
+ _OUTLINED_FUNCTION_207
+ _OUTLINED_FUNCTION_208
+ _OUTLINED_FUNCTION_209
+ _OUTLINED_FUNCTION_210
+ _OUTLINED_FUNCTION_211
+ _OUTLINED_FUNCTION_212
+ _OUTLINED_FUNCTION_213
+ _OUTLINED_FUNCTION_214
+ _OUTLINED_FUNCTION_215
+ _OUTLINED_FUNCTION_216
+ _OUTLINED_FUNCTION_217
+ _OUTLINED_FUNCTION_218
+ _OUTLINED_FUNCTION_219
+ _OUTLINED_FUNCTION_220
+ _OUTLINED_FUNCTION_221
+ _OUTLINED_FUNCTION_222
+ _OUTLINED_FUNCTION_223
+ _OUTLINED_FUNCTION_224
+ _OUTLINED_FUNCTION_225
+ _OUTLINED_FUNCTION_226
+ _OUTLINED_FUNCTION_227
+ _OUTLINED_FUNCTION_228
+ _OUTLINED_FUNCTION_229
+ _OUTLINED_FUNCTION_230
+ _OUTLINED_FUNCTION_231
+ _OUTLINED_FUNCTION_232
+ _OUTLINED_FUNCTION_233
+ _OUTLINED_FUNCTION_234
+ _OUTLINED_FUNCTION_235
+ _OUTLINED_FUNCTION_236
+ _OUTLINED_FUNCTION_237
+ _OUTLINED_FUNCTION_238
+ _OUTLINED_FUNCTION_239
+ _OUTLINED_FUNCTION_240
+ _OUTLINED_FUNCTION_241
+ _OUTLINED_FUNCTION_242
+ _OUTLINED_FUNCTION_243
+ _OUTLINED_FUNCTION_244
+ _OUTLINED_FUNCTION_245
+ _OUTLINED_FUNCTION_246
+ _OUTLINED_FUNCTION_247
+ _OUTLINED_FUNCTION_248
+ _OUTLINED_FUNCTION_249
+ _OUTLINED_FUNCTION_250
+ _OUTLINED_FUNCTION_251
+ _OUTLINED_FUNCTION_252
+ _OUTLINED_FUNCTION_253
+ _OUTLINED_FUNCTION_254
+ __OBJC_$_INSTANCE_METHODS_GKPlayerCredential(GKNillableShims|Nullability)
+ ___27-[GKDispatchGroup perform:]_block_invoke.9
+ ___27-[GKDispatchGroup perform:]_block_invoke.9.cold.1
+ ___36-[GKServiceProxy forwardInvocation:]_block_invoke.503
+ ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.12
+ ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.12.cold.1
+ ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.13
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.508
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.508.cold.1
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.509
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.806
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.807
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.807.cold.1
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.807.cold.2
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.807.cold.3
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.807.cold.4
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.807.cold.5
+ ___48-[GKDaemonProxy handleDialogRequest:completion:]_block_invoke
+ ___52-[GKDaemonProxy handleEngagementRequest:completion:]_block_invoke
+ ___56-[GKDaemonProxy handleAuthenticationRequest:completion:]_block_invoke
+ ___67-[GKServiceProxy replyToDuplicatesForRequest:withInvocation:queue:]_block_invoke.505
+ ___block_descriptor_40_e8_32s_e63_v24?0"<GKDaemonProxyDataUpdateDelegate>"8?<v?"NSError">16ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_61_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.195
+ _block_copy_helper.106
+ _block_copy_helper.178
+ _block_copy_helper.201
+ _block_copy_helper.75
+ _block_copy_helper.89
+ _block_descriptor.108
+ _block_descriptor.180
+ _block_descriptor.203
+ _block_descriptor.77
+ _block_descriptor.91
+ _block_destroy_helper.107
+ _block_destroy_helper.179
+ _block_destroy_helper.202
+ _block_destroy_helper.76
+ _block_destroy_helper.90
+ _objc_msgSend$__swift_objectForKeyedSubscript:
+ _objc_msgSend$__swift_setObject:forKeyedSubscript:
+ _objc_msgSend$_gkHasValidServerURLRequest
+ _objc_msgSend$_gkImageURLForSize:scale:
+ _objc_msgSend$accountType
+ _objc_msgSend$accountsWithAccountTypeIdentifier:
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$addSuccessBlock:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$compositeNameForFirstName:lastName:
+ _objc_msgSend$defaultTextModerator
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$elementType
+ _objc_msgSend$environmentForString:
+ _objc_msgSend$explanation
+ _objc_msgSend$fetchAppIconURLForBundleID:completionHandler:
+ _objc_msgSend$fetchImageForURL:gameKitDirectoryURLHint:completionHandler:
+ _objc_msgSend$fetchMetadataForGameKitDirectoryURL:completionHandler:
+ _objc_msgSend$forLocale:
+ _objc_msgSend$gameKitDirectoryServicePrivate
+ _objc_msgSend$gkSaveAccount:verify:withCompletion:
+ _objc_msgSend$handleAMSRequest:selector:completion:delegateAction:
+ _objc_msgSend$handleAuthenticationRequest:completion:
+ _objc_msgSend$handleDialogRequest:completion:
+ _objc_msgSend$handleEngagementRequest:completion:
+ _objc_msgSend$icons
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithLongLong:
+ _objc_msgSend$initWithTask:metrics:
+ _objc_msgSend$initWithUnit:
+ _objc_msgSend$initWithUnsignedInt:
+ _objc_msgSend$initialLimit
+ _objc_msgSend$inviteeCount
+ _objc_msgSend$isValid
+ _objc_msgSend$listGameKitDirectoriesForBundleID:completionHandler:
+ _objc_msgSend$loadURLEventPromiseWithContext:
+ _objc_msgSend$localeAgnosticTextModerator
+ _objc_msgSend$mainQueue
+ _objc_msgSend$minTimeBetweenAppearances
+ _objc_msgSend$monitorStatsUpdated:
+ _objc_msgSend$originalRequest
+ _objc_msgSend$processName
+ _objc_msgSend$recordLoadUrlMetrics:
+ _objc_msgSend$recordMultiplayerActivityMetrics:
+ _objc_msgSend$resetPeriod
+ _objc_msgSend$retryLimitHit
+ _objc_msgSend$revokePseudonym:completionHandler:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$sendGroupActivityInviteTo:participantID:pushToken:
+ _objc_msgSend$sendPingTo:sequence:
+ _objc_msgSend$sendPongTo:sequence:
+ _objc_msgSend$setAppleIDWithDSID:inUse:forService:
+ _objc_msgSend$setForCurrentProcessAllowingPDF:
+ _objc_msgSend$setGkIsSynchronous:
+ _objc_msgSend$setLanguage:
+ _objc_msgSend$setString:
+ _objc_msgSend$sharedSession
+ _objc_msgSend$shortDebugName
+ _objc_msgSend$showSharePlayMatchDeclinedToJoinAlertWithReason:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$targetWithPid:
+ _objc_msgSend$threadDictionary
+ _objc_msgSend$totalPlayerCount
+ _objc_msgSend$transportDidUpdateWithInfo:
+ _objc_msgSend$underlyingDictionary
+ _objc_release_x2
+ _objc_release_x3
+ _objectdestroy.142Tm
+ _objectdestroy.15Tm
+ _objectdestroy.50Tm
+ _objectdestroy.83Tm
+ _objectdestroy.88Tm
+ _secureCodedPropertyKeys.onceToken.284
+ _secureCodedPropertyKeys.sSecureCodedKeys.283
+ _swift_unknownObjectRelease_n
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____Sg_ABt 10Foundation6LocaleV
- -[GKDispatchGroup dealloc]
- -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:persistentRecordID:]
- GCC_except_table19
- GCC_except_table211
- GCC_except_table256
- __OBJC_$_INSTANCE_METHODS_GKPlayerCredential(GKNillableShims)
- ___23-[GKDispatchGroup wait]_block_invoke
- ___27-[GKDispatchGroup perform:]_block_invoke.11.cold.1
- ___27-[GKDispatchGroup perform:]_block_invoke.13
- ___36-[GKServiceProxy forwardInvocation:]_block_invoke.481
- ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.14
- ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.14.cold.1
- ___39-[GKDispatchGroup notifyOnQueue:block:]_block_invoke.15
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.487
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.487.cold.1
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.488
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.783
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.1
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.2
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.3
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.4
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.5
- ___67-[GKServiceProxy replyToDuplicatesForRequest:withInvocation:queue:]_block_invoke.484
- ___block_descriptor_48_e8_32b40b_e5_v8?0ls32l8s40l8
- ___block_descriptor_52_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32o40o48b_e14_v16?0?<v?>8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32o40o48b_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32o40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_61_e8_32o40b_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32o40o48o56b_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.178
- ___swift_coroFrameAllocStub
- _block_copy_helper.104
- _block_copy_helper.189
- _block_copy_helper.212
- _block_copy_helper.73
- _block_copy_helper.87
- _block_descriptor.106
- _block_descriptor.191
- _block_descriptor.214
- _block_descriptor.75
- _block_descriptor.89
- _block_destroy_helper.105
- _block_destroy_helper.190
- _block_destroy_helper.213
- _block_destroy_helper.74
- _block_destroy_helper.88
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x7
- _objectdestroy.14Tm
- _objectdestroy.164Tm
- _objectdestroy.49Tm
- _objectdestroy.94Tm
- _objectdestroy.99Tm
CStrings:
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKLocalPlayer.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatch.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchRequest.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchmaker.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKPlayer.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKSavedGameManager.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKTurnBasedMatch.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKCollectionUtils.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKDaemonProxy.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKInternalRepresentation.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKMatchmaker+Nearby.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUpdateGroup+NoARC.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils+FriendRequest.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/NSDictionary+GKImageAdditions.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/NSInvocation+GKAdditions+NoARC.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKCompositeTransport.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKTransportContext.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKMultiplayerServiceInterface.m"
+ "/Library/Caches/com.apple.xbs/82473E6B-6127-4661-BDED-7C4C52D58E2C/TemporaryDirectory.dt6nPw/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKServiceInterface.m"
+ "@124@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104B112@116"
+ "Delegating AMS %@ request to %@"
+ "GKDispatchGroup.m"
+ "Missing DSID on credential: %@"
+ "Must have a reply block to handle AMS %@ request."
+ "No delegate found to handle AMS %@ request."
+ "Nullability"
+ "Received AMS %@ request"
+ "T@\"NSString\",C,V_name"
+ "TB,R,N,V_hasOptedOutOfKnowledgeGraph"
+ "Vv32@0:8@\"AMSAuthenticateRequest\"16@?<v@?@\"AMSAuthenticateResult\"@\"NSError\">24"
+ "Vv32@0:8@\"AMSDialogRequest\"16@?<v@?@\"AMSDialogResult\"@\"NSError\">24"
+ "Vv32@0:8@\"AMSEngagementRequest\"16@?<v@?@\"AMSEngagementResult\"@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@?<v@?B>24"
+ "Vv48@0:8@16:24@?32@?40"
+ "Vv64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48B52@?<v@?@\"GKAuthenticateResponse\"@\"NSError\">56"
+ "Vv64@0:8@16@24@32@40B48B52@?56"
+ "_hasOptedOutOfKnowledgeGraph"
+ "authenticatePlayerWithUsername:password:altDSID:DSID:isGame:usingFastPath:handler:"
+ "authentication"
+ "dialog"
+ "engagement"
+ "handleAMSRequest:selector:completion:delegateAction:"
+ "handleAuthenticationRequest:completion:"
+ "handleDialogRequest:completion:"
+ "handleEngagementRequest:completion:"
+ "hasOptedOutOfKnowledgeGraph"
+ "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:hasOptedOutOfKnowledgeGraph:persistentRecordID:"
+ "launchOverlayForGameBundleId:completionHandler:"
+ "nullableDSID"
+ "v24@?0@\"<GKDaemonProxyDataUpdateDelegate>\"8@?<v@?@@\"NSError\">16"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKLocalPlayer.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatch.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchRequest.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKMatchmaker.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKPlayer.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKSavedGameManager.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/API/GKTurnBasedMatch.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKCollectionUtils.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKDaemonProxy.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKInternalRepresentation.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKMatchmaker+Nearby.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUpdateGroup+NoARC.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils+FriendRequest.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/GKUtils.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/NSDictionary+GKImageAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/NSInvocation+GKAdditions+NoARC.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKCompositeTransport.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/Transport/GKTransportContext.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKMultiplayerServiceInterface.m"
- "/Library/Caches/com.apple.xbs/Sources/GameCenter/Frameworks/GameCenterFoundation/gamed/GKServiceInterface.m"
- "@120@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104@112"
- "GKDispatchGroup+NoARC.m"
- "IllegalStateError"
- "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:persistentRecordID:"

```
