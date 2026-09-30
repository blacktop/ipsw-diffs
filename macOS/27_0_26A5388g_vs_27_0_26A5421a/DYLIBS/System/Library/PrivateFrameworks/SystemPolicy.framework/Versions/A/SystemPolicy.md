## SystemPolicy

> `/System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy`

```diff

-823.0.3.0.0
-  __TEXT.__text: 0x19378
-  __TEXT.__objc_methlist: 0x19a8
+823.1.1.0.0
+  __TEXT.__text: 0x19520
+  __TEXT.__objc_methlist: 0x19f0
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1825
+  __TEXT.__cstring: 0x1826
   __TEXT.__gcc_except_tab: 0x1bc
   __TEXT.__oslogstring: 0x1544
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf78
+  __DATA_CONST.__objc_selrefs: 0xfa0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x4a0
   __DATA_CONST.__got: 0x2e0
-  __AUTH_CONST.__const: 0x910
+  __AUTH_CONST.__const: 0x930
   __AUTH_CONST.__cfstring: 0x2220
-  __AUTH_CONST.__objc_const: 0x37e0
+  __AUTH_CONST.__objc_const: 0x3818
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x4a0
-  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0x248
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 812
-  Symbols:   1795
+  Functions: 818
+  Symbols:   1804
   CStrings:  460
 
Symbols:
+ -[PolicyScanTarget ensureQuarantineStateChecked]
+ -[PolicyScanTarget quarantineOverrideURL]
+ -[PolicyScanTarget setQuarantineOverrideURL:]
+ -[SPExecutionPolicy purgeUnmountedPolicyScanCacheEntries:]
+ OBJC_IVAR_$_PolicyScanTarget._quarantineOverrideURL
+ ___58-[SPExecutionPolicy purgeUnmountedPolicyScanCacheEntries:]_block_invoke
+ _arrayContainsOnlyURLs
+ _objc_msgSend$ensureQuarantineStateChecked
+ _objc_msgSend$purgeUnmountedPolicyScanCacheEntriesWithReply:
```
