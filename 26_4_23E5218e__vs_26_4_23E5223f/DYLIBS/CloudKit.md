## CloudKit

> `/System/Library/Frameworks/CloudKit.framework/CloudKit`

```diff

-2350.31.0.0.0
-  __TEXT.__text: 0x300374
-  __TEXT.__auth_stubs: 0x4000
-  __TEXT.__objc_methlist: 0x2062c
+2350.33.0.0.0
+  __TEXT.__text: 0x300678
+  __TEXT.__auth_stubs: 0x3ff0
+  __TEXT.__objc_methlist: 0x20674
   __TEXT.__const: 0x8988
   __TEXT.__dlopen_cstrs: 0x13c
   __TEXT.__constg_swiftt: 0x1e14

   __TEXT.__swift5_fieldmd: 0x195c
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x430
-  __TEXT.__cstring: 0x1f871
+  __TEXT.__cstring: 0x1f667
   __TEXT.__swift5_proto: 0x4fc
   __TEXT.__swift5_types: 0x238
   __TEXT.__swift5_capture: 0x1df0
-  __TEXT.__swift_as_entry: 0x4a4
-  __TEXT.__swift_as_ret: 0x58c
-  __TEXT.__oslogstring: 0x15dcd
+  __TEXT.__swift_as_entry: 0x4a8
+  __TEXT.__swift_as_ret: 0x594
+  __TEXT.__oslogstring: 0x15e0c
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__gcc_except_tab: 0xaf68
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0xece0
-  __TEXT.__eh_frame: 0xaaf4
+  __TEXT.__unwind_info: 0xed00
+  __TEXT.__eh_frame: 0xaaac
   __TEXT.__objc_classname: 0x48b7
-  __TEXT.__objc_methname: 0x40c3d
-  __TEXT.__objc_methtype: 0x77d8
-  __TEXT.__objc_stubs: 0x23060
+  __TEXT.__objc_methname: 0x40cdd
+  __TEXT.__objc_methtype: 0x7825
+  __TEXT.__objc_stubs: 0x23100
   __DATA_CONST.__got: 0x16e8
   __DATA_CONST.__const: 0x6bb8
   __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x428
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbae0
+  __DATA_CONST.__objc_selrefs: 0xbb10
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0xe58
   __DATA_CONST.__objc_arraydata: 0x600
-  __AUTH_CONST.__auth_got: 0x2018
+  __AUTH_CONST.__auth_got: 0x2010
   __AUTH_CONST.__const: 0xb760
-  __AUTH_CONST.__cfstring: 0x1cf80
+  __AUTH_CONST.__cfstring: 0x1cfa0
   __AUTH_CONST.__objc_const: 0x37b70
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x330

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2B78080C-1F41-3C4D-98C0-F732276EF38A
-  Functions: 20366
-  Symbols:   5307
-  CStrings:  20783
+  UUID: 2FE53B1E-2E2C-3FC0-AAED-A1DF7E26ACEC
+  Functions: 20372
+  Symbols:   5306
+  CStrings:  20796
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "CKSQLiteDatabase<%p>: getxattr() failed fetching %s at path: %s. error = %s"
+ "CKSQLiteDatabase<%p>: setxattr() failed setting %s at path: %s. error = %s"
+ "CKSQLiteDatabaseLastSuccessfulOpenDate"
+ "CKSQLiteDatabaseOpenAttemptCount"
+ "Database open crash loop detected at path: %s"
+ "lastSuccessfulOpenDate:"
+ "openAttemptCountAtPath:"
+ "q24@0:8r*16"
+ "q32@0:8r*16r*24"
+ "setLastSuccessfulOpenDate:dbPath:"
+ "setOpenAttemptCount:dbPath:"
+ "setValue:forAttribute:atPath:"
+ "v32@0:8@16r*24"
+ "v32@0:8q16r*24"
+ "v40@0:8q16r*24r*32"
+ "valueForAttribute:atPath:"
- "/AppleInternal/Library/BuildRoots/4~CI7TugA0vnH0o816zwITOU48e_MNbr-fy9Lh3Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7TugA0vnH0o816zwITOU48e_MNbr-fy9Lh3Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "CKSQLiteDatabase<%p>: getxattr() failed checking for open crash at path: %s. error = %s"
- "CKSQLiteDatabaseIsOpening"

```
