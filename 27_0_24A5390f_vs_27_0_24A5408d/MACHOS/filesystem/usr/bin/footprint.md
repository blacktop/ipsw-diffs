## footprint

> `/usr/bin/footprint`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-364.0.0.0.0
-  __TEXT.__text: 0x21314
-  __TEXT.__auth_stubs: 0xce0
+365.0.0.0.0
+  __TEXT.__text: 0x215c0
+  __TEXT.__auth_stubs: 0xcf0
   __TEXT.__objc_stubs: 0x2560
   __TEXT.__objc_methlist: 0x131c
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x303f
+  __TEXT.__cstring: 0x3072
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methtype: 0x80c
   __TEXT.__gcc_except_tab: 0x43c
   __TEXT.__objc_methname: 0x25d4
   __TEXT.__ustring: 0xd0
   __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__unwind_info: 0x4d8
   __DATA_CONST.__const: 0x748
   __DATA_CONST.__cfstring: 0x12e0
   __DATA_CONST.__objc_classlist: 0xc8

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__auth_got: 0x688
+  __DATA_CONST.__got: 0x270
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x3200
+  __DATA.__objc_const: 0x3220
   __DATA.__objc_selrefs: 0xa78
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x250
   __DATA.__bss: 0x48c8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 453
-  Symbols:   1556
-  CStrings:  1102
+  Functions: 454
+  Symbols:   1560
+  CStrings:  1105
 
Symbols:
+ -[FPOutputFormatterPerfdata _emitTimeMeasurementForTime:metric:]
+ OBJC_IVAR_$_FPOutputFormatterPerfdata._dateFormatter
+ _pdunit_s
+ _pdwriter_record_label_dbl
Functions:
+ +[FPSharedCache instanceCache]
- +[FPSharedCache instanceCache]
~ -[FPOutputFormatterPerfdata initWithPath:] : 424 -> 496
~ -[FPOutputFormatterPerfdata startAtTime:] : 12 -> 104
+ -[FPOutputFormatterPerfdata _emitTimeMeasurementForTime:metric:]
~ -[FPOutputFormatterPerfdata endAtTime:] : 160 -> 200
~ -[FPOutputFormatterPerfdata .cxx_destruct] : 80 -> 92
CStrings:
+ "date"
+ "mach_absolute_time_ns"
+ "mach_continuous_time_ns"
```
