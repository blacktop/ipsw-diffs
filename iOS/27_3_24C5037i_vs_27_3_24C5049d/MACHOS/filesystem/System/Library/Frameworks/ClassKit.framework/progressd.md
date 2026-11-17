## progressd

> `/System/Library/Frameworks/ClassKit.framework/progressd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
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

 152.2.1.0.0
-  __TEXT.__text: 0x176e70
+  __TEXT.__text: 0x176f08
   __TEXT.__auth_stubs: 0x1b80
   __TEXT.__lazy_helpers: 0x54
   __TEXT.__objc_stubs: 0x14fc0

   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__objc_classname: 0x187d
-  __TEXT.__objc_methtype: 0x3bef
+  __TEXT.__objc_methtype: 0x3bd1
   __TEXT.__oslogstring: 0xe5cc
   __TEXT.__cstring: 0x1cebe
   __TEXT.__objc_methname: 0x1be38
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ sub_100002c30 : 12 -> 8
~ sub_100159048 -> sub_100159044 : 12 -> 8
~ sub_10016f518 -> sub_10016f510 : 9024 -> 9144
~ sub_100172018 -> sub_100172088 : 112 -> 124
~ sub_1001763b8 -> sub_100176434 : 432 -> 460
CStrings:
+ "{os_unfair_recursive_lock_s=\"_os_unfair_recursive_lock_opaque\"[2I]}"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
```
