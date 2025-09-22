## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.110.5.0.0
-  __TEXT.__text: 0x2eda28
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x2abc0
+4025.210.8.1.0
+  __TEXT.__text: 0x2edf8c
+  __TEXT.__auth_stubs: 0x16f0
+  __TEXT.__objc_methlist: 0x2ac50
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2b7e6
+  __TEXT.__cstring: 0x2b79b
   __TEXT.__oslogstring: 0xd871
   __TEXT.__gcc_except_tab: 0x63ac
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xb0f0
-  __TEXT.__objc_classname: 0x4d07
-  __TEXT.__objc_methname: 0x4cae2
+  __TEXT.__unwind_info: 0xb108
+  __TEXT.__objc_classname: 0x4d17
+  __TEXT.__objc_methname: 0x4cc8e
   __TEXT.__objc_methtype: 0x8f16
-  __TEXT.__objc_stubs: 0x27ee0
-  __DATA_CONST.__got: 0x1438
-  __DATA_CONST.__const: 0xae40
-  __DATA_CONST.__objc_classlist: 0x1180
+  __TEXT.__objc_stubs: 0x27fa0
+  __DATA_CONST.__got: 0x1440
+  __DATA_CONST.__const: 0xad70
+  __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xede0
+  __DATA_CONST.__objc_selrefs: 0xee38
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xfb8
   __DATA_CONST.__objc_arraydata: 0x260
-  __AUTH_CONST.__auth_got: 0xb80
+  __AUTH_CONST.__auth_got: 0xb88
   __AUTH_CONST.__const: 0x3020
-  __AUTH_CONST.__cfstring: 0x22fc0
-  __AUTH_CONST.__objc_const: 0x45448
+  __AUTH_CONST.__cfstring: 0x22d40
+  __AUTH_CONST.__objc_const: 0x45538
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x8200
+  __AUTH.__objc_data: 0x8250
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x31d8
+  __DATA.__objc_ivar: 0x31e0
   __DATA.__data: 0x1c80
   __DATA.__bss: 0x850
   __DATA.__common: 0x8

   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36AE6EB4-1A27-316B-8782-A8FBA0034936
-  Functions: 20020
-  Symbols:   54972
-  CStrings:  24229
+  UUID: 7EB781F7-CFFD-3A43-8271-819B436839EE
+  Functions: 20033
+  Symbols:   54983
+  CStrings:  24205
 
