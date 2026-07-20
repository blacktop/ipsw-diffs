## com.apple.iokit.IOHIDFamily

> `com.apple.iokit.IOHIDFamily`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-2360.0.4.0.0
+2360.0.6.0.0
   __TEXT.__cstring: 0x4d6d
   __TEXT.__os_log: 0x4921
   __TEXT.__const: 0x1d80
-  __TEXT_EXEC.__text: 0xa1cbc
+  __TEXT_EXEC.__text: 0xa1d2c
   __TEXT_EXEC.__auth_stubs: 0xd50
   __DATA.__data: 0xbea
   __DATA.__common: 0xe88

   __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 3845
+  Functions: 3846
   Symbols:   5363
   CStrings:  1236
 
Functions:
~ __ZN14IOHIDInterface21GetElementValues_ImplEjP18IOMemoryDescriptor : 1104 -> 1120
+ sub_fffffe000ab887e8
~ _OUTLINED_FUNCTION_80 : 20 -> 12
~ _OUTLINED_FUNCTION_81 : 12 -> 20
~ __ZN16IOHIDEventDriver39createDigitizerTransducerEventForReportEP19DigitizerTransduceryj : 4140 -> 4208
```
