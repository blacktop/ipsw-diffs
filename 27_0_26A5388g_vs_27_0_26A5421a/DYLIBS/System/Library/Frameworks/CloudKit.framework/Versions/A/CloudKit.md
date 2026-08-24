## CloudKit

> `/System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit`

```diff

-2710.116.0.0.0
-  __TEXT.__text: 0x38a8b4
-  __TEXT.__objc_methlist: 0x218ac
-  __TEXT.__const: 0xe398
+2710.120.0.0.0
+  __TEXT.__text: 0x38d344
+  __TEXT.__objc_methlist: 0x2194c
+  __TEXT.__const: 0xe3a8
   __TEXT.__dlopen_cstrs: 0x13c
-  __TEXT.__swift5_typeref: 0x6be2
-  __TEXT.__swift5_capture: 0x3b14
-  __TEXT.__cstring: 0x21328
-  __TEXT.__constg_swiftt: 0x2924
-  __TEXT.__swift5_reflstr: 0x1d7f
-  __TEXT.__swift5_fieldmd: 0x2538
+  __TEXT.__swift5_typeref: 0x6c00
+  __TEXT.__swift5_capture: 0x3b54
+  __TEXT.__cstring: 0x2147c
+  __TEXT.__constg_swiftt: 0x293c
+  __TEXT.__swift5_reflstr: 0x1d9f
+  __TEXT.__swift5_fieldmd: 0x2544
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_assocty: 0x5c8
   __TEXT.__swift5_proto: 0x858
   __TEXT.__swift5_types: 0x354
-  __TEXT.__swift_as_entry: 0x758
-  __TEXT.__swift_as_ret: 0x87c
-  __TEXT.__swift_as_cont: 0xe5c
-  __TEXT.__oslogstring: 0x16bb8
+  __TEXT.__swift_as_entry: 0x75c
+  __TEXT.__swift_as_ret: 0x880
+  __TEXT.__swift_as_cont: 0xe68
+  __TEXT.__oslogstring: 0x16f8d
   __TEXT.__swift5_mpenum: 0x60
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__gcc_except_tab: 0xacdc
+  __TEXT.__gcc_except_tab: 0xad30
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x11988
-  __TEXT.__eh_frame: 0x10454
+  __TEXT.__unwind_info: 0x119e0
+  __TEXT.__eh_frame: 0x104fc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x29d8
+  __DATA_CONST.__const: 0x29e8
   __DATA_CONST.__objc_classlist: 0x1090
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x478
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf28
+  __DATA_CONST.__objc_selrefs: 0xbf80
   __DATA_CONST.__objc_protorefs: 0x198
-  __DATA_CONST.__objc_superrefs: 0xe78
+  __DATA_CONST.__objc_superrefs: 0xe80
   __DATA_CONST.__objc_arraydata: 0x688
   __DATA_CONST.__got: 0x1970
-  __AUTH_CONST.__const: 0x17090
-  __AUTH_CONST.__cfstring: 0x1ddc0
-  __AUTH_CONST.__objc_const: 0x39b00
+  __AUTH_CONST.__const: 0x171b0
+  __AUTH_CONST.__cfstring: 0x1df20
+  __AUTH_CONST.__objc_const: 0x39b80
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0xc60
+  __AUTH_CONST.__objc_intobj: 0xc78
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__auth_got: 0x2308

   __AUTH.__data: 0x1080
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
-  __DATA.__objc_ivar: 0x1978
+  __DATA.__objc_ivar: 0x1980
   __DATA.__data: 0x6028
   __DATA.__bss: 0xe648
   __DATA.__common: 0x7e8
   __DATA_DIRTY.__objc_ivar: 0xb30
   __DATA_DIRTY.__objc_data: 0x4aa8
-  __DATA_DIRTY.__data: 0x10e0
-  __DATA_DIRTY.__bss: 0xe90
+  __DATA_DIRTY.__data: 0x1100
+  __DATA_DIRTY.__bss: 0xeb0
   __DATA_DIRTY.__common: 0x111
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24394
-  Symbols:   6440
-  CStrings:  6222
+  Functions: 24445
+  Symbols:   6445
+  CStrings:  6251
 
Symbols:
+ _$sSo11CKContainerC8CloudKitE25fetchOrgAdminUserRecordIDSo08CKRecordI0CSgyYaKF
+ _$sSo11CKContainerC8CloudKitE25fetchOrgAdminUserRecordIDSo08CKRecordI0CSgyYaKFTu
+ _CKCurrentProcessIsContainerized
+ _CKDataFromFileAtPathWithAttributes
+ _CKSQLiteContainerAttribution_AgentSessionStoreSecure
CStrings:
+ "%s credentials are valid again. Scheduling sync."
+ "%s setting isWaitingForValidCredentials from last error"
+ "AccountInfoCache.archive"
+ "AgentSessionStoreSecure"
+ "CKSQLiteContainerAttribution_AgentSessionStoreSecure"
+ "Cleared in-memory account info cache."
+ "Containers"
+ "Could not locate caches directory for account info cache: %@"
+ "Could not read account info validation counter. This process may need to add (allow user-preference-read (preference-domain \"com.apple.CloudKit\")) to its sandbox profile to avoid a performance issue."
+ "Failed to read account info cache file %@: %@"
+ "Failed to remove account info cache directory %@: %@"
+ "Failed to remove account info cache file %@: %@"
+ "Failed to unarchive account info cache (archive length %lu): %@"
+ "Failed to write account info cache file %@ %@ after recreating its directory with error %@"
+ "Failed to write account info cache file %@ %@: %@"
+ "Failed to write account info cache file %@ with error %@ %@. Could not recreate its directory: %@"
+ "FrameworkCachesDirectory"
+ "Malformed package archive"
+ "Missing package archive"
+ "Obsolete package archive"
+ "Read account info from %{public}@ cache."
+ "Received updated framework cache directory from cloudd %@"
+ "Removed account info cache directory %@"
+ "Removed legacy CloudKitAccountInfoCache user-defaults entry."
+ "Skipping account info cache write: setup hash is nil or empty."
+ "Waiting for valid credentials"
+ "Wrote account info cache file %@ %@"
+ "Wrote account info cache file %@ %@ after recreating its directory"
+ "com.apple.agentsessionstore.secure"
+ "com.apple.cloudkit.CKAccountInfoFIOQueue"
+ "fetchOrgAdminUserRecordID()"
+ "globally"
+ "in the data container"
+ "in-memory"
+ "on-disk"
- "CKAccountInfoCacheReset"
- "Cleared account info cache."
- "Could not validate account info cache. This process may need to add (allow user-preference-read (preference-domain \"com.apple.CloudKit\")) to its sandbox profile to avoid a performance issue."
- "Failed to unarchive account info cache: %@"
- "Unknown error unarchiving CKPackage"
- "a"
```
