## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-969.4.2.0.0
-  __TEXT.__text: 0xd40a0
-  __TEXT.__auth_stubs: 0x2460
+969.5.5.0.0
+  __TEXT.__text: 0xd3258
+  __TEXT.__auth_stubs: 0x2420
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x7a8
-  __TEXT.__objc_methlist: 0x8f38
-  __TEXT.__const: 0x2374
-  __TEXT.__gcc_except_tab: 0x1b30
+  __TEXT.__objc_methlist: 0xb4dc
+  __TEXT.__const: 0x25c4
+  __TEXT.__gcc_except_tab: 0x1b50
   __TEXT.__oslogstring: 0x589f
-  __TEXT.__cstring: 0x5f58
+  __TEXT.__cstring: 0x5c38
   __TEXT.__ustring: 0x1c
-  __TEXT.__swift5_typeref: 0x18fa
+  __TEXT.__swift5_typeref: 0x19a0
   __TEXT.__swift5_reflstr: 0x6e7
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__constg_swiftt: 0x157c

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x100
   __TEXT.__swift5_capture: 0xe40
+  __TEXT.__swift_as_entry: 0x184
+  __TEXT.__swift_as_ret: 0x1b0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4aa8
-  __TEXT.__eh_frame: 0x4534
+  __TEXT.__unwind_info: 0x4980
+  __TEXT.__eh_frame: 0x459c
   __TEXT.__objc_classname: 0x177f
-  __TEXT.__objc_methname: 0x1ef27
-  __TEXT.__objc_methtype: 0x6a7f
+  __TEXT.__objc_methname: 0x1ef93
+  __TEXT.__objc_methtype: 0x6aed
   __TEXT.__objc_stubs: 0x14f80
-  __DATA_CONST.__got: 0xef8
-  __DATA_CONST.__const: 0x2958
+  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__const: 0x2710
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x388
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x63c0
+  __DATA_CONST.__objc_selrefs: 0x6dd8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x1248
-  __AUTH_CONST.__auth_ptr: 0x658
-  __AUTH_CONST.__const: 0x3148
+  __AUTH_CONST.__auth_got: 0x1228
+  __AUTH_CONST.__auth_ptr: 0x660
+  __AUTH_CONST.__const: 0x34e8
   __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x15420
+  __AUTH_CONST.__objc_const: 0x110d8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x2c08
-  __AUTH.__data: 0x1360
+  __AUTH.__objc_data: 0x29d0
+  __AUTH.__data: 0x1398
   __DATA.__objc_ivar: 0xbac
-  __DATA.__data: 0x3820
+  __DATA.__data: 0x3880
   __DATA.__bss: 0x23c8
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x460

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
-  Functions: 5489
-  Symbols:   4469
-  CStrings:  6656
+  Functions: 5473
+  Symbols:   4550
+  CStrings:  6647
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_getExistentialTypeMetadata
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataSingleCase
- _swift_initStructMetadata
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
CStrings:
+ "@\"UIConversationContext\"16@0:8"
+ "T@\"UIConversationContext\",?,&,N"
+ "conversationContext"
+ "setConversationContext:"
+ "textView:insertInputSuggestion:"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
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
- "invalid Collection: less than 'count' elements in collection"

```
