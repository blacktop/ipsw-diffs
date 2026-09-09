## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 5411.101.0.0.0
-  __TEXT.__text: 0x2db04
+  __TEXT.__text: 0x2db1c
   __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_stubs: 0x3100
   __TEXT.__objc_methlist: 0x1c48
Functions:
~ sub_29b4 : 9384 -> 9392
~ sub_25dec -> sub_25df4 : 2056 -> 2060
~ sub_267b0 -> sub_267bc : 752 -> 756
~ sub_2a980 -> sub_2a990 : 672 -> 676
~ sub_2d870 -> sub_2d884 : 360 -> 364
CStrings:
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"
```
