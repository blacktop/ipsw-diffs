## tipsd

> `/usr/libexec/tipsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-866.2.3.0.0
-  __TEXT.__text: 0x17db8
-  __TEXT.__auth_stubs: 0xd70
+866.2.4.0.0
+  __TEXT.__text: 0x17e70
+  __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_stubs: 0x2e80
   __TEXT.__objc_methlist: 0xd88
   __TEXT.__const: 0x374

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__auth_got: 0x6d0
   __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0xe8
   __DATA.__objc_const: 0xc70

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 492
-  Symbols:   402
+  Symbols:   403
   CStrings:  927
 
Symbols:
+ _TPSHMManagerHomeAccessoryAddedNotificationString
Functions:
~ sub_100004c84 : 848 -> 936
~ sub_100006c3c -> sub_100006c94 : 108 -> 176
~ sub_100006ca8 -> sub_100006d44 : 72 -> 100
```
