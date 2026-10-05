## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-446.40.35.0.0
-  __TEXT.__text: 0x4244
+446.40.44.0.0
+  __TEXT.__text: 0x42ac
   __TEXT.__const: 0x760
   __TEXT.__cstring: 0x5815
   __TEXT.__oslogstring: 0x39b

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 32
-  Symbols:   82
+  Functions: 33
+  Symbols:   83
   CStrings:  551
 
Symbols:
+ _os_eligibility_bring_up_daemon_4_network_prompt
Functions:
+ _os_eligibility_bring_up_daemon_4_network_prompt
CStrings:
+ "CA-BC"
+ "CA-PE"
- "CA-NB"
- "CA-NS"
```
