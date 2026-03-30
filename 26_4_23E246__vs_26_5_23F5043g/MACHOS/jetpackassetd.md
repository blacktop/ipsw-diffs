## jetpackassetd

> `/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd`

```diff

-9.4.21.0.0
-  __TEXT.__text: 0x9ea84
+9.5.3.0.0
+  __TEXT.__text: 0x9fd38
   __TEXT.__auth_stubs: 0x28d0
   __TEXT.__objc_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__const: 0x3770
-  __TEXT.__swift5_typeref: 0xfe9
-  __TEXT.__cstring: 0x51a4
+  __TEXT.__const: 0x38e0
+  __TEXT.__swift5_typeref: 0x1033
+  __TEXT.__cstring: 0x5424
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xf28
+  __TEXT.__constg_swiftt: 0xfb0
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0xdbc
-  __TEXT.__swift5_fieldmd: 0x106c
-  __TEXT.__swift5_types: 0x150
+  __TEXT.__swift5_reflstr: 0xe3c
+  __TEXT.__swift5_fieldmd: 0x1118
+  __TEXT.__swift5_types: 0x15c
   __TEXT.__objc_classname: 0x18b
   __TEXT.__objc_methname: 0xd5e
-  __TEXT.__swift_as_entry: 0x1f4
-  __TEXT.__swift_as_ret: 0x4c8
+  __TEXT.__swift_as_entry: 0x204
+  __TEXT.__swift_as_ret: 0x4d4
   __TEXT.__swift5_capture: 0x2d0
-  __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_proto: 0x234
+  __TEXT.__swift5_protos: 0x50
+  __TEXT.__swift5_proto: 0x244
   __TEXT.__swift5_assocty: 0x308
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__objc_methtype: 0x3e8
-  __TEXT.__unwind_info: 0x26a8
-  __TEXT.__eh_frame: 0x7ef8
+  __TEXT.__unwind_info: 0x2718
+  __TEXT.__eh_frame: 0x7f78
   __DATA_CONST.__auth_got: 0x1470
   __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__auth_ptr: 0x6c0
-  __DATA_CONST.__const: 0x28d0
+  __DATA_CONST.__auth_ptr: 0x6d0
+  __DATA_CONST.__const: 0x29b8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xa38
   __DATA.__objc_selrefs: 0x380
   __DATA.__objc_data: 0x240
-  __DATA.__data: 0x1920
-  __DATA.__common: 0x150
-  __DATA.__bss: 0x3b00
+  __DATA.__data: 0x19c8
+  __DATA.__common: 0x168
+  __DATA.__bss: 0x3c00
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 121A62C7-874F-36C7-BF4E-4DEB98044856
-  Functions: 1963
+  UUID: EC2B0BAC-A0A3-3F0D-A037-34BFC7E732CB
+  Functions: 1993
   Symbols:   1035
-  CStrings:  638
+  CStrings:  649
 
Symbols:
+ _$s10Foundation4DateV1loiySbAC_ACtFZ
+ _$sSS10describingSSx_tclufC
- _$s7JetCore26AssetPushSubscriptionStoreP4find10channelIDsSayAA0cdE6RecordVGSaySSG_tKFTj
- _$s7JetCore27AssetPushSubscriptionRecordV9isPendingSbvg
CStrings:
+ " rows as pending for channel "
+ ", TTR was not filed."
+ "Checkpoint mismatch: marked "
+ "Failed to sync checkpoints after marking pending: "
+ "JetPackStaleAssetAllowRateLimited"
+ "MaintenanceRefreshAssetsTaskHandler failed to update rows for channel `"
+ "Running jetpackassetd startup task"
+ "Skipping stale asset check because a TTR was already filed"
+ "Stale assets found, but TTR was not filed."
+ "TTR authorization status is: "
+ "TTR is rate-limited but override preference is set - allowing"
+ "TTR is rate-limited. For testing, set `defaults write com.apple.jetpackassetd JetEngine_JetPackStaleAssetAllowRateLimited -bool true` and `ttrutil developmentMode enable`"
+ "com.apple.jetpackassetd.startup"
+ "scheduleNextTask: deriving a schedule based on the existing pending push subscription records"
- "Failed to sync checkpoints after asset refresh: "
- "MaintenanceRefreshAssetsTaskHandler.handleTask.checkpoint"
- "Skipping stale asset check because a TTR prompt was already shown"

```
