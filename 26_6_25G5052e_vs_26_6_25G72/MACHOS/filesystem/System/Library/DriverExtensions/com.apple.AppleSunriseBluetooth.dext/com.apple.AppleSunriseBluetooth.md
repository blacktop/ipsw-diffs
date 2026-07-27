## com.apple.AppleSunriseBluetooth

> `/System/Library/DriverExtensions/com.apple.AppleSunriseBluetooth.dext/com.apple.AppleSunriseBluetooth`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__osclassinfo`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

 100.0.0.0.0
   __TEXT.__text: 0x2ed6c
-  __TEXT.__auth_stubs: 0x900
+  __TEXT.__auth_stubs: 0x910
   __TEXT.__cstring: 0xaf30
   __TEXT.__const: 0x1580
   __TEXT.__unwind_info: 0x888
   __TEXT.__oslogstring: 0x20f3
-  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__osclassinfo: 0x60

   - /System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   Functions: 943
-  Symbols:   1188
+  Symbols:   1189
   CStrings:  1630
 
Symbols:
+ _PE_i_can_has_debugger
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kDAtgb/Sources/AppleSunriseBluetooth_driverkit/Sunrise/dale/gl_device.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IRUNyv/Sources/AppleSunriseBluetooth_driverkit/Sunrise/dale/gl_device.cpp"
```
