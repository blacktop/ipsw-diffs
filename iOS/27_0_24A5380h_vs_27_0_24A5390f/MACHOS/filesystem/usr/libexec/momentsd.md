## momentsd

> `/usr/libexec/momentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-415.0.0.0.0
-  __TEXT.__text: 0x2625c0
+416.0.0.0.0
+  __TEXT.__text: 0x262534
   __TEXT.__auth_stubs: 0x1d00
   __TEXT.__objc_stubs: 0x1e960
   __TEXT.__objc_methlist: 0x11e84
-  __TEXT.__cstring: 0x2798e
+  __TEXT.__cstring: 0x2797e
   __TEXT.__objc_classname: 0x1e55
   __TEXT.__objc_methtype: 0x368e
   __TEXT.__objc_methname: 0x39b38

   __TEXT.__unwind_info: 0x5548
   __TEXT.__eh_frame: 0xb28
   __DATA_CONST.__const: 0xc148
-  __DATA_CONST.__cfstring: 0x26840
+  __DATA_CONST.__cfstring: 0x26820
   __DATA_CONST.__objc_classlist: 0x810
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x630
-  __DATA_CONST.__objc_intobj: 0x3900
+  __DATA_CONST.__objc_intobj: 0x3918
   __DATA_CONST.__objc_arraydata: 0x1708
   __DATA_CONST.__objc_arrayobj: 0xb10
   __DATA_CONST.__objc_doubleobj: 0x5c0
Functions:
~ -[NSArray(MOExtensions) getDurationOfMOEventArray] : 204 -> 240
~ -[MORoutineServiceManager _fetchEarliestVisitDateInRoutineWithHandler:] : 672 -> 676
~ ___71-[MORoutineServiceManager _fetchEarliestVisitDateInRoutineWithHandler:]_block_invoke : 748 -> 568
```
