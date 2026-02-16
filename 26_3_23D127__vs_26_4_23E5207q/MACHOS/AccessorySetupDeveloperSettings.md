## AccessorySetupDeveloperSettings

> `/System/Library/PreferenceBundles/AccessorySetupDeveloperSettings.bundle/AccessorySetupDeveloperSettings`

```diff

-323.7.0.0.0
-  __TEXT.__text: 0x1505c
-  __TEXT.__auth_stubs: 0x1070
+324.20.1.1.1
+  __TEXT.__text: 0x20d28
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_stubs: 0x4a0
   __TEXT.__objc_methlist: 0x1bc
-  __TEXT.__cstring: 0x799
-  __TEXT.__const: 0xd80
-  __TEXT.__constg_swiftt: 0x58c
-  __TEXT.__swift5_typeref: 0x1359
-  __TEXT.__swift5_reflstr: 0x302
-  __TEXT.__swift5_fieldmd: 0x33c
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x54
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__objc_methname: 0x62f
-  __TEXT.__oslogstring: 0x45c
-  __TEXT.__swift5_capture: 0x188
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methtype: 0x283
-  __TEXT.__unwind_info: 0x4c8
-  __TEXT.__eh_frame: 0x438
-  __DATA_CONST.__auth_got: 0x838
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__auth_ptr: 0x3c8
-  __DATA_CONST.__const: 0xa90
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__cstring: 0x934
+  __TEXT.__const: 0x1404
+  __TEXT.__constg_swiftt: 0x78c
+  __TEXT.__swift5_typeref: 0x1b82
+  __TEXT.__swift5_reflstr: 0x804
+  __TEXT.__swift5_fieldmd: 0x6d0
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__objc_classname: 0x23f
+  __TEXT.__objc_methname: 0xa0d
+  __TEXT.__objc_methtype: 0x2f5
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__oslogstring: 0x835
+  __TEXT.__swift5_capture: 0x1b0
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__eh_frame: 0x810
+  __DATA_CONST.__auth_got: 0x918
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__auth_ptr: 0x400
+  __DATA_CONST.__const: 0x13e0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x5f8
-  __DATA.__objc_selrefs: 0x210
+  __DATA.__objc_const: 0x800
+  __DATA.__objc_selrefs: 0x220
   __DATA.__objc_data: 0x300
-  __DATA.__data: 0xb20
+  __DATA.__data: 0xec8
   __DATA.__common: 0x58
-  __DATA.__bss: 0xb00
+  __DATA.__bss: 0x1220
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 857AD2A7-D6C6-37DF-B38C-93C8FCCC5CF2
-  Functions: 413
-  Symbols:   149
-  CStrings:  188
+  UUID: 1F6E6973-D238-3CD0-8514-3EB5E6D9C5A6
+  Functions: 572
+  Symbols:   153
+  CStrings:  254
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ _objc_release_x28
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_storeEnumTagMultiPayload
- _malloc
CStrings:
+ "AccessorySetupDeveloperSettings"
+ "An unexpected error occurred while decoding file %s: %s"
+ "Analysis result showing suggested threshold"
+ "Calculated optimal threshold: %ld dBm"
+ "Channel validity check failed for placement %s. Samples contained channels outside 37, 38, 39."
+ "Could not parse file %s as either plain JSON or Base64-encoded JSON."
+ "Data Collection: %@"
+ "Error Shown when the Scan timed out and nodevices of interest were found"
+ "Error message when analysis session folder is not found"
+ "Error shown when Bluetooth is turned off or unavailable"
+ "Error shown when multiple peripherals were discovered"
+ "Error shown when scanning is inprogress"
+ "Error when bit width is invalid"
+ "Error when data is insufficient for analysis"
+ "Error when decimal value is out of range for specified bit width"
+ "Error when no JSON files are found for analysis"
+ "Error when no valid samples are loaded for analysis"
+ "Error when session folder is not found for analysis"
+ "Failed to convert threshold %ld to %ld-bit signed hex: %{public}s. Falling back to standard signed hex display."
+ "Generated %ld filtered data points."
+ "Generic error prefix for analysis results"
+ "Loaded %ld total samples for analysis."
+ "Message shown while analysis is calculating"
+ "Per-channel sample count validation passed."
+ "RSSI spread validation passed."
+ "Scan task finished (cleanup)."
+ "Validation Failed: Could not determine RSSI spread for channel %ld (no samples?)."
+ "Validation Failed: Could not determine total RSSI spread (no samples?)."
+ "Validation Failed: Insufficient samples for channel %ld. Expected at least %ld, got %ld."
+ "Validation Failed: RSSI spread for channel %ld (%lddB) exceeded %lddB."
+ "Validation Failed: Total RSSI spread (%lddB) exceeded %lddB."
+ "_TtC31AccessorySetupDeveloperSettingsP33_25614F34AB244A913F73A9E516F25EA419ResourceBundleClass"
+ "_TtCV31AccessorySetupDeveloperSettings22PathlossAnalysisEngineP33_E7B98B2B2150CDEBF5CE8CEB0E38B0E917NIMaxOfMeanFilter"
+ "_analysisResult"
+ "_currentStatus"
+ "_isAnalyzing"
+ "analysis.calculating"
+ "analysis.errorPrefix"
+ "analysis.errorSessionFolderNotFound"
+ "analysis.header"
+ "analysis.suggestedThreshold"
+ "analysisError.folderNotFound"
+ "analysisError.insufficientData"
+ "analysisError.noJSONFilesFound"
+ "analysisError.noSamplesLoaded"
+ "bufferSize"
+ "bundleWithIdentifier:"
+ "button.export"
+ "button.exported"
+ "button.processResults"
+ "button.processing"
+ "com.apple.accessorysetupdevelopersettings"
+ "distance.1m"
+ "distance.20cm"
+ "distance.50cm"
+ "distanceItems"
+ "error.bluetoothNotReady"
+ "error.invalidBitWidth"
+ "error.multiplePeripherals"
+ "error.scanInProgress"
+ "error.scanTimeout"
+ "error.valueOutOfRangeForBitWidth"
+ "mainBundle"
+ "maxRssiSpread"
+ "placement.bottom"
+ "placement.left"
+ "placement.right"
+ "placement.top"
+ "placementItems"
+ "requiredChannels"
+ "requiredPerChannelSamples"
+ "samples"
+ "selectDistance.footer"
+ "selectDistance.header"
+ "session.header"
+ "status.channelValidityFailed"
+ "status.collectingSamples"
+ "status.collectionComplete"
+ "status.footer"
+ "status.header"
+ "status.insufficientPerChannelSamples"
+ "status.ready"
+ "status.rssiSpreadTooWide"
+ "status.savingSamples"
+ "status.startingCollection"
- "A scan is already in progress"
- "Bluetooth is not powered on or available"
- "Collecting samples..."
- "Collection complete"
- "Collection complete; saving samples..."
- "Collection failed: "
- "Collection failed: Multiple advertising devices found"
- "Collection timed out; please try again"
- "Data Collection: "
- "For each distance, place the accessory at the specified distance from this device and complete all four placements\n\nNote: Do not press back arrow until all tests are completed and exported"
- "Refer to spec doc for detailed placement instructions"
- "Scan task finished."
- "Starting Collection..."
- "_statusMessage"
- "distanceTitles"
- "placementTitles"

```
