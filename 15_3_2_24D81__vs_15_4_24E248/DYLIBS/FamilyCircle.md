## FamilyCircle

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle`

```diff

-226.228.0.0.0
-  __TEXT.__text: 0x80140
-  __TEXT.__auth_stubs: 0x1d90
-  __TEXT.__objc_methlist: 0x2d8c
-  __TEXT.__const: 0x3078
-  __TEXT.__oslogstring: 0x2d5f
-  __TEXT.__cstring: 0x5600
+226.459.0.0.0
+  __TEXT.__text: 0x83420
+  __TEXT.__auth_stubs: 0x1dc0
+  __TEXT.__objc_methlist: 0x3374
+  __TEXT.__const: 0x3238
+  __TEXT.__oslogstring: 0x2f2f
+  __TEXT.__cstring: 0x52f0
   __TEXT.__gcc_except_tab: 0x2bc
   __TEXT.__dlopen_cstrs: 0x10b
-  __TEXT.__swift5_typeref: 0x144c
-  __TEXT.__constg_swiftt: 0x159c
-  __TEXT.__swift5_reflstr: 0xcca
-  __TEXT.__swift5_fieldmd: 0xe98
+  __TEXT.__swift5_typeref: 0x1554
+  __TEXT.__constg_swiftt: 0x1640
+  __TEXT.__swift5_reflstr: 0xcfa
+  __TEXT.__swift5_fieldmd: 0xf14
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x358
-  __TEXT.__swift5_proto: 0x254
-  __TEXT.__swift5_types: 0x11c
-  __TEXT.__swift5_capture: 0x698
+  __TEXT.__swift5_proto: 0x270
+  __TEXT.__swift5_types: 0x128
+  __TEXT.__swift5_capture: 0x688
+  __TEXT.__swift_as_entry: 0xe8
+  __TEXT.__swift_as_ret: 0x110
   __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x23b0
-  __TEXT.__eh_frame: 0x25c8
-  __TEXT.__objc_classname: 0x868
-  __TEXT.__objc_methname: 0x8d06
-  __TEXT.__objc_methtype: 0x11ff
-  __TEXT.__objc_stubs: 0x4440
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0xba8
-  __DATA_CONST.__objc_classlist: 0x2e8
-  __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xd8
+  __TEXT.__unwind_info: 0x2308
+  __TEXT.__eh_frame: 0x2758
+  __TEXT.__objc_classname: 0x891
+  __TEXT.__objc_methname: 0x8eba
+  __TEXT.__objc_methtype: 0x120a
+  __TEXT.__objc_stubs: 0x44c0
+  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2018
-  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x2120
+  __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xed8
-  __AUTH_CONST.__const: 0x3c90
-  __AUTH_CONST.__cfstring: 0x3760
-  __AUTH_CONST.__objc_const: 0xb0d8
+  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH_CONST.__const: 0x3e40
+  __AUTH_CONST.__cfstring: 0x37a0
+  __AUTH_CONST.__objc_const: 0xab00
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1640
-  __AUTH.__data: 0x1008
-  __DATA.__objc_ivar: 0x384
-  __DATA.__data: 0x18e0
-  __DATA.__bss: 0x42a0
+  __AUTH.__objc_data: 0x16d8
+  __AUTH.__data: 0x1038
+  __DATA.__objc_ivar: 0x388
+  __DATA.__data: 0x1998
+  __DATA.__bss: 0x4640
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x28

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F3815448-1B5A-3009-8576-240530D8E556
-  Functions: 3312
-  Symbols:   3990
-  CStrings:  3255
+  UUID: CC97E174-E86A-3C4E-907F-0EB21794DE20
+  Functions: 3307
+  Symbols:   4120
+  CStrings:  3272
 
