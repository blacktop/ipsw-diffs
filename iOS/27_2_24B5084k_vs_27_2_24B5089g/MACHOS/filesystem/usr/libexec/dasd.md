## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-2467.40.37.0.0
-  __TEXT.__text: 0x175100
-  __TEXT.__auth_stubs: 0x2240
-  __TEXT.__objc_stubs: 0x1b380
-  __TEXT.__objc_methlist: 0x1334c
-  __TEXT.__const: 0x1578
-  __TEXT.__objc_methname: 0x2ebb5
-  __TEXT.__cstring: 0x10706
-  __TEXT.__oslogstring: 0x171a9
-  __TEXT.__objc_classname: 0x1ca8
-  __TEXT.__objc_methtype: 0x4231
-  __TEXT.__gcc_except_tab: 0x502c
+2467.40.41.0.0
+  __TEXT.__text: 0x1763b8
+  __TEXT.__auth_stubs: 0x2250
+  __TEXT.__objc_stubs: 0x1b520
+  __TEXT.__objc_methlist: 0x1343c
+  __TEXT.__const: 0x1588
+  __TEXT.__objc_methname: 0x2ed55
+  __TEXT.__cstring: 0x10806
+  __TEXT.__oslogstring: 0x172e9
+  __TEXT.__objc_classname: 0x1cd8
+  __TEXT.__objc_methtype: 0x42e1
+  __TEXT.__gcc_except_tab: 0x5044
   __TEXT.__dlopen_cstrs: 0x552
   __TEXT.__swift5_typeref: 0x966
   __TEXT.__swift5_capture: 0x220

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6520
+  __TEXT.__unwind_info: 0x65a0
   __TEXT.__eh_frame: 0xbd0
-  __DATA_CONST.__const: 0x4fa8
-  __DATA_CONST.__cfstring: 0x11ae0
-  __DATA_CONST.__objc_classlist: 0x708
+  __DATA_CONST.__const: 0x5038
+  __DATA_CONST.__cfstring: 0x11c20
+  __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x5c0
+  __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_intobj: 0x17b8
-  __DATA_CONST.__objc_arraydata: 0x4a0
-  __DATA_CONST.__objc_arrayobj: 0x1c8
+  __DATA_CONST.__objc_arraydata: 0x4f8
+  __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA_CONST.__auth_got: 0x1130
+  __DATA_CONST.__auth_got: 0x1138
   __DATA_CONST.__got: 0xe58
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x33fc8
-  __DATA.__objc_selrefs: 0x9e20
-  __DATA.__objc_ivar: 0x1644
-  __DATA.__objc_data: 0x4908
-  __DATA.__data: 0x21a0
+  __DATA.__objc_const: 0x34420
+  __DATA.__objc_selrefs: 0x9e88
+  __DATA.__objc_ivar: 0x1650
+  __DATA.__objc_data: 0x4958
+  __DATA.__data: 0x2200
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8411
-  Symbols:   1019
-  CStrings:  12534
+  Functions: 8441
+  Symbols:   1020
+  CStrings:  12573
 
Symbols:
+ _MGIsDeviceOneOfType
CStrings:
+ "AppLifecycleRecorder"
+ "B36@0:8@16B24@28"
+ "B48@0:8Q16@24@32^@40"
+ "Backfilled %lu app lifecycle checkpoints"
+ "Backfilling app lifecycle checkpoints for %{public}@ - %{public}@"
+ "Donated checkpoint %lu for %{public}@ at %{public}@"
+ "Failed to read App.InFocus: %{public}@"
+ "Failed to record checkpoint %lu for %{public}@: %{public}@"
+ "Nothing to backfill; resume point is not before the window end"
+ "_DASAppLifecycleRecorder"
+ "_DASProcessLifecycleDelegate"
+ "_liveDonationStartDate"
+ "absoluteTimestamp"
+ "appLifecycle"
+ "backfillCheckpointsUpToDate:"
+ "backfillHistoryPrecedingLiveWindow"
+ "com.apple.DocumentsApp"
+ "com.apple.MobileSMS"
+ "com.apple.Notes"
+ "com.apple.dasd.appLifecycleBackfill"
+ "com.apple.dasd.appLifecycleRecorder"
+ "com.apple.iCal"
+ "com.apple.mail"
+ "com.apple.mobilecal"
+ "com.apple.mobilenotes"
+ "com.apple.reminders"
+ "donateTransitionForApp:foregrounded:atDate:"
+ "inLongInactivityWindow"
+ "initInternal"
+ "isThermallyConstrainedHardware"
+ "notifyDelegatesOfTransitionForApp:foregrounded:atDate:"
+ "processLifecycleMonitor:observedTransitionForApp:foregrounded:atDate:"
+ "reportCustomCheckpoint:forTask:atDate:error:"
+ "resumeDateBefore:"
+ "sharedRecorder"
+ "startDonating"
+ "v32@0:8@\"_DASProcessLifecycleMonitor\"16@\"NSSet\"24"
+ "v44@0:8@\"_DASProcessLifecycleMonitor\"16@\"NSString\"24B32@\"NSDate\"36"
+ "v44@0:8@16@24B32@36"
```
