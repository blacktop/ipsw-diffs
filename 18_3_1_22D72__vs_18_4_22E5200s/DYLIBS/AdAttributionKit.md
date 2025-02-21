## AdAttributionKit

> `/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit`

```diff

-2.2.15.0.0
-  __TEXT.__text: 0x3109c
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x4956
-  __TEXT.__cstring: 0x10cc
+2.4.13.0.0
+  __TEXT.__text: 0x35c38
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x1a8
+  __TEXT.__const: 0x5836
+  __TEXT.__cstring: 0xffd
   __TEXT.__oslogstring: 0x367
-  __TEXT.__swift5_typeref: 0xe00
-  __TEXT.__constg_swiftt: 0xf38
-  __TEXT.__swift5_fieldmd: 0xf28
-  __TEXT.__swift5_reflstr: 0x805
+  __TEXT.__swift5_typeref: 0x1094
+  __TEXT.__constg_swiftt: 0x11d4
+  __TEXT.__swift5_fieldmd: 0x13e8
+  __TEXT.__swift5_reflstr: 0xc48
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x460
-  __TEXT.__swift5_types: 0x190
-  __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_capture: 0x1d0
-  __TEXT.__unwind_info: 0x1300
-  __TEXT.__eh_frame: 0x1d14
-  __TEXT.__objc_methname: 0x549
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__swift5_proto: 0x530
+  __TEXT.__swift5_types: 0x1dc
+  __TEXT.__swift_as_entry: 0xb4
+  __TEXT.__swift_as_ret: 0xbc
+  __TEXT.__swift5_assocty: 0x180
+  __TEXT.__swift5_capture: 0x23c
+  __TEXT.__unwind_info: 0x1478
+  __TEXT.__eh_frame: 0x2368
+  __TEXT.__objc_methname: 0x5fa
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x130
-  __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__auth_ptr: 0x390
-  __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__objc_const: 0x750
-  __AUTH.__objc_data: 0x228
-  __AUTH.__data: 0x5b8
-  __DATA.__data: 0xbb0
-  __DATA.__bss: 0x7c00
-  __DATA.__common: 0x128
+  __DATA_CONST.__objc_selrefs: 0x150
+  __DATA_CONST.__objc_protorefs: 0x38
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_ptr: 0x420
+  __AUTH_CONST.__const: 0x3b68
+  __AUTH_CONST.__objc_const: 0x868
+  __AUTH.__data: 0x7a8
+  __DATA.__data: 0xe90
+  __DATA.__bss: 0x9600
+  __DATA.__common: 0x148
   __DATA_DIRTY.__objc_data: 0xc0
-  __DATA_DIRTY.__data: 0x558
+  __DATA_DIRTY.__data: 0x560
   __DATA_DIRTY.__bss: 0x1000
   __DATA_DIRTY.__common: 0x20
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1698
-  Symbols:   233
-  CStrings:  177
+  Functions: 1829
+  Symbols:   263
+  CStrings:  179
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "An invalid conversion tag was specified"
+ "Conversion tag was used in a context that is not supported"
+ "_TtC20AttributionKitCommon30PostbackProxyServiceConnection"
+ "_TtP20AttributionKitCommon28PostbackProxyServiceProtocol_"
+ "clearDevelopmentPostbacksWithReply:"
+ "coarse"
+ "com.apple.attributionkitd.xpc.postback-proxy"
+ "conversionTagNotSupported"
+ "conversionValueTier"
+ "createDevelopmentPostbacksWithConfigurationData:reply:"
+ "developerModeAppNotInstalled"
+ "developerModeDeveloperPostbackCopyURLMalformed"
+ "fine"
+ "invalidConversionTag"
+ "isMarketplaceIDIncluded"
+ "isPublisherItemIDIncluded"
+ "measurementWindowConfigurations"
+ "none"
+ "retrieveDeveloperPostbackURLForBundleID:reply:"
+ "transmitDevelopmentPostbacksWithReply:"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
