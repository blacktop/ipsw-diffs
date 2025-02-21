## UIIntelligenceSupportAgent

> `/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent`

```diff

-8220.0.0.0.0
-  __TEXT.__text: 0x54c9c
-  __TEXT.__auth_stubs: 0x1e20
-  __TEXT.__const: 0x1c98
-  __TEXT.__constg_swiftt: 0x888
-  __TEXT.__swift5_typeref: 0xdd7
+8435.0.0.0.0
+  __TEXT.__text: 0x57870
+  __TEXT.__auth_stubs: 0x1fe0
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0x1ed8
+  __TEXT.__constg_swiftt: 0x8a8
+  __TEXT.__swift5_typeref: 0xe9d
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0xb57
-  __TEXT.__swift5_fieldmd: 0xc40
+  __TEXT.__swift5_reflstr: 0xc07
+  __TEXT.__swift5_fieldmd: 0xcb0
   __TEXT.__swift5_proto: 0x170
   __TEXT.__swift5_types: 0xc4
-  __TEXT.__cstring: 0x18d7
-  __TEXT.__oslogstring: 0xa3d
-  __TEXT.__swift5_capture: 0x204
+  __TEXT.__cstring: 0x14a7
+  __TEXT.__oslogstring: 0xa9d
+  __TEXT.__swift5_capture: 0x238
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__unwind_info: 0xd98
-  __TEXT.__eh_frame: 0xe50
+  __TEXT.__unwind_info: 0xd68
+  __TEXT.__eh_frame: 0x1038
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x30a
+  __TEXT.__objc_methname: 0x31f
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH_CONST.__auth_ptr: 0x568
-  __AUTH_CONST.__const: 0x1458
-  __AUTH_CONST.__objc_const: 0x1460
+  __AUTH_CONST.__auth_got: 0xff0
+  __AUTH_CONST.__auth_ptr: 0x580
+  __AUTH_CONST.__const: 0x13d0
+  __AUTH_CONST.__objc_const: 0x1290
   __AUTH.__data: 0x88
   __DATA.__data: 0x6f0
-  __DATA.__bss: 0x2590
+  __DATA.__bss: 0x2510
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x1020
+  __DATA_DIRTY.__data: 0x12f0
   __DATA_DIRTY.__common: 0x20
-  __DATA_DIRTY.__bss: 0x700
+  __DATA_DIRTY.__bss: 0x780
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1240
-  Symbols:   257
-  CStrings:  263
+  Functions: 1226
+  Symbols:   267
+  CStrings:  243
 
Symbols:
+ _OBJC_CLASS_$_NSOrderedSet
+ _swift_allocBox
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_projectBox
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
- _CGRectApplyAffineTransform
- _CGRegionCreateDifferenceWithRegion
- _CGRegionCreateEmptyRegion
- _CGRegionCreateIntersectionWithRegion
- _CGRegionCreateUnionWithRegion
- _CGRegionCreateWithRect
- _CGRegionIsEmpty
- _objc_release_x9
- _objc_retain_x27
- _objc_retain_x9
- _swift_initStructMetadata
CStrings:
+ "%{public, signpost.description:begin_time}llu PastDeadline %{public}s"
+ "Accepting new connection %{public}s"
+ "AsyncProviderTask("
+ "agent failed to notify client %{public}s for %{public}s (details: %{public}s)"
+ "appIntentsRequest"
+ "appIntentsRequest: "
+ "array"
+ "client %{public}s disconnected"
+ "client %{public}s provided %{public}ld fragment%{public}s for [%{public}s]"
+ "completed %{public}s; async provider tasks still pending: %{public}ld"
+ "ignoring async provider task that completed late past its deadline: %{public}s"
+ "includeOffscreenSelectedElements"
+ "includeOffscreenSelectedElements: "
+ "initWithArray:"
+ "maximumOffscreenSubelements"
+ "maximumOffscreenSubelements: "
+ "maximumoffscreen"
+ "starting %{public}s with %{public}s until deadline"
+ "targetedAppBundleIdentifiers"
+ "targetedAppBundleIdentifiers: "
+ "timed out %{public}s; async provider tasks still pending: %{public}ld"
- "%{public}s"
- "Accepting new connection %s"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "ElementHierarchy(roots: "
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
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
- "agent failed to notify client %s (details: %{public}s)"
- "client %s disconnected"
- "client %{public}s provided %{public}ld fragments"
- "completed async provider task '%{public}s' for %{public}s"
- "ignoring completed async provider task for untracked request %{public}s: '%{public}s'"
- "includeAppIntentsPayloadDebugDescription"
- "includeAppIntentsPayloadDebugDescription: "
- "includeAppIntentsPayloads"
- "includeAppIntentsPayloads: "
- "invalid Collection: less than 'count' elements in collection"
- "starting async provider task '%{public}s' for %{public}s with %{public}s until deadline"
- "timed out async provider task '%{public}s' for %{public}s"

```
