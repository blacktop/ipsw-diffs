## NetFS

> `/System/Library/Frameworks/NetFS.framework/Versions/A/NetFS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-64.100.2.0.0
-  __TEXT.__text: 0xb280
-  __TEXT.__auth_stubs: 0xa30
+64.160.2.0.0
+  __TEXT.__text: 0xb308
+  __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x98
   __TEXT.__oslogstring: 0x807

   __TEXT.__objc_methname: 0x2f9
   __TEXT.__objc_methtype: 0x277
   __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 203
-  Symbols:   424
+  Symbols:   426
   CStrings:  271
 
Symbols:
+ __DefaultRuneLocale
+ ___maskrune
Functions:
~ _FindPluginBySchemeInLibrary : 456 -> 592
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FLIhFu/Sources/NetFSFramework/URLMount.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtAQgX/Sources/NetFSFramework/URLMount.c"
```
