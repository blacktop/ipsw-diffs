## promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

-478.0.0.0.0
-  __TEXT.__text: 0x131724
+485.0.0.0.0
+  __TEXT.__text: 0x13100c
   __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_stubs: 0x16540
-  __TEXT.__objc_methlist: 0x126bc
-  __TEXT.__const: 0xe6b0
-  __TEXT.__objc_methname: 0x211a3
-  __TEXT.__oslogstring: 0xafda
-  __TEXT.__cstring: 0xa314
+  __TEXT.__objc_stubs: 0x16360
+  __TEXT.__objc_methlist: 0x126a4
+  __TEXT.__const: 0xe6a8
+  __TEXT.__objc_methname: 0x21023
+  __TEXT.__oslogstring: 0xb025
+  __TEXT.__cstring: 0xa308
   __TEXT.__objc_classname: 0x2419
   __TEXT.__objc_methtype: 0x4701
   __TEXT.__gcc_except_tab: 0xeac

   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x36f4
+  __TEXT.__unwind_info: 0x36e0
   __TEXT.__eh_frame: 0x118
   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x8958
+  __DATA_CONST.__const: 0x8918
   __DATA_CONST.__cfstring: 0xd640
   __DATA_CONST.__objc_classlist: 0x9f0
   __DATA_CONST.__objc_catlist: 0xc0

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x130
   __DATA.__objc_const: 0x22f78
-  __DATA.__objc_selrefs: 0x8150
+  __DATA.__objc_selrefs: 0x80d8
   __DATA.__objc_protorefs: 0xb8
-  __DATA.__objc_classrefs: 0xc88
+  __DATA.__objc_classrefs: 0xc78
   __DATA.__objc_superrefs: 0x6d0
   __DATA.__objc_ivar: 0x13f8
   __DATA.__objc_data: 0x6390

   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A7B7CA0F-5569-38C2-99F0-6C73C7C0D4FC
-  Functions: 6678
-  Symbols:   1968
-  CStrings:  11563
+  UUID: 6DFD69CF-3940-34DD-AC5F-25C499DF8190
+  Functions: 6674
+  Symbols:   1967
+  CStrings:  11550
 
Symbols:
+ _kAPDeviceInfoOperatingSystemvisionOS
- _OBJC_CLASS_$_APOdmlReranker
- _OBJC_CLASS_$_APOdmlSettings
CStrings:
+ "ODML disabled. Sorting content data."
+ "ODML enabled. Reranking content data."
+ "visionOS"
- "_processRerankedRepresentations:originalContentData:withError:"
- "_rerankOnDevice:completionHandler:"
- "deploymentID"
- "experimentID"
- "getRerankedAdsWithTimeLimit:completion:"
- "initWithPersonalizedAdsEnabled:placementType:"
- "initWithPlacementType:assetManagerType:"
- "insertObject:atIndex:"
- "odmlEnabled"
- "odmlResponse"
- "setAndRerankAds:"
- "setDeploymentId:"
- "setExperimentId:"
- "setOdmlSuccess:"
- "setTreatmentId:"
- "treatmentID"

```
