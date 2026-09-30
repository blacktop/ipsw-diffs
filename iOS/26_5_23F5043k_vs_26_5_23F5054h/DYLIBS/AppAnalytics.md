## AppAnalytics

> `/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics`

```diff

-531.0.0.0.0
-  __TEXT.__text: 0x1401b8
-  __TEXT.__auth_stubs: 0x27f0
+533.0.0.0.0
+  __TEXT.__text: 0x140aa4
+  __TEXT.__auth_stubs: 0x2830
   __TEXT.__objc_methlist: 0x1b24
-  __TEXT.__const: 0xc1e0
-  __TEXT.__constg_swiftt: 0x4f20
-  __TEXT.__swift5_typeref: 0x2d24
-  __TEXT.__swift5_reflstr: 0x2da7
-  __TEXT.__swift5_fieldmd: 0x3fc8
+  __TEXT.__const: 0xc300
+  __TEXT.__constg_swiftt: 0x4f60
+  __TEXT.__swift5_typeref: 0x2d40
+  __TEXT.__swift5_reflstr: 0x2df7
+  __TEXT.__swift5_fieldmd: 0x4024
   __TEXT.__swift5_builtin: 0x230
   __TEXT.__swift5_assocty: 0x4f8
-  __TEXT.__swift5_proto: 0x838
-  __TEXT.__swift5_types: 0x534
-  __TEXT.__swift5_capture: 0x2398
+  __TEXT.__swift5_proto: 0x848
+  __TEXT.__swift5_types: 0x53c
+  __TEXT.__swift5_capture: 0x23f4
   __TEXT.__cstring: 0x4d9c
-  __TEXT.__swift_as_entry: 0xbc
-  __TEXT.__swift_as_ret: 0xb0
+  __TEXT.__swift_as_entry: 0xc4
+  __TEXT.__swift_as_ret: 0xb8
   __TEXT.__swift5_protos: 0xb4
-  __TEXT.__oslogstring: 0x229f
+  __TEXT.__oslogstring: 0x250f
   __TEXT.__swift5_mpenum: 0xe0
-  __TEXT.__unwind_info: 0x44d8
-  __TEXT.__eh_frame: 0x5638
+  __TEXT.__unwind_info: 0x4520
+  __TEXT.__eh_frame: 0x5688
   __TEXT.__objc_classname: 0x10ec
-  __TEXT.__objc_methname: 0x42c5
+  __TEXT.__objc_methname: 0x42e5
   __TEXT.__objc_methtype: 0xff5
-  __TEXT.__objc_stubs: 0x1280
-  __DATA_CONST.__got: 0x748
+  __TEXT.__objc_stubs: 0x1240
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc48
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_protorefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x1400
-  __AUTH_CONST.__const: 0xafa0
-  __AUTH_CONST.__objc_const: 0x6a08
+  __AUTH_CONST.__auth_got: 0x1420
+  __AUTH_CONST.__const: 0xb100
+  __AUTH_CONST.__objc_const: 0x6a28
   __AUTH.__objc_data: 0x1418
   __AUTH.__data: 0x7e8
-  __DATA.__data: 0x1fe8
-  __DATA.__bss: 0xb800
+  __DATA.__data: 0x2008
+  __DATA.__bss: 0xba00
   __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_data: 0x19d8
-  __DATA_DIRTY.__data: 0x55a8
+  __DATA_DIRTY.__objc_data: 0x19e0
+  __DATA_DIRTY.__data: 0x5598
   __DATA_DIRTY.__bss: 0x2e00
   __DATA_DIRTY.__common: 0x160
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B7AE21B4-8AF0-3EB2-9DCD-335766F8AB3F
-  Functions: 6527
-  Symbols:   2653
-  CStrings:  1341
+  UUID: 318C7C83-6C82-3675-B1E7-CA89E35727F1
+  Functions: 6547
+  Symbols:   2655
+  CStrings:  1345
 
Symbols:
+ _associated conformance 12AppAnalytics15TrackingConsentC15DecisionResolveOSHAASQ
+ _associated conformance 12AppAnalytics15TrackingConsentC5State33_28267B4B036CAF985B11AC40B7DF8A35LLVSHAASQ
+ _objectdestroy.40Tm
+ _objectdestroy.45Tm
+ _objectdestroy.53Tm
+ _symbolic _____ 12AppAnalytics15TrackingConsentC15DecisionResolveO
+ _symbolic _____ 12AppAnalytics15TrackingConsentC5State33_28267B4B036CAF985B11AC40B7DF8A35LLV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 12AppAnalytics15TrackingConsentC5State33_28267B4B036CAF985B11AC40B7DF8A35LLV
+ _type_layout_string 12AppAnalytics15TrackingConsentC5State33_28267B4B036CAF985B11AC40B7DF8A35LLV
- _OBJC_CLASS_$_NSISO8601DateFormatter
- _objc_msgSend$setFormatOptions:
- _objc_msgSend$stringFromDate:
- _objectdestroy.34Tm
- _objectdestroy.52Tm
- _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 12AppAnalytics15TrackingConsentC0G10PermissionO
CStrings:
+ "TrackingConsent: Failed to decode consent decision from UserDefaults. Error: %s"
+ "TrackingConsent: Failed to encode consent decision: %s. Error: %s"
+ "TrackingConsent: Migrated permission: %s to decision: %s"
+ "TrackingConsent: Persisting consent decision: %s"
+ "TrackingConsent: Reconciliation triggered. Storing new decision: %s"
+ "TrackingConsent: Removed potentially stale value for key: %s due to decoding failure."
+ "TrackingConsent: Retrieved consent decision: %s, from UserDefaults, with key: %s"
+ "TrackingConsent: Stored consent decision: %s, to UserDefaults, with key: %s"
+ "TrackingConsent: Waiting for decision to be resolved"
+ "TrackingConsent: Will track user consent for tracking analytics; All analytics processing will be queued until user consent"
+ "TrackingConsent: has been allowed"
+ "TrackingConsent: has been allowed but decision was not reconciled yet, this is an unexpected state and will be ignored"
+ "TrackingConsent: has been denied"
+ "TrackingConsent: has been denied but decision was not reconciled yet, this is an unexpected state and will be ignored"
+ "TrackingConsent: has not been resolved yet"
+ "TrackingConsent: initialized with default value of: %s"
+ "TrackingConsent: popped"
+ "TrackingConsent: pushed"
+ "decisionReconciliationTask"
+ "stateLock"
- "Failed to decode consent decision from UserDefaults. Error: %s"
- "Failed to encode consent decision: %s. Error: %s"
- "Migrated permission: %s to decision: %s"
- "Persisting consent decision: %s"
- "Reconciliation triggered. Storing new decision: %s"
- "Retrieved consent decision: %s, from UserDefaults, with key: %s"
- "Stored consent decision: %s, to UserDefaults, with key: %s"
- "Tracking consent has been allowed"
- "Tracking consent has been denied"
- "Tracking consent initialized with resolved decision: %s"
- "Tracking consent popped"
- "Tracking consent pushed"
- "Will track user consent for tracking analytics; All analytics processing will be queued until user consent"
- "consented"
- "setFormatOptions:"
- "stringFromDate:"

```
