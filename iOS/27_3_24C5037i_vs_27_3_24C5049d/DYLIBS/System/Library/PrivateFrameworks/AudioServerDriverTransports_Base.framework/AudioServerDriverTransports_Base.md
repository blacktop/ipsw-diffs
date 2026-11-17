## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`

```diff

-420.1.0.0.0
-  __TEXT.__text: 0x3de70
-  __TEXT.__objc_methlist: 0x35a4
-  __TEXT.__gcc_except_tab: 0x6108
+420.2.0.0.0
+  __TEXT.__text: 0x3ebb8
+  __TEXT.__objc_methlist: 0x3624
+  __TEXT.__gcc_except_tab: 0x6394
   __TEXT.__const: 0x4f6
-  __TEXT.__cstring: 0x148e
-  __TEXT.__oslogstring: 0x315c
-  __TEXT.__unwind_info: 0x2518
+  __TEXT.__cstring: 0x1495
+  __TEXT.__oslogstring: 0x3251
+  __TEXT.__unwind_info: 0x2558
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1dd0
+  __DATA_CONST.__objc_selrefs: 0x1e28
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__got: 0x2c8
   __AUTH_CONST.__const: 0x548
   __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x5500
+  __AUTH_CONST.__objc_const: 0x5580
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_ivar: 0x338
   __DATA.__data: 0x840
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1761
-  Symbols:   2976
-  CStrings:  570
+  Functions: 1773
+  Symbols:   2990
+  CStrings:  576
 
Symbols:
+ -[ASDTChangeRequestManager currentQueueForObject:withName:]
+ -[ASDTChangeRequestManager deviceAdded:]
+ -[ASDTChangeRequestManager deviceRemoved:]
+ -[ASDTChangeRequestManager removedObjects]
+ -[ASDTChangeRequestManager setRemovedObjects:]
+ -[ASDTChangeRequestManager waitForBusyQueueWithName:forObject:withTimeout:]
+ -[ASDTChangeRequestQueue abandon]
+ -[ASDTChangeRequestQueue abandoned]
+ -[ASDTChangeRequestQueue executingOnCurrentThread]
+ -[ASDTChangeRequestQueue isRunning]
+ -[ASDTChangeRequestQueue setAbandoned:]
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_IVAR_$_ASDTChangeRequestManager._removedObjects
+ _OBJC_IVAR_$_ASDTChangeRequestQueue._abandoned
CStrings:
+ "\""
+ "%@: Device %@ removed; dropped %lu pending change requests"
+ "%@: Discarding %lu change requests for released device %@"
+ "%@: Dropping config change %u for removed device: %@"
+ "%@: Replacing stale change request queue for %@ (flags 0x%x, %lu requests)"
+ "420.2"
+ "B"
- "420.1"
```
