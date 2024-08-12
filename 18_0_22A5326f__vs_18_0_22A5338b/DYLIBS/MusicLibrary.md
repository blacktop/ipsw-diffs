## MusicLibrary

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`

```diff

-4024.100.111.0.0
-  __TEXT.__text: 0x279958
+4024.110.1.0.0
+  __TEXT.__text: 0x279950
   __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0xd814
   __TEXT.__const: 0x26080
   __TEXT.__gcc_except_tab: 0x137cc
-  __TEXT.__cstring: 0x660c6
+  __TEXT.__cstring: 0x6612c
   __TEXT.__oslogstring: 0x19dde
   __TEXT.__ustring: 0x210
   __TEXT.__dlopen_cstrs: 0x193

   __DATA_CONST.__objc_selrefs: 0x6a18
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x510
-  __DATA_CONST.__objc_arraydata: 0x1078
+  __DATA_CONST.__objc_arraydata: 0x1070
   __AUTH_CONST.__auth_got: 0xfe8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x12560
   __AUTH_CONST.__cfstring: 0x24aa0
   __AUTH_CONST.__objc_const: 0x15830
-  __AUTH_CONST.__objc_arrayobj: 0x2070
+  __AUTH_CONST.__objc_arrayobj: 0x2058
   __AUTH_CONST.__objc_intobj: 0x1b48
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
CStrings:
+ "SELECT 1 FROM container WHERE store_cloud_id != 0 AND cloud_is_subscribed AND liked_state != 2 LIMIT 1"
+ "SELECT 1 FROM item JOIN item_store USING (item_pid) JOIN item_stats USING (item_pid) WHERE item.in_my_library AND item_store.cloud_status = 8 AND item_stats.liked_state != 2 LIMIT 1"
- "SELECT 1 FROM container WHERE store_cloud_id != 0 AND cloud_is_subscribed LIMIT 1"
- "SELECT 1 FROM item JOIN item_store USING (item_pid) WHERE in_my_library AND cloud_status = ? LIMIT 1"

```
