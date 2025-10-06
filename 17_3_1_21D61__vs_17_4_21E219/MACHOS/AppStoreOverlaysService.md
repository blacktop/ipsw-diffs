## AppStoreOverlaysService

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService`

```diff

-6.3.2.0.0
-  __TEXT.__text: 0x1404c
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x2460
-  __TEXT.__objc_methlist: 0xde8
-  __TEXT.__const: 0x4d4
-  __TEXT.__cstring: 0x1037
-  __TEXT.__objc_classname: 0x338
-  __TEXT.__objc_methname: 0x2e3f
-  __TEXT.__objc_methtype: 0x8ce
-  __TEXT.__oslogstring: 0xab9
+6.4.31.0.0
+  __TEXT.__text: 0x14bf8
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_stubs: 0x2500
+  __TEXT.__objc_methlist: 0xe40
+  __TEXT.__const: 0x4f4
+  __TEXT.__cstring: 0x1147
+  __TEXT.__objc_classname: 0x33c
+  __TEXT.__objc_methname: 0x3009
+  __TEXT.__objc_methtype: 0x90c
+  __TEXT.__oslogstring: 0xb12
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x34c
-  __TEXT.__swift5_typeref: 0x31e
-  __TEXT.__swift5_reflstr: 0x1da
-  __TEXT.__swift5_fieldmd: 0x20c
+  __TEXT.__constg_swiftt: 0x39c
+  __TEXT.__swift5_typeref: 0x32e
+  __TEXT.__swift5_reflstr: 0x1ea
+  __TEXT.__swift5_fieldmd: 0x228
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__unwind_info: 0x62c
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x9d8
   __DATA_CONST.__cfstring: 0x380
-  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2548
-  __DATA.__objc_selrefs: 0xc48
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x278
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__objc_data: 0xbf8
-  __DATA.__data: 0x960
+  __DATA.__objc_const: 0x25c0
+  __DATA.__objc_selrefs: 0xc78
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_data: 0xcc8
+  __DATA.__data: 0x990
   __DATA.__bss: 0x660
   __DATA.__common: 0xc0
+  - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1101D0B8-BA3A-3365-8548-99167B19EC64
-  Functions: 510
-  Symbols:   278
-  CStrings:  858
+  UUID: ECFF6E3A-C9A2-3175-B9F4-1158643E76DA
+  Functions: 526
+  Symbols:   281
+  CStrings:  873
 
Symbols:
+ _ASDInstallAttributionInteractionTypeClick
+ _ASDInstallAttributionInteractionTypeView
+ __swift_FORCE_LOAD_$_swiftAccelerate
CStrings:
+ "\x03"
+ "@\"<ASOServiceOverlayInteractionObserver>\""
+ "ASOAttributionKitBridge"
+ "ASOServiceOverlayInteractionObserver"
+ "Received error while recording click through impression: "
+ "Received error while recording view through impression: "
+ "T@\"<ASOServiceOverlayInteractionObserver>\",N,&,VoverlayInteractionObserver"
+ "T@\"<ASOServiceOverlayInteractionObserver>\",N,V_offerButtonObserver"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",N,R"
+ "Unable to record an AttributionKit impression because the advertised item id is invalid."
+ "compactJWSDictionaryKey"
+ "logger"
+ "overlayInteractionObserver"
+ "overlayWasTapped"
+ "recordAttributionKitImpressionWithCompactJWS:storeIdentifier:hostBundleID:interactionType:attributionKitRecorder:"
+ "recordClickThroughWithAdvertisedItemID:compactJWS:bundleID:"
+ "recordInstallAttributionWithParameters:storeIdentifier:hostAdamID:clientBundleId:interactionType:"
+ "recordInstallAttributionWithParameters:storeIdentifier:hostAdamID:clientBundleId:interactionType:attributionKitRecorder:skanRecorder:"
+ "recordSKAdNetworkImpressionWithParameters:storeIdentifier:hostAdamID:clientBundleId:interactionType:skanRecorder:"
+ "recordViewThroughWithAdvertisedItemID:compactJWS:bundleID:"
+ "setInteractionType:"
+ "setOverlayInteractionObserver:"
+ "unsignedLongLongValue"
+ "v40@0:8Q16@24@32"
+ "v56@0:8@16@24@32@40q48"
+ "v56@0:8@16@24@32q40@48"
+ "v64@0:8@16@24@32@40q48@56"
+ "v72@0:8@16@24@32@40q48@56@64"
- "\x13"
- "@\"<ASOServiceOfferButtonTapObserver>\""
- "ASOServiceOfferButtonTapObserver"
- "T@\"<ASOServiceOfferButtonTapObserver>\",N,&,VofferButtonTapObserver"
- "T@\"<ASOServiceOfferButtonTapObserver>\",N,V_offerButtonObserver"
- "TB,N,V_didAttribute"
- "_didAttribute"
- "didAttribute"
- "offerButtonTapObserver"
- "recordInstallAttributionWithParameters:storeIdentifier:hostAdamID:clientBundleId:"
- "recordInstallAttributionWithParameters:storeIdentifier:hostAdamID:clientBundleId:recorder:"
- "setDidAttribute:"
- "setOfferButtonTapObserver:"
- "v48@0:8@16@24@32@40"
- "v56@0:8@16@24@32@40@48"

```
