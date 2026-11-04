## misd

> `/usr/libexec/misd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x21bc8
-  __TEXT.__auth_stubs: 0x1250
+408.60.5.502.1
+  __TEXT.__text: 0x22260
+  __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x39c
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xb718
+  __TEXT.__const: 0x168
+  __TEXT.__cstring: 0xbad0
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x915
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x6b7
-  __TEXT.__unwind_info: 0x7b8
-  __DATA_CONST.__const: 0xa18
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__const: 0x9d8
   __DATA_CONST.__cfstring: 0xba0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x930
+  __DATA_CONST.__auth_got: 0x920
   __DATA_CONST.__got: 0x2e0
   __DATA.__objc_const: 0x488
   __DATA.__objc_selrefs: 0x2c8
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3a0
-  __DATA.__common: 0xa0
+  __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 457
-  Symbols:   393
-  CStrings:  1758
+  Functions: 463
+  Symbols:   391
+  CStrings:  1783
 
Symbols:
+ _strlcpy
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
CStrings:
+ "\"%s\" %s job failed"
+ "\"%s\" pid %d already gone"
+ "\"%s\" pid %d exit"
+ "\"%s\" pid %d exited unexpectedly"
+ "%s: \"%s\" is %s"
+ "%s: \"%s\" is %s, deferring"
+ "%s: \"%s\" respawn failed"
+ "%s: %s already in use, trying next unit"
+ "%s: TERM to \"%s\" pid %d: %s"
+ "%s: [internal error] interface %p not pending attach"
+ "%s: [internal error] network %s already has bridge %s"
+ "%s: [internal error] started network %s has no gateway if"
+ "%s: bridge%d: name too long"
+ "%s: bridge_create, network %s"
+ "%s: cancelling interface %p pending attach on network %s"
+ "%s: dispatch_source_create failed for pid %d"
+ "%s: killing \"%s\" pid %d"
+ "%s: mis_difaddr, err %d, network %s"
+ "%s: network %s has no bridge"
+ "%s: network %s has no gateway interface, nothing to deconfigure"
+ "%s: no exit monitor for \"%s\" pid %d"
+ "%s: no network with a ready gateway interface needs \"%s\""
+ "%s: releasing name %s for network %s despite failed destroy"
+ "%s: start addr is the broadcast address, network %s"
+ "%s: start addr is the network address, network %s"
+ "(bridge, unnamed until started)"
+ "(int_if->mii_flags & MIS_INT_IF_FLAGS_ATTACH_PENDING) == 0"
+ "SIOCIFCREATE2 %s: %s"
+ "bridge_create"
+ "created interface %s"
+ "int_if->mii_network == network"
+ "mis_network_add_pending_internal_interface"
+ "mis_network_cancel_pending_internal_interface"
+ "mis_network_gateway_exists"
+ "mis_network_remove_pending_internal_interface"
+ "no leasable addresses on %s"
+ "rtadvd_begin_terminate"
+ "rtadvd_install_monitor"
+ "rtadvd_spawn"
+ "rtadvd_terminate_complete"
+ "rtadvd_unload"
+ "running"
+ "sending TERM to \"%s\" pid %d"
+ "started \"%s\" as pid %d"
+ "stopped \"%s\""
+ "terminating"
- "\"%s\" enabling job error %s(%ld)"
- "\"%s\" exit"
- "%s: %s already exists, deleting"
- "%s: bridge_create"
- "%s: failed to delete %s"
- "%s: mis_get_bridge_name"
- "%s: no network has configured rtadvd"
- "%s: start addr is not in subnet, network %s"
- "SIOCIFCREATE2: %m"
- "bridge_name != NULL"
- "com.apple.misd.%p"
- "creating interface: %s"
- "failed to create process termination queue"
- "mis_get_bridge_name"
- "mis_rtadvd.c"
- "rtadvd monitor process error"
- "rtadvd monitor process failed for process queue"
- "rtadvd semaphore create failed"
- "rtadvd_source != NULL"
- "sending TERM to  \"%s\" pid %d"
- "spawned \"%s\" as pid %d"
```
