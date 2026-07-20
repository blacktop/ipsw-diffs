## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-3283.0.9.502.1
-  __TEXT.__text: 0xe4d14
+3283.0.13.0.0
+  __TEXT.__text: 0xe4fa4
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x84c
-  __TEXT.__const: 0x8ba0
-  __TEXT.__cstring: 0x3b7c8
+  __TEXT.__const: 0x8bb0
+  __TEXT.__cstring: 0x3b8b1
   __TEXT.__objc_methname: 0x1ee7
   __TEXT.__oslogstring: 0x1dd3
   __TEXT.__objc_classname: 0x124
   __TEXT.__objc_methtype: 0x2b9a
-  __TEXT.__gcc_except_tab: 0x464
+  __TEXT.__gcc_except_tab: 0x468
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x7a

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3286
   Symbols:   1566
-  CStrings:  5383
+  CStrings:  5387
 
Functions:
~ _spaceman_alloc : 4144 -> 4156
~ sub_100025470 -> sub_10002547c : 3604 -> 3628
~ _omap_get : 628 -> 632
~ _nx_reaper_checkpoint_traverse : 1272 -> 1680
~ sub_10005e2b8 -> sub_10005e478 : 596 -> 640
~ sub_10008f27c -> sub_10008f468 : 1176 -> 1240
~ sub_10008f714 -> sub_10008f940 : 248 -> 260
~ sub_10008f80c -> sub_10008fa44 : 1808 -> 1872
~ sub_10008ff1c -> sub_100090194 : 264 -> 288
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "3283.0.13"
+ "apfs_sanity_check"
+ "reap list object 0x%llx first index %u larger than max index %u\n"
+ "reap list object 0x%llx free index %u larger than max index %u\n"
+ "reap list object 0x%llx last index %u larger than max index %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "3283.0.9.502.1"
- "reap list object 0x%llx first index %u larger than max %u\n"
- "reap list object 0x%llx free index %u larger than max %u\n"
- "reap list object 0x%llx last index %u larger than max %u\n"
```
