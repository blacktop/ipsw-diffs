## SiriAppResolution

> `/System/Library/PrivateFrameworks/SiriAppResolution.framework/Versions/A/SiriAppResolution`

```diff

-3600.28.13.0.0
-  __TEXT.__text: 0x1af38
-  __TEXT.__const: 0x1160
-  __TEXT.__cstring: 0x763
-  __TEXT.__swift5_typeref: 0x786
-  __TEXT.__constg_swiftt: 0x938
-  __TEXT.__swift5_reflstr: 0x436
-  __TEXT.__swift5_fieldmd: 0x574
+3605.14.1.0.0
+  __TEXT.__text: 0x1c0f8
+  __TEXT.__const: 0x12d0
+  __TEXT.__cstring: 0x783
+  __TEXT.__swift5_typeref: 0x7e8
+  __TEXT.__constg_swiftt: 0x9d0
+  __TEXT.__swift5_reflstr: 0x464
+  __TEXT.__swift5_fieldmd: 0x5f4
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x98
-  __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0x80
+  __TEXT.__swift5_proto: 0xac
+  __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_capture: 0x358
-  __TEXT.__oslogstring: 0xbde
+  __TEXT.__oslogstring: 0xcde
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__unwind_info: 0xa28
   __TEXT.__eh_frame: 0x7a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1628
-  __AUTH_CONST.__objc_const: 0x6e8
-  __AUTH_CONST.__auth_got: 0x550
-  __AUTH.__data: 0x338
-  __DATA.__data: 0x410
+  __AUTH_CONST.__const: 0x1860
+  __AUTH_CONST.__objc_const: 0x708
+  __AUTH_CONST.__auth_got: 0x590
+  __AUTH.__data: 0x348
+  __DATA.__data: 0x450
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x380
   __DATA_DIRTY.__bss: 0x480
   __DATA_DIRTY.__common: 0x20
+  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 738
-  Symbols:   362
-  CStrings:  99
+  Functions: 772
+  Symbols:   379
+  CStrings:  101
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _LSSystemApplicationType
+ _OBJC_CLASS_$_LSApplicationProxy
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSExtension
+ __swift_closure_destructor.67Tm
+ _associated conformance 17SiriAppResolution0aB20AuthorizationVerdictOSHAASQ
+ _dispatch_semaphore_create
+ _objc_msgSend$_intents_findSiriEntitledAppsContainingAnIntentsExtensionWithCompletion:
+ _objc_msgSend$applicationType
+ _swift_dynamicCastObjCClass
+ _symbolic $s17SiriAppResolution0A20AuthorizationReadingP
+ _symbolic So21OS_dispatch_semaphoreC
+ _symbolic _____ 17SiriAppResolution04StubA19AuthorizationReaderV
+ _symbolic _____ 17SiriAppResolution07IntentsA19AuthorizationReaderV
+ _symbolic _____ 17SiriAppResolution08ExcludedB8DecisionO
+ _symbolic _____ 17SiriAppResolution0aB20AuthorizationVerdictO
- __swift_closure_destructor.41Tm
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
