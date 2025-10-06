## logd

> `/usr/libexec/logd`

```diff

-1481.0.12.0.0
-  __TEXT.__text: 0x20a18
+1481.40.16.0.0
+  __TEXT.__text: 0x20f5c
   __TEXT.__auth_stubs: 0x16b0
   __TEXT.__objc_stubs: 0x5a0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x3f4
-  __TEXT.__cstring: 0x2d62
+  __TEXT.__cstring: 0x3037
   __TEXT.__objc_methname: 0x3d7
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C37ACC53-314C-3C29-8EF7-A62E9041A3FD
+  UUID: 6DC82D2A-50C9-3527-9156-3CBA1C4F971F
   Functions: 458
   Symbols:   410
-  CStrings:  479
+  CStrings:  497
 
CStrings:
+ "    - %s/%s: %lld bytes\n"
+ "    - %s: %lld bytes IN USE\n"
+ "    - %s: %lld bytes LOCKED\n"
+ "    - %s: %lld bytes RECENT\n"
+ "    - %s: %lld bytes REMOVED\n"
+ "%s/%s.0.log"
+ "%s/%s.1.log"
+ "BUG IN LIBTRACE: failed to create queue target from subsystem"
+ "Compacted %lld bytes"
+ "Periodic complete. Removed %lld bytes."
+ "Purge complete. Goal: %lld bytes. Removed: %lld bytes"
+ "Purging UUID Cache"
+ "Purging book: %s, Removed: %lld bytes"
+ "Received a Cancel Request from CacheDelete. Ignoring..."
+ "Received a Periodic Request from CacheDelete"
+ "Received a Purge Request from CacheDelete with urgency: %d and goal: %lld"
+ "Received a Purgeable Request from CacheDelete"
+ "Reporting %lld/%lld bytes as purgeable"
+ "Unable to open timesync database at %s: error %d"
+ "com.apple.%s.log"
+ "files_in_use: %ld bytes: %lld\n"
+ "files_locked: %ld bytes: %lld\n"
+ "files_recent: %ld bytes: %lld\n"
+ "logd"
- "com.apple.logd.log"
- "files_in_use: %ld\n"
- "files_locked: %ld\n"
- "files_recent: %ld\n"
- "logd.0.log"
- "logd.1.log"

```
