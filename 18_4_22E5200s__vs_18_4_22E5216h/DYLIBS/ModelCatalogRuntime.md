## ModelCatalogRuntime

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`

```diff

-162.744.10.3.0
-  __TEXT.__text: 0x532f8
-  __TEXT.__auth_stubs: 0x1f20
+162.749.4.0.0
+  __TEXT.__text: 0x5b7c0
+  __TEXT.__auth_stubs: 0x1f40
   __TEXT.__objc_methlist: 0x4c8
-  __TEXT.__const: 0x1378
-  __TEXT.__swift5_typeref: 0x11bf
-  __TEXT.__swift5_fieldmd: 0x6e8
-  __TEXT.__constg_swiftt: 0xbec
+  __TEXT.__const: 0x1408
+  __TEXT.__swift5_typeref: 0x11fd
+  __TEXT.__swift5_fieldmd: 0x714
+  __TEXT.__constg_swiftt: 0xc28
   __TEXT.__cstring: 0x1823
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x630
+  __TEXT.__swift5_reflstr: 0x640
   __TEXT.__swift5_assocty: 0x118
-  __TEXT.__oslogstring: 0x2b3a
-  __TEXT.__swift5_protos: 0x30
-  __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_capture: 0x538
+  __TEXT.__oslogstring: 0x2e3a
+  __TEXT.__swift5_protos: 0x34
+  __TEXT.__swift5_proto: 0xa0
+  __TEXT.__swift5_types: 0xa0
+  __TEXT.__swift5_capture: 0x548
   __TEXT.__swift_as_entry: 0xfc
-  __TEXT.__swift_as_ret: 0x118
-  __TEXT.__unwind_info: 0x1368
-  __TEXT.__eh_frame: 0x3138
+  __TEXT.__swift_as_ret: 0x11c
+  __TEXT.__unwind_info: 0x1430
+  __TEXT.__eh_frame: 0x3684
   __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methname: 0x959
+  __TEXT.__objc_methname: 0x971
   __TEXT.__objc_methtype: 0x127
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x330
+  __DATA_CONST.__objc_selrefs: 0x338
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0xf90
-  __AUTH_CONST.__auth_ptr: 0x850
-  __AUTH_CONST.__const: 0x1678
+  __AUTH_CONST.__auth_got: 0xfa0
+  __AUTH_CONST.__auth_ptr: 0x7e0
+  __AUTH_CONST.__const: 0x16d0
   __AUTH_CONST.__objc_const: 0xf30
   __AUTH.__objc_data: 0x328
   __AUTH.__data: 0x878
   __DATA.__data: 0xaa0
   __DATA.__bss: 0xd10
-  __DATA.__common: 0x1a0
+  __DATA.__common: 0x1c8
   __DATA_DIRTY.__objc_data: 0xf8
   __DATA_DIRTY.__data: 0x6d0
   __DATA_DIRTY.__common: 0x98

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1790
-  Symbols:   210
-  CStrings:  448
+  Functions: 1896
+  Symbols:   211
+  CStrings:  455
 
