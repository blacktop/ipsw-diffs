## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit`

```diff

-1587.0.27.0.0
-  __TEXT.__text: 0x15a30
-  __TEXT.__objc_methlist: 0x14f8
+1587.1.3.0.0
+  __TEXT.__text: 0x16034
+  __TEXT.__objc_methlist: 0x15a0
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x1dea
+  __TEXT.__cstring: 0x1e26
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__oslogstring: 0x8a3
   __TEXT.__unwind_info: 0x450

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd88
+  __DATA_CONST.__objc_selrefs: 0xdc0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x1e90
+  __AUTH_CONST.__cfstring: 0xbc0
+  __AUTH_CONST.__objc_const: 0x1f80
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 539
-  Symbols:   1029
-  CStrings:  249
+  Functions: 553
+  Symbols:   1051
+  CStrings:  253
 
Symbols:
+ -[UARPDevice transportDomain]
+ -[UARPDevice(FeatureSupport) setDeviceTransportDomain:]
+ -[UARPDeviceConfiguration productGroup]
+ -[UARPDeviceConfiguration productNumber]
+ -[UARPDeviceConfiguration setProductGroup:]
+ -[UARPDeviceConfiguration setProductNumber:]
+ -[UARPDeviceManager productGroup:endpointIndex:]
+ -[UARPDeviceManager productGroup:endpointIndex:componentIndex:]
+ -[UARPDeviceManager productNumber:endpointIndex:]
+ -[UARPDeviceManager productNumber:endpointIndex:componentIndex:]
+ -[UARPHostEndpointProperties assetIdentifier]
+ -[UARPHostEndpointProperties setAssetIdentifier:]
+ -[UARPHostEndpointProperties setTransportDomain:]
+ -[UARPHostEndpointProperties transportDomain]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table97
+ OBJC_IVAR_$_UARPDevice._transportDomain
+ OBJC_IVAR_$_UARPDeviceConfiguration._productGroup
+ OBJC_IVAR_$_UARPDeviceConfiguration._productNumber
+ OBJC_IVAR_$_UARPHostEndpointProperties._assetIdentifier
+ OBJC_IVAR_$_UARPHostEndpointProperties._transportDomain
+ _objc_msgSend$setTransportDomain:
+ _objc_msgSend$transportDomain
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table101
- GCC_except_table104
- GCC_except_table107
- GCC_except_table110
- GCC_except_table113
- GCC_except_table116
- GCC_except_table119
- GCC_except_table122
- GCC_except_table125
- GCC_except_table130
- GCC_except_table133
- GCC_except_table73
- GCC_except_table75
- GCC_except_table76
- GCC_except_table93
- GCC_except_table98
CStrings:
+ "ProductGroup"
+ "ProductNumber"
+ "assetIdentifier"
+ "transportDomain"
```
