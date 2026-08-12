## DriverManagement

> `/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement`

```diff

-514.0.0.0.0
-  __TEXT.__text: 0x1a6fc
-  __TEXT.__objc_methlist: 0x2b0
-  __TEXT.__const: 0x1af0
-  __TEXT.__cstring: 0xa15
-  __TEXT.__swift5_typeref: 0x692
+514.2.1.0.0
+  __TEXT.__text: 0x1b3b4
+  __TEXT.__objc_methlist: 0x2c4
+  __TEXT.__const: 0x1b20
+  __TEXT.__cstring: 0xb05
+  __TEXT.__swift5_typeref: 0x702
   __TEXT.__constg_swiftt: 0x420
-  __TEXT.__swift5_reflstr: 0x387
-  __TEXT.__swift5_fieldmd: 0x504
+  __TEXT.__swift5_reflstr: 0x3a7
+  __TEXT.__swift5_fieldmd: 0x520
   __TEXT.__swift5_proto: 0x150
   __TEXT.__swift5_types: 0x70
   __TEXT.__swift5_assocty: 0x78

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x16c
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x770
+  __TEXT.__unwind_info: 0x790
   __TEXT.__eh_frame: 0x7a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c0
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x1c8
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x1d0
-  __AUTH_CONST.__const: 0xef8
-  __AUTH_CONST.__objc_const: 0x6c0
-  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__const: 0xf48
+  __AUTH_CONST.__objc_const: 0x748
+  __AUTH_CONST.__auth_got: 0x7a8
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x2e8
+  __DATA.__data: 0x2f8
   __DATA.__bss: 0x19d0
   __DATA_DIRTY.__objc_data: 0x300
-  __DATA_DIRTY.__data: 0x600
+  __DATA_DIRTY.__data: 0x608
   __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x1080
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 742
-  Symbols:   477
-  CStrings:  56
+  Functions: 754
+  Symbols:   485
+  CStrings:  60
 
Symbols:
+ -[DriverManager driverApprovalStatesForCurrentAppWithError:]
+ __PROTOCOL_INSTANCE_METHODS__TtP16DriverManagement32DriverKitDaemonAppClientProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP16DriverManagement32DriverKitDaemonAppClientProtocol_
+ __PROTOCOL__TtP16DriverManagement32DriverKitDaemonAppClientProtocol_
+ _flat unique 16DriverManagement0A26KitDaemonAppClientProtocol_p
+ _objc_autorelease
+ _objc_msgSend$driverApprovalStatesForCurrentAppWithError:
+ _objc_msgSend$getApprovalStateForCallingAppWithReplyBlock:
+ _symbolic $s16DriverManagement0A26KitDaemonAppClientProtocolP
+ _symbolic ______p 16DriverManagement0A26KitDaemonAppClientProtocolP
- -[DriverManager refreshForCurrentAppSync]
- _objc_msgSend$refreshForCurrentAppSync
CStrings:
+ "Connection to service %{public}s invalidated"
+ "Failed to get approval states for current app: %{public}s"
+ "Failed to get scoped approval state"
+ "Unexpected non-third-party entry on scoped app path: %{public}s"
+ "com.apple.DriverKitAppServer"
+ "driverApprovalStatesForCurrentApp(withError:)"
+ "fetchApprovalStatesForCurrentAppSync()"
- "Failed to get approval state"
- "refreshApprovalStatesForCurrentApp()"
- "refreshForCurrentAppSync()"
```
