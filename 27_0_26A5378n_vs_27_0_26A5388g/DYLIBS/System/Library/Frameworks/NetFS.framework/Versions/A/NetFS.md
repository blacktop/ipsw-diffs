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

-70.0.0.0.0
-  __TEXT.__text: 0xafbc
+71.0.0.0.0
+  __TEXT.__text: 0xb040
   __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x98
   __TEXT.__oslogstring: 0x807

   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x60
-  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__auth_got: 0x530
   __DATA.__data: 0x210
   __DATA.__bss: 0x1
   __DATA_DIRTY.__data: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 199
-  Symbols:   422
+  Symbols:   424
   CStrings:  221
 
Symbols:
+ __DefaultRuneLocale
+ ___maskrune
Functions:
~ _FindPluginBySchemeInLibrary : 456 -> 588
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IiBXAl/Sources/NetFSFramework/URLMount.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kMbYgZ/Sources/NetFSFramework/URLMount.c"
```
