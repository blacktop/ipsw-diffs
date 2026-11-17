## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3610.10.1.0.0
-  __TEXT.__text: 0x76060
+3610.12.1.0.0
+  __TEXT.__text: 0x760e4
   __TEXT.__objc_methlist: 0x36f0
   __TEXT.__const: 0x198
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xb8b9
+  __TEXT.__cstring: 0xb8c5
   __TEXT.__oslogstring: 0xf1bb
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xe0c
Symbols:
+ +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:error:]
+ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:error:]
- +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]
- +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]
Functions:
~ +[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:] : 1756 -> 1776
~ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:] -> +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:error:] : 440 -> 460
~ +[UAFInstrumentationProvider logAvailableAssetDailyStatus] : 256 -> 260
~ +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:] -> +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:error:] : 1336 -> 1384
~ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke : 32 -> 36
~ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke.536 : 108 -> 112
~ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.572 : 632 -> 648
~ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.573 : 32 -> 36
~ sub_20546578c -> sub_205c59804 : 112 -> 124
CStrings:
+ "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:error:]"
+ "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:error:]"
- "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]"
- "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]"
```
