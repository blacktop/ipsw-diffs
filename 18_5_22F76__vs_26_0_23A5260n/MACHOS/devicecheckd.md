## devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

-109.6.0.0.0
-  __TEXT.__text: 0x33c8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x45c
+119.0.0.0.0
+  __TEXT.__text: 0x4414
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x640
+  __TEXT.__objc_methlist: 0x484
   __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methname: 0x9e9
-  __TEXT.__objc_methtype: 0x4d2
-  __TEXT.__cstring: 0x37d
+  __TEXT.__objc_methname: 0xa73
+  __TEXT.__objc_methtype: 0x53b
+  __TEXT.__cstring: 0x3c5
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__oslogstring: 0x49e
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x1a0
+  __TEXT.__oslogstring: 0x549
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x300
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x628
-  __DATA.__objc_selrefs: 0x2c8
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_const: 0x660
+  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1052655B-0534-3291-9A9A-B5B794DCF8BF
-  Functions: 69
-  Symbols:   119
-  CStrings:  224
+  UUID: 6FBDA95A-EDB0-36B9-B604-A5F58BE2D122
+  Functions: 90
+  Symbols:   124
+  CStrings:  238
 
Symbols:
+ _AppAttest_AppAttestation_GetKey
+ _OBJC_CLASS_$_SecKeyProxy
+ _dispatch_async
+ _dispatch_queue_get_label
+ _objc_retain_x24
CStrings:
+ "%25s:%-5d Created key proxy. { keyProxy=%@, endpoint=%@ }"
+ "%25s:%-5d Created server processing queue. { queueName=%s }"
+ "%25s:%-5d Failed to get key properties. { error=%@ }"
+ "@\"SecKeyProxy\""
+ "T@\"SecKeyProxy\",&,N,V_keyProxy"
+ "_keyProxy"
+ "com.apple.devicecheck.server.processing"
+ "endpoint"
+ "getKeyProxyEndpoint:keyId:teamIdentifier:completion:"
+ "initWithKey:"
+ "keyProxy"
+ "setKeyProxy:"
+ "v24@?0^{__SecKey=}8@\"NSError\"16"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">40"

```
