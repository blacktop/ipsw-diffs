## NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

-5739.4.0.0.0
-  __TEXT.__text: 0x97094
-  __TEXT.__auth_stubs: 0x2f30
+5756.0.0.0.0
+  __TEXT.__text: 0x9c528
+  __TEXT.__auth_stubs: 0x3000
   __TEXT.__objc_stubs: 0x3100
   __TEXT.__objc_methlist: 0x2308
-  __TEXT.__const: 0x5a04
+  __TEXT.__const: 0x5b74
   __TEXT.__gcc_except_tab: 0x240
-  __TEXT.__cstring: 0x5abb
-  __TEXT.__oslogstring: 0xc8a
-  __TEXT.__objc_methname: 0x6c06
+  __TEXT.__cstring: 0x5dbb
+  __TEXT.__oslogstring: 0xd5a
+  __TEXT.__objc_methname: 0x6c44
   __TEXT.__objc_classname: 0x67a
   __TEXT.__objc_methtype: 0x1c84
-  __TEXT.__constg_swiftt: 0x1ecc
-  __TEXT.__swift5_typeref: 0x677c
+  __TEXT.__constg_swiftt: 0x1f38
+  __TEXT.__swift5_typeref: 0x68fc
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x1488
-  __TEXT.__swift5_fieldmd: 0x1b4c
+  __TEXT.__swift5_reflstr: 0x14a8
+  __TEXT.__swift5_fieldmd: 0x1b90
   __TEXT.__swift5_assocty: 0x430
-  __TEXT.__swift5_proto: 0x458
-  __TEXT.__swift5_types: 0x240
+  __TEXT.__swift5_proto: 0x478
+  __TEXT.__swift5_types: 0x248
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_capture: 0x4c8
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1f38
-  __TEXT.__eh_frame: 0x1754
-  __DATA_CONST.__auth_got: 0x17b0
-  __DATA_CONST.__got: 0xc08
-  __DATA_CONST.__auth_ptr: 0xad0
-  __DATA_CONST.__const: 0x3be0
+  __TEXT.__unwind_info: 0x1fe8
+  __TEXT.__eh_frame: 0x19ec
+  __DATA_CONST.__auth_got: 0x1818
+  __DATA_CONST.__got: 0xc18
+  __DATA_CONST.__auth_ptr: 0xae8
+  __DATA_CONST.__const: 0x3c70
   __DATA_CONST.__cfstring: 0xb00
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0x1e0
-  __DATA.__objc_const: 0x55b8
-  __DATA.__objc_selrefs: 0x1a40
+  __DATA.__objc_const: 0x5648
+  __DATA.__objc_selrefs: 0x1a60
   __DATA.__objc_ivar: 0x118
-  __DATA.__objc_data: 0x1380
-  __DATA.__data: 0x4d58
-  __DATA.__bss: 0x8318
-  __DATA.__common: 0xc0
+  __DATA.__objc_data: 0x13d0
+  __DATA.__data: 0x4ed8
+  __DATA.__bss: 0x8718
+  __DATA.__common: 0xc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 686F0FC8-6421-3212-A159-62A63DF1C3E4
-  Functions: 2805
-  Symbols:   591
-  CStrings:  2029
+  UUID: 588CDB0F-BABD-365F-807A-FED878228AB2
+  Functions: 2869
+  Symbols:   594
+  CStrings:  2048
 
Symbols:
+ _FCIsWidgetDebugInspectionEnabled
+ _FCURLForWidgetDebugLogs
+ _OBJC_CLASS_$_NSDateFormatter
CStrings:
+ "_TtC7NewsTag19WidgetDebugLogStore"
+ "assembled %zd sessions, coalesced to %zd"
+ "creating missing disappearance for batch with engagement"
+ "debugInspection"
+ "discarding batch because disappearance event date %{public}@ is not after appearance event date %{public}@"
+ "discarding batch from %{public}@ because it has no disappearance event"
+ "event batch produced session, appearedAt=%{public}@, disappearedAt=%{public}@, enagged=%{public}@"
+ "event-processing sidecar task limited sessions from %ld to %ld"
+ "failed to create TTR view because a URL could not be constructed, logsPath=%{public}@"
+ "failed to log debug inspection to disk, error=%{public}@"
+ "failed to prune debug inspection log, url=%{public}@, error=%{public}@"
+ "failed to prune debug inspection logs, error=%{public}@"
+ "fc_gzipDeflate"
+ "https://apple.news/ttr?attachments="
+ "logsDirectory"
+ "maxCountOnDisk"
+ "processing event batch: %{public}@"
+ "reporting widget session, appearedAt=%{public}@, disappearedAt=%{public}@, enagaged=%{public}@"
+ "setDateFormat:"
+ "stringFromDate:"
+ "widget-inspection-data-"
+ "will not register seen headlines because none are eligible"
+ "will not register seen headlines because the user engaged with the widget"
+ "will not register seen headlines because widgets are not the only thing visible"
+ "will register seen headlines due to widget disappearance, disappearanceDate=%{public}@, exposureTime=%llums, exposureTimeThreshold=%llums"
- "assembled %zd sessions"
- "creating missing disappearance for batch with needed events"
- "creating missing disappearance for most recent batch"
- "discarding batch because it has no disappearance event"
- "reporting widget session, appearedAt=%{public}@, disappearedAt=%{public}@"
- "will register once-visible headlines due to widget disappearance, disappearanceDate=%{public}@, exposureTime=%llums, exposureTimeThreshold=%llums"

```
