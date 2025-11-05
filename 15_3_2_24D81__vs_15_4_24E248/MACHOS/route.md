## route

> `/sbin/route`

```diff

-698.60.4.0.0
-  __TEXT.__text: 0x2e78
-  __TEXT.__auth_stubs: 0x3e0
+705.100.5.0.0
+  __TEXT.__text: 0x3bec
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__const: 0x28
-  __TEXT.__cstring: 0x84c
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x1f0
+  __TEXT.__cstring: 0xa22
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0x28
-  __DATA.__data: 0x54a
+  __DATA.__data: 0x75a
+  __DATA.__common: 0x61c
   __DATA.__bss: 0x30c
-  __DATA.__common: 0x5e4
   - /usr/lib/libSystem.B.dylib
-  UUID: BDBEE5FA-8410-3879-BA82-C4E9D31BF6A0
-  Functions: 39
-  Symbols:   69
-  CStrings:  136
+  UUID: 13399F88-DB73-3D5B-B3A0-427504D6A802
+  Functions: 36
+  Symbols:   70
+  CStrings:  175
 
Symbols:
+ _if_indextoname
+ _strcasecmp
- ___sprintf_chk
CStrings:
+ "\ngot message of size %ld on %s"
+ "# filtering flags 0x%08x no_flags 0x%08x ifindex %u ifname \"%s\"\n"
+ "bad interface name: \"%s\""
+ "broadcast"
+ "condemned"
+ "dead"
+ "deladdr"
+ "delclone"
+ "delmaddr"
+ "dynamic"
+ "empty interface index: \"%s\""
+ "get2"
+ "get_ext"
+ "get_silent"
+ "global"
+ "ifindex"
+ "ifinfo"
+ "ifinfo2"
+ "ifref"
+ "index: %u %s"
+ "interface index to big \"%s\""
+ "local"
+ "miss"
+ "modified"
+ "mulicast"
+ "newaddr"
+ "newmadd2r"
+ "newmaddr"
+ "no name for interface index: \"%s\""
+ "noifref"
+ "pinned"
+ "prcloning"
+ "proto3"
+ "proxy"
+ "redirect"
+ "resolve"
+ "router"
+ "unsuported parameter \"%s\""
+ "up"
+ "wascloned"
- "\ngot message of size %d on %s"

```
