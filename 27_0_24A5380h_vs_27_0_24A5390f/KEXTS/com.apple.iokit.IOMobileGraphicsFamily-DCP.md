## com.apple.iokit.IOMobileGraphicsFamily-DCP

> `com.apple.iokit.IOMobileGraphicsFamily-DCP`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-700.50.80.0.0
-  __TEXT.__cstring: 0x57af
+700.50.85.0.0
+  __TEXT.__cstring: 0x57f6
   __TEXT.__const: 0x32e8
-  __TEXT_EXEC.__text: 0x29834
+  __TEXT_EXEC.__text: 0x298c4
   __TEXT_EXEC.__auth_stubs: 0xe60
   __DATA.__data: 0xe8
   __DATA.__common: 0x2720

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 794
   Symbols:   0
-  CStrings:  471
+  CStrings:  472
 
Functions:
~ __ZN21IOMobileFramebufferAP21swap_submit_with_tagsEP12IOMFBSwapRecP12IOUserClientjPj : 4572 -> 4716
CStrings:
+ "SwapIdleBuffer received with no idle caching surface; dropping swap %u"
```
