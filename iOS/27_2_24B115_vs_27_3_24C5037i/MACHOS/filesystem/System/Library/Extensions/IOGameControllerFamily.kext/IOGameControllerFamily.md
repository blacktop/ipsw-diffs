## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

-14.1.2.0.0
+14.2.2.0.0
   __TEXT.__const: 0x480
   __TEXT.__cstring: 0x104c
   __TEXT.__os_log: 0x1c18
-  __TEXT_EXEC.__text: 0x1aa3c
+  __TEXT_EXEC.__text: 0x1aa5c
   __TEXT_EXEC.__auth_stubs: 0x540
   __DATA.__data: 0xc8
   __DATA.__common: 0x290

   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0xe0
-  Functions: 673
-  Symbols:   773
+  Functions: 674
+  Symbols:   774
   CStrings:  299
 
Symbols:
+ __ZN22IOGCDynamicDeviceProbe5closeEP9IOServicej
Functions:
~ __ZN22IOGCDynamicDeviceProbe11handleCloseEP9IOServicej : 152 -> 32
+ __ZN22IOGCDynamicDeviceProbe5closeEP9IOServicej
```
