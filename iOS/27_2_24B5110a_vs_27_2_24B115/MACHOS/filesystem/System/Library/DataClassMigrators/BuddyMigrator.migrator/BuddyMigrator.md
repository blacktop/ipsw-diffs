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
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5411.2.4.0.0
-  __TEXT.__text: 0x2c1b8
+5411.2.5.0.0
+  __TEXT.__text: 0x2c1b4
   __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_stubs: 0x31e0
   __TEXT.__objc_methlist: 0x1c70
Functions:
~ sub_296c : 8992 -> 8988
CStrings:
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"
```
