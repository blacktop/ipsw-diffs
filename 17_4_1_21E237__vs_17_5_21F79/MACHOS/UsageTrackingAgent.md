## UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

-336.0.0.0.0
+346.0.0.0.0
   __TEXT.__text: 0x5eaf4
-  __TEXT.__auth_stubs: 0x1e30
+  __TEXT.__auth_stubs: 0x1e40
   __TEXT.__objc_stubs: 0x30c0
   __TEXT.__objc_methlist: 0xa74
   __TEXT.__const: 0x1592
-  __TEXT.__cstring: 0x3c33
+  __TEXT.__cstring: 0x3cb3
   __TEXT.__objc_classname: 0x1b4
   __TEXT.__objc_methname: 0x43a6
   __TEXT.__objc_methtype: 0xfbf

   __TEXT.__swift5_protos: 0x78
   __TEXT.__unwind_info: 0x1ddc
   __TEXT.__eh_frame: 0xf78
-  __DATA_CONST.__auth_got: 0xf28
+  __DATA_CONST.__auth_got: 0xf30
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x48
   __DATA_CONST.__const: 0x27c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7C8703CF-E83E-3336-AD06-6B4FAB2CD79F
+  UUID: 37C483F6-9B45-38E5-9EC8-C017BAC037E3
   Functions: 1277
-  Symbols:   820
+  Symbols:   821
   CStrings:  1343
 
Symbols:
+ _$s14DeviceActivity0aB11DataStoringP011deleteLocalC00eA10IdentifierySb_tKFTj
+ _$s14DeviceActivity0aB9DataStoreV011deleteLocalC00eA10IdentifierySb_tKF
+ _$s14DeviceActivity0aB9DataStoreV09deleteAllC0yyKF
- _$s14DeviceActivity0aB11DataStoringP011deleteLocalC0yyKFTj
- _$s14DeviceActivity0aB9DataStoreV09deleteAllC00eA10IdentifierySb_tKF
CStrings:
+ "Failed to add metadata to record because it was likely already moved to the Cloud folder: %{public}s"
+ "Failed to add segment to record because it was likely already moved to the Cloud folder: %{public}s"
- "Failed to add metadata to record: %{public}s"
- "Failed to add segment to record: %{public}s"

```