Symbols:
+ +[MRCBProductInfo cbProductIDFromModelID:]
+ +[MRCBProductInfo isAirPodsDeviceWithModelID:]
+ +[MRCBProductInfo isAirPodsMaxDeviceWithModelID:]
+ +[MRCBProductInfo isBeatsDeviceWithModelID:]
+ +[MRCBProductInfo isW1DeviceWithModelID:]
+ +[MRCBProductInfo isW2DeviceWithModelID:]
+ +[MRCBProductInfo isW3DeviceWithModelID:]
+ -[MRAVEndpoint groupLeaderIsPlaceholder]
+ -[MRAVOutputDevice belongsToLocalCluster]
+ -[MRAVOutputDevice hasPlaceholderName]
+ -[MRAVOutputDevice isAirpodsMaxDevice]
+ -[MRAVOutputDevice isLocalDeviceOrBelongsToLocalCluster]
+ -[MRContentItemMetadata setTransitionInfo:]
+ -[MRContentItemMetadata transitionInfo]
+ -[_MRContentItemMetadataProtobuf hasTransitionInfoData]
+ -[_MRContentItemMetadataProtobuf setTransitionInfoData:]
+ -[_MRContentItemMetadataProtobuf transitionInfoData]
+ GCC_except_table220
+ GCC_except_table250
+ GCC_except_table334
+ OBJC_IVAR_$__MRContentItemMetadataProtobuf._transitionInfoData
+ _CBProductIDFromNSString
+ _MRContentItemCopyTransitionInfo
+ _MRContentItemGetTransitionInfo
+ _MRContentItemSetTransitionInfo
+ _OBJC_CLASS_$_MRCBProductInfo
+ _OBJC_IVAR_$_MRContentItemMetadata._transitionInfo
+ _OBJC_METACLASS_$_MRCBProductInfo
+ __OBJC_$_CLASS_METHODS_MRCBProductInfo
+ __OBJC_CLASS_RO_$_MRCBProductInfo
+ __OBJC_METACLASS_RO_$_MRCBProductInfo
+ ___MRContentItemSetTransitionInfo_block_invoke
+ ___block_literal_global.253
+ ___block_literal_global.257
+ ___block_literal_global.312
+ _objc_msgSend$belongsToLocalCluster
+ _objc_msgSend$cbProductIDFromModelID:
+ _objc_msgSend$hasPlaceholderName
+ _objc_msgSend$hasTransitionInfoData
+ _objc_msgSend$isAirPodsDeviceWithModelID:
+ _objc_msgSend$isAirPodsMaxDeviceWithModelID:
+ _objc_msgSend$isAirpodsMaxDevice
+ _objc_msgSend$isW3DeviceWithModelID:
+ _objc_msgSend$setTransitionInfo:
+ _objc_msgSend$setTransitionInfoData:
+ _objc_msgSend$transitionInfo
+ _objc_msgSend$transitionInfoData
- -[MRAVOutputDevice isB298Device]
- -[MRAVOutputDevice isB515CDevice]
- -[MRAVOutputDevice isB515Device]
- -[MRAVOutputDevice isB688Device]
- -[MRAVOutputDevice isB698CDevice]
- -[MRAVOutputDevice isB698Device]
- -[MRAVOutputDevice isB735Device]
- -[MRAVOutputDevice isB768Device]
- GCC_except_table100
- GCC_except_table219
- GCC_except_table248
- GCC_except_table333
- _MRAVOutputDeviceB188ModelID
- _MRAVOutputDeviceB282ModelID
- _MRAVOutputDeviceB288ModelID
- _MRAVOutputDeviceB298ModelID
- _MRAVOutputDeviceB312ModelID
- _MRAVOutputDeviceB352ModelID
- _MRAVOutputDeviceB364ModelID
- _MRAVOutputDeviceB372ModelID
- _MRAVOutputDeviceB419ModelID
- _MRAVOutputDeviceB443ModelID
- _MRAVOutputDeviceB444ModelID
- _MRAVOutputDeviceB494ModelID
- _MRAVOutputDeviceB498ModelID
- _MRAVOutputDeviceB507ModelID
- _MRAVOutputDeviceB515CModelID
- _MRAVOutputDeviceB515ModelID
- _MRAVOutputDeviceB607ModelID
- _MRAVOutputDeviceB688ModelID
- _MRAVOutputDeviceB698CModelID
- _MRAVOutputDeviceB698ModelID
- _MRAVOutputDeviceB735EModelID
- _MRAVOutputDeviceB735MModelID
- _MRAVOutputDeviceB768CHEModelID
- _MRAVOutputDeviceB768CHMModelID
- _MRAVOutputDeviceB768EModelID
- _MRAVOutputDeviceB768MModelID
- ___block_literal_global.249
- ___block_literal_global.255
- ___block_literal_global.309
- _objc_msgSend$isB298Device
- _objc_msgSend$isB515CDevice
- _objc_msgSend$isB515Device
- _objc_msgSend$isB688Device
- _objc_msgSend$isB698CDevice
- _objc_msgSend$isB698Device
CStrings:
+ "MRCBProductInfo"
+ "NoLocalEndpointConnection (without recent reboot detected)"
+ "T@\"NSData\",&,N,V_transitionInfoData"
+ "T@\"NSDictionary\",C,N,V_transitionInfo"
+ "UGL iPhone"
+ "_transitionInfo"
+ "_transitionInfoData"
+ "belongsToLocalCluster"
+ "cbProductIDFromModelID:"
+ "destinationInt"
+ "groupLeaderIsPlaceholder"
+ "hasPlaceholderName"
+ "hasTransitionInfoData"
+ "isAirPodsDeviceWithModelID:"
+ "isAirPodsMaxDeviceWithModelID:"
+ "isAirpodsMaxDevice"
+ "isBeatsDeviceWithModelID:"
+ "isLocalDeviceOrBelongsToLocalCluster"
+ "isW1DeviceWithModelID:"
+ "isW2DeviceWithModelID:"
+ "isW3DeviceWithModelID:"
+ "originatorInt"
+ "setTransitionInfo:"
+ "setTransitionInfoData:"
+ "transitionInfo"
+ "transitionInfoData"
- "76,5023"
- "76,5024"
- "76,8194"
- "76,8195"
- "76,8197"
- "76,8198"
- "76,8201"
- "76,8202"
- "76,8203"
- "76,8204"
- "76,8205"
- "76,8206"
- "76,8207"
- "76,8208"
- "76,8209"
- "76,8210"
- "76,8211"
- "76,8212"
- "76,8214"
- "76,8217"
- "76,8219"
- "76,8221"
- "76,8222"
- "76,8223"
- "76,8224"
- "76,8228"
- "isB298Device"
- "isB515CDevice"
- "isB515Device"
- "isB688Device"
- "isB698CDevice"
- "isB698Device"

```
