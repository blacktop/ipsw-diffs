## XboxGamepad

> `/System/Library/DriverExtensions/XboxGamepad.dext/XboxGamepad`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__got`

```diff

-14.1.2.0.0
-  __TEXT.__text: 0x99f8
-  __TEXT.__auth_stubs: 0x500
+14.2.2.0.0
+  __TEXT.__text: 0x9c10
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__const: 0xcc8
   __TEXT.__cstring: 0x37a
-  __TEXT.__oslogstring: 0xeca
-  __DATA_CONST.__const: 0x1e20
+  __TEXT.__oslogstring: 0xf25
+  __DATA_CONST.__const: 0x1e60
   __DATA_CONST.__osclassinfo: 0x50
-  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x48
   __DATA.__data: 0x179
   __DATA.__common: 0x50

   - /System/DriverKit/System/Library/Frameworks/HIDDriverKit.framework/HIDDriverKit
   - /System/DriverKit/System/Library/Frameworks/USBDriverKit.framework/USBDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 276
-  Symbols:   372
-  CStrings:  118
+  Functions: 278
+  Symbols:   375
+  CStrings:  119
 
Symbols:
+ __ZN15IODispatchQueue13DispatchAsyncEU13block_pointerFvvE
+ __ZN9IOService9TerminateEyPFiP15OSMetaClassBase5IORPCE
+ ____ZN13XboxUSBDevice10Start_ImplEP9IOService_block_invoke_2
CStrings:
+ "[%s 0x%llx] Failed to obtain 'Default' queue. CopyDispatchQueue() returned %{mach.errno}d\n"
```
