## nexusd

> `/usr/libexec/nexusd`

```diff

-780.15.0.0.0
-  __TEXT.__text: 0x770
+790.18.0.0.0
+  __TEXT.__text: 0x76c
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__cstring: 0x44
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x20
   __DATA.__bss: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 41396A13-B989-36C8-86E6-7B995EF6D300
+  UUID: ADE9BE35-4A88-3E52-8A89-D1B7BF7E84B3
   Functions: 12
-  Symbols:   77
+  Symbols:   73
   CStrings:  7
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_10000147c -> sub_10000139c : 104 -> 100

```
