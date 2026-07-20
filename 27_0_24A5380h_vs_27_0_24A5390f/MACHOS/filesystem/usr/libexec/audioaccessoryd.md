## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-40.33.1.0.0
-  __TEXT.__text: 0x257afc
+40.36.1.0.0
+  __TEXT.__text: 0x258aa8
   __TEXT.__auth_stubs: 0x3bb0
-  __TEXT.__objc_stubs: 0x1f220
-  __TEXT.__objc_methlist: 0xe8ac
-  __TEXT.__const: 0x4d00
+  __TEXT.__objc_stubs: 0x1f2c0
+  __TEXT.__objc_methlist: 0xe8bc
+  __TEXT.__const: 0x4d10
   __TEXT.__gcc_except_tab: 0x5a3c
   __TEXT.__cstring: 0x58a93
   __TEXT.__objc_classname: 0x1143
-  __TEXT.__objc_methname: 0x2d345
+  __TEXT.__objc_methname: 0x2d3c5
   __TEXT.__objc_methtype: 0x4209
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__oslogstring: 0x9d5a
+  __TEXT.__oslogstring: 0x9e5a
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x1ee4
-  __TEXT.__constg_swiftt: 0x210c
+  __TEXT.__constg_swiftt: 0x2114
   __TEXT.__swift5_reflstr: 0x1bbb
   __TEXT.__swift5_fieldmd: 0x1998
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x228
-  __TEXT.__swift5_capture: 0x1f94
+  __TEXT.__swift5_capture: 0x1fb8
   __TEXT.__swift5_proto: 0x3a4
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift_as_entry: 0x7c

   __TEXT.__swift_as_cont: 0xe8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x7240
+  __TEXT.__unwind_info: 0x7250
   __TEXT.__eh_frame: 0x2d80
-  __DATA_CONST.__const: 0xcce0
-  __DATA_CONST.__cfstring: 0xb9e0
+  __DATA_CONST.__const: 0xcd30
+  __DATA_CONST.__cfstring: 0xb980
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x228
-  __DATA_CONST.__objc_intobj: 0x330
+  __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x358
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__auth_got: 0x1de8
-  __DATA_CONST.__got: 0x1120
+  __DATA_CONST.__got: 0x1130
   __DATA_CONST.__auth_ptr: 0x7b8
   __DATA.__objc_const: 0x1fee8
-  __DATA.__objc_selrefs: 0x92e0
+  __DATA.__objc_selrefs: 0x9308
   __DATA.__objc_ivar: 0x1884
-  __DATA.__objc_data: 0x3668
+  __DATA.__objc_data: 0x3670
   __DATA.__data: 0x5940
   __DATA.__bss: 0x7630
   __DATA.__common: 0x3a8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12022
-  Symbols:   1688
-  CStrings:  16342
+  Functions: 12034
+  Symbols:   1690
+  CStrings:  16348
 
Symbols:
+ _OBJC_CLASS_$_DAExtensionRuntimeAssertion
+ _RPOptionStatusFlags
CStrings:
+ "-[AASourceDeviceManager _startScanningWithControlFlags:]_block_invoke_5"
+ "Failed to create DAExtensionRuntimeAssertion for UUID %s"
+ "Failed to execute runtime assertion for UUID %s: %@"
+ "No DADevice found for UUID %s, skipping runtime assertion"
+ "Runtime assertion requested for UUID %s (duration: %fs)"
+ "Using exsting extensionSession connection"
+ "daDeviceForBTIdentifier:"
+ "executeCommand:error:"
+ "initWithDevice:capabilityFlags:"
+ "setDuration:"
- "-[AASourceDeviceManager _startScanningWithControlFlags:]_block_invoke_6"
- "AudioAccessory1,"
- "AudioAccessory5,"
- "AudioAccessory6,"
```
