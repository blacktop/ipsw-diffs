## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/Versions/A/iCloudQuota`

```diff

-301.24.0.27.0
-  __TEXT.__text: 0x74fd0
-  __TEXT.__objc_methlist: 0x52ec
+301.24.1.3.0
+  __TEXT.__text: 0x75bbc
+  __TEXT.__objc_methlist: 0x535c
   __TEXT.__const: 0x1370
-  __TEXT.__cstring: 0x4d41
+  __TEXT.__cstring: 0x4d81
   __TEXT.__gcc_except_tab: 0x560
-  __TEXT.__oslogstring: 0x76be
+  __TEXT.__oslogstring: 0x77be
   __TEXT.__dlopen_cstrs: 0x2f9
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x7f8

   __TEXT.__swift_as_cont: 0xe0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x2480
+  __TEXT.__unwind_info: 0x24a8
   __TEXT.__eh_frame: 0x1500
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c18
+  __DATA_CONST.__objc_selrefs: 0x2c50
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x728
-  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__got: 0x720
   __AUTH_CONST.__const: 0x2660
-  __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0xa330
+  __AUTH_CONST.__cfstring: 0x6160
+  __AUTH_CONST.__objc_const: 0xa380
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x948
   __AUTH_CONST.__auth_got: 0xa90
   __AUTH.__objc_data: 0x13f8
   __AUTH.__data: 0x5f0
-  __DATA.__objc_ivar: 0x62c
+  __DATA.__objc_ivar: 0x634
   __DATA.__data: 0x540
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xf40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2906
-  Symbols:   5103
-  CStrings:  1504
+  Functions: 2918
+  Symbols:   5120
+  CStrings:  1512
 
Symbols:
+ +[ICQOffer _appendAdopterBannerSpecificationsFromEntries:source:to:]
+ +[ICQOffer(Internal) adopterBannerSpecificationsFromServerDictionary:]
+ +[_ICQDeviceInfo normalizedPendingItemsCount:]
+ -[ICQCloudStorageDataController reportDeleteWithSuccess:bundleId:completion:]
+ -[ICQOfferManager _debugMockRegularOfferIfEnabled]
+ -[_ICQAlertSpecification messageWithKey:]
+ -[_ICQAlertSpecification titleWithKey:]
+ -[_ICQBannerSpecification appId]
+ GCC_except_table36
+ GCC_except_table42
+ GCC_except_table63
+ GCC_except_table82
+ GCC_except_table84
+ OBJC_IVAR_$__ICQAlertSpecification._messageTemplates
+ OBJC_IVAR_$__ICQAlertSpecification._titleTemplates
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ __77-[ICQCloudStorageDataController reportDeleteWithSuccess:bundleId:completion:]_block_invoke
+ ___77-[ICQCloudStorageDataController reportDeleteWithSuccess:bundleId:completion:]_block_invoke
+ _objc_msgSend$_appendAdopterBannerSpecificationsFromEntries:source:to:
+ _objc_msgSend$_debugMockRegularOfferIfEnabled
+ _objc_msgSend$reportDeleteWithSuccess:forAltDSID:appId:completion:
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
- GCC_except_table35
- GCC_except_table41
- GCC_except_table62
- GCC_except_table81
- GCC_except_table83
CStrings:
+ "Failed to report delete with error: %@"
+ "Reaching out to daemon to report Manage Storage delete for %{public}@."
+ "Returning icqctl debug mock offer for bundle %@: %@"
+ "XPC Error while reaching out to daemon to report delete."
+ "contextBasedMesg"
+ "contextBasedTitle"
+ "debug-mock-offer"
+ "pendingItemsCount %@ is too low, treating as nil"
```
