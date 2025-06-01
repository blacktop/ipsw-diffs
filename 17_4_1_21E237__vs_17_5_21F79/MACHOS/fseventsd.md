## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1376.100.3.0.0
-  __TEXT.__text: 0x14ba8
+1376.120.2.0.0
+  __TEXT.__text: 0x1566c
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__cstring: 0xb14
+  __TEXT.__cstring: 0xb5f
   __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0x2762
-  __TEXT.__unwind_info: 0x2fc
+  __TEXT.__oslogstring: 0x2a32
+  __TEXT.__unwind_info: 0x314
   __DATA_CONST.__auth_got: 0x5f0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BAC2D426-63D6-3CD8-9330-22FE88769E3C
-  Functions: 345
+  UUID: 9592313F-78D7-3B1A-887E-564633D764DF
+  Functions: 359
   Symbols:   210
-  CStrings:  408
+  CStrings:  426
 
CStrings:
+ "%s: malformed history archive - header too small - (%s)\n"
+ "%s: malformed history file - > PATH_MAX \n"
+ "%s: malformed history file - DLS_DOCID_SIZE \n"
+ "%s: malformed history file - DLS_EVENTID_SIZE \n"
+ "%s: malformed history file - DLS_EVENTID_SIZE truncated"
+ "%s: malformed history file - DLS_EVENTMASK_SIZE \n"
+ "%s: malformed history file - DLS_EVENTMASK_SIZE truncated"
+ "%s: malformed history file - DLS_FILEID_SIZE \n"
+ "%s: malformed history file - DLS_FILEID_SIZE truncated"
+ "%s: malformed history file - DLS_FILEID_SIZE+DLS_DOCID_SIZE truncated"
+ "%s: malformed history file - doc_id truncated"
+ "%s: malformed history file - event_id truncated"
+ "%s: malformed history file - event_mask truncated"
+ "%s: malformed history file - file_id truncated"
+ "get_last_event_id"
+ "process_disk_event_buf"
+ "read_disk_log"
+ "swap_disk_event_buf"

```
