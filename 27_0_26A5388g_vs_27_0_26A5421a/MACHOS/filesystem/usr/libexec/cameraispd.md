## cameraispd

> `/usr/libexec/cameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-20.57.4.0.0
-  __TEXT.__text: 0x8a12c
-  __TEXT.__auth_stubs: 0x18d0
+20.70.0.0.0
+  __TEXT.__text: 0x8a4b0
+  __TEXT.__auth_stubs: 0x18f0
   __TEXT.__objc_stubs: 0x980
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x630a
-  __TEXT.__const: 0x1fd90
+  __TEXT.__cstring: 0x63d5
+  __TEXT.__const: 0x1fe20
   __TEXT.__gcc_except_tab: 0xed0
-  __TEXT.__oslogstring: 0x4874
+  __TEXT.__oslogstring: 0x4922
   __TEXT.__objc_methname: 0x9dd
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methtype: 0x5f9
-  __TEXT.__unwind_info: 0xeb0
-  __DATA_CONST.__const: 0x8b10
+  __TEXT.__unwind_info: 0xec8
+  __DATA_CONST.__const: 0x8b30
   __DATA_CONST.__cfstring: 0x2660
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__auth_got: 0xc88
   __DATA_CONST.__got: 0x13d0
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x5c8
   __DATA.__objc_selrefs: 0x390
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x3af330
-  __DATA.__bss: 0x510
+  __DATA.__data: 0x3be330
+  __DATA.__bss: 0x528
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1377
-  Symbols:   1052
-  CStrings:  1516
+  Functions: 1381
+  Symbols:   1054
+  CStrings:  1523
 
Symbols:
+ _dlopen
+ _dlsym
CStrings:
+ "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
+ "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
+ "/usr/local/share/firmware/isp/0227_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "20.70"
+ "CMIOObjectGetPropertyData"
+ "CMIOObjectGetPropertyDataSize"
+ "ISP still in use by another session; keeping shared interface open\n"
- "20.57.4"
```
