## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1598.40.4.0.0
-  __TEXT.__text: 0x60134
+1598.60.5.0.0
+  __TEXT.__text: 0x602f4
   __TEXT.__auth_stubs: 0x1700
   __TEXT.__objc_stubs: 0x9420
   __TEXT.__objc_methlist: 0x3f74
   __TEXT.__const: 0x1d4
-  __TEXT.__cstring: 0x10d32
+  __TEXT.__cstring: 0x10dcd
   __TEXT.__objc_classname: 0x38b
   __TEXT.__objc_methtype: 0x183c
   __TEXT.__gcc_except_tab: 0xda8
   __TEXT.__objc_methname: 0xa7b4
-  __TEXT.__oslogstring: 0x8111
+  __TEXT.__oslogstring: 0x8177
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x1630
-  __DATA_CONST.__const: 0x13c0
-  __DATA_CONST.__cfstring: 0x117c0
+  __TEXT.__unwind_info: 0x1638
+  __DATA_CONST.__const: 0x13e0
+  __DATA_CONST.__cfstring: 0x11880
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__auth_got: 0xb90
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x468
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x53b8
   __DATA.__objc_selrefs: 0x2a08

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1776
+  Functions: 1779
   Symbols:   505
-  CStrings:  4872
+  CStrings:  4880
 
CStrings:
+ "/usr/bin/triagectl"
+ "Allowing remote invocation because on apple packet bridge"
+ "DeviceConfiguration"
+ "Got result %d for apple packet bridge check"
+ "IsComputePacketBridge"
+ "RegionalSafetyAnalysisAssetVersion"
+ "TASK_TYPE_DEVICE_CONFIGURATION"
+ "logs/DeviceConfiguration"
+ "logs/RegionalSafetyAnalysis"
- "/usr/local/bin/triagectl"
```
