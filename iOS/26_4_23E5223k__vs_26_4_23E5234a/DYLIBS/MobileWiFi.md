## MobileWiFi

> `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`

```diff

-1995.26.5.0.0
-  __TEXT.__text: 0x2e830
-  __TEXT.__auth_stubs: 0xdc0
+1995.26.6.0.0
+  __TEXT.__text: 0x2e8b4
+  __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0x44e5
   __TEXT.__const: 0x6b0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x450
   __AUTH_CONST.__cfstring: 0x58a0
   __AUTH_CONST.__objc_const: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81C35427-0ECB-3A92-85A0-B0FBC34F31FF
-  Functions: 1159
-  Symbols:   2716
+  UUID: FB429874-DF49-35F8-AAAE-7B3E3013DC8B
+  Functions: 1160
+  Symbols:   2724
   CStrings:  1801
 
Symbols:
+ _WiFiSecurityCopyNonSyncablePasswordWithTimeout.cold.1
+ _WiFiSecurityCopyPasswordWithTimeout.cold.1
+ __Block_release
+ ___WiFiSecurityQueue.onceToken
+ ___WiFiSecurityQueue.queue
+ _____WiFiSecurityQueue_block_invoke
+ _dispatch_block_create_with_qos_class
+ _dispatch_queue_attr_make_with_qos_class
- _WiFiSecurityPasswordBackupQueue.onceToken
- _WiFiSecurityPasswordBackupQueue.queue
- ___WiFiSecurityPasswordBackupQueue_block_invoke
- _dispatch_get_global_queue

```
