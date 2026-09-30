## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-444.0.0.0.0
-  __TEXT.__text: 0x40594
-  __TEXT.__auth_stubs: 0x980
+446.0.0.0.1
+  __TEXT.__text: 0x4110c
+  __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_stubs: 0x6e60
-  __TEXT.__objc_methlist: 0x2d58
+  __TEXT.__objc_methlist: 0x2d48
   __TEXT.__const: 0x208
-  __TEXT.__gcc_except_tab: 0x1930
-  __TEXT.__cstring: 0x33c6
-  __TEXT.__objc_methname: 0x84ca
-  __TEXT.__oslogstring: 0x50e7
+  __TEXT.__gcc_except_tab: 0x1958
+  __TEXT.__cstring: 0x3464
+  __TEXT.__oslogstring: 0x5370
   __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methtype: 0x1126
-  __TEXT.__unwind_info: 0xe40
-  __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0x210
+  __TEXT.__objc_methname: 0x84aa
+  __TEXT.__objc_methtype: 0x1137
+  __TEXT.__unwind_info: 0xe38
+  __DATA_CONST.__auth_got: 0x500
+  __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x1638
-  __DATA_CONST.__cfstring: 0x2920
+  __DATA_CONST.__cfstring: 0x2980
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA.__objc_const: 0x4270
-  __DATA.__objc_selrefs: 0x2128
+  __DATA.__objc_selrefs: 0x2120
   __DATA.__objc_ivar: 0x338
   __DATA.__objc_data: 0xd20
   __DATA.__data: 0x250

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MetricKit.framework/MetricKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46F3CBCD-515F-329B-A55A-B36E4B9D8451
-  Functions: 1392
-  Symbols:   230
-  CStrings:  2954
+  UUID: BF97E26C-CF21-365A-93FC-DC750F1BC0D3
+  Functions: 1400
+  Symbols:   237
+  CStrings:  2977
 
Symbols:
+ _IOBSDNameMatching
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryCreateIterator
+ _IOServiceGetMatchingService
+ _kIOMainPortDefault
CStrings:
+ "%@ %@: %llu > diskCapacity: %llu"
+ "%@ %@: < 0"
+ "%s: Can't get volume size for %s (err %d)"
+ "%s: Failed to find root disk size"
+ "%s:%s: spaceAvail %llu (capacity:%llu)"
+ "+[SASupport getDiskCapacity]"
+ "+[SASupport getDiskUsed]"
+ "Age %llu for dirKey number %llu, inode %llu, bundleID %@"
+ "Exceeded the number of max iterations (%d) while iterating %@ parents in the IO registry"
+ "Exceeded the number of max iterations (%d) while searching for the IO media device in the IO registry"
+ "Failed to create IO iterator with error code %d"
+ "Failed to find %@ entry is the IO registry"
+ "Failed to get boot disk IO media object in registry"
+ "Failed to get containing block device for disk %@"
+ "IOBlockStorageDevice"
+ "IOMedia"
+ "IOService"
+ "Size"
+ "cfBootDisk: %@"
+ "checkDirStatSizeInconsistency:path:diskCapacity:"
+ "dirStats physicalSize: %llu > diskCapacity: %llu for dirKey %llu bundleIDs %@"
+ "getDiskCapacity"
+ "getDiskUsed"
+ "v40@0:8@16@24q32"
- "checkDirStatSizeInconsistency:path:"
- "getLastSentTelemetryDate"
- "lastSpeculativeDownloadSentTelemetryDate"
- "shouldSendTelemetry"
- "updateLastSentTelemetryDate"

```
