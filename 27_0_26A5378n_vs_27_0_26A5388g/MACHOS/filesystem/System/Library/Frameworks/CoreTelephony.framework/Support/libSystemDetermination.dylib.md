## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-13478.2.0.0.0
-  __TEXT.__text: 0x6f0a0
+13482.0.0.0.0
+  __TEXT.__text: 0x6f464
   __TEXT.__const: 0x3df9
-  __TEXT.__gcc_except_tab: 0x5918
-  __TEXT.__cstring: 0x2dab
-  __TEXT.__oslogstring: 0x9ccc
+  __TEXT.__gcc_except_tab: 0x592c
+  __TEXT.__cstring: 0x2dcc
+  __TEXT.__oslogstring: 0x9dbe
   __TEXT.__unwind_info: 0x23f8
   __TEXT.__auth_stubs: 0x13f0
   __DATA_CONST.__const: 0xdf8

   - /usr/lib/libobjc.A.dylib
   Functions: 1788
   Symbols:   2927
-  CStrings:  1440
+  CStrings:  1445
 
CStrings:
+ "424 Bad Location received on WiFi. Suppressing WiFi PCSCF and retrying on cellular."
+ "ImsRegistrationState: UE is Registered for %s on %{public}s%s (%s)"
+ "No cellular PCSCF available after 424 Bad Location. Giving up."
+ "RCSRegRefreshTimer: already registered, re-arming timer."
+ "RCSRegistrationEvent-NoCellPcscf"
+ "Skipping WiFi PCSCF %s due to 424 Bad Location"
- "ImsRegistrationState: UE is Registered for %s (0x%08x) on %{public}s%s (%s)"
```
