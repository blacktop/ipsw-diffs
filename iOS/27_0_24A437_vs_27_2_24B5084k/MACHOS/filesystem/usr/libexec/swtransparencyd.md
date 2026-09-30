## swtransparencyd

> `/usr/libexec/swtransparencyd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1766.0.60.0.0
-  __TEXT.__text: 0xf38a8
-  __TEXT.__auth_stubs: 0x27e0
+1766.40.47.0.0
+  __TEXT.__text: 0xf4c24
+  __TEXT.__auth_stubs: 0x2810
   __TEXT.__objc_stubs: 0x65c0
   __TEXT.__objc_methlist: 0x70b4
-  __TEXT.__const: 0x5ed0
-  __TEXT.__cstring: 0x4da9
-  __TEXT.__oslogstring: 0x36bd
+  __TEXT.__const: 0x5ef0
+  __TEXT.__cstring: 0x4ea9
+  __TEXT.__oslogstring: 0x37bd
   __TEXT.__objc_classname: 0x1a24
   __TEXT.__objc_methname: 0x780d
   __TEXT.__objc_methtype: 0x20a5

   __TEXT.__swift5_typeref: 0x141b
   __TEXT.__swift5_capture: 0x724
   __TEXT.__swift5_fieldmd: 0x1a64
-  __TEXT.__constg_swiftt: 0x1ad4
+  __TEXT.__constg_swiftt: 0x1ae4
   __TEXT.__swift5_reflstr: 0x1261
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x36c

   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_mpenum: 0x7c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x5a10
-  __TEXT.__eh_frame: 0x69f4
-  __DATA_CONST.__const: 0x5fc8
-  __DATA_CONST.__cfstring: 0x3060
+  __TEXT.__unwind_info: 0x5a68
+  __TEXT.__eh_frame: 0x6a6c
+  __DATA_CONST.__const: 0x6038
+  __DATA_CONST.__cfstring: 0x30c0
   __DATA_CONST.__objc_classlist: 0x648
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x2f8
-  __DATA_CONST.__auth_got: 0x1400
+  __DATA_CONST.__auth_got: 0x1418
   __DATA_CONST.__got: 0x698
-  __DATA_CONST.__auth_ptr: 0x508
+  __DATA_CONST.__auth_ptr: 0x510
   __DATA.__objc_const: 0xe860
   __DATA.__objc_selrefs: 0x2158
   __DATA.__objc_ivar: 0x468
   __DATA.__objc_data: 0x3d10
   __DATA.__data: 0x48c0
-  __DATA.__common: 0x2a8
+  __DATA.__common: 0x2b0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6031
-  Symbols:   957
-  CStrings:  2894
+  Functions: 6052
+  Symbols:   960
+  CStrings:  2901
 
Symbols:
+ _$s10Foundation4DateV17timeIntervalSinceySdACF
+ _$s12Transparency0A13SWSysdiagnoseV12StateMachineV5state5flags12pendingFlags12publicKeybag13containerPath12reachability18lastMilestoneFetchAESSSg_SaySSGSgAoC06PublicJ0VSgAmC12ReachabilityVSg10Foundation4DateVSgtcfC
+ _$s12Transparency0A13SWSysdiagnoseV25milestoneRefreshFreshnessSdvgZ
+ _ccvrf_proof_to_hash
+ _ccvrf_sizeof_hash
- _$s12Transparency0A13SWSysdiagnoseV12StateMachineV5state5flags12pendingFlags12publicKeybag13containerPath12reachabilityAESSSg_SaySSGSgAnC06PublicJ0VSgAlC12ReachabilityVSgtcfC
- _objc_retain_x6
CStrings:
+ "Failed to read most recent milestone receiptTime: %@"
+ "Milestone younger than refresh threshold, skipping milestone-refresh work"
+ "SELECT receiptTime\nFROM SignedLogHeads\nWHERE application=? AND logType=? AND consistencyVerified=? AND milestone=1\nORDER BY receiptTime DESC\nLIMIT 1"
+ "VRF witness output does not match proof_to_hash(proof)"
+ "VRF witness output not bound to proof"
+ "no directory to delete %@ from"
+ "no directory to write %@ to"
```
