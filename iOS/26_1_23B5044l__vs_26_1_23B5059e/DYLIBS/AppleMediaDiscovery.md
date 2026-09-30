## AppleMediaDiscovery

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery`

```diff

-1.4.2.0.0
-  __TEXT.__text: 0xf1c80
+1.4.6.0.0
+  __TEXT.__text: 0xf1e70
   __TEXT.__auth_stubs: 0x1710
   __TEXT.__objc_methlist: 0x3b50
   __TEXT.__const: 0x698

   __TEXT.__unwind_info: 0x1360
   __TEXT.__eh_frame: 0x660
   __TEXT.__objc_classname: 0x67d
-  __TEXT.__objc_methname: 0x9e03
+  __TEXT.__objc_methname: 0x9dca
   __TEXT.__objc_methtype: 0xddb
-  __TEXT.__objc_stubs: 0x8f20
+  __TEXT.__objc_stubs: 0x8f00
   __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0xdb8
+  __DATA_CONST.__const: 0xdb0
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2800
+  __DATA_CONST.__objc_selrefs: 0x27f8
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x12c0
   __AUTH_CONST.__auth_got: 0xb98

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F824B72-F28E-35D8-A40B-C39D9A0F429C
+  UUID: 933DD715-7A8C-3327-9086-DB3B6F83AD70
   Functions: 1901
-  Symbols:   5319
-  CStrings:  6138
+  Symbols:   5318
+  CStrings:  6136
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_AppleMediaDiscovery
- _AMD_CLIENT_DSID
- _AMD_CLIENT_IAE_SEGMENT_NOTIFICATION
- _objc_msgSend$postNotificationName:object:userInfo:deliverImmediately:
Functions:
~ +[AMDSQLite deleteEventsOlderThan:] : 452 -> 1500
~ +[AMDAppSegment refreshSegmentsForAllTreatmentsForUser:error:] : 2796 -> 2244
CStrings:
+ "SQLITE deleteEventsOlderThan: Stream '%@' does not have creationTime"
- "Error retrieving segment data for notification: %@"
- "Sending IAE segment notification"
- "postNotificationName:object:userInfo:deliverImmediately:"

```
