## AppleEthernetRL

> `/System/Library/Extensions/AppleEthernetRL.kext/AppleEthernetRL`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-171.0.0.0.0
-  __TEXT.__cstring: 0x2a8f
+175.40.1.0.0
+  __TEXT.__cstring: 0x2ad5
   __TEXT.__const: 0x22888
   __TEXT.__os_log: 0x75
-  __TEXT_EXEC.__text: 0x27b1c
+  __TEXT_EXEC.__text: 0x27b60
   __TEXT_EXEC.__auth_stubs: 0x720
   __DATA.__data: 0x1e8
   __DATA.__common: 0x128

   __DATA_CONST.__got: 0xc0
   Functions: 580
   Symbols:   1154
-  CStrings:  343
+  CStrings:  344
 
Symbols:
+ __ZZN15AppleEthernetRL4stopEP9IOServiceE20kalloc_type_view_292
- __ZZN15AppleEthernetRL4stopEP9IOServiceE20kalloc_type_view_283
CStrings:
+ "[0x%llx] rl::%s(%d): failed to allocate essential timer event source\n"
```
