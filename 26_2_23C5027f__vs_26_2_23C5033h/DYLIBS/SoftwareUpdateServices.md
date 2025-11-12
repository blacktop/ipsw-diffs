## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.60.20.0.1
-  __TEXT.__text: 0xb7ef0
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0xb284
+950.60.25.0.0
+  __TEXT.__text: 0xb815c
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0xb29c
   __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x22f7b
-  __TEXT.__gcc_except_tab: 0x138c
+  __TEXT.__cstring: 0x23146
+  __TEXT.__gcc_except_tab: 0x13cc
   __TEXT.__oslogstring: 0x85d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3378
+  __TEXT.__unwind_info: 0x3380
   __TEXT.__objc_classname: 0xf4b
-  __TEXT.__objc_methname: 0x19e84
+  __TEXT.__objc_methname: 0x19ead
   __TEXT.__objc_methtype: 0x34fb
-  __TEXT.__objc_stubs: 0x14ea0
+  __TEXT.__objc_stubs: 0x14ee0
   __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__const: 0x2a08
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5fd8
+  __DATA_CONST.__objc_selrefs: 0x5fe8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x330
+  __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x146e0
+  __AUTH_CONST.__cfstring: 0x147c0
   __AUTH_CONST.__objc_const: 0x160b0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E773BB83-7BF8-3E97-8601-54B56575A659
-  Functions: 4625
-  Symbols:   15363
-  CStrings:  10719
+  UUID: 508AD98A-8D8F-38B8-98E9-3602519F774C
+  Functions: 4627
+  Symbols:   15371
+  CStrings:  10736
 
Symbols:
+ -[SUSHistoryInstalls createTableIfNeeded]
+ -[SUSHistoryInstalls dealloc]
+ ___32-[SUInstaller installCompleted:]_block_invoke.396
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.397
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.406
+ ___32-[SUInstaller installCompleted:]_block_invoke_4.407
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.541
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.545
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.510
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.323
+ ___block_literal_global.328
+ ___block_literal_global.333
+ ___block_literal_global.338
+ ___block_literal_global.343
+ ___block_literal_global.348
+ ___block_literal_global.353
+ ___block_literal_global.361
+ ___block_literal_global.366
+ ___block_literal_global.374
+ ___block_literal_global.406
+ ___block_literal_global.408
+ ___block_literal_global.414
+ ___block_literal_global.420
+ ___block_literal_global.442
+ ___block_literal_global.482
+ ___block_literal_global.529
+ ___block_literal_global.554
+ ___block_literal_global.559
+ ___block_literal_global.592
+ ___block_literal_global.597
+ ___block_literal_global.611
+ ___block_literal_global.639
+ ___block_literal_global.649
+ ___chkstk_darwin
+ _objc_msgSend$createTableIfNeeded
+ _objc_msgSend$localizedDescription
+ _sqlite3_close
+ _sqlite3_open_v2
- ___32-[SUInstaller installCompleted:]_block_invoke.387
- ___32-[SUInstaller installCompleted:]_block_invoke_2.388
- ___32-[SUInstaller installCompleted:]_block_invoke_3.397
- ___32-[SUInstaller installCompleted:]_block_invoke_4.398
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.532
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.536
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.498
- ___block_literal_global.290
- ___block_literal_global.293
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.319
- ___block_literal_global.324
- ___block_literal_global.329
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.344
- ___block_literal_global.352
- ___block_literal_global.357
- ___block_literal_global.365
- ___block_literal_global.397
- ___block_literal_global.399
- ___block_literal_global.405
- ___block_literal_global.411
- ___block_literal_global.433
- ___block_literal_global.473
- ___block_literal_global.520
- ___block_literal_global.545
- ___block_literal_global.550
- ___block_literal_global.583
- ___block_literal_global.588
- ___block_literal_global.602
- ___block_literal_global.630
- ___block_literal_global.637
- _sqlite3_open
CStrings:
+ "%s: Attempting to delete and recreate database due to protection class issue"
+ "%s: DB successfully recreated after deletion"
+ "%s: Database file doesn't exist, skipping retry"
+ "%s: Error opening database: %s"
+ "%s: Failed to delete existing database: %@"
+ "%s: Failed to insert log: %s"
+ "%s: Failed to open database even after deletion: %s"
+ "%s: Successfully deleted existing database"
+ "%s: failed to query database: %s"
+ "-[SUSHistoryInstalls createTableIfNeeded]"
+ "Found splat update (%@.%@) applied at (%@) and then system reboot at (%@), considering as new OS"
+ "createTableIfNeeded"
+ "localizedDescription"
- "%s: Error opening database"
- "%s: Failed to insert log"
- "%s: failed to query database"

```
