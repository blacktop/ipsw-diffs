## remoted

> `/usr/libexec/remoted`

```diff

-202.40.9.0.0
-  __TEXT.__text: 0x43998
+202.40.12.0.0
+  __TEXT.__text: 0x438fc
   __TEXT.__auth_stubs: 0x1830
   __TEXT.__objc_stubs: 0x2460
   __TEXT.__objc_methlist: 0x1550
   __TEXT.__const: 0x1f2
-  __TEXT.__oslogstring: 0x844c
+  __TEXT.__oslogstring: 0x859c
   __TEXT.__cstring: 0x20dd
   __TEXT.__objc_methname: 0x24f5
   __TEXT.__objc_classname: 0x2f4
   __TEXT.__objc_methtype: 0x79b
-  __TEXT.__gcc_except_tab: 0x15dc
+  __TEXT.__gcc_except_tab: 0x15d8
   __TEXT.__unwind_info: 0xf28
   __DATA_CONST.__auth_got: 0xc28
   __DATA_CONST.__got: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 699DC4A6-C9F1-363F-82E9-C37EB4817379
+  UUID: 3B990D72-8F15-30AB-905F-35C0615617BC
   Functions: 1390
   Symbols:   494
   CStrings:  1913
Functions:
~ sub_100020de8 : 1312 -> 1168
~ sub_100027498 -> sub_100027408 : 440 -> 444
~ sub_1000276f0 -> sub_100027664 : 736 -> 732
~ sub_100027c98 -> sub_100027c08 : 892 -> 888
~ sub_100028014 -> sub_100027f80 : 612 -> 608
~ sub_1000285a4 -> sub_10002850c : 624 -> 620
CStrings:
+ "%{public}@> Accepting device connection (client=\"%{public}s\")"
+ "%{public}@> Connect succeeded for %s (client=\"%{public}s\")"
+ "%{public}s> Got CONNECT command (client=\"%{public}s\")"
+ "Accepting service connection for \"%{public}s\" (client=\"%{public}s\")"
+ "Authenticating device certificate on behalf of client... (client=\"%{public}s\")"
+ "Canceling client browse. (client=\"%{public}s\")"
+ "Completed client browse (present-only). (client=\"%{public}s\")"
+ "Completed immediate devices. (client=\"%{public}s\")"
+ "Delivering device (client=\"%{public}s\")"
+ "Disconnecting remote device %{public}s (client=\"%{public}s\")"
+ "Failed to copy certificate data. (client=\"%{public}s\")"
+ "Failed to copy certificate from identity: %d (client=\"%{public}s\")"
+ "Failed to copy key attributes. (client=\"%{public}s\")"
+ "Failed to copy key data. (client=\"%{public}s\")"
+ "Failed to copy private key from identity: %d (client=\"%{public}s\")"
+ "Fetching service %{public}s on %{public}s (client=\"%{public}s\")"
+ "Get device query: %{public}@ (client=\"%{public}s\")"
+ "Listing local services exposed to %{public}s (client=\"%{public}s\")"
+ "Listing services on %{public}s (client=\"%{public}s\")"
+ "No local identity available. (client=\"%{public}s\")"
+ "Registering client browse (present-only). (client=\"%{public}s\")"
+ "Registering client browse. (client=\"%{public}s\")"
+ "Resetting remote device %{public}s (client=\"%{public}s\")"
+ "Sending device note %{public}s sensitive properties (client=\"%{public}s\")"
+ "Successfully authenticated device certificate on behalf of client (client=\"%{public}s\")"
+ "Unregistering client browse. (client=\"%{public}s\")"
+ "device_authenticate: Failed to authenticate peer cert (client=\"%{public}s\")"
+ "device_authenticate: Failed to create cert from data (client=\"%{public}s\")"
+ "device_authenticate: No certificate data (client=\"%{public}s\")"
+ "device_check_service: Unable to find service with name %{public}s (client=\"%{public}s\")"
+ "device_get: Returning device of type %d (client=\"%{public}s\")"
+ "device_get: Unable to find device with type %d (client=\"%{public}s\")"
+ "device_get_service: Client lacks privilege to find service with name %{public}s (client=\"%{public}s\")"
+ "device_get_service: Returning service \"%{public}s\" (client=\"%{public}s\")"
+ "device_get_service: Unable to find service with name %{public}s (client=\"%{public}s\")"
+ "device_list_local_services: Client lacks privilege (client=\"%{public}s\")"
+ "device_list_services: Returning %zd/%d services for device %{public}s (client=\"%{public}s\")"
+ "device_reset: Client lacks privilege to reset device (client=\"%{public}s\")"
+ "device_set_alias: Client lacks privilege to name device (client=\"%{public}s\")"
+ "device_timesync: Client lacks privilege (client=\"%{public}s\")"
+ "service_handler: Client lacks privilege to interact with service with name %{public}s (client=\"%{public}s\")"
+ "setting remote device %{public}s alias as %{public}s (client=\"%{public}s\")"
- "%{public}@> Accepting device connection (client=\"%s\")"
- "%{public}@> Connect succeeded for %s (client=\"%s\")"
- "%{public}s> Got CONNECT command (client=\"%s\")"
- "Accepting service connection for \"%{public}s\" (client=\"%s\")"
- "Authenticating device certificate on behalf of client... (client=\"%s\")"
- "Canceling client browse. (client=\"%s\")"
- "Completed client browse (present-only). (client=\"%s\")"
- "Completed immediate devices. (client=\"%s\")"
- "Delivering device (client=\"%s\")"
- "Disconnecting remote device %{public}s (client=\"%s\")"
- "Failed to copy certificate data. (client=\"%s\")"
- "Failed to copy certificate from identity: %d (client=\"%s\")"
- "Failed to copy key attributes. (client=\"%s\")"
- "Failed to copy key data. (client=\"%s\")"
- "Failed to copy private key from identity: %d (client=\"%s\")"
- "Fetching service %{public}s on %{public}s (client=\"%s\")"
- "Get device query: %{public}@ (client=\"%s\")"
- "Listing local services exposed to %{public}s (client=\"%s\")"
- "Listing services on %{public}s (client=\"%s\")"
- "No local identity available. (client=\"%s\")"
- "Registering client browse (present-only). (client=\"%s\")"
- "Registering client browse. (client=\"%s\")"
- "Resetting remote device %{public}s (client=\"%s\")"
- "Sending device note %{public}s sensitive properties (client=\"%s\")"
- "Successfully authenticated device certificate on behalf of client (client=\"%s\")"
- "Unregistering client browse. (client=\"%s\")"
- "device_authenticate: Failed to authenticate peer cert (client=\"%s\")"
- "device_authenticate: Failed to create cert from data (client=\"%s\")"
- "device_authenticate: No certificate data (client=\"%s\")"
- "device_check_service: Unable to find service with name %{public}s (client=\"%s\")"
- "device_get: Returning device of type %d (client=\"%s\")"
- "device_get: Unable to find device with type %d (client=\"%s\")"
- "device_get_service: Client lacks privilege to find service with name %{public}s (client=\"%s\")"
- "device_get_service: Returning service \"%{public}s\" (client=\"%s\")"
- "device_get_service: Unable to find service with name %{public}s (client=\"%s\")"
- "device_list_local_services: Client lacks privilege (client=\"%s\")"
- "device_list_services: Returning %zd/%d services for device %{public}s (client=\"%s\")"
- "device_reset: Client lacks privilege to reset device (client=\"%s\")"
- "device_set_alias: Client lacks privilege to name device (client=\"%s\")"
- "device_timesync: Client lacks privilege (client=\"%s\")"
- "service_handler: Client lacks privilege to interact with service with name %{public}s (client=\"%s\")"
- "setting remote device %{public}s alias as %{public}s (client=\"%s\")"

```
