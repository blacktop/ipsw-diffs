## SettingsIntentExtension

> `/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension`

```diff

-3400.100.1.0.0
+3400.105.2.0.0
   __TEXT.__text: 0x398
   __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0x20

   __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48

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
   Functions: 10
-  Symbols:   54
+  Symbols:   62
   CStrings:  13
 
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
