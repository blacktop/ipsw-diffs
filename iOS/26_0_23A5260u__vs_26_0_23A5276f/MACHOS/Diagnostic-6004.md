## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

-1053.0.0.0.0
-  __TEXT.__text: 0x12640
+1066.0.11.0.0
+  __TEXT.__text: 0x12648
   __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x4bc
   __TEXT.__cstring: 0xff9
-  __TEXT.__objc_methname: 0xc78
+  __TEXT.__objc_methname: 0xc92
   __TEXT.__objc_classname: 0x118
   __TEXT.__objc_methtype: 0x368
   __TEXT.__const: 0x9d8

   __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__auth_ptr: 0x2d0
-  __DATA_CONST.__const: 0xdf8
+  __DATA_CONST.__const: 0xdd8
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc8

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D3EAACB3-0599-3EC6-B6ED-E2216169C7DB
+  UUID: E71CE3A6-FAF6-3540-82F0-4373A7528944
   Functions: 456
-  Symbols:   170
+  Symbols:   166
   CStrings:  355
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
Functions:
~ sub_100001fd8 -> sub_100001ea8 : 164 -> 168
~ sub_1000093d8 -> sub_1000092ac : 608 -> 612
CStrings:
+ "cStringUsingEncoding:"
+ "setActive:withOptions:error:"
- "cString"
- "setActive:error:"

```
