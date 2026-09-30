## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-1027.4.0.0.0
-  __TEXT.__text: 0x103d38
+1027.7.0.0.0
+  __TEXT.__text: 0x104014
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_stubs: 0x10d80
-  __TEXT.__objc_methlist: 0xd8c4
+  __TEXT.__objc_stubs: 0x10da0
+  __TEXT.__objc_methlist: 0xd8cc
   __TEXT.__const: 0x688
-  __TEXT.__gcc_except_tab: 0x2658
-  __TEXT.__objc_methname: 0x1c0fd
-  __TEXT.__cstring: 0xda55
-  __TEXT.__oslogstring: 0x15626
+  __TEXT.__gcc_except_tab: 0x26a0
+  __TEXT.__objc_methname: 0x1c11e
+  __TEXT.__cstring: 0xda8b
+  __TEXT.__oslogstring: 0x1578d
   __TEXT.__objc_classname: 0x225b
   __TEXT.__objc_methtype: 0x49be
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x3a40
+  __TEXT.__unwind_info: 0x3a50
   __DATA_CONST.__auth_got: 0x888
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA.__objc_const: 0x19f30
-  __DATA.__objc_selrefs: 0x5dc8
+  __DATA.__objc_selrefs: 0x5dd0
   __DATA.__objc_ivar: 0x11c4
   __DATA.__objc_data: 0x4dd0
   __DATA.__data: 0x19d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 692FB18F-57E1-36AD-9FA7-595DFE12449A
-  Functions: 5750
+  UUID: CFE5C607-EEAA-302E-AD56-0E701989FCF2
+  Functions: 5752
   Symbols:   696
-  CStrings:  10146
+  CStrings:  10151
 
CStrings:
+ "-[NetworkRelayAgent removeAllMigrationScanCandidates]"
+ "26"
+ "EPMigrationAutoTrigger: NetworkRelayPairing migration discovery in progress and actively migrating"
+ "EPMigrationAutoTrigger: NetworkRelayPairing migration discovery in progress but no more candidates, stopping discovery"
+ "EPMigrationAutoTrigger: NetworkRelayPairing migration discovery in progress but not actively migrating (StatusCode %lu), stopping"
+ "EPMigrationAutoTrigger: NetworkRelayPairing migration pairing in progress, leave it alone"
+ "NanoRegistry-1027.7"
+ "[Push-New] Not calling requestAuthMethodForDevice with method %lu on an already requested candidate %@"
+ "[Push-New] Pushing a newly discovered candidate %@"
+ "[Push-New] recently pushed candidate has PIN request pending"
+ "removeAllMigrationScanCandidates"
- "32"
- "NanoRegistry-1027.4"
- "NetworkRelayPairing is in progress but no more candidates, stop scanning"
- "NetworkRelayPairing migration discovery in progress and actively migrating"
- "NetworkRelayPairing migration discovery in progress but not actively migrating (StatusCode %lu), stopping"
- "Pushing a newly discovered candidate %@"

```
