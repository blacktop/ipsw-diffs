## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

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

-1617.0.3.0.0
-  __TEXT.__cstring: 0xa379
-  __TEXT.__os_log: 0x866a
+1617.0.9.0.0
+  __TEXT.__cstring: 0xa25c
+  __TEXT.__os_log: 0x85bf
   __TEXT.__const: 0x2018
-  __TEXT_EXEC.__text: 0x942b4
+  __TEXT_EXEC.__text: 0x94240
   __TEXT_EXEC.__auth_stubs: 0xd40
   __DATA.__data: 0x1f0
   __DATA.__common: 0x970

   __DATA_CONST.__got: 0x1f0
   Functions: 1974
   Symbols:   0
-  CStrings:  1150
+  CStrings:  1147
 
Functions:
~ sub_fffffe000a5d2e7c -> sub_fffffe000a5f16fc : 100 -> 148
~ sub_fffffe000a5d4f10 -> sub_fffffe000a5f37c0 : 252 -> 272
~ sub_fffffe000a63736c -> sub_fffffe000a655c30 : 2540 -> 2356
CStrings:
+ "smc-port-number"
+ "usb-c-port-number"
- "%s@%s: %s::%s: Client %p is requesting %umA wake and %umA sleep for port %u\n"
- "%s@%s: %s::%s: Client %p port %u has EDT current overrides of %umA wake and %umA sleep\n"
- "%s@%s: %s::%s: Granting %umA wake and %umA sleep based on override for port %u\n"
- "%s@%s: %s::%s: Port %u %umA/%umA wake and %umA/%umA sleep\n"
- "UsbCPortNumber"
```
