## BiometricKit

> `/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`

```diff

-511.100.15.0.0
-  __TEXT.__text: 0x4292c
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x2c64
-  __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x2b4e
-  __TEXT.__oslogstring: 0x47dd
-  __TEXT.__gcc_except_tab: 0xdc4
-  __TEXT.__unwind_info: 0x1088
+544.0.0.0.0
+  __TEXT.__text: 0x43a74
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0x2c9c
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x2c82
+  __TEXT.__oslogstring: 0x4e24
+  __TEXT.__gcc_except_tab: 0xdf4
+  __TEXT.__unwind_info: 0x10a0
   __TEXT.__objc_classname: 0x4e7
-  __TEXT.__objc_methname: 0x5d5f
-  __TEXT.__objc_methtype: 0x12ab
-  __TEXT.__objc_stubs: 0x38c0
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x848
+  __TEXT.__objc_methname: 0x5daf
+  __TEXT.__objc_methtype: 0x12ef
+  __TEXT.__objc_stubs: 0x3920
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1758
+  __DATA_CONST.__objc_selrefs: 0x1778
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x17e0
-  __AUTH_CONST.__objc_const: 0x5248
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__objc_const: 0x5250
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x820
+  __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA.__bss: 0x31
+  __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xa0
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71BE1B9B-353E-385E-A54F-74D6A1268EE4
-  Functions: 1500
-  Symbols:   4592
-  CStrings:  2218
+  UUID: 1E2DDD2A-101B-37B1-B172-A54EB312D67A
+  Functions: 1514
+  Symbols:   4587
+  CStrings:  2238
 
Symbols:
+ +[BiometricKitXPCClient clientUUID]
+ +[BiometricKitXPCClient clientUUID].cold.1
+ +[BiometricKitXPCClient clientUUID].cold.2
+ +[BiometricKitXPCClient clientUUID].cold.3
+ +[BiometricKitXPCClient clientUUID].cold.4
+ +[BiometricKitXPCClient clientUUID].cold.5
+ -[BKDevicePearl prewarmCamera:error:]
+ -[BKDevicePearl prewarmCamera:error:].cold.1
+ -[BiometricKitXPCClient prewarmCamera:]
+ -[BiometricKitXPCClient prewarmCamera:].cold.1
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table238
+ GCC_except_table246
+ GCC_except_table251
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table46
+ GCC_except_table96
+ GCC_except_table99
+ _ComponentSetUpdate.cold.26
+ _NSFileOwnerAccountName
+ _NSFileProtectionKey
+ _NSFileProtectionNone
+ ___39-[BiometricKitXPCClient prewarmCamera:]_block_invoke
+ ___39-[BiometricKitXPCClient prewarmCamera:]_block_invoke_2
+ ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.228
+ ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.230
+ ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.232
+ ___82+[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke.85.cold.2
+ ___block_descriptor_48_e8_32r40r_e8_v12?0i8lr32l8r40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8s64l8
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.316
+ ___block_literal_global.319
+ ___block_literal_global.327
+ ___block_literal_global.330
+ ___block_literal_global.334
+ ___block_literal_global.337
+ ___block_literal_global.341
+ ___block_literal_global.347
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.374
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.387
+ _backtrace
+ _backtrace_image_offsets
+ _objc_msgSend$clientUUID
+ _objc_msgSend$prewarmCamera:
+ _objc_msgSend$prewarmCamera:client:replyBlock:
+ _os_transaction_create
+ _uuid_compare
+ _uuid_copy
- GCC_except_table101
- GCC_except_table104
- GCC_except_table107
- GCC_except_table110
- GCC_except_table113
- GCC_except_table116
- GCC_except_table119
- GCC_except_table122
- GCC_except_table135
- GCC_except_table138
- GCC_except_table141
- GCC_except_table144
- GCC_except_table150
- GCC_except_table153
- GCC_except_table156
- GCC_except_table159
- GCC_except_table162
- GCC_except_table165
- GCC_except_table168
- GCC_except_table174
- GCC_except_table177
- GCC_except_table180
- GCC_except_table183
- GCC_except_table186
- GCC_except_table189
- GCC_except_table192
- GCC_except_table198
- GCC_except_table201
- GCC_except_table204
- GCC_except_table207
- GCC_except_table210
- GCC_except_table213
- GCC_except_table216
- GCC_except_table219
- GCC_except_table222
- GCC_except_table225
- GCC_except_table228
- GCC_except_table231
- GCC_except_table234
- GCC_except_table237
- GCC_except_table245
- GCC_except_table250
- GCC_except_table253
- GCC_except_table256
- GCC_except_table259
- GCC_except_table262
- GCC_except_table265
- GCC_except_table268
- GCC_except_table271
- GCC_except_table93
- GCC_except_table98
- ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.225
- ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.227
- ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.229
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.307
- ___block_literal_global.310
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.318
- ___block_literal_global.320
- ___block_literal_global.329
- ___block_literal_global.335
- ___block_literal_global.338
- ___block_literal_global.340
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.365
- ___block_literal_global.375
CStrings:
+ "([[NSFileManager defaultManager] createDirectoryAtPath:path withIntermediateDirectories:__objc_no attributes:@{ NSFileOwnerAccountName: @\"mobile\", NSFileProtectionKey: NSFileProtectionNone } error:((void*)0)])"
+ "B32@0:8Q16^@24"
+ "BKAccessory::isAuthorized: -> %d, authorized:%d, error:%@\n"
+ "BKAccessory::isConnected: -> %d, connected:%d, error:%@\n"
+ "BKAccessory:isAuthorized: %p (_cid:%lu)\n"
+ "BKAccessory:isConnected: %p (_cid:%lu)\n"
+ "BKAccessoryGroup::accessories (_cid:%lu)\n"
+ "BKAccessoryGroup::accessories -> %@, error:%@\n"
+ "BKAccessoryGroup::connectedAccessories (_cid:%lu)\n"
+ "BKAccessoryGroup::connectedAccessories -> %@, error:%@\n"
+ "BKClientUUID"
+ "BKDefaults::numberForKey: %@\n"
+ "BKDefaults::numberForKey: -> (%@: %@), error:%@\n"
+ "BKDefaults::setNumber:forKey: (%@: %@)\n"
+ "BKDefaults::setNumber:forKey: (%@: %@) -> %d, error:%@\n"
+ "BKDefaults::stringForKey: %@\n"
+ "BKDefaults::stringForKey: -> (%@: %@), error:%@\n"
+ "BKDevice::accessories (_cid:%lu)\n"
+ "BKDevice::accessories -> %@, error:%@\n"
+ "BKDevice::accessoryGroups (_cid:%lu)\n"
+ "BKDevice::accessoryGroups -> %@, error:%@\n"
+ "BKDevice::bioLockoutState:forUser: %p, %u (_cid:%lu)\n"
+ "BKDevice::bioLockoutState:forUser: -> %d, state:%ld, error:%@\n"
+ "BKDevice::biometryAvailability:forUser: %p, %u (_cid:%lu)\n"
+ "BKDevice::biometryAvailability:forUser: -> %d, info:%ld, error:%@\n"
+ "BKDevice::connectedAccessories (_cid:%lu)\n"
+ "BKDevice::connectedAccessories -> %@, error:%@\n"
+ "BKDevice::createEnrollOperation -> %@, error:%@\n"
+ "BKDevice::createMatchOperation -> %@, error:%@\n"
+ "BKDevice::createPresenceDetectOperation -> %@, error:%@\n"
+ "BKDevice::deviceHardwareState: %p (_cid:%lu)\n"
+ "BKDevice::deviceHardwareState: -> %d, state:%ld, error:%@\n"
+ "BKDevice::deviceWithDescriptor: -> %@ (_cid:%lu) %@\n"
+ "BKDevice::dropAllUnlockTokens (_cid:%lu)\n"
+ "BKDevice::dropAllUnlockTokens -> %d(err:0x%x), error:%@\n"
+ "BKDevice::effectiveProtectedConfigurationForUser: %u (_cid:%lu)\n"
+ "BKDevice::effectiveProtectedConfigurationForUser: -> %{public}@, error:%@\n"
+ "BKDevice::expressModeState:forUser: %p, %u (_cid:%lu)\n"
+ "BKDevice::expressModeState:forUser: -> %d, state:%ld, error:%@\n"
+ "BKDevice::extendedBioLockoutState:forUser: %p, %u (_cid:%lu)\n"
+ "BKDevice::extendedBioLockoutState:forUser: -> %d, state:%ld, error:%@\n"
+ "BKDevice::forceBioLockoutForAllUsers (_cid:%lu)\n"
+ "BKDevice::forceBioLockoutForUser: %u (_cid:%lu)\n"
+ "BKDevice::forceBioLockoutForUser: -> %d(err:0x%x), error:%@\n"
+ "BKDevice::forceBioLockoutIfLockedForUser: %u (_cid:%lu)\n"
+ "BKDevice::forceBioLockoutIfLockedForUser: -> %d(0x%x), error:%@\n"
+ "BKDevice::freeIdentityCountForUser: %u (_cid:%lu)\n"
+ "BKDevice::freeIdentityCountForUser: -> %ld, error:%@\n"
+ "BKDevice::freeIdentityCountForUser:accessoryGroup: %u (_cid:%lu)\n"
+ "BKDevice::freeIdentityCountForUser:accessoryGroup: -> %ld, error:%@\n"
+ "BKDevice::identities (_cid:%lu)\n"
+ "BKDevice::identities -> %lu: %{public}@, error:%@\n"
+ "BKDevice::identitiesDatabaseHashForUser: %u (_cid:%lu)\n"
+ "BKDevice::identitiesDatabaseHashForUser: -> %@, error:%@\n"
+ "BKDevice::identitiesDatabaseUUIDForUser: %u (_cid:%lu)\n"
+ "BKDevice::identitiesDatabaseUUIDForUser: -> %@, error:%@\n"
+ "BKDevice::identitiesForUser: %u (_cid:%lu)\n"
+ "BKDevice::identitiesForUser: -> %@, error:%@\n"
+ "BKDevice::identitiesForUser:accessoryGroup: %u, %@ (_cid:%lu)\n"
+ "BKDevice::identitiesForUser:accessoryGroup: -> %@, error:%@\n"
+ "BKDevice::identityForUUID: %@ (_cid:%lu)\n"
+ "BKDevice::identityForUUID: -> %@, error:%@\n"
+ "BKDevice::lastMatchEvent (_cid:%lu)\n"
+ "BKDevice::lastMatchEvent -> %@, error:%@\n"
+ "BKDevice::maxIdentityCount (_cid:%lu)\n"
+ "BKDevice::maxIdentityCount -> %ld, error:%@\n"
+ "BKDevice::protectedConfigurationForUser: %u (_cid:%lu)\n"
+ "BKDevice::protectedConfigurationForUser: -> %{public}@, error:%@\n"
+ "BKDevice::removeAllIdentitiesForUser:async: %u, %d (_cid:%lu)\n"
+ "BKDevice::removeAllIdentitiesForUser:async: -> reply(%d, %@)\n"
+ "BKDevice::removeAllIdentitiesForUser:async: -> void\n"
+ "BKDevice::removeIdentity:async: %@, %d (_cid:%lu)\n"
+ "BKDevice::removeIdentity:async: -> reply(%d, %@)\n"
+ "BKDevice::removeIdentity:async: -> void\n"
+ "BKDevice::setDelegate: %@\n"
+ "BKDevice::setDelegate: -> void\n"
+ "BKDevice::setProtectedConfiguration:forUser:credentialSet:async: %{public}@, %u, NSData(length:%lu), %d (_cid:%lu)\n"
+ "BKDevice::setProtectedConfiguration:forUser:credentialSet:async: -> reply(%d, %@)\n"
+ "BKDevice::setProtectedConfiguration:forUser:credentialSet:async: -> void\n"
+ "BKDevice::setString:forKey: (%@: %@)\n"
+ "BKDevice::setString:forKey: (%@: %@) -> %d, error:%@\n"
+ "BKDevice::setSystemProtectedConfiguration:credentialSet:async: %{public}@, NSData(length:%lu), %d (_cid:%lu)\n"
+ "BKDevice::setSystemProtectedConfiguration:credentialSet:async: -> reply(%d, %@)\n"
+ "BKDevice::setSystemProtectedConfiguration:credentialSet:async: -> void\n"
+ "BKDevice::statusMessage:details:client: matchEventOccurred:(result:%d, timeStamp:%llu) => delegate:%p(%@)\n"
+ "BKDevice::systemProtectedConfiguration (_cid:%lu)\n"
+ "BKDevice::systemProtectedConfiguration: -> %{public}@, error:%@\n"
+ "BKDevice::updateIdentity:async: %@, %d (_cid:%lu)\n"
+ "BKDevice::updateIdentity:async: -> reply(%d, %@)\n"
+ "BKDevice::updateIdentity:async: -> void\n"
+ "BKDeviceManager::availableDevicesWithFailure -> %@, failure:%d\n"
+ "BKDeviceManager::availableDevicesWithFailure: %p\n"
+ "BKDevicePearl::clearIdentityMigrationFailureForUser: %u (_cid:%lu)\n"
+ "BKDevicePearl::clearIdentityMigrationFailureForUser: -> %d, error:%@\n"
+ "BKDevicePearl::createEnrollOperation -> %@, error:%@\n"
+ "BKDevicePearl::createMatchOperation -> %@, error:%@\n"
+ "BKDevicePearl::createPresenceDetectOperation -> %@, error:%@\n"
+ "BKDevicePearl::deviceAvailableWithFailure: %p\n"
+ "BKDevicePearl::deviceAvailableWithFailure: -> %d, failure:%d\n"
+ "BKDevicePearl::periocularMatchState (_cid:%lu)\n"
+ "BKDevicePearl::periocularMatchState -> %@, error:%@\n"
+ "BKDevicePearl::periocularMatchStateForUser: %u (_cid:%lu)\n"
+ "BKDevicePearl::periocularMatchStateForUser: -> %@, error:%@\n"
+ "BKDevicePearl::prewarmCamera: %lu (_cid:%lu)\n"
+ "BKDevicePearl::prewarmCamera: -> %d, error:%@\n"
+ "BKDevicePearl::queryIdentityMigrationFailureForUser: %u (_cid:%lu)\n"
+ "BKDevicePearl::queryIdentityMigrationFailureForUser: -> %@, error:%@\n"
+ "BKDevicePearl::removePeriocularEnrollmentsForUser:identityUUID:removeAll:async: %u, %@, %d, %d (_cid:%lu)\n"
+ "BKDevicePearl::removePeriocularEnrollmentsForUser:identityUUID:removeAll:async: -> reply(%d, %@)\n"
+ "BKDevicePearl::removePeriocularEnrollmentsForUser:identityUUID:removeAll:async: -> void\n"
+ "BKDevicePearl::setTemplate:forIdentity: -> %d, error:%@\n"
+ "BKDevicePearl::setTemplate:forIdentity: NSData(length:%lu), %p (_cid:%lu)\n"
+ "BKDevicePearl::statusMessage:client: %u, %llu\n"
+ "BKDevicePearl::statusMessage:client: -> void\n"
+ "BKDevicePearl::supportsPeriocularEnrollment (_cid:%lu)\n"
+ "BKDevicePearl::supportsPeriocularEnrollment -> %@, error:%@\n"
+ "BKDeviceTouchID::createEnrollOperation -> %@, error:%@\n"
+ "BKDeviceTouchID::createExtendEnrollTouchIDOperation\n"
+ "BKDeviceTouchID::createExtendEnrollTouchIDOperation -> %@, error:%@\n"
+ "BKDeviceTouchID::createMatchOperation -> %@, error:%@\n"
+ "BKDeviceTouchID::createPresenceDetectOperation -> %@, error:%@\n"
+ "BKDeviceTouchID::deviceAvailableWithFailure: %p\n"
+ "BKDeviceTouchID::deviceAvailableWithFailure: -> %d, failure:%d\n"
+ "BKDeviceTouchID::enableBackgroundFingerDetection: %d (_cid:%lu)\n"
+ "BKDeviceTouchID::enableBackgroundFingerDetection: -> %d(err:0x%x), error:%@\n"
+ "BKEnrollOperation::enrollResult:details:client: %p(%@), %p, %llu\n"
+ "BKEnrollOperation::enrollResult:details:client: -> void\n"
+ "BKEnrollOperation::processEnrollFailReason: %ld => delegate:%p(%@)\n"
+ "BKEnrollOperation::startBioOperation: -> void\n"
+ "BKEnrollOperation::startBioOperation: async:%d (_cid:%lu)\n"
+ "BKEnrollOperation::statusMessage:details:client: %u, %p, %llu (_cid:%lu)\n"
+ "BKEnrollOperation::statusMessage:details:client: -> void\n"
+ "BKEnrollOperation::statusMessage:details:client: percentCompleted:%ld => delegate:%p(%@)\n"
+ "BKEnrollPearlOperation::enrollUpdate: progressedWithInfo:(percentageCompleted:%ld, enrolledPoses:%@) => delegate:%p(%@)\n"
+ "BKEnrollPearlOperation::enrollUpdate:client: percentCompleted:%ld => delegate:%p(%@)\n"
+ "BKEnrollPearlOperation::statusMessage:client: %u, %llu\n"
+ "BKEnrollPearlOperation::statusMessage:client: -> void\n"
+ "BKEnrollPearlOperation::statusMessage:client: faceDetectStateChanged:%d => delegate:%p(%@)\n"
+ "BKEnrollPearlOperation::statusMessage:client: failedWithReason:%ld => delegate:%p(%@)\n"
+ "BKEnrollPearlOperation::statusMessage:client: progressedWithInfo:%ld => delegate:%p(%@)\n"
+ "BKEnrollPearlOperation:complete (_cid:%lu)\n"
+ "BKEnrollPearlOperation:complete -> %d, error:%@\n"
+ "BKEnrollPearlOperation:resume (_cid:%lu)\n"
+ "BKEnrollPearlOperation:resume -> %d, error:%@\n"
+ "BKEnrollPearlOperation:start (_cid:%lu)\n"
+ "BKEnrollPearlOperation:start -> %d, error:%@\n"
+ "BKEnrollPearlOperation:suspend (_cid:%lu)\n"
+ "BKEnrollPearlOperation:suspend -> %d, error:%@\n"
+ "BKEnrollResultInfo::initWithServerIdentity:details:device: %@, %@, %@\n"
+ "BKEnrollTouchIDOperation::homeButtonPressed: clientID:%llu\n"
+ "BKEnrollTouchIDOperation::homeButtonPressed: homeButtonPressedInEnrollOperation => delegate:%p(%@)\n"
+ "BKEnrollTouchIDOperation::statusMessage:client: %u, %llu\n"
+ "BKEnrollTouchIDOperation::statusMessage:client: -> void\n"
+ "BKEnrollTouchIDOperation::statusMessage:client: encounteredCaptureError:%ld => delegate:%p(%@)\n"
+ "BKExtendEnrollTouchIDOperation::homeButtonPressed: clientID:%llu\n"
+ "BKExtendEnrollTouchIDOperation::homeButtonPressed: homeButtonPressedInEnrollOperation => delegate:%p(%@)\n"
+ "BKExtendEnrollTouchIDOperation::matchResult:client: hasUpdated:%d => delegate:%p(%@)\n"
+ "BKExtendEnrollTouchIDOperation::matchResult:withDictionary:client: %p(%@), %p, %llu\n"
+ "BKExtendEnrollTouchIDOperation::matchResult:withDictionary:client: -> void\n"
+ "BKExtendEnrollTouchIDOperation::startBioOperation: -> void\n"
+ "BKExtendEnrollTouchIDOperation::startBioOperation: async:%d (_cid:%lu)\n"
+ "BKExtendEnrollTouchIDOperation::statusMessage:client: %u, %llu\n"
+ "BKExtendEnrollTouchIDOperation::statusMessage:client: -> void\n"
+ "BKExtendEnrollTouchIDOperation::statusMessage:client: encounteredCaptureError:%ld => delegate:%p(%@)\n"
+ "BKFaceDetectOperation::startBioOperation: -> void\n"
+ "BKFaceDetectOperation::startBioOperation: async:%d (_cid:%lu)\n"
+ "BKFaceDetectOperation::statusMessage:details:client: %u, %p, %llu\n"
+ "BKFaceDetectOperation::statusMessage:details:client: -> void\n"
+ "BKFaceDetectOperation::statusMessage:details:client: faceDetectStateChanged:%d => delegate:%p(%@)\n"
+ "BKFaceDetectOperation::statusMessage:details:client: motionDetectStateChanged => delegate:%p(%@)\n"
+ "BKMatchOperation::matchResult:withDictionary:client: %p(%@), %p(LockoutState:%d,Unlocked:%d,CredentialAdded:%d,Ignored:%d), %llu\n"
+ "BKMatchOperation::matchResult:withDictionary:client: -> void\n"
+ "BKMatchOperation::processMatchFailReason: %ld => delegate:%p(%@)\n"
+ "BKMatchOperation::startBioOperation: -> void\n"
+ "BKMatchOperation::startBioOperation: async:%d (_cid:%lu)\n"
+ "BKMatchOperation::statusMessage:client: %u, %llu (_cid:%lu)\n"
+ "BKMatchOperation::statusMessage:client: -> void\n"
+ "BKMatchPearlOperation::enableAutoRetry -> %d(err:0x%x), error:%@\n"
+ "BKMatchPearlOperation::enableAutoRetry: %d (_cid:%lu)\n"
+ "BKMatchPearlOperation::pauseFaceDetectTimer -> %d(err:0x%x), error:%@\n"
+ "BKMatchPearlOperation::pauseFaceDetectTimer: %d (_cid:%lu)\n"
+ "BKMatchPearlOperation::startNewMatchAttempt (_cid:%lu)\n"
+ "BKMatchPearlOperation::startNewMatchAttempt -> %d(err:0x%x), error:%@\n"
+ "BKMatchPearlOperation::statusMessage:details:client: %u, %@, %llu\n"
+ "BKMatchPearlOperation::statusMessage:details:client: -> void\n"
+ "BKMatchPearlOperation::statusMessage:details:client: faceDetectStateChanged:%d => delegate:%p(%@)\n"
+ "BKMatchPearlOperation::statusMessage:details:client: failedWithReason:%ld => delegate:%p(%@)\n"
+ "BKMatchPearlOperation::statusMessage:details:client: providedFaceOcclusionInfo:(hasFaceOcclusion:%d) => delegate:%p(%@)\n"
+ "BKMatchPearlOperation::statusMessage:details:client: providedFaceWUPoseEligibilityInfo:(isEligible:%d) => delegate:%p(%@)\n"
+ "BKMatchPearlOperation::statusMessage:details:client: providedFeedback:%ld => delegate:%p(%@)\n"
+ "BKMatchPearlOperation::statusMessage:details:client: requestedPasscodeShortcutWithReason:(reason:%ld) => delegate:%p(%@)\n"
+ "BKMatchResultInfo::initWithServerIdentity:details:device: %@, %@, %@\n"
+ "BKMatchTouchIDOperation::statusMessage:client: %u, %llu\n"
+ "BKMatchTouchIDOperation::statusMessage:client: -> void\n"
+ "BKMatchTouchIDOperation::statusMessage:client: encounteredCaptureError:%ld => delegate:%p(%@)\n"
+ "BKOperation::cancel (_cid:%lu)\n"
+ "BKOperation::changeState: %ld\n"
+ "BKOperation::changeState: -> void\n"
+ "BKOperation::initWithDevice: %@\n"
+ "BKOperation::initWithDevice: -> %@ (_cid:%lu)\n"
+ "BKOperation::operationEndsWithReason: %ld (_cid:%lu)\n"
+ "BKOperation::setDelegate: %@ (_cid:%lu)\n"
+ "BKOperation::setDelegate: -> void\n"
+ "BKOperation::startOperation: -> reply(%d, %@)\n"
+ "BKOperation::startOperation: -> void\n"
+ "BKOperation::startOperation: async:%d)\n"
+ "BKOperation::statusMessage:client: %u, client:%llu\n"
+ "BKOperation::statusMessage:client: -> void\n"
+ "BKOperation::userPresent (_cid:%lu)\n"
+ "BKOperation::userPresent -> %d, error:%@\n"
+ "BKPresenceDetectOperation::startBioOperation: -> void\n"
+ "BKPresenceDetectOperation::startOperation: async:%d (_cid:%lu)\n"
+ "BiometricKitXPCClient::interruptConnection (_cid:%lu)\n"
+ "BiometricKitXPCClient::xpcConnection interrupted\n"
+ "BiometricKitXPCClient::xpcConnection invalidated\n"
+ "BiometricKitXPCClient::xpcConnection processing kBiometricKitServerStartedNotification\n"
+ "Please adopt new BiometricKit entitlements (see rdar://105770455 for additional details), client UUID %@\n"
+ "clientUUID"
+ "createMatchInfo:withTopology:withMatchImage: %p(%@), %p, %p\n"
+ "createMatchInfo:withTopology:withMatchImage: -> %p(%@)\n"
+ "detectFingerWithOptions: -> err:0x%x\n"
+ "diagnostics:withOptions:passed:withDetails: %d, %@, %p, %p\n"
+ "diagnostics:withOptions:passed:withDetails: -> err:0x%x, passed:%d, details:%@\n"
+ "dropUnlockToken -> err:0x%x\n"
+ "enableBackgroundFdet: -> err:0x%x\n"
+ "enroll:forUser:withOptions: %d, %u, %p(EnrollWCS:%p,EnrollWAT:%p,AuthWCS:%p,AuthWAT:%p)\n"
+ "enroll:forUser:withOptions: -> err:0x%x\n"
+ "forceBioLockoutForUser: %u\n"
+ "forceBioLockoutForUser: -> err:0x%x\n"
+ "getBioLockoutStateForUser: %u\n"
+ "getCountersignedStoreToken: -> err:0x%x, token:NSData(length: %ld)\n"
+ "getFreeIdentityCount:forUser: %d, %u\n"
+ "getIdentitiesDatabaseHashForUser: %u\n"
+ "getIdentitiesDatabaseHashForUser: -> NSData(length: %lu)\n"
+ "getIdentitiesDatabaseUUIDForUser: %u\n"
+ "getIdentityFromUUID: -> %p(%@)\n"
+ "getProtectedConfigurationForUser: %u\n"
+ "getTemplateInfo: -> %p(%@)\n"
+ "i + 1 < stackSize"
+ "i24@0:8Q16"
+ "imageOffsets"
+ "isEphemeralMultiUser: %u\n"
+ "isFaceIDPlatform: %u\n"
+ "isTouchIDAvailableWithInfo: -> %d, info:%ld\n"
+ "isTouchIDPlatformWithFailure -> %u, failure:%d\n"
+ "isTouchIDPlatformWithFailure(%p)\n"
+ "match: --> match:withOptions:\n"
+ "match:withOptions: %@, %p(AuthWCS:%p,MatchCSFEE:%p,AuthWAT:%p,MatchATFEE:%p,MatchATTBPB:%p,MatchFCS:%p,Priority:%d,MatchFEE:%d,MatchFPA:%d,MatchFU:%d,MatchFMP:%d,MatchFMC:%d,MatchBPB:%d,MatchSOS:%d,MatchCO:%d,MatchGBB:%d,FilterOutHBE:%d,SuppressHF:%d)\n"
+ "match:withOptions: -> err:0x%x\n"
+ "prewarmCamera:"
+ "prewarmCamera:client:replyBlock:"
+ "prewarmCamera:error:"
+ "registerDSID:withAuthToken: (x), %p\n"
+ "registerDSID:withAuthToken: -> err:0x%x\n"
+ "registerDSID:withOptions: (x), %p(AuthWCS:%p,AuthWAT:%p)\n"
+ "registerDSID:withOptions: -> err:0x%x\n"
+ "registerStoreToken: -> err:0x%x\n"
+ "registerStoreToken: NSData(length: %lu)\n"
+ "removeAllIdentitiesForUser:withOptions: %d, %@\n"
+ "removeAllIdentitiesForUser:withOptions: -> err:0x%x\n"
+ "removeAllIdentitiesForUser:withOptions:withReply: %d, %@\n"
+ "removeIdentity: --> removeIdentity:withOptions:\n"
+ "removeIdentity:withOptions: %p(%@), %@\n"
+ "removeIdentity:withOptions: -> err:0x%x\n"
+ "removeIdentity:withOptions:withReply: %p(%@), %@\n"
+ "resetAppleConnectCounter -> err:0x%x\n"
+ "setProtectedConfiguration:forUser:withOptions: %p(UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,ApplePayEnabled:%d,EfUnlockEnabled:%d,EfIdentificationEnabled:%d,EfLoginEnabled:%d,EfApplePayEnabled:%d), %u, %p(AuthWCS:%p,AuthWAT:%p))\n"
+ "setProtectedConfiguration:forUser:withOptions: -> err:0x%x\n"
+ "setProtectedConfiguration:forUser:withOptions:withReply: %p(UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,ApplePayEnabled:%d,EfUnlockEnabled:%d,EfIdentificationEnabled:%d,EfLoginEnabled:%d,EfApplePayEnabled:%d), %u, %p(AuthWCS:%p,AuthWAT:%p))\n"
+ "setProtectedConfiguration:withAuthToken: %p(UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,ApplePayEnabled:%d,EfUnlockEnabled:%d,EfIdentificationEnabled:%d,EfLoginEnabled:%d,EfApplePayEnabled:%d), %p\n"
+ "setProtectedConfiguration:withAuthToken: -> err:0x%x\n"
+ "setSystemProtectedConfiguration:forUser:withOptions: %p(TouchIDEnabled:%d,UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,UnlockTokenMaxLifetime:%d), %p(AuthWCS:%p,AuthWAT:%p))\n"
+ "setSystemProtectedConfiguration:withOptions: -> err:0x%x\n"
+ "setUserDSID:withAuthToken: (x), %p\n"
+ "setUserDSID:withAuthToken: -> err:0x%x\n"
+ "setUserDSID:withOptions: (x), %p(AuthWCS:%p,AuthWAT:%p)\n"
+ "setUserDSID:withOptions: -> err:0x%x\n"
+ "stack"
+ "stackSize <= MAX_BACKTRACE_LENGTH"
+ "stackSize > 0"
+ "statusMessage: %u\n"
+ "updateCallback(observer:%p)\n"
+ "updateIdentity:withOptions: %p(%@), %@\n"
+ "updateIdentity:withOptions: -> err:0x%x\n"
+ "updateIdentity:withOptions:withReply: %p(%@), %@\n"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?i>32"
- "BKAccessory::isAuthorized: -> %u %@\n"
- "BKAccessory::isConnected: -> %u %@\n"
- "BKAccessory:isAuthorized: (_cid %lu)\n"
- "BKAccessory:isConnected: (_cid %lu)\n"
- "BKAccessoryGroup::accessoriesWithError: (_cid %lu)\n"
- "BKAccessoryGroup::accessoriesWithError: -> %@ %@\n"
- "BKAccessoryGroup::connectedAccessoriesWithError: (_cid %lu)\n"
- "BKAccessoryGroup::connectedAccessoriesWithError: -> %@ %@\n"
- "BKDevice::accessoriesWithError: (_cid %lu)\n"
- "BKDevice::accessoriesWithError: -> %@ %@\n"
- "BKDevice::accessoryGroupsWithError: (_cid %lu)\n"
- "BKDevice::accessoryGroupsWithError: -> %@ %@\n"
- "BKDevice::bioLockoutState:forUser: %p %d (_cid %lu)\n"
- "BKDevice::bioLockoutState:forUser: -> %d %ld %@\n"
- "BKDevice::biometryAvailability:forUser: %p %d (_cid %lu)\n"
- "BKDevice::biometryAvailability:forUser: -> %d %ld %@\n"
- "BKDevice::connectedAccessoriesWithError: (_cid %lu)\n"
- "BKDevice::connectedAccessoriesWithError: -> %@ %@\n"
- "BKDevice::createEnrollOperation -> %@ %@\n"
- "BKDevice::createMatchOperation -> %@ %@\n"
- "BKDevice::createPresenceDetectOperation -> %@ %@\n"
- "BKDevice::deviceHardwareState: %p (_cid %lu)\n"
- "BKDevice::deviceHardwareState: -> %d %ld %@\n"
- "BKDevice::deviceWithDescriptor: -> %@ (_cid %lu) %@\n"
- "BKDevice::dropAllUnlockTokens (_cid %lu)\n"
- "BKDevice::dropAllUnlockTokens -> %d(%{errno}d) %@\n"
- "BKDevice::effectiveProtectedConfigurationForUser: %d (_cid %lu)\n"
- "BKDevice::effectiveProtectedConfigurationForUser: -> %{public}@\n"
- "BKDevice::expressModeState:forUser: %p %d (_cid %lu)\n"
- "BKDevice::expressModeState:forUser: -> %d %ld %@\n"
- "BKDevice::extendedBioLockoutState:forUser: %p %d (_cid %lu)\n"
- "BKDevice::extendedBioLockoutState:forUser: -> %d %ld %@\n"
- "BKDevice::forceBioLockoutForAllUsers (_cid %lu)\n"
- "BKDevice::forceBioLockoutForUser: %d (_cid %lu)\n"
- "BKDevice::forceBioLockoutForUser: -> %d(%{errno}d) %@\n"
- "BKDevice::forceBioLockoutIfLockedForUser: %d (_cid %lu)\n"
- "BKDevice::forceBioLockoutIfLockedForUser: -> %d(%{errno}d) %@\n"
- "BKDevice::freeIdentityCountForUser: %d (_cid %lu)\n"
- "BKDevice::freeIdentityCountForUser: -> %ld %@\n"
- "BKDevice::freeIdentityCountForUser:accessoryGroup: %d (_cid %lu)\n"
- "BKDevice::freeIdentityCountForUser:accessoryGroup: -> %ld %@\n"
- "BKDevice::identities (_cid %lu)\n"
- "BKDevice::identities -> %lu: %{public}@ %@\n"
- "BKDevice::identitiesDatabaseHashForUser: %d (_cid %lu)\n"
- "BKDevice::identitiesDatabaseHashForUser: -> %@ %@\n"
- "BKDevice::identitiesDatabaseUUIDForUser: %d (_cid %lu)\n"
- "BKDevice::identitiesDatabaseUUIDForUser: -> %@ %@\n"
- "BKDevice::identitiesForUser: %d (_cid %lu)\n"
- "BKDevice::identitiesForUser: -> %@ %@\n"
- "BKDevice::identitiesForUser:accessoryGroup: %d %@ (_cid %lu)\n"
- "BKDevice::identitiesForUser:accessoryGroup: -> %@ %@\n"
- "BKDevice::identityForUUID: %@ (_cid %lu)\n"
- "BKDevice::identityForUUID: -> %@ %@\n"
- "BKDevice::lastMatchEventWithError: (_cid %lu)\n"
- "BKDevice::lastMatchEventWithError: -> %@ %@\n"
- "BKDevice::maxIdentityCount (_cid %lu)\n"
- "BKDevice::maxIdentityCount -> %ld %@\n"
- "BKDevice::numberForKey:%@\n"
- "BKDevice::numberForKey:%@ -> %@ %@\n"
- "BKDevice::protectedConfigurationForUser: %d (_cid %lu)\n"
- "BKDevice::protectedConfigurationForUser: -> %{public}@\n"
- "BKDevice::removeAllIdentitiesForUser: %d (async %u, _cid %lu)\n"
- "BKDevice::removeAllIdentitiesForUser: -> reply(%d, %@)\n"
- "BKDevice::removeAllIdentitiesForUser: -> void\n"
- "BKDevice::removeIdentity: %@ (async %u, _cid %lu)\n"
- "BKDevice::removeIdentity: -> reply(%d, %@)\n"
- "BKDevice::removeIdentity: -> void\n"
- "BKDevice::setDelegate %@\n"
- "BKDevice::setDelegate -> void\n"
- "BKDevice::setNumber:%@ forKey:%@\n"
- "BKDevice::setNumber:%@ forKey:%@ -> %d %@\n"
- "BKDevice::setProtectedConfiguration:forUser:credentialSet: %{public}@ %d %p (async %u, _cid %lu)\n"
- "BKDevice::setProtectedConfiguration:forUser:credentialSet: -> reply(%d, %@)\n"
- "BKDevice::setProtectedConfiguration:forUser:credentialSet: -> void\n"
- "BKDevice::setString:%@ forKey:%@\n"
- "BKDevice::setString:%@ forKey:%@ -> %d %@\n"
- "BKDevice::setSystemProtectedConfiguration:credentialSet: %{public}@ %p (async %u, _cid %lu)\n"
- "BKDevice::setSystemProtectedConfiguration:credentialSet: -> reply(%d, %@)\n"
- "BKDevice::setSystemProtectedConfiguration:credentialSet: -> void\n"
- "BKDevice::statusMessage: %p(%@) matchEventOccurred: result=%u, timeStamp=%llu\n"
- "BKDevice::stringForKey:%@\n"
- "BKDevice::stringForKey:%@ -> %@ %@\n"
- "BKDevice::systemProtectedConfiguration (_cid %lu)\n"
- "BKDevice::systemProtectedConfiguration: -> %{public}@\n"
- "BKDevice::updateIdentity: %@ (async %u, _cid %lu)\n"
- "BKDevice::updateIdentity: -> reply(%d, %@)\n"
- "BKDevice::updateIdentity: -> void\n"
- "BKDeviceManager::availableDevicesWithFailure\n"
- "BKDeviceManager::availableDevicesWithFailure -> %@ (%u)\n"
- "BKDevicePearl::clearIdentityMigrationFailureForUser -> %d %@\n"
- "BKDevicePearl::clearIdentityMigrationFailureForUser: %u (_cid %lu)\n"
- "BKDevicePearl::createEnrollOperation -> %@ %@\n"
- "BKDevicePearl::createMatchOperation -> %@ %@\n"
- "BKDevicePearl::createPresenceDetectOperation -> %@ %@\n"
- "BKDevicePearl::deviceAvailableWithFailure\n"
- "BKDevicePearl::deviceAvailableWithFailure -> %d\n"
- "BKDevicePearl::periocularMatchStateForUser %u (_cid %lu)\n"
- "BKDevicePearl::periocularMatchStateForUser -> %@ %@\n"
- "BKDevicePearl::periocularMatchStateWithError (_cid %lu)\n"
- "BKDevicePearl::periocularMatchStateWithError -> %@ %@\n"
- "BKDevicePearl::queryIdentityMigrationFailureForUser -> %@ %@\n"
- "BKDevicePearl::queryIdentityMigrationFailureForUser: %u (_cid %lu)\n"
- "BKDevicePearl::removePeriocularEnrollmentsForUser: -> void\n"
- "BKDevicePearl::removePeriocularEnrollmentsForUser:%u identityUUID:%@ removeAll:%u (async %u, _cid %lu)\n"
- "BKDevicePearl::removePeriocularEnrollmentsFromIdentity: -> reply(%d, %@)\n"
- "BKDevicePearl::setTemplate (_cid %lu)\n"
- "BKDevicePearl::setTemplate -> %d %@\n"
- "BKDevicePearl::statusMessage: %u\n"
- "BKDevicePearl::statusMessage: -> void\n"
- "BKDevicePearl::supportsPeriocularEnrollmentWithError (_cid %lu)\n"
- "BKDevicePearl::supportsPeriocularEnrollmentWithError -> %@ %@\n"
- "BKDeviceTouchID::createEnrollOperation -> %@ %@\n"
- "BKDeviceTouchID::createExtendEnrollTouchIDOperationWithError\n"
- "BKDeviceTouchID::createExtendEnrollTouchIDOperationWithError -> %@ %@\n"
- "BKDeviceTouchID::createMatchOperation -> %@ %@\n"
- "BKDeviceTouchID::createPresenceDetectOperation -> %@ %@\n"
- "BKDeviceTouchID::deviceAvailableWithFailure\n"
- "BKDeviceTouchID::deviceAvailableWithFailure -> %d (%u)\n"
- "BKDeviceTouchID::enableBackgroundFingerDetection: %d (_cid %lu)\n"
- "BKDeviceTouchID::enableBackgroundFingerDetection: -> %d %{errno}d %@\n"
- "BKEnrollOperation::enrollResult %p(%@)\n"
- "BKEnrollOperation::enrollResult -> void\n"
- "BKEnrollOperation::processEnrollFailReason: %p(%@) failedWithReason: %ld\n"
- "BKEnrollOperation::startBioOperation (_cid %lu)\n"
- "BKEnrollOperation::startBioOperation -> void\n"
- "BKEnrollOperation::statusMessage: %p(%@) percentCompleted: %ld\n"
- "BKEnrollOperation::statusMessage: %u (_cid %lu)\n"
- "BKEnrollOperation::statusMessage: -> void\n"
- "BKEnrollPearlOperation::enrollUpdate: %p(%@) percentCompleted: %ld\n"
- "BKEnrollPearlOperation::enrollUpdate: %p(%@) progressedWithInfo: percentageCompleted=%ld enrolledPoses=%@\n"
- "BKEnrollPearlOperation::statusMessage: %p(%@) faceDetectStateChanged: %d\n"
- "BKEnrollPearlOperation::statusMessage: %p(%@) failedWithReason: %ld\n"
- "BKEnrollPearlOperation::statusMessage: %p(%@) progressedWithInfo: %ld\n"
- "BKEnrollPearlOperation::statusMessage: %u\n"
- "BKEnrollPearlOperation::statusMessage: -> void\n"
- "BKEnrollPearlOperation:complete (_cid %lu)\n"
- "BKEnrollPearlOperation:complete -> %d %@\n"
- "BKEnrollPearlOperation:resume (_cid %lu)\n"
- "BKEnrollPearlOperation:resume -> %d %@\n"
- "BKEnrollPearlOperation:start (_cid %lu)\n"
- "BKEnrollPearlOperation:start -> %d %@\n"
- "BKEnrollPearlOperation:suspend (_cid %lu)\n"
- "BKEnrollPearlOperation:suspend -> %d %@\n"
- "BKEnrollResultInfo::initWithServerIdentity:details:device: %@ %@ %@\n"
- "BKEnrollTouchIDOperation::homeButtonPressed\n"
- "BKEnrollTouchIDOperation::homeButtonPressed: %p(%@) homeButtonPressedInEnrollOperation\n"
- "BKEnrollTouchIDOperation::statusMessage: %p(%@) encounteredCaptureError: %ld\n"
- "BKEnrollTouchIDOperation::statusMessage: %u\n"
- "BKEnrollTouchIDOperation::statusMessage: -> void\n"
- "BKExtendEnrollTouchIDOperation::homeButtonPressed\n"
- "BKExtendEnrollTouchIDOperation::homeButtonPressed: %p(%@) homeButtonPressedInEnrollOperation\n"
- "BKExtendEnrollTouchIDOperation::matchResult: %p(%@) hasUpdated: %u\n"
- "BKExtendEnrollTouchIDOperation::matchResult:withDictionary: %p(%@) %p)\n"
- "BKExtendEnrollTouchIDOperation::matchResult:withDictionary: -> void\n"
- "BKExtendEnrollTouchIDOperation::startBioOperation (_cid %lu)\n"
- "BKExtendEnrollTouchIDOperation::startBioOperation -> void\n"
- "BKExtendEnrollTouchIDOperation::statusMessage: %p(%@) encounteredCaptureError: %ld\n"
- "BKExtendEnrollTouchIDOperation::statusMessage: %u\n"
- "BKExtendEnrollTouchIDOperation::statusMessage: -> void\n"
- "BKFaceDetectOperation::startBioOperation (_cid %lu)\n"
- "BKFaceDetectOperation::startBioOperation -> void\n"
- "BKFaceDetectOperation::statusMessage: %p(%@) faceDetectStateChanged: %d\n"
- "BKFaceDetectOperation::statusMessage: %p(%@) motionDetectStateChanged\n"
- "BKFaceDetectOperation::statusMessage: %u\n"
- "BKFaceDetectOperation::statusMessage: -> void\n"
- "BKMatchOperation::matchResult:withDictionary: %p(%@) %p(LockoutState:%d,Unlocked:%d,CredentialAdded:%d,Ignored:%u)\n"
- "BKMatchOperation::matchResult:withDictionary: -> void\n"
- "BKMatchOperation::processMatchFailReason: %p(%@) failedWithReason: %ld\n"
- "BKMatchOperation::startBioOperation (_cid %lu)\n"
- "BKMatchOperation::startBioOperation -> void\n"
- "BKMatchOperation::statusMessage: %u (_cid %lu)\n"
- "BKMatchOperation::statusMessage: -> void\n"
- "BKMatchPearlOperation::enableAutoRetry -> %d(%{errno}d) %@\n"
- "BKMatchPearlOperation::enableAutoRetry: %u (_cid %lu)\n"
- "BKMatchPearlOperation::pauseFaceDetectTimer -> %d(%{errno}d) %@\n"
- "BKMatchPearlOperation::pauseFaceDetectTimer: %u (_cid %lu)\n"
- "BKMatchPearlOperation::startNewMatchAttemptWithError (_cid %lu)\n"
- "BKMatchPearlOperation::startNewMatchAttemptWithError -> %d(%{errno}d) %@\n"
- "BKMatchPearlOperation::statusMessage: %p(%@) faceDetectStateChanged: %d\n"
- "BKMatchPearlOperation::statusMessage: %p(%@) failedWithReason: %ld\n"
- "BKMatchPearlOperation::statusMessage: %p(%@) providedFaceOcclusionInfo: hasFaceOcclusion=%d\n"
- "BKMatchPearlOperation::statusMessage: %p(%@) providedFaceWUPoseEligibilityInfo: isEligible=%d\n"
- "BKMatchPearlOperation::statusMessage: %p(%@) providedFeedback: %ld\n"
- "BKMatchPearlOperation::statusMessage: %p(%@) requestedPasscodeShortcutWithReason: reason=%ld\n"
- "BKMatchPearlOperation::statusMessage: %u, details = %@\n"
- "BKMatchPearlOperation::statusMessage: -> void\n"
- "BKMatchResultInfo::initWithServerIdentity:details:device: %@ %@ %@\n"
- "BKMatchTouchIDOperation::statusMessage: %p(%@) encounteredCaptureError: %ld\n"
- "BKMatchTouchIDOperation::statusMessage: %u\n"
- "BKMatchTouchIDOperation::statusMessage: -> void\n"
- "BKOperation::cancel (_cid %lu)\n"
- "BKOperation::changeState %ld\n"
- "BKOperation::changeState -> void\n"
- "BKOperation::initWithDevice %@\n"
- "BKOperation::initWithDevice -> %@ (_cid %lu)\n"
- "BKOperation::operationEndsWithReason: %ld (_cid %lu)\n"
- "BKOperation::setDelegate %@ (_cid %lu)\n"
- "BKOperation::setDelegate -> void\n"
- "BKOperation::startOperation -> reply(%d, %@)\n"
- "BKOperation::startOperation -> void\n"
- "BKOperation::startOperation(async=%u)\n"
- "BKOperation::statusMessage: %u\n"
- "BKOperation::statusMessage: -> void\n"
- "BKOperation::userPresent (_cid %lu)\n"
- "BKOperation::userPresent -> %d %@\n"
- "BKPresenceDetectOperation::startBioOperation -> void\n"
- "BKPresenceDetectOperation::startOperation (_cid %lu)\n"
- "BiometricKitXPCClient::initWithDeviceType : connection interrupted\n"
- "BiometricKitXPCClient::initWithDeviceType : connection invalidated\n"
- "BiometricKitXPCClient::initWithDeviceType : processing kBiometricKitServerStartedNotification\n"
- "BiometricKitXPCClient::interruptConnection (_cid %lu)\n"
- "Please adopt new BiometricKit entitlements (see rdar://105770455 for additional details)\n"
- "createMatchInfo:withTopology:withMatchImage: %p(%@) %p %p\n"
- "createMatchInfo:withTopology:withMatchImage: -> %@\n"
- "detectFingerWithOptions: -> %{errno}d\n"
- "diagnostics:withOptions:passed:withDetails: %d %@ %p %p\n"
- "diagnostics:withOptions:passed:withDetails: -> %{errno}d %d %@\n"
- "dropUnlockToken -> %{errno}d\n"
- "enableBackgroundFdet: -> %{errno}d\n"
- "enroll:forUser:withOptions: %d %d %p(EnrollWCS:%p,EnrollWAT:%p,AuthWCS:%p,AuthWAT:%p)\n"
- "enroll:forUser:withOptions: -> %{errno}d\n"
- "forceBioLockoutForUser: %d\n"
- "forceBioLockoutForUser: -> %{errno}d\n"
- "getBioLockoutStateForUser: %d\n"
- "getCountersignedStoreToken: -> %{errno}d %p\n"
- "getFreeIdentityCount:forUser: %d %d\n"
- "getIdentitiesDatabaseHashForUser: %d\n"
- "getIdentitiesDatabaseHashForUser: -> %p(%@)\n"
- "getIdentitiesDatabaseUUIDForUser: %d\n"
- "getIdentityFromUUID: -> %@\n"
- "getProtectedConfigurationForUser: %d\n"
- "getTemplateInfo: -> %@\n"
- "isEphemeralMultiUser(): ephemeralMultiUser = %d\n"
- "isFaceIDPlatform(): faceIDPlatform = %d\n"
- "isTouchIDAvailableWithInfo: -> %d, %ld\n"
- "isTouchIDPlatform() -> %d\n"
- "isTouchIDPlatform() <-\n"
- "match:withOptions: %@ %p(AuthWCS:%p,MatchCSFEE:%p,AuthWAT:%p,MatchATFEE:%p,MatchATTBPB:%p,MatchFCS:%p,Priority:%d,MatchFEE:%d,MatchFPA:%d,MatchFU:%d,MatchFMP:%d,MatchFMC:%d,MatchBPB:%d,MatchSOS:%d,MatchCO:%d,MatchGBB:%d,FilterOutHBE:%d,SuppressHF:%d)\n"
- "match:withOptions: -> %{errno}d\n"
- "registerDSID:withAuthToken: (x) %p\n"
- "registerDSID:withAuthToken: -> %{errno}d\n"
- "registerDSID:withOptions: (x) %p(AuthWCS:%p,AuthWAT:%p)\n"
- "registerDSID:withOptions: -> %{errno}d\n"
- "registerStoreToken: %p\n"
- "registerStoreToken: -> %{errno}d\n"
- "removeAllIdentitiesForUser:withOptions: %d %@\n"
- "removeAllIdentitiesForUser:withOptions: -> %{errno}d\n"
- "removeAllIdentitiesForUser:withOptions:withReply: %d %@\n"
- "removeIdentity:withOptions: %p(%@) %@\n"
- "removeIdentity:withOptions: -> %{errno}d\n"
- "removeIdentity:withOptions:withReply: %p(%@) %@\n"
- "resetAppleConnectCounter -> %{errno}d\n"
- "setProtectedConfiguration:forUser:withOptions: %p(UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,ApplePayEnabled:%d,EfUnlockEnabled:%d,EfIdentificationEnabled:%d,EfLoginEnabled:%d,EfApplePayEnabled:%d) %d %p(AuthWCS:%p,AuthWAT:%p))\n"
- "setProtectedConfiguration:forUser:withOptions: -> %{errno}d\n"
- "setProtectedConfiguration:forUser:withOptions:withReply: %p(UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,ApplePayEnabled:%d,EfUnlockEnabled:%d,EfIdentificationEnabled:%d,EfLoginEnabled:%d,EfApplePayEnabled:%d) %d %p(AuthWCS:%p,AuthWAT:%p))\n"
- "setProtectedConfiguration:withAuthToken: %p(UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,ApplePayEnabled:%d,EfUnlockEnabled:%d,EfIdentificationEnabled:%d,EfLoginEnabled:%d,EfApplePayEnabled:%d) %p\n"
- "setProtectedConfiguration:withAuthToken: -> %{errno}d\n"
- "setSystemProtectedConfiguration:forUser:withOptions: %p(TouchIDEnabled:%d,UnlockEnabled:%d,IdentificationEnabled:%d,LoginEnabled:%d,UnlockTokenMaxLifetime:%d) %p(AuthWCS:%p,AuthWAT:%p))\n"
- "setSystemProtectedConfiguration:withOptions: -> %{errno}d\n"
- "setUserDSID:withAuthToken: (x) %p\n"
- "setUserDSID:withAuthToken: -> %{errno}d\n"
- "setUserDSID:withOptions: (x) %p(AuthWCS:%p,AuthWAT:%p)\n"
- "setUserDSID:withOptions: -> %{errno}d\n"
- "statusMessage: %d\n"
- "updateCallback <- notificationCenter:%p, observer:%p, name:%@, object:%p, userInfo:%@\n"
- "updateIdentity:withOptions: %p(%@) %@\n"
- "updateIdentity:withOptions: -> %{errno}d\n"
- "updateIdentity:withOptions:withReply: %p(%@) %@\n"

```
