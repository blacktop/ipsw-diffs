## logd

> `/usr/libexec/logd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-1965.0.0.0.0
-  __TEXT.__text: 0x27f98
-  __TEXT.__auth_stubs: 0x1a30
+1966.0.6.0.0
+  __TEXT.__text: 0x27ff8
+  __TEXT.__auth_stubs: 0x1a40
   __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x288
-  __TEXT.__cstring: 0x4afa
+  __TEXT.__cstring: 0x4b1c
   __TEXT.__objc_methname: 0x3e2
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methtype: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0xd20
+  __DATA_CONST.__auth_got: 0xd28
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x120

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   Functions: 549
-  Symbols:   474
-  CStrings:  648
+  Symbols:   475
+  CStrings:  649
 
Symbols:
+ __os_trace_prefscachedir_path
Functions:
~ sub_10000af20 : 844 -> 856
~ sub_1000151ec -> sub_1000151f8 : 1800 -> 1884
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vF2ins/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/logd.build/DerivedSources/OSLogDarwin_C.c"
+ "Failed to create prefscachedir %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M60y6a/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/logd.build/DerivedSources/OSLogDarwin_C.c"
```
