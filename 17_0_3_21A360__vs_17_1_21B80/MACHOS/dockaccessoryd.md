## dockaccessoryd

> `/usr/libexec/dockaccessoryd`

```diff

-31.3.0.0.0
-  __TEXT.__text: 0x1a609c
-  __TEXT.__auth_stubs: 0x2cb0
+55.0.0.0.0
+  __TEXT.__text: 0x1ad148
+  __TEXT.__auth_stubs: 0x2d40
   __TEXT.__objc_stubs: 0xc3a0
-  __TEXT.__objc_methlist: 0x9090
-  __TEXT.__objc_methname: 0x1586d
-  __TEXT.__cstring: 0x11fe5
+  __TEXT.__objc_methlist: 0x90d0
+  __TEXT.__objc_methname: 0x158cf
+  __TEXT.__cstring: 0x123f5
   __TEXT.__objc_classname: 0x1476
   __TEXT.__objc_methtype: 0x3378
-  __TEXT.__const: 0x2fe8
+  __TEXT.__const: 0x3028
   __TEXT.__oslogstring: 0xc5b8
   __TEXT.__gcc_except_tab: 0x7f4
-  __TEXT.__swift5_typeref: 0x1e1f
+  __TEXT.__swift5_typeref: 0x1e89
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x4334
-  __TEXT.__swift5_reflstr: 0x1c9a
-  __TEXT.__swift5_fieldmd: 0x2050
+  __TEXT.__constg_swiftt: 0x44a8
+  __TEXT.__swift5_reflstr: 0x1d6a
+  __TEXT.__swift5_fieldmd: 0x20e8
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__swift5_capture: 0xe9c
+  __TEXT.__swift5_capture: 0xf38
   __TEXT.__swift5_proto: 0x1bc
-  __TEXT.__swift5_types: 0x1a0
+  __TEXT.__swift5_types: 0x1a8
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4874
-  __TEXT.__eh_frame: 0x41c8
-  __DATA_CONST.__auth_got: 0x1668
-  __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0x6f60
+  __TEXT.__unwind_info: 0x49c4
+  __TEXT.__eh_frame: 0x4258
+  __DATA_CONST.__auth_got: 0x16b0
+  __DATA_CONST.__got: 0x5c0
+  __DATA_CONST.__auth_ptr: 0x158
+  __DATA_CONST.__const: 0x7198
   __DATA_CONST.__cfstring: 0x5e60
-  __DATA_CONST.__objc_classlist: 0x610
+  __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x2a0
+  __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x20

   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x166d0
-  __DATA.__objc_selrefs: 0x4160
-  __DATA.__objc_protorefs: 0x160
+  __DATA.__objc_const: 0x16a30
+  __DATA.__objc_selrefs: 0x4178
+  __DATA.__objc_protorefs: 0x180
   __DATA.__objc_classrefs: 0x670
   __DATA.__objc_superrefs: 0x3d8
   __DATA.__objc_ivar: 0xa10
-  __DATA.__objc_data: 0x66e0
-  __DATA.__data: 0x59a0
+  __DATA.__objc_data: 0x68b8
+  __DATA.__data: 0x5b20
   __DATA.__bss: 0x3110
-  __DATA.__common: 0x5d8
+  __DATA.__common: 0x5f0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6502
-  Symbols:   1118
-  CStrings:  6759
+  Functions: 6567
+  Symbols:   1129
+  CStrings:  6784
 
Symbols:
+ _$s10Foundation3URLV18temporaryDirectoryACvgZ
+ _$s10Foundation3URLV4pathSSvg
+ _$s10Foundation3URLV8filePath13directoryHint10relativeToACSS_AC09DirectoryF0OACSgtcfC
+ _$s10Foundation3URLV9appending9component13directoryHintACx_AC09DirectoryF0OtSyRzlF
+ _$s11DockKitCore0aC7ManagerC28diagnosticsCollectionEnabledSbvgZ
+ _$s11DockKitCore6ErrorsO37FailedToConsumeExtensionForLocalAssetyACSS_tcACmFWC
+ _$s8Dispatch0A9PredicateO7onQueueyACSo17OS_dispatch_queueCcACmFWC
+ _$s8Dispatch0A9PredicateOMa
+ _$s8Dispatch25_dispatchPreconditionTestySbAA0A9PredicateOF
+ _sandbox_extension_consume
+ _sandbox_extension_release
CStrings:
+ "Client %d has %ld pending actuator feedback messages, dropping"
+ "Client %d has %ld pending traj feedback messages, dropping"
+ "Diagnostics transfer request failed with %@"
+ "Failed something on remote proxy: %@"
+ "Failed to consume extension "
+ "No accessory connected"
+ "No accessory connected, try again"
+ "SuperBinary.uarp"
+ "_TtC14dockaccessoryd15dockCertHandler"
+ "_TtC14dockaccessoryd28CertificationServiceDelegate"
+ "_TtP11DockKitCore22DockClientCertProtocol_"
+ "_TtP11DockKitCore22DockDaemonCertProtocol_"
+ "_TtP11DockKitCore30XPCCertificationClientProtocol_"
+ "_TtP11DockKitCore30XPCDaemonCertificationProtocol_"
+ "_finishCameraSession(appId:)"
+ "_outstandingActuationNotificationCount"
+ "_outstandingTrajectoryNotificationCount"
+ "cert interface open"
+ "certificationHandler"
+ "collecting diagnostics and dumping to sys logs"
+ "com.apple.dockaccessoryd.certification"
+ "creating firmware directory ar %s"
+ "dumpState"
+ "logBuffer"
+ "manualFirmwareUpdateWithFilePath:sandboxExt:completion:"
+ "process %d is not entitled for certification. Add entitlements and try again"
+ "protocolCertification"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeItemAtPath:error:"
+ "scheduleSendBarrierBlock:"
+ "updateCameraSessionWithSession:new:completion:"
+ "v36@0:8@\"_TtC11DockKitCore24CameraSessionInformation\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?iB@\"NSError\">32"
- "%s %s %ld"
- "Device connection failed with error "
- "Failing setting "
- "Setting accessory reachable %@"
- "finishCameraSession(appId:)"
- "manualFirmwareUpdateWithInfo:path:completion:"
- "msg"
- "pg is %s"
- "updateCameraSessionWithSession:completion:"
- "v32@0:8@\"_TtC11DockKitCore24CameraSessionInformation\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v40@0:8@\"_TtC11DockKitCore12DockCoreInfo\"16@\"NSString\"24@?<v@?iB@\"NSError\">32"

```
