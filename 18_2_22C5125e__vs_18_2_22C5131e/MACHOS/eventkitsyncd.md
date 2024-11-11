## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-407.0.0.0.0
-  __TEXT.__text: 0x6d2e4
+408.0.0.0.0
+  __TEXT.__text: 0x6d514
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0xc060
+  __TEXT.__objc_stubs: 0xc0c0
   __TEXT.__objc_methlist: 0x6934
-  __TEXT.__cstring: 0x56d2
-  __TEXT.__objc_methname: 0xee79
-  __TEXT.__objc_classname: 0x8d8
+  __TEXT.__cstring: 0x573b
+  __TEXT.__objc_methname: 0xee6e
+  __TEXT.__objc_classname: 0x8db
   __TEXT.__objc_methtype: 0x2321
   __TEXT.__const: 0x288
-  __TEXT.__oslogstring: 0xa59f
+  __TEXT.__oslogstring: 0xa652
   __TEXT.__gcc_except_tab: 0x8f0
   __TEXT.__unwind_info: 0x1528
   __DATA_CONST.__auth_got: 0x6b0

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA.__objc_const: 0x10260
-  __DATA.__objc_selrefs: 0x3a80
+  __DATA.__objc_selrefs: 0x3a90
   __DATA.__objc_ivar: 0x90c
   __DATA.__objc_data: 0x1d10
   __DATA.__data: 0x7e8

   - /usr/lib/libz.1.dylib
   Functions: 2660
   Symbols:   360
-  CStrings:  4625
+  CStrings:  4630
 
CStrings:
+ "\x01\x12"
+ "-[NEKEventChangeObserver notifyForDatabaseUpdates]"
+ "-[NEKReminderChangeObserver notifyForDatabaseUpdates]"
+ "== Started EventKitSync-408"
+ "Active sync session - ignoring incomingData for drift or duplication with IDS identifier: %!@(MISSING)"
+ "Deserialized analytics data from watch with IDS identifier: %!@(MISSING)"
+ "Failed to deserialize analytics data from watch with IDS identifier: %!@(MISSING)"
+ "initWithSyncController:"
+ "originalGUID"
- "== Started EventKitSync-407"
- "Failure to deserialize analytics data from watch"
- "TB,R,N,V_isCurrentlySyncing"
- "_isCurrentlySyncing"

```
