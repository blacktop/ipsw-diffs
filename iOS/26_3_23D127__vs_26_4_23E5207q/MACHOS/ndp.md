## ndp

> `/usr/sbin/ndp`

```diff

-730.80.3.0.0
-  __TEXT.__text: 0x3a9c
+741.0.0.0.0
+  __TEXT.__text: 0x3afc
   __TEXT.__auth_stubs: 0x310
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xb5b
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__cstring: 0xbc9
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__auth_got: 0x188
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x58

   __DATA.__bss: 0x25d4
   __DATA.__common: 0x298
   - /usr/lib/libSystem.B.dylib
-  UUID: 55C96367-59A9-3965-84B4-6F5FC3C1E1FD
-  Functions: 22
-  Symbols:   97
-  CStrings:  197
+  UUID: C131FA9B-7619-3F08-9B4C-007843721BBC
+  Functions: 24
+  Symbols:   99
+  CStrings:  201
 
Symbols:
+ get.cold.1
+ rtmsg.cold.1
Functions:
~ _main : 6360 -> 6424
~ _dump : 1688 -> 1676
~ _delete : 592 -> 576
~ _rtrlist : 672 -> 668
~ _set : 900 -> 884
~ _rtilist : 776 -> 820
~ _get : 356 -> 268
~ _rtmsg : 616 -> 576
CStrings:
+ "plist: truncated advertiser data"
+ "plist: truncated data"
+ "rtilist: truncated data"
+ "rtilist: truncated router data"

```