Symbols:
+ +[FAFamilyCircleCache cacheQueue].cold.1
+ +[FAFamilyPresenterHostInterface XPCInterface].cold.1
+ +[FAPeopleDiscoveryService sharedInstance].cold.1
+ +[FAPushNotificationHandler sharedHandler].cold.1
+ +[FAServerBagFlag megadomeKillSwitch].cold.1
+ +[FAServerBagFlag memberPhotoRequest404CacheDurationHours]
+ +[FAServerBagFlag memberPhotoRequest404CacheDurationHours].cold.1
+ +[FAServerBagFlag registerDeviceWithPDS].cold.1
+ +[FASettingPresetsCache cacheQueue].cold.1
+ +[FASettingsPresetConfiguration boolKeys].cold.1
+ +[_FAFamilyCircleRequestConnectionProvider sharedInstance].cold.1
+ -[FAFamilyCircle isEqual:]
+ -[FAFamilyCircle isEqualToFAFamilyCircle:]
+ -[FAFamilyMember hasParentalControlsEnabled].cold.1
+ -[FAFamilyMember isParent].cold.1
+ -[FAServerBagFlag getCacheDurationforMemberPhoto404Response:]
+ -[FAServerBagFlag intValue]
+ -[FAServerBagFlag setIntValue:]
+ -[FASettingProtoAccountRestrictionsRequest removeRestrictionsWithCompletion:]
+ -[FASettingProtoAccountRestrictionsRequest setRestrictionsWithCompletion:]
+ OBJC_IVAR_$_FAServerBagFlag._intValue
+ _FAAgeAttestationLogSystem.cold.1
+ _FAAgeAttestationLogSystem.log
+ _FAAgeAttestationLogSystem.onceToken
+ _FALogSystem.cold.1
+ _FAMemberPhotoRequest404CacheDurationHours
+ _FAMemberPhotoRequest404CacheDurationHoursDefault
+ _FASignpostGetNanoseconds.cold.1
+ _FASignpostLogSystem.cold.1
+ _FAURLEndpointConnectWithFamily
+ _OBJC_CLASS_$_FAMemberPhotoRequest404Cache
+ _OBJC_CLASS_$_FASettingProtoAccountRestrictionsRequest
+ _OBJC_METACLASS_$_FAMemberPhotoRequest404Cache
+ _OBJC_METACLASS_$_FASettingProtoAccountRestrictionsRequest
+ __74-[FASettingProtoAccountRestrictionsRequest setRestrictionsWithCompletion:]_block_invoke.cold.1
+ __77-[FASettingProtoAccountRestrictionsRequest removeRestrictionsWithCompletion:]_block_invoke.cold.1
+ __CATEGORY_NSUserDefaults_$_FamilyCircle
+ __CATEGORY_PROTOCOLS_NSUserDefaults_$_FamilyCircle
+ __DATA_FAMemberPhotoRequest404Cache
+ __FAAgeAttestationLogSystem
+ __INSTANCE_METHODS_FAMemberPhotoRequest404Cache
+ __IVARS_FAMemberPhotoRequest404Cache
+ __METACLASS_DATA_FAMemberPhotoRequest404Cache
+ __OBJC_$_INSTANCE_METHODS_FASettingProtoAccountRestrictionsRequest
+ __OBJC_CLASS_RO_$_FASettingProtoAccountRestrictionsRequest
+ __OBJC_METACLASS_RO_$_FASettingProtoAccountRestrictionsRequest
+ __PROTOCOL_INSTANCE_METHODS_KeyValuePersisting
+ __PROTOCOL_KeyValuePersisting
+ __PROTOCOL_METHOD_TYPES_KeyValuePersisting
+ ___58+[FAServerBagFlag memberPhotoRequest404CacheDurationHours]_block_invoke
+ ___74-[FASettingProtoAccountRestrictionsRequest setRestrictionsWithCompletion:]_block_invoke
+ ___77-[FASettingProtoAccountRestrictionsRequest removeRestrictionsWithCompletion:]_block_invoke
+ ____FAAgeAttestationLogSystem_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.10
+ __block_literal_global.2
+ __block_literal_global.29
+ _associated conformance 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV10CodingKeysOSHAASQ
+ _associated conformance 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV10CodingKeysOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV10CodingKeysOs0J3KeyAAs28CustomDebugStringConvertible
+ _flat unique So18KeyValuePersisting_p
+ _objc_msgSend$clearRestrictionsforProtoAccountWithCompletion:
+ _objc_msgSend$isEqualToFAFamilyCircle:
+ _objc_msgSend$setIntValue:
+ _objc_msgSend$setRestrictionsForProtoAccountWithCompletion:
+ _symbolic $s12FamilyCircle18KeyValuePersistingP
+ _symbolic IeyB_Sg
+ _symbolic SDySS_____G 10Foundation4DateV
+ _symbolic SS______t 10Foundation4DateV
+ _symbolic SccySb______pG s5ErrorP
+ _symbolic SccySo14FAFamilyCircleC______pG s5ErrorP
+ _symbolic Sccy___________pG 10Foundation3URLV s5ErrorP
+ _symbolic _____ 10Foundation11JSONDecoderC
+ _symbolic _____ 10Foundation11JSONEncoderC
+ _symbolic _____ 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV
+ _symbolic _____ 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV10CodingKeysO
+ _symbolic _____ 12FamilyCircle26MemberPhotoRequest404CacheC
+ _symbolic ______p 12FamilyCircle18KeyValuePersistingP
+ _symbolic _____ySS_____G s18_DictionaryStorageC 10Foundation4DateV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 12FamilyCircle11CacheRecord33_5FFEDBB06CEB4ADD96E911548DB43824LLV10CodingKeysO
+ block_copy_helper.2
+ block_copy_helper.37
+ block_copy_helper.39
+ block_copy_helper.45
+ block_descriptor.4
+ block_descriptor.41
+ block_descriptor.47
+ block_destroy_helper.3
+ block_destroy_helper.38
+ block_destroy_helper.40
+ block_destroy_helper.46
+ memberPhotoRequest404CacheDurationHours.memberPhotoRequest404CacheDurationHours
+ memberPhotoRequest404CacheDurationHours.onceToken
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_FamilyCircle
- block_copy_helper.40
- block_copy_helper.43
- block_descriptor.2
- block_descriptor.42
- block_descriptor.45
- block_destroy_helper.41
- block_destroy_helper.44
CStrings:
+ "@\"NSData\"24@0:8@\"NSString\"16"
+ "B32@0:8@16q24"
+ "Error saving rate last404Response record: %s"
+ "FAMemberPhotoRequest404Cache"
+ "FASettingProtoAccountRestrictionsRequest"
+ "Failed to create a connection with error: %@"
+ "KeyValuePersisting"
+ "MemberPhotoRequest404Cache: %s %{bool}d"
+ "MemberPhotoRequest404Cache: %s getLast404Response %s"
+ "MemberPhotoRequest404Cache: %s no 404 cache for member, allow request"
+ "MemberPhotoRequest404Cache: cacheMeasurementDuration: %s"
+ "MemberPhotoRequest404Cache: saved 404 response for %s)"
+ "Tq,N,V_intValue"
+ "_intValue"
+ "ageAttestation"
+ "clearRestrictionsforProtoAccountWithCompletion:"
+ "com.apple.FamilyCircle.MemberPhotoRequest404Cache"
+ "connectWithFamily"
+ "dataForKey:"
+ "decoder"
+ "encoder"
+ "getCacheDurationforMemberPhoto404Response:"
+ "getLast404ResponseFor:"
+ "isEqualToFAFamilyCircle:"
+ "memberPhotoRequest404CacheDurationHours"
+ "persistence"
+ "q20@0:8B16"
+ "removeRestrictionsWithCompletion:"
+ "save404ResponseFor:"
+ "setIntValue:"
+ "setRestrictionsForProtoAccountWithCompletion:"
+ "setRestrictionsWithCompletion:"
+ "setValue:forKey:"
+ "shouldAllowRequest(for:cacheDuration:)"
+ "shouldAllowRequestFor:cacheDuration:"
+ "standardUserDefaults"
+ "use default value for FAMemberPhotoRequest404CacheDurationHour"
+ "v32@0:8@16@\"NSString\"24"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
