## filevaultd

> `/usr/libexec/filevaultd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__objc_methname`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-58.0.1.0.0
-  __TEXT.__text: 0x61dc
+58.0.2.0.0
+  __TEXT.__text: 0x62b4
   __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x200
+  __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0x190
   __TEXT.__const: 0x3a8
   __TEXT.__cstring: 0x114

   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x120
   __DATA.__objc_const: 0x270
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x150
   __DATA.__objc_data: 0x188
-  __DATA.__data: 0x1f0
+  __DATA.__data: 0x200
   __DATA.__common: 0x78
   __DATA.__bss: 0x280
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 122
   Symbols:   260
-  CStrings:  96
+  CStrings:  98
 
Functions:
~ sub_100001ba0 : 3372 -> 3588
~ sub_100003d2c -> sub_100003e04 : 84 -> 76
~ sub_100003d80 -> sub_100003e50 : 76 -> 88
~ sub_100003dcc -> sub_100003ea8 : 88 -> 84
CStrings:
+ "currentUser"
+ "isAdministrator"
```
