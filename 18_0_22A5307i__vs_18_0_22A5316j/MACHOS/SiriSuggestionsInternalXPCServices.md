## SiriSuggestionsInternalXPCServices

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsInternalXPCServices.xpc/SiriSuggestionsInternalXPCServices`

```diff

-3400.113.1.0.0
-  __TEXT.__text: 0x14d0
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0x40
-  __TEXT.__const: 0x114
-  __TEXT.__cstring: 0x14d
-  __TEXT.__objc_methname: 0x1f0
-  __TEXT.__oslogstring: 0x97
+3400.118.1.0.0
+  __TEXT.__text: 0x2be8
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x58
+  __TEXT.__const: 0x134
+  __TEXT.__cstring: 0x4c0
+  __TEXT.__objc_methname: 0x269
+  __TEXT.__oslogstring: 0x207
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xa0
-  __TEXT.__swift5_typeref: 0x81
+  __TEXT.__constg_swiftt: 0xb0
+  __TEXT.__swift5_typeref: 0xaf
   __TEXT.__swift5_fieldmd: 0x40
   __TEXT.__swift5_types: 0xc
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0xe9
-  __TEXT.__swift5_capture: 0x34
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__eh_frame: 0xb8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x190
+  __TEXT.__swift5_capture: 0x88
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__eh_frame: 0x180
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x450
-  __DATA.__objc_selrefs: 0x50
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x140
+  __DATA.__objc_const: 0x460
+  __DATA.__objc_selrefs: 0x60
+  __DATA.__objc_data: 0x1d0
+  __DATA.__data: 0x168
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete
+  - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 47
-  Symbols:   69
-  CStrings:  63
+  Functions: 89
+  Symbols:   81
+  CStrings:  88
 
Symbols:
+ __swiftEmptyArrayStorage
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_release_x23
+ _objc_retain_x23
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "%!s(MISSING) UnInstalled - clearing phrases in SiriSuggestionsInternalXPCServices"
+ "Apps Installed %!s(MISSING) - Re-Building some parts of the AutoComplete index via SiriSuggestionsInternalXPCServices"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "SiriAutoCompleteIndexBuilder deletePhrasesFromApp with %!s(MISSING) function %!s(MISSING)"
+ "SiriAutoCompleteIndexBuilder updateIndexForAppInstall function done with updatedRecords - %!l(MISSING)d"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "buildAutoCompleteIndexWithFirstBuildPostOSInstall:with:"
+ "deletePhrasesForAppUnInstallsWithBundleIds:with:"
+ "invalid Collection: less than 'count' elements in collection"
+ "updateIndexForAppInstallWithBundleIds:with:"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?q>20"
+ "v32@0:8@\"NSArray\"16@?<v@?B>24"
+ "v32@0:8@\"NSArray\"16@?<v@?q>24"
+ "v32@0:8@16@?24"
- "buildAutoCompleteIndexWith:"
- "v24@0:8@?16"
- "v24@0:8@?<v@?q>16"

```
