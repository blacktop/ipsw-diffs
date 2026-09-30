## cupsd

> `/usr/sbin/cupsd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-531.1.0.0.0
-  __TEXT.__text: 0x3fa0c
+532.0.0.0.0
+  __TEXT.__text: 0x3fb98
   __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__cstring: 0x10c29
+  __TEXT.__cstring: 0x10c71
   __TEXT.__const: 0x340
   __TEXT.__oslogstring: 0x6b
   __TEXT.__unwind_info: 0x540

   - /usr/lib/libz.1.dylib
   Functions: 392
   Symbols:   532
-  CStrings:  2610
+  CStrings:  2613
 
Symbols:
+ _removefileat
- _rmdir
Functions:
~ sub_10001076c : 1580 -> 1624
~ sub_1000143a0 -> sub_1000143cc : 404 -> 604
~ sub_100014534 -> sub_100014628 : 24 -> 384
~ sub_10001454c -> sub_1000147a8 : 384 -> 24
~ sub_1000206a0 -> sub_100020794 : 1172 -> 1324
CStrings:
+ "Failed to get directory fd \"%s\" - %s"
+ "Skipping \"%s/%s\" - %s"
+ "WebInterface"
```
