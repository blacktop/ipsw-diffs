## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_stublist`
- `__DATA.__common`

```diff

-1064.0.0.0.0
-  __TEXT.__text: 0x3ef6b0
+1067.0.0.0.0
+  __TEXT.__text: 0x3f2bd0
   __TEXT.__auth_stubs: 0x37d0
-  __TEXT.__objc_stubs: 0x4d00
+  __TEXT.__objc_stubs: 0x4d40
   __TEXT.__objc_methlist: 0xf80
-  __TEXT.__objc_methname: 0x7795
+  __TEXT.__objc_methname: 0x77d5
   __TEXT.__objc_classname: 0x2e9d
-  __TEXT.__cstring: 0x4599
+  __TEXT.__cstring: 0x46a9
   __TEXT.__objc_methtype: 0x2024
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x133b0
-  __TEXT.__constg_swiftt: 0xc578
-  __TEXT.__swift5_typeref: 0x7921
+  __TEXT.__const: 0x13350
+  __TEXT.__constg_swiftt: 0xc5f4
+  __TEXT.__swift5_typeref: 0x7993
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0x66b5
-  __TEXT.__swift5_fieldmd: 0x660c
+  __TEXT.__swift5_reflstr: 0x66d5
+  __TEXT.__swift5_fieldmd: 0x6638
   __TEXT.__swift5_assocty: 0x950
-  __TEXT.__swift5_proto: 0xc7c
+  __TEXT.__swift5_proto: 0xc74
   __TEXT.__swift5_types: 0x638
-  __TEXT.__swift5_capture: 0x654c
-  __TEXT.__oslogstring: 0x2095d
-  __TEXT.__swift5_protos: 0x224
+  __TEXT.__swift5_capture: 0x65fc
+  __TEXT.__oslogstring: 0x20c9d
+  __TEXT.__swift5_protos: 0x22c
   __TEXT.__swift_as_entry: 0x674
-  __TEXT.__swift_as_ret: 0x884
-  __TEXT.__swift_as_cont: 0x11d0
+  __TEXT.__swift_as_ret: 0x87c
+  __TEXT.__swift_as_cont: 0x11c4
   __TEXT.__swift5_acfuncs: 0xb4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x84f0
-  __TEXT.__eh_frame: 0x147c4
-  __DATA_CONST.__const: 0x13e40
+  __TEXT.__unwind_info: 0x8510
+  __TEXT.__eh_frame: 0x146cc
+  __DATA_CONST.__const: 0x13f60
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0x1bf0
-  __DATA_CONST.__got: 0x1570
-  __DATA_CONST.__auth_ptr: 0x1670
-  __DATA.__objc_const: 0x1dde0
-  __DATA.__objc_selrefs: 0x1710
+  __DATA_CONST.__got: 0x1580
+  __DATA_CONST.__auth_ptr: 0x1678
+  __DATA.__objc_const: 0x1e0f0
+  __DATA.__objc_selrefs: 0x1720
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x3348
-  __DATA.__data: 0x142c0
+  __DATA.__objc_data: 0x3360
+  __DATA.__data: 0x14300
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0x13b80
+  __DATA.__bss: 0x13980
   __DATA.__common: 0x4b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10230
-  Symbols:   1814
-  CStrings:  4164
+  Functions: 10245
+  Symbols:   1815
+  CStrings:  4183
 
Symbols:
+ _$s12AppleAccount21DeviceListFetchResultV10versionTagSSSgvg
+ _$s12AppleAccount9SetupBaseC7context4base16btAddressMonitor0G13StateProvider5queueACyxGAA09BluetoothD13ConfigurationV_xSo13CBActivatable_So013CBAdvertisingH9ReportingpAA0mjK0CSo012OS_dispatch_L0Ctcfc
+ _$s8Dispatch0A3QoSV13userInitiatedACvgZ
+ _AKDeviceListChangedNotification
+ _NSLocalizedDescriptionKey
- _$s10Foundation6LocaleVMa
- _$s10Foundation6LocaleVMn
- _$s12AppleAccount9SetupBaseC7context4base16btAddressMonitor0G13StateProviderACyxGAA09BluetoothD13ConfigurationV_xSo13CBActivatable_So013CBAdvertisingH9ReportingpAA0ljK0Ctcfc
- _$sSy10FoundationE7compare_7options5range6localeSo18NSComparisonResultVqd___So22NSStringCompareOptionsVSnySS5IndexVGSgAA6LocaleVSgtSyRd__lF
CStrings:
+ " %s Skipping duplicate resolved handle: %s"
+ " Trusted Contacts Preflight"
+ "AppInstallObserver: Handling distributed notification. Event: %s"
+ "AppInstallObserver: Missing bundleIDs for state-change notification."
+ "AppInstallObserver: state change for %s"
+ "Cached %ld devices (serveEnabled: %{bool}d)"
+ "Caller-initiated force refresh, bypassing cache reads"
+ "Cloud sync failed before %s; deferring readiness checks: %s"
+ "Dataclass App Install Observer - State change for %s"
+ "Device list changed notification received: %s"
+ "Device list fetch ETag — prior: %{private,mask.hash}s, fresh: %{private,mask.hash}s"
+ "PCS keys upload completed successfully (retries: %{public}ld). Status code: %{public}ld"
+ "PCS keys upload failed with HTTP status %{public}ld."
+ "PCS keys upload returned HTTP 500 (server could not decrypt). Re-running flow with re-encrypted keys. Retries remaining: %{public}ld"
+ "PCS keys upload returned no response."
+ "PCS pre-encryption blob for services [%{public}s] (base64): %{private}s"
+ "accuracyRecorder"
+ "attachPdpStateAndHealth: pdpHealth unavailable (property nil, cache nil)"
+ "attachPdpStateAndHealth: pdpHealth=%@ attached"
+ "attachPdpStateAndHealth: pdpState=%lu source=%s"
+ "com.apple.LaunchServices.applicationStateChanged"
+ "com.apple.appleaccount.setupbase"
+ "com.apple.appleaccountd.identity.background-refresh"
+ "com.apple.appleaccountd.identity.background-upload"
+ "com.apple.authkit.device-list-category-changed"
+ "initWithUnsignedInteger:"
+ "isWalrusPreEncryptionBlobLoggingEnabled"
- "AppInstallObserver: Handling distributed notification."
- "Cached %ld devices with TTL %fs"
- "Caller-initiated force refresh, bypassing cache reads (writes %s)"
- "Device list changed notification received"
- "PCS keys upload completed successfully."
- "Rejecting outdated version: new='%{private,mask.hash}s' < current='%{private,mask.hash}s'"
- "Skipping cache write — kill switch engaged"
- "com.apple.authkit.trusted-device-list-changed"
```
