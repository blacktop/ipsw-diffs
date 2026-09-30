## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-3860.400.51.0.0
-  __TEXT.__text: 0x85e8c
-  __TEXT.__auth_stubs: 0x10c0
+3860.500.83.0.0
+  __TEXT.__text: 0x8a9d8
+  __TEXT.__auth_stubs: 0x10a0
   __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_stubs: 0xa800
+  __TEXT.__objc_stubs: 0xa840
   __TEXT.__objc_methlist: 0x61b4
   __TEXT.__const: 0x278
-  __TEXT.__gcc_except_tab: 0x10858
-  __TEXT.__cstring: 0x3982
-  __TEXT.__objc_methname: 0xf12e
+  __TEXT.__gcc_except_tab: 0x10934
+  __TEXT.__cstring: 0x39b3
+  __TEXT.__objc_methname: 0xf154
   __TEXT.__objc_classname: 0xbef
-  __TEXT.__objc_methtype: 0x2f3d
-  __TEXT.__oslogstring: 0xf504
-  __TEXT.__unwind_info: 0x2dd8
-  __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0x710
+  __TEXT.__objc_methtype: 0x2f3a
+  __TEXT.__oslogstring: 0xf58a
+  __TEXT.__unwind_info: 0x3080
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x15c8
-  __DATA_CONST.__cfstring: 0x1d60
+  __DATA_CONST.__cfstring: 0x1d80
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x8ea8
-  __DATA.__objc_selrefs: 0x36d8
+  __DATA.__objc_selrefs: 0x36e8
   __DATA.__objc_ivar: 0x704
   __DATA.__objc_data: 0x1630
   __DATA.__data: 0xe4c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8EC0C274-3A45-383E-9766-043A8101AC77
-  Functions: 2067
-  Symbols:   494
-  CStrings:  4132
+  UUID: 1F3A45D5-BFFF-38D9-B766-F2E771D8DC8B
+  Functions: 2069
+  Symbols:   496
+  CStrings:  4137
 
Symbols:
+ _AVAssetDownloadSessionDownloadFileProtectionTypeKey
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _OBJC_CLASS_$__DASFileProtection
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ __CFN_createNewResumeDataWithExtractor
+ _objc_release_x2
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "Failed to create secure task to check session-bundle-id | BundleID:%{public}@"
+ "Using value from entitlement for bundle ID | %{public}@"
+ "com.apple.nsurlsession.private.session-bundle-id"
+ "complete"
+ "downloadTaskWithResumeData:extractor:identifier:uniqueIdentifier:reply:"
+ "setFileProtection:"
+ "v56@0:8@\"NSData\"16@\"<STExtractor>\"24Q32@\"NSUUID\"40@?<v@?B>48"
- "downloadTaskWithResumeData:identifier:uniqueIdentifier:reply:"
- "v48@0:8@\"NSData\"16Q24@\"NSUUID\"32@?<v@?B>40"
- "v48@0:8@16Q24@32@?40"

```
