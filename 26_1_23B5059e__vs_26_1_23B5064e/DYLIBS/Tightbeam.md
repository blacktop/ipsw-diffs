## Tightbeam

> `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`

```diff

-483.40.1.0.0
-  __TEXT.__text: 0x28250
-  __TEXT.__auth_stubs: 0x1130
+483.40.2.0.0
+  __TEXT.__text: 0x28300
+  __TEXT.__auth_stubs: 0x1180
   __TEXT.__const: 0x1bca
   __TEXT.__cstring: 0x31b0
   __TEXT.__constg_swiftt: 0x13b8

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x8a0
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH_CONST.__const: 0x2ab0
   __AUTH_CONST.__objc_const: 0x1058
   __DATA.__data: 0x4d0

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 96613A04-477A-3539-BE53-01B68DD9B1E7
+  UUID: E9F81524-EAF1-33BE-B69C-F75166A3A093
   Functions: 1393
-  Symbols:   1566
+  Symbols:   1571
   CStrings:  289
 
Symbols:
+ _audit_token_to_pid
+ _audit_token_to_pidversion
+ _audit_token_to_rgid
+ _audit_token_to_ruid
+ _os_mach_msg_get_audit_trailer
Functions:
~ ____tb_mach_transport_create_block_invoke : 628 -> 792
~ __tb_mach_transport_send_message : 388 -> 400

```
