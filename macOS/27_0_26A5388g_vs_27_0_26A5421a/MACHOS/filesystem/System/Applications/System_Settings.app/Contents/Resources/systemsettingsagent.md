## systemsettingsagent

> `/System/Applications/System Settings.app/Contents/Resources/systemsettingsagent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2027.0.6.400.0
-  __TEXT.__text: 0x10c88
-  __TEXT.__auth_stubs: 0xa00
+2027.0.10.401.0
+  __TEXT.__text: 0x10ca0
+  __TEXT.__auth_stubs: 0xa10
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__const: 0x3de
-  __TEXT.__cstring: 0x506
+  __TEXT.__cstring: 0x536
   __TEXT.__swift5_typeref: 0x169
   __TEXT.__objc_methtype: 0x2a
   __TEXT.__swift5_capture: 0xbc
-  __TEXT.__oslogstring: 0xbcb
+  __TEXT.__oslogstring: 0xbdb
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1d8
   __TEXT.__swift5_reflstr: 0x1dc

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0x2b0
-  __TEXT.__eh_frame: 0x348
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__eh_frame: 0x370
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA.__objc_const: 0x218

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 213
-  Symbols:   249
-  CStrings:  125
+  Symbols:   250
+  CStrings:  126
 
Symbols:
+ _os_transaction_create
Functions:
~ sub_10000a778 : 572 -> 588
~ sub_10000aa98 -> sub_10000aaa8 : 108 -> 120
~ sub_10000abe8 -> sub_10000ac04 : 860 -> 856
CStrings:
+ "Detached task started (os_transaction held)"
+ "com.apple.systemsettingsagent.indexing"
- "Detached task started"
```
