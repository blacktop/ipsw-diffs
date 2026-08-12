## CloudSubscriptionFeatures

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`

```diff

-301.24.0.26.1
-  __TEXT.__text: 0x112fec
+301.24.0.29.0
+  __TEXT.__text: 0x114c0c
   __TEXT.__objc_methlist: 0xe6c
-  __TEXT.__const: 0xb764
-  __TEXT.__cstring: 0x4711
-  __TEXT.__oslogstring: 0x737d
+  __TEXT.__const: 0xb874
+  __TEXT.__cstring: 0x4751
+  __TEXT.__oslogstring: 0x749d
   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__dlopen_cstrs: 0xc4
-  __TEXT.__constg_swiftt: 0x2bbc
-  __TEXT.__swift5_typeref: 0x2a8c
+  __TEXT.__constg_swiftt: 0x2bf4
+  __TEXT.__swift5_typeref: 0x2ab4
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x25d1
-  __TEXT.__swift5_fieldmd: 0x2e10
+  __TEXT.__swift5_reflstr: 0x2641
+  __TEXT.__swift5_fieldmd: 0x2e6c
   __TEXT.__swift5_assocty: 0x4d0
-  __TEXT.__swift5_proto: 0x864
-  __TEXT.__swift5_types: 0x35c
-  __TEXT.__swift5_capture: 0x169c
+  __TEXT.__swift5_proto: 0x870
+  __TEXT.__swift5_types: 0x364
+  __TEXT.__swift5_capture: 0x16bc
   __TEXT.__swift5_protos: 0x9c
   __TEXT.__swift_as_entry: 0x390
   __TEXT.__swift_as_ret: 0x3b0
-  __TEXT.__swift_as_cont: 0x87c
+  __TEXT.__swift_as_cont: 0x878
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__unwind_info: 0x4170
-  __TEXT.__eh_frame: 0xace0
+  __TEXT.__eh_frame: 0xaca8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x938
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x550
-  __AUTH_CONST.__const: 0x9270
+  __DATA_CONST.__got: 0x570
+  __AUTH_CONST.__const: 0x93f0
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x3588
-  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__objc_const: 0x35a8
+  __AUTH_CONST.__auth_got: 0x1118
   __AUTH.__objc_data: 0x3f0
   __AUTH.__data: 0x7c0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x1790
-  __DATA.__bss: 0xc540
+  __DATA.__bss: 0xc640
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xf10
+  __DATA_DIRTY.__objc_data: 0xf18
   __DATA_DIRTY.__data: 0x1f90
   __DATA_DIRTY.__bss: 0x2be0
   __DATA_DIRTY.__common: 0x48

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4876
-  Symbols:   2035
-  CStrings:  955
+  Functions: 4899
+  Symbols:   2042
+  CStrings:  957
 
Symbols:
+ ___swift_closure_destructor.104Tm
+ ___swift_closure_destructor.173Tm
+ ___swift_closure_destructor.77Tm
+ ___swift_memcpy144_8
+ _associated conformance 25CloudSubscriptionFeatures20WaitlistDequeueEventV9FeatureIDOSHAASQ
+ _symbolic _____ 25CloudSubscriptionFeatures20WaitlistDequeueEventV
+ _symbolic _____ 25CloudSubscriptionFeatures20WaitlistDequeueEventV9FeatureIDO
+ _symbolic _____Sgyc 10Foundation4DateV
+ _symbolic _____yKc 25CloudSubscriptionFeatures40SignupForWaitlistRequestFinishDiagnosticV
+ _type_layout_string 25CloudSubscriptionFeatures20WaitlistDequeueEventV
- ___swift_closure_destructor.100Tm
- ___swift_closure_destructor.169Tm
- ___swift_closure_destructor.74Tm
CStrings:
+ "%{public}s hadAllAccess: %{bool}d, hasAllAccess: %{bool}d, shouldUnregister: %{bool}d"
+ "%{public}s: There is an account, skipping unregistration"
+ "%{public}s: We do not have access to all waitlist features, skipping unregistration.\n Old features: %s,\n new features: %s"
+ "%{public}s: We transitioned to having access for all waitlist features, proceeding with unregistration."
+ "Unable to get diagnostic for signup for waitlist finish events: %@"
+ "[%{public}s] Gained access to Enhanced Siri and had a ticket with date: %{public}s, took TimeInterval %{public}f to complete."
+ "[%{public}s] Gained access to Enhanced Siri but did not have a ticket with date."
+ "[%{public}s] Network fetch finished for all features"
+ "com.apple.CloudSubscriptionFeatures.waitlist.dequeue"
- "%s: There is an account, skipping unregistration"
- "%s: We did not transition to having access, skipping unregistration.\n Old features: %s,\n new features: %s"
- "%s: We transitioned to having access for adm"
- "%s: We transitioned to having access for afm"
- "%s: We transitioned to having access, proceeding with unregistration."
- "[%{public}s] CFU code deprecated, skipping CFU checks"
- "[%{public}s]network fetch finished for all features"
```
