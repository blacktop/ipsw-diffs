## com.apple.filesystems.webdav

> `com.apple.filesystems.webdav`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__got`

```diff

-403.100.1.0.0
-  __TEXT.__cstring: 0x828
+403.160.3.0.1
+  __TEXT.__cstring: 0x878
   __TEXT.__const: 0xd0
-  __TEXT_EXEC.__text: 0x5b64
+  __TEXT_EXEC.__text: 0x5c28
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x340
   __DATA.__common: 0x38
   __DATA.__bss: 0x818
-  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x30
-  Functions: 65
-  Symbols:   224
-  CStrings:  55
+  Functions: 66
+  Symbols:   229
+  CStrings:  57
 
Symbols:
+ _proc_find
+ _proc_rele
+ _proc_task
+ _sock_getsockopt
+ _webdav_check_agent_entitlement
CStrings:
+ "webdav_sendmsg: entitlement check = %d\n"
+ "webdav_sendmsg: sock_getsockopt() = %d\n"
```
