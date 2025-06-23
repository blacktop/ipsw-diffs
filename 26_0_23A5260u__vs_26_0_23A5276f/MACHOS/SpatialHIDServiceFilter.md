## SpatialHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/SpatialHIDServiceFilter.plugin/SpatialHIDServiceFilter`

```diff

-13.0.28.0.0
-  __TEXT.__text: 0x8138
+13.0.31.0.0
+  __TEXT.__text: 0x81a8
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0xd74
   __TEXT.__objc_classname: 0x2fa
-  __TEXT.__objc_methname: 0x217e
-  __TEXT.__objc_methtype: 0xde3
+  __TEXT.__objc_methname: 0x2184
+  __TEXT.__objc_methtype: 0xdf0
   __TEXT.__cstring: 0x50d
-  __TEXT.__const: 0xc5
+  __TEXT.__const: 0xcd
   __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__oslogstring: 0xb89
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__oslogstring: 0xb9e
+  __TEXT.__unwind_info: 0x2b0
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x2a8

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1a30
-  __DATA.__objc_selrefs: 0x890
+  __DATA.__objc_selrefs: 0x898
   __DATA.__objc_ivar: 0x138
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x8a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22FCE97D-1EC8-3A47-A199-A937EB08C5FE
+  UUID: A51C75C6-B0DE-3649-BCE6-047FAEB32356
   Functions: 296
   Symbols:   135
-  CStrings:  753
+  CStrings:  754
 
Functions:
~ sub_17a8 : 916 -> 908
~ sub_274c -> sub_2744 : 132 -> 140
~ sub_4f7c : 3596 -> 3684
~ sub_6258 -> sub_62b0 : 588 -> 612
CStrings:
+ "[%#llx] Haptics supported {\ncutoff time: %f\ntransients: (supported=%{bool}d, id=%d, duration=%f)\nhigh band: (supported=%{bool}d, id=%d, duration=%f)\nlow band: (supported=%{bool}d, id=%d, duration=%f)\n}"
+ "usage"
+ "{?=\"supported\"B\"waveformID\"S\"duration\"d}"
- "[%#llx] Haptics supported {\ncutoff time: %f\ntransients: (supported=%{bool}d, duration=%f)\nhigh band: (supported=%{bool}d, duration=%f)\nlow band: (supported=%{bool}d, duration=%f)\n}"
- "{?=\"supported\"B\"duration\"d}"

```
