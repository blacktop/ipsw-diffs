## MiLoDiagnostic

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/MiLoDiagnostic.appex/MiLoDiagnostic`

```diff

-35.0.1.0.0
-  __TEXT.__text: 0x908
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__cstring: 0xb9
-  __TEXT.__oslogstring: 0x1e7
+59.0.1.0.9
+  __TEXT.__text: 0xd30
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x220
+  __TEXT.__objc_methlist: 0x20
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__cstring: 0xd0
+  __TEXT.__oslogstring: 0x232
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x113
-  __TEXT.__objc_methtype: 0xb
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x120
+  __TEXT.__objc_methname: 0x172
+  __TEXT.__objc_methtype: 0x1f
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x78
+  __DATA.__objc_selrefs: 0x90
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7CA0C08-05B6-3D34-9664-AED0E730047F
-  Functions: 7
-  Symbols:   53
-  CStrings:  37
+  UUID: 4A7C455F-EF6D-3ACC-813A-011756E2B47E
+  Functions: 11
+  Symbols:   56
+  CStrings:  49
 
Symbols:
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x27
+ _objc_sync_enter
+ _objc_sync_exit
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_claimAutoreleasedReturnValue
- _objc_release_x24
- _objc_retain
- _objc_retain_x1
- _objc_retain_x8
CStrings:
+ "%@ attachment: %@"
+ "%@ export processing finished"
+ "Database export reply called with urls: %@"
+ "Diagnostics extension export timeout, one or both exports timed out"
+ "Export completed with %lu attachments"
+ "Export timeout for %@, skipping processing"
+ "Got database export reply with error: %@"
+ "Got visual logger export reply with error: %@"
+ "Non-existing file from %@ export! path: %@"
+ "Visual logger export reply called with urls: %@"
+ "count"
+ "database"
+ "exportVisualLoggerDataWithReply:"
+ "processExportURLs:intoAttachments:exportType:isRunning:"
+ "v48@0:8@16@24@32@40"
+ "visual_logger"
- "Diagnostics extension export timeout, export timed out"
- "Diagnostics extension non existing file, got a non-existing file from exportDatabase! This should never happen. path: %@"
- "Got reply with error : %@ , diagnostic extention export error"
- "MiLoAttachment attachment : %@"
- "database export reply called with urls: %@"
- "database export reply finished"

```
