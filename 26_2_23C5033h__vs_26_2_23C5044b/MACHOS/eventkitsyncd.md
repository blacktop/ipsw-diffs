## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-419.0.0.0.0
-  __TEXT.__text: 0x74b80
+420.0.0.0.0
+  __TEXT.__text: 0x7533c
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0xc620
-  __TEXT.__objc_methlist: 0x7290
-  __TEXT.__cstring: 0x58ef
-  __TEXT.__objc_methname: 0xf533
-  __TEXT.__objc_classname: 0x8fb
-  __TEXT.__objc_methtype: 0x24d7
+  __TEXT.__objc_stubs: 0xc880
+  __TEXT.__objc_methlist: 0x7390
+  __TEXT.__cstring: 0x595a
+  __TEXT.__objc_methname: 0xf880
+  __TEXT.__objc_classname: 0x918
+  __TEXT.__objc_methtype: 0x2554
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xb947
-  __TEXT.__gcc_except_tab: 0xc08
-  __TEXT.__unwind_info: 0x1668
+  __TEXT.__oslogstring: 0xb9a6
+  __TEXT.__gcc_except_tab: 0xc04
+  __TEXT.__unwind_info: 0x1678
   __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__got: 0x410
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x17c0
-  __DATA_CONST.__cfstring: 0x4e40
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__cfstring: 0x4f00
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x280
-  __DATA_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xea60
-  __DATA.__objc_selrefs: 0x3dd8
-  __DATA.__objc_ivar: 0x948
-  __DATA.__objc_data: 0x1db0
+  __DATA.__objc_const: 0xed78
+  __DATA.__objc_selrefs: 0x3e78
+  __DATA.__objc_ivar: 0x97c
+  __DATA.__objc_data: 0x1e00
   __DATA.__data: 0x800
   __DATA.__bss: 0x178
   __DATA.__common: 0x1c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CD8D10BF-FA3C-36A6-9AB3-E334CC0038EA
-  Functions: 2798
-  Symbols:   361
-  CStrings:  5328
+  UUID: 07470C8C-98FF-3F94-8BB6-EB20E841963E
+  Functions: 2817
+  Symbols:   362
+  CStrings:  5390
 
Symbols:
+ _IDSErrorDomain
CStrings:
+ "== Started EventKitSync-420"
+ "@\"NEKChangeTracker\""
+ "NEKSyncSessionAnalytics"
+ "T@\"NEKChangeTracker\",R,N,V_changeTracker"
+ "TB,N,V_isNightlySync"
+ "TB,N,V_isRetrySync"
+ "TB,R,N,V_isRetry"
+ "TB,R,N,V_isSending"
+ "TI,R,N,V_sessionStatus"
+ "TI,R,N,V_sessionType"
+ "TQ,R,N,V_ekEventStoreItemsSynced"
+ "TQ,R,N,V_remStoreItemsSynced"
+ "Td,N,V_stop"
+ "Td,R,N,V_duration"
+ "[Session: %{public}@] Unable to summarize change, key doesn't have the right format %{public}@"
+ "_batchChangeCounts"
+ "_changeTracker"
+ "_duration"
+ "_ekEventStoreItemsSynced"
+ "_isRetry"
+ "_isRetrySync"
+ "_isSending"
+ "_needsNightlySync"
+ "_nextSendIsRetry"
+ "_remStoreItemsSynced"
+ "_sessionStatus"
+ "_sessionType"
+ "_stop"
+ "_summarizeChanges:"
+ "_totalChangeCounts"
+ "changeTracker"
+ "com.apple.eventkitsync.syncsessions"
+ "duration"
+ "ekEventStoreChangeCount"
+ "ekEventStoreItemsSynced"
+ "initWithNEKSyncSession:syncSession:"
+ "isNightlySync"
+ "isRetry"
+ "isRetrySync"
+ "recordSuccessForSession:receiving:isNightlySync:"
+ "remStoreChangeCount"
+ "remStoreItemsSynced"
+ "resetForBatch"
+ "sendAnalyticsForSyncSession:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "sessionStatus"
+ "sessionType"
+ "setIsNightlySync:"
+ "setIsRetrySync:"
+ "setStop:"
+ "stop"
+ "v32@0:8@16B24B28"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
- "== Started EventKitSync-419"
- "_changeCounts"
- "recordSuccessForSession:receiving:"

```
