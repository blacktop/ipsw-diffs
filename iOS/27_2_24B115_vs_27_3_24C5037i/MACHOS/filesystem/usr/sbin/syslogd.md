## syslogd

> `/usr/sbin/syslogd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

-409.40.3.0.0
-  __TEXT.__text: 0x13398
+409.60.2.0.0
+  __TEXT.__text: 0x134dc
   __TEXT.__auth_stubs: 0xe00
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x352c
+  __TEXT.__cstring: 0x3606
   __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__const: 0xf18
   __DATA_CONST.__auth_got: 0x700

   - /usr/lib/libbsm.0.dylib
   Functions: 222
   Symbols:   251
-  CStrings:  570
+  CStrings:  572
 
Functions:
~ sub_1000094e0 : 348 -> 672
CStrings:
+ "[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message prepending uid %lu request for uid %lu]"
+ "[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message prepending uid %lu's (gid %lu) request for gid %lu]"
```
