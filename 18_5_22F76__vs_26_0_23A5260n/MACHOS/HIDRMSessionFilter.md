## HIDRMSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/HIDRMSessionFilter.plugin/HIDRMSessionFilter`

```diff

 21.0.0.0.0
-  __TEXT.__text: 0xb20
-  __TEXT.__auth_stubs: 0x270
+  __TEXT.__text: 0x98c
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0xca
   __TEXT.__objc_methname: 0x20a

   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x1ff
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x128
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0B691CFE-A142-3F4F-BB19-203F02ECAC9C
+  UUID: BBF57F01-5E7A-3332-AC4A-D2A9C42C9824
   Functions: 40
-  Symbols:   55
+  Symbols:   48
   CStrings:  77
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release
+ _objc_release_x19
+ _objc_retain_x21
- ___chkstk_darwin
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x22
- _objc_release_x23
- _objc_retain_x20
- _objc_retain_x22
- _objc_retain_x3
Functions:
~ sub_13c0 -> sub_12e0 : 136 -> 100
~ sub_14b4 -> sub_13b0 : 708 -> 508
~ sub_1878 -> sub_16ac : 396 -> 232
~ sub_1a58 -> sub_17e8 : 80 -> 76

```
