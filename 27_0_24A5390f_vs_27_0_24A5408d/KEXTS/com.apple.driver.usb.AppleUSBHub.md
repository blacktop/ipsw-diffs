## com.apple.driver.usb.AppleUSBHub

> `com.apple.driver.usb.AppleUSBHub`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-1617.0.9.0.0
-  __TEXT.__cstring: 0x1eb9
-  __TEXT.__os_log: 0x1fbe
+1617.0.12.0.0
+  __TEXT.__cstring: 0x1e48
+  __TEXT.__os_log: 0x1f61
   __TEXT.__const: 0x68
-  __TEXT_EXEC.__text: 0x1b5b8
+  __TEXT_EXEC.__text: 0x1b08c
   __TEXT_EXEC.__auth_stubs: 0x3f0
   __DATA.__data: 0xc8
   __DATA.__common: 0x128

   __DATA_CONST.__kalloc_type: 0x1c0
   __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0xb8
-  Functions: 254
+  Functions: 253
   Symbols:   0
-  CStrings:  208
+  CStrings:  204
 
Functions:
- __ZN15AppleUSBHubPort19cableChangeOccurredEP18IOTimerEventSource
CStrings:
- "%s@%s: %s::%s: deferring power off\n"
- "%s@%s: %s::%s: powering off\n"
- "%s@%s: %s::%s: powering on\n"
- "cableChangeOccurred"
```
