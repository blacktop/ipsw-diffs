## FindMyNotificationsContent

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent`

```diff

-415.34.7.13.20
-  __TEXT.__text: 0xcbf0
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0xa14
+415.34.7.13.25
+  __TEXT.__text: 0xcd04
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x50c
+  __TEXT.__const: 0xa04
   __TEXT.__cstring: 0xb0a
-  __TEXT.__objc_methname: 0x12b6
-  __TEXT.__constg_swiftt: 0x6c4
-  __TEXT.__swift5_typeref: 0x42a
-  __TEXT.__swift5_reflstr: 0x400
-  __TEXT.__swift5_fieldmd: 0x410
-  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__objc_methname: 0x1051
+  __TEXT.__constg_swiftt: 0x6d8
+  __TEXT.__swift5_typeref: 0x442
+  __TEXT.__swift5_reflstr: 0x420
+  __TEXT.__swift5_fieldmd: 0x420
+  __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_capture: 0x34
   __TEXT.__oslogstring: 0x14b
   __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x48
-  __TEXT.__objc_classname: 0x63
-  __TEXT.__objc_methtype: 0x5f2
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__objc_classname: 0x50
+  __TEXT.__objc_methtype: 0x4b4
+  __TEXT.__unwind_info: 0x358
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x5a0
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__auth_got: 0x588
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__auth_ptr: 0x1d0
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0xf60
-  __DATA.__objc_selrefs: 0x708
-  __DATA.__objc_data: 0xbc0
-  __DATA.__data: 0x8a8
-  __DATA.__common: 0xe1
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA.__objc_const: 0xe80
+  __DATA.__objc_selrefs: 0x660
+  __DATA.__objc_data: 0xbb0
+  __DATA.__data: 0x858
+  __DATA.__common: 0xc9
   __DATA.__bss: 0xb80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/FMF.framework/FMF
   - /System/Library/PrivateFrameworks/FMFCore.framework/FMFCore
   - /System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore
-  - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 276
-  Symbols:   356
-  CStrings:  395
+  Functions: 272
+  Symbols:   353
+  CStrings:  359
 
Symbols:
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$ss13ManagedBufferCMn
+ _$ss13ManagedBufferCMo
+ _objc_retain_x26
+ _objc_retain_x28
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _$s10FindMyBase16isFeatureEnabledySb0E5Flags0eG3Key_pF
- _$s10FindMyBase7FeatureO0aB0O0D5Flags0dE3KeyAAMc
- _$s10FindMyBase7FeatureO0aB0O15fencesMigrationyA2EmFWC
- _$s10FindMyBase7FeatureO0aB0OMa
- _$sSqMa
- _OBJC_CLASS_$_FMFSession
- _swift_allocBox
- _swift_beginAccess
- _swift_endAccess
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_updateClassMetadata2
CStrings:
+ "personLock"
- "FMFSessionDelegate"
- "connectionError:"
- "didChangeActiveLocationSharingDevice:"
- "didFailToFetchLocationForHandle:withError:"
- "didFailToHandleMappingPacket:error:"
- "didReceiveFriendshipRequest:"
- "didReceiveLocation:"
- "didReceiveServerError:"
- "didStartAbilityToGetLocationForHandle:"
- "didStartSharingMyLocationWithHandle:"
- "didStopAbilityToGetLocationForHandle:"
- "didStopSharingMyLocationWithHandle:"
- "didUpdateActiveDeviceList:"
- "didUpdateFavoriteHandles:"
- "didUpdateFences:"
- "didUpdateHidingStatus:"
- "didUpdatePendingOffersForHandles:"
- "didUpdatePreferences:"
- "fmfSession"
- "initWithDelegate:"
- "mappingPacketProcessingCompleted:"
- "networkReachabilityUpdated:"
- "person"
- "sendMappingPacket:toHandle:"
- "v24@0:8@\"FMFDevice\"16"
- "v24@0:8@\"FMFFriendshipRequest\"16"
- "v24@0:8@\"FMFHandle\"16"
- "v24@0:8@\"FMFLocation\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v32@0:8@\"FMFHandle\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"FMFHandle\"24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"

```
