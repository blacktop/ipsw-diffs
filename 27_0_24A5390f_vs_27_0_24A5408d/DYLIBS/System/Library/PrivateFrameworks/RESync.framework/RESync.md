## RESync

> `/System/Library/PrivateFrameworks/RESync.framework/RESync`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-453.0.5.502.1
-  __TEXT.__text: 0x78378
+453.2.1.0.0
+  __TEXT.__text: 0x78390
   __TEXT.__objc_methlist: 0x2d4
   __TEXT.__const: 0x1fe8
   __TEXT.__cstring: 0x6dee

   __AUTH_CONST.__objc_const: 0x5e8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__auth_got: 0x790
-  __AUTH.__thread_vars: 0x48
-  __AUTH.__thread_bss: 0x18
+  __AUTH.__thread_vars: 0x60
+  __AUTH.__thread_bss: 0x20
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x108
   __DATA.__common: 0x1148

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2333
-  Symbols:   3528
+  Symbols:   3529
   CStrings:  991
 
Symbols:
+ __ZN2re26IntrospectionExclusiveLock20m_exclusiveLockLevelE
Functions:
~ __ZN2re10introspectIcEERKNS_17IntrospectionBaseEb : 96 -> 120
```
