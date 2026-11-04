## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-59.0.0.0.0
-  __TEXT.__text: 0x9254
-  __TEXT.__auth_stubs: 0x9a0
+59.1.0.0.0
+  __TEXT.__text: 0x92f4
+  __TEXT.__auth_stubs: 0x9b0
   __TEXT.__objc_stubs: 0xd80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x9e4
-  __TEXT.__gcc_except_tab: 0x9d4
+  __TEXT.__objc_methlist: 0x9ec
+  __TEXT.__gcc_except_tab: 0xa40
   __TEXT.__const: 0x1e8
   __TEXT.__cstring: 0xd27
   __TEXT.__oslogstring: 0xaa5
-  __TEXT.__objc_methname: 0x188e
+  __TEXT.__objc_methname: 0x18ae
   __TEXT.__objc_classname: 0x1ae
-  __TEXT.__objc_methtype: 0x6a8
+  __TEXT.__objc_methtype: 0x6b3
   __TEXT.__swift5_typeref: 0xa8
   __TEXT.__constg_swiftt: 0x19c
   __TEXT.__swift5_reflstr: 0x58

   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x490
+  __TEXT.__unwind_info: 0x498
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x1460

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0xf60
-  __DATA.__objc_selrefs: 0x6f0
+  __DATA.__objc_selrefs: 0x6f8
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x200
   __DATA.__data: 0x308

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 272
-  Symbols:   176
-  CStrings:  670
+  Functions: 273
+  Symbols:   177
+  CStrings:  671
 
Symbols:
+ _IOHIDEventCreateVendorDefinedEvent
Functions:
~ sub_1dc4 : 444 -> 404
- sub_2230
- sub_2450
+ sub_6fa8
+ sub_7a44
+ sub_7ea0
CStrings:
+ "@56@0:8Q16I24I28I32*36q44I52"
+ "parseInputReport:"
+ "vendorDefinedEvent:usagePage:usage:version:data:length:options:"
- "@40@0:8r*16Q24Q32"
- "parseInputReport:withLength:withTimestamp:"
```
