## PreviewsServices

> `/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices`

```diff

-21.20.7.0.0
-  __TEXT.__text: 0xa064
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x4e2
-  __TEXT.__cstring: 0xa96
+21.30.32.0.0
+  __TEXT.__text: 0xa818
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x158
+  __TEXT.__const: 0x552
+  __TEXT.__cstring: 0xcb6
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__oslogstring: 0x70
+  __TEXT.__oslogstring: 0xe8
   __TEXT.__swift5_typeref: 0x280
   __TEXT.__swift5_fieldmd: 0x2ac
   __TEXT.__constg_swiftt: 0x25c
   __TEXT.__swift5_reflstr: 0x1db
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_capture: 0xd8
+  __TEXT.__swift5_capture: 0xc8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__objc_classname: 0x90
-  __TEXT.__objc_methname: 0x418
-  __TEXT.__objc_methtype: 0x1a2
-  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__unwind_info: 0x324
+  __TEXT.__objc_classname: 0x92
+  __TEXT.__objc_methname: 0x444
+  __TEXT.__objc_methtype: 0x1ac
+  __TEXT.__objc_stubs: 0x240
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xde0
-  __DATA_CONST.__objc_selrefs: 0x120
+  __DATA_CONST.__objc_const: 0xe10
+  __DATA_CONST.__objc_selrefs: 0x130
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x510
+  __AUTH_CONST.__auth_got: 0x520
   __AUTH.__objc_data: 0x1b8
   __AUTH.__data: 0x260
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x490
-  __DATA.__bss: 0x590
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x4c0
+  __DATA.__bss: 0x610
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 310
-  Symbols:   413
-  CStrings:  177
+  Functions: 317
+  Symbols:   426
+  CStrings:  198
 
Symbols:
+ -[UVPropertyList data]
+ -[UVPropertyList data].cold.1
+ -[UVPropertyList dictionary].cold.1
+ -[UVPropertyList dictionary].cold.2
+ -[UVPropertyList initWithData:]
+ GCC_except_table21
+ _OBJC_IVAR_$_UVPropertyList._data
+ _OUTLINED_FUNCTION_1
+ _block_copy_helper.11
+ _block_copy_helper.21
+ _block_descriptor.13
+ _block_descriptor.23
+ _block_destroy_helper.12
+ _block_destroy_helper.22
+ _objc_msgSend$data
+ _objc_msgSend$dictionary
+ _objc_msgSend$initWithData:
- -[UVPropertyList _encodeWithAnyCoder:].cold.1
- GCC_except_table18
- _block_copy_helper.12
- _block_copy_helper.23
- _block_descriptor.14
- _block_descriptor.25
- _block_destroy_helper.13
- _block_destroy_helper.24
- _swift_bridgeObjectRetain_n
CStrings:
+ "\x02"
+ "@\"NSData\""
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSData\",R,N"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSString\",?,R,C"
+ "UVPropertyList data did not deserialize to a [String: Any] dictionary"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_data"
+ "initWithData:"
+ "invalid Collection: less than 'count' elements in collection"
- "T@\"NSDictionary\",R,N,V_dictionary"
- "UVPropertyList did not contain a [String: Any] dictionary"

```
