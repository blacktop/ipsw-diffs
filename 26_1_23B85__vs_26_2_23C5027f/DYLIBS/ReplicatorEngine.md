## ReplicatorEngine

> `/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine`

```diff

-126.1.6.0.0
-  __TEXT.__text: 0x17bbe0
-  __TEXT.__auth_stubs: 0x2870
+126.2.3.0.0
+  __TEXT.__text: 0x17dfe8
+  __TEXT.__auth_stubs: 0x28b0
   __TEXT.__objc_methlist: 0x5f4
-  __TEXT.__const: 0xb3e8
-  __TEXT.__cstring: 0x37a8
+  __TEXT.__const: 0xb4c8
+  __TEXT.__cstring: 0x3858
   __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__oslogstring: 0x7dfd
-  __TEXT.__constg_swiftt: 0x3cd0
-  __TEXT.__swift5_typeref: 0x3990
+  __TEXT.__oslogstring: 0x7f2d
+  __TEXT.__constg_swiftt: 0x3dd4
+  __TEXT.__swift5_typeref: 0x3a4e
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x25e5
-  __TEXT.__swift5_fieldmd: 0x30fc
+  __TEXT.__swift5_reflstr: 0x2615
+  __TEXT.__swift5_fieldmd: 0x3194
   __TEXT.__swift5_assocty: 0x4b8
-  __TEXT.__swift5_proto: 0x920
-  __TEXT.__swift5_types: 0x368
-  __TEXT.__swift5_capture: 0x255c
+  __TEXT.__swift5_proto: 0x928
+  __TEXT.__swift5_types: 0x374
+  __TEXT.__swift5_capture: 0x25c8
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift5_protos: 0xa0
+  __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x40d8
+  __TEXT.__unwind_info: 0x4118
   __TEXT.__eh_frame: 0x5d94
   __TEXT.__objc_classname: 0x16e
-  __TEXT.__objc_methname: 0x1723
+  __TEXT.__objc_methname: 0x1772
   __TEXT.__objc_methtype: 0xa7a
   __TEXT.__objc_stubs: 0x860
-  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__got: 0x738
   __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x728
+  __DATA_CONST.__objc_selrefs: 0x730
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1448
-  __AUTH_CONST.__const: 0xa8b0
+  __AUTH_CONST.__auth_got: 0x1468
+  __AUTH_CONST.__const: 0xaae0
   __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x41a8
+  __AUTH_CONST.__objc_const: 0x42c0
   __AUTH.__objc_data: 0x710
-  __AUTH.__data: 0x43d8
+  __AUTH.__data: 0x44c8
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x2dc0
+  __DATA.__data: 0x2dd0
   __DATA.__bss: 0x10690
-  __DATA.__common: 0x188
+  __DATA.__common: 0x190
   __DATA_DIRTY.__objc_data: 0x158
   __DATA_DIRTY.__data: 0x458
   __DATA_DIRTY.__bss: 0x580

   - /System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4784A2DB-B66E-31B1-A891-BD8BC4B2C3E6
-  Functions: 6419
-  Symbols:   3113
-  CStrings:  1258
+  UUID: 7FCACF48-AEB5-3E1A-B0A2-19C5667B6EE9
+  Functions: 6453
+  Symbols:   3148
+  CStrings:  1269
 
Symbols:
+ _BSDispatchQueueAssertMain
+ _OBJC_CLASS_$_BSContinuousMachTimer
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __DATA__TtC16ReplicatorEngine11PowerLogger
+ __IVARS__TtC16ReplicatorEngine11PowerLogger
+ __METACLASS_DATA__TtC16ReplicatorEngine11PowerLogger
+ _symbolic $s16ReplicatorEngine12PowerLoggingP
+ _symbolic $s16ReplicatorEngine13PowerLogEntryP
+ _symbolic Say______pG 16ReplicatorEngine13PowerLogEntryP
+ _symbolic So21BSContinuousMachTimerCSg
+ _symbolic _____ 16ReplicatorEngine11PowerLoggerC
+ _symbolic _____ 16ReplicatorEngine8PowerLogO
+ _symbolic _____ 16ReplicatorEngine8PowerLogO15RecordSyncEventV
+ _symbolic _____SgXw 16ReplicatorEngine11PowerLoggerC
+ _symbolic _____SgXwz_Xx 16ReplicatorEngine11PowerLoggerC
+ _symbolic ______p 16ReplicatorEngine12PowerLoggingP
+ _symbolic ______p 16ReplicatorEngine13PowerLogEntryP
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 16ReplicatorEngine13PowerLogEntryP
+ _type_layout_string 16ReplicatorEngine8PowerLogO15RecordSyncEventV
CStrings:
+ "%{public}s Adding record with record ID: %{public}s client defined ID: %{public}s"
+ "(%{public}s) Allow list prevents sending sync item record id: %{public}s Error: %{public}s."
+ "(%{public}s) Error sending sync item record id: %{public}s Error: %{public}s"
+ "(%{public}s) Network failure encountered when sending sync item record id: %{public}s Error: %{public}s"
+ "Adding records with IDs: %{public}s and client defined IDs %{public}s"
+ "Powerlog Flush Periodic Timer"
+ "Record sync completed record id: %{public}s"
+ "_TtC16ReplicatorEngine11PowerLogger"
+ "com.apple.replicatord.powerlog"
+ "entries"
+ "flushTimer"
+ "powerLogger"
+ "scheduleRepeatingWithFireInterval:repeatInterval:leewayInterval:queue:handler:"
+ "v16@?0@\"BSContinuousMachTimer\"8"
- "(%{public}s) Allow list prevents sending sync item: %{public}s."
- "(%{public}s) Error sending sync item: %{public}s"
- "(%{public}s) Network failure encountered when sending sync item: %{public}s"

```
