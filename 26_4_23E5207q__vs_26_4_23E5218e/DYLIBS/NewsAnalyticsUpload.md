## NewsAnalyticsUpload

> `/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload`

```diff

-5861.1.0.0.0
-  __TEXT.__text: 0x1a4b8
+5864.0.0.0.0
+  __TEXT.__text: 0x1a4c0
   __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0xb5c
   __TEXT.__const: 0x1879

   __TEXT.__objc_methtype: 0xbec
   __TEXT.__objc_stubs: 0x2380
   __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics
   - /System/Library/PrivateFrameworks/NewsCore.framework/NewsCore
   - /System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FB0DD7C4-FD7B-3F20-A21C-C13B44F6D698
+  UUID: A94F0DA3-6283-3EC7-96A1-B135E2255421
   Functions: 794
-  Symbols:   1649
+  Symbols:   1655
   CStrings:  892
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_NewsAnalyticsUpload
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_NewsAnalyticsUpload
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_NewsAnalyticsUpload
Functions:
~ sub_26744e43c -> sub_267ff051c : 868 -> 876
CStrings:
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsAnalyticsUpload/TelemetryUploader.swift"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NAUAnalyticsEnvelopeTracker.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeManager.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStore.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStoreEntry.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssembler.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssemblerUtilities.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadUploader.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsUploadScheduler.m"
+ "/Library/Caches/com.apple.xbs/1DCFE137-72E3-4605-9233-DA95BA283994/TemporaryDirectory.R2kxHm/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAppConfigAnalyticsPayloadAssemblerConfigProvider.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsAnalyticsUpload/TelemetryUploader.swift"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NAUAnalyticsEnvelopeTracker.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeManager.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStore.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStoreEntry.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssembler.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssemblerUtilities.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadUploader.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsUploadScheduler.m"
- "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAppConfigAnalyticsPayloadAssemblerConfigProvider.m"

```
