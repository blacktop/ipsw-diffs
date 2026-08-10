## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-600.45.0.0.0
+600.53.0.0.0
   __TEXT.__const: 0x23a8
   __TEXT.__os_log: 0x9d48
   __TEXT.__cstring: 0x114b
-  __TEXT_EXEC.__text: 0x541e8
+  __TEXT_EXEC.__text: 0x541e4
   __TEXT_EXEC.__auth_stubs: 0x5e0
   __DATA.__data: 0x458
   __DATA.__common: 0x78
Functions:
~ __ZN13AppleProResHW12timerHandlerEP18IOTimerEventSource : 2880 -> 2896
~ __ZN13AppleProResHW5startEP9IOService : 5476 -> 5456
```
