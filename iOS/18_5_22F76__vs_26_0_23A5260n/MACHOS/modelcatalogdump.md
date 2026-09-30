## modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

-162.762.0.0.0
-  __TEXT.__text: 0xf658
-  __TEXT.__auth_stubs: 0xb60
+206.3.0.0.0
+  __TEXT.__text: 0x18a10
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__cstring: 0x566
+  __TEXT.__const: 0x3fc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x314
-  __TEXT.__constg_swiftt: 0x74
-  __TEXT.__swift5_typeref: 0x225
-  __TEXT.__swift5_fieldmd: 0xa8
-  __TEXT.__cstring: 0x35a
+  __TEXT.__constg_swiftt: 0xa0
+  __TEXT.__swift5_typeref: 0x3e5
+  __TEXT.__swift5_fieldmd: 0x78
+  __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__swift5_capture: 0x30
-  __TEXT.__objc_methname: 0x3e
-  __TEXT.__swift5_reflstr: 0x53
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__eh_frame: 0x938
-  __DATA_CONST.__auth_got: 0x5b0
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__auth_ptr: 0x1c0
-  __DATA_CONST.__const: 0x1e0
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift5_capture: 0x40
+  __TEXT.__objc_methname: 0x9e
+  __TEXT.__swift5_reflstr: 0x2d
+  __TEXT.__unwind_info: 0x518
+  __TEXT.__eh_frame: 0xe68
+  __DATA_CONST.__auth_got: 0x7c8
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x208
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x28
-  __DATA.__data: 0x2b8
+  __DATA.__objc_selrefs: 0x48
+  __DATA.__data: 0x358
   __DATA.__common: 0x18
   __DATA.__bss: 0x680
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/TabularData.framework/TabularData
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: EC5E6464-5CA4-30E4-AF9F-9CEC4B72D01C
-  Functions: 299
-  Symbols:   94
-  CStrings:  23
+  UUID: 5B4868D5-4CDE-35C6-9EFC-C84996FB1FD4
+  Functions: 439
+  Symbols:   101
+  CStrings:  41
 
Symbols:
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _bzero
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x8
+ _strerror
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_getForeignTypeMetadata
+ _swift_initStackObject
+ _sysctl
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_allocBox
- _swift_bridgeObjectRelease_n
- _swift_getAssociatedConformanceWitness
- _swift_getAssociatedTypeWitness
- _swift_release_n
CStrings:
+ "  AFM + ADM Subscriptions"
+ "  Asset Information"
+ "  Asset Information (Monitored Update)"
+ "  Asset Information (Printing updates then exiting...)"
+ "  Device Configuration"
+ "  Use Case Asset Availability"
+ " * ✅ ready for: "
+ " * ❌ NOT ready for: "
+ " - All Enabled Languages: "
+ " - Feature Flag: "
+ " - System Language: "
+ " cannot be represented as pid_t."
+ ", current token: "
+ ", pidsLockingToken: "
+ "==============================================================================="
+ "Asset Availability will be displayed for each <language> parameter relevant to the current device"
+ "Availability for "
+ "Error getting process name for PID "
+ "Error: Int value "
+ "Required Resource Name"
+ "Resource Configuration Identifier"
+ "Tool command completed in "
+ "_deviceLanguage"
+ "asset is downloaded and able to be fetched"
+ "asset is not able to be fetched"
+ "asset is not marked as required for this specific use-case variant"
+ "downloadStatusForSubscribers:queue:completion:"
+ "name"
+ "subscriptionsForSubscriber:"
+ "v16@?0Q8"
- " is available for the following "
- " parameter combinations: "
- ", while asset is missing"
- ", while coherent asset has version "
- ", while coherent asset is missing"
- "---- No use case association ----"
- "GM\tApple Intelligence / Generative Models essential"
- "If you wish the tool to show all resource variants"
- "Stopping monitoring, printing status updates then exiting..."
- "The tags of the resources"
- "⚠️ asset has version "
- "⚠️ coherent asset has version "

```
