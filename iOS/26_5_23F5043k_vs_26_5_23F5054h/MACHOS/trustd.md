## trustd

> `filesystem/usr/libexec/trustd`

```diff

-61901.120.36.0.3
-  __TEXT.__text: 0x69658
-  __TEXT.__auth_stubs: 0x2450
+61901.120.56.0.1
+  __TEXT.__text: 0x6940c
+  __TEXT.__auth_stubs: 0x2410
   __TEXT.__objc_stubs: 0x3160
   __TEXT.__objc_methlist: 0xd54
   __TEXT.__const: 0x5ab1
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__gcc_except_tab: 0xc20
-  __TEXT.__cstring: 0x739c
-  __TEXT.__oslogstring: 0x6736
+  __TEXT.__cstring: 0x7357
+  __TEXT.__oslogstring: 0x676b
   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methname: 0x3030
   __TEXT.__objc_methtype: 0xc75
-  __TEXT.__unwind_info: 0x1178
-  __DATA_CONST.__auth_got: 0x1238
-  __DATA_CONST.__got: 0x7d0
+  __TEXT.__unwind_info: 0x1170
+  __DATA_CONST.__auth_got: 0x1218
+  __DATA_CONST.__got: 0x7c8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x4f10
-  __DATA_CONST.__cfstring: 0x6860
+  __DATA_CONST.__const: 0x4ea0
+  __DATA_CONST.__cfstring: 0x6840
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B5C7B4E8-8044-3972-9E4C-0F06E288E6D6
-  Functions: 1344
-  Symbols:   849
-  CStrings:  3228
+  UUID: 28EAAF74-D560-3F8C-B4F0-03BFF73E273B
+  Functions: 1339
+  Symbols:   844
+  CStrings:  3225
 
Symbols:
- __os_activity_create
- __os_activity_current
- _os_activity_scope_enter
- _os_activity_scope_leave
- _securityd_send_sync_and_do
CStrings:
+ "CRLite: crlite_info: %@"
+ "CRLite: setting determined error result 'revoked' for cert %ld"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/7BD9B574-B86B-4AA5-8A5B-46D03238BB9C/TemporaryDirectory.iStmIC/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "valid: setting determined error result 'revoked' for cert %ld"
- "B24@?0^v8^^{__CFError}16"
- "Failed to copy apple anchors: %@"
- "Falling back to built-in anchors"
- "SecTrustCopyAppleTrustAnchors"
- "com.apple.security.file./Library/Caches/com.apple.xbs/7829CA60-F7EB-4500-BF75-00494D53CAFB/TemporaryDirectory.TRhBEk/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "failed to convert string for key %s to utf8"

```
