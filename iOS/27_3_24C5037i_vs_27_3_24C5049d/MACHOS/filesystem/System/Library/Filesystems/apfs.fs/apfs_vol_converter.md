## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3288.60.7.0.0
-  __TEXT.__text: 0x5a350
-  __TEXT.__auth_stubs: 0xa10
+3288.60.11.0.1
+  __TEXT.__text: 0x5a568
+  __TEXT.__auth_stubs: 0xa30
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x750
-  __TEXT.__cstring: 0x120bd
-  __TEXT.__gcc_except_tab: 0x6a4
-  __TEXT.__unwind_info: 0xf48
-  __DATA_CONST.__const: 0xb20
+  __TEXT.__const: 0x7a0
+  __TEXT.__cstring: 0x120c2
+  __TEXT.__gcc_except_tab: 0x6ec
+  __TEXT.__unwind_info: 0xf70
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__cfstring: 0xb80
-  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__auth_got: 0x520
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__data: 0x370

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 911
-  Symbols:   187
+  Functions: 917
+  Symbols:   191
   CStrings:  1618
 
Symbols:
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZTINSt3__119__shared_weak_countE
CStrings:
+ "3288.60.11.0.1"
- "3288.60.7"
```
