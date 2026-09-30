## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-5200.2.4.1.5
-  __TEXT.__text: 0x55098
+5200.2.7.1.3
+  __TEXT.__text: 0x55410
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x3a44
+  __TEXT.__objc_methlist: 0x3a54
   __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x624b
-  __TEXT.__gcc_except_tab: 0xab8
-  __TEXT.__oslogstring: 0x60df
+  __TEXT.__cstring: 0x6581
+  __TEXT.__gcc_except_tab: 0xaa4
+  __TEXT.__oslogstring: 0x60cd
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1370
+  __TEXT.__unwind_info: 0x1390
   __TEXT.__objc_classname: 0x120a
-  __TEXT.__objc_methname: 0xee3e
+  __TEXT.__objc_methname: 0xeec0
   __TEXT.__objc_methtype: 0x2655
-  __TEXT.__objc_stubs: 0x8940
+  __TEXT.__objc_stubs: 0x89a0
   __DATA_CONST.__got: 0x838
   __DATA_CONST.__const: 0x1c38
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2da8
+  __DATA_CONST.__objc_selrefs: 0x2dc8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x2d0
   __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__cfstring: 0x34a0
   __AUTH_CONST.__objc_const: 0x8a50
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x5a0
+  __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x1140
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x1590
+  __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1811
-  Symbols:   2427
-  CStrings:  3100
+  Functions: 1819
+  Symbols:   2435
+  CStrings:  3106
 
CStrings:
+ "INSERT OR REPLACE INTO medication_schedules (uuid, medication_uuid, medication_identifier, start_date_time, end_date_time, created_time_zone, frequency_type, cycle_start_date_components, note, creation_date, deleted, sync_provenance, sync_identity, minimum_compatibility_version, origin_compatibility_version, schedule_type, display_options, sync_anchor) SELECT uuid, medication_uuid, medication_identifier, 0.0, NULL, ?, 0, NULL, NULL, creation_date, deleted, sync_provenance, sync_identity, ?, ?, 0, 0, (sync_anchor + ?) FROM medication_schedules WHERE schedule_type = 0 AND frequency_type = 0 AND minimum_compatibility_version <= origin_compatibility_version AND deleted = 0"
+ "UPDATE medication_schedules SET schedule_type = frequency_type, sync_anchor = (sync_anchor + ?) WHERE schedule_type = 0 AND frequency_type != 0"
+ "[%!{(MISSING)public}@] Received invalid schedule: %!{(MISSING)public}@"
+ "_setInvalidSchedulesAsLocallyIncompatibleWithMaximumIntegerValue:error:"
+ "isInvalid"
+ "needsToBeMadeUnavailable"
+ "unitTesting_invalidate"
- "[%!{(MISSING)public}@] Received unexepcted schedule with type null: %!{(MISSING)public}@"

```
