## com.apple.DriverKit.AppleUserECM

> `/System/Library/DriverExtensions/com.apple.DriverKit.AppleUserECM.dext/com.apple.DriverKit.AppleUserECM`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__got`

```diff

-73.0.2.0.0
-  __TEXT.__text: 0x607c
-  __TEXT.__auth_stubs: 0x4c0
+73.40.6.0.0
+  __TEXT.__text: 0x62bc
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__const: 0xbb0
-  __TEXT.__cstring: 0x6d6
-  __TEXT.__oslogstring: 0xcf7
-  __DATA_CONST.__const: 0xe40
+  __TEXT.__cstring: 0x711
+  __TEXT.__oslogstring: 0xd2b
+  __DATA_CONST.__const: 0xe50
   __DATA_CONST.__osclassinfo: 0x40
-  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x38
   __DATA.__bss: 0x8
   __DATA.__common: 0x40

   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/USBDriverKit.framework/USBDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 146
-  Symbols:   285
-  CStrings:  112
+  Functions: 147
+  Symbols:   287
+  CStrings:  115
 
Symbols:
+ __ZN15IODispatchQueue17WakeupWithOptionsEPvy
+ __ZN15IODispatchQueue5SleepEPvy
+ __ZN16IODispatchSource9SetEnableEbPFiP15OSMetaClassBase5IORPCE
- __NSConcreteGlobalBlock
CStrings:
+ "%s::%s: timed out waiting for interruptCancelEvent\n"
+ "AppleUserECMInterruptDispatchQueue"
+ "deactivate_block_invoke"
```
