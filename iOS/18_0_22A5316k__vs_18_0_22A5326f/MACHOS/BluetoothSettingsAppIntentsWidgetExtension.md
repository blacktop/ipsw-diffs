## BluetoothSettingsAppIntentsWidgetExtension

> `/System/Library/ExtensionKit/Extensions/BluetoothSettingsAppIntentsWidgetExtension.appex/BluetoothSettingsAppIntentsWidgetExtension`

```diff

-440.46.0.0.0
+440.51.1.0.0
   __TEXT.__text: 0x7958
   __TEXT.__auth_stubs: 0x770
   __TEXT.__const: 0xfb4

   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x618
-  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x168

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 281
-  Symbols:   71
+  Symbols:   79
   CStrings:  38
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "com.apple.Preferences.BluetoothPowerToggle"
- "com.apple.springboard.BluetoothPowerToggle"

```
