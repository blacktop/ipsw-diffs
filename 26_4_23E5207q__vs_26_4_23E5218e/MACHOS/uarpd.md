## uarpd

> `/usr/libexec/uarpd`

```diff

-1345.100.155.0.0
-  __TEXT.__text: 0x97a24
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_stubs: 0x89a0
-  __TEXT.__objc_methlist: 0x75c8
-  __TEXT.__objc_methname: 0xcea8
-  __TEXT.__objc_classname: 0x18da
-  __TEXT.__objc_methtype: 0x28b3
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x94d7
-  __TEXT.__oslogstring: 0x72c2
-  __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__unwind_info: 0x1d98
-  __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0xfb8
-  __DATA_CONST.__cfstring: 0x4b60
-  __DATA_CONST.__objc_classlist: 0x528
+1345.100.162.0.0
+  __TEXT.__text: 0x995e8
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_stubs: 0x8c00
+  __TEXT.__objc_methlist: 0x76c8
+  __TEXT.__objc_methname: 0xd168
+  __TEXT.__objc_classname: 0x18e8
+  __TEXT.__objc_methtype: 0x28c3
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x9583
+  __TEXT.__oslogstring: 0x76b8
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__unwind_info: 0x1de0
+  __DATA_CONST.__auth_got: 0x530
+  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__const: 0xfc0
+  __DATA_CONST.__cfstring: 0x4b80
+  __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x510
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xe948
-  __DATA.__objc_selrefs: 0x2a18
-  __DATA.__objc_ivar: 0xa38
-  __DATA.__objc_data: 0x3390
+  __DATA.__objc_const: 0xec68
+  __DATA.__objc_selrefs: 0x2ab8
+  __DATA.__objc_ivar: 0xa84
+  __DATA.__objc_data: 0x33e0
   __DATA.__data: 0x548
   __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: A91440EA-FA05-36F4-B1B3-1AB4D9FB2D49
-  Functions: 3436
-  Symbols:   226
-  CStrings:  4884
+  UUID: 0D838B4C-9B8A-33FB-A55C-2D627067A405
+  Functions: 3476
+  Symbols:   228
+  CStrings:  4956
 
Symbols:
+ _OBJC_CLASS_$_NSCalendar
+ _dispatch_queue_attr_make_with_autorelease_frequency
CStrings:
+ "%s: (SIRI) Adding UARPSiriModel to downloaded models ; locale %@, hash %@"
+ "%s: (SIRI) Adding UARPSiriModel to preinstalled models ; locale %@, hash %@"
+ "%s: (SIRI) Adding voice trigger model to downloaded models ; locale %@, hash %@"
+ "%s: (SIRI) Adding voice trigger model to preinstalled models ; locale %@, hash %@"
+ "%s: (SIRI) Engine Capability %lu"
+ "%s: (SIRI) Engine version %@"
+ "%s: (SIRI) dlModels; %@"
+ "%s: (SIRI) piModels; %@"
+ "%s: Providing SandBox Extension for CRSH Asset at URL: %@"
+ "%s: Providing SandBox Extension for LOGS Asset at URL: %@"
+ "%s: Providing SandBox Extension through Direct Endpoint (%@)"
+ "%s: Unable to checl for best model"
+ "%s: Unable to expand SuperBinary"
+ "%s: Unable to process HSML asset"
+ "%s: Unable to write HSML Dynamic Asset"
+ "%s: bad model type class for locale %@, hash %@"
+ "%s: bad model type class for model hash"
+ "%s: bad model type class for model locale, hash %@"
+ "%s: could not create UARPSiriModel for locale %@, hash %@"
+ "%s: no model hash tlv"
+ "%s: no model locale tlv, hash %@"
+ "%s: no model type TLV for locale %@, hash %@"
+ "-[UARPHostEndpoint tapToRadarProvideCRSHAssets]"
+ "-[UARPHostEndpoint tapToRadarProvideLOGSAssets]"
+ "-[UARPHostManager commonProcessHSML:]"
+ "-[UARPHostManager processHSML:outputURL:]"
+ "-[UARPSiriAsset expandSuperBinaryPayload:]"
+ "@\"UARPPruner\""
+ "@32@0:8@16d24"
+ "Days From Compose"
+ "Evaluate %@ for pruning"
+ "File %@ is not old enough to prune"
+ "Nothing left to prune, stopping pruning for %@"
+ "Pruning Expired File at %@"
+ "T@\"NSURL\",R,V_pruningURL"
+ "Td,R,V_maxFileAge"
+ "UARPPruner"
+ "_analyticsAssetsPruner"
+ "_assetsPruner"
+ "_cachedAssetsPruner"
+ "_crashAssetsPruner"
+ "_heySiriAssetsPruner"
+ "_isPruning"
+ "_logsAssetsPruner"
+ "_mappedAnalyticsAssetsPruner"
+ "_maxFileAge"
+ "_packetCapturePruner"
+ "_personalizationAssetsPruner"
+ "_pruneBaseTime"
+ "_pruningURL"
+ "_sysdiagnoseApprovedPruner"
+ "_sysdiagnosePruner"
+ "_timer"
+ "_tmapDatabasePruner"
+ "_voiceAssistAssetsPruner"
+ "cancelTimer"
+ "com.apple.uarp.endpoint.pruning"
+ "commonProcessHSML:"
+ "component:fromDate:"
+ "crashAssetsFolder"
+ "currentCalendar"
+ "d"
+ "d16@0:8"
+ "expandSuperBinaryPayload:"
+ "expandSuperBinaryPayloads"
+ "hostpruner"
+ "initWithDaysFromNow:"
+ "initWithDict:"
+ "initWithURL:maxFileAge:"
+ "localizedDescription"
+ "logsAssetsFolder"
+ "maxFileAge"
+ "processHSML:outputURL:"
+ "pruningURL"
+ "setSupportsJustSiri:"
+ "startPruning"
+ "startPruningTempFiles"
+ "stopPruning"
+ "stopPruningTempFiles"
+ "tapToRadarProvideCRSHAssets"
+ "tapToRadarProvideLOGSAssets"
+ "timer interval for pruning %@"
+ "timerInterval"
+ "writeToURL:options:error:"
- "%s: %lu files to be pruned from %@"
- "%s: Could not prune folder %@"
- "%s: Saving Crash Binary File %@ to send later"
- "%s: Saving Crash Report File %@ to send later"
- "-[UARPHostManager commonProcessHSML:hostEndpoint:]"
- "-[UARPHostManager pruneFolder:timeNow:maxFileAge:error:]"
- "B48@0:8@16@24d32o^@40"
- "Removing Expired File at %@"
- "_tapToRadarCRSHAssetURLs"
- "commonProcessHSML:hostEndpoint:"
- "processHSML:hostEndpoint:"
- "pruneFolder:timeNow:maxFileAge:error:"
- "reverseObjectEnumerator"

```
