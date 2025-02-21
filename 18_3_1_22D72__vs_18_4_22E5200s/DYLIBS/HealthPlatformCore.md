## HealthPlatformCore

> `/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore`

```diff

-5200.3.6.1.1
-  __TEXT.__text: 0xd8c6c
-  __TEXT.__auth_stubs: 0x3190
-  __TEXT.__objc_methlist: 0x1f8
-  __TEXT.__const: 0x2e80
-  __TEXT.__cstring: 0x3fb8
+5200.4.19.1.2
+  __TEXT.__text: 0xca700
+  __TEXT.__auth_stubs: 0x3160
+  __TEXT.__objc_methlist: 0x3a0
+  __TEXT.__const: 0x3070
+  __TEXT.__cstring: 0x3c18
   __TEXT.__constg_swiftt: 0x1c70
   __TEXT.__swift5_typeref: 0x1cdb
   __TEXT.__swift5_fieldmd: 0x1150

   __TEXT.__swift5_assocty: 0x148
   __TEXT.__swift5_proto: 0x1fc
   __TEXT.__swift5_types: 0x12c
-  __TEXT.__swift5_capture: 0x168c
+  __TEXT.__swift5_capture: 0x16ac
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__oslogstring: 0x34ff
+  __TEXT.__oslogstring: 0x35af
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2420
-  __TEXT.__eh_frame: 0x1710
+  __TEXT.__unwind_info: 0x2270
+  __TEXT.__eh_frame: 0x17b8
   __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0x13c7
+  __TEXT.__objc_methname: 0x145a
   __TEXT.__objc_methtype: 0x134
-  __DATA_CONST.__got: 0xce0
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__got: 0xce8
+  __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist2: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_selrefs: 0x7a8
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x18c8
+  __AUTH_CONST.__auth_got: 0x18b0
   __AUTH_CONST.__auth_ptr: 0x960
-  __AUTH_CONST.__const: 0x45f8
-  __AUTH_CONST.__objc_const: 0x25e8
+  __AUTH_CONST.__const: 0x4698
+  __AUTH_CONST.__objc_const: 0x2318
   __AUTH.__objc_data: 0x138
   __AUTH.__data: 0x2f8
-  __DATA.__data: 0x550
+  __DATA.__data: 0x540
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x810
   __DATA_DIRTY.__objc_data: 0x980
-  __DATA_DIRTY.__data: 0x3d00
+  __DATA_DIRTY.__data: 0x3d20
   __DATA_DIRTY.__bss: 0x2780
-  __DATA_DIRTY.__common: 0x1d0
+  __DATA_DIRTY.__common: 0x1b8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3481
-  Symbols:   424
-  CStrings:  885
+  Functions: 3349
+  Symbols:   445
+  CStrings:  869
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getFunctionTypeMetadata0
+ _swift_initStructMetadataWithLayoutString
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftWebKit
- _objc_release_x10
- _objc_retain_x10
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "[%{public}s] Comparing locales '%s' and '%s'"
+ "[%{public}s] Comparing versions '%s' and '%s'"
+ "[%{public}s] Could not get version or locale from metadata"
+ "[%{public}s] Failed to delete all searchable items: %{public}s"
+ "[%{public}s] Got a request to reindex %{public}ld searchable items"
+ "[%{public}s] Got a request to reindex all searchable items"
+ "[%{public}s] Great success, we were able to delete all of the searchable items from our index"
+ "[%{public}s] No persistent store exists"
+ "[%{public}s] Updating UserDefaults with new version: %s and locale: %s"
+ "[%{public}s] Version, locale, and store identifier match up; we don't need to do anything here!"
+ "searchableIndex:reindexAllSearchableItemsWithAcknowledgementHandler:"
+ "searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:"
+ "v40@0:8@16@24@?32"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
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
- "[%s] Comparing locales '%s' and '%s'"
- "[%s] Comparing versions '%s' and '%s'"
- "[%s] Could not get version or locale from metadata"
- "[%s] Failed to delete all searchable items: %{public}s"
- "[%s] Great success, we were able to delete all of the searchable items from our index"
- "[%s] No persistent store exists"
- "[%s] Updating UserDefaults with new version: %s and locale: %s"
- "[%s] Version, locale, and store identifier match up; we don't need to do anything here!"
- "invalid Collection: less than 'count' elements in collection"

```
