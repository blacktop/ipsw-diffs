## PurpleReverseProxy

> `/usr/libexec/PurpleReverseProxy`

```diff

-102.0.0.0.0
-  __TEXT.__text: 0x68ec
-  __TEXT.__auth_stubs: 0x810
+104.0.0.0.0
+  __TEXT.__text: 0x6934
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__const: 0x6c
-  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__gcc_except_tab: 0x110
   __TEXT.__cstring: 0x13f0
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__auth_got: 0x410
+  __TEXT.__unwind_info: 0x1f8
+  __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__cfstring: 0xe80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 2E0CAA2A-92DB-399C-AA95-E563013062E7
+  UUID: 53367E66-0AB2-3497-868B-63077C5AA7E4
   Functions: 105
-  Symbols:   148
+  Symbols:   149
   CStrings:  320
 
Symbols:
+ _dispatch_async_f
Functions:
~ sub_100003510 : 176 -> 224
~ sub_100003628 -> sub_100003658 : 104 -> 100
~ sub_100003690 -> sub_1000036bc : 124 -> 376
~ sub_10000370c -> sub_100003834 : 376 -> 104
~ sub_100003888 -> sub_1000038a0 : 4 -> 188
~ sub_10000388c -> sub_10000395c : 140 -> 4

```
