## Activity Monitor

> `/System/Applications/Utilities/Activity Monitor.app/Contents/MacOS/Activity Monitor`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1140.0.0.0.0
-  __TEXT.__text: 0x43e24
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_stubs: 0xca60
-  __TEXT.__objc_methlist: 0x6308
+1141.0.0.0.0
+  __TEXT.__text: 0x441d8
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_stubs: 0xcb60
+  __TEXT.__objc_methlist: 0x6360
   __TEXT.__const: 0x248
-  __TEXT.__gcc_except_tab: 0xc90
-  __TEXT.__objc_methname: 0x1296f
-  __TEXT.__cstring: 0x356f
+  __TEXT.__gcc_except_tab: 0xcac
+  __TEXT.__objc_methname: 0x12a9d
+  __TEXT.__cstring: 0x359e
   __TEXT.__objc_classname: 0x6dc
   __TEXT.__objc_methtype: 0x309f
-  __TEXT.__ustring: 0x3a8
-  __TEXT.__unwind_info: 0x13e8
-  __DATA_CONST.__const: 0x1430
-  __DATA_CONST.__cfstring: 0x4be0
+  __TEXT.__ustring: 0x4c8
+  __TEXT.__unwind_info: 0x1400
+  __DATA_CONST.__const: 0x1460
+  __DATA_CONST.__cfstring: 0x4c20
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x700
+  __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x528
-  __DATA.__objc_const: 0xb380
-  __DATA.__objc_selrefs: 0x46b0
-  __DATA.__objc_ivar: 0xad8
+  __DATA.__objc_const: 0xb3e0
+  __DATA.__objc_selrefs: 0x46e8
+  __DATA.__objc_ivar: 0xae0
   __DATA.__objc_data: 0x14f0
   __DATA.__data: 0x7f0
   __DATA.__common: 0x8

   - /usr/lib/libquit.dylib
   - /usr/lib/libsysmon.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 2004
-  Symbols:   413
-  CStrings:  4539
+  Functions: 2014
+  Symbols:   416
+  CStrings:  4554
 
Symbols:
+ _dispatch_after
+ _dispatch_time
+ _sysmon_request_create_with_error
CStrings:
+ "### SMStatisticsManager: failed to create system sysmon request — retrying"
+ "### SMStatisticsManager: system sysmon request error: %s — re-arming"
+ "(null)"
+ "TB,V_rebuildingSystemRequest"
+ "TQ,V_systemRequestIntervalMS"
+ "_rebuildSystemSysmonRequest"
+ "_rebuildingSystemRequest"
+ "_scheduleSystemSysmonRequestRebuild"
+ "_startSystemSysmonRequest"
+ "_systemRequestIntervalMS"
+ "rebuildingSystemRequest"
+ "setRebuildingSystemRequest:"
+ "setSystemRequestIntervalMS:"
+ "systemRequestIntervalMS"
+ "v24@?0@\"NSObject<OS_sysmon_table>\"8r*16"
```
