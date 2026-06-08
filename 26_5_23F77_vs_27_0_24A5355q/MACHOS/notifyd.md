## notifyd

> `/usr/sbin/notifyd`

```diff

-348.120.4.0.0
-  __TEXT.__text: 0xb3fc
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1c56
-  __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x70
+367.0.0.0.0
+  __TEXT.__text: 0xb38c
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x1c31
   __DATA_CONST.__const: 0xb30
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x70
   __DATA.__data: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x2d0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 779B7F77-AE38-3110-A065-90F6A7FDE615
-  Functions: 135
-  Symbols:   165
-  CStrings:  281
+  UUID: B8EEF2C7-83BD-30CF-8572-4AF4DA81A6B0
+  Functions: 137
+  Symbols:   166
+  CStrings:  280
 
Symbols:
+ ___memset_chk
CStrings:
+ "(strlen(buf) + strlen(name)) <= pnode->plen"
+ "_path_vnode_create_node"
+ "_path_vnode_create_nodes"
+ "create_port_with_qlimit"
+ "kr == KERN_SUCCESS"
+ "pnode->plen <= sizeof(buf)"
- "(strlen(buf) + strlen(pnode->pname[i])) <= pnode->plen"
- "__notify_generate_common_port"
- "__notify_server_register_mach_port_3"
- "_path_node_update"
- "buf != NULL"
- "kstatus == KERN_SUCCESS"
- "pnode->pname[i] != NULL"

```
