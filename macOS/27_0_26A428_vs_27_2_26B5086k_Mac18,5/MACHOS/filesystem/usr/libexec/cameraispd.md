## cameraispd

> `/usr/libexec/cameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-20.70.0.0.0
-  __TEXT.__text: 0x8b758
-  __TEXT.__auth_stubs: 0x18f0
-  __TEXT.__objc_stubs: 0x980
+20.104.2.0.0
+  __TEXT.__text: 0x8bde0
+  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x6586
-  __TEXT.__const: 0x1fe20
+  __TEXT.__cstring: 0x66b7
+  __TEXT.__const: 0x1ff10
   __TEXT.__gcc_except_tab: 0xed0
-  __TEXT.__oslogstring: 0x4922
-  __TEXT.__objc_methname: 0x9dd
+  __TEXT.__oslogstring: 0x49ff
+  __TEXT.__objc_methname: 0xa0c
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methtype: 0x5f9
-  __TEXT.__unwind_info: 0x1810
-  __DATA_CONST.__const: 0x8b38
-  __DATA_CONST.__cfstring: 0x28c0
+  __TEXT.__unwind_info: 0x1820
+  __DATA_CONST.__const: 0x8b18
+  __DATA_CONST.__cfstring: 0x2920
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xc88
-  __DATA_CONST.__got: 0x1400
+  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__got: 0x1408
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x5c8
-  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_selrefs: 0x3a0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x3be330
+  __DATA.__data: 0x5723c0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1380
-  Symbols:   1060
-  CStrings:  1545
+  Functions: 1384
+  Symbols:   1059
+  CStrings:  1559
 
Symbols:
+ __DefaultRuneLocale
- _dlopen
- _dlsym
CStrings:
+ "%08X-%04X-%04X-%04X-%012X"
+ "%s - CopyBuiltInCameraDeviceUID returned NULL on macOS — falling back to \"0\"; privacy indicator may not engage.\n"
+ "%s - CopyBuiltInCameraDeviceUID: unexpected kMGQProductType=%{public}@\n"
+ ","
+ "/usr/local/share/firmware/isp/2727_01XX.dat"
+ "/usr/local/share/firmware/isp/3527_02XX.dat"
+ "/usr/local/share/firmware/isp/3527_03XX.dat"
+ "/usr/local/share/firmware/isp/4227_01XX.dat"
+ "/usr/local/share/firmware/isp/4427_01XX.dat"
+ "/usr/local/share/firmware/isp/7127_02XX.dat"
+ "/usr/local/share/firmware/isp/7327_01XX.dat"
+ "/usr/local/share/firmware/isp/7327_02XX.dat"
+ "20.104.2"
+ "CopyBuiltInCameraDeviceUID"
+ "ProductType"
+ "Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n"
+ "Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n"
+ "characterAtIndex:"
+ "componentsSeparatedByString:"
- "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
- "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
- "20.70"
- "CMIOObjectGetPropertyData"
- "CMIOObjectGetPropertyDataSize"
```
