## GPUToolsTransport

> `/System/Library/PrivateFrameworks/GPUToolsTransport.framework/Versions/A/GPUToolsTransport`

```diff

-2027.0.39.0.0
-  __TEXT.__text: 0x5c220
-  __TEXT.__objc_methlist: 0x962c
+2027.0.44.0.0
+  __TEXT.__text: 0x5c630
+  __TEXT.__objc_methlist: 0x966c
   __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x47e6
-  __TEXT.__oslogstring: 0x1382
-  __TEXT.__unwind_info: 0x1dc0
+  __TEXT.__cstring: 0x4803
+  __TEXT.__oslogstring: 0x13b3
+  __TEXT.__unwind_info: 0x1dd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3040
+  __DATA_CONST.__objc_selrefs: 0x3068
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x798
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x2a0
-  __AUTH_CONST.__const: 0xe10
-  __AUTH_CONST.__cfstring: 0x4b80
-  __AUTH_CONST.__objc_const: 0x15198
+  __AUTH_CONST.__const: 0xe70
+  __AUTH_CONST.__cfstring: 0x4ba0
+  __AUTH_CONST.__objc_const: 0x15208
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5320
-  __DATA.__objc_ivar: 0xb80
+  __DATA.__objc_ivar: 0xb88
   __DATA.__data: 0x1e08
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3000
-  Symbols:   7580
-  CStrings:  804
+  Functions: 3009
+  Symbols:   7598
+  CStrings:  806
 
Symbols:
+ -[GTServiceProperties accessLevel]
+ -[GTServiceProperties setAccessLevel:]
+ -[GTServiceProvider accessLevelForPort:]
+ -[GTServiceProviderObserver originatorUntrusted]
+ -[GTServiceProviderObserver setOriginatorUntrusted:]
+ OBJC_IVAR_$_GTServiceProperties._accessLevel
+ OBJC_IVAR_$_GTServiceProviderObserver._originatorUntrusted
+ _MessageOriginatorIsUntrusted
+ __OBJC_$_INSTANCE_VARIABLES_GTServiceProviderObserver
+ __OBJC_$_PROP_LIST_GTServiceProviderObserver
+ ___block_descriptor_104_8_32s40s48s56s64s72s80bs88r_e5_v8?0l
+ ___block_descriptor_49_8_32s40s_e15_v16?0"NSURL"8l
+ ___block_descriptor_49_8_32s40s_e27_v24?0"NSURL"8"NSError"16l
+ ___copy_helper_block_8_32s40s48s56s64s72s80b88r
+ ___destroy_helper_block_8_32s40s48s56s64s72s80s88r
+ _hideDeviceUDIDInURLIfUntrusted
+ _objc_msgSend$accessLevel
+ _objc_msgSend$originatorUntrusted
+ _objc_msgSend$setAccessLevel:
+ _objc_msgSend$setOriginatorUntrusted:
+ _servicesVisibleToOriginator
- ___block_descriptor_96_8_32s40s48s56s64s72s80bs_e5_v8?0l
- ___copy_helper_block_8_32s40s48s56s64s72s80b
- ___destroy_helper_block_8_32s40s48s56s64s72s80s
CStrings:
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu accessLevel=%llu>"
+ "accessLevel"
+ "failed to issue sandbox extension for %{public}@"
- "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
```
