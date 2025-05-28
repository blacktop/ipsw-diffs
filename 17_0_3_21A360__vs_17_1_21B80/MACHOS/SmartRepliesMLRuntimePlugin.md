## SmartRepliesMLRuntimePlugin

> `/System/Library/PrivateFrameworks/SmartReplies.framework/PlugIns/SmartRepliesMLRuntimePlugin.appex/SmartRepliesMLRuntimePlugin`

```diff

-41.0.0.0.0
-  __TEXT.__text: 0x8a2c
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0x500
-  __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x386
-  __TEXT.__cstring: 0xa73
-  __TEXT.__oslogstring: 0x43e
-  __TEXT.__objc_classname: 0x34
-  __TEXT.__objc_methname: 0x6d5
-  __TEXT.__objc_methtype: 0x18b
+42.3.0.0.0
+  __TEXT.__text: 0x914c
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__const: 0x396
+  __TEXT.__cstring: 0xb83
+  __TEXT.__objc_methname: 0x7cf
+  __TEXT.__oslogstring: 0x4b1
+  __TEXT.__objc_classname: 0x44
+  __TEXT.__objc_methtype: 0x1da
   __TEXT.__constg_swiftt: 0x218
   __TEXT.__swift5_typeref: 0x204
   __TEXT.__swift5_fieldmd: 0xe4

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x23c
+  __TEXT.__unwind_info: 0x260
   __TEXT.__eh_frame: 0x1d8
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__cfstring: 0x400
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x6b0
-  __DATA.__objc_selrefs: 0x208
+  __DATA.__objc_const: 0x788
+  __DATA.__objc_selrefs: 0x238
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x250
+  __DATA.__objc_classrefs: 0xd8
+  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0x2a0
   __DATA.__data: 0x3be0
   __DATA.__common: 0x20
   __DATA.__bss: 0x400

   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CVNLP.framework/CVNLP
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 167
-  Symbols:   180
-  CStrings:  222
+  Functions: 175
+  Symbols:   188
+  CStrings:  253
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_MetricsLogger
+ _OBJC_METACLASS_$_MetricsLogger
+ __NSConcreteStackBlock
+ _dispatch_async
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _objc_retain_x23
CStrings:
+ "\x01"
+ "\x12"
+ "@\"MetricsLogger\""
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@24@0:8Q16"
+ "MetricsLogger"
+ "Recording image captioning result CoreAnalytics event for: %@, success: %@, failureType: %@, captionConfidence: %f"
+ "_analyticsSynchronizationQueue"
+ "_friendlyStringForResultFailureType:"
+ "_metricsClientIdentifier"
+ "_metricsLogger"
+ "bundleIdentifier"
+ "captionConfidence"
+ "clientIdentifier"
+ "com.apple.Safari.ImageCaptioning.Result"
+ "com.apple.SmartReplies.ImageCaptioningAnalytics"
+ "failed"
+ "failureType"
+ "low confidence"
+ "low quality input"
+ "model failure"
+ "model unavailable"
+ "none"
+ "numberWithBool:"
+ "numberWithUnsignedInteger:"
+ "potentially unsafe"
+ "recordImageCaptioningResultWithClientIdentifier:success:failureType:confidence:"
+ "succeeded"
+ "success"
+ "v40@0:8@16B24Q28f36"
+ "v8@?0"
- "\x11"

```
