## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation`

```diff

-815.0.0.0.0
-  __TEXT.__text: 0x8bb88
+817.0.0.0.0
+  __TEXT.__text: 0x8be88
   __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_methlist: 0x67b4
+  __TEXT.__objc_methlist: 0x6774
   __TEXT.__swift5_typeref: 0xa20
   __TEXT.__cstring: 0x320f
   __TEXT.__swift5_capture: 0x4e4

   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x2c50
   __TEXT.__eh_frame: 0x2aa0
-  __TEXT.__objc_classname: 0xfcd
-  __TEXT.__objc_methname: 0xb5a8
+  __TEXT.__objc_classname: 0xfc3
+  __TEXT.__objc_methname: 0xb5c1
   __TEXT.__objc_methtype: 0x2436
   __TEXT.__objc_stubs: 0x84c0
   __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0x440
+  __DATA_CONST.__const: 0x778
+  __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c00
+  __DATA_CONST.__objc_selrefs: 0x2bf8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x370
   __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__auth_ptr: 0x1b8
-  __AUTH_CONST.__const: 0x2968
+  __AUTH_CONST.__const: 0x29f8
   __AUTH_CONST.__cfstring: 0x48c0
-  __AUTH_CONST.__objc_const: 0xe6d0
-  __AUTH.__objc_data: 0x19f0
+  __AUTH_CONST.__objc_const: 0xe640
+  __AUTH.__objc_data: 0x19a0
   __AUTH.__data: 0x218
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x3278
+  __DATA.__objc_clsrolist: 0x10
   __DATA.__bss: 0x908
   __DATA_DIRTY.__objc_ivar: 0x530
   __DATA_DIRTY.__objc_data: 0x1040

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3336
-  Symbols:   6361
+  Functions: 3332
+  Symbols:   6301
   CStrings:  677
 
Symbols:
+ -[NSArray(HMFoundation) hmf_enumerateWithAutoreleasePoolUsingBlock:]
+ -[NSDictionary(HMFoundation) hmf_enumerateKeysAndObjectsWithAutoreleasePoolUsingBlock:]
+ -[NSSet(HMFoundation) hmf_enumerateWithAutoreleasePoolUsingBlock:]
+ ___66-[NSSet(HMFoundation) hmf_enumerateWithAutoreleasePoolUsingBlock:]_block_invoke
+ ___68-[NSArray(HMFoundation) hmf_enumerateWithAutoreleasePoolUsingBlock:]_block_invoke
+ ___87-[NSDictionary(HMFoundation) hmf_enumerateKeysAndObjectsWithAutoreleasePoolUsingBlock:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e12_v24?08^B16l
+ ___block_descriptor_40_e8_32bs_e15_v32?0816^B24l
+ ___block_descriptor_40_e8_32bs_e15_v32?08Q16^B24l
+ _generic_ro_datas
- +[HMUIndent indentWithLevel:]
- +[HMUIndent level]
- -[HMUIndent indentByFactor:]
- -[NSDictionary(HMFDeprecated) boolForKey:]
- -[NSDictionary(HMFDeprecated) boolForKey:keyPresent:]
- -[NSDictionary(HMFDeprecated) nullForKey:]
- -[NSDictionary(HMFDeprecated) numberForKey:]
- _OBJC_CLASS_$_HMUIndent
- _OBJC_METACLASS_$_HMUIndent
- __OBJC_$_CLASS_METHODS_HMUIndent
- __OBJC_$_INSTANCE_METHODS_HMUIndent
- __OBJC_CLASS_RO_$_HMUIndent
- __OBJC_METACLASS_RO_$_HMUIndent
- _isEqualToObject
- _kDumpStateAccessoryCategoryKey
- _kDumpStateAccessoryKey
- _kDumpStateAccessoryProfileKey
- _kDumpStateAccessorySetupHashKey
- _kDumpStateAccessoryTransportKey
- _kDumpStateActionSetKey
- _kDumpStateApplicationDataKey
- _kDumpStateBridgeAccessoryKey
- _kDumpStateBridgedAccessoryKey
- _kDumpStateBulletinNotificationGroupCamerasKey
- _kDumpStateBulletinNotificationGroupKey
- _kDumpStateBulletinNotificationGroupServicesKey
- _kDumpStateBulletinNotificationKey
- _kDumpStateCharacteristicKey
- _kDumpStateCurrentUser
- _kDumpStateEventKey
- _kDumpStateExecuteOnceKey
- _kDumpStateExecuteSessionKey
- _kDumpStateHomeDaemonVersionKey
- _kDumpStateHomeKey
- _kDumpStateHomeManagerKey
- _kDumpStateHomeNotificationRegistrationsKey
- _kDumpStateIdentityKey
- _kDumpStateIncomingInvitesKey
- _kDumpStateInvitesKey
- _kDumpStateKeychainItemKey
- _kDumpStateKeychainKey
- _kDumpStateLocationKey
- _kDumpStateMediaActionKey
- _kDumpStateMeshKey
- _kDumpStateMetadataKey
- _kDumpStateNetServiceKey
- _kDumpStateOutgoingInvitesKey
- _kDumpStatePendingResponses
- _kDumpStatePredicateKey
- _kDumpStateRecurrenceKey
- _kDumpStateRemovedUserKey
- _kDumpStateResidentKey
- _kDumpStateRoomKey
- _kDumpStateSecondaryAccessoryKey
- _kDumpStateServiceGroupKey
- _kDumpStateServiceKey
- _kDumpStateSharedHomeSourceVersion
- _kDumpStateSharedHomeUpdateHandler
- _kDumpStateSharedHomeUpdateSession
- _kDumpStateStateKey
- _kDumpStateSyncManagerKey
- _kDumpStateTimerTriggerKey
- _kDumpStateTriggerKey
- _kDumpStateUserAccessTokenKey
- _kDumpStateUserKey
- _kDumpStateWriteActionKey
- _kDumpStateZoneKey
- _kIndentLevel
- _randomDataWithLength
- _randomUInt32
CStrings:
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/HMFoundation/HMFoundation/Swift/AsyncSerialQueue.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/HMFoundation/HMFoundation/Swift/AsyncSerialQueue.swift"

```
