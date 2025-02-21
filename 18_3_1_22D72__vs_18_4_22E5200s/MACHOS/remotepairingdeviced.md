## remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

-199.60.1.0.0
-  __TEXT.__text: 0x65904
-  __TEXT.__auth_stubs: 0x3130
+199.100.14.0.0
+  __TEXT.__text: 0x5f894
+  __TEXT.__auth_stubs: 0x3110
   __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0xa4
-  __TEXT.__const: 0x17e8
-  __TEXT.__oslogstring: 0x2dc9
-  __TEXT.__cstring: 0x572b
+  __TEXT.__objc_methlist: 0x1ac
+  __TEXT.__const: 0x1ad2
+  __TEXT.__oslogstring: 0x2f49
+  __TEXT.__cstring: 0x548b
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__objc_methname: 0x5ab
   __TEXT.__objc_classname: 0xd8
   __TEXT.__objc_methtype: 0x11e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x172c
-  __TEXT.__swift5_typeref: 0x13c8
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x1299
-  __TEXT.__swift5_fieldmd: 0xd20
+  __TEXT.__constg_swiftt: 0x1710
+  __TEXT.__swift5_typeref: 0x13b8
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_reflstr: 0x1399
+  __TEXT.__swift5_fieldmd: 0xd24
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x98
-  __TEXT.__swift5_types: 0xac
-  __TEXT.__swift5_capture: 0xe24
+  __TEXT.__swift5_proto: 0x94
+  __TEXT.__swift5_types: 0xa4
+  __TEXT.__swift5_capture: 0xe44
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x12e0
-  __TEXT.__eh_frame: 0x1140
-  __DATA_CONST.__auth_got: 0x18a8
+  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__eh_frame: 0x1018
+  __DATA_CONST.__auth_got: 0x1898
   __DATA_CONST.__got: 0x868
   __DATA_CONST.__auth_ptr: 0x8a0
-  __DATA_CONST.__const: 0x2ee0
+  __DATA_CONST.__const: 0x2ec0
   __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x44d0
-  __DATA.__objc_selrefs: 0x210
+  __DATA.__objc_const: 0x42c8
+  __DATA.__objc_selrefs: 0x2a8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x2ff0
+  __DATA.__data: 0x3000
   __DATA.__bss: 0xd90
   __DATA.__common: 0x90
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2119
-  Symbols:   1212
-  CStrings:  765
+  Functions: 2018
+  Symbols:   1220
+  CStrings:  754
 
Symbols:
+ _$s8Dispatch0A9PredicateO7onQueueyACSo17OS_dispatch_queueCcACmFWC
+ _$s8Dispatch0A9PredicateOMa
+ _$s8Dispatch25_dispatchPreconditionTestySbAA0A9PredicateOF
+ _$ss10_HashTableV11startBucketAB0D0Vvg
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ _swift_deallocPartialClassInstance
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getTupleTypeMetadata
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- _$s10Foundation13__DataStorageC5bytes6lengthACSVSg_Sitcfc
- _$s10Foundation4DataV14RangeReferenceCMa
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _objc_release_x9
- _swift_getTupleTypeLayout
- _swift_initEnumMetadataMultiPayload
CStrings:
+ "$__lazy_storage_$__lockStateManager"
+ "$__lazy_storage_$_firstUnlockHasCompleted"
+ "Failed to cancel %{public}s notification. Received error code %u from notify_cancel"
+ "Failed to register for %{public}s darwin notification. Received error code %u from notify_register_dispatch"
+ "First unlock completed. Executing deferred work"
+ "Ignoring %{public}s notification since device has not yet passed first unlock"
+ "Received darwin notification for developer mode change. Invalidating previously computed metadata"
+ "Registered for %{public}s notification"
+ "Unregistered for %{public}s notification"
+ "_developerModeStatusChangedNotificationName"
+ "_developerModeStatusDarwinNotificationToken"
+ "_keybagLockStatusChangedNotificationToken"
+ "_lockStateChangeNotificationName"
+ "_unlockedSinceBootFunc"
+ "_userAssignedNameDarwinNotificationToken"
+ "advert controlChannel peerInitiatingPairing completion "
+ "com.apple.mobile.keybagd.lock_status"
- "$__lazy_storage_$_auxiliaryMetadataService"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "First unlock notification received. Executing deferred work"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_TtC20remotepairingdeviced28StubAuxiliaryMetadataService"
- "darwinNotificationToken"
- "firstUnlockHasCompleted"
- "invalid Collection: less than 'count' elements in collection"

```
