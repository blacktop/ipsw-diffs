## promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

-555.48.1.2.0
-  __TEXT.__text: 0x1f5ee0
+555.48.1.8.0
+  __TEXT.__text: 0x1f6410
   __TEXT.__auth_stubs: 0x3600
-  __TEXT.__objc_stubs: 0x17ea0
-  __TEXT.__objc_methlist: 0x148a4
+  __TEXT.__objc_stubs: 0x17ec0
+  __TEXT.__objc_methlist: 0x148bc
   __TEXT.__const: 0x17408
-  __TEXT.__objc_methname: 0x2435b
-  __TEXT.__oslogstring: 0xd77b
-  __TEXT.__cstring: 0x1257c
+  __TEXT.__objc_methname: 0x243b2
+  __TEXT.__oslogstring: 0xd7b7
+  __TEXT.__cstring: 0x12633
   __TEXT.__objc_classname: 0x25c0
   __TEXT.__objc_methtype: 0x4a1a
   __TEXT.__gcc_except_tab: 0x1708

   __TEXT.__eh_frame: 0x3d18
   __DATA_CONST.__auth_got: 0x1b10
   __DATA_CONST.__got: 0xfc0
-  __DATA_CONST.__auth_ptr: 0xbc0
-  __DATA_CONST.__const: 0xdf88
-  __DATA_CONST.__cfstring: 0xeb20
+  __DATA_CONST.__auth_ptr: 0xd28
+  __DATA_CONST.__const: 0xdf90
+  __DATA_CONST.__cfstring: 0xeb60
   __DATA_CONST.__objc_classlist: 0xd30
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x290

   __DATA_CONST.__objc_dictobj: 0xa28
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x26940
-  __DATA.__objc_selrefs: 0x8df8
-  __DATA.__objc_ivar: 0x1498
+  __DATA.__objc_const: 0x26988
+  __DATA.__objc_selrefs: 0x8e08
+  __DATA.__objc_ivar: 0x149c
   __DATA.__objc_data: 0x7db8
   __DATA.__data: 0x91c0
   __DATA.__common: 0x1a8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9619
-  Symbols:   2127
-  CStrings:  11331
+  Functions: 9623
+  Symbols:   2128
+  CStrings:  11340
 
Symbols:
+ _kAPisProtoU13
CStrings:
+ "%@ WHERE impressionId = ? AND purpose = %lu AND event = %lu"
+ "%@ WHERE impressionId = ? AND purpose IN (%lu, %lu) AND event IN (%lu, %lu, %lu, %lu) AND timestamp >= ? AND timestamp < ? ORDER BY timestamp ASC"
+ "Error getting placed event."
+ "SELECT rowid, * FROM APDBAdSignalTrack WHERE triggerRowId = ? AND (opportunity + impression + click + conversion) < 4 LIMIT %ld OFFSET %ld"
+ "TB,R,V_isProtoU13"
+ "This is a Proto U13 user. No ad requests allowed to server."
+ "Unable to get placed event rows"
+ "_isProtoU13"
+ "isProtoU13"
+ "placedEventsForImpressionId:"
+ "signalTracksWithPendingCountsForTriggerRowId:limit:offset:"
- "%@ WHERE impressionId = ? AND purpose IN (%lu, %lu) AND event IN (%lu, %lu, %lu, %lu, %lu) AND timestamp >= ? AND timestamp < ? ORDER BY timestamp ASC"
- "SELECT rowid, * FROM APDBAdSignalTrack WHERE triggerRowId = ? LIMIT %ld OFFSET %ld"
- "signalTracksForTriggerRowId:limit:offset:"

```
