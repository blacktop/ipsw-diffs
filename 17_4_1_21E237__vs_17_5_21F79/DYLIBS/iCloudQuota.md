## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.21.4.10.0
-  __TEXT.__text: 0x81238
+301.21.4.14.0
+  __TEXT.__text: 0x81670
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x542c
+  __TEXT.__objc_methlist: 0x54a4
   __TEXT.__const: 0xdf0
-  __TEXT.__cstring: 0x6fb1
+  __TEXT.__cstring: 0x6fe1
   __TEXT.__oslogstring: 0x7301
   __TEXT.__gcc_except_tab: 0x4d8
   __TEXT.__dlopen_cstrs: 0x35f

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x222c
+  __TEXT.__unwind_info: 0x2288
   __TEXT.__eh_frame: 0x2108
-  __TEXT.__objc_classname: 0xa2c
-  __TEXT.__objc_methname: 0xcde2
+  __TEXT.__objc_classname: 0xa40
+  __TEXT.__objc_methname: 0xcf32
   __TEXT.__objc_methtype: 0xc4e
-  __TEXT.__objc_stubs: 0x8b20
+  __TEXT.__objc_stubs: 0x8c60
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x1d90
-  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7d90
-  __DATA_CONST.__objc_selrefs: 0x2d40
-  __DATA_CONST.__objc_classrefs: 0x588
-  __DATA_CONST.__objc_superrefs: 0x278
+  __DATA_CONST.__objc_const: 0x7e48
+  __DATA_CONST.__objc_selrefs: 0x2d98
+  __DATA_CONST.__objc_classrefs: 0x598
+  __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x2060
-  __AUTH_CONST.__cfstring: 0x6f40
-  __AUTH_CONST.__objc_const: 0x3078
+  __AUTH_CONST.__cfstring: 0x6f80
+  __AUTH_CONST.__objc_const: 0x30c0
   __AUTH_CONST.__const: 0x1898
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0x1478

   __AUTH_CONST.__auth_got: 0xb48
   __AUTH.__objc_data: 0x1840
   __AUTH.__data: 0x780
-  __DATA.__objc_ivar: 0x650
-  __DATA.__data: 0x758
-  __DATA.__bss: 0x1480
+  __DATA.__objc_ivar: 0x658
+  __DATA.__data: 0x7a8
+  __DATA.__bss: 0x1450
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xd58
+  __DATA_DIRTY.__objc_data: 0xda8
   __DATA_DIRTY.__data: 0x1e8
   __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 57878DEE-8F5B-3CED-866D-24CAA6C91869
-  Functions: 3259
-  Symbols:   8170
-  CStrings:  5056
+  UUID: 8E2F015A-8C36-3C28-B8FF-C3EE9FD0C5A1
+  Functions: 3268
+  Symbols:   8208
+  CStrings:  5074
 
Symbols:
+ -[ICQOfferCacheObject .cxx_destruct]
+ -[ICQOfferCacheObject bundleIdentifier]
+ -[ICQOfferCacheObject daemonOffer]
+ -[ICQOfferCacheObject initWithDaemonOffer:bundleIdentifier:]
+ -[ICQOfferCacheObject offer]
+ -[ICQOfferCacheObject setBundleIdentifier:]
+ -[ICQOfferCacheObject setDaemonOffer:]
+ -[ICQOfferManager removeCachedOfferForType:]
+ -[ICQOfferManager setCachedOfferForType:daemonOffer:bundleIdentifier:]
+ -[ICQOfferManager shouldPresentAppLaunchLink:]
+ GCC_except_table36
+ _OBJC_CLASS_$_ICQOfferCacheObject
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_IVAR_$_ICQOfferCacheObject._bundleIdentifier
+ _OBJC_IVAR_$_ICQOfferCacheObject._daemonOffer
+ _OBJC_METACLASS_$_ICQOfferCacheObject
+ __OBJC_$_INSTANCE_METHODS_ICQOfferCacheObject
+ __OBJC_$_INSTANCE_VARIABLES_ICQOfferCacheObject
+ __OBJC_$_PROP_LIST_ICQOfferCacheObject
+ __OBJC_CLASS_RO_$_ICQOfferCacheObject
+ __OBJC_METACLASS_RO_$_ICQOfferCacheObject
+ ___39-[ICQOfferManager _refetchDefaultOffer]_block_invoke.65
+ ___62-[ICQOfferManager appLaunchLinkDidPresentForBundleIdentifier:]_block_invoke.27
+ ___62-[ICQOfferManager appLaunchLinkDidPresentForBundleIdentifier:]_block_invoke.27.cold.1
+ ___62-[ICQOfferManager appLaunchLinkDidPresentForBundleIdentifier:]_block_invoke.27.cold.2
+ ___70-[ICQOfferManager setCachedOfferForType:daemonOffer:bundleIdentifier:]_block_invoke
+ ___88-[ICQOfferManager _getOfferForAccount:bundleIdentifier:options:offerContext:completion:]_block_invoke.48
+ ___88-[ICQOfferManager _getOfferForAccount:bundleIdentifier:options:offerContext:completion:]_block_invoke.50
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.30
+ ___block_literal_global.74
+ _objc_msgSend$components:fromDate:toDate:options:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$day
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$initWithDaemonOffer:bundleIdentifier:
+ _objc_msgSend$initWithTimeIntervalSince1970:
+ _objc_msgSend$now
+ _objc_msgSend$offer
+ _objc_msgSend$removeCachedOfferForType:
+ _objc_msgSend$setCachedOfferForType:daemonOffer:bundleIdentifier:
+ _objc_msgSend$setDouble:forKey:
- -[ICQOfferManager setCachedOfferForType:newOffer:]
- GCC_except_table35
- GCC_except_table50
- ___39-[ICQOfferManager _refetchDefaultOffer]_block_invoke.58
- ___50-[ICQOfferManager setCachedOfferForType:newOffer:]_block_invoke
- ___62-[ICQOfferManager appLaunchLinkDidPresentForBundleIdentifier:]_block_invoke.22
- ___62-[ICQOfferManager appLaunchLinkDidPresentForBundleIdentifier:]_block_invoke.22.cold.1
- ___62-[ICQOfferManager appLaunchLinkDidPresentForBundleIdentifier:]_block_invoke.22.cold.2
- ___88-[ICQOfferManager _getOfferForAccount:bundleIdentifier:options:offerContext:completion:]_block_invoke.42
- ___88-[ICQOfferManager _getOfferForAccount:bundleIdentifier:options:offerContext:completion:]_block_invoke.44
- ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.25
- ___block_literal_global.71
- _objc_msgSend$setCachedOfferForType:newOffer:
CStrings:
+ "ICQOfferCacheObject"
+ "T@\"ICQDaemonOffer\",&,N,V_daemonOffer"
+ "T@\"NSString\",C,N,V_bundleIdentifier"
+ "components:fromDate:toDate:options:"
+ "currentCalendar"
+ "day"
+ "doubleForKey:"
+ "iCloudAppLaunchLinkPresentationDate"
+ "initWithDaemonOffer:bundleIdentifier:"
+ "initWithTimeIntervalSince1970:"
+ "lockscreen"
+ "now"
+ "removeCachedOfferForType:"
+ "setCachedOfferForType:daemonOffer:bundleIdentifier:"
+ "setDaemonOffer:"
+ "setDouble:forKey:"
+ "shouldPresentAppLaunchLink:"
- "setCachedOfferForType:newOffer:"

```
