## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-1064.0.0.0.0
-  __TEXT.__text: 0x3e0984
-  __TEXT.__auth_stubs: 0x3360
-  __TEXT.__objc_stubs: 0x4ac0
+1067.0.0.0.0
+  __TEXT.__text: 0x3e40c8
+  __TEXT.__auth_stubs: 0x3370
+  __TEXT.__objc_stubs: 0x4b00
   __TEXT.__objc_methlist: 0xee8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x11e40
-  __TEXT.__constg_swiftt: 0xbc44
-  __TEXT.__swift5_typeref: 0x72a1
+  __TEXT.__const: 0x11e30
+  __TEXT.__constg_swiftt: 0xbc70
+  __TEXT.__swift5_typeref: 0x72ed
   __TEXT.__swift5_builtin: 0x280
-  __TEXT.__swift5_reflstr: 0x61f5
-  __TEXT.__swift5_fieldmd: 0x60d4
+  __TEXT.__swift5_reflstr: 0x6205
+  __TEXT.__swift5_fieldmd: 0x60f0
   __TEXT.__swift5_assocty: 0x870
   __TEXT.__swift5_proto: 0xb94
   __TEXT.__swift5_types: 0x5d4
   __TEXT.__objc_classname: 0x2b3d
-  __TEXT.__objc_methname: 0x71e5
+  __TEXT.__objc_methname: 0x7225
   __TEXT.__objc_methtype: 0x1f04
-  __TEXT.__swift5_capture: 0x6370
-  __TEXT.__swift5_protos: 0x1fc
-  __TEXT.__oslogstring: 0x1fa0d
-  __TEXT.__cstring: 0x42d9
+  __TEXT.__swift5_capture: 0x6430
+  __TEXT.__swift5_protos: 0x200
+  __TEXT.__oslogstring: 0x1fcad
+  __TEXT.__cstring: 0x43a9
   __TEXT.__swift5_acfuncs: 0xa0
   __TEXT.__swift_as_entry: 0x5c8
   __TEXT.__swift_as_ret: 0x7a0
   __TEXT.__swift_as_cont: 0x102c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7ed0
-  __TEXT.__eh_frame: 0x1291c
-  __DATA_CONST.__const: 0x13650
+  __TEXT.__unwind_info: 0x7f10
+  __TEXT.__eh_frame: 0x1294c
+  __DATA_CONST.__const: 0x137e8
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__auth_got: 0x19b8
-  __DATA_CONST.__got: 0x1480
-  __DATA_CONST.__auth_ptr: 0x1560
-  __DATA.__objc_const: 0x1cd00
-  __DATA.__objc_selrefs: 0x1660
+  __DATA_CONST.__auth_got: 0x19c0
+  __DATA_CONST.__got: 0x1488
+  __DATA_CONST.__auth_ptr: 0x1568
+  __DATA.__objc_const: 0x1cff0
+  __DATA.__objc_selrefs: 0x1670
   __DATA.__objc_data: 0x2ff8
-  __DATA.__data: 0x13140
+  __DATA.__data: 0x13150
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0x12480
+  __DATA.__bss: 0x12400
   __DATA.__common: 0x498
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9783
-  Symbols:   1707
-  CStrings:  4025
+  Functions: 9805
+  Symbols:   1709
+  CStrings:  4040
 
Symbols:
+ _$s12AppleAccount9SetupBaseC7context4base16btAddressMonitor0G13StateProvider5queueACyxGAA09BluetoothD13ConfigurationV_xSo13CBActivatable_So013CBAdvertisingH9ReportingpAA0mjK0CSo012OS_dispatch_L0Ctcfc
+ _$s8Dispatch0A3QoSV13userInitiatedACvgZ
+ _NSLocalizedDescriptionKey
- _$s12AppleAccount9SetupBaseC7context4base16btAddressMonitor0G13StateProviderACyxGAA09BluetoothD13ConfigurationV_xSo13CBActivatable_So013CBAdvertisingH9ReportingpAA0ljK0Ctcfc
CStrings:
+ " %s Skipping duplicate resolved handle: %s"
+ " Trusted Contacts Preflight"
+ "Cloud sync failed before %s; deferring readiness checks: %s"
+ "PCS keys upload completed successfully (retries: %{public}ld). Status code: %{public}ld"
+ "PCS keys upload failed with HTTP status %{public}ld."
+ "PCS keys upload returned HTTP 500 (server could not decrypt). Re-running flow with re-encrypted keys. Retries remaining: %{public}ld"
+ "PCS keys upload returned no response."
+ "PCS pre-encryption blob for services [%{public}s] (base64): %{private}s"
+ "attachPdpStateAndHealth: pdpHealth unavailable (property nil, cache nil)"
+ "attachPdpStateAndHealth: pdpHealth=%@ attached"
+ "attachPdpStateAndHealth: pdpState=%lu source=%s"
+ "com.apple.appleaccount.setupbase"
+ "com.apple.appleaccountd.identity.background-refresh"
+ "com.apple.appleaccountd.identity.background-upload"
+ "initWithUnsignedInteger:"
+ "isWalrusPreEncryptionBlobLoggingEnabled"
- "PCS keys upload completed successfully."
```
