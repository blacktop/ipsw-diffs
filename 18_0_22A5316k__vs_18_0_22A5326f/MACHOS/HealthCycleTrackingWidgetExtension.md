## HealthCycleTrackingWidgetExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/HealthCycleTrackingWidgetExtension.appex/HealthCycleTrackingWidgetExtension`

```diff

-5132.0.0.0.0
+5138.0.1.1.0
   __TEXT.__text: 0x248
   __TEXT.__auth_stubs: 0x70
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x80

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 8
-  Symbols:   28
+  Symbols:   36
   CStrings:  0
 
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