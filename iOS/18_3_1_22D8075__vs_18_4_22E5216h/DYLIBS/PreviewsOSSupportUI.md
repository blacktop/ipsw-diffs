## PreviewsOSSupportUI

> `/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI`

```diff

-22.20.7.0.0
-  __TEXT.__text: 0x1f4a8
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x21c
-  __TEXT.__const: 0x1ea8
-  __TEXT.__cstring: 0xd20
+22.30.25.0.0
+  __TEXT.__text: 0x17c58
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x3ec
+  __TEXT.__const: 0x1da8
+  __TEXT.__cstring: 0xb34
   __TEXT.__oslogstring: 0x190
   __TEXT.__swift5_typeref: 0x868
   __TEXT.__constg_swiftt: 0x648

   __TEXT.__swift5_capture: 0x17c
   __TEXT.__swift5_proto: 0x1c4
   __TEXT.__swift5_types: 0xac
-  __TEXT.__unwind_info: 0x9f8
-  __TEXT.__eh_frame: 0x680
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__eh_frame: 0x6d0
   __TEXT.__objc_classname: 0x121
   __TEXT.__objc_methname: 0x91c
   __TEXT.__objc_methtype: 0x27d
   __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x268
+  __DATA_CONST.__objc_selrefs: 0x340
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__auth_ptr: 0x2b0
-  __AUTH_CONST.__const: 0x1b40
+  __AUTH_CONST.__const: 0x1ac0
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x1288
+  __AUTH_CONST.__objc_const: 0xf50
   __AUTH.__objc_data: 0x4e8
-  __AUTH.__data: 0x520
+  __AUTH.__data: 0x5a0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x7d8
+  __DATA.__data: 0x820
   __DATA.__bss: 0x3880
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS
   - /System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS
   - /System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport
   - /System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices
   - /System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

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
-  Functions: 983
-  Symbols:   230
-  CStrings:  274
+  Functions: 865
+  Symbols:   242
+  CStrings:  265
 
Symbols:
+ _OBJC_CLASS_$_UVFenceHandle
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x23
+ _objc_retain_x27
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_getTupleTypeMetadata2
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x26
- _objc_retain_x9
- _swift_arrayDestroy
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSingleCase
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ "identifier providerContext "
+ "preferences fenceHandle "
+ "update sceneContext "
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
