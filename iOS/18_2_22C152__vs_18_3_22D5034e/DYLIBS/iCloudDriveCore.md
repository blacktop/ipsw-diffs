## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3097.60.161.0.0
-  __TEXT.__text: 0x2d7540
+3097.80.13.0.0
+  __TEXT.__text: 0x2d78c4
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x16828
+  __TEXT.__objc_methlist: 0x16838
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x79253
-  __TEXT.__oslogstring: 0x39a37
+  __TEXT.__cstring: 0x7935e
+  __TEXT.__oslogstring: 0x39ad4
   __TEXT.__gcc_except_tab: 0x180c4
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x8730
+  __TEXT.__unwind_info: 0x8738
   __TEXT.__objc_classname: 0x23a6
-  __TEXT.__objc_methname: 0x3d79a
+  __TEXT.__objc_methname: 0x3d7c5
   __TEXT.__objc_methtype: 0x7600
-  __TEXT.__objc_stubs: 0x2a400
-  __DATA_CONST.__got: 0x1668
+  __TEXT.__objc_stubs: 0x2a420
+  __DATA_CONST.__got: 0x1670
   __DATA_CONST.__const: 0x8788
   __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd180
+  __DATA_CONST.__objc_selrefs: 0xd188
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x7f0
   __DATA_CONST.__objc_arraydata: 0xe00
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x27a8
-  __AUTH_CONST.__cfstring: 0x21740
-  __AUTH_CONST.__objc_const: 0x39d00
+  __AUTH_CONST.__const: 0x27b0
+  __AUTH_CONST.__cfstring: 0x21760
+  __AUTH_CONST.__objc_const: 0x39d30
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1d64
+  __DATA.__objc_ivar: 0x1d68
   __DATA.__data: 0x2168
   __DATA.__bss: 0x218
   __DATA_DIRTY.__objc_data: 0x34d0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12414
-  Symbols:   15165
-  CStrings:  21824
+  Functions: 12416
+  Symbols:   15169
+  CStrings:  21831
 
Symbols:
+ _BRWhatsAppContainerID
CStrings:
+ "TB,R,N,V_isWhatsApp"
+ "UPDATE client_uploads SET transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL, throttle_state = 1 WHERE throttle_state = 33 AND upload_error LIKE '%%(CKErrorDomain:15)%%'"
+ "[DEBUG] returning item busy for %@ since there is an active upload in progess.%@"
+ "[NOTICE] Recovered %lld stuck upload jobs on CKErrorServerRejectedRequest%@"
+ "_isWhatsApp"
+ "br_fixup_upload_jobs_stuck_on_server_rejected"
+ "isWhatsApp"

```
