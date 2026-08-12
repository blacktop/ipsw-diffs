## com.apple.DriverKit.AppleUserECM

> `/System/Library/DriverExtensions/com.apple.DriverKit.AppleUserECM.dext/com.apple.DriverKit.AppleUserECM`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-73.0.1.0.0
-  __TEXT.__text: 0x60e8
+73.0.2.0.0
+  __TEXT.__text: 0x60fc
   __TEXT.__auth_stubs: 0x4c0
   __TEXT.__const: 0xbb0
   __TEXT.__cstring: 0x68a
   __TEXT.__oslogstring: 0xcf7
-  __DATA_CONST.__const: 0xe00
+  __DATA_CONST.__const: 0xe40
   __DATA_CONST.__osclassinfo: 0x40
   __DATA_CONST.__auth_got: 0x260
   __DATA_CONST.__got: 0x38

   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/USBDriverKit.framework/USBDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 145
-  Symbols:   284
+  Functions: 146
+  Symbols:   285
   CStrings:  112
 
Symbols:
+ __NSConcreteGlobalBlock
Functions:
~ __ZN12AppleUserECM9Stop_ImplEP9IOService : 908 -> 928
+ sub_100001d48
~ __ZN12AppleUserECM8activateEv : 1192 -> 1188
```
