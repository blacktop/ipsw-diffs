## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/Versions/A/PlugInKitDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-512.0.0.0.0
-  __TEXT.__text: 0x1ba24
+513.0.0.0.0
+  __TEXT.__text: 0x1bd2c
   __TEXT.__auth_stubs: 0xab0
   __TEXT.__objc_stubs: 0x3360
   __TEXT.__objc_methlist: 0x1008
   __TEXT.__const: 0x62
   __TEXT.__objc_methname: 0x31aa
-  __TEXT.__oslogstring: 0x32e9
-  __TEXT.__cstring: 0x1314
+  __TEXT.__oslogstring: 0x3338
+  __TEXT.__cstring: 0x1381
   __TEXT.__objc_classname: 0x171
   __TEXT.__objc_methtype: 0x752
   __TEXT.__gcc_except_tab: 0x504
-  __TEXT.__unwind_info: 0x490
-  __DATA_CONST.__const: 0x6d0
-  __DATA_CONST.__cfstring: 0x12e0
+  __TEXT.__unwind_info: 0x498
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__cfstring: 0x1300
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x568
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2768
   __DATA.__objc_selrefs: 0xe98

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 495
-  Symbols:   1402
-  CStrings:  1165
+  Functions: 497
+  Symbols:   1405
+  CStrings:  1168
 
Symbols:
+ GCC_except_table52
+ _PKDExcludedExtensionPointsKey
+ ___33-[PKDTransaction lockDownPlugIns]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e26_B32?0"PKDPlugIn"8Q16^B24l
- GCC_except_table48
CStrings:
+ "B32@?0@\"PKDPlugIn\"8Q16^B24"
+ "excludedExtensionPoints is only supported for application-scope lockdown requests"
+ "sparing %lu plug-in(s) from lockdown for excluded extension points: %{public}@"
```
