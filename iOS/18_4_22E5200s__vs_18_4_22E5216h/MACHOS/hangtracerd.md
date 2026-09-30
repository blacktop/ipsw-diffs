## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-352.0.0.0.0
-  __TEXT.__text: 0x30830
+354.2.0.0.0
+  __TEXT.__text: 0x30d80
   __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x5320
-  __TEXT.__objc_methlist: 0x2024
+  __TEXT.__objc_stubs: 0x5340
+  __TEXT.__objc_methlist: 0x2014
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x4bb7
+  __TEXT.__cstring: 0x4c18
   __TEXT.__objc_classname: 0x31f
-  __TEXT.__objc_methname: 0x8538
+  __TEXT.__objc_methname: 0x85a2
   __TEXT.__objc_methtype: 0x1005
-  __TEXT.__gcc_except_tab: 0x5b4
-  __TEXT.__oslogstring: 0x5872
-  __TEXT.__unwind_info: 0x988
+  __TEXT.__gcc_except_tab: 0x57c
+  __TEXT.__oslogstring: 0x59cc
+  __TEXT.__unwind_info: 0x9a0
   __DATA_CONST.__auth_got: 0x770
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1ec8
+  __DATA_CONST.__const: 0x1f08
   __DATA_CONST.__cfstring: 0x63a0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x4950
-  __DATA.__objc_selrefs: 0x1a60
+  __DATA.__objc_selrefs: 0x1a70
   __DATA.__objc_ivar: 0x41c
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x548

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1108
+  Functions: 1115
   Symbols:   375
-  CStrings:  2851
+  CStrings:  2862
 
CStrings:
+ "%s, Check for pending hangs request from %@"
+ "%s, No active pending hang block, adding workload for %@"
+ "%s, Saving a tailspin now."
+ "%s: hangWaitTimeoutMS: %llu"
+ "addObjectsFromArray:"
+ "allRecordsMutable"
+ "checkForPendingHangsAfterTimeout"
+ "checkForPendingHangsWrapper"
+ "excluding process exit record, timediff (%llu) > %llu, processName %@, pid %d, exitTimestamp %llu, exitReasonCode %llu, exitReasonNamespace %u"
+ "indexOfObject:inSortedRange:options:usingComparator:"
+ "insertObject:atIndex:"
+ "q24@?0@\"HTHangInfo\"8@\"HTHangInfo\"16"
+ "record# %d, processName %@, pid %d, spawnTimestamp %llu, exitTimestamp %llu, exitReasonCode %llu, exitReasonNamespace %u, jetsam_priority %u"
- "discarding stale record, time since exit %.0fms, HT_STALE_RECORD_THRESHOLD_IN_MSEC %llums, %@"
- "insert:"

```
