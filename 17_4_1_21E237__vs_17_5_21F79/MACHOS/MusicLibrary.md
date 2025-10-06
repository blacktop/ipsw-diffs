## MusicLibrary

> `/System/Library/SyncBundles/MusicLibrary.syncBundle/MusicLibrary`

```diff

-4023.510.4.0.0
+4023.610.4.0.0
   __TEXT.__text: 0x6c758
   __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_stubs: 0x4aa0

   __TEXT.__objc_methname: 0x5cc0
   __TEXT.__objc_classname: 0x224
   __TEXT.__objc_methtype: 0xbd5
-  __TEXT.__cstring: 0x2267
+  __TEXT.__cstring: 0x22e3
   __TEXT.__oslogstring: 0x42b9
   __TEXT.__dlopen_cstrs: 0x108
   __TEXT.__unwind_info: 0x1770

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 993FA8E3-C27D-34B0-8F60-7BB8A0A8B50C
+  UUID: EB64DBD5-9D53-33CB-A61F-085F6F1ECE83
   Functions: 560
   Symbols:   355
   CStrings:  1726
CStrings:
+ "SELECT DISTINCT item.keep_local_status_reason, container.container_pid FROM item JOIN container_item USING (item_pid) JOIN container USING (container_pid) WHERE (item.keep_local_status = ? AND container.keep_local > ? AND container.keep_local_status_reason != ?)"
+ "SELECT DISTINCT item.keep_local_status_reason, container_pid FROM item JOIN container_item USING (item_pid) JOIN container USING (container_pid) WHERE (item.keep_local_status = ? OR item.keep_local_status = ?) AND container.keep_local > ? AND (container.keep_local_status_reason & item.keep_local_status_reason != item.keep_local_status_reason)"
- "SELECT item.keep_local_status_reason, container.container_pid FROM item JOIN container_item USING (item_pid) JOIN container USING (container_pid) WHERE (item.keep_local_status = ? AND container.keep_local > ? AND container.keep_local_status_reason != ?)"
- "SELECT item.keep_local_status_reason, container_pid FROM item JOIN container_item USING (item_pid) JOIN container USING (container_pid) WHERE (item.keep_local_status = ? OR item.keep_local_status = ?) AND container.keep_local > ?"

```
