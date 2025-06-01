## SharingUI

> `/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI`

```diff

-1936.10.1.2.18
-  __TEXT.__text: 0x6f210
+1936.20.66.2.11
+  __TEXT.__text: 0x6f554
   __TEXT.__auth_stubs: 0x1b40
   __TEXT.__objc_methlist: 0x3510
-  __TEXT.__const: 0xaa4
+  __TEXT.__const: 0xab4
   __TEXT.__gcc_except_tab: 0xe14
-  __TEXT.__cstring: 0x4188
-  __TEXT.__oslogstring: 0x139c
+  __TEXT.__cstring: 0x4198
+  __TEXT.__oslogstring: 0x13cb
   __TEXT.__constg_swiftt: 0x290
   __TEXT.__swift5_typeref: 0x406
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_capture: 0x5fc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2084
+  __TEXT.__unwind_info: 0x20a4
   __TEXT.__eh_frame: 0x9a0
   __TEXT.__objc_classname: 0x842
-  __TEXT.__objc_methname: 0xd831
-  __TEXT.__objc_methtype: 0x1fb1
-  __TEXT.__objc_stubs: 0xa260
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x1070
+  __TEXT.__objc_methname: 0xd8a3
+  __TEXT.__objc_methtype: 0x1fc5
+  __TEXT.__objc_stubs: 0xa2a0
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x1098
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7f60
-  __DATA_CONST.__objc_selrefs: 0x3178
+  __DATA_CONST.__objc_const: 0x7fb8
+  __DATA_CONST.__objc_selrefs: 0x3188
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__cfstring: 0x1be0
-  __AUTH_CONST.__objc_const: 0x15d0
+  __AUTH_CONST.__objc_const: 0x1588
   __AUTH_CONST.__const: 0x14c8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0xdc8
   __AUTH.__data: 0x370
   __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x4a8
+  __DATA.__objc_classrefs: 0x4a0
   __DATA.__objc_superrefs: 0x158
   __DATA.__objc_ivar: 0x574
   __DATA.__data: 0xea8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AD180490-6D5C-3DF3-BCE3-FC696003314D
-  Functions: 2085
-  Symbols:   6038
-  CStrings:  3518
+  UUID: 2FF4A0F3-B0A9-38C0-BA97-8FAB334F12C7
+  Functions: 2092
+  Symbols:   6054
+  CStrings:  3524
 
Symbols:
+ +[SFShareSheetRendering drawingCommandsForMoreListEntryTitle:labelColor:hostConfig:activityCategory:]
+ +[SFShareSheetRendering morePlatterMaxWidthFromConfig:activityCategory:]
+ -[SFAirDropDiscoveryController isCellularUsageEnabled]
+ -[SFAirDropDiscoveryController setCellularUsageEnabled:]
+ -[SFB332SetupObserver updateDeviceInfoWithName:batteryLevel:batteryLevelKnown:edge:orientation:isCharging:]
+ -[SFUILoadedMetadataCollection loadedSerializedMetadatas]
+ -[SFUILoadedMetadataCollection setLoadedSerializedMetadatas:]
+ GCC_except_table8
+ _OBJC_IVAR_$_SFUILoadedMetadataCollection._loadedSerializedMetadatas
+ _SFNotificationAirDropCellularUsageChanged
+ _SFUILinkMetadataSerializationForLocalUseOnly
+ ___101+[SFShareSheetRendering drawingCommandsForMoreListEntryTitle:labelColor:hostConfig:activityCategory:]_block_invoke
+ ___49-[SFUILoadedMetadataCollection _didFinishLoading]_block_invoke
+ ___49-[SFUILoadedMetadataCollection _didFinishLoading]_block_invoke_2
+ ___50-[SFUILoadedMetadataCollection initWithMetadatas:]_block_invoke
+ ___50-[SFUILoadedMetadataCollection initWithMetadatas:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_literal_global.376
+ _avatarImageScale
+ _objc_msgSend$cellularUsageEnabled
+ _objc_msgSend$loadedSerializedMetadatas
+ _objc_msgSend$morePlatterMaxWidthFromConfig:activityCategory:
+ _objc_msgSend$setCellularUsageEnabled:
+ _objc_msgSend$setLoadedSerializedMetadatas:
+ _objc_msgSend$updateDeviceInfoWithName:batteryLevel:batteryLevelKnown:edge:orientation:isCharging:
- +[SFShareSheetRendering drawingCommandsForMoreListEntryTitle:labelColor:hostConfig:]
- +[SFShareSheetRendering morePlatterMaxWidthFromConfig:]
- +[SFUILoadedMetadataCollection _serializeMetadatas:]
- -[SFB332SetupObserver updateDeviceInfoWithName:batteryLevel:batteryLevelKnown:edge:orientation:]
- -[SFUILoadedMetadataCollection latestSerializedMetadatas]
- -[SFUILoadedMetadataCollection setLatestSerializedMetadatas:]
- _OBJC_IVAR_$_SFUILoadedMetadataCollection._latestSerializedMetadatas
- __OBJC_$_CLASS_METHODS_SFUILoadedMetadataCollection
- ___84+[SFShareSheetRendering drawingCommandsForMoreListEntryTitle:labelColor:hostConfig:]_block_invoke
- ___block_literal_global.368
- _objc_msgSend$_serializeMetadatas:
- _objc_msgSend$morePlatterMaxWidthFromConfig:
- _objc_msgSend$setLatestSerializedMetadatas:
- _objc_msgSend$updateDeviceInfoWithName:batteryLevel:batteryLevelKnown:edge:orientation:
CStrings:
+ "Changing cellular usage enabled to %d"
+ "T@\"NSArray\",C,N,V_loadedSerializedMetadatas"
+ "TB,GisCellularUsageEnabled"
+ "_loadedSerializedMetadatas"
+ "cellularUsageEnabled"
+ "d32@0:8@16q24"
+ "did finish serializing loaded metadata:%@"
+ "drawingCommandsForMoreListEntryTitle:labelColor:hostConfig:activityCategory:"
+ "isCellularUsageEnabled"
+ "loadedSerializedMetadatas"
+ "morePlatterMaxWidthFromConfig:activityCategory:"
+ "setCellularUsageEnabled:"
+ "setLoadedSerializedMetadatas:"
+ "updateDeviceInfoWithName:batteryLevel:batteryLevelKnown:edge:orientation:isCharging:"
+ "v16@?0@\"NSArray\"8"
+ "v56@0:8@\"NSString\"16d24B32Q36Q44B52"
+ "v56@0:8@16d24B32Q36Q44B52"
- "Failed to serialize metadata: %@"
- "T@\"NSArray\",C,N,V_latestSerializedMetadatas"
- "_latestSerializedMetadatas"
- "_serializeMetadatas:"
- "drawingCommandsForMoreListEntryTitle:labelColor:hostConfig:"
- "latestSerializedMetadatas"
- "morePlatterMaxWidthFromConfig:"
- "setLatestSerializedMetadatas:"
- "updateDeviceInfoWithName:batteryLevel:batteryLevelKnown:edge:orientation:"
- "v52@0:8@\"NSString\"16d24B32Q36Q44"
- "v52@0:8@16d24B32Q36Q44"

```
