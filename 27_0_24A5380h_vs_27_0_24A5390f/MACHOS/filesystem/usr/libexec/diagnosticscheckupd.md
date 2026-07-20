## diagnosticscheckupd

> `/usr/libexec/diagnosticscheckupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x49198
+1374.0.27.0.0
+  __TEXT.__text: 0x492bc
   __TEXT.__auth_stubs: 0x15d0
-  __TEXT.__objc_stubs: 0x5b20
+  __TEXT.__objc_stubs: 0x5b40
   __TEXT.__objc_methlist: 0x380c
-  __TEXT.__cstring: 0x2f29
+  __TEXT.__cstring: 0x2ec9
   __TEXT.__objc_methname: 0x8251
   __TEXT.__objc_classname: 0xbe2
   __TEXT.__objc_methtype: 0x26bb
   __TEXT.__const: 0x1ea8
   __TEXT.__gcc_except_tab: 0xb84
-  __TEXT.__oslogstring: 0x34da
+  __TEXT.__oslogstring: 0x353a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1534
   __TEXT.__swift5_typeref: 0xbf3

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_cont: 0x38
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x1338
+  __TEXT.__unwind_info: 0x1340
   __TEXT.__eh_frame: 0x7e8
   __DATA_CONST.__const: 0x2ed8
   __DATA_CONST.__cfstring: 0x1680

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_intobj: 0xa20
-  __DATA_CONST.__objc_arraydata: 0x2b8
+  __DATA_CONST.__objc_intobj: 0xa38
+  __DATA_CONST.__objc_arraydata: 0x2c0
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x20
Functions:
~ sub_100038844 : 252 -> 744
~ sub_100038940 -> sub_100038b2c : 40 -> 4
~ sub_100038968 -> sub_100038b30 : 40 -> 4
~ sub_100038990 -> sub_100038b34 : 4 -> 40
~ sub_100038994 -> sub_100038b5c : 4 -> 40
~ sub_10003b150 -> sub_10003b33c : 1168 -> 968
CStrings:
+ "We have been asked to dismiss a view controller that we are not presenting, ignoring."
- "CheckerBoard completion: showing final completion screen without session polling"
```
