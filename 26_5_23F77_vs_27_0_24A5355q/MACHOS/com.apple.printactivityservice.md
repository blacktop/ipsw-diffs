## com.apple.printactivityservice

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.printactivityservice.xpc/com.apple.printactivityservice`

```diff

-32.7.0.0.0
-  __TEXT.__text: 0x7a40
-  __TEXT.__auth_stubs: 0x850
+42.0.0.0.0
+  __TEXT.__text: 0xa114
+  __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x328
-  __TEXT.__const: 0x5d8
-  __TEXT.__cstring: 0x34c
+  __TEXT.__objc_methlist: 0x338
+  __TEXT.__const: 0x832
+  __TEXT.__cstring: 0x8cc
   __TEXT.__objc_classname: 0x94
-  __TEXT.__objc_methname: 0xac0
+  __TEXT.__objc_methname: 0xaea
   __TEXT.__objc_methtype: 0x180
-  __TEXT.__swift5_typeref: 0x1f7
-  __TEXT.__swift5_reflstr: 0xfd
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0xb8
-  __TEXT.__swift5_fieldmd: 0x17c
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_capture: 0x7c
+  __TEXT.__swift5_typeref: 0x283
+  __TEXT.__constg_swiftt: 0x124
+  __TEXT.__swift5_reflstr: 0x28d
+  __TEXT.__swift5_fieldmd: 0x374
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0x6c
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_capture: 0x8c
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__eh_frame: 0x270
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__auth_ptr: 0x1a0
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0x1c0
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__unwind_info: 0x350
+  __TEXT.__eh_frame: 0x3c0
+  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x4b8
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__auth_ptr: 0x1f0
+  __DATA.__objc_const: 0x470
   __DATA.__objc_selrefs: 0x378
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x1c8
-  __DATA.__data: 0x258
-  __DATA.__bss: 0x8e0
+  __DATA.__objc_data: 0x1d0
+  __DATA.__data: 0x3b8
+  __DATA.__bss: 0xda0
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/PrivateFrameworks/PrintKit.framework/PrintKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25F5806F-7CA2-3BA0-8B35-79926C092186
-  Functions: 224
-  Symbols:   136
-  CStrings:  192
+  UUID: 8C14A544-DB31-3D33-BA34-67FD6627F578
+  Functions: 253
+  Symbols:   164
+  CStrings:  235
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveEveryObserver
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _PCCancelPrintJobNotification
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _swift_arrayInitWithCopy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x25
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_updateClassMetadata2
- _OBJC_CLASS_$_NSLock
- _OBJC_CLASS_$_UIImage
- _PKPrinterUUIDKey
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "A paper tray is missing."
+ "Changed Certificate - Check the printer for errors."
+ "Check the printer for errors."
+ "Expired Certificate - Check the printer for errors."
+ "Invalid Certificate - Check the printer for errors."
+ "PCCancelPrintJobNotification"
+ "PKJobListNotification"
+ "PKJobProgressNotification"
+ "Software for the printer is missing."
+ "The printer cover is open."
+ "The printer door is open."
+ "The printer has a paper jam."
+ "The printer is almost out of paper."
+ "The printer is offline."
+ "The printer is out of paper."
+ "The printer is paused."
+ "The printer may be out of ink."
+ "The printer may be out of toner."
+ "The printer needs paper."
+ "The software for this printer is not correctly installed."
+ "Unknown Certificate - Check the printer for errors."
+ "addedObservers"
+ "cancel"
+ "com.apple.printd.job-list"
+ "com.apple.printd.job-progress"
+ "connecting-to-device"
+ "cups-insecure-filter-warning"
+ "cups-missing-filter"
+ "cups-pki-changed"
+ "cups-pki-expired"
+ "cups-pki-invalid"
+ "cups-pki-unknown"
+ "fuser-under-temp"
+ "input-tray-missing"
+ "jobImageURL"
+ "jobPrinterStateReasons"
+ "localizedStringForKey:value:table:"
+ "marker-supply-empty"
+ "marker-supply-low"
+ "marker-waste-almost-full"
+ "marker-waste-full"
+ "output-area-almost-full"
+ "output-area-full"
+ "output-tray-missing"
+ "postNotificationName:object:"
- "Could not remove file at path: "
- "initWithData:"
- "jobImagePath"
- "lock"
- "pendingJobsLock"
- "removeItemAtPath:error:"
- "unlock"

```
