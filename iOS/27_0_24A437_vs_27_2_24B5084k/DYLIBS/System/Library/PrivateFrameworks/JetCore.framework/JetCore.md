## JetCore

> `/System/Library/PrivateFrameworks/JetCore.framework/JetCore`

```diff

-10.0.47.0.0
-  __TEXT.__text: 0x254664
+10.1.8.0.0
+  __TEXT.__text: 0x25b780
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x61c
-  __TEXT.__const: 0x1eef4
-  __TEXT.__cstring: 0xa551
+  __TEXT.__const: 0x1f0f4
+  __TEXT.__cstring: 0xaa01
   __TEXT.__oslogstring: 0x48c
-  __TEXT.__constg_swiftt: 0x7c70
-  __TEXT.__swift5_typeref: 0x8477
+  __TEXT.__constg_swiftt: 0x7d24
+  __TEXT.__swift5_typeref: 0x84d7
   __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_reflstr: 0x3b52
-  __TEXT.__swift5_fieldmd: 0x6ac0
-  __TEXT.__swift5_assocty: 0x10a0
-  __TEXT.__swift5_proto: 0x1768
-  __TEXT.__swift5_types: 0x9b0
-  __TEXT.__swift5_capture: 0x3808
+  __TEXT.__swift5_reflstr: 0x3bd0
+  __TEXT.__swift5_fieldmd: 0x6bb4
+  __TEXT.__swift5_assocty: 0x10b8
+  __TEXT.__swift5_proto: 0x1780
+  __TEXT.__swift5_types: 0x9bc
+  __TEXT.__swift5_capture: 0x3828
   __TEXT.__swift5_mpenum: 0x218
-  __TEXT.__swift5_protos: 0x1a4
+  __TEXT.__swift5_protos: 0x1a8
   __TEXT.__swift_as_entry: 0x548
-  __TEXT.__swift_as_ret: 0x5ac
-  __TEXT.__swift_as_cont: 0xa6c
-  __TEXT.__unwind_info: 0xbe00
-  __TEXT.__eh_frame: 0x15210
+  __TEXT.__swift_as_ret: 0x5b4
+  __TEXT.__swift_as_cont: 0xa7c
+  __TEXT.__unwind_info: 0xbf50
+  __TEXT.__eh_frame: 0x15540
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x580
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x840
+  __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xa08
-  __AUTH_CONST.__const: 0x1a7d0
+  __DATA_CONST.__got: 0xa18
+  __AUTH_CONST.__const: 0x1aa98
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x2c58
+  __AUTH_CONST.__objc_const: 0x2d50
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1f48
+  __AUTH_CONST.__auth_got: 0x1f60
   __AUTH.__objc_data: 0x578
-  __AUTH.__data: 0x2790
+  __AUTH.__data: 0x2848
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x64e0
+  __DATA.__data: 0x66a0
   __DATA.__common: 0x3e8
   __DATA_DIRTY.__objc_data: 0x2b0
-  __DATA_DIRTY.__data: 0x3738
+  __DATA_DIRTY.__data: 0x3748
   __DATA_DIRTY.__bss: 0x5910
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12810
-  Symbols:   4052
-  CStrings:  974
+  Functions: 12911
+  Symbols:   4063
+  CStrings:  1000
 
Symbols:
+ __DATA__TtC7JetCore14JetAssetClient
+ __IVARS__TtC7JetCore14JetAssetClient
+ __METACLASS_DATA__TtC7JetCore14JetAssetClient
+ ___swift_closure_destructor.31Tm
+ _associated conformance 7JetCore18AssetPendingOriginOSHAASQ
+ _objc_msgSend$sharedSession
+ _symbolic $s7JetCore27URLSessionAsyncDataFetchingP
+ _symbolic _____ 7JetCore0A11AssetClientC
+ _symbolic _____ 7JetCore18AssetPendingOriginO
+ _symbolic _____ 7JetCore19MetricsCommonFieldsV
+ _symbolic ______p 7JetCore27URLSessionAsyncDataFetchingP
+ _symbolic _____y_____G 7JetCore14DaemonResponseO AA0c2NoD0V
+ _type_layout_string 7JetCore19MetricsCommonFieldsV
- ___swift_closure_destructor.37Tm
- ___swift_memcpy168_8
CStrings:
+ " = 'push' THEN pending_origin ELSE "
+ " END,\n    modified_at = "
+ ",\n    pending_origin = "
+ ",\n    pending_origin = CASE WHEN pending = 1 AND pending_origin IN ('checkpoint', 'apsReconnect') AND "
+ ",\n    schedule_to = "
+ "ALTER TABLE push_subscription ADD COLUMN pending_origin TEXT"
+ "AssetPushSubscriptionSQLiteStore DB migration to v7..."
+ "Cannot retrieve asset via daemon: "
+ "Daemon prewarm failed: "
+ "DaemonSession.sendSync"
+ "Direct fetch failed: "
+ "Error occurred when sending synchronous request to daemon: "
+ "Falling back to direct network fetch"
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
