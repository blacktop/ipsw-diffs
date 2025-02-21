## FaceTimeMessageStore

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore`

```diff

-1525.400.141.0.0
-  __TEXT.__text: 0x106a80
-  __TEXT.__auth_stubs: 0x2580
-  __TEXT.__objc_methlist: 0x680
-  __TEXT.__const: 0x8a50
-  __TEXT.__cstring: 0x3a27
-  __TEXT.__constg_swiftt: 0x2d24
-  __TEXT.__swift5_typeref: 0x2e3e
+1525.500.125.2.2
+  __TEXT.__text: 0xf6c5c
+  __TEXT.__auth_stubs: 0x2530
+  __TEXT.__objc_methlist: 0x1208
+  __TEXT.__const: 0x91b0
+  __TEXT.__cstring: 0x3627
+  __TEXT.__constg_swiftt: 0x2cb4
+  __TEXT.__swift5_typeref: 0x2dcc
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_reflstr: 0x1e18
   __TEXT.__swift5_assocty: 0x400
   __TEXT.__swift5_fieldmd: 0x2648
   __TEXT.__swift5_proto: 0x7fc
   __TEXT.__swift5_types: 0x27c
-  __TEXT.__swift5_capture: 0x12d8
-  __TEXT.__oslogstring: 0x8663
+  __TEXT.__swift5_capture: 0x1344
+  __TEXT.__oslogstring: 0x872b
+  __TEXT.__swift_as_entry: 0x3fc
+  __TEXT.__swift_as_ret: 0x43c
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_protos: 0x7c
-  __TEXT.__unwind_info: 0x4ac8
-  __TEXT.__eh_frame: 0xa184
+  __TEXT.__unwind_info: 0x4800
+  __TEXT.__eh_frame: 0x9bd4
   __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methname: 0x3d1b
+  __TEXT.__objc_methname: 0x3da9
   __TEXT.__objc_methtype: 0xb34
-  __DATA_CONST.__got: 0x9f8
-  __DATA_CONST.__const: 0x7f8
+  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe20
+  __DATA_CONST.__objc_selrefs: 0x1398
   __DATA_CONST.__objc_protorefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x12c0
-  __AUTH_CONST.__auth_ptr: 0x8f8
-  __AUTH_CONST.__const: 0x6bf8
-  __AUTH_CONST.__objc_const: 0x53a8
-  __AUTH.__objc_data: 0x710
-  __AUTH.__data: 0x5c0
-  __DATA.__data: 0x20f8
+  __AUTH_CONST.__auth_got: 0x1298
+  __AUTH_CONST.__auth_ptr: 0x940
+  __AUTH_CONST.__const: 0x6f68
+  __AUTH_CONST.__objc_const: 0x41d0
+  __AUTH.__objc_data: 0x3a8
+  __AUTH.__data: 0x418
+  __DATA.__data: 0x2118
   __DATA.__objc_stublist: 0x10
-  __DATA.__bss: 0xa060
+  __DATA.__bss: 0x9de0
   __DATA.__common: 0xb8
-  __DATA_DIRTY.__objc_data: 0xdd0
-  __DATA_DIRTY.__data: 0x29d0
-  __DATA_DIRTY.__common: 0x2f0
-  __DATA_DIRTY.__bss: 0x4f80
+  __DATA_DIRTY.__objc_data: 0xda8
+  __DATA_DIRTY.__data: 0x2ba8
+  __DATA_DIRTY.__common: 0x2e8
+  __DATA_DIRTY.__bss: 0x5200
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6743
-  Symbols:   2400
-  CStrings:  1701
+  Functions: 6616
+  Symbols:   2425
+  CStrings:  1679
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- __swift_FORCE_LOAD_$_swiftFileProvider
- _memcmp
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
CStrings:
+ "Closing transaction: %{public}s"
+ "Could not find captions for voicemail at %{public}s with error %{public}@"
+ "Failed to deserialize storedMessage transcriptData with error %{public}@"
+ "Failed to fetch messages for voicemail diff. %{public}@"
+ "Failed to unarchive captions at url %{public}s"
+ "Failed to wrap accountInfo: %{public}@"
+ "Fetch request with id %{public}s failed after %{public}ss. Error: %{public}@"
+ "Fetch request with id %{public}s took %{public}ss and returned %{public}ld result(s)"
+ "Inbox messages: %{public}s"
+ "Junk messages: %{public}s"
+ "MessageStore: Failed adding %@ for %{public}@ to %{public}@ %{public}@"
+ "MessageStoreServiceDelegate: Updating client connection %{public}@ with added messages: %{public}s"
+ "MessageStoreServiceDelegate: Updating client connection %{public}@ with deleted message uuids: %{public}s"
+ "MessageStoreServiceDelegate: Updating client connection %{public}@ with deleted messages: %{public}s"
+ "MessageStoreServiceDelegate: Updating client connection %{public}@ with messageStoreRequiresRefetch notification"
+ "MessageStoreServiceDelegate: Updating client connection %{public}@ with updated account info: %@"
+ "MessageStoreServiceDelegate: Updating client connection %{public}@ with updated messages: %{public}s"
+ "Opening transaction: %{public}s"
+ "Removing posted notifications. FaceTime: %{public}s, MobilePhone: %{public}s"
+ "Trash messages: %{public}s"
+ "Unable to read data at URL %{public}s, _newTranscriptData not set"
+ "Unable to read data at sandboxed URL %{public}s"
+ "automaticCallActivationDisabled"
+ "calculated inserts: %{public}s"
+ "calculated updates: %{public}s"
+ "callConnectHapticsEnabled"
+ "callTranscriptionGASRExpansionEnabled"
+ "continuityEmergencyMultiDeviceDiscoveryEnabled"
+ "mooseEnabled"
+ "setTranscribedTextContent:"
- "Can't construct Array with count < 0"
- "Closing transaction: %s"
- "Could not find captions for voicemail at %s with error %@"
- "Division by zero"
- "Division results in an overflow"
- "Error getting messages with recordUUIDs %{public}s %{public}@"
- "Failed to deserialize storedMessage transcriptData with error %@"
- "Failed to fetch messages for voicemail diff. %@"
- "Failed to wrap accountInfo: %@"
- "Fatal error"
- "Fetch request with id %s failed after %ss"
- "Fetch request with id %s took %ss and returned %ld result(s)"
- "Handling store merged notification"
- "Inbox messages: %s"
- "Insufficient space allocated to copy string contents"
- "Junk messages: %s"
- "MessageStore: Failed adding %@ to %@ %{public}@"
- "MessageStoreServiceDelegate: Updating client connection %@ with added messages: %s"
- "MessageStoreServiceDelegate: Updating client connection %@ with deleted message uuids: %s"
- "MessageStoreServiceDelegate: Updating client connection %@ with deleted messages: %s"
- "MessageStoreServiceDelegate: Updating client connection %@ with messageStoreRequiresRefetch notification"
- "MessageStoreServiceDelegate: Updating client connection %@ with updated account info: %@"
- "MessageStoreServiceDelegate: Updating client connection %@ with updated messages: %s"
- "Negative value is not representable"
- "Opening transaction: %s"
- "Removing posted notifications. FaceTime: %{public}s, MobilePhone: %s"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TB,N"
- "Trash messages: %s"
- "Unable to read data at URL %s, _newTranscriptData not set"
- "Unable to read data at sandboxed URL %s"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "calculated inserts: %s"
- "calculated updates: %s"
- "invalid Collection: less than 'count' elements in collection"
- "setSupportsSecureCoding:"
- "setTextContent:"
- "v20@0:8B16"

```
