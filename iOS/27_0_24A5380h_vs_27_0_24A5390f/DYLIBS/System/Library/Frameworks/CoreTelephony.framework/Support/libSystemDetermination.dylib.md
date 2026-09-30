## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-13478.3.1.3.0
-  __TEXT.__text: 0x6f654
+13482.1.0.0.0
+  __TEXT.__text: 0x6faa0
   __TEXT.__const: 0x3ef9
-  __TEXT.__gcc_except_tab: 0x597c
-  __TEXT.__cstring: 0x36a3
-  __TEXT.__oslogstring: 0x9d41
-  __TEXT.__unwind_info: 0x2418
+  __TEXT.__gcc_except_tab: 0x5988
+  __TEXT.__cstring: 0x36c4
+  __TEXT.__oslogstring: 0x9e3c
+  __TEXT.__unwind_info: 0x2420
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xdf8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 1798
   Symbols:   2959
-  CStrings:  1453
+  CStrings:  1458
 
CStrings:
+ "424 Bad Location received on WiFi. Suppressing WiFi PCSCF and retrying on cellular."
+ "No cellular PCSCF available after 424 Bad Location. Giving up."
+ "RCSRegRefreshTimer: already registered, re-arming timer."
+ "RCSRegistrationEvent-NoCellPcscf"
+ "Skipping WiFi PCSCF %s due to 424 Bad Location"
```
