## dtfetchsymbolsd

> `/usr/libexec/dtfetchsymbolsd`

```diff

-31.0.0.0.0
-  __TEXT.__text: 0x6198
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__const: 0x20e
-  __TEXT.__cstring: 0x2d0
-  __TEXT.__swift5_typeref: 0x10d
+35.0.0.0.0
+  __TEXT.__text: 0x5c78
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__const: 0x25e
+  __TEXT.__cstring: 0x89
+  __TEXT.__swift5_typeref: 0x103
   __TEXT.__oslogstring: 0x201
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x68

   __TEXT.__swift5_reflstr: 0x16
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__unwind_info: 0x190
   __TEXT.__eh_frame: 0x118
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0xc0
-  __DATA.__common: 0xc0
-  __DATA.__bss: 0x3e0
+  __DATA.__data: 0xb8
+  __DATA.__common: 0x70
+  __DATA.__bss: 0x3b0
   - /Library/Apple/System/Library/PrivateFrameworks/Mercury.framework/Versions/A/Mercury
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: EA52A05E-B60F-3415-962F-DE3F328D37BC
-  Functions: 122
-  Symbols:   192
-  CStrings:  32
+  UUID: B9D63FE4-3C41-3290-80E2-3B73D67AF441
+  Functions: 115
+  Symbols:   186
+  CStrings:  19
 
Symbols:
+ _$ss20__StaticArrayStorageCN
+ __swiftImmortalRefCount
+ _objc_retain
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$sypN
- _swift_arrayDestroy
- _swift_initStackObject
- _swift_once
- _swift_setDeallocating
CStrings:
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
