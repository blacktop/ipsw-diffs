## nehelper

> `/usr/libexec/nehelper`

```diff

-1838.80.4.0.0
-  __TEXT.__text: 0x205bc
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0x2460
+1838.102.2.0.0
+  __TEXT.__text: 0x21a74
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_stubs: 0x24c0
   __TEXT.__objc_methlist: 0x30c
   __TEXT.__const: 0x4c
-  __TEXT.__gcc_except_tab: 0x308
-  __TEXT.__objc_methname: 0x1c3b
-  __TEXT.__oslogstring: 0x3f30
-  __TEXT.__cstring: 0x56ce
+  __TEXT.__gcc_except_tab: 0x32c
+  __TEXT.__objc_methname: 0x1c8b
+  __TEXT.__oslogstring: 0x4377
+  __TEXT.__cstring: 0x57b1
   __TEXT.__objc_classname: 0x1a5
   __TEXT.__objc_methtype: 0x251
-  __TEXT.__unwind_info: 0x3d4
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x168
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xbc8
-  __DATA_CONST.__cfstring: 0x4b40
+  __DATA_CONST.__const: 0xc30
+  __DATA_CONST.__cfstring: 0x4be0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x12c0
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x1988
-  __DATA.__objc_selrefs: 0x938
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x210
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_const: 0x19a8
+  __DATA.__objc_selrefs: 0x950
+  __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8
   __DATA.__bss: 0x290

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8C53F66C-4858-3710-B1FA-18DC044B6237
-  Functions: 232
+  UUID: FD4C0916-79A7-3DC1-8F94-11ADC2D86628
+  Functions: 242
   Symbols:   373
-  CStrings:  2137
+  CStrings:  2177
 
Symbols:
+ _NEGetConsoleUserUID
+ _ne_session_get_boot_session_uuid
- ___NSArray0__struct
- ___NSDictionary0__struct
CStrings:
+ "%@ is trying to access information for %s but is not entitled to do so. Please add the com.apple.private.network.socket-delegate or the com.apple.private.necp.policies entitlement"
+ "%@: Cache was already fully populated"
+ "%@: Cannot populate synthesized UUID, count is wrong (%lu)"
+ "%@: Populating the cache with %lu %@UUID(s) for %@"
+ "%@: Populating the cache with UUIDs for %lu app rules"
+ "%@: Saving the cache"
+ "%lu UUIDs for %@ are already in the cache"
+ "979C0A62-49FE-4739-BDCB-CAC584AC832D"
+ "A synthetic UUID for %@ is already in the cache"
+ "B32@?0@8Q16^B24"
+ "Caching %lu UUID(s) for %@"
+ "Caching a synthetic UUID for %@"
+ "Denying add redirected address command because %@ does not have the %s entitlement"
+ "Denying clear redirected addresses command because %@ does not have the %s entitlement"
+ "Denying interface manager connection because %@ does not have the %s entitlement"
+ "Denying set domain dictionary command because %@ does not have the %s entitlement"
+ "Denying set match domains command because %@ does not have the %s entitlement"
+ "Denying set routes command because %@ does not have the %s entitlement"
+ "Denying settings manager connection because %@ does not have the %s entitlement"
+ "Denying test connection because %@ does not have the %s entitlement"
+ "Failed to get the current boot session UUID"
+ "Failed to load configuration %@"
+ "Failed to set SIOCSIFDIRECTLINK to 1 for %s: [%d] %s"
+ "No configuration ID provided for populating the cache"
+ "Removing UUIDs for %@"
+ "Synthentic UUID count is wrong (%lu)"
+ "T@\"NSObject<OS_dispatch_queue>\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "_spiEntitled"
+ "boot-uuid"
+ "cache-app-bundle-id"
+ "com.apple.commcenter.ne.cellularusage"
+ "com.apple.datausage.dns.multicast"
+ "com.apple.private.networkextension.spi"
+ "interface-direct-link"
+ "isEqualToArray:"
+ "isIdentifierExternal"
+ "matchPath"
+ "process%d"
+ "synthetic "
- "%@ is trying to access information for %@ but is not entitled to do so. Please add the com.apple.private.network.socket-delegate or the com.apple.private.necp.policies entitlement"
- "Denying connection from %s (%d) because it is missing the %s entitlement"
- "Denying connection from process %d because it is missing the %s entitlement"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSString\",R,N"
- "app-paths"

```
