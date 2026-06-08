## milod

> `/usr/libexec/milod`

```diff

-62.0.3.0.0
-  __TEXT.__text: 0x120
+106.0.2.0.0
+  __TEXT.__text: 0x11c
   __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_stubs: 0x60
   __TEXT.__oslogstring: 0xe
   __TEXT.__cstring: 0x2c
+  __TEXT.__const: 0x2
   __TEXT.__objc_methname: 0x16
   __TEXT.__unwind_info: 0x68
+  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x60
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93EEC25C-E7EC-370E-9A83-FFFD2BCC9B9D
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 1413FFC8-EB04-3940-BC42-B7E8E5D62CEB
   Functions: 3
-  Symbols:   17
+  Symbols:   24
   CStrings:  7
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_1000008f0 -> sub_100000ae0 : 200 -> 196

```
