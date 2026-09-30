## securityd

> `/usr/libexec/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__thread_vars`

```diff

-62460.40.49.502.1
-  __TEXT.__text: 0x267174
+62460.40.56.502.1
+  __TEXT.__text: 0x267540
   __TEXT.__auth_stubs: 0x4340
-  __TEXT.__objc_stubs: 0x1d9e0
-  __TEXT.__objc_methlist: 0x15e98
+  __TEXT.__objc_stubs: 0x1da60
+  __TEXT.__objc_methlist: 0x15ec0
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x22bd0
-  __TEXT.__objc_methname: 0x2e65f
-  __TEXT.__oslogstring: 0x2ff02
+  __TEXT.__cstring: 0x22bde
+  __TEXT.__objc_methname: 0x2e77f
+  __TEXT.__oslogstring: 0x2ff32
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
-  __TEXT.__objc_classname: 0x2559
-  __TEXT.__objc_methtype: 0xb0a4
+  __TEXT.__objc_classname: 0x2577
+  __TEXT.__objc_methtype: 0xb0cf
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0xa0c8
+  __TEXT.__gcc_except_tab: 0xa124
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x7cb8
+  __TEXT.__unwind_info: 0x7cd0
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x14a40
+  __DATA_CONST.__const: 0x14a28
   __DATA_CONST.__cfstring: 0x1c760
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x260
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x810

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__auth_got: 0x21b0
-  __DATA_CONST.__got: 0x1550
+  __DATA_CONST.__got: 0x1558
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x23cd8
-  __DATA.__objc_selrefs: 0x98b8
-  __DATA.__objc_ivar: 0x1ae8
+  __DATA.__objc_const: 0x23d18
+  __DATA.__objc_selrefs: 0x98d8
+  __DATA.__objc_ivar: 0x1aec
   __DATA.__objc_data: 0x5d98
-  __DATA.__data: 0x3158
+  __DATA.__data: 0x31b8
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x28
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9920
-  Symbols:   1894
-  CStrings:  16432
+  Functions: 9922
+  Symbols:   1895
+  CStrings:  16443
 
Symbols:
+ _AKTelemetryFlowID
CStrings:
+ "@\"<TDLNotificationFlowIDConsumer>\""
+ "@212@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136#144#152@160@168B176B180B184@188@196@204"
+ "T@\"<TDLNotificationFlowIDConsumer>\",R,W,V_tdlNotificationFlowIDConsumer"
+ "TDLNotificationFlowIDConsumer"
+ "Updating trusted device list, flowID source: %s"
+ "_tdlNotificationFlowIDConsumer"
+ "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:idmsStableTrustedDevicesVersion:flowID:"
+ "consumeIdMSTDLNotificationFlowID"
+ "idMSTDLNotificationFlowID"
+ "idms"
+ "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsD:accountIsW:reachabilityTracker:escrowChecker:tdlNotificationFlowIDConsumer:"
+ "initWithFlowID:deviceSessionID:idMSTDLNotificationFlowID:"
+ "not idms"
+ "notificationOfMachineIDListChangeWithFlowID:"
+ "requestTrustedDeviceListRefreshWithFlowID:"
+ "setTelemetryFlowID:"
+ "tdlNotificationFlowIDConsumer"
+ "v100@0:8@16@24@32@40@48@56@64B72@76@84@92"
+ "\xf1b"
- "@204@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136#144#152@160@168B176B180B184@188@196"
- "afterAuthKitFetch:userInitiatedRemovals:evictedRemovals:unknownReasonRemovals:trustedDeviceHash:deletedDeviceHash:trustedDevicesUpdateTimestamp:accountIsDemo:version:idmsStableTrustedDevicesVersion:"
- "initForContainer:contextID:activeAccount:stateHolder:flagHandler:sosAdapter:octagonAdapter:accountsAdapter:authKitAdapter:personaAdapter:deviceInfoAdapter:secureBackupAdapter:laContextAdapter:ckksAccountSync:lockStateTracker:cuttlefishXPCWrapper:escrowRequestClass:notifierClass:flowID:deviceSessionID:permittedToSendMetrics:accountIsD:accountIsW:reachabilityTracker:escrowChecker:"
- "initWithFlowID:deviceSessionID:"
- "notificationOfMachineIDListChange"
- "requestTrustedDeviceListRefresh"
- "v92@0:8@16@24@32@40@48@56@64B72@76@84"
- "\xf1a"
```
