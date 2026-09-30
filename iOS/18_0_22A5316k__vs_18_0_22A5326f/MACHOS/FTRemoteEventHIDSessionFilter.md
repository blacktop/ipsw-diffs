## FTRemoteEventHIDSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/FTRemoteEventHIDSessionFilter.plugin/FTRemoteEventHIDSessionFilter`

```diff

-31.0.0.0.0
+35.0.0.0.0
   __TEXT.__text: 0x3af8
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x68

   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 56
-  Symbols:   71
+  Symbols:   79
   CStrings:  98
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd

```
