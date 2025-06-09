## WatchdogClient

> `/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient`

```diff

-299.120.2.0.0
-  __TEXT.__text: 0x128c
-  __TEXT.__auth_stubs: 0x230
+321.0.0.0.0
+  __TEXT.__text: 0x1350
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x133
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__cstring: 0x13e
+  __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x118
+  __AUTH_CONST.__auth_got: 0x120
   __AUTH_CONST.__const: 0x48
   __DATA_DIRTY.__bss: 0x388
   - /usr/lib/libSystem.B.dylib
-  UUID: A2F56B67-3050-34FC-BE07-C0CB75A6FC24
+  UUID: 0C485C92-AD70-35D0-A315-B53156909D98
   Functions: 22
-  Symbols:   159
-  CStrings:  10
+  Symbols:   162
+  CStrings:  11
 
Symbols:
+ __WDOGClient_PollIsAlive.cold.2
+ ___block_descriptor_tmp.9
+ _dispatch_queue_get_threadid_4wdt
- ___block_descriptor_tmp.7
Functions:
~ __WDOGClient_PollIsAlive : 1148 -> 1300
~ __WDOGClient_ReplyIsAlive : 388 -> 432
CStrings:
+ "(tid:%llu)"

```
