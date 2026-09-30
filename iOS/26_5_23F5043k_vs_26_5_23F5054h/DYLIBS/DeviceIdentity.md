## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-1076.120.9.0.0
-  __TEXT.__text: 0x1cd24
-  __TEXT.__auth_stubs: 0x860
+1076.120.11.0.0
+  __TEXT.__text: 0x1ce9c
+  __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x504
-  __TEXT.__cstring: 0x3e97
+  __TEXT.__cstring: 0x3ed4
   __TEXT.__const: 0xabaa
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x6e3
+  __TEXT.__oslogstring: 0x70e
   __TEXT.__gcc_except_tab: 0xa14
   __TEXT.__dlopen_cstrs: 0x134
   __TEXT.__unwind_info: 0x3d8
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x1778
+  __TEXT.__objc_methname: 0x178d
   __TEXT.__objc_methtype: 0x349
-  __TEXT.__objc_stubs: 0x10a0
+  __TEXT.__objc_stubs: 0x10c0
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x36c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x4f0
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x43e0
+  __AUTH_CONST.__cfstring: 0x4400
   __AUTH_CONST.__objc_const: 0x7b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE35276B-F463-351F-8FEF-1CD974572BD9
-  Functions: 270
-  Symbols:   1365
-  CStrings:  1490
+  UUID: 6E3A764A-1E23-3B91-886B-24765F53B5BF
+  Functions: 272
+  Symbols:   1371
+  CStrings:  1494
 
Symbols:
+ ___block_literal_global.6
+ __os_log_debug_impl
+ _isSupportedDeviceIdentityClient.cold.3
+ _objc_msgSend$valueForEntitlement:
- ___block_literal_global.3
Functions:
~ _isSupportedDeviceIdentityClient : 376 -> 640
+ _OUTLINED_FUNCTION_2
~ _isSupportedDeviceIdentityClient.cold.2 : 108 -> 88
+ _isSupportedDeviceIdentityClient.cold.3
CStrings:
+ "Allowlist bypassed for %@ via entitlement."
+ "com.apple.mobileactivationd.deviceidentity-allowlist-exempt"
+ "iOS Device Activator (MobileActivation-1076.120.11)"
+ "valueForEntitlement:"
- "iOS Device Activator (MobileActivation-1076.120.9)"

```
