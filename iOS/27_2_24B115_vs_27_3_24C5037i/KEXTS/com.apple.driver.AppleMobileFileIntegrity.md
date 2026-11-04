## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1171.40.9.0.0
+1171.60.2.0.0
   __TEXT.__cstring: 0xb98c
   __TEXT.__const: 0x1568
   __TEXT.__os_log: 0x3a5
-  __TEXT_EXEC.__text: 0x29b44
+  __TEXT_EXEC.__text: 0x29b70
   __TEXT_EXEC.__auth_stubs: 0x10c0
   __DATA.__data: 0x4f2
   __DATA.__common: 0xf0

   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 917
+  Functions: 918
   Symbols:   0
   CStrings:  1170
 
CStrings:
+ "AMFI: Only launchd can set the system service launch type (parent trusted? %d)\n"
- "AMFI: Only launchd can set the system service launch type (parent changed: %d)\n"
```
