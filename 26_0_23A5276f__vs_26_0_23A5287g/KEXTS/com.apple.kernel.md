## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.0.122.0.1
-  __TEXT.__const: 0x34ba0
+12377.0.132.0.2
+  __TEXT.__const: 0x34bc0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7d1e2
-  __TEXT.__os_log: 0x3bf1f
+  __TEXT.__cstring: 0x7d3bf
+  __TEXT.__os_log: 0x3bf8f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xaca48
+  __DATA_CONST.__const: 0xac9f8
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__kalloc_type: 0x13f80
   __DATA_CONST.__assert: 0x5dc

   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x88ff30
+  __TEXT_EXEC.__text: 0x891728
   __TEXT_EXEC.__hib_text: 0xe38
   __TEXT_BOOT_EXEC.__bootcode: 0x5218
   __KLD.__text: 0x1818

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x3098
+  __KLDDATA.__const: 0x30d0
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x17de9
   __DATA.__lock_grp: 0x5b70
-  __DATA.__percpu: 0x6e88
-  __DATA.__common: 0x5c100
+  __DATA.__percpu: 0x6f08
+  __DATA.__common: 0x5c120
   __DATA.__bss: 0x96cc8
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x4d10

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x46f97
-  UUID: A9EF4BD6-3A69-3F2A-9698-FFBD6F7B195C
-  Functions: 20601
+  __LINKINFO.__symbolsets: 0x46fda
+  UUID: 90EE574F-F96C-3700-8BDC-4D92BB95FAFF
+  Functions: 20614
   Symbols:   0
-  CStrings:  19902
+  CStrings:  19915
 
CStrings:
+ "%s: %s: clearing SCF_PROTO_ATTACHED"
+ "%s: %s: proto count %d"
+ "%s: %s: setting SCF_PROTO_ATTACHED"
+ "%s: end 0x%lx is not page aligned @%s:%d"
+ "%s: gDramBase/gDramSize not initialized @%s:%d"
+ "%s: range crosses DRAM boundary. First inconsistent page 0x%lx %s DRAM @%s:%d"
+ "%s: start 0x%lx is not page aligned @%s:%d"
+ "VM_KERN_MEMORY_CPUTRACE"
+ "after in_pcbladdr addr %s laddr %s ipoa_boundif %u outif %s"
+ "bridge_interface_attach_protocol"
+ "bridge_interface_proto_attach_changed"
+ "calling in_pcbladdr addr %s laddr %s ipoa_boundif %u outif %s"
+ "in_pcbsetport error %d"
+ "in_pcbsetport returned lport %u"
+ "ip_output error %d"
+ "necp_socket_is_allowed_to_send_recv_v4 error %d"
+ "pmap_map_bd_with_options"
- "%s: ifp %s has address"
- "The ProductVersion from SystemVersionCompat.plist"
- "in_pcbconnect error %d"
- "osproductversioncompat"

```
