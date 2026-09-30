## bluetoothaudiod

> `/usr/sbin/bluetoothaudiod`

```diff

-350.36.1.0.0
-  __TEXT.__text: 0x5c970
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x9b80
-  __TEXT.__objc_methlist: 0x57d8
+350.38.0.0.0
+  __TEXT.__text: 0x5ea60
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x9f80
+  __TEXT.__objc_methlist: 0x5988
   __TEXT.__const: 0x82c
-  __TEXT.__objc_methname: 0xe4e6
-  __TEXT.__oslogstring: 0x8aad
-  __TEXT.__cstring: 0x55a8
-  __TEXT.__objc_classname: 0x450
-  __TEXT.__objc_methtype: 0x1c47
+  __TEXT.__objc_methname: 0xe846
+  __TEXT.__oslogstring: 0x8b65
+  __TEXT.__cstring: 0x57bc
+  __TEXT.__objc_classname: 0x459
+  __TEXT.__objc_methtype: 0x1c54
   __TEXT.__gcc_except_tab: 0x928
-  __TEXT.__unwind_info: 0xef8
-  __DATA_CONST.__auth_got: 0x4c8
+  __TEXT.__unwind_info: 0xf58
+  __DATA_CONST.__auth_got: 0x4d0
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1430
-  __DATA_CONST.__cfstring: 0x4c00
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__const: 0x1458
+  __DATA_CONST.__cfstring: 0x4ec0
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x200
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x9290
-  __DATA.__objc_selrefs: 0x3080
-  __DATA.__objc_ivar: 0x648
-  __DATA.__objc_data: 0xdc0
+  __DATA.__objc_const: 0x9360
+  __DATA.__objc_selrefs: 0x3180
+  __DATA.__objc_ivar: 0x64c
+  __DATA.__objc_data: 0xe10
   __DATA.__data: 0x698
   __DATA.__common: 0x28
   __DATA.__bss: 0xb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84450D47-3CF3-3F5E-B9E8-D1A368749F50
-  Functions: 2066
-  Symbols:   305
-  CStrings:  4783
+  UUID: 505EC61A-0D61-310E-BB59-090F8E9BEE72
+  Functions: 2104
+  Symbols:   306
+  CStrings:  4868
 
Symbols:
+ _objc_opt_new
CStrings:
+ "@\"Metadata\""
+ "ASE ID %d contextTypes: 0x%02X CCID size: %d isSink: %d"
+ "C44@0:8B16@20@28^@36"
+ "Can't run Acceptor Interface Requests when AccpetorInterface not found."
+ "Can't run Acceptor Interface Requests when CAP not found."
+ "Can't run Acceptor Interface Requests while not in test mode"
+ "Can't run Acceptor Interface Requests while not in test mode."
+ "CharIndex"
+ "ContentCtrlID"
+ "Custom Audio Config Setting requires input"
+ "HAPReadActivePresetIndex:"
+ "HAPReadHearingAidFeatures:"
+ "Metadata"
+ "Name of preset %d not writable"
+ "Num of specified ASE IDs (%lu) doesn't match num of Metadata (%lu)"
+ "Preset %d not available"
+ "PublishHAL"
+ "ReceiverStopReady"
+ "Running in Test mode not updating volume"
+ "SinkAseID"
+ "SourceAseID"
+ "T@\"Metadata\",&,N,V_metadata"
+ "_metadata"
+ "acceptorInterfaceRequest"
+ "addChannelConfigWithCodecIndex:withContextType:withCCID:withDirection:"
+ "didWriteValueForCharacteristic: %@"
+ "handleAcceptorInterfaceRequest:"
+ "indexOfObjectIdenticalTo:"
+ "interfaceRequest"
+ "metadata"
+ "objectAtIndex:"
+ "presetAvailable:"
+ "presetNameWritable:"
+ "readActPresetIndex"
+ "readActivePresetIndex"
+ "readAvailableContexts"
+ "readHAFeatures"
+ "readHearingAidFeatures"
+ "readSinkASE"
+ "readSinkASE:"
+ "readSinkAudioLocations"
+ "readSourceASE"
+ "readSourceASE:"
+ "readSourceAudioLocations"
+ "readSupportedContexts"
+ "sendEnableRequestForDevice:withSnkAseID:withSrcAseID:"
+ "sendEnableRequestWithSnkAseID:WithSrcAseID:"
+ "sendEnableRequestWithSnkAseID:withSrcAseID:"
+ "sendReadActivePresetIndex"
+ "sendReadAvailableContexts"
+ "sendReadHearingAidFeatures"
+ "sendReadSinkASE:"
+ "sendReadSinkAudioLocations"
+ "sendReadSourceASE:"
+ "sendReadSourceAudioLocations"
+ "sendReadSupportedContexts"
+ "sendReceiverStopReadyRequestForDevice:"
+ "sendUpdateMetadataRequestForDirection:OptionalASE:withMetadata:withLTVData:"
+ "sendWriteASEControlPoint"
+ "sendWriteSinkAudioLocations"
+ "sendWriteSourceAudioLocations"
+ "setMetadata:"
+ "v36@0:8C16S20@24B32"
+ "writeASEControlPoint"
+ "writeSinkAudioLocations"
+ "writeSourceAudioLocations"
- "ASE ID %d contextTypes: 0x%02X isSink: %d"
- "C44@0:8B16^@20^@28^@36"
- "Num of specified ASE IDs (%lu) doesn't match num of context types (%lu)"
- "Writable Preset records are not supported by peripheral %@ "
- "addChannelConfigWithCodecIndex:withContextType:withDirection:"
- "sendEnableRequest"
- "sendEnableRequestForDevice:"
- "sendUpdateMetadataRequestForDirection:OptionalASE:withMetaData:withLTVData:"
- "unsignedShortValue"
- "v28@0:8C16S20B24"

```
