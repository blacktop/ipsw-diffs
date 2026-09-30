## Diagnostic-6008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6008.appex/Diagnostic-6008`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0x5fe0
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x94
+820.100.56.0.0
+  __TEXT.__text: 0x5c98
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x2fc
   __TEXT.__const: 0x125
-  __TEXT.__objc_methname: 0x57f
-  __TEXT.__cstring: 0xa87
+  __TEXT.__objc_methname: 0x594
+  __TEXT.__cstring: 0x837
   __TEXT.__constg_swiftt: 0x2a0
   __TEXT.__swift5_typeref: 0x12c
   __TEXT.__swift5_reflstr: 0x69c

   __TEXT.__oslogstring: 0x10f
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0xdd
-  __TEXT.__objc_methtype: 0x32a
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x350
+  __TEXT.__objc_methtype: 0x339
+  __TEXT.__unwind_info: 0x168
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0xd58
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_const: 0x948
+  __DATA.__objc_selrefs: 0x210
   __DATA.__objc_data: 0x4e0
   __DATA.__data: 0x6c0
   __DATA.__common: 0x8

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
-  Functions: 106
-  Symbols:   105
-  CStrings:  206
+  Functions: 105
+  Symbols:   107
+  CStrings:  193
 
Symbols:
+ _objc_release_x24
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x8
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy
CStrings:
+ "displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:navigationBarActions:completion:"
+ "v84@0:8@\"NSArray\"16i24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@\"NSArray\"68@?<v@?@\"NSString\"@\"NSError\">76"
+ "v84@0:8@16i24@28@36@44@52@60@68@?76"
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
- "displayInstructions:style:imageLocators:title:subtitle:iconLocator:options:completion:"
- "invalid Collection: less than 'count' elements in collection"
- "v76@0:8@\"NSArray\"16i24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSArray\"60@?<v@?@\"NSString\"@\"NSError\">68"
- "v76@0:8@16i24@28@36@44@52@60@?68"

```
