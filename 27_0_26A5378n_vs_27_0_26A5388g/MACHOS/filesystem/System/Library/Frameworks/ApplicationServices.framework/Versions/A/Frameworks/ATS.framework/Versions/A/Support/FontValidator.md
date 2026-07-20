## FontValidator

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Support/FontValidator`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`

```diff

-599.0.0.0.0
+600.0.0.0.0
   __TEXT.__text: 0x126e0
   __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0xbe0

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x740
   __DATA.__objc_selrefs: 0x390
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B54j5R/Sources/ValidatorRules_executables/Validation/coresources/validatehighlevel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eQ4gfb/Sources/ValidatorRules_executables/Validation/coresources/validatehighlevel.c"
```
