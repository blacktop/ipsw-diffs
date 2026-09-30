## GPUToolsTransport

> `/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport`

```diff

-2027.0.37.0.0
-  __TEXT.__text: 0x567b8
-  __TEXT.__objc_methlist: 0x962c
+2027.0.44.0.0
+  __TEXT.__text: 0x56bd8
+  __TEXT.__objc_methlist: 0x966c
   __TEXT.__const: 0x5a8
-  __TEXT.__cstring: 0x4767
-  __TEXT.__oslogstring: 0x12fd
-  __TEXT.__unwind_info: 0x1d30
+  __TEXT.__cstring: 0x4784
+  __TEXT.__oslogstring: 0x132e
+  __TEXT.__unwind_info: 0x1d48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1048
+  __DATA_CONST.__const: 0x1098
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fb0
+  __DATA_CONST.__objc_selrefs: 0x2fd8
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x798
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x4c60
-  __AUTH_CONST.__objc_const: 0x15198
+  __AUTH_CONST.__cfstring: 0x4c80
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
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2960
-  Symbols:   7558
-  CStrings:  814
+  Functions: 2969
+  Symbols:   7576
+  CStrings:  816
 
Symbols:
+ -[GTServiceProperties accessLevel]
+ -[GTServiceProperties setAccessLevel:]
+ -[GTServiceProvider accessLevelForPort:]
+ -[GTServiceProviderObserver originatorUntrusted]
+ -[GTServiceProviderObserver setOriginatorUntrusted:]
+ _MessageOriginatorIsUntrusted
+ _OBJC_IVAR_$_GTServiceProperties._accessLevel
+ _OBJC_IVAR_$_GTServiceProviderObserver._originatorUntrusted
+ __OBJC_$_INSTANCE_VARIABLES_GTServiceProviderObserver
+ __OBJC_$_PROP_LIST_GTServiceProviderObserver
+ ___block_descriptor_104_8_32s40s48s56s64s72s80bs88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8s72l8s80l8
+ ___block_descriptor_49_8_32s40s_e15_v16?0"NSURL"8ls32l8s40l8
+ ___block_descriptor_49_8_32s40s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8
+ _hideDeviceUDIDInURLIfUntrusted
+ _objc_msgSend$accessLevel
+ _objc_msgSend$originatorUntrusted
+ _objc_msgSend$setAccessLevel:
+ _objc_msgSend$setOriginatorUntrusted:
+ _servicesVisibleToOriginator
- ___block_descriptor_96_8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
CStrings:
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu accessLevel=%llu>"
+ "accessLevel"
+ "failed to issue sandbox extension for %{public}@"
- "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
```
