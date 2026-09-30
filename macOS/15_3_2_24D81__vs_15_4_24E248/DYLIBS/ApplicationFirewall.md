## ApplicationFirewall

> `/System/Library/PrivateFrameworks/ApplicationFirewall.framework/Versions/A/ApplicationFirewall`

```diff

-280.80.2.0.0
-  __TEXT.__text: 0x458c
+305.0.0.0.0
+  __TEXT.__text: 0x4404
   __TEXT.__auth_stubs: 0x140
+  __TEXT.__objc_methlist: 0x124
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x2b4
   __TEXT.__oslogstring: 0x93a

   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x108
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0xb0
   __AUTH_CONST.__const: 0x2d0
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x338
+  __AUTH_CONST.__objc_const: 0x110
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C9BB4F5F-ADA8-3209-8909-6AA15E65A175
-  Functions: 101
-  Symbols:   210
+  UUID: 3CC60A93-D678-303B-ACC0-19FED7D0E9D0
+  Functions: 104
+  Symbols:   243
   CStrings:  126
 
Symbols:
+ AFClientConnection.cold.1
+ AFGetAllowBuiltInSignedApp.cold.2
+ AFGetAllowDownloadedSignedApp.cold.2
+ AFGetStealthMode.cold.2
+ AFSetAllowDownloadedSignedApp.cold.2
+ AFSetStealthMode.cold.2
+ __AFAddApplicationByBundleID_block_invoke.64.cold.2
+ __AFAddApplicationByBundleID_block_invoke.cold.2
+ __AFAddApplicationByPath_block_invoke.61.cold.2
+ __AFAddApplicationByPath_block_invoke.cold.2
+ __AFGetAllApplications_block_invoke.30.cold.2
+ __AFGetAllApplications_block_invoke.cold.2
+ __AFGetAllowBuiltInSignedApp_block_invoke.cold.2
+ __AFGetAllowDownloadedSignedApp_block_invoke.cold.2
+ __AFGetAppStateByBundleID_block_invoke.cold.2
+ __AFGetAppStateByPath_block_invoke.cold.2
+ __AFGetStealthMode_block_invoke.cold.2
+ __AFRemoveApplicationByBundleID_block_invoke.72.cold.2
+ __AFRemoveApplicationByBundleID_block_invoke.cold.2
+ __AFRemoveApplicationByPath_block_invoke.69.cold.2
+ __AFRemoveApplicationByPath_block_invoke.cold.2
+ __AFSetAllowBuiltInSignedApp_block_invoke.87.cold.2
+ __AFSetAllowBuiltInSignedApp_block_invoke.cold.2
+ __AFSetAllowDownloadedSignedApp_block_invoke.102.cold.2
+ __AFSetAllowDownloadedSignedApp_block_invoke.cold.2
+ __AFSetAppStateByBundleID_block_invoke.56.cold.2
+ __AFSetAppStateByBundleID_block_invoke.cold.2
+ __AFSetAppStateByPath_block_invoke.53.cold.2
+ __AFSetAppStateByPath_block_invoke.cold.2
+ __AFSetStealthMode_block_invoke.115.cold.2
+ __AFSetStealthMode_block_invoke.cold.2
+ check_internal_build.cold.1
+ fw_framework_log_obj.cold.1

```
