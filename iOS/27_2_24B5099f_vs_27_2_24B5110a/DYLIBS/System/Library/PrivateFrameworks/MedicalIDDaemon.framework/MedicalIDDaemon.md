## MedicalIDDaemon

> `/System/Library/PrivateFrameworks/MedicalIDDaemon.framework/MedicalIDDaemon`

```diff

-7027.1.54.2.3
-  __TEXT.__text: 0x949c
+7027.1.56.2.9
+  __TEXT.__text: 0xc17c
   __TEXT.__objc_methlist: 0x304
-  __TEXT.__const: 0x6d8
-  __TEXT.__swift5_typeref: 0x2a4
+  __TEXT.__const: 0x6e8
+  __TEXT.__swift5_typeref: 0x29e
   __TEXT.__swift5_fieldmd: 0x198
   __TEXT.__constg_swiftt: 0x270
-  __TEXT.__oslogstring: 0x5cd
-  __TEXT.__swift5_reflstr: 0x131
+  __TEXT.__oslogstring: 0x7dd
   __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x131
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x28
-  __TEXT.__cstring: 0x201
-  __TEXT.__swift5_capture: 0x4c
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__cstring: 0x221
+  __TEXT.__swift5_capture: 0x110
+  __TEXT.__unwind_info: 0x388
+  __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x280
+  __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x219
+  __AUTH_CONST.__const: 0x499
   __AUTH_CONST.__objc_const: 0x548
-  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH.__objc_data: 0x2c0
   __AUTH.__data: 0x110
-  __DATA.__data: 0x588
+  __DATA.__data: 0x5a8
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x98
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 187
-  Symbols:   315
-  CStrings:  36
+  Functions: 237
+  Symbols:   322
+  CStrings:  44
 
Symbols:
+ _CNErrorDomain
+ _associated conformance SC11CNErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
+ _associated conformance SC11CNErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC11CNErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_AC06_ErrorB8Protocol
+ _associated conformance SC11CNErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_SY
+ _associated conformance SC11CNErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomF0
+ _associated conformance SC11CNErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
+ _associated conformance SC11CNErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC11CNErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0F0
+ _associated conformance SC11CNErrorCodeLeVSHSCSQ
+ _associated conformance So11CNErrorCodeV10Foundation06_ErrorB8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So11CNErrorCodeV10Foundation06_ErrorB8ProtocolSCSQ
+ _kHKMedicalIDFollowUpExtensionIdentifier
+ _kHKMedicalIDFollowUpReviewCompletedDateKey
+ _objc_retain_x28
+ _swift_deallocClassInstance
+ _swift_getEnumCaseMultiPayload
+ _swift_release_x22
+ _swift_release_x23
+ _swift_storeEnumTagMultiPayload
+ _symbolic _____ SC11CNErrorCodeLeV
+ _symbolic _____ So11CNErrorCodeV
+ _type_layout_string SC11CNErrorCodeLeV
- _HKErrorDomain
- _associated conformance SC11HKErrorCodeLeV10Foundation13CustomNSErrorSCs5Error
- _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_8RawValueSYs17FixedWidthInteger
- _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_AC06_ErrorB8Protocol
- _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0B0AcDP_SY
- _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomF0
- _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC26_ObjectiveCBridgeableError
- _associated conformance SC11HKErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
- _associated conformance SC11HKErrorCodeLeV10Foundation26_ObjectiveCBridgeableErrorSCs0F0
- _associated conformance SC11HKErrorCodeLeVSHSCSQ
- _associated conformance So11HKErrorCodeV10Foundation06_ErrorB8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
- _associated conformance So11HKErrorCodeV10Foundation06_ErrorB8ProtocolSCSQ
- _symbolic _____ 10Foundation4DateV
- _symbolic _____ SC11HKErrorCodeLeV
- _symbolic _____ So11HKErrorCodeV
- _type_layout_string SC11HKErrorCodeLeV
CStrings:
+ "%s Cleared retired follow-up item success=%{bool,public}d error=%{public}s"
+ "%s Emergency contact no longer exists; not counting it: %{public}@"
+ "%s Failed persisting processed date: %{public}@"
+ "%s Failed reading a follow-up marker; state unknown: %{public}@"
+ "%s Failed reading pending follow-up items; not posting: %{public}@"
+ "%s Failed reading pending follow-up items; retrying next launch: %{public}@"
+ "%s Failed to fetch Medical ID; skipping until the next launch: %{public}@"
+ "%s Failed to read emergency contacts; skipping until the next launch: %{public}@"
+ "%s Follow-up already handled for this profile; checking for a retired item."
+ "%s Follow-up state unknown; skipping until the next launch."
+ "%s Marked follow-up as processed"
+ "%s No FLFollowUpController; cannot check for a retired item."
+ "%s No FLFollowUpController; cannot replace the retired item."
+ "%s Profile not eligible for review follow-up item, marking as processed."
+ "%s Review follow-up item is already pending; not reposting."
+ "[%{public}s] Creating Medical ID profile extension"
+ "reviewFollowUpProcessedDate"
- "%s Failed persisting submit date: %{public}@"
- "%s Failed reading submit date; assuming already submitted: %{public}@"
- "%s Failed to fetch Medical ID; treating as not set up: %{public}@"
- "%s Failed to fetch contact for phone-number count: %{public}@"
- "%s Follow-up item has already been submitted"
- "%s Marked follow-up item as submitted"
- "%s Medical ID unavailable (protected data inaccessible); will retry: %{public}@"
- "%s Profile not eligible for review follow-up item."
- "%s Submit date unavailable (protected data inaccessible); will retry: %{public}@"
```
