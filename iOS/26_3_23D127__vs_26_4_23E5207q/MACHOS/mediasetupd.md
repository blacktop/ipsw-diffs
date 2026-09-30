## mediasetupd

> `/usr/libexec/mediasetupd`

```diff

-249.0.0.0.0
-  __TEXT.__text: 0x31ce8
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_stubs: 0x4b80
-  __TEXT.__objc_methlist: 0x1fb4
-  __TEXT.__cstring: 0x2404
-  __TEXT.__oslogstring: 0x581c
+249.40.9.0.0
+  __TEXT.__text: 0x32948
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0x4c40
+  __TEXT.__objc_methlist: 0x1fac
+  __TEXT.__cstring: 0x240f
+  __TEXT.__oslogstring: 0x58f7
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0xd38
-  __TEXT.__objc_methname: 0x6ad2
-  __TEXT.__objc_classname: 0x33e
-  __TEXT.__objc_methtype: 0x12b8
-  __TEXT.__unwind_info: 0xb10
-  __DATA_CONST.__auth_got: 0x380
+  __TEXT.__gcc_except_tab: 0xe78
+  __TEXT.__objc_methname: 0x6b06
+  __TEXT.__objc_classname: 0x33b
+  __TEXT.__objc_methtype: 0x12c7
+  __TEXT.__unwind_info: 0xbc8
+  __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0x540
-  __DATA_CONST.__const: 0x2060
+  __DATA_CONST.__const: 0x2038
   __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3108
-  __DATA.__objc_selrefs: 0x1ba0
-  __DATA.__objc_ivar: 0x160
+  __DATA.__objc_const: 0x30e8
+  __DATA.__objc_selrefs: 0x1bb8
+  __DATA.__objc_ivar: 0x15c
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x4e0
   __DATA.__bss: 0xe0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6722D229-AADA-371E-ADBF-7D508AD40957
-  Functions: 957
-  Symbols:   289
-  CStrings:  2073
+  UUID: F3E0E324-5319-3708-87F8-FA21FA8B3F80
+  Functions: 967
+  Symbols:   286
+  CStrings:  2080
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "-[MSDPublicDBManager _syncDataWithCloudKitWithSystemTask:completion:]"
+ "@\"CKOperation\""
+ "A sync with the public db is already underway with a different system task than requested. Restarting sync."
+ "Failed to fetch PublicDB Info, PublicDBManager finalized"
+ "Failed to fetch PublicDB Info, sync operation changed"
+ "T@\"CKOperation\",&,N,V_queuedOperation"
+ "_queuedOperation"
+ "_syncDataWithCloudKitWithSystemTask:completion:"
+ "cancel"
+ "configuration"
+ "home:didUpdateAccessoryInvitationsForUser:"
+ "queuedOperation"
+ "setQueuedOperation:"
+ "setSystemTask:"
+ "syncDataWithCloudKitWithSystemTask:completion:"
+ "systemTask"
- "-[MSDPublicDBManager _syncDataWithCloudKitWithCompletion:]"
- "TB,N,V_isCurrentlySyncing"
- "_isCurrentlySyncing"
- "_syncDataWithCloudKitWithCompletion:"
- "_withLock:"
- "executePendingRequests:forPublicDBInfo:error:"
- "home:didUpdateAccesoryInvitationsForUser:"
- "isCurrentlySyncing"
- "setIsCurrentlySyncing:"

```
