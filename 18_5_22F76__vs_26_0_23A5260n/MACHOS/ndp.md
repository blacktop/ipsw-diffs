## ndp

> `/usr/sbin/ndp`

```diff

-705.100.5.0.0
-  __TEXT.__text: 0x3494
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x9fe
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x178
+725.0.0.0.0
+  __TEXT.__text: 0x3878
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0xae7
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x58
   __DATA.__data: 0x50
   __DATA.__bss: 0x25e8
   __DATA.__common: 0x298
   - /usr/lib/libSystem.B.dylib
-  UUID: 002CADBA-1EA6-39D6-835D-8FBCA632A8AE
-  Functions: 44
-  Symbols:   130
-  CStrings:  180
+  UUID: 401806ED-78DE-3992-9F08-AAB96038737D
+  Functions: 48
+  Symbols:   136
+  CStrings:  191
 
Symbols:
+ _inet_ntop
+ _printb
+ _rtilist
+ rtilist.cold.1
+ rtilist.cold.2
+ rtilist.cold.3
Functions:
~ _main : 3080 -> 3000
+ sub_100001230
~ _dump : 1692 -> 1664
+ _rtilist
+ _printb
CStrings:
+ "        "
+ "       ndp -A wait [-nt]"
+ "       ndp -I [interface | delete]"
+ "       ndp -a[lntx]"
+ "       ndp -z[n]"
+ "    %s if=%s"
+ "  routers:"
+ "%s=%o"
+ "%s=%x"
+ ", expires=%s\n"
+ "Never"
+ "acndfIilprstA:HPRxwWz"
+ "flags"
+ "prefix: %s/%d\n"
+ "stateflags"
+ "sysctl(ICMPV6CTL_ND6_RTILIST)"
- "       ndp -I [interface|delete]"
- "       ndp -a[lnt]"
- "       ndp -x"
- "       ndp [-nt] -A wait"
- "acndfIilprstA:HPRxwW"

```
