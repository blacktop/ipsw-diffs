## fsck_exfat

> `/System/Library/Filesystems/exfat.fs/fsck_exfat`

```diff

-488.120.2.0.0
-  __TEXT.__text: 0x96c0
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__cstring: 0x29df
-  __TEXT.__const: 0x251
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x10
+522.0.0.0.0
+  __TEXT.__text: 0xa6bc
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__const: 0x272
+  __TEXT.__cstring: 0x2c8f
+  __TEXT.__oslogstring: 0x18
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__cfstring: 0x60
-  __DATA.__data: 0x23d0
-  __DATA.__bss: 0xec610
-  __DATA.__common: 0x168
+  __DATA.__data: 0x26f0
+  __DATA.__bss: 0x2018
+  __DATA.__common: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  UUID: 39FA0D8F-A79B-3EA7-91C6-28CBAB4C60D5
-  Functions: 165
-  Symbols:   100
-  CStrings:  349
+  UUID: 059C52FC-BDCB-3E6C-B57E-EF8FBFE55FF7
+  Functions: 171
+  Symbols:   103
+  CStrings:  363
 
Symbols:
+ __os_log_default
+ __os_log_fault_impl
+ _os_log_type_enabled
+ _unlink
- _CFSetGetCount
CStrings:
+ "%s: Flushing cached block with idx %u to file"
+ "%s: Reading block with idx %u from file"
+ "%s: ran out of buffers!"
+ "Check FS: Verify data structure: Failed"
+ "Check FS: Verify data structures"
+ "Continue checking the volume with in-memory bitmap."
+ "Could not allocate bitmap cache block"
+ "Could not allocate cache buffers"
+ "Could not allocate struct fsck_bitmap_cache"
+ "Could not read cluster %u from FAT."
+ "Could not read cluster %u from cache."
+ "Could not release cached buffer. error = %d."
+ "Failed reading from bitmap cache file with error = %d. offset %u length %u."
+ "Failed to create bitmap cache file (%s), error = %d."
+ "Failed to truncate bitmap cache file (%s), error = %d."
+ "Failed to unlink bitmap cache file (%s), error = %d."
+ "Failed writing to bitmap cache file with error = %d. offset %u length %u."
+ "Hash bitmap collision: index: %u\n"
+ "fsck_exfat_bitmap_get_word"
- "Could not read FAT for cluster %u"
- "Could not read cluster %u"
- "Could not release cluster %u"
- "fsck_exfat_bitmap_init"
- "g.bitmap == NULL"

```
