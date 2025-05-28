## UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

-346.0.0.0.0
-  __TEXT.__text: 0x5eaf4
-  __TEXT.__auth_stubs: 0x1e40
+346.8.0.0.0
+  __TEXT.__text: 0x6157c
+  __TEXT.__auth_stubs: 0x1eb0
   __TEXT.__objc_stubs: 0x30c0
   __TEXT.__objc_methlist: 0xa74
-  __TEXT.__const: 0x1592
-  __TEXT.__cstring: 0x3cb3
-  __TEXT.__objc_classname: 0x1b4
+  __TEXT.__const: 0x15b2
+  __TEXT.__cstring: 0x3f13
+  __TEXT.__objc_classname: 0x1c6
   __TEXT.__objc_methname: 0x43a6
   __TEXT.__objc_methtype: 0xfbf
   __TEXT.__gcc_except_tab: 0x424
   __TEXT.__oslogstring: 0x2dd4
-  __TEXT.__constg_swiftt: 0xf98
-  __TEXT.__swift5_typeref: 0x19c8
+  __TEXT.__constg_swiftt: 0xfa8
+  __TEXT.__swift5_typeref: 0x1a12
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0x3c5
-  __TEXT.__swift5_fieldmd: 0x4b8
+  __TEXT.__swift5_reflstr: 0x3f5
+  __TEXT.__swift5_fieldmd: 0x4d0
   __TEXT.__swift5_assocty: 0x200
   __TEXT.__swift5_proto: 0xe8
   __TEXT.__swift5_types: 0x50
-  __TEXT.__swift5_capture: 0x978
+  __TEXT.__swift5_capture: 0x9c0
   __TEXT.__swift5_protos: 0x78
-  __TEXT.__unwind_info: 0x1ddc
-  __TEXT.__eh_frame: 0xf78
-  __DATA_CONST.__auth_got: 0xf30
-  __DATA_CONST.__got: 0x450
+  __TEXT.__unwind_info: 0x1dfc
+  __TEXT.__eh_frame: 0xf80
+  __DATA_CONST.__auth_got: 0xf68
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x27c8
+  __DATA_CONST.__const: 0x2910
   __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0x318
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x2750
+  __DATA.__objc_const: 0x27a8
   __DATA.__objc_selrefs: 0xf80
   __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xb40
-  __DATA.__data: 0x1060
+  __DATA.__data: 0x10d0
   __DATA.__bss: 0x11c0
   __DATA.__common: 0x160
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1277
-  Symbols:   821
-  CStrings:  1257
+  Functions: 1302
+  Symbols:   828
+  CStrings:  1269
 
Symbols:
+ _$s14DeviceActivity0aB9DataStoreV05localA10IdentifierSSyKF
+ _$s14DeviceActivity0aB9DataStoreV10localZonesSaySS8zoneName_AA16_SegmentIntervalO07segmentJ0tGvg
+ _$s14DeviceActivity0aB9DataStoreV16localRecordNames11forZoneName15segmentIntervalSaySSGSS_AA08_SegmentL0OtKF
+ _$s14DeviceActivity0aB9DataStoreV17fetchCloudSegment11userAltDSID16deviceIdentifier15segmentInterval10recordNameAA01_abC0V0bG0VSS_SSAA01_gN0OSStKF
+ _$s14DeviceActivity0aB9DataStoreV18fetchCloudMetadata11userAltDSID16deviceIdentifier15segmentIntervalAA01_abC0V0G0VSS_SSAA08_SegmentN0OtKF
+ _$s14DeviceActivity0aB9DataStoreV6decodeyx10Foundation0C0VKSeRzSERzlFZ
+ _$s14DeviceActivity0aB9DataStoreV6encodey10Foundation0C0VxKSeRzSERzlFZ
+ _dispatch_sync
+ _os_transaction_create
+ _swift_isEscapingClosureAtFileLocation
- _$s14DeviceActivity0aB9DataStoreV24fetchLocalEncodedSegment15segmentInterval10recordName10Foundation0C0VAA01_hJ0O_SStKF
- _$s14DeviceActivity0aB9DataStoreV25fetchLocalEncodedMetadata15segmentInterval10Foundation0C0VAA08_SegmentJ0O_tKF
- _$s14DeviceActivity0aB9DataStoreV26localRecordNamesByZoneNameSDySSSaySSGGyKF
CStrings:
+ "Failed to update local object for %{public}s because the user has Alt DSID"
+ "OS_os_transaction"
+ "Taking a transaction in order to upload local data."
+ "There are no more changes to upload. Releasing sync transaction."
+ "There are still more changes to upload. Keeping sync transaction alive."
+ "Uploading %{public}ld records for %{public}s."
+ "com.apple.UsageTrackingAgent.SyncCoordinator.transactionQueue"
+ "com.apple.UsageTrackingAgent.transaction.alarm"
+ "com.apple.UsageTrackingAgent.transaction.device-activity-collection"
+ "com.apple.UsageTrackingAgent.transaction.sync"
+ "transaction"
+ "transactionQueue"

```
