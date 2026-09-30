## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__dof_VirtualAu`
- `__TEXT.__dof_Aggregate`
- `__TEXT.__dof_VirtualA0`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1451.208.0.0.0
-  __TEXT.__text: 0x550bb4
+1451.209.0.0.0
+  __TEXT.__text: 0x551444
   __TEXT.__realtime: 0x14a38
   __TEXT.__auth_stubs: 0x2a40
-  __TEXT.__objc_stubs: 0x12a0
+  __TEXT.__objc_stubs: 0x1280
   __TEXT.__init_offsets: 0x104c
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0xb4938
-  __TEXT.__cstring: 0x376f2
-  __TEXT.__gcc_except_tab: 0x65bec
+  __TEXT.__const: 0xb4910
+  __TEXT.__cstring: 0x37739
+  __TEXT.__gcc_except_tab: 0x65c2c
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__swift5_capture: 0x168
-  __TEXT.__oslogstring: 0x58ca1
-  __TEXT.__objc_methname: 0xf99
+  __TEXT.__oslogstring: 0x58deb
+  __TEXT.__objc_methname: 0xf89
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methtype: 0x422
   __TEXT.__constg_swiftt: 0xf8

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x15ab0
+  __TEXT.__unwind_info: 0x15b08
   __TEXT.__eh_frame: 0x730
-  __DATA_CONST.__const: 0x296b0
+  __DATA_CONST.__const: 0x29728
   __DATA_CONST.__cfstring: 0x2ec0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x1538
   __DATA_CONST.__got: 0x540
   __DATA_CONST.__auth_ptr: 0x70
   __DATA.__objc_const: 0x630
-  __DATA.__objc_selrefs: 0x580
+  __DATA.__objc_selrefs: 0x578
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x2b8
   __DATA.__data: 0x5b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12517
-  Symbols:   836
-  CStrings:  12319
+  Functions: 12531
+  Symbols:   834
+  CStrings:  12326
 
Symbols:
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantIntegerNumber
CStrings:
+ "%25s:%-5d Applying global calibration of 0 dB for repaired mic '%s'"
+ "%25s:%-5d Failed to read repair state for syscfg key '%s' - skipping"
+ "%25s:%-5d Repair detected for mics hosted under syscfg key '%s' - state: %s"
+ "%25s:%-5d Repair detected for syscfg key '%s' - calibrating %s"
+ "%25s:%-5d Repair detected for syscfg key '%s', but it hosts no mic trim gains on this product - nothing to calibrate"
+ "%25s:%-5d Repaired Mic Check returned syscfg keys: %s"
+ "@@ Strips Sep 12 2026 08:23:41"
+ "Issue"
+ "Mismatch"
+ "Original"
+ "RepairedWithServicePart"
+ "RepairedWithUsedPart"
+ "Unsupported"
- "%25s:%-5d Back Glass repair detected"
- "%25s:%-5d Cover Glass repair detected"
- "%25s:%-5d Repaired Mic Check returned: %s"
- "@@ Strips Sep  3 2026 00:42:08"
- "I"
- "integerValue"
```
