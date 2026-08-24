## appleh16camerad

> `/usr/libexec/appleh16camerad`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-6.14.1.0.0
-  __TEXT.__text: 0x86478
-  __TEXT.__auth_stubs: 0x16f0
+6.20.0.0.0
+  __TEXT.__text: 0x86a3c
+  __TEXT.__auth_stubs: 0x1740
   __TEXT.__objc_stubs: 0x9c0
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x6356
-  __TEXT.__const: 0x19b60
+  __TEXT.__cstring: 0x6463
+  __TEXT.__const: 0x19b80
   __TEXT.__gcc_except_tab: 0xfd0
-  __TEXT.__oslogstring: 0x437d
+  __TEXT.__oslogstring: 0x4467
   __TEXT.__objc_methname: 0x9f4
   __TEXT.__objc_classname: 0xa9
   __TEXT.__objc_methtype: 0x62a
-  __TEXT.__unwind_info: 0xe68
-  __DATA_CONST.__const: 0xa360
-  __DATA_CONST.__cfstring: 0x2320
+  __TEXT.__unwind_info: 0xe90
+  __DATA_CONST.__const: 0xa3c0
+  __DATA_CONST.__cfstring: 0x2360
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xb88
-  __DATA_CONST.__got: 0x1258
+  __DATA_CONST.__auth_got: 0xbb0
+  __DATA_CONST.__got: 0x1260
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0x5c8
   __DATA.__objc_selrefs: 0x3a0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x3722a8
-  __DATA.__bss: 0x1818
+  __DATA.__data: 0x3812a8
+  __DATA.__bss: 0x1840
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1339
-  Symbols:   975
-  CStrings:  1481
+  Functions: 1348
+  Symbols:   981
+  CStrings:  1491
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ __xpc_type_bool
+ _dlopen
+ _dlsym
+ _xpc_bool_get_value
+ _xpc_connection_copy_entitlement_value
CStrings:
+ "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
+ "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_02XX.dat"
+ "6.20"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "CMIOObjectGetPropertyData"
+ "CMIOObjectGetPropertyDataSize"
+ "EnforceClientEntitlement"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "com.apple.private.appleh16camerad.client"
- "6.14.1"
```
