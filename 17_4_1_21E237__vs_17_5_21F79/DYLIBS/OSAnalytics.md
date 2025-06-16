## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-656.100.20.0.0
-  __TEXT.__text: 0x37560
-  __TEXT.__auth_stubs: 0x1330
-  __TEXT.__objc_methlist: 0x14e4
-  __TEXT.__const: 0x4e8
-  __TEXT.__oslogstring: 0x2e07
-  __TEXT.__cstring: 0x7cc3
-  __TEXT.__gcc_except_tab: 0xdb8
+656.122.3.0.0
+  __TEXT.__text: 0x3a37c
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_methlist: 0x16e4
+  __TEXT.__const: 0x4f0
+  __TEXT.__oslogstring: 0x3101
+  __TEXT.__cstring: 0x8079
+  __TEXT.__gcc_except_tab: 0xdc0
   __TEXT.__dlopen_cstrs: 0x163
-  __TEXT.__unwind_info: 0x8a4
-  __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x43dc
-  __TEXT.__objc_methtype: 0x9ad
-  __TEXT.__objc_stubs: 0x3f00
+  __TEXT.__unwind_info: 0x958
+  __TEXT.__objc_classname: 0x301
+  __TEXT.__objc_methname: 0x481e
+  __TEXT.__objc_methtype: 0x9f2
+  __TEXT.__objc_stubs: 0x4200
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__const: 0xee0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20c0
-  __DATA_CONST.__objc_selrefs: 0x12a0
-  __DATA_CONST.__objc_classrefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_const: 0x2548
+  __DATA_CONST.__objc_selrefs: 0x1380
+  __DATA_CONST.__objc_classrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x8f0
-  __AUTH_CONST.__objc_const: 0x9f0
-  __AUTH_CONST.__cfstring: 0x8300
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__cfstring: 0x85e0
+  __AUTH_CONST.__objc_const: 0xb58
+  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x9a8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x1b8
+  __AUTH_CONST.__auth_got: 0x9b0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x25c
+  __DATA.__data: 0x1c8
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x2b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FAAA956E-1920-31B2-A440-14C64EA33A64
-  Functions: 830
-  Symbols:   3209
-  CStrings:  3604
+  UUID: 83C4B13B-59F9-3FB1-937C-15162A770FD0
+  Functions: 902
+  Symbols:   3432
+  CStrings:  3725
 
