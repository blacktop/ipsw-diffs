## notifyd

> `/usr/sbin/notifyd`

```diff

-348.120.4.0.0
-  __TEXT.__text: 0xb3fc sha256:6b3c124687583e14934385b93a1cb8a2ac09e702d0d85edf0b22c1bfe5c82a0d
-  __TEXT.__auth_stubs: 0x940 sha256:aa498fdef9322924ac50739f79969334e55c36beaabae953a1bc63a460e28d38
-  __TEXT.__const: 0x1b8 sha256:b7fdf6c7a71a1ab6258dc9e985d44c7f3fdb30319fb10d35140e7ad84113c1fd
-  __TEXT.__cstring: 0x1c56 sha256:29585e7cd98633a683b03cda064489912c6f7731bc0a80a1e3608b92e17cfca9
-  __DATA_CONST.__auth_got: 0x4a0 sha256:bb353d104c20149efdcb7109da9497616959d00772921e68da62b203743e93fe
-  __DATA_CONST.__got: 0x70 sha256:d2f96ad3b77df240f69eff3a61a40a0ee0e77de7146154deddcd149ff9a82217
-  __DATA_CONST.__const: 0xb30 sha256:2dcb3f1506899f112aca8c89cab4bf1e364518660750051700ff3096b06ebf34
-  __DATA.__data: 0x8 sha256:2bb47f903f0733f608aea175953db005468f10fad3b2670f388dd490dba77f08
+367.0.0.0.0
+  __TEXT.__text: 0xb38c sha256:49b39d48fb4b6dc96d7072a4146b6047317f40991a1bc34229600050d103b425
+  __TEXT.__auth_stubs: 0x950 sha256:fddf243c4e8b74fe51f8331e0a22e757d97fe794abdbb576e5137e9cf7e5462f
+  __TEXT.__const: 0x1a0 sha256:ebcb191580fb5d846133b6c882239ffb91ce1595c8441c6ead7f343111893a6a
+  __TEXT.__cstring: 0x1c31 sha256:09e5a1bde0ce588fb2dcc92f144f1d87a515b2b5ae408140c547ae2a07ae5398
+  __DATA_CONST.__const: 0xb30 sha256:0eb07394489f0f8f34686c6f0ed228199a99c8ce5e9eec66cee6a61f9f0529ad
+  __DATA_CONST.__auth_got: 0x4a8 sha256:5179d45745d9c8c2f232fc473d4f24cf70048fd190d0e637ddcf6460eb1d0a0f
+  __DATA_CONST.__got: 0x70 sha256:d6c3293efb0e347c1eea90a34c5af1086c6741102b4dd6d8bf66db70a047e693
+  __DATA.__data: 0x8 sha256:7700d15be1910fb2f43d7c4acb5347ee0304e1c0a7dbaf93b27116beddcafa0a
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
   __DATA.__bss: 0x2d0 sha256:fe2f74a1e0b16a66452888eb4d734bc455cf1304481bb495d59afa8cf9cae93b
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
