## diskimagespawner

> `/usr/libexec/diskimagespawner`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-596.0.0.0.0
-  __TEXT.__text: 0x24edc
+598.0.0.0.0
+  __TEXT.__text: 0x24f5c
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0x1897
-  __TEXT.__gcc_except_tab: 0x2638
+  __TEXT.__gcc_except_tab: 0x2634
   __TEXT.__cstring: 0x17ce
   __TEXT.__oslogstring: 0x837
   __TEXT.__objc_classname: 0x96
Functions:
~ sub_100009c50 : 308 -> 316
~ sub_100011ee8 -> sub_100011ef0 : 528 -> 468
~ sub_100012148 -> sub_100012114 : 556 -> 736
CStrings:
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ujPbJ8/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ujPbJ8/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.giQfGG/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.giQfGG/Sources/DiskImages2/app/utils.cpp:179:13)]"
```