Symbols:
+ -[ExclaveAddressSpace .cxx_destruct]
+ -[ExclaveAddressSpace addressSpaceId]
+ -[ExclaveAddressSpace layoutId]
+ -[ExclaveAddressSpace name]
+ -[ExclaveAddressSpace setAddressSpaceId:]
+ -[ExclaveAddressSpace setLayoutId:]
+ -[ExclaveAddressSpace setName:]
+ -[ExclaveLayout .cxx_destruct]
+ -[ExclaveLayout init]
+ -[ExclaveLayout layoutId]
+ -[ExclaveLayout segments]
+ -[ExclaveLayout setLayoutId:]
+ -[ExclaveLayout setSegments:]
+ -[ExclaveStackEntry .cxx_destruct]
+ -[ExclaveStackEntry addFrames:]
+ -[ExclaveStackEntry addressSpaceId]
+ -[ExclaveStackEntry frames]
+ -[ExclaveStackEntry setAddressSpaceId:]
+ -[ExclaveStackEntry setFrames:]
+ -[ExclaveThread .cxx_destruct]
+ -[ExclaveThread addStackEntries:]
+ -[ExclaveThread schedulingContextId]
+ -[ExclaveThread setSchedulingContextId:]
+ -[ExclaveThread setStackEntries:]
+ -[ExclaveThread stackEntries]
+ -[OSAExclaveContainer .cxx_destruct]
+ -[OSAExclaveContainer addressSpaces]
+ -[OSAExclaveContainer appendNotesTo:]
+ -[OSAExclaveContainer getFramesForThread:usingCatalog:]
+ -[OSAExclaveContainer getFramesForThread:usingCatalog:].cold.1
+ -[OSAExclaveContainer getFramesForThread:usingCatalog:].cold.2
+ -[OSAExclaveContainer getFramesForThread:usingCatalog:].cold.3
+ -[OSAExclaveContainer init]
+ -[OSAExclaveContainer isExclaveValid]
+ -[OSAExclaveContainer layouts]
+ -[OSAExclaveContainer notes]
+ -[OSAExclaveContainer parseKCdata:]
+ -[OSAExclaveContainer parseKCdata:].cold.1
+ -[OSAExclaveContainer parseKCdata:].cold.2
+ -[OSAExclaveContainer parseKCdata:].cold.3
+ -[OSAExclaveContainer parseKCdata:].cold.4
+ -[OSAExclaveContainer parseKCdata:].cold.5
+ -[OSAExclaveContainer parseKCdata:].cold.6
+ -[OSAExclaveContainer parseKCdata:].cold.7
+ -[OSAExclaveContainer parseKCdata:].cold.8
+ -[OSAExclaveContainer setIsExclaveValid:]
+ -[OSAExclaveContainer setNotes:]
+ -[OSAExclaveContainer setThreadId:withScId:]
+ -[OSAExclaveContainer threadIdToScId]
+ -[OSAExclaveContainer threads]
+ -[OSAStackShotReport decodeKCDataWithBlock:withTuning:usingCatalog:].cold.21
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table7
+ GCC_except_table9
+ _OBJC_CLASS_$_ExclaveAddressSpace
+ _OBJC_CLASS_$_ExclaveLayout
+ _OBJC_CLASS_$_ExclaveStackEntry
+ _OBJC_CLASS_$_ExclaveThread
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_OSAExclaveContainer
+ _OBJC_IVAR_$_ExclaveAddressSpace._addressSpaceId
+ _OBJC_IVAR_$_ExclaveAddressSpace._layoutId
+ _OBJC_IVAR_$_ExclaveAddressSpace._name
+ _OBJC_IVAR_$_ExclaveLayout._layoutId
+ _OBJC_IVAR_$_ExclaveLayout._segments
+ _OBJC_IVAR_$_ExclaveStackEntry._addressSpaceId
+ _OBJC_IVAR_$_ExclaveStackEntry._frames
+ _OBJC_IVAR_$_ExclaveThread._schedulingContextId
+ _OBJC_IVAR_$_ExclaveThread._stackEntries
+ _OBJC_IVAR_$_OSAExclaveContainer._addressSpaces
+ _OBJC_IVAR_$_OSAExclaveContainer._isExclaveValid
+ _OBJC_IVAR_$_OSAExclaveContainer._layouts
+ _OBJC_IVAR_$_OSAExclaveContainer._notes
+ _OBJC_IVAR_$_OSAExclaveContainer._threadIdToScId
+ _OBJC_IVAR_$_OSAExclaveContainer._threads
+ _OBJC_METACLASS_$_ExclaveAddressSpace
+ _OBJC_METACLASS_$_ExclaveLayout
+ _OBJC_METACLASS_$_ExclaveStackEntry
+ _OBJC_METACLASS_$_ExclaveThread
+ _OBJC_METACLASS_$_OSAExclaveContainer
+ _OSAGetBootTime
+ _OSAGetProcessUptime
+ __OBJC_$_INSTANCE_METHODS_ExclaveAddressSpace
+ __OBJC_$_INSTANCE_METHODS_ExclaveLayout
+ __OBJC_$_INSTANCE_METHODS_ExclaveStackEntry
+ __OBJC_$_INSTANCE_METHODS_ExclaveThread
+ __OBJC_$_INSTANCE_METHODS_OSAExclaveContainer
+ __OBJC_$_INSTANCE_VARIABLES_ExclaveAddressSpace
+ __OBJC_$_INSTANCE_VARIABLES_ExclaveLayout
+ __OBJC_$_INSTANCE_VARIABLES_ExclaveStackEntry
+ __OBJC_$_INSTANCE_VARIABLES_ExclaveThread
+ __OBJC_$_INSTANCE_VARIABLES_OSAExclaveContainer
+ __OBJC_$_PROP_LIST_ExclaveAddressSpace
+ __OBJC_$_PROP_LIST_ExclaveLayout
+ __OBJC_$_PROP_LIST_ExclaveStackEntry
+ __OBJC_$_PROP_LIST_ExclaveThread
+ __OBJC_$_PROP_LIST_OSAExclaveContainer
+ __OBJC_CLASS_RO_$_ExclaveAddressSpace
+ __OBJC_CLASS_RO_$_ExclaveLayout
+ __OBJC_CLASS_RO_$_ExclaveStackEntry
+ __OBJC_CLASS_RO_$_ExclaveThread
+ __OBJC_CLASS_RO_$_OSAExclaveContainer
+ __OBJC_METACLASS_RO_$_ExclaveAddressSpace
+ __OBJC_METACLASS_RO_$_ExclaveLayout
+ __OBJC_METACLASS_RO_$_ExclaveStackEntry
+ __OBJC_METACLASS_RO_$_ExclaveThread
+ __OBJC_METACLASS_RO_$_OSAExclaveContainer
+ ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.398
+ ___OSASafeCreateDirectory_block_invoke
+ ___block_descriptor_212_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_descriptor_83_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.40
+ ___block_literal_global.60
+ ___rtc_internal_block_invoke.63
+ ___rtc_internal_block_invoke.63.cold.1
+ ___rtc_internal_block_invoke.63.cold.2
+ ___rtc_internal_block_invoke.65
+ ___rtc_internal_block_invoke.66
+ ___rtc_internal_block_invoke.66.cold.1
+ ___rtc_internal_realtime_block_invoke
+ __unnamed_array_storage.351
+ _getRTCReportingClass
+ _getkRTCReportingSessionInfoBatchEvent
+ _getkRTCReportingSessionInfoBatchEvent.cold.1
+ _getkRTCReportingSessionInfoClientType
+ _getkRTCReportingSessionInfoClientType.cold.1
+ _getkRTCReportingSessionInfoClientVersion
+ _getkRTCReportingSessionInfoClientVersion.cold.1
+ _getkRTCReportingSessionInfoContainsRealtimeEvents
+ _getkRTCReportingSessionInfoContainsRealtimeEvents.cold.1
+ _getkRTCReportingSessionInfoSessionID
+ _getkRTCReportingSessionInfoSessionID.cold.1
+ _getkRTCReportingUserInfoClientName
+ _getkRTCReportingUserInfoClientName.cold.1
+ _getkRTCReportingUserInfoServiceName
+ _getkRTCReportingUserInfoServiceName.cold.1
+ _objc_msgSend$addFrames:
+ _objc_msgSend$addStackEntries:
+ _objc_msgSend$addressSpaceId
+ _objc_msgSend$addressSpaces
+ _objc_msgSend$frames
+ _objc_msgSend$getFramesForThread:usingCatalog:
+ _objc_msgSend$isExclaveValid
+ _objc_msgSend$layoutId
+ _objc_msgSend$layouts
+ _objc_msgSend$notes
+ _objc_msgSend$parseKCdata:
+ _objc_msgSend$schedulingContextId
+ _objc_msgSend$segments
+ _objc_msgSend$sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:
+ _objc_msgSend$setAddressSpaceId:
+ _objc_msgSend$setLayoutId:
+ _objc_msgSend$setMaximumSignificantDigits:
+ _objc_msgSend$setSchedulingContextId:
+ _objc_msgSend$setThreadId:withScId:
+ _objc_msgSend$setUsesSignificantDigits:
+ _objc_msgSend$stackEntries
+ _objc_msgSend$stringForObjectValue:
+ _objc_msgSend$threadIdToScId
+ _objc_msgSend$threads
+ _objc_retain_x9
+ _objc_setProperty_nonatomic_copy
+ _rtc_internal_realtime.RTCReportingClass
+ _rtc_internal_realtime.onceToken
+ _rtcsc_send_base
+ _rtcsc_send_base.cold.1
+ _rtcsc_send_realtime
- ___block_literal_global.37
- ___rtc_internal_block_invoke.40
- ___rtc_internal_block_invoke.40.cold.1
- ___rtc_internal_block_invoke.40.cold.2
- ___rtc_internal_block_invoke.40.cold.3
- ___rtc_internal_block_invoke.40.cold.4
- ___rtc_internal_block_invoke.40.cold.5
- ___rtc_internal_block_invoke.40.cold.6
- ___rtc_internal_block_invoke.40.cold.7
- ___rtc_internal_block_invoke.40.cold.8
- ___rtc_internal_block_invoke.40.cold.9
- ___rtc_internal_block_invoke.43
- ___rtc_internal_block_invoke.51
- ___rtc_internal_block_invoke.51.cold.1
- __unnamed_array_storage.403
- _objc_release_x2
CStrings:
+ "\x03"
+ "-[OSAExclaveContainer parseKCdata:]"
+ "=== Attempted change gid on existing path: %{public}@ from %d to _analyticsusers (%u) with result %d %{public}s"
+ "=== Attempted change gid on new dir: %{public}@ from %d to _analyticsusers (%u) with result %d %{public}s"
+ "=== Attempted change perms on existing path: %{public}@ from 0x%X to 0x%X with result %d %{public}s"
+ "=== Attempted change perms on new dir: %{public}@ from 0x%X to 0x%X with result %d %{public}s"
+ "Address space info does exist for asid %@"
+ "Exclave data not present for SCID %@"
+ "Exclave data not present for thread %llu"
+ "Exclave frames offset of %d for thread %llu is invalid"
+ "ExclaveAddressSpace"
+ "ExclaveLayout"
+ "ExclaveStackEntry"
+ "ExclaveThread"
+ "Layout info does not exist for layout id %@"
+ "OSAExclave.m"
+ "OSAExclaveContainer"
+ "Omitted invalid exclave data for thread %llu"
+ "RTCReporting Realtime: sendOneMessageWithSessionInfo failed"
+ "RTCReporting Realtime: sendOneMessageWithSessionInfo succeeded"
+ "T@\"NSMutableArray\",&,N,V_frames"
+ "T@\"NSMutableArray\",&,N,V_notes"
+ "T@\"NSMutableArray\",&,N,V_segments"
+ "T@\"NSMutableArray\",&,N,V_stackEntries"
+ "T@\"NSMutableDictionary\",R,N,V_addressSpaces"
+ "T@\"NSMutableDictionary\",R,N,V_layouts"
+ "T@\"NSMutableDictionary\",R,N,V_threadIdToScId"
+ "T@\"NSMutableDictionary\",R,N,V_threads"
+ "T@\"NSNumber\",&,N,V_addressSpaceId"
+ "T@\"NSNumber\",&,N,V_layoutId"
+ "T@\"NSNumber\",&,N,V_schedulingContextId"
+ "T@\"NSString\",C,N,V_name"
+ "TB,N,V_isExclaveValid"
+ "Thread %llu has an incorrect exclave frame offset %d"
+ "Thread %llu has exclave frames but no kernel frames"
+ "Thread %llu with %lu kernel frames has exclave frames but invalid exclave frame offset of %d. Skipping adding exclave frames into kernel frames "
+ "_addressSpaceId"
+ "_addressSpaces"
+ "_frames"
+ "_isExclaveValid"
+ "_layoutId"
+ "_layouts"
+ "_schedulingContextId"
+ "_segments"
+ "_stackEntries"
+ "_threadIdToScId"
+ "_threads"
+ "addFrames:"
+ "addStackEntries:"
+ "addressSpaceId"
+ "addressSpaces"
+ "boot_time_appx"
+ "com.apple.osanalytics.directory_modification"
+ "container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_ADDRESSSPACE)"
+ "container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_IPCSTACKENTRY)"
+ "container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_SCRESULT)"
+ "container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_TEXTLAYOUT)"
+ "create_dir"
+ "create_dir_success"
+ "created directory '%{public}@'"
+ "exclaveScid"
+ "getFramesForThread:usingCatalog:"
+ "isExclaveValid"
+ "layoutId"
+ "layouts"
+ "modify_gid"
+ "modify_gid_success"
+ "modify_gid_value"
+ "modify_perms"
+ "modify_perms_success"
+ "modify_perms_value"
+ "original_gid"
+ "original_perms"
+ "osanalytics_beacon"
+ "parseKCdata:"
+ "path sanitize failed"
+ "proc_uptime_appx"
+ "progname"
+ "schedulingContextId"
+ "segments"
+ "sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:"
+ "setAddressSpaceId:"
+ "setFrames:"
+ "setIsExclaveValid:"
+ "setLayoutId:"
+ "setMaximumSignificantDigits:"
+ "setNotes:"
+ "setSchedulingContextId:"
+ "setSegments:"
+ "setStackEntries:"
+ "setThreadId:withScId:"
+ "setUsesSignificantDigits:"
+ "stackEntries"
+ "start_path"
+ "stringForObjectValue:"
+ "threadIdToScId"
+ "{kcdata_iter=^{kcdata_item}^v}32@0:8{kcdata_iter=^{kcdata_item}^v}16"
- "created directory '%@'"

```
