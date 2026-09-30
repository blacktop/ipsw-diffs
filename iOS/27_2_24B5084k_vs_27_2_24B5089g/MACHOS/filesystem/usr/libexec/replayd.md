## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-765.9.1.0.0
-  __TEXT.__text: 0xb94f4
+765.11.1.0.0
+  __TEXT.__text: 0xb96d0
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0xf320
   __TEXT.__objc_methlist: 0x74a0
   __TEXT.__const: 0x3e4
   __TEXT.__gcc_except_tab: 0xfc8
   __TEXT.__objc_methname: 0x15f58
-  __TEXT.__oslogstring: 0x166f4
-  __TEXT.__cstring: 0x17c86
+  __TEXT.__oslogstring: 0x167e9
+  __TEXT.__cstring: 0x17cf7
   __TEXT.__objc_classname: 0xa44
   __TEXT.__objc_methtype: 0x43f5
-  __TEXT.__unwind_info: 0x33d8
+  __TEXT.__unwind_info: 0x33e0
   __DATA_CONST.__const: 0x2b00
   __DATA_CONST.__cfstring: 0x5d20
   __DATA_CONST.__objc_classlist: 0x278

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3680
+  Functions: 3682
   Symbols:   802
-  CStrings:  7382
+  CStrings:  7387
 
CStrings:
+ " [ERROR] %{public}s:%d pickerDidCancel rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [ERROR] %{public}s:%d pickerDidDismiss rejected: caller lacks ScreenCaptureKit private entitlement"
+ " [INFO] %{public}s:%d skipping invalid pid=%@"
+ "-[RPConnectionManager pickerDidCancel:forStream:]"
+ "-[RPConnectionManager pickerDidDismiss:forStream:isCancelled:]"
```