Symbols:
+ _objc_retain_x9
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initStructMetadataWithLayoutString
CStrings:
+ " + %{public}s"
+ " - %{public}s"
+ " - SubscriptionEvaluator omitting subscription for decision: %{public}s %{public}s, argument values map to previously returned subscription"
+ " - SubscriptionEvaluator omitting subscription for decision: %{public}s %{public}s, did not find usage alias subscription with corresponding argument values"
+ " - SubscriptionEvaluator received row with parameters: %{public}s"
+ " - SubscriptionEvaluator received row with parameters: %{public}s, expirationDate: %f"
+ "Decision for use case: %{public}s parameters: %{public}s"
+ "Decision for use case: %{public}s parameters: %{public}s expirationDate: %{public}f"
+ "SubscriptionEvaluationManager done processing %{public}ld decisions"
+ "SubscriptionEvaluationManager failed to evaluate subscriptions: %{public}@"
+ "SubscriptionEvaluationManager failed to write subscriptions: %{public}@"
+ "SubscriptionEvaluationManager made: %{public}ld subscription decisions"
+ "SubscriptionEvaluationManager received new trigger event: %{public}s"
+ "SubscriptionEvaluationManager recovered %{public}ld decisions"
+ "SubscriptionEvaluationManager running evaluate task with: %{public}ld use cases"
+ "SubscriptionEvaluator evaluating download condition for use case: %{public}s"
+ "SubscriptionEvaluator found no download condition for use case: %{public}s"
+ "SubscriptionEvaluator received error: %{public}@ while evaluating download condition: %s"
+ "SubscriptionEvaluator received invalid parameter name: %{public}s"
+ "SubscriptionEvaluator received row result: %{public}s"
+ "SubscriptionWriter NOT notifying Catalog.notifyGenerativeExperiencesReady"
+ "SubscriptionWriter could not determine subscription names for request resource key: %{public}s with error: %{public}@"
+ "SubscriptionWriter could not usage alias subscription for use case %{public}s with argument keys %{public}s and values %{public}s: %@"
+ "SubscriptionWriter determined %{public}ld subscriptions that should be subscribed:"
+ "SubscriptionWriter determined %{public}ld subscriptions to remove:"
+ "SubscriptionWriter found %{public}ld current subscriptions:"
+ "SubscriptionWriter notifying Catalog.notifyGenerativeExperiencesReady"
+ "SubscriptionWriter received asset manager error when subscribing: %{public}@"
+ "SubscriptionWriter received asset manager error when unsubscribing: %{public}@"
+ "SubscriptionWriter successfully subscribed to %{public}ld subscriptions"
+ "SubscriptionWriter successfully unsubscribed from %{public}ld subscriptions"
+ "UseCase: %{public}s"
+ "availableUseCases: Use case identifier %s, with arguments: %s is ready (no matching required variants)."
+ "getConsistencyToken: found new token: %s for %s, updating store"
+ "invalidateAssetSet associated pids: %s"
+ "invalidateAssetSet failed to collect pid information after failure"
+ "processIdsLockingToken:"
- " + %s"
- " - SubscriptionEvaluator omitting subscription for decision: %s %s, argument values map to previously returned subscription"
- " - SubscriptionEvaluator omitting subscription for decision: %s %s, did not find usage alias subscription with corresponding argument values"
- " - SubscriptionEvaluator received row with parameters: %s"
- " - SubscriptionEvaluator received row with parameters: %s, expirationDate: %f"
- "Decision for use case: %s parameters: %s"
- "Decision for use case: %s parameters: %s expirationDate: %f"
- "SubscriptionEvaluationManager done processing %ld decisions"
- "SubscriptionEvaluationManager failed to evaluate subscriptions: %@"
- "SubscriptionEvaluationManager failed to write subscriptions: %@"
- "SubscriptionEvaluationManager made: %ld subscription decisions"
- "SubscriptionEvaluationManager received new trigger event: %s"
- "SubscriptionEvaluationManager recovered %ld decisions"
- "SubscriptionEvaluationManager running evaluate task with: %ld use cases"
- "SubscriptionEvaluator evaluating download condition for use case: %s"
- "SubscriptionEvaluator found no download condition for use case: %s"
- "SubscriptionEvaluator received error: %@ while evaluating download condition: %s"
- "SubscriptionEvaluator received invalid parameter name: %s"
- "SubscriptionEvaluator received row result: %s"
- "SubscriptionWriter could not determine subscription name for request resources key: %s with error: %@"
- "SubscriptionWriter could not usage alias subscription for use case %s with argument keys %s and values %s: %@"
- "SubscriptionWriter determined %ld subscriptions that should be subscribed:"
- "SubscriptionWriter determined %ld subscriptions to remove:"
- "SubscriptionWriter found %ld current subscriptions:"
- "SubscriptionWriter received asset manager error when subscribing: %@"
- "SubscriptionWriter received asset manager error when unsubscribing: %@"
- "SubscriptionWriter successfully subscribed to %ld subscriptions"
- "SubscriptionWriter successfully unsubscribed from %ld subscriptions"
- "UseCase: %s"
- "getConsistencyToken: found new token: %s for %s"

```
