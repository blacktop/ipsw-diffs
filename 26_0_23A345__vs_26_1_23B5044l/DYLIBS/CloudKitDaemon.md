## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2300.147.3.1.0
-  __TEXT.__text: 0x39a82c
+2320.11.0.0.0
+  __TEXT.__text: 0x39ac74
   __TEXT.__auth_stubs: 0x4030
-  __TEXT.__objc_methlist: 0x2f5ac
-  __TEXT.__const: 0x4068
+  __TEXT.__objc_methlist: 0x2f5f4
+  __TEXT.__const: 0x4058
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0x1d68
-  __TEXT.__oslogstring: 0x2e983
+  __TEXT.__oslogstring: 0x2ea42
   __TEXT.__swift5_capture: 0x6a0
-  __TEXT.__cstring: 0x286d3
+  __TEXT.__cstring: 0x286c1
   __TEXT.__constg_swiftt: 0x19b8
   __TEXT.__swift5_reflstr: 0x1059
   __TEXT.__swift5_fieldmd: 0x11e0

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xd820
+  __TEXT.__gcc_except_tab: 0xd8b0
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xc028
+  __TEXT.__unwind_info: 0xc030
   __TEXT.__eh_frame: 0x30e0
-  __TEXT.__objc_classname: 0x554e
-  __TEXT.__objc_methname: 0x5aa6b
-  __TEXT.__objc_methtype: 0x8b97
-  __TEXT.__objc_stubs: 0x38620
-  __DATA_CONST.__got: 0x1c60
+  __TEXT.__objc_classname: 0x556a
+  __TEXT.__objc_methname: 0x5aab7
+  __TEXT.__objc_methtype: 0x8bcf
+  __TEXT.__objc_stubs: 0x38640
+  __DATA_CONST.__got: 0x1c80
   __DATA_CONST.__const: 0x8c58
   __DATA_CONST.__objc_classlist: 0x1450
   __DATA_CONST.__objc_catlist: 0x138
-  __DATA_CONST.__objc_protolist: 0x210
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x12078
   __DATA_CONST.__objc_protorefs: 0xa0

   __AUTH_CONST.__auth_got: 0x2028
   __AUTH_CONST.__const: 0x4aa8
   __AUTH_CONST.__cfstring: 0x21300
-  __AUTH_CONST.__objc_const: 0x47e38
+  __AUTH_CONST.__objc_const: 0x47f28
   __AUTH_CONST.__objc_intobj: 0xc18
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0xb90
   __AUTH.__objc_data: 0x58c8
   __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0x180c
-  __DATA.__data: 0x3c10
+  __DATA.__objc_ivar: 0x181c
+  __DATA.__data: 0x3c70
   __DATA.__bss: 0x2f40
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x1940
+  __DATA_DIRTY.__objc_ivar: 0x1944
   __DATA_DIRTY.__objc_data: 0x78e0
   __DATA_DIRTY.__data: 0x1fb0
   __DATA_DIRTY.__bss: 0x3768

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 45E785AA-D228-37B4-AB16-70C3CB75787D
-  Functions: 19615
-  Symbols:   2728
-  CStrings:  27794
+  UUID: 5A6AC42E-ABB0-330B-BFD3-29C42D8D6434
+  Functions: 19619
+  Symbols:   2732
+  CStrings:  27803
 
Symbols:
+ _CKTestDeviceOptionFakeAccountChangeOnAccountReload
+ _kCKAccountIDChangedPerContainerNewAccountIDKey
+ _kCKAccountIDChangedPerContainerNotificationKey
+ _kCKAccountIDChangedPerContainerOldAccountIDKey
CStrings:
+ "(Cached) Walrus enabled for account with ID %@"
+ "@\"CKAssetDownloadPreauthorization\"16@0:8"
+ "@\"NSURL\"16@0:8"
+ "CKDMMCSItemGroupEquality"
+ "CKNoFollowFileURL"
+ "Cancelling operation %@ because the underlying account changed from %@ to %@"
+ "Not cancelling operation %@ because we are targeting the publicDB and adopter prefers anonymous requests."
+ "T@\"CKAssetDownloadPreauthorization\",R,N,V_downloadPreauthorization"
+ "T@\"NSMutableSet\",R,N,V_itemsGroups"
+ "T@\"NSString\",R,N,V_owner"
+ "T@\"NSString\",R,N,V_requestor"
+ "T@\"NSURL\",R,N,V_contentBaseURL"
+ "T@,&,N,V_accountChangeObserver"
+ "TB,R,N,GisAnonymous"
+ "_accountChangeObserver"
+ "_cachedHash"
+ "_itemsGroups"
+ "_lastGroup"
+ "accountChangeObserver"
+ "allItemGroups.count == 1"
+ "hashOfItem:"
+ "initWithItem:"
+ "item:matchesItem:"
+ "itemsGroups"
+ "member:"
+ "putItemGroupSet.itemsGroups.count == 1"
+ "setAccountChangeObserver:"
+ "v24@?0@\"CKDMMCSItemGroup\"8^B16"
- "Error getting cached walrus status. %@"
- "T@\"CKAssetDownloadPreauthorization\",R,N"
- "T@\"NSArray\",&,N,V_tuple"
- "T@\"NSMutableDictionary\",&,N,V_itemsByGroupTuple"
- "T@\"NSOperationQueue\",R,N,V_concurrencyThrottleQueue"
- "_concurrencyThrottleQueue"
- "_itemsByGroupTuple"
- "_tuple"
- "concurrencyThrottleQueue"
- "initWithTuple:"
- "itemGroupSet.allItemGroups.count == 1"
- "itemsByGroupTuple"
- "putItemGroupSet.allItemGroups.count == 1"
- "scheduleOperation:block:"
- "setItemsByGroupTuple:"
- "setTuple:"
- "tuple"
- "tupleForItem:"
- "v32@?0@8@\"CKDMMCSItemGroup\"16^B24"

```
