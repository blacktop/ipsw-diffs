## uarpd

> `/usr/libexec/uarpd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-1587.0.21.0.0
-  __TEXT.__text: 0xa9140
+1587.0.27.0.0
+  __TEXT.__text: 0xaa678
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0xa3a0
-  __TEXT.__objc_methlist: 0x8678
-  __TEXT.__objc_methname: 0xf393
-  __TEXT.__objc_classname: 0x1ce4
-  __TEXT.__cstring: 0xad03
-  __TEXT.__objc_methtype: 0x2a49
+  __TEXT.__objc_stubs: 0xa560
+  __TEXT.__objc_methlist: 0x86a8
+  __TEXT.__objc_methname: 0xf20e
+  __TEXT.__objc_classname: 0x1cf6
+  __TEXT.__cstring: 0xaefc
+  __TEXT.__objc_methtype: 0x2a72
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x8e2f
+  __TEXT.__oslogstring: 0x9052
   __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__unwind_info: 0x2340
-  __DATA_CONST.__const: 0x1140
-  __DATA_CONST.__cfstring: 0x5440
-  __DATA_CONST.__objc_classlist: 0x600
+  __TEXT.__unwind_info: 0x2398
+  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__cfstring: 0x5460
+  __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x5e8
+  __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x648
-  __DATA.__objc_const: 0x10918
-  __DATA.__objc_selrefs: 0x30f8
-  __DATA.__objc_ivar: 0xb90
-  __DATA.__objc_data: 0x3c00
+  __DATA.__objc_const: 0x105e8
+  __DATA.__objc_selrefs: 0x3170
+  __DATA.__objc_ivar: 0xb30
+  __DATA.__objc_data: 0x3c50
   __DATA.__data: 0x548
   __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3943
-  Symbols:   208
-  CStrings:  4924
+  Functions: 3961
+  Symbols:   209
+  CStrings:  4939
 
Symbols:
+ _NSURLContentModificationDateKey
CStrings:
+ "%02ld-%02ld-%02ld"
+ "%04ld-%02ld-%02ld"
+ "%s: All ripe files pruned at %@"
+ "%s: Failed to create pruner for %@"
+ "%s: Failed to instantiate UARPSuperBinaryPayloadLayer3 at index %lu for %@"
+ "%s: Hit max prunings at %@"
+ "%s: Nothing to prune at %@"
+ "%s: Pruned %lu files / directories this iteration"
+ "%s: Pruning all directories"
+ "%s: Pruning all files under %@"
+ "%s: Set pruning timer with start time of %llu, interval time %llu, leeway time %llu"
+ "%s: Stop pruning timer"
+ "%s: Totally pruned %lu files / directories"
+ "%s: could not instantiate UARPSuperBinaryLayer3 for tag %@ on endpoint %@"
+ "%s: could not instantiate UARPSuperBinaryPayloadLayer3 for asset %@ on endpoint %@"
+ "%s: for pruning %@"
+ "%s: processSuperBinaryPropertyList: failed to process"
+ "-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackUnsolicitedDynamicAssetOffered:assetTag:]_block_invoke"
+ "-[UARPPruner prune]"
+ "-[UARPPrunerManager addPrunerWithFolderPath:prunerType:maxFileAge:]"
+ "-[UARPPrunerManager pruneAssets]_block_invoke"
+ "-[UARPPrunerManager pruneDatabaseEntries]_block_invoke"
+ "-[UARPPrunerManager prunePacketCaptures]_block_invoke"
+ "-[UARPPrunerManager startPruning]_block_invoke"
+ "-[UARPPrunerManager stopPruningInternal]"
+ "-[UARPPrunerManager timerFired]"
+ "@\"UARPPrunerManager\""
+ "@40@0:8@16Q24d32"
+ "File %@ is not old enough to prune; last modified date %@"
+ "PLST"
+ "Pruned Expired File at %@; last modified date %@"
+ "Q32@0:8@16@24"
+ "TQ,R,V_prunerType"
+ "UARPPrunerManager"
+ "_pruneInterval"
+ "_prunerManager"
+ "_prunerType"
+ "_pruners"
+ "addPrunerWithFolderPath:prunerType:maxFileAge:"
+ "endpointControllerStartPruning"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "getResourceValue:forKey:error:"
+ "initWithPruneInterval:"
+ "initWithURL:prunerType:maxFileAge:"
+ "processSuperBinaryPropertyList:"
+ "processURL:pruneBaseTime:"
+ "prune"
+ "pruneAll"
+ "pruneAssets"
+ "pruneDatabaseEntries"
+ "pruneNow"
+ "prunePacketCaptures"
+ "prunerType"
+ "q24@?0@\"NSURL\"8@\"NSURL\"16"
+ "siriAssetsFolder"
+ "sortedArrayUsingComparator:"
+ "stopPruningInternal"
+ "timerFired"
+ "v40@0:8@16Q24d32"
- "%s: Error creating payload at index %lu"
- "%s: Failed to create payload at index %lu"
- "@\"UARPPruner\""
- "@32@0:8@16d24"
- "Evaluate %@ for pruning"
- "File %@ is not old enough to prune"
- "Nothing left to prune, stopping pruning for %@"
- "Pruning Expired File at %@"
- "T@\"NSString\",R,V_analyticsAssetsFolder"
- "T@\"NSString\",R,V_assetsFolder"
- "T@\"NSString\",R,V_cachedAssetsFolder"
- "T@\"NSString\",R,V_crashAssetsFolder"
- "T@\"NSString\",R,V_endpointDatabaseFolder"
- "T@\"NSString\",R,V_heySiriAssetsFolder"
- "T@\"NSString\",R,V_logsAssetsFolder"
- "T@\"NSString\",R,V_mappedAnalyticsAssetsFolder"
- "T@\"NSString\",R,V_packetCaptureFolder"
- "T@\"NSString\",R,V_personalizationAssetsFolder"
- "T@\"NSString\",R,V_sysdiagnoseApprovedFolder"
- "T@\"NSString\",R,V_sysdiagnoseFolder"
- "T@\"NSString\",R,V_tmapDatabaseFolder"
- "T@\"NSString\",R,V_voiceAssistAssetsFolder"
- "_analyticsAssetsPruner"
- "_assetsPruner"
- "_cachedAssetsPruner"
- "_crashAssetsPruner"
- "_endpointDatabasePruner"
- "_heySiriAssetsPruner"
- "_logsAssetsPruner"
- "_mappedAnalyticsAssetsPruner"
- "_packetCapturePruner"
- "_personalizationAssetsPruner"
- "_pruneBaseTime"
- "_sysdiagnoseApprovedPruner"
- "_sysdiagnosePruner"
- "_tmapDatabasePruner"
- "_voiceAssistAssetsPruner"
- "cancelTimer"
- "date"
- "initWithURL:maxFileAge:"
- "timer interval for pruning %@"
- "timerInterval"
- "yyyy-MM-dd-HH-mm-ss"
- "yyyy-MM-dd-hh-mm-ss"
```
