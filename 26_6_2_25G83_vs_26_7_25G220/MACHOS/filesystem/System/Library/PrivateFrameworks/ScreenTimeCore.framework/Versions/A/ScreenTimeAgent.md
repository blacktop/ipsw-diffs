## ScreenTimeAgent

> `System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-605.6.5.0.0
-  __TEXT.__text: 0x138b84
-  __TEXT.__auth_stubs: 0x20f0
+605.6.5.2.0
+  __TEXT.__text: 0x138bb4
+  __TEXT.__auth_stubs: 0x2100
   __TEXT.__objc_stubs: 0x12940
   __TEXT.__objc_methlist: 0xa22c
   __TEXT.__const: 0x4f18

   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x4438
+  __TEXT.__unwind_info: 0x4430
   __TEXT.__eh_frame: 0x4838
-  __DATA_CONST.__auth_got: 0x1088
+  __DATA_CONST.__auth_got: 0x1090
   __DATA_CONST.__got: 0x1148
   __DATA_CONST.__auth_ptr: 0x688
   __DATA_CONST.__const: 0x9e68

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 6138
-  Symbols:   1227
+  Symbols:   1228
   CStrings:  7250
 
Symbols:
+ _SecTaskGetCodeSignStatus
Functions:
~ sub_1000b53d8 : 1148 -> 816
~ sub_1000b5854 -> sub_1000b5708 : 204 -> 220
~ sub_1000b5920 -> sub_1000b57e4 : 928 -> 1292
~ sub_1000b6140 -> sub_1000b6170 : 100 -> 20
~ sub_1000b61a4 -> sub_1000b6184 : 20 -> 96
~ sub_1000b61b8 -> sub_1000b61e4 : 96 -> 100
CStrings:
+ "Expiring One More Minute for %{private}@"
+ "Updated declarations with Organization Settings: %{private}@"
- "Expiring One More Minute for %{public}@"
- "Updated declarations with Organization Settings: %{public}@"
```
