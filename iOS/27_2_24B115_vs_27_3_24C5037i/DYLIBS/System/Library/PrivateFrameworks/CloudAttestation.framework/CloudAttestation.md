## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-323.40.16.0.0
-  __TEXT.__text: 0x143040
+323.60.13.0.0
+  __TEXT.__text: 0x14f164
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x1f4f0
-  __TEXT.__constg_swiftt: 0x3114
-  __TEXT.__swift5_typeref: 0x2e9a
-  __TEXT.__swift5_proto: 0xd8c
-  __TEXT.__swift5_types: 0x478
-  __TEXT.__swift5_fieldmd: 0x3e68
-  __TEXT.__swift5_reflstr: 0x33a3
-  __TEXT.__oslogstring: 0x35d8
-  __TEXT.__cstring: 0x2864
-  __TEXT.__swift_as_entry: 0x378
-  __TEXT.__swift_as_ret: 0x338
-  __TEXT.__swift_as_cont: 0x4e8
-  __TEXT.__swift5_capture: 0x27c
+  __TEXT.__const: 0x1f880
+  __TEXT.__constg_swiftt: 0x31a4
+  __TEXT.__swift5_typeref: 0x2f3e
+  __TEXT.__swift5_proto: 0xdc0
+  __TEXT.__swift5_types: 0x488
+  __TEXT.__swift5_fieldmd: 0x3f38
+  __TEXT.__swift5_reflstr: 0x33d3
+  __TEXT.__oslogstring: 0x3918
+  __TEXT.__cstring: 0x28b4
+  __TEXT.__swift_as_entry: 0x388
+  __TEXT.__swift_as_ret: 0x34c
+  __TEXT.__swift_as_cont: 0x510
+  __TEXT.__swift5_capture: 0x294
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_assocty: 0x6b0
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__unwind_info: 0x69c8
-  __TEXT.__eh_frame: 0xb010
+  __TEXT.__unwind_info: 0x6c50
+  __TEXT.__eh_frame: 0xb7a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x8340
+  __AUTH_CONST.__const: 0x8478
   __AUTH_CONST.__objc_const: 0x838
-  __AUTH_CONST.__auth_got: 0x13c0
-  __AUTH.__data: 0x3a0
-  __DATA.__data: 0x2cb8
+  __AUTH_CONST.__auth_got: 0x13d8
+  __AUTH.__data: 0x4a8
+  __DATA.__data: 0x2da8
   __DATA.__common: 0x2a0
   __DATA_DIRTY.__objc_data: 0x200
   __DATA_DIRTY.__data: 0x49d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7716
-  Symbols:   2492
-  CStrings:  427
+  Functions: 7853
+  Symbols:   2512
+  CStrings:  437
 
Symbols:
+ ___swift_closure_destructor.24Tm
+ ___swift_closure_destructorTm
+ _associated conformance 16CloudAttestation16TransparencyLeafVSHAASQ
+ _associated conformance 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV10CodingKeysOSHAASQ
+ _associated conformance 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV10CodingKeysOs0M3KeyAAs23CustomStringConvertible
+ _associated conformance 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV10CodingKeysOs0M3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 16CloudAttestation7ReleaseV11CoprocessorV17SwiftASN1Internal21DERImplicitlyTaggableAaF12DERParseable
+ _associated conformance 16CloudAttestation7ReleaseV11CoprocessorV17SwiftASN1Internal21DERImplicitlyTaggableAaF15DERSerializable
+ _associated conformance 16CloudAttestation7ReleaseV11CoprocessorVSHAASQ
+ _symbolic Say_____G 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV
+ _symbolic Say_____G 16CloudAttestation7ReleaseV11CoprocessorV
+ _symbolic Say_____GSg 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV
+ _symbolic Shy_____G 16CloudAttestation7ReleaseV11CoprocessorV
+ _symbolic _____ 16CloudAttestation16TransparencyLeafV
+ _symbolic _____ 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV
+ _symbolic _____ 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV10CodingKeysO
+ _symbolic _____ 16CloudAttestation7ReleaseV11CoprocessorV
+ _symbolic _____y_____G s11_SetStorageC 16CloudAttestation7ReleaseV11CoprocessorV
+ _symbolic _____y_____G s22KeyedEncodingContainerV 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV10CodingKeysO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV
+ _type_layout_string 16CloudAttestation20EncodableCoprocessor33_3DB6F6642BC10C52065B0F3D59117C75LLV
- ___swift_closure_destructor.20Tm
CStrings:
+ "Chaining compute node to proxy via milestone (computeNodeRevision=%{public}s, milestone=%{public}s, proxyNodeRevision=%{public}s)"
+ "Compute node is anchored at the proxy milestone, no consistency proof required (milestone=%{public}s)"
+ "Compute node tree head does not match the proxy milestone despite matching revisions (milestone=%{public}s)"
+ "Empty coprocessors must be omitted"
+ "Not caching a consistency proof that fails merkle verification (from=%{public}s, to=%{public}s)"
+ "Not caching an inclusion proof that fails merkle verification (revision=%{public}s)"
+ "Proxy milestone consistency proof does not terminate at the proxy inclusion proof tree head (milestone=%{public}s)"
+ "Proxy milestone consistency proof is invalid"
+ "Proxy milestone predates compute node revision (computeNodeRevision=%{public}s, proxyMilestoneRevision=%{public}s)"
+ "Tree heads in consistency proof do not match expected tree heads (expectedStart=%{public}s, consistencyProofStart=%{public}s, consistencyProofEnd=%{public}s, expectedEnd=%{public}s)"
+ "trustCacheTickets"
- "Tree heads in consistency proof do not match inclusion proof tree heads (computeNodeInclusionProof=%{public}s, consistencyProofStart=%{public}s, consistencyProofEnd=%{public}s, proxyNodeInclusionProof=%{public}s)"
```
