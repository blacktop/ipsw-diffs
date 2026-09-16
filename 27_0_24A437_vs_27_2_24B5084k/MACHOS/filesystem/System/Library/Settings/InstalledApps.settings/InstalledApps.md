## InstalledApps

> `/System/Library/Settings/InstalledApps.settings/InstalledApps`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

   __TEXT.__text: 0x234d4
   __TEXT.__auth_stubs: 0x1790
   __TEXT.__objc_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x22c
+  __TEXT.__objc_methlist: 0x234
   __TEXT.__const: 0x1fe6
   __TEXT.__cstring: 0xe11
   __TEXT.__oslogstring: 0x3c8

   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_types: 0x64
   __TEXT.__objc_classname: 0x137
+  __TEXT.__objc_methname: 0xa5c
   __TEXT.__objc_methtype: 0x1cf
   __TEXT.__swift5_capture: 0x21c
-  __TEXT.__objc_methname: 0xa33
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_cont: 0x5c
   __TEXT.__swift5_mpenum: 0x40

   __DATA_CONST.__auth_got: 0xbd0
   __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x580
-  __DATA.__objc_const: 0x580
-  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_const: 0x588
+  __DATA.__objc_selrefs: 0x268
   __DATA.__objc_data: 0x208
   __DATA.__data: 0xc78
   __DATA.__common: 0x60

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 676
   Symbols:   197
-  CStrings:  256
+  CStrings:  257
 
CStrings:
+ "profileConnectionDidReceiveAllowCloudSyncChangedNotification:userInfo:"
```
