## diagnosticd

> `/usr/libexec/diagnosticd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-1965.0.0.0.0
+1966.0.6.0.0
   __TEXT.__text: 0x839c
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_stubs: 0x3e0
-  __TEXT.__const: 0x70
+  __TEXT.__const: 0x78
   __TEXT.__cstring: 0x14fc
   __TEXT.__objc_methname: 0x285
   __TEXT.__unwind_info: 0x1b8
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vF2ins/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/diagnosticd.build/DerivedSources/OSLogDarwin_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M60y6a/Binaries/libtrace_executables/install/TempContent/Objects/libtrace.build/diagnosticd.build/DerivedSources/OSLogDarwin_C.c"
```
