## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4025.110.2.0.0
-  __TEXT.__text: 0x145278
+4025.200.12.0.0
+  __TEXT.__text: 0x145f68
   __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x156a0
-  __TEXT.__objc_methlist: 0xb414
+  __TEXT.__objc_stubs: 0x15700
+  __TEXT.__objc_methlist: 0xb47c
   __TEXT.__dlopen_cstrs: 0x705
   __TEXT.__const: 0x4f0
-  __TEXT.__oslogstring: 0x29742
-  __TEXT.__cstring: 0x10a65
-  __TEXT.__objc_methname: 0x21b12
+  __TEXT.__oslogstring: 0x297fe
+  __TEXT.__cstring: 0x10b5b
+  __TEXT.__objc_methname: 0x21b9c
   __TEXT.__constg_swiftt: 0x98
   __TEXT.__swift5_typeref: 0x9c
   __TEXT.__swift5_reflstr: 0x27

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__gcc_except_tab: 0x595c
+  __TEXT.__gcc_except_tab: 0x59d4
   __TEXT.__objc_classname: 0x2668
   __TEXT.__objc_methtype: 0x463e
-  __TEXT.__unwind_info: 0x3ae8
+  __TEXT.__unwind_info: 0x3b20
   __TEXT.__eh_frame: 0x3e0
   __DATA_CONST.__auth_got: 0xae8
   __DATA_CONST.__got: 0x1048
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x5f40
-  __DATA_CONST.__cfstring: 0xc2e0
+  __DATA_CONST.__const: 0x60a8
+  __DATA_CONST.__cfstring: 0xc300
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_intobj: 0xee8
-  __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__objc_arrayobj: 0x288
+  __DATA_CONST.__objc_intobj: 0xf18
+  __DATA_CONST.__objc_arraydata: 0x2b8
+  __DATA_CONST.__objc_arrayobj: 0x2a0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA.__objc_const: 0x16038
-  __DATA.__objc_selrefs: 0x65c8
+  __DATA.__objc_selrefs: 0x65e0
   __DATA.__objc_ivar: 0xe2c
   __DATA.__objc_data: 0x52f8
   __DATA.__data: 0x1228
-  __DATA.__bss: 0x4d0
+  __DATA.__bss: 0x560
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 281F7CC6-233B-3126-A011-28D8E2AA4199
-  Functions: 5067
-  Symbols:   923
-  CStrings:  10886
+  UUID: E847586C-60A4-3F96-8531-7E3B1DE1AD05
+  Functions: 5090
+  Symbols:   922
+  CStrings:  10894
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCoreImage
CStrings:
+ "Adding pending change to favorite track with persistentID=%lld, storeID=%lld, subscriptionStoreID=%lld"
+ "Error setting liked state changed dates for %d trackPIDS"
+ "Migrating to version 710000"
+ "SELECT item_pid, store_item_id, subscription_store_item_id FROM item JOIN item_store USING(item_pid) JOIN item_stats USING(item_pid) WHERE in_my_library AND liked_state=? AND liked_state_changed_date=? AND store_saga_id=? AND media_type IN (?,?)"
+ "_supportedInterfaceForCloudServerListenerXPCConnection"
+ "_supportedInterfaceForCloudServerXPCConnection"
+ "_supportedInterfaceForXPCConnection"

```
