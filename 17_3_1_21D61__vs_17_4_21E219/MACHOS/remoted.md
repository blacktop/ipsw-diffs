## remoted

> `/usr/libexec/remoted`

```diff

-127.40.2.0.0
-  __TEXT.__text: 0x3338c
-  __TEXT.__auth_stubs: 0x14b0
-  __TEXT.__objc_stubs: 0x1d00
-  __TEXT.__objc_methlist: 0x11f0
+131.102.1.0.0
+  __TEXT.__text: 0x339d4
+  __TEXT.__auth_stubs: 0x14c0
+  __TEXT.__objc_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0x11f8
   __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0x6621
-  __TEXT.__cstring: 0x19ad
-  __TEXT.__objc_methname: 0x1f33
+  __TEXT.__oslogstring: 0x67f5
+  __TEXT.__cstring: 0x19b4
+  __TEXT.__objc_methname: 0x1f3f
   __TEXT.__objc_classname: 0x279
   __TEXT.__objc_methtype: 0x6bd
-  __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__unwind_info: 0xaf4
-  __DATA_CONST.__auth_got: 0xa68
+  __TEXT.__gcc_except_tab: 0x5b8
+  __TEXT.__unwind_info: 0xb10
+  __DATA_CONST.__auth_got: 0xa70
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0xf20
   __DATA_CONST.__cfstring: 0x9a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x2340
-  __DATA.__objc_selrefs: 0x778
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0xa0
+  __DATA.__objc_selrefs: 0x780
   __DATA.__objc_ivar: 0x1ec
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1361
-  Symbols:   389
-  CStrings:  1455
+  Functions: 1360
+  Symbols:   390
+  CStrings:  1458
 
Symbols:
+ _xpc_connection_get_pid
CStrings:
+ "%{public}@> Accepting device connection (client=\"%s\")"
+ "%{public}s> Connect succeeded (client=\"%s\")"
+ "%{public}s> Got CONNECT command (client=\"%s\")"
+ "Accepting service connection for \"%{public}s\" (client=\"%s\")"
+ "Canceling client browse. (client=\"%s\")"
+ "Completed client browse (present-only). (client=\"%s\")"
+ "Completed immediate devices. (client=\"%s\")"
+ "Delivering device (client=\"%s\")"
+ "Disconnecting remote device %{public}s (client=\"%s\")"
+ "Fetching service %{public}s on %{public}s (client=\"%s\")"
+ "Listing local services exposed to %{public}s (client=\"%s\")"
+ "Listing services on %{public}s (client=\"%s\")"
+ "Registering client browse (present-only). (client=\"%s\")"
+ "Registering client browse. (client=\"%s\")"
+ "Resetting remote device %{public}s (client=\"%s\")"
+ "Sending device note %{public}s sensitive properties (client=\"%s\")"
+ "Unregistering client browse. (client=\"%s\")"
+ "deactivate"
+ "device_check_service: Unable to find service with name %{public}s (client=\"%s\")"
+ "device_get_service: Client lacks privilege to find service with name %{public}s (client=\"%s\")"
+ "device_get_service: Returning service \"%{public}s\" (client=\"%s\")"
+ "device_get_service: Unable to find service with name %{public}s (client=\"%s\")"
+ "device_get_unique: Returning device of type %d (client=\"%s\")"
+ "device_get_unique: Unable to find device with type %d (client=\"%s\")"
+ "device_list_local_services: Client lacks privilege (client=\"%s\")"
+ "device_list_services: Returning %zd/%d services for device %{public}s (client=\"%s\")"
+ "device_reset: Client lacks privilege to reset device (client=\"%s\")"
+ "device_set_alias: Client lacks privilege to name device (client=\"%s\")"
+ "device_timesync: Client lacks privilege (client=\"%s\")"
+ "pid/%d"
+ "service_handler: Client lacks privilege to interact with service with name %{public}s (client=\"%s\")"
+ "setsockopt(IPV6_BOUND_IF) failed %{darwin.errno}d"
+ "setting remote device %{public}s alias as %{public}s (client=\"%s\")"
- "%{public}@> Accepting device connection"
- "%{public}s> Connect succeeded"
- "%{public}s> Got CONNECT command"
- "Accepting service connection for \"%{public}s\""
- "Canceling client browse."
- "Completed client browse (present-only)."
- "Completed immediate devices."
- "Delivering device"
- "Disconnecting remote device %{public}s"
- "Fetching service %{public}s on %{public}s"
- "Listing local services exposed to %{public}s"
- "Listing services on %{public}s"
- "Registering client browse (present-only)."
- "Registering client browse."
- "Resetting remote device %{public}s"
- "Sending device note %{public}s sensitive properties"
- "Unregistering client browse."
- "device_check_service: Unable to find service with name %{public}s"
- "device_get_service: Client lacks privilege to find service with name %{public}s"
- "device_get_service: Returning handle to \"%{public}s\""
- "device_get_service: Unable to find service with name %{public}s"
- "device_get_unique: Returning device of type %d"
- "device_get_unique: Unable to find device with type %d"
- "device_list_local_services: Client lacks privilege"
- "device_list_services: Returning %zd/%d services for device %{public}s"
- "device_reset: Client lacks privilege to reset device"
- "device_set_alias: Client lacks privilege to name device"
- "device_timesync: Client lacks privilege"
- "service_handler: Client lacks privilege to interact with service with name %{public}s"
- "setting remote device %{public}s alias as %{public}s"

```
