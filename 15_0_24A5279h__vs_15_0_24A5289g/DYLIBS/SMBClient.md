## SMBClient

> `/System/Library/PrivateFrameworks/SMBClient.framework/Versions/A/SMBClient`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x1fe10
-  __TEXT.__auth_stubs: 0xc70
+488.0.0.0.0
+  __TEXT.__text: 0x206b8
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__const: 0x880
-  __TEXT.__cstring: 0x1364
-  __TEXT.__oslogstring: 0x2ef2
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__cstring: 0x13db
+  __TEXT.__oslogstring: 0x308a
+  __TEXT.__unwind_info: 0x460
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x10
-  __AUTH_CONST.__auth_got: 0x638
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__cfstring: 0xe20
   __DATA.__data: 0x40

   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /System/Library/PrivateFrameworks/KerberosHelper.framework/Versions/A/KerberosHelper
   - /usr/lib/libSystem.B.dylib
-  Functions: 572
-  Symbols:   846
-  CStrings:  327
+  Functions: 581
+  Symbols:   859
+  CStrings:  334
 
Symbols:
+ _strcasestr
+ _sysctl_get_buf
+ _sysctlbyname
+ _uuid_compare
+ get_client_interfaces.cold.3
+ get_client_interfaces.cold.4
+ get_client_interfaces.cold.5
+ sysctl_get_buf.cold.1
+ sysctl_get_buf.cold.2
+ sysctl_get_buf.cold.3
+ sysctl_get_buf.cold.4
CStrings:
+ "Null"
+ "getNumberRSSQueues"
+ "kern.skywalk.llink_list"
+ "kern.skywalk.stats.net_if"
+ "mc_clnt_rss_channels"
+ "mc_srvr_rss_channels"
+ "notNull"
+ "sysctl_get_buf"
- "mc_max_rss_channels"

```
