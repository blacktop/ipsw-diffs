## AppStoreFoundation

> `/System/Library/PrivateFrameworks/AppStoreFoundation.framework/Versions/A/AppStoreFoundation`

```diff

-11.2.29.0.0
-  __TEXT.__text: 0x6750
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x4b8
+11.4.24.0.0
+  __TEXT.__text: 0x6834
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x634
   __TEXT.__const: 0x88
   __TEXT.__swift5_typeref: 0x5e
   __TEXT.__swift5_fieldmd: 0x10

   __TEXT.__cstring: 0x30f
   __TEXT.__oslogstring: 0x4be
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0xd1
   __TEXT.__objc_methname: 0x1047
   __TEXT.__objc_methtype: 0x202

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_selrefs: 0x4e0
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x168
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x1420
+  __AUTH_CONST.__objc_const: 0x1160
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x120

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8A77A6F8-5F09-3B61-A1F9-965886C57555
+  UUID: 45EE8061-2A11-3763-BD6D-CC55754C36FE
   Functions: 123
-  Symbols:   511
+  Symbols:   513
   CStrings:  414
 
Symbols:
+ _ASFLogHandleForCategory
+ _objc_retainAutoreleaseReturnValue
Functions:
~ sub_1b9beeba0 -> sub_1bb521b00 : 160 -> 152
~ -[ASFReceipt initWithData:] -> _ASFLogHandleForCategory : 7988 -> 84
~ sub_1b9bf1798 -> -[ASFReceipt initWithData:] : 100 -> 8208
~ sub_1b9bf17fc -> sub_1bb524820 : 24 -> 100
~ +[ASFAsn1Token readTokenFromBuffer:opaque:length:] : 1360 -> 1348
~ -[ASFVolumeMonitor installableVolumes] : 84 -> 80
~ -[ASFVolumeMonitor removableVolumes] : 84 -> 80
~ -[ASFVolumeMonitor disksAppeared:] : 928 -> 920
~ -[ASFVolumeMonitor disksChanged:] : 2532 -> 2524
~ -[ASFVolumeMonitor disksDisappeared:] : 852 -> 844

```
