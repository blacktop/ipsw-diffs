## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4024.100.105.0.0
-  __TEXT.__text: 0x12c470
+4024.200.3.0.0
+  __TEXT.__text: 0x12c754
   __TEXT.__auth_stubs: 0x12d0
   __TEXT.__objc_stubs: 0x14b60
   __TEXT.__objc_methlist: 0x9888
   __TEXT.__const: 0x330
-  __TEXT.__gcc_except_tab: 0x4e78
-  __TEXT.__oslogstring: 0x26ae1
+  __TEXT.__gcc_except_tab: 0x4e90
+  __TEXT.__oslogstring: 0x26be7
   __TEXT.__objc_classname: 0x252c
   __TEXT.__objc_methname: 0x1fa11
   __TEXT.__objc_methtype: 0x41b4
-  __TEXT.__cstring: 0xf447
+  __TEXT.__cstring: 0xf4f7
   __TEXT.__dlopen_cstrs: 0x6b8
   __TEXT.__unwind_info: 0x36e0
   __TEXT.__eh_frame: 0x48

   __DATA_CONST.__got: 0x1048
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x5880
-  __DATA_CONST.__cfstring: 0xb820
+  __DATA_CONST.__cfstring: 0xb840
   __DATA_CONST.__objc_classlist: 0x7e0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x170

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4650
+  Functions: 4651
   Symbols:   847
-  CStrings:  8904
+  CStrings:  8908
 
CStrings:
+ "%!{(MISSING)public}@ - Finished running maintenance task with error=%!{(MISSING)public}@"
+ "Found at least one item in library with invalid saga id and valid download parameters. Will initiate a reset sync to clear state"
+ "Migrating to version 600050"
+ "SELECT item_pid FROM item JOIN item_store USING(item_pid) WHERE (media_type IN (8, 1032) AND store_saga_id = 0 AND match_redownload_params != '' AND in_my_library = 1) LIMIT 1"
+ "[BecomeActive::Cloud] Skipped cloud library update, updating all subscribed containers now (not ignoring min refresh interval)..."
- "[BecomeActive::Cloud] Skipped cloud library update, updating all subscribed containers now..."

```
