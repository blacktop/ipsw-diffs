## HealthAppHealthDaemonSupport

> `/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x1314c
+7027.1.36.2.7
+  __TEXT.__text: 0x18d38
   __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__const: 0x980
-  __TEXT.__cstring: 0x351
-  __TEXT.__swift5_typeref: 0x453
-  __TEXT.__swift5_capture: 0x7ac
-  __TEXT.__constg_swiftt: 0x3c8
-  __TEXT.__swift5_reflstr: 0x14a
-  __TEXT.__swift5_fieldmd: 0x268
+  __TEXT.__const: 0x9e8
+  __TEXT.__cstring: 0x3f1
+  __TEXT.__swift5_typeref: 0x48d
+  __TEXT.__swift5_capture: 0x7c0
+  __TEXT.__constg_swiftt: 0x3ec
+  __TEXT.__swift5_reflstr: 0x1ab
+  __TEXT.__swift5_fieldmd: 0x2b4
   __TEXT.__oslogstring: 0x1e3
   __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift_as_entry: 0x38
-  __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift_as_cont: 0x4c
-  __TEXT.__unwind_info: 0x810
-  __TEXT.__eh_frame: 0x798
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x34
+  __TEXT.__swift_as_cont: 0x60
+  __TEXT.__unwind_info: 0x910
+  __TEXT.__eh_frame: 0xa70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1df0
+  __AUTH_CONST.__const: 0x1f30
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x8e8
-  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__auth_got: 0x678
   __AUTH.__objc_data: 0x1d0
   __AUTH.__data: 0xc8
-  __DATA.__data: 0x550
+  __DATA.__data: 0x590
   __DATA_DIRTY.__objc_data: 0x288
   __DATA_DIRTY.__data: 0x2c8
   __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
-  - /System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration
   - /System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 741
-  Symbols:   382
-  CStrings:  29
+  Functions: 790
+  Symbols:   393
+  CStrings:  32
 
Symbols:
+ _OBJC_CLASS_$_HPFUserInteractionFetchRequestXPCTransport
+ ___swift_closure_destructor.15Tm
+ ___swift_memcpy72_8
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_HealthAppHealthDaemonSupport
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_HealthAppHealthDaemonSupport
+ _objc_msgSend$hk_error:description:
+ _objc_msgSend$remote_fetchInteractionsWithRequest:withCompletion:
+ _objc_msgSend$remote_softDeleteInteractions:withCompletion:
+ _swift_dynamicCastClass
+ _swift_release_x10
+ _swift_release_x12
+ _swift_retain
+ _symbolic Say_____G 10Foundation4UUIDV
+ _symbolic So42HPFUserInteractionFetchRequestXPCTransportC
+ _symbolic _____ 09HealthAppA13DaemonSupport29CustomPinnedContentIdentifierO
- ___swift_closure_destructor.11Tm
- ___swift_closure_destructor.8Tm
- ___swift_memcpy32_8
- _objc_msgSend$hk_error:userInfo:
- _objc_msgSend$remote_fetchInteractionsWithFeatureIdentifier:itemIdentifier:withCompletion:
- _objc_msgSend$remote_softDeleteInteractionWithUUID:withCompletion:
- _symbolic _____ 10Foundation4UUIDV
CStrings:
+ "Expected an HAHDAwakeningInputSignalRegistrarServerInterface proxy, got "
+ "Expected an HAHDUserInteractionStoreServerInterface proxy, got "
+ "HKObjectType_CycleTrackingCustom"
+ "fetchInteractions(_:)"
+ "softDeleteInteractions(uuids:)"
- "fetchInteractions(featureIdentifier:itemIdentifier:)"
- "softDeleteInteraction(uuid:)"
```
