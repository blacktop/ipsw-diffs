## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1404.0.0.0.0
-  __TEXT.__text: 0x17e3c
-  __TEXT.__auth_stubs: 0xd60
+1405.0.0.0.0
+  __TEXT.__text: 0x1804c
+  __TEXT.__auth_stubs: 0xd70
   __TEXT.__cstring: 0xd74
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x307e
+  __TEXT.__oslogstring: 0x313a
   __TEXT.__unwind_info: 0x358
-  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x2d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0BCCE789-2200-3696-9833-9B750EEF398C
+  UUID: F12ADC5F-5332-3678-8E8E-AD57255A10AF
   Functions: 377
-  Symbols:   240
-  CStrings:  487
+  Symbols:   241
+  CStrings:  490
 
Symbols:
+ _stat
Functions:
~ sub_100011154 : 1148 -> 1676
CStrings:
+ "%s: (%s) dev(%d) Check purge threshold - delta(%ld) last_id(%llu)"
+ "%s: (%s) dev(%d) Cooldown period for purge threshold - delta(%ld) last_id(%llu)"
+ "%s: (%s) dev(%d) stat failed <%d>:<%s> "
+ "%s: di %p (%s) dev(%d) - HFSIOC_GET_VERY_LOW_DISK blocks(%u) "
+ "%s: di %p (%s) dev(%d) - HFSIOC_GET_VERY_LOW_DISK failed <%d>:<%s> "
- "%s: di %p (%s) dev(%d) - HFSIOC_GET_DESIRED_DISK blocks(%u) "
- "%s: di %p (%s) dev(%d) - HFSIOC_GET_DESIRED_DISK failed <%d>:<%s> "

```
