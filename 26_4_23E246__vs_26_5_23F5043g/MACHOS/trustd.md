## trustd

> `/usr/libexec/trustd`

```diff

-61901.102.2.0.0
-  __TEXT.__text: 0x687a0
-  __TEXT.__auth_stubs: 0x23f0
-  __TEXT.__objc_stubs: 0x3120
-  __TEXT.__objc_methlist: 0xd3c
-  __TEXT.__const: 0x5cb1
+61901.120.36.0.3
+  __TEXT.__text: 0x69658
+  __TEXT.__auth_stubs: 0x2450
+  __TEXT.__objc_stubs: 0x3160
+  __TEXT.__objc_methlist: 0xd54
+  __TEXT.__const: 0x5ab1
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__gcc_except_tab: 0xc90
-  __TEXT.__cstring: 0x7354
-  __TEXT.__oslogstring: 0x66a1
+  __TEXT.__gcc_except_tab: 0xc20
+  __TEXT.__cstring: 0x739c
+  __TEXT.__oslogstring: 0x6736
   __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x3016
-  __TEXT.__objc_methtype: 0xc64
-  __TEXT.__unwind_info: 0x1168
-  __DATA_CONST.__auth_got: 0x1208
-  __DATA_CONST.__got: 0x7c0
+  __TEXT.__objc_methname: 0x3030
+  __TEXT.__objc_methtype: 0xc75
+  __TEXT.__unwind_info: 0x1178
+  __DATA_CONST.__auth_got: 0x1238
+  __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x4ed0
-  __DATA_CONST.__cfstring: 0x6820
+  __DATA_CONST.__const: 0x4f10
+  __DATA_CONST.__cfstring: 0x6860
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA.__objc_const: 0x1710
-  __DATA.__objc_selrefs: 0xde8
-  __DATA.__objc_ivar: 0xd8
+  __DATA.__objc_const: 0x16e0
+  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x420
-  __DATA.__bss: 0x540
+  __DATA.__data: 0x428
+  __DATA.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 65DB3B96-895B-3EF7-8E12-3678E89EC5AA
-  Functions: 1335
-  Symbols:   841
-  CStrings:  3216
+  UUID: B5C7B4E8-8044-3972-9E4C-0F06E288E6D6
+  Functions: 1344
+  Symbols:   849
+  CStrings:  3228
 
Symbols:
+ _CFDictionaryCreateCopy
+ _SecAreQARootCertificatesEnabled
+ ___NSArray0__struct
+ __os_activity_create
+ __os_activity_current
+ _os_activity_scope_enter
+ _os_activity_scope_leave
+ _securityd_send_sync_and_do
CStrings:
+ "@40@0:8@16@24@32"
+ "B24@?0^v8^^{__CFError}16"
+ "CRLite: certificate is %s"
+ "CopyAppleAnchors"
+ "Failed to copy apple anchors: %@"
+ "Failed to evaluate CRLite certificate revocation status against filter %lld: %@"
+ "Falling back to built-in anchors"
+ "Found test anchor type for %@; not allowed on prod system"
+ "SELECT filterid FROM crlitefiltercoverage WHERE logid=?1 AND ?2 >= start AND ?2 <= end ORDER BY generatedat"
+ "SecTrustCopyAppleTrustAnchors"
+ "Using system trust store %llu"
+ "_SecRevocationDbCRLiteMergeCoveringFilter failed: %@"
+ "addEntriesFromDictionary:"
+ "anchorRecordsForLookupKey:"
+ "anchorRecordsForLookupKey:hash:hashKey:"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/7829CA60-F7EB-4500-BF75-00494D53CAFB/TemporaryDirectory.TRhBEk/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "copyCertForAppleCertHash:"
+ "failed to convert string for key %s to utf8"
+ "loadBuiltInAppleAnchors"
+ "notRevoked"
- "Failed to evaluate CRLite certificate revocation status against filter %ld: %@"
- "Malformed anchor records for %{public}@, not an array"
- "SELECT filterid,generatedat FROM crlitefiltercoverage WHERE logid=?1 AND ?2 >= start AND ?2 <= end ORDER BY generatedat DESC LIMIT 1"
- "T@\"NSMutableDictionary\",&,V_built_in_anchors"
- "_SecRevocationDbCRLiteGetMostRecentCoveringFilter failed: %@"
- "_built_in_anchors"
- "arrayWithArray:"
- "built_in_anchors"
- "com.apple.security.file./Library/Caches/com.apple.xbs/19F1A4C1-4FFA-4630-A5B9-DCC6A0FB228D/TemporaryDirectory.aGwbio/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "setBuilt_in_anchors:"

```
