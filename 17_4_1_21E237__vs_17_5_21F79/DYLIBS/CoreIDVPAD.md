## CoreIDVPAD

> `/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD`

```diff

-1.401.0.0.0
-  __TEXT.__text: 0x4c20c
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0xbf8
-  __TEXT.__const: 0x21b6
+1.402.0.0.0
+  __TEXT.__text: 0x4e248
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_methlist: 0xc18
+  __TEXT.__const: 0x21c6
   __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__cstring: 0x34fe
+  __TEXT.__cstring: 0x379e
   __TEXT.__oslogstring: 0x2a6
-  __TEXT.__constg_swiftt: 0x1a74
+  __TEXT.__constg_swiftt: 0x1a6c
   __TEXT.__swift5_typeref: 0xc46
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0xd26

   __TEXT.__swift5_proto: 0x174
   __TEXT.__swift5_types: 0x100
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_capture: 0x1f0
-  __TEXT.__unwind_info: 0x127c
-  __TEXT.__eh_frame: 0x11b8
+  __TEXT.__swift5_capture: 0x200
+  __TEXT.__unwind_info: 0x129c
+  __TEXT.__eh_frame: 0x11c0
   __TEXT.__objc_classname: 0x1db
-  __TEXT.__objc_methname: 0x2292
-  __TEXT.__objc_methtype: 0x940
-  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_methname: 0x22a8
+  __TEXT.__objc_methtype: 0x971
+  __TEXT.__objc_stubs: 0xe80
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3468
-  __DATA_CONST.__objc_selrefs: 0x8b0
+  __DATA_CONST.__objc_const: 0x3488
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__const: 0x1fe8
-  __AUTH_CONST.__auth_got: 0xb30
-  __AUTH.__objc_data: 0xde8
+  __AUTH_CONST.__const: 0x2010
+  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH.__objc_data: 0xde0
   __AUTH.__data: 0x1f68
   __DATA.__got_weak: 0x10
   __DATA.__objc_ivar: 0x120

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0000592F-3E6C-3CC7-91FB-8388BC1A8270
-  Functions: 1554
-  Symbols:   1793
-  CStrings:  981
+  UUID: 00B25CBD-1169-3CF1-A394-6C717A4B5147
+  Functions: 1568
+  Symbols:   1797
+  CStrings:  993
 
Symbols:
+ -[_PADClassifier finishLivenessStepUp:]
+ _objc_msgSend$finishLivenessStepUp:
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
CStrings:
+ ", processing options: "
+ "Attempted to finalize liveness results before FAC processing has completed"
+ "CIDVPAD.show-padframe-logging"
+ "Current Gesture Timestamps FAC: %s"
+ "FAC results are not complete, unable to finish processing without selfie."
+ "Invalid reference frame timestamp recieved: %s"
+ "PADInternalClassifier: Called `startLiveness` after classifier has loaded. Proceeding as expected."
+ "PADInternalClassifier: Called `startLiveness` before classifier has loaded. Deferring call until classfier is ready."
+ "PADInternalClassifier: Classifier loaded. Starting liveness from earlier call."
+ "Processing frame at timestamp "
+ "finishLivenessStepUp:"
+ "v24@0:8@?<v@?@\"PADClassifierResult\"@\"NSError\">16"

```
