## pppd

> `/usr/sbin/pppd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-1045.0.0.0.0
-  __TEXT.__text: 0x2cc08
+1045.0.0.0.1
+  __TEXT.__text: 0x2cbf8
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__const: 0x708
   __TEXT.__cstring: 0x8db7

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 627
-  Symbols:   944
+  Functions: 626
+  Symbols:   943
   CStrings:  1434
 
Symbols:
- _options_from_user
Functions:
~ _main : 4476 -> 4468
- _options_for_tty
```
