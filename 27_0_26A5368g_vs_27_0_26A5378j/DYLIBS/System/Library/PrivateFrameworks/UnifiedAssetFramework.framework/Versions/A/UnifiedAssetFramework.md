## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework`

```diff

-  __TEXT.__text: 0x7f99c
-  __TEXT.__objc_methlist: 0x35d8
+  __TEXT.__text: 0x7fc30
+  __TEXT.__objc_methlist: 0x3658
   __TEXT.__const: 0x198
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xb6aa
-  __TEXT.__oslogstring: 0xf0d0
+  __TEXT.__cstring: 0xb7ad
+  __TEXT.__oslogstring: 0xeffd
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xe30
-  __TEXT.__unwind_info: 0x1210
+  __TEXT.__unwind_info: 0x1228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x868
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2648
+  __DATA_CONST.__objc_selrefs: 0x2678
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x130
-  __DATA_CONST.__got: 0x600
-  __AUTH_CONST.__const: 0x1cf8
-  __AUTH_CONST.__cfstring: 0x4ee0
-  __AUTH_CONST.__objc_const: 0x4570
+  __DATA_CONST.__got: 0x608
+  __AUTH_CONST.__const: 0x1d28
+  __AUTH_CONST.__cfstring: 0x5040
+  __AUTH_CONST.__objc_const: 0x46c0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x7c8
-  __AUTH.__objc_data: 0x520
+  __AUTH.__objc_data: 0x5c0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x320
   __DATA.__data: 0x2c0
   __DATA.__bss: 0x38
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xb90
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x260
-  __DATA_DIRTY.__common: 0x60
+  __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1506
-  Symbols:   3944
-  CStrings:  2736
+  Functions: 1514
+  Symbols:   3969
+  CStrings:  2756
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[UAFAssetOriginReport sourceStringForEntry:]
+ +[UAFAutoAssetHistory persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:atomicInstanceMetadata:originReport:]
+ +[UAFBiomeInstrumenter logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetOriginReport:assetSetDailyStatusEventType:]
+ +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]
+ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]
+ -[UAFAssetOriginReport .cxx_destruct]
+ -[UAFAssetOriginReport _originDictForMAEntry:]
+ -[UAFAssetOriginReport _populateFromMAReport:error:errorOut:]
+ -[UAFAssetOriginReport atomicInstanceUUID]
+ -[UAFAssetOriginReport initWithAutoAssetSet:atomicInstance:atomicEntries:error:]
+ -[UAFAssetOriginReport originEntryForSpecifier:]
+ -[UAFAssetOriginReport originInfoForSpecifier:]
+ -[UAFAssetOriginReport reportValid]
+ -[UAFAssetOriginReport underlyingMAReport]
+ GCC_except_table114
+ GCC_except_table123
+ OBJC_IVAR_$_UAFAssetOriginReport._assetSetIdentifier
+ OBJC_IVAR_$_UAFAssetOriginReport._atomicInstanceUUID
+ OBJC_IVAR_$_UAFAssetOriginReport._specifierToOriginEntry
+ OBJC_IVAR_$_UAFAssetOriginReport._underlyingMAReport
+ _OBJC_CLASS_$_UAFAssetOriginReport
+ _OBJC_METACLASS_$_UAFAssetOriginReport
+ __OBJC_$_CLASS_METHODS_UAFAssetOriginReport
+ __OBJC_$_INSTANCE_METHODS_UAFAssetOriginReport
+ __OBJC_$_INSTANCE_VARIABLES_UAFAssetOriginReport
+ __OBJC_$_PROP_LIST_UAFAssetOriginReport
+ __OBJC_CLASS_RO_$_UAFAssetOriginReport
+ __OBJC_METACLASS_RO_$_UAFAssetOriginReport
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0l
+ _objc_msgSend$_emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:
+ _objc_msgSend$_originDictForMAEntry:
+ _objc_msgSend$_populateFromMAReport:error:errorOut:
+ _objc_msgSend$initWithAutoAssetSet:atomicInstance:atomicEntries:error:
+ _objc_msgSend$logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetOriginReport:assetSetDailyStatusEventType:
+ _objc_msgSend$logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:
+ _objc_msgSend$nameOfBasicOriginType:
+ _objc_msgSend$originEntryForSpecifier:
+ _objc_msgSend$originInfoForSpecifier:
+ _objc_msgSend$persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:atomicInstanceMetadata:originReport:
+ _objc_msgSend$sourceStringForEntry:
+ _objc_msgSend$underlyingMAReport
- +[UAFAutoAssetHistory persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:]
- +[UAFAutoAssetManager assetSetEmpty:]
- +[UAFBiomeInstrumenter _collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:]
- +[UAFBiomeInstrumenter logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:]
- +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]
- +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]
- GCC_except_table115
- GCC_except_table124
- ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke_2
- _objc_msgSend$_collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:
- _objc_msgSend$_emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:
- _objc_msgSend$assetSetEmpty:
- _objc_msgSend$catalogCachedAssetSetID
- _objc_msgSend$logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:
- _objc_msgSend$logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:
- _objc_msgSend$newerAtomicInstanceDiscovered
- _objc_msgSend$persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:
CStrings:
+ "%s UAFAssetOriginReport: lockedAtomicEntriesOriginReportSync returned nil for '%{public}@'/%{public}@: %{public}@"
+ "+[UAFAutoAssetHistory persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:atomicInstanceMetadata:originReport:]"
+ "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetOriginReport:assetSetDailyStatusEventType:]"
+ "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]"
+ "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetOriginReport:assetSetDailyStatusEventType:]"
+ "-[UAFAssetOriginReport _populateFromMAReport:error:errorOut:]"
+ "BMUAFAssetUAFAssetSource"
+ "MAAutoAssetSetOriginEntry"
+ "UAFDiagnostics"
+ "_Factory_Install"
+ "_Over_The_Air"
+ "_PreSoftware_Update_Staging"
+ "assetAvailableOSBuild"
+ "assetDownloadedOSBuild"
+ "atomicInstanceMetadata"
+ "atomicInstanceUUID"
+ "fromFactory"
+ "fromPSUS"
- "%s Auto asset set %{public}@ is desired but newest published atomic instance %{public}@ from catalog %{public}@ contains no assets"
- "%s Auto asset set %{public}@ is desired but no atomic instance is available"
- "%s Could not retrieve the asset origin metadata for auto asset set %{public}@ atomic instance %{public}@ : %{public}@"
- "+[UAFAutoAssetHistory persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:]"
- "+[UAFBiomeInstrumenter _collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:]"
- "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:]"
- "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]"
- "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]"
- "Collection of Auto Asset Set Origin"

```
