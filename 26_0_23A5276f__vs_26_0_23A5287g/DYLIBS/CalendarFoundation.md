## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation`

```diff

-1599.0.0.0.0
-  __TEXT.__text: 0x5bb1c
+1601.0.0.0.0
+  __TEXT.__text: 0x5beac
   __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_methlist: 0x5c34
+  __TEXT.__objc_methlist: 0x5c4c
   __TEXT.__cstring: 0x6692
-  __TEXT.__const: 0x3c4
+  __TEXT.__const: 0x3d4
   __TEXT.__gcc_except_tab: 0xb58
-  __TEXT.__oslogstring: 0x381c
+  __TEXT.__oslogstring: 0x384c
   __TEXT.__ustring: 0x2d8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x36

   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1a18
+  __TEXT.__unwind_info: 0x1a20
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0xba5
-  __TEXT.__objc_methname: 0xe910
+  __TEXT.__objc_methname: 0xe95f
   __TEXT.__objc_methtype: 0x16ad
-  __TEXT.__objc_stubs: 0xa9e0
+  __TEXT.__objc_stubs: 0xaa20
   __DATA_CONST.__got: 0x838
   __DATA_CONST.__const: 0x17d8
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40f8
+  __DATA_CONST.__objc_selrefs: 0x4110
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x100

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F751F62D-E95A-31F8-8071-AE9386B0CCCE
-  Functions: 2527
-  Symbols:   8601
-  CStrings:  5588
+  UUID: 6A74C337-3630-3298-9B69-CFDDBE911CB4
+  Functions: 2529
+  Symbols:   8607
+  CStrings:  5591
 
Symbols:
+ -[CalAccountsProvider allAccountsFromAllTypesWithError:]
+ -[CalAccountsProvider providerForCalDAVAccount:]
+ -[CalAccountsProvider topLevelAccountsWithUsername:]
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table47
+ _objc_msgSend$allAccountTypes
+ _objc_msgSend$allAccountsFromAllTypesWithError:
- -[CalAccountsProvider _providerForCalDAVAccount:]
Functions:
+ -[CalAccountsProvider topLevelAccountsWithUsername:]
+ -[CalAccountsProvider allAccountsFromAllTypesWithError:]
~ ___113+[CalLocationPrediction predictedLocationOfInterestForEventTitle:eventLocation:calendarIdentifier:timeout:error:]_block_invoke.cold.1 : 208 -> 212
~ ___113+[CalLocationPrediction predictedLocationOfInterestForEventTitle:eventLocation:calendarIdentifier:timeout:error:]_block_invoke.cold.2 : 180 -> 184
~ ___113+[CalLocationPrediction predictedLocationOfInterestForEventTitle:eventLocation:calendarIdentifier:timeout:error:]_block_invoke.cold.3 : 148 -> 152
CStrings:
+ "%lu locations of interest found for title %{private}@, location: %{private}@, calendar: %@"
+ "Error fetching locations of interest for title %{private}@, location: %{private}@, calendar: %@: %@"
+ "No locations of interest found for title %{private}@, location: %{private}@, calendar: %@"
+ "allAccountTypes"
+ "allAccountsFromAllTypesWithError:"
+ "providerForCalDAVAccount:"
+ "topLevelAccountsWithUsername:"
- "%lu locations of interest found for title %@, location: %@, calendar: %@"
- "Error fetching locations of interest for title %@, location: %@, calendar: %@: %@"
- "No locations of interest found for title %@, location: %@, calendar: %@"
- "_providerForCalDAVAccount:"

```
