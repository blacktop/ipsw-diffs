## coreidvd

> `/usr/libexec/coreidvd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-9.104.0.0.0
-  __TEXT.__text: 0x6b22f4
-  __TEXT.__auth_stubs: 0xd450
+9.107.1.0.0
+  __TEXT.__text: 0x6b46ac
+  __TEXT.__auth_stubs: 0xd460
   __TEXT.__objc_stubs: 0x70e0
   __TEXT.__objc_methlist: 0x213c
-  __TEXT.__const: 0x32d70
-  __TEXT.__cstring: 0x29b6a
+  __TEXT.__const: 0x32dc0
+  __TEXT.__cstring: 0x29b8a
   __TEXT.__objc_classname: 0x371a
-  __TEXT.__objc_methname: 0xdc76
+  __TEXT.__objc_methname: 0xdca6
   __TEXT.__objc_methtype: 0x4a7e
-  __TEXT.__swift5_typeref: 0xc225
-  __TEXT.__swift5_fieldmd: 0xe6c0
-  __TEXT.__constg_swiftt: 0xdba8
+  __TEXT.__swift5_typeref: 0xc243
+  __TEXT.__swift5_fieldmd: 0xe6cc
+  __TEXT.__constg_swiftt: 0xdbc0
   __TEXT.__swift5_builtin: 0x2e4
-  __TEXT.__swift5_reflstr: 0xc1cd
+  __TEXT.__swift5_reflstr: 0xc1fd
   __TEXT.__swift5_assocty: 0xc58
   __TEXT.__swift5_protos: 0x1e0
   __TEXT.__swift5_proto: 0x1e50
   __TEXT.__swift5_types: 0xc44
-  __TEXT.__oslogstring: 0x2ef69
-  __TEXT.__swift5_capture: 0x64cc
+  __TEXT.__oslogstring: 0x2f009
+  __TEXT.__swift5_capture: 0x64dc
   __TEXT.__swift5_mpenum: 0x98
-  __TEXT.__swift_as_entry: 0x1324
-  __TEXT.__swift_as_ret: 0x1c50
-  __TEXT.__swift_as_cont: 0x3830
+  __TEXT.__swift_as_entry: 0x1330
+  __TEXT.__swift_as_ret: 0x1c60
+  __TEXT.__swift_as_cont: 0x383c
   __TEXT.__swift5_acfuncs: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x19208
-  __TEXT.__eh_frame: 0x480f0
-  __DATA_CONST.__const: 0x25560
+  __TEXT.__unwind_info: 0x18dc8
+  __TEXT.__eh_frame: 0x48258
+  __DATA_CONST.__const: 0x255c0
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_protolist: 0x230

   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__linkguard: 0xe
-  __DATA_CONST.__auth_got: 0x6a38
-  __DATA_CONST.__got: 0x4320
+  __DATA_CONST.__auth_got: 0x6a40
+  __DATA_CONST.__got: 0x4318
   __DATA_CONST.__auth_ptr: 0x2438
-  __DATA.__objc_const: 0x11888
+  __DATA.__objc_const: 0x118a8
   __DATA.__objc_selrefs: 0x25c0
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x37d0
-  __DATA.__data: 0x18540
+  __DATA.__data: 0x18560
   __DATA.__common: 0x730
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18960
-  Symbols:   6001
-  CStrings:  8512
+  Functions: 18976
+  Symbols:   6003
+  CStrings:  8519
 
Symbols:
+ _$s11Distributed0A23TargetInvocationDecoderP18decodeNextArgumentqd__yKlFTj
+ _$s7CoreIDV21MobileDocumentElementV6weightACvgZ
+ _$sScTss5NeverORszABRs_rlE17checkCancellationyyKFZ
+ _ODIServiceProviderIdIDVMigrate
- _$s7Network30NWActorSystemInvocationDecoderV18decodeNextArgumentxyKSeRzSERzlF
- _swift_conformsToProtocol2
CStrings:
+ "%s finished ODI"
+ "%s kicking off ODI"
+ "%s reusing ODI assessment"
+ "%s skipping ODI assessment"
+ "Non fatal - failed to fetch ODI assessment with error: %@"
+ "Parsed KRL document type mismatch."
+ "ProducedAssetManager warmup ODI for %s - %s or %s - isDeviceMigration: %{bool}d"
+ "application/identifierlist+cwt"
+ "fetchODIAssessment()"
+ "isDeviceMigration"
+ "odiAssessmentTask"
- "Finished ODI"
- "Kicking off ODI"
- "ProducedAssetManager warmup ODI for %s - %s or %s"
- "documentWarmup(configuration:documents:region:proofingSessionID:)"
```
