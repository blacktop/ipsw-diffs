## PrivacyAndSecuritySettings

> `/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`

```diff

-2027.1.5.1.100
-  __TEXT.__text: 0x8ab94
-  __TEXT.__auth_stubs: 0x2cf0
-  __TEXT.__objc_stubs: 0xf60
+2027.1.7.0.0
+  __TEXT.__text: 0x92e9c
+  __TEXT.__auth_stubs: 0x2da0
+  __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x5a8
-  __TEXT.__const: 0x73f4
+  __TEXT.__const: 0x77e4
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__cstring: 0x4486
-  __TEXT.__objc_classname: 0xd6a
-  __TEXT.__constg_swiftt: 0x1688
-  __TEXT.__swift5_typeref: 0x7d8a
-  __TEXT.__objc_methname: 0x1f75
+  __TEXT.__cstring: 0x4766
+  __TEXT.__objc_classname: 0xdba
+  __TEXT.__constg_swiftt: 0x1864
+  __TEXT.__swift5_typeref: 0x85a2
+  __TEXT.__objc_methname: 0x2095
   __TEXT.__objc_methtype: 0x5c9
-  __TEXT.__swift5_reflstr: 0x1ba1
-  __TEXT.__swift5_fieldmd: 0x1718
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_assocty: 0x430
-  __TEXT.__swift5_capture: 0xb4c
-  __TEXT.__swift5_proto: 0x238
-  __TEXT.__swift5_types: 0x164
-  __TEXT.__swift_as_entry: 0xe4
-  __TEXT.__swift_as_ret: 0xb4
-  __TEXT.__swift_as_cont: 0x1f4
+  __TEXT.__swift5_reflstr: 0x1c51
+  __TEXT.__swift5_fieldmd: 0x1820
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_assocty: 0x478
+  __TEXT.__swift5_capture: 0xc08
+  __TEXT.__swift5_proto: 0x260
+  __TEXT.__swift5_types: 0x170
+  __TEXT.__swift_as_entry: 0xf4
+  __TEXT.__swift_as_ret: 0xc8
+  __TEXT.__swift_as_cont: 0x2ec
   __TEXT.__oslogstring: 0xea1
+  __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x54
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2558
-  __TEXT.__eh_frame: 0x2e24
-  __DATA_CONST.__const: 0x3928
+  __TEXT.__unwind_info: 0x27d0
+  __TEXT.__eh_frame: 0x36ec
+  __DATA_CONST.__const: 0x3c38
   __DATA_CONST.__cfstring: 0x40
-  __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x1688
-  __DATA_CONST.__got: 0xb58
-  __DATA_CONST.__auth_ptr: 0xd48
-  __DATA.__objc_const: 0x2f40
-  __DATA.__objc_selrefs: 0x670
+  __DATA_CONST.__auth_got: 0x16e0
+  __DATA_CONST.__got: 0xb88
+  __DATA_CONST.__auth_ptr: 0xd58
+  __DATA.__objc_const: 0x3178
+  __DATA.__objc_selrefs: 0x688
   __DATA.__objc_data: 0x970
-  __DATA.__data: 0x3e70
-  __DATA.__common: 0xf8
+  __DATA.__data: 0x4038
+  __DATA.__common: 0x108
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreODI.framework/CoreODI
   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2526
-  Symbols:   360
-  CStrings:  885
+  Functions: 2660
+  Symbols:   366
+  CStrings:  913
 
Symbols:
+ _AnalyticsCreateSession
+ _AnalyticsEndSession
+ _AnalyticsSendEventWithSession
+ _NSFileSize
+ _objc_release_x1
+ _swift_unknownObjectWeakAssign
CStrings:
+ "PrivacySettings.ExportAllFailed"
+ "PrivacySettings.TransferLogEmptyResult"
+ "_TtC26PrivacyAndSecuritySettings31PUIAnalyticsLogTelemetrySession"
+ "activeViewCount"
+ "attributesOfItemAtPath:error:"
+ "code"
+ "com.apple.settings.view_analytics_logs.export_complete"
+ "com.apple.settings.view_analytics_logs.export_initiated"
+ "com.apple.settings.view_analytics_logs.file_opened"
+ "com.apple.settings.view_analytics_logs.filter_applied"
+ "com.apple.settings.view_analytics_logs.pane_visit"
+ "com.apple.settings.view_analytics_logs.remote_device_request_complete"
+ "com.apple.settings.view_analytics_logs.remote_device_request_initiated"
+ "deviceClass"
+ "domain"
+ "fetchLogsOnBackgroundThread(for:deviceClass:using:)"
+ "generationLatencyMs"
+ "graceSeconds"
+ "hasEnded"
+ "missingFileCount"
+ "pendingEndTask"
+ "reportType"
+ "requestLatencyMs"
+ "requestedDeviceType"
+ "sessionDomain"
+ "sessionId"
+ "telemetry"
+ "telemetryFactory"
+ "transferLog(filePath:for:deviceClass:reportType:)"
+ "transport"
- "fetchLogsOnBackgroundThread(for:using:)"
- "transferLog(filePath:for:)"
```
