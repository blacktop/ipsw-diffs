## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

-14.1.2.0.0
+14.2.2.0.0
   __TEXT.__const: 0x480
   __TEXT.__cstring: 0x27de
   __TEXT.__os_log: 0x90fa
-  __TEXT_EXEC.__text: 0x2a858
+  __TEXT_EXEC.__text: 0x2a88c
   __TEXT_EXEC.__auth_stubs: 0x540
   __DATA.__data: 0xc8
   __DATA.__common: 0x2b8

   __DATA_CONST.__kalloc_type: 0x880
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0xe0
-  Functions: 993
-  Symbols:   1704
+  Functions: 994
+  Symbols:   1705
   CStrings:  619
 
Symbols:
+ __ZN22IOGCDynamicDeviceProbe5closeEP9IOServicej
Functions:
~ __ZN22IOGCDynamicDeviceProbe11handleCloseEP9IOServicej : 268 -> 168
+ __ZN22IOGCDynamicDeviceProbe5closeEP9IOServicej
```
