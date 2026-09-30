## Uninstall

> `/System/Library/PrivateFrameworks/Uninstall.framework/Versions/A/Uninstall`

```diff

-267.0.0.0.0
-  __TEXT.__text: 0x5328
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x408
+267.100.1.0.0
+  __TEXT.__text: 0x54bc
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_methlist: 0x5a0
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__cstring: 0x2bd
-  __TEXT.__oslogstring: 0x10a
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__oslogstring: 0x127
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methname: 0xfb3
+  __TEXT.__objc_methname: 0xfc2
   __TEXT.__objc_methtype: 0x3a9
-  __TEXT.__objc_stubs: 0xe40
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0xe60
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1c8
   __AUTH_CONST.__const: 0x3b0
   __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0xbe0
+  __AUTH_CONST.__objc_const: 0x8f8
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x228

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E8BD5F4-14DC-33AE-9F21-203499FA3964
-  Functions: 149
-  Symbols:   474
-  CStrings:  339
+  UUID: 9D3F33F2-B1BD-3670-9FB0-0C2BB8AC3353
+  Functions: 150
+  Symbols:   478
+  CStrings:  341
 
Symbols:
+ UNLogObject.cold.1
+ __LSUnregisterURL
+ __os_log_impl
+ _objc_msgSend$URLWithString:
Functions:
~ -[UNUninstallClient _setupConnection] : 760 -> 752
~ -[UNUninstallClient completedUninstallOfBundlePaths:] : 100 -> 468
~ -[UNDockConnection removeItemsWithPaths:] : 980 -> 988
~ -[UNUninstallRequest queueRequest] : 164 -> 168
~ -[UNUninstallRequest(Private) initWithBundleAtURL:asClient:] : 232 -> 236
~ -[UNUninstallRequest(Private) initWithBundlesAtURLsInArray:asClient:] : 424 -> 428
~ -[UNDaemonConnection requestUninstallOfBundlesAtPaths:withRequest:] : 408 -> 396
~ _UNLogObject : 84 -> 68
~ _notify_server : 140 -> 144
~ _uninstall_client_authorized_service_port : 480 -> 484
~ _uninstall_client_uninstall_bundles : 436 -> 440
~ _uninstall_client_abort_uninstall : 380 -> 384
~ __Xuninstall_did_start : 100 -> 96
~ __Xuninstall_cant_be_aborted : 100 -> 96
~ __Xuninstall_progress : 100 -> 96
~ __Xuninstall_did_finish : 100 -> 96
~ _status_server : 152 -> 156
~ __DIStartTransaction : 372 -> 376
~ __DIEndTransaction : 332 -> 336
~ __DICopyContents : 484 -> 488
~ __DIMoveItem : 324 -> 328
~ __DIRemoveItem : 332 -> 336
~ __DIUpdateItem : 332 -> 336
~ __DSTempGetSpecialPort : 416 -> 420
CStrings:
+ "URLWithString:"
+ "_LSUnregisterURL returned %d"

```
