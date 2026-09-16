## SiriAppResolution

> `/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution`

```diff

-3600.28.13.0.0
-  __TEXT.__text: 0x1b524
-  __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0x763
-  __TEXT.__swift5_typeref: 0x786
-  __TEXT.__constg_swiftt: 0x938
-  __TEXT.__swift5_reflstr: 0x436
-  __TEXT.__swift5_fieldmd: 0x574
+3605.14.1.0.0
+  __TEXT.__text: 0x1c670
+  __TEXT.__const: 0x12e0
+  __TEXT.__cstring: 0x783
+  __TEXT.__swift5_typeref: 0x7e8
+  __TEXT.__constg_swiftt: 0x9d0
+  __TEXT.__swift5_reflstr: 0x464
+  __TEXT.__swift5_fieldmd: 0x5f4
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x98
-  __TEXT.__swift5_proto: 0xa0
-  __TEXT.__swift5_types: 0x80
+  __TEXT.__swift5_proto: 0xb0
+  __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_capture: 0x358
-  __TEXT.__oslogstring: 0xc8e
+  __TEXT.__oslogstring: 0xd8e
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0xa20
+  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__unwind_info: 0xa60
   __TEXT.__eh_frame: 0x7a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1638
-  __AUTH_CONST.__objc_const: 0x6e8
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH.__data: 0x338
-  __DATA.__data: 0x410
+  __AUTH_CONST.__const: 0x1870
+  __AUTH_CONST.__objc_const: 0x708
+  __AUTH_CONST.__auth_got: 0x6e0
+  __AUTH.__data: 0x348
+  __DATA.__data: 0x450
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x380
   __DATA_DIRTY.__bss: 0x480
   __DATA_DIRTY.__common: 0x20
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 745
-  Symbols:   404
-  CStrings:  101
+  Functions: 779
+  Symbols:   422
+  CStrings:  103
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _LSSystemApplicationType
+ _OBJC_CLASS_$_LSApplicationProxy
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSExtension
+ ___swift_closure_destructor.67Tm
+ _associated conformance 17SiriAppResolution0aB20AuthorizationVerdictOSHAASQ
+ _dispatch_semaphore_create
+ _objc_msgSend$_intents_findSiriEntitledAppsContainingAnIntentsExtensionWithCompletion:
+ _objc_msgSend$applicationType
+ _objc_release_x26
+ _swift_dynamicCastObjCClass
+ _symbolic $s17SiriAppResolution0A20AuthorizationReadingP
+ _symbolic So21OS_dispatch_semaphoreC
+ _symbolic _____ 17SiriAppResolution04StubA19AuthorizationReaderV
+ _symbolic _____ 17SiriAppResolution07IntentsA19AuthorizationReaderV
+ _symbolic _____ 17SiriAppResolution08ExcludedB8DecisionO
+ _symbolic _____ 17SiriAppResolution0aB20AuthorizationVerdictO
- ___swift_closure_destructor.41Tm
- _symbolic _____XMT 17SiriAppResolution08LSPluginA22KitExtensionMembershipC
CStrings:
+ "Only candidate %s needs Siri authorization; resolving to it so the guard can prompt"
+ "SiriKitExtensionMembership: _intents_findSiriEntitledAppsContainingAnIntentsExtension failed: %s"
+ "SiriKitExtensionMembership: discovered %ld Use-with-Siri toggle app(s)"
+ "TCCDirectSiriAppAccessReader: kTCCServiceSiriAccess deny-list invalidated; will refetch on next query"
+ "com.apple.TCC.kTCCServiceSiriAccess.authorization.changed"
- "SiriKitExtensionMembership: discovered %ld SiriKit host bundle(s)"
- "SiriKitExtensionMembership: plugin enumeration error: %s"
- "com.apple.intents-service"
```
