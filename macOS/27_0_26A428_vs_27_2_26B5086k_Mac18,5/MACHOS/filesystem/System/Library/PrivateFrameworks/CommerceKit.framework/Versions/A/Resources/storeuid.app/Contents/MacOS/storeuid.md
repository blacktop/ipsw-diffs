## storeuid

> `/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/Resources/storeuid.app/Contents/MacOS/storeuid`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-717.0.7.0.0
-  __TEXT.__text: 0xa5d4
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0x2080
+717.1.1.0.0
+  __TEXT.__text: 0x9f2c
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0x2020
   __TEXT.__objc_methlist: 0xf2c
-  __TEXT.__cstring: 0x1c99
-  __TEXT.__objc_methname: 0x3495
+  __TEXT.__cstring: 0x1a77
+  __TEXT.__objc_methname: 0x3449
   __TEXT.__objc_classname: 0x2d9
   __TEXT.__objc_methtype: 0x1b94
-  __TEXT.__const: 0x58
+  __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0x56b
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__unwind_info: 0x3a0
   __DATA_CONST.__const: 0x838
-  __DATA_CONST.__cfstring: 0x1220
+  __DATA_CONST.__cfstring: 0x10c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2d10
-  __DATA.__objc_selrefs: 0xda0
+  __DATA.__objc_selrefs: 0xd88
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x720

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 208
-  Symbols:   170
-  CStrings:  933
+  Symbols:   168
+  CStrings:  919
 
Symbols:
- _sqlite3_column_double
- _sqlite3_column_text
Functions:
~ sub_1000042d0 : 2516 -> 812
CStrings:
- "Error fetching app review bag values - %@"
- "Review request denied for %@. Already reviewed."
- "Review request denied for %@. Could not validate request - %s"
- "Review request denied for %@. Primary account: %@."
- "Review request denied for %@. Too many requests."
- "Review request denied for %@. Version was reviewed."
- "SELECT bundle_version, reviewed, timestamp FROM review_request WHERE bundle_id = ? ORDER BY timestamp DESC;"
- "bagValuesForKeys:error:"
- "dateWithTimeIntervalSinceNow:"
- "inAppReviewRequestLimitWindow"
- "inAppReviewRequestsPerWindow"
- "inAppReviewRequireNewVersionAfterReview"
- "inAppReviewRequiredDaysAfterReview"
- "timeIntervalSince1970"
```
