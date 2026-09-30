## notifyd

> `/usr/sbin/notifyd`

```diff

-348.120.4.0.0
-  __TEXT.__text: 0xb3fc
-  __TEXT.__auth_stubs: 0x940
+348.160.3.0.0
+  __TEXT.__text: 0xb3bc
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1c56
-  __DATA_CONST.__auth_got: 0x4a0
+  __TEXT.__cstring: 0x1c61
+  __DATA_CONST.__auth_got: 0x4a8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xb30
   __DATA.__data: 0x8

   __DATA.__bss: 0x2d0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 779B7F77-AE38-3110-A065-90F6A7FDE615
+  UUID: 7B577522-AD70-3033-B8D5-D3638584E0FD
   Functions: 135
-  Symbols:   165
+  Symbols:   166
   CStrings:  281
 
Symbols:
+ ___memset_chk
Functions:
~ sub_100003c08 : 308 -> 316
~ sub_1000044d0 -> sub_1000044d8 : 1344 -> 1280
~ sub_100005f90 -> sub_100005f58 : 848 -> 840
CStrings:
+ "(strlen(buf) + strlen(name)) <= pnode->plen"
+ "_path_vnode_create_node"
+ "_path_vnode_create_nodes"
+ "pnode->plen <= sizeof(buf)"
- "(strlen(buf) + strlen(pnode->pname[i])) <= pnode->plen"
- "_path_node_update"
- "buf != NULL"
- "pnode->pname[i] != NULL"

```
