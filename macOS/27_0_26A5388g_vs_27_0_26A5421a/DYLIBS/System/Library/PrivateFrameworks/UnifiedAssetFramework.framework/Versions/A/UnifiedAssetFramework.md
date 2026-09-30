## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework`

```diff

-3600.74.1.0.0
-  __TEXT.__text: 0x801c8
+3600.77.1.0.0
+  __TEXT.__text: 0x801cc
   __TEXT.__objc_methlist: 0x3670
   __TEXT.__const: 0x198
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xb7e7
+  __TEXT.__cstring: 0xb7de
   __TEXT.__oslogstring: 0xf115
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xe30
Symbols:
+ -[UAFAssetOriginReport _populateFromMAReport:error:]
+ _objc_msgSend$_populateFromMAReport:error:
- -[UAFAssetOriginReport _populateFromMAReport:error:errorOut:]
- _objc_msgSend$_populateFromMAReport:error:errorOut:
Functions:
~ -[UAFSubscriptionStoreManager _openDatabase:] : 2792 -> 2784
~ -[UAFAssetOriginReport initWithAutoAssetSet:atomicInstance:atomicEntries:error:] : 464 -> 484
~ -[UAFAssetOriginReport _populateFromMAReport:error:errorOut:] -> -[UAFAssetOriginReport _populateFromMAReport:error:] : 1196 -> 1188
CStrings:
+ "-[UAFAssetOriginReport _populateFromMAReport:error:]"
- "-[UAFAssetOriginReport _populateFromMAReport:error:errorOut:]"
```
