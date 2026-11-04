## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-446.0.4.0.0
-  __TEXT.__text: 0x6fa48
+447.0.1.0.0
+  __TEXT.__text: 0x70dec
   __TEXT.__auth_stubs: 0x1710
-  __TEXT.__objc_stubs: 0x38c0
-  __TEXT.__objc_methlist: 0x2524
-  __TEXT.__cstring: 0xa5e3
-  __TEXT.__objc_methname: 0x61df
+  __TEXT.__objc_stubs: 0x3940
+  __TEXT.__objc_methlist: 0x2534
+  __TEXT.__cstring: 0xa713
+  __TEXT.__objc_methname: 0x623f
   __TEXT.__objc_classname: 0x357
-  __TEXT.__objc_methtype: 0x1975
-  __TEXT.__const: 0x762
-  __TEXT.__gcc_except_tab: 0x1c10
-  __TEXT.__oslogstring: 0xb183
+  __TEXT.__objc_methtype: 0x19d5
+  __TEXT.__const: 0x772
+  __TEXT.__gcc_except_tab: 0x1db8
+  __TEXT.__oslogstring: 0xb45e
   __TEXT.__swift5_typeref: 0x4c2
   __TEXT.__swift5_capture: 0x418
   __TEXT.__swift5_fieldmd: 0xac

   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x154
-  __TEXT.__unwind_info: 0x21c8
+  __TEXT.__unwind_info: 0x2220
   __TEXT.__eh_frame: 0x15c8
-  __DATA_CONST.__const: 0x18e0
-  __DATA_CONST.__cfstring: 0x1c80
+  __DATA_CONST.__const: 0x19c0
+  __DATA_CONST.__cfstring: 0x1ca0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x138
   __DATA.__objc_const: 0x3118
-  __DATA.__objc_selrefs: 0x13a8
+  __DATA.__objc_selrefs: 0x13c0
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x600
   __DATA.__data: 0x700

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1850
+  Functions: 1859
   Symbols:   567
-  CStrings:  2851
+  CStrings:  2870
 
CStrings:
+ "%s : %d: malformed xp key in TXT record for server :%@, expected %d bytes but got %lu, skipping."
+ "%s : %d: network name :%@ matches with mdns record :%@, but xpanid :%@ differs from :%@"
+ "%s : %d: no xp key in TXT record for server :%@, continue to next network if available."
+ "%s : %d: xpanid :%@ matches with mdns record :%@"
+ "%s:%d: Entered. Matching records (%lu) with Mdns records, policy :%lu"
+ "%s:%d: Failed to allocate matchedRecords"
+ "%s:%d: record for network %@ already matched by earlier border router, skipping"
+ "-[THThreadNetworkCredentialsKeychainBackingStore getActiveRecords:matchPolicy:]"
+ "@32@0:8@16Q24"
+ "B24@?0@\"THThreadNetworkCredentialsActiveDataSetRecord\"8@\"THThreadNetworkCredentialsActiveDataSetRecord\"16"
+ "CTCS:Dedupic logic will not kick in, only %lu record(s) provided"
+ "CTCS:collapsed %lu active record(s) into %lu, skipped %lu record(s) (no extended PAN ID or name)"
+ "CTCS:dropping network %@, with no extended PAN ID or name"
+ "CTCS:no preferred network for nearby flag:err=%@"
+ "CTCS:preferred network fetch failed:err=%@"
+ "Failed to get active credentials for nearby networks; Backing store is nil"
+ "arrayWithObjects:count:"
+ "dictionaryWithCapacity:"
+ "getActiveRecords:matchPolicy:"
+ "q24@?0@\"NSDate\"8@\"NSDate\"16"
+ "retrieveActiveAndPreferredRecordsWithCompletion:"
+ "v24@0:8@?<v@?@\"NSSet\"@\"THThreadNetworkCredentialsActiveDataSetRecord\"@\"NSError\">16"
+ "v32@?0@\"NSSet\"8@\"THThreadNetworkCredentialsActiveDataSetRecord\"16@\"NSError\"24"
- "%s:%d: Entered. Matching records (%lu) with Mdns records"
- "%s:%d: Failed to allocate recordList"
- "-[THThreadNetworkCredentialsKeychainBackingStore getActiveRecords:]"
- "getActiveRecords:"
```
