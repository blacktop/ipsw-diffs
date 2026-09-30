## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_builtin`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-301.24.0.23.0
-  __TEXT.__text: 0x75d4c
-  __TEXT.__objc_methlist: 0x590c
-  __TEXT.__const: 0x1138
-  __TEXT.__cstring: 0x4f80
-  __TEXT.__oslogstring: 0x85f9
+301.24.0.25.0
+  __TEXT.__text: 0x77298
+  __TEXT.__objc_methlist: 0x597c
+  __TEXT.__const: 0x1198
+  __TEXT.__cstring: 0x4ff0
+  __TEXT.__oslogstring: 0x8799
   __TEXT.__gcc_except_tab: 0x5a8
   __TEXT.__dlopen_cstrs: 0x3b5
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x6e0
-  __TEXT.__swift5_capture: 0x318
+  __TEXT.__swift5_typeref: 0x71c
+  __TEXT.__swift5_capture: 0x32c
   __TEXT.__swift5_reflstr: 0x2a1
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__constg_swiftt: 0x64c
-  __TEXT.__swift5_fieldmd: 0x310
+  __TEXT.__constg_swiftt: 0x678
+  __TEXT.__swift5_fieldmd: 0x320
   __TEXT.__swift5_proto: 0x8c
-  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift5_types: 0x4c
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift_as_cont: 0xc0
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1d10
+  __TEXT.__unwind_info: 0x1d70
   __TEXT.__eh_frame: 0x1160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e20
-  __DATA_CONST.__objc_classlist: 0x398
+  __DATA_CONST.__const: 0x1e48
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3040
+  __DATA_CONST.__objc_selrefs: 0x3060
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x710
-  __DATA_CONST.__got: 0x800
-  __AUTH_CONST.__const: 0x1248
+  __DATA_CONST.__objc_arraydata: 0x730
+  __DATA_CONST.__got: 0x810
+  __AUTH_CONST.__const: 0x1298
   __AUTH_CONST.__cfstring: 0x6680
-  __AUTH_CONST.__objc_const: 0xb340
+  __AUTH_CONST.__objc_const: 0xb388
   __AUTH_CONST.__objc_intobj: 0x9a8
-  __AUTH_CONST.__objc_dictobj: 0x190
+  __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__auth_got: 0xbe0
-  __AUTH.__objc_data: 0x1500
-  __AUTH.__data: 0x460
+  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH.__objc_data: 0x15b0
+  __AUTH.__data: 0x490
   __DATA.__objc_ivar: 0x6b4
-  __DATA.__data: 0x548
-  __DATA.__bss: 0x1130
+  __DATA.__data: 0x558
+  __DATA.__bss: 0x1150
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x10d0
   __DATA_DIRTY.__data: 0x278

   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift
+  - /System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2907
-  Symbols:   5480
-  CStrings:  1626
+  Functions: 2941
+  Symbols:   5500
+  CStrings:  1634
 
Symbols:
+ +[ICQDaemonOfferManager logDailyQuotaUsageAnalyticsIgnoringThrottle:]
+ +[ICQDaemonOfferManager logDailyQuotaUsageAnalytics]
+ +[ICQDaemonOfferManager persistedOfferStubs]
+ +[ICQDaemonOfferManager persistedOffer]
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table72
+ GCC_except_table80
+ GCC_except_table97
+ _OBJC_CLASS_$_QuotaAnalytics
+ _OBJC_METACLASS_$_QuotaAnalytics
+ __CLASS_METHODS_QuotaAnalytics
+ __DATA_QuotaAnalytics
+ __INSTANCE_METHODS_QuotaAnalytics
+ __METACLASS_DATA_QuotaAnalytics
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_iCloudQuota
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$logDailyQuotaUsageAnalytics
+ _objc_msgSend$logDailyQuotaUsageAnalyticsIgnoringThrottle:
+ _objc_msgSend$persistedOfferStubs
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic Sd10totalQuota_Sd11usedStoraget
+ _symbolic _____ 11iCloudQuota0B9AnalyticsC
+ _symbolic _____XMT 11iCloudQuota0B9AnalyticsC
- GCC_except_table108
- GCC_except_table113
- GCC_except_table27
- GCC_except_table28
- GCC_except_table50
- GCC_except_table58
- GCC_except_table68
- GCC_except_table76
- GCC_except_table93
CStrings:
+ "Cached offer has no quota info dictionary; skipping logging daily quota usage event."
+ "Daily quota usage event already logged today; skipping."
+ "Logging daily quota usage event"
+ "No cached offer available; skipping logging daily quota usage event."
+ "Quota info missing totalQuota/totalUsed; skipping logging daily quota usage event."
+ "Successfully logged daily quota usage event"
+ "com.apple.iCloudNotification.quotaUsageLastLoggedDate"
+ "com.apple.massStorage.iCloudInfo.quotaUsage"
```
