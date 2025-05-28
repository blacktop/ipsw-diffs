## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-528.0.0.0.0
-  __TEXT.__text: 0x2e378
-  __TEXT.__auth_stubs: 0x1490
+528.1.0.0.0
+  __TEXT.__text: 0x2e80c
+  __TEXT.__auth_stubs: 0x14a0
   __TEXT.__const: 0x408
-  __TEXT.__cstring: 0x1bb3
-  __TEXT.__oslogstring: 0x1fa0
-  __TEXT.__dlopen_cstrs: 0x9e
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__cstring: 0x1ca0
+  __TEXT.__oslogstring: 0x1fa7
+  __TEXT.__dlopen_cstrs: 0xdf
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__const: 0x4b8
   __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__const: 0x3e8
-  __AUTH_CONST.__auth_got: 0xa48
-  __DATA.__data: 0x2d8
-  __DATA.__bss: 0x6a9
+  __AUTH_CONST.__auth_got: 0xa50
+  __DATA.__data: 0x2e8
+  __DATA.__bss: 0x6b9
   __DATA_DIRTY.__data: 0x258
   __DATA_DIRTY.__bss: 0x1628
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 628
-  Symbols:   1869
-  CStrings:  463
+  Functions: 633
+  Symbols:   1887
+  CStrings:  475
 
Symbols:
+ _CCHmac
+ __ZGVZL16NetFSLibraryCorePPcE16frameworkLibrary
+ __ZGVZL46getNetFSCopyURLForRemountingVolumeURLSymbolLocvE3ptr
+ __ZL16matchURLPropertyPK7__CFURLPK10__CFStringPKv.cold.1
+ __ZL17audit_stringNetFS
+ __ZN12BookmarkDataC2EPK13__CFAllocatorPK8__CFData.cold.1
+ __ZN19BookmarkMutableData8FinalizeEPKvm
+ __ZN19BookmarkMutableData8FinalizeEPKvm.cold.1
+ __ZZL16NetFSLibraryCorePPcE16frameworkLibrary
+ __ZZL46getNetFSCopyURLForRemountingVolumeURLSymbolLocvE3ptr
+ ____ZL16NetFSLibraryCorePPc_block_invoke
+ ____ZL46getNetFSCopyURLForRemountingVolumeURLSymbolLocv_block_invoke
+ ___block_descriptor_tmp.19
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.7
+ ___block_literal_global.22
- __ZN19BookmarkMutableData8FinalizeEv
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.26
- ___block_literal_global.18
CStrings:
+ "%s: %s"
+ "BookmarkData"
+ "BookmarkData.cpp"
+ "Finalize"
+ "NetFSCopyURLForRemountingVolumeURL"
+ "invalid TOC: cycle"
+ "invalid bookmark length"
+ "invalid data item pointer"
+ "invalid data section length"
+ "invalid header"
+ "scopeKeyLength == kBookmarkSecurityScopeCookieSize"
+ "softlink:r:path:/System/Library/Frameworks/NetFS.framework/NetFS"

```
