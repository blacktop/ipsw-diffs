## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-3826.400.120.0.0
-  __TEXT.__text: 0x6fce8
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_stubs: 0x9dc0
-  __TEXT.__objc_methlist: 0x49c8
-  __TEXT.__gcc_except_tab: 0xd678
+3826.500.91.0.0
+  __TEXT.__text: 0x70588
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__objc_stubs: 0x9ee0
+  __TEXT.__objc_methlist: 0x55a4
   __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x358d
-  __TEXT.__objc_methname: 0xd807
-  __TEXT.__objc_classname: 0xba1
-  __TEXT.__objc_methtype: 0x2bd1
-  __TEXT.__oslogstring: 0xb1d5
-  __TEXT.__unwind_info: 0x26a8
-  __DATA_CONST.__auth_got: 0x820
-  __DATA_CONST.__got: 0x6e8
-  __DATA_CONST.__const: 0x1600
-  __DATA_CONST.__cfstring: 0x1e40
+  __TEXT.__gcc_except_tab: 0xd77c
+  __TEXT.__cstring: 0x3594
+  __TEXT.__objc_methname: 0xd913
+  __TEXT.__objc_classname: 0xba0
+  __TEXT.__objc_methtype: 0x2c1a
+  __TEXT.__oslogstring: 0xb255
+  __TEXT.__unwind_info: 0x26b8
+  __DATA_CONST.__auth_got: 0x830
+  __DATA_CONST.__got: 0x6f0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x15e0
+  __DATA_CONST.__cfstring: 0x1e60
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x120

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x9778
-  __DATA.__objc_selrefs: 0x2f18
+  __DATA.__objc_const: 0x8248
+  __DATA.__objc_selrefs: 0x3228
   __DATA.__objc_ivar: 0x630
   __DATA.__objc_data: 0x15e0
   __DATA.__data: 0xd88

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1809
-  Symbols:   478
-  CStrings:  3485
+  Functions: 1800
+  Symbols:   482
+  CStrings:  3501
 
Symbols:
+ _SANDBOX_CHECK_CANONICAL
+ _SANDBOX_CHECK_NO_REPORT
+ _snprintf
+ _strdup
CStrings:
+ "/.nofollow%s"
+ "/.nofollow/"
+ "@56@0:8@16{?=[8I]}24"
+ "Client tried to set _directoryForDownloadedFiles but does not have access to directory"
+ "NDSession <%{public}@> %{public}@ applying overrides %@"
+ "NDSession <%{public}@> Client tried to set _directoryForDownloadedFiles but does not have access to directory"
+ "NDSession <%{public}@> Client tried to set _pathToDownloadTaskFile but is not allowed to create %@"
+ "Too many total tasks for app <%{public}@>, skipping other sessions"
+ "_allowsCellularAccess"
+ "_allowsConstrainedNetworkAccess"
+ "_allowsExpensiveNetworkAccess"
+ "_downloadFileProtectionType"
+ "_forceEnablePQTLS"
+ "applyOverrides:forTaskWithIdentifier:"
+ "noFollowRealURL:"
+ "realpath failed on %@"
+ "safeDirectoryForDownloads:auditToken:"
+ "safeURLForDownload:auditToken:"
+ "set_downloadFileProtectionType:"
+ "set_forceEnablePQTLS:"
+ "v32@0:8@\"_NSURLSessionBackgroundTaskOverrides\"16Q24"
- "Client tried to set _directoryForDownloadedFiles but does not have access to directory %@"
- "NDSession <%{public}@> Client tried to set _directoryForDownloadedFiles but does not have access to directory %@"
- "NDSession <%{public}@> Client tried to set _pathToDownloadTaskFile but is not allowed to create %@: %{errno}d"
- "_isSafeDirectoryForDownloads:withToken:"
- "file-write-create"

```
