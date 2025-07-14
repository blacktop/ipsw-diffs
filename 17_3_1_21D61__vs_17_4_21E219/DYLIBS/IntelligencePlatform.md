## IntelligencePlatform

> `/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform`

```diff

-75.3.6.0.2
-  __TEXT.__text: 0x48d284
-  __TEXT.__auth_stubs: 0x4410
-  __TEXT.__objc_methlist: 0x90e0
-  __TEXT.__const: 0x37c88
-  __TEXT.__swift5_typeref: 0x11470
-  __TEXT.__cstring: 0x1b755
-  __TEXT.__constg_swiftt: 0x118ec
-  __TEXT.__swift5_reflstr: 0x8f0c
-  __TEXT.__swift5_fieldmd: 0xffdc
-  __TEXT.__swift5_builtin: 0x528
-  __TEXT.__swift5_assocty: 0x2c60
-  __TEXT.__swift5_proto: 0x358c
-  __TEXT.__swift5_types: 0x11f8
+75.12.7.1.0
+  __TEXT.__text: 0x47338c
+  __TEXT.__auth_stubs: 0x4450
+  __TEXT.__objc_methlist: 0x90f8
+  __TEXT.__const: 0x37f98
+  __TEXT.__cstring: 0x1be35
+  __TEXT.__swift5_typeref: 0x11424
+  __TEXT.__constg_swiftt: 0x11950
+  __TEXT.__swift5_reflstr: 0x8f2c
+  __TEXT.__swift5_fieldmd: 0x1004c
+  __TEXT.__swift5_builtin: 0x550
+  __TEXT.__swift5_assocty: 0x2c48
+  __TEXT.__swift5_proto: 0x35b8
+  __TEXT.__swift5_types: 0x1204
   __TEXT.__swift5_protos: 0x1e8
-  __TEXT.__swift5_capture: 0x4cc4
+  __TEXT.__swift5_capture: 0x4d34
   __TEXT.__swift5_mpenum: 0x1c0
-  __TEXT.__gcc_except_tab: 0xb8c
+  __TEXT.__gcc_except_tab: 0xbc8
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x2e11
-  __TEXT.__unwind_info: 0x16ef0
-  __TEXT.__eh_frame: 0x28b08
+  __TEXT.__oslogstring: 0x2f24
+  __TEXT.__unwind_info: 0x173ac
+  __TEXT.__eh_frame: 0x28ec8
   __TEXT.__objc_classname: 0x1d94
-  __TEXT.__objc_methname: 0x16dbc
-  __TEXT.__objc_methtype: 0x305b
-  __TEXT.__objc_stubs: 0x49e0
-  __DATA_CONST.__got: 0xab8
-  __DATA_CONST.__const: 0x13d0
+  __TEXT.__objc_methname: 0x16e8e
+  __TEXT.__objc_methtype: 0x30a3
+  __TEXT.__objc_stubs: 0x4a20
+  __DATA_CONST.__got: 0xae8
+  __DATA_CONST.__const: 0x13f0
   __DATA_CONST.__objc_classlist: 0xd28
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x22a88
-  __DATA_CONST.__objc_selrefs: 0x2f40
+  __DATA_CONST.__objc_const: 0x22ae8
+  __DATA_CONST.__objc_selrefs: 0x2f70
+  __DATA_CONST.__objc_protorefs: 0x120
+  __DATA_CONST.__objc_classrefs: 0x958
+  __DATA_CONST.__objc_superrefs: 0x5a0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__const: 0x289f8
+  __AUTH_CONST.__const: 0x28bb8
   __AUTH_CONST.__objc_const: 0x5710
   __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x2218
+  __AUTH_CONST.__auth_got: 0x2238
   __AUTH.__objc_data: 0x14b8
   __AUTH.__data: 0x3928
-  __DATA.__objc_protorefs: 0x120
-  __DATA.__objc_classrefs: 0x958
-  __DATA.__objc_superrefs: 0x5a0
-  __DATA.__objc_ivar: 0x14a0
+  __DATA.__objc_ivar: 0x14a4
   __DATA.__objc_data: 0x48
-  __DATA.__data: 0x16858
-  __DATA.__bss: 0x59180
-  __DATA.__common: 0x430
+  __DATA.__data: 0x17210
+  __DATA.__bss: 0x59600
+  __DATA.__common: 0x190
   __DATA_DIRTY.__const: 0x128
   __DATA_DIRTY.__objc_const: 0x48
   __DATA_DIRTY.__objc_data: 0x64d8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/Vision.framework/Vision
+  - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AA608F98-99C0-3C01-9B4E-1D0D42B09006
-  Functions: 42539
-  Symbols:   1011
-  CStrings:  6649
+  UUID: 2B4A9A0F-D55A-3D3D-9B91-ACBB72EB3E65
+  Functions: 42143
+  Symbols:   1017
+  CStrings:  6702
 
Symbols:
+ _BMDeviceMetadataDevicePlatformAsString
+ _BMSiriRemembersInteractionInteractionDirectionAsString
+ _BMSiriRemembersInteractionInteractionSourceAsString
+ _BMSiriRemembersInteractionInteractionStatusAsString
+ _BMSiriRemembersInteractionUserDonatorTypeAsString
+ _OBJC_CLASS_$_BMDeviceMetadataUtils
CStrings:
+ "006: Add isLocal and devicePlatform"
+ "007: Add userDonatorType column"
+ "008: Redo source column"
+ "@\"GDXPCViewService\""
+ "Can't construct Array with count < 0"
+ "DELETE FROM configs"
+ "DELETE FROM entities"
+ "DELETE FROM interactionEntities"
+ "DELETE FROM interactions"
+ "DELETE FROM processedInteractions"
+ "DROP INDEX IF EXISTS interactions_sourceStreams"
+ "Division by zero"
+ "Division results in an overflow"
+ "GDXPCCoordinationService: error during migrateViewDatabases call: %@"
+ "GDXPCCoordinationService: error during streamsUpdated call: %@"
+ "GDXPCCoordinationService: migrateViewDatabases called"
+ "GDXPCCoordinationService: streamsChanged called with %tu updated and %tu deletes"
+ "GDXPCInternalService: error during featureKeysWithError call: %@"
+ "GDXPCInternalService: featureKeysWithError called."
+ "Insufficient space allocated to copy string contents"
+ "Must take zero or more splits"
+ "Negative value is not representable"
+ "No library available on this users device"
+ "Not enough bits to represent the passed value"
+ "Range requires lowerBound <= upperBound"
+ "Swift/Array.swift"
+ "Swift/Collection.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "UPDATE interactions SET devicePlatform = ?"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_xpcService"
+ "invalid Collection: less than 'count' elements in collection"
+ "mapSpanToOriginalSpace: Either the original string, preprocessed string, or the responses are empty."
+ "migrateViewDatabasesWithCompletion:"
+ "migrateViewDatabasesWithError:"
+ "platform"
+ "streamsChangedWithUpdated:deletes:completion:"
+ "streamsChangedWithUpdated:deletes:error:"
+ "userDonatorType"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?B@\"NSError\">32"
- "GDXPCViewService: error during featureKeysWithError call: %@"
- "GDXPCViewService: featureKeysWithError called."

```
