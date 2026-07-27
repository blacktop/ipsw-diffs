## storeuid

> `/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/Current/Resources/storeuid.app/Contents/MacOS/storeuid`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 716.4.2.0.0
-  __TEXT.__text: 0xa750
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x2000
+  __TEXT.__text: 0xae58
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_stubs: 0x2060
   __TEXT.__objc_methlist: 0xf1c
-  __TEXT.__cstring: 0x194c
-  __TEXT.__objc_methname: 0x33f4
+  __TEXT.__cstring: 0x1b6e
+  __TEXT.__objc_methname: 0x3440
   __TEXT.__objc_classname: 0x2e6
   __TEXT.__objc_methtype: 0x1b1d
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x58
   __TEXT.__oslogstring: 0x56b
   __TEXT.__gcc_except_tab: 0x1b0
   __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x838
-  __DATA_CONST.__cfstring: 0x1080
+  __DATA_CONST.__cfstring: 0x11e0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x2cc8
-  __DATA.__objc_selrefs: 0xd78
+  __DATA.__objc_selrefs: 0xd90
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x720

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 207
-  Symbols:   163
-  CStrings:  909
+  Symbols:   165
+  CStrings:  923
 
Symbols:
+ _sqlite3_column_double
+ _sqlite3_column_text
Functions:
~ sub_100004798 : 880 -> 2680
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NAlRXY/Sources/Commerce/CommerceKit/UIService/AppStoreXPC.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NAlRXY/Sources/Commerce/CommerceKit/UIService/InAppService/StoreReviewController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NAlRXY/Sources/Commerce/CommerceKit/UIService/UIServiceInterface.m"
+ "Error fetching app review bag values - %@"
+ "Review request denied for %@. Already reviewed."
+ "Review request denied for %@. Could not validate request - %s"
+ "Review request denied for %@. Primary account: %@."
+ "Review request denied for %@. Too many requests."
+ "Review request denied for %@. Version was reviewed."
+ "SELECT bundle_version, reviewed, timestamp FROM review_request WHERE bundle_id = ? ORDER BY timestamp DESC;"
+ "bagValuesForKeys:error:"
+ "dateWithTimeIntervalSinceNow:"
+ "inAppReviewRequestLimitWindow"
+ "inAppReviewRequestsPerWindow"
+ "inAppReviewRequireNewVersionAfterReview"
+ "inAppReviewRequiredDaysAfterReview"
+ "timeIntervalSince1970"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lMb0UV/Sources/Commerce/CommerceKit/UIService/AppStoreXPC.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lMb0UV/Sources/Commerce/CommerceKit/UIService/InAppService/StoreReviewController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lMb0UV/Sources/Commerce/CommerceKit/UIService/UIServiceInterface.m"
```
