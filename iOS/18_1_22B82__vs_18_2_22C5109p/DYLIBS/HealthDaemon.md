## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0x761bfc
-  __TEXT.__auth_stubs: 0x3720
-  __TEXT.__objc_methlist: 0x3cd38
-  __TEXT.__const: 0x1c39c
-  __TEXT.__oslogstring: 0x3eef1
+5200.2.4.1.5
+  __TEXT.__text: 0x762d78
+  __TEXT.__auth_stubs: 0x3730
+  __TEXT.__objc_methlist: 0x3cd68
+  __TEXT.__const: 0x1c37c
+  __TEXT.__oslogstring: 0x3ef40
   __TEXT.__swift5_typeref: 0x387
   __TEXT.__swift5_fieldmd: 0x20c
   __TEXT.__constg_swiftt: 0x4fc
-  __TEXT.__cstring: 0x762e5
+  __TEXT.__cstring: 0x764a4
   __TEXT.__swift5_reflstr: 0x1b0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_capture: 0xe0
-  __TEXT.__gcc_except_tab: 0x37a9c
+  __TEXT.__gcc_except_tab: 0x37b18
   __TEXT.__dlopen_cstrs: 0x15b
   __TEXT.__ustring: 0x70
   __TEXT.__unwind_info: 0x1c1c8
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_classname: 0xc675
-  __TEXT.__objc_methname: 0x8baff
-  __TEXT.__objc_methtype: 0x174ed
-  __TEXT.__objc_stubs: 0x4f060
+  __TEXT.__objc_methname: 0x8bc3b
+  __TEXT.__objc_methtype: 0x1754a
+  __TEXT.__objc_stubs: 0x4f120
   __DATA_CONST.__got: 0x50d8
-  __DATA_CONST.__const: 0x1cc78
+  __DATA_CONST.__const: 0x1cce8
   __DATA_CONST.__objc_classlist: 0x2890
   __DATA_CONST.__objc_catlist: 0x488
   __DATA_CONST.__objc_protolist: 0x9a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19240
+  __DATA_CONST.__objc_selrefs: 0x19278
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x1d98
-  __DATA_CONST.__objc_arraydata: 0x8708
-  __AUTH_CONST.__auth_got: 0x1ba8
+  __DATA_CONST.__objc_arraydata: 0x8710
+  __AUTH_CONST.__auth_got: 0x1bb0
   __AUTH_CONST.__auth_ptr: 0xa8
   __AUTH_CONST.__const: 0xdc98
-  __AUTH_CONST.__cfstring: 0x3c480
-  __AUTH_CONST.__objc_const: 0x83ac8
-  __AUTH_CONST.__objc_arrayobj: 0x1ec0
+  __AUTH_CONST.__cfstring: 0x3c6a0
+  __AUTH_CONST.__objc_const: 0x83b18
+  __AUTH_CONST.__objc_arrayobj: 0x1ed8
   __AUTH_CONST.__objc_intobj: 0x4410
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0xb638
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x4298
+  __DATA.__objc_ivar: 0x429c
   __DATA.__data: 0x76c0
   __DATA.__bss: 0x2b0
   __DATA.__common: 0x24

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 33357
-  Symbols:   39889
-  CStrings:  35721
+  Functions: 33365
+  Symbols:   39903
+  CStrings:  35750
 
Symbols:
+ _HDCloudSyncFullSyncActiveDuration
+ _HDCloudSyncFullSyncNumberOfRuns
+ _HDCloudSyncFullSyncOngoing
+ _HDCloudSyncFullSyncRunStartTime
+ _HDCloudSyncFullSyncStartTime
+ _HDHealthDaemonConcurrentDatabaseReadersKey
+ _HKCloudSyncFullSyncReasonToString
CStrings:
+ "\n\nConcurrent Readers: %!l(MISSING)u"
+ "%!{(MISSING)public}@: HDDatabase allocated with %!{(MISSING)public}lu concurrent readers"
+ "ALTER TABLE cloud_sync_stores ADD COLUMN pending_full_sync INTEGER NOT NULL DEFAULT 0"
+ "HDCloudSyncFullSyncActiveDuration"
+ "HDCloudSyncFullSyncNumberOfRuns"
+ "HDCloudSyncFullSyncOngoing"
+ "HDCloudSyncFullSyncRunStartTime"
+ "HDCloudSyncFullSyncStartTime"
+ "HDHealthDaemonConcurrentDatabaseReadersKey"
+ "Long database transaction %!{(MISSING)public}@ duration: duration=%!{(MISSING)public}@, wait=%!{(MISSING)public}@, work=%!{(MISSING)public}@, write=%!{(MISSING)BOOL}d, protected=%!{(MISSING)BOOL}d, priority=%!{(MISSING)BOOL}d, cache=%!l(MISSING)d, journal=%!l(MISSING)d, queue=%!s(MISSING)"
+ "T@\"NSString\",R,C,N,V_domainName"
+ "TB,R,N,V_pendingFullSync"
+ "_pendingFullSync"
+ "activeDuration"
+ "cloudSync_reportFullSyncMetricsWithReason:shard:daysSincePreviousFullSync:totalDuration:activeDuration:numberOfRuns:incomplete:"
+ "daysSincePreviousFullSync"
+ "dictionaryForKey:"
+ "doubleForKey:"
+ "fullSyncReason"
+ "fullsync-metrics"
+ "incomplete"
+ "numberOfRuns"
+ "pendingFullSync"
+ "pending_full_sync"
+ "remote_qaSourceForBundleIdentifier:name:completion:"
+ "setDouble:forKey:"
+ "shard"
+ "shardResponsible"
+ "stateWithPendingFullSync:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"HKSource\"@\"NSError\">32"
+ "v68@0:8@16@24@32d40d48@56B64"
- "T@\"NSString\",R,N,V_domainName"
- "long outermost database transaction: duration=%!{(MISSING)public}@, wait=%!{(MISSING)public}@, work=%!{(MISSING)public}@, write=%!{(MISSING)BOOL}d, protected=%!{(MISSING)BOOL}d, priority=%!{(MISSING)BOOL}d, cache=%!l(MISSING)d, journal=%!l(MISSING)d, queue=%!s(MISSING)"

```
