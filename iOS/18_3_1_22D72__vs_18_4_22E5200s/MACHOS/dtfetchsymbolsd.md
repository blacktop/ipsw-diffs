## dtfetchsymbolsd

> `/usr/libexec/dtfetchsymbolsd`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x6140
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__const: 0x20e
-  __TEXT.__cstring: 0x2d0
-  __TEXT.__swift5_typeref: 0x10d
+35.0.0.0.0
+  __TEXT.__text: 0x5878
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__const: 0x27e
+  __TEXT.__cstring: 0xb9
+  __TEXT.__swift5_typeref: 0x103
   __TEXT.__oslogstring: 0x201
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x68

   __TEXT.__swift5_reflstr: 0x16
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__unwind_info: 0x180
   __TEXT.__eh_frame: 0x118
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0xc0
-  __DATA.__common: 0xc0
-  __DATA.__bss: 0x3e0
+  __DATA.__data: 0xb8
+  __DATA.__common: 0x70
+  __DATA.__bss: 0x3b0
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Mercury.framework/Mercury
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 122
-  Symbols:   193
-  CStrings:  32
+  Functions: 109
+  Symbols:   190
+  CStrings:  20
 
Symbols:
+ _$ss20__StaticArrayStorageCN
+ __swiftImmortalRefCount
+ _objc_release_x24
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _$sSS6appendyySSF
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$sypN
- _objc_release_x25
- _swift_arrayDestroy
- _swift_initStackObject
- _swift_once
- _swift_setDeallocating
CStrings:
+ "com.apple.dt.fetchsymbolsd.handlerQueue"
- "Fatal error"
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
