## JetCore

> `/System/Library/PrivateFrameworks/JetCore.framework/Versions/A/JetCore`

```diff

-10.0.47.0.0
-  __TEXT.__text: 0x25bf20
+10.1.8.0.0
+  __TEXT.__text: 0x263d40
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__const: 0x1ef94
-  __TEXT.__cstring: 0xa611
+  __TEXT.__const: 0x1f1c4
+  __TEXT.__cstring: 0xab21
   __TEXT.__oslogstring: 0x48c
-  __TEXT.__constg_swiftt: 0x7c70
-  __TEXT.__swift5_typeref: 0x84c7
+  __TEXT.__constg_swiftt: 0x7d24
+  __TEXT.__swift5_typeref: 0x8597
   __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_reflstr: 0x3b52
-  __TEXT.__swift5_fieldmd: 0x6ac0
-  __TEXT.__swift5_assocty: 0x10a0
-  __TEXT.__swift5_proto: 0x1768
-  __TEXT.__swift5_types: 0x9b0
-  __TEXT.__swift5_capture: 0x38d0
+  __TEXT.__swift5_reflstr: 0x3bd0
+  __TEXT.__swift5_fieldmd: 0x6bb4
+  __TEXT.__swift5_assocty: 0x10b8
+  __TEXT.__swift5_proto: 0x1780
+  __TEXT.__swift5_types: 0x9bc
+  __TEXT.__swift5_capture: 0x3900
   __TEXT.__swift5_mpenum: 0x218
-  __TEXT.__swift5_protos: 0x1a4
-  __TEXT.__swift_as_entry: 0x548
-  __TEXT.__swift_as_ret: 0x5b0
-  __TEXT.__swift_as_cont: 0xa6c
-  __TEXT.__unwind_info: 0xb950
-  __TEXT.__eh_frame: 0x15248
+  __TEXT.__swift5_protos: 0x1a8
+  __TEXT.__swift_as_entry: 0x550
+  __TEXT.__swift_as_ret: 0x5c4
+  __TEXT.__swift_as_cont: 0xa8c
+  __TEXT.__unwind_info: 0xbb50
+  __TEXT.__eh_frame: 0x15688
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x588
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x850
+  __DATA_CONST.__objc_selrefs: 0x860
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xa08
-  __AUTH_CONST.__const: 0x1a988
+  __DATA_CONST.__got: 0xa18
+  __AUTH_CONST.__const: 0x1aca0
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x2c58
+  __AUTH_CONST.__objc_const: 0x2d50
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1e20
+  __AUTH_CONST.__auth_got: 0x1e48
   __AUTH.__objc_data: 0x578
-  __AUTH.__data: 0x2790
+  __AUTH.__data: 0x2848
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x64c0
+  __DATA.__data: 0x6690
   __DATA.__common: 0x3e8
   __DATA_DIRTY.__objc_data: 0x2b0
-  __DATA_DIRTY.__data: 0x37a0
+  __DATA_DIRTY.__data: 0x3780
   __DATA_DIRTY.__bss: 0x5910
   __DATA_DIRTY.__common: 0xfc
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12841
-  Symbols:   4030
-  CStrings:  977
+  Functions: 12960
+  Symbols:   4047
+  CStrings:  1005
 
Symbols:
+ __DATA__TtC7JetCore14JetAssetClient
+ __IVARS__TtC7JetCore14JetAssetClient
+ __METACLASS_DATA__TtC7JetCore14JetAssetClient
+ __swift_closure_destructor.31Tm
+ _associated conformance 7JetCore18AssetPendingOriginOSHAASQ
+ _objc_msgSend$cancel
+ _objc_msgSend$sharedSession
+ _swift_task_addCancellationHandler
+ _swift_task_removeCancellationHandler
+ _symbolic $s7JetCore27URLSessionAsyncDataFetchingP
+ _symbolic ScCy______So13NSURLResponseCt______pG 10Foundation4DataV s5ErrorP
+ _symbolic _____ 7JetCore0A11AssetClientC
+ _symbolic _____ 7JetCore18AssetPendingOriginO
+ _symbolic _____ 7JetCore19MetricsCommonFieldsV
+ _symbolic ______So13NSURLResponseCt 10Foundation4DataV
+ _symbolic ______p 7JetCore27URLSessionAsyncDataFetchingP
+ _symbolic _____ySb11isCancelled_So16NSURLSessionTaskCSg4taskt_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____y_____G 7JetCore14DaemonResponseO AA0c2NoD0V
+ _type_layout_string 7JetCore19MetricsCommonFieldsV
- ___swift_memcpy168_8
- __swift_closure_destructor.37Tm
CStrings:
+ " = 'push' THEN pending_origin ELSE "
+ " END,\n    modified_at = "
+ ",\n    pending_origin = "
+ ",\n    pending_origin = CASE WHEN pending = 1 AND pending_origin IN ('checkpoint', 'apsReconnect') AND "
+ ",\n    schedule_to = "
+ "ALTER TABLE push_subscription ADD COLUMN pending_origin TEXT"
+ "AssetPushSubscriptionSQLiteStore DB migration to v7..."
+ "Cannot activate twice"
+ "Cannot retrieve asset via daemon: "
+ "Daemon prewarm failed: "
+ "DaemonSession.sendSync"
+ "Direct fetch failed: "
+ "Error occurred when sending synchronous request to daemon: "
+ "Falling back to direct network fetch"
+ "Foundation/arm64e-apple-macos.private.swiftinterface"
+ "JetAssetClient.prewarm"
+ "MetricsCommonFields: use the typed property for '"
+ "Received an XPC error sending synchronous request: "
+ "Sending synchronous prewarm request to daemon"
+ "Sending synchronous request to daemon: "
+ "UPDATE push_subscription SET\n    pending = 1,\n    download_attempts = 0,\n    schedule_from = "
+ "UPDATE push_subscription SET pending = 0, download_attempts = NULL, schedule_from = NULL, schedule_to = NULL, priority = NULL, server_timestamp = NULL, pending_origin = NULL, modified_at = "
+ "XPC session (sendSync) cancelled: "
+ "apsReconnect"
+ "checkpoint"
+ "pendingOriginRaw"
+ "push"
+ "push304Retry"
+ "sendSync complete"
+ "✅ AssetPushSubscriptionSQLiteStore DB migration to v7 complete"
- "Sending one-way prewarm request to daemon"
- "UPDATE push_subscription SET pending = 0, download_attempts = NULL, schedule_from = NULL, schedule_to = NULL, priority = NULL, server_timestamp = NULL, modified_at = "
```
