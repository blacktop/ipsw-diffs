## AirTraffic

> `/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic`

```diff

-4023.300.2.0.0
+4023.500.34.0.0
   __TEXT.__text: 0x19200
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x1f00

   __TEXT.__oslogstring: 0x1541
   __TEXT.__unwind_info: 0x708
   __TEXT.__objc_classname: 0x2ce
-  __TEXT.__objc_methname: 0x4e79
+  __TEXT.__objc_methname: 0x4e8b
   __TEXT.__objc_methtype: 0xb1c
   __TEXT.__objc_stubs: 0x39e0
   __DATA_CONST.__got: 0x160

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x39c0
   __DATA_CONST.__objc_selrefs: 0x1460
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_classrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__cfstring: 0x1d80
   __AUTH_CONST.__objc_const: 0xaf8

   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_protorefs: 0x58
-  __DATA.__objc_classrefs: 0x1a0
-  __DATA.__objc_superrefs: 0xc8
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x318
   __DATA.__data: 0x720
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x24
+  __DATA.__bss: 0x24
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__bss: 0x34
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44C41CA9-A7A7-3738-A320-B84860AD4F84
+  UUID: BA0D4B6B-B51C-35DE-A8B0-6C3E6C87E0E4
   Functions: 804
   Symbols:   2937
-  CStrings:  1843
+  CStrings:  1844
 
Symbols:
+ __OBJC_$_PROP_LIST_ATMessageLink.77
+ ___20-[ATConnection init]_block_invoke.103
+ ___20-[ATConnection init]_block_invoke.105
+ ___26-[ATConnection cancelSync]_block_invoke.124
+ ___29-[ATConnection clearSyncData]_block_invoke.148
+ ___29-[ATConnection keepATCAlive:]_block_invoke.158
+ ___30-[ATServiceProxy messageLinks]_block_invoke.65
+ ___31-[ATConnection getAssetMetrics]_block_invoke.178
+ ___34-[ATMessageLinkProxy addObserver:]_block_invoke.98
+ ___37-[ATServiceProxy initWithConnection:]_block_invoke.57
+ ___38-[ATConnection lowBatteryNotification]_block_invoke.153
+ ___38-[ATConnection requestSyncForLibrary:]_block_invoke.109
+ ___40-[ATConnection getDataRestoreIsComplete]_block_invoke.181
+ ___42+[ATSession _cancelSessionWithIdentifier:]_block_invoke.173
+ ___45-[ATConnection prioritizeAsset:forDataclass:]_block_invoke.129
+ ___47+[ATSession _remoteSessionsWithTypeIdentifier:]_block_invoke.170
+ ___47-[ATConnection purgePartialAsset:forDataclass:]_block_invoke.134
+ ___47-[ATConnection requestKeybagSyncToPairedDevice]_block_invoke.119
+ ___50-[ATConnection openDeviceMessageLinkWithPriority:]_block_invoke.175
+ ___51-[ATConnection isSyncing:automatically:wirelessly:]_block_invoke.163
+ ___53-[ATMessageLinkProxy addRequestHandler:forDataClass:]_block_invoke.99
+ ___54-[ATConnection _sendStatusRegistrationWithCompletion:]_block_invoke.143
+ ___55-[ATConnection requestSyncForPairedDeviceWithPriority:]_block_invoke.114
+ ___55-[ATMessageLinkProxy removeRequestHandlerForDataClass:]_block_invoke.100
+ ___57+[ATSession _remoteActiveSessionCountWithTypeIdentifier:]_block_invoke.174
+ ___Block_byref_object_copy_.1186
+ ___Block_byref_object_copy_.1395
+ ___Block_byref_object_copy_.1675
+ ___Block_byref_object_copy_.199
+ ___Block_byref_object_copy_.277
+ ___Block_byref_object_copy_.363
+ ___Block_byref_object_dispose_.1187
+ ___Block_byref_object_dispose_.1396
+ ___Block_byref_object_dispose_.1676
+ ___Block_byref_object_dispose_.200
+ ___Block_byref_object_dispose_.278
+ ___Block_byref_object_dispose_.364
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.1263
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.133
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.140
+ ___block_literal_global.145
+ ___block_literal_global.147
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.177
+ ___block_literal_global.180
+ ___block_literal_global.1837
+ ___block_literal_global.306
+ ___block_literal_global.373
+ ___block_literal_global.59
+ ___block_literal_global.601
- __OBJC_$_PROP_LIST_ATMessageLink.76
- ___20-[ATConnection init]_block_invoke.102
- ___20-[ATConnection init]_block_invoke.104
- ___26-[ATConnection cancelSync]_block_invoke.123
- ___29-[ATConnection clearSyncData]_block_invoke.147
- ___29-[ATConnection keepATCAlive:]_block_invoke.157
- ___30-[ATServiceProxy messageLinks]_block_invoke.64
- ___31-[ATConnection getAssetMetrics]_block_invoke.177
- ___34-[ATMessageLinkProxy addObserver:]_block_invoke.97
- ___37-[ATServiceProxy initWithConnection:]_block_invoke.56
- ___38-[ATConnection lowBatteryNotification]_block_invoke.152
- ___38-[ATConnection requestSyncForLibrary:]_block_invoke.108
- ___40-[ATConnection getDataRestoreIsComplete]_block_invoke.180
- ___42+[ATSession _cancelSessionWithIdentifier:]_block_invoke.171
- ___45-[ATConnection prioritizeAsset:forDataclass:]_block_invoke.128
- ___47+[ATSession _remoteSessionsWithTypeIdentifier:]_block_invoke.169
- ___47-[ATConnection purgePartialAsset:forDataclass:]_block_invoke.133
- ___47-[ATConnection requestKeybagSyncToPairedDevice]_block_invoke.118
- ___50-[ATConnection openDeviceMessageLinkWithPriority:]_block_invoke.174
- ___51-[ATConnection isSyncing:automatically:wirelessly:]_block_invoke.162
- ___53-[ATMessageLinkProxy addRequestHandler:forDataClass:]_block_invoke.98
- ___54-[ATConnection _sendStatusRegistrationWithCompletion:]_block_invoke.142
- ___55-[ATConnection requestSyncForPairedDeviceWithPriority:]_block_invoke.113
- ___55-[ATMessageLinkProxy removeRequestHandlerForDataClass:]_block_invoke.99
- ___57+[ATSession _remoteActiveSessionCountWithTypeIdentifier:]_block_invoke.173
- ___Block_byref_object_copy_.1185
- ___Block_byref_object_copy_.1392
- ___Block_byref_object_copy_.1670
- ___Block_byref_object_copy_.210
- ___Block_byref_object_copy_.281
- ___Block_byref_object_copy_.386
- ___Block_byref_object_dispose_.1186
- ___Block_byref_object_dispose_.1393
- ___Block_byref_object_dispose_.1671
- ___Block_byref_object_dispose_.211
- ___Block_byref_object_dispose_.282
- ___Block_byref_object_dispose_.387
- ___block_literal_global.110
- ___block_literal_global.112
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.122
- ___block_literal_global.125
- ___block_literal_global.1264
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.132
- ___block_literal_global.135
- ___block_literal_global.137
- ___block_literal_global.139
- ___block_literal_global.144
- ___block_literal_global.146
- ___block_literal_global.149
- ___block_literal_global.151
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.176
- ___block_literal_global.179
- ___block_literal_global.1835
- ___block_literal_global.310
- ___block_literal_global.396
- ___block_literal_global.58
- ___block_literal_global.619
CStrings:
+ "T@\"NSString\",?,R,C"

```
