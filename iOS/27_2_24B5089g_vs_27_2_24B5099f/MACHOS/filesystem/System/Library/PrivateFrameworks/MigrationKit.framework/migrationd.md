## migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-1439.0.0.0.0
-  __TEXT.__text: 0x19ba4
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_stubs: 0x440
-  __TEXT.__objc_methlist: 0x44c
-  __TEXT.__cstring: 0x43c
+1441.40.1.0.0
+  __TEXT.__text: 0x1be00
+  __TEXT.__auth_stubs: 0x1260
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__objc_methlist: 0x464
+  __TEXT.__cstring: 0x53c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x984
-  __TEXT.__const: 0x6aa
+  __TEXT.__swift5_typeref: 0x4c5
+  __TEXT.__const: 0x6ca
+  __TEXT.__swift5_capture: 0x440
+  __TEXT.__oslogstring: 0xa14
   __TEXT.__constg_swiftt: 0x204
-  __TEXT.__swift5_typeref: 0x4ab
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x137
   __TEXT.__swift5_fieldmd: 0x170
   __TEXT.__swift5_types: 0x14
   __TEXT.__objc_classname: 0x11f
-  __TEXT.__objc_methtype: 0x58b
-  __TEXT.__swift5_capture: 0x428
-  __TEXT.__swift_as_entry: 0xa4
-  __TEXT.__swift_as_ret: 0xa0
-  __TEXT.__swift_as_cont: 0x1c4
-  __TEXT.__objc_methname: 0xaed
+  __TEXT.__objc_methname: 0xb05
+  __TEXT.__objc_methtype: 0x5ab
+  __TEXT.__swift_as_entry: 0xac
+  __TEXT.__swift_as_ret: 0xb4
+  __TEXT.__swift_as_cont: 0x1e0
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x8c8
-  __TEXT.__eh_frame: 0x14e0
-  __DATA_CONST.__const: 0x878
+  __TEXT.__unwind_info: 0x958
+  __TEXT.__eh_frame: 0x1700
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__auth_got: 0x8f8
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__auth_ptr: 0x1c8
-  __DATA.__objc_const: 0x720
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA_CONST.__auth_got: 0x938
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__auth_ptr: 0x1d8
+  __DATA.__objc_const: 0x728
+  __DATA.__objc_selrefs: 0x2b8
   __DATA.__objc_data: 0x188
-  __DATA.__data: 0x5d0
+  __DATA.__data: 0x5f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 453
-  Symbols:   484
-  CStrings:  244
+  Functions: 474
+  Symbols:   499
+  CStrings:  256
 
Symbols:
+ _$s12MigrationKit20TransferCancelOriginO04userD0yA2CmFWC
+ _$s12MigrationKit20TransferCancelOriginO8uiExitedyA2CmFWC
+ _$s12MigrationKit20TransferCancelOriginO9uiCrashedyA2CmFWC
+ _$s12MigrationKit20TransferCancelOriginOMa
+ _$s12MigrationKit20TransferCancelOriginOMn
+ _$s12MigrationKit21TransferCancelContextV6origin7message15underlyingError8function4file4lineAcA0cD6OriginO_SSs0I0_pSgs12StaticStringVAOSutcfC
+ _$s12MigrationKit21TransferCancelContextV6originAA0cD6OriginOvg
+ _$s12MigrationKit21TransferCancelContextVMa
+ _$s12MigrationKit21TransferCancelContextVMn
+ _$s12MigrationKit27AppContentTelemetryBackstopO15registerHandleryyFZ
+ _$s12MigrationKit27AppContentTelemetryBackstopO9reconcileyyYaFZ
+ _$s12MigrationKit27AppContentTelemetryBackstopO9reconcileyyYaFZTu
+ _$s12MigrationKit6ClientC25currentTelemetrySessionIDs6UInt16VSgyYaFTjTu
+ _$s12MigrationKit6ClientC6cancel0D7ContextyAA014TransferCancelE0VSg_tYaFTjTu
+ _$s12MigrationKit6ServerC25currentTelemetrySessionIDs6UInt16VSgyYaFTjTu
+ _$s12MigrationKit6ServerC6cancel0D7ContextyAA014TransferCancelE0VSg_tYaFTjTu
+ _$sSS10describingSSx_tclufC
+ _$ss11_StringGutsV4growyySiF
- _$s12MigrationKit6ClientC6cancelyyYaFTjTu
- _$s12MigrationKit6ServerC6cancelyyYaFTjTu
- _swift_retain_x28
CStrings:
+ "UI connection interrupted: "
+ "UI connection invalidated: "
+ "User cancelled migration from the UI"
+ "cancel(cancelContext:)"
+ "cancel(origin: %{public}s)"
+ "com.apple.migrationd.deferred-tasks"
+ "didUpdateTelemetrySessionID:"
+ "interrupted(pid:processName:)"
+ "invalidated(pid:processName:)"
+ "no telemetry session id to push to the cellular client."
+ "pushing the telemetry session id. session_id=%hu"
+ "v20@0:8S16"
```
