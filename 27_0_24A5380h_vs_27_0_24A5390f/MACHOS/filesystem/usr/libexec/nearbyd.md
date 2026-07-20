## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-560.0.0.0.0
-  __TEXT.__text: 0x54dce4
+564.0.0.0.0
+  __TEXT.__text: 0x54fc54
   __TEXT.__auth_stubs: 0x30d0
-  __TEXT.__objc_stubs: 0x16b80
-  __TEXT.__init_offsets: 0x6fc
-  __TEXT.__objc_methlist: 0xf404
-  __TEXT.__gcc_except_tab: 0x54538
-  __TEXT.__const: 0x3e6260
-  __TEXT.__cstring: 0x38cec
-  __TEXT.__objc_methname: 0x22e85
-  __TEXT.__oslogstring: 0x62465
-  __TEXT.__objc_classname: 0x204e
-  __TEXT.__objc_methtype: 0x221fd
+  __TEXT.__objc_stubs: 0x16dc0
+  __TEXT.__init_offsets: 0x6f8
+  __TEXT.__objc_methlist: 0xf504
+  __TEXT.__gcc_except_tab: 0x54774
+  __TEXT.__const: 0x3fa810
+  __TEXT.__cstring: 0x3890c
+  __TEXT.__objc_methname: 0x230e5
+  __TEXT.__oslogstring: 0x629c5
+  __TEXT.__objc_classname: 0x202e
+  __TEXT.__objc_methtype: 0x2229d
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x7ec
   __TEXT.__swift5_capture: 0x574

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
-  __TEXT.__unwind_info: 0x1cbf8
+  __TEXT.__unwind_info: 0x1cc18
   __TEXT.__eh_frame: 0x5a0
-  __DATA_CONST.__const: 0x1f160
-  __DATA_CONST.__cfstring: 0x171c0
-  __DATA_CONST.__objc_classlist: 0x630
+  __DATA_CONST.__const: 0x1f240
+  __DATA_CONST.__cfstring: 0x17240
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x530
-  __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__objc_arrayobj: 0x210
+  __DATA_CONST.__objc_superrefs: 0x528
+  __DATA_CONST.__objc_arraydata: 0x480
+  __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_intobj: 0x978
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__auth_got: 0x1880
   __DATA_CONST.__got: 0xe50
   __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x1b148
-  __DATA.__objc_selrefs: 0x6f28
-  __DATA.__objc_ivar: 0x1994
-  __DATA.__objc_data: 0x4978
+  __DATA.__objc_const: 0x1b1b8
+  __DATA.__objc_selrefs: 0x6fc0
+  __DATA.__objc_ivar: 0x19a8
+  __DATA.__objc_data: 0x4928
   __DATA.__data: 0x41ac
-  __DATA.__bss: 0xe720
-  __DATA.__common: 0xe60
+  __DATA.__bss: 0xe680
+  __DATA.__common: 0xe70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23361
+  Functions: 23388
   Symbols:   1307
-  CStrings:  19693
+  CStrings:  19733
 
CStrings:
+ "#btcs,needsRestrictedStateOperation: %@"
+ "#roseprovider,CMAM is disabled"
+ "#ses-btcs,Range not sent to update engine: range %.2f m, error code %d"
+ "#ses-btcs,Sending to update engine: range %.2f m, error code %d"
+ "@84@0:8@16d24@32@40@48^v56^{CSRange=dddidddddI}64^v72I80"
+ "@max.self"
+ "AppStateMonitor is required to check if client is on restricted state operation allowlist."
+ "B32@0:8@16d24"
+ "BTCSFusionConfig"
+ "BTCSFusionConfig initialized to: %ld (%s)"
+ "BTCSFusionConfig invalid value %ld, defaulting to SingleCalib"
+ "BTCSRangeAlgorithmSelect defaulting to: 3 (Fused)"
+ "BTCSRangeAlgorithmSelect initialized to: %ld (Fused)"
+ "Fused range %.4f m exceeds 30m, flagging RangeNotAvailable"
+ "LE"
+ "LE InputIQNotMatch — unexpected tone count, should not happen in production"
+ "LE uncertainty: %.4f (meanRSSI=%.1f dBm, maxRssi=%.1f dBm, d=%.2f m)"
+ "LE upper bound: range=%.4f m errorCode=%d"
+ "MedianCalib"
+ "MedianCalibTrans"
+ "Missing tones detected in active range [%u, %u) — measurement quality degraded"
+ "Near-field claim %.2f m rejected: maxRssi %.1f dBm < %.1f dBm threshold"
+ "RSSI calibration refined (median): rssi0=%.1f dBm [%.1f, %.1f, %.1f]"
+ "RSSI calibration sample 1: rssi0=%.1f dBm (leUBRange=%.2f m maxRssi=%.1f dBm)"
+ "SR"
+ "SR Engine: RSSIMismatch — RSSI %.1f dBm at %.2f m in bottom %.0f%% (CDF = %.4f, predicted mean %.1f dBm)"
+ "SR Engine: Rayleigh model at %.2f m — mean RSSI = %.1f dBm, CDF(%.1f dBm) = %.4f"
+ "SR Engine: mode0_rssi_max = %.1f dBm"
+ "SingleCalib"
+ "TQ,N,V_fusedErrorCode"
+ "TQ,N,V_fusionMode"
+ "TQ,N,V_leErrorCode"
+ "TQ,N,V_srErrorCode"
+ "TQ,N,V_srTrackerCategory"
+ "Td,N,V_eventTime"
+ "Td,N,V_fusedRange"
+ "Td,N,V_leUncertainty"
+ "Td,N,V_srUncertainty"
+ "_calib"
+ "_clientInterestedInDeviceAngleState"
+ "_eventTime"
+ "_fusedErrorCode"
+ "_fusedRange"
+ "_fusionMode"
+ "_isClientOnBTCSRestrictedStateOperationAllowlist"
+ "_lastMERange"
+ "_leErrorCode"
+ "_leUncertainty"
+ "_needsRestrictedStateOperation"
+ "_srErrorCode"
+ "_srTrackerCategory"
+ "_srUncertainty"
+ "calibrating (%lu samples): LE unavailable (leError=%d), falling through to post-cal"
+ "calibrating (%lu samples): fusedRange=leRange=%.4f m (leError=%d)"
+ "clientNeedsBTCSRestrictedStateOperation"
+ "computeWeightedBlend:leUpperBound:"
+ "eventTime"
+ "filteredArrayUsingPredicate:"
+ "fusedErrorCode"
+ "fusedRange"
+ "fusionMode"
+ "getRangeFromIQ: engines not initialized (mode not set), returning RNA"
+ "getUpdatesEngine"
+ "leErrorCode"
+ "leUncertainty"
+ "mode0_rssi_max"
+ "mode0_rssi_mean_predicted"
+ "mode0_rssi_rayleigh_cdf"
+ "needsRestrictedStateOperation"
+ "post-cal: RSSIMismatch, leUB also bad → RNA"
+ "post-cal: RSSIMismatch, need leUB for weighted blend"
+ "post-cal: fusedRange=%.4f m (%s, leError=%d srError=%d)"
+ "post-cal: leUB=HighInterference, use leRange=%.4f m"
+ "post-cal: weighted blend fusedRange=%.4f m (srWeight=%.2f srRange=%.4f leUB=%.4f rssi0=%.1f dBm uncertainty=%.4f)"
+ "pre-cal: fusedRange=leRange=%.4f m (leError=%d fusedError=%d)"
+ "predicateWithFormat:"
+ "rssi0_dbm"
+ "rssi_calib_samples"
+ "selectFusedRange:mode0MaxRssi:"
+ "self < 0"
+ "session:didChangeViewRotationAngle:"
+ "setEventTime:"
+ "setFusedErrorCode:"
+ "setFusedRange:"
+ "setFusionMode:"
+ "setLeErrorCode:"
+ "setLeUncertainty:"
+ "setSrErrorCode:"
+ "setSrTrackerCategory:"
+ "setSrUncertainty:"
+ "srErrorCode"
+ "srTrackerCategory"
+ "srUncertainty"
+ "strong-signal: fusedRange=srRange=%.4f m (maxRssi=%.1f dBm)"
+ "toneArr count %lu < required %u, skipping hasMissingTones check"
+ "v32@0:8@\"ARSession\"16d24"
+ "v32@0:8@16r^{RangeEstimate=dddQId}24"
+ "v32@0:8Q16^{CSRange=dddidddddI}24"
+ "valueForKeyPath:"
+ "{RSSICalibState=\"sampleCount\"Q\"samples\"{array<double, 3UL>=\"__elems_\"[3d]}\"rssi0Dbm\"d}"
+ "\x91"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91"
- "#btcs,initiator only channel=%d, sweepIndex=%@"
- "#dma,CMAM is disabled"
- "#dma,sending initial unknown cmam state"
- "#dma,starting monitoring"
- "#roseprovider,onCMDAStateChange,index,%u"
- "#ses-btcs,Raw range not sent to update engine: raw range %.2f m, error code %d"
- "#ses-btcs,Sending to update engine: raw range %.2f m, error code %d"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Proximity/Framework/BTCSEngine/src/ToA_wcs_algo/toa_wcs.c"
- "/System/Library/NearbyInteractionBundles/BTCSNeuralNetworkResources.bundle"
- "@84@0:8@16d24@32@40@48^v56^{CSRange=ddidddddI}64^v72I80"
- "Attempting to load network from: %s\n"
- "BTCS Neural Network initialized successfully"
- "BTCSRangeAlgorithmSelect defaulting to: 1 (Super Resolution)"
- "Building Espresso plan..."
- "CSEEngineLE.mm"
- "DMA"
- "ERROR: .weights file does not exist at: %s\n"
- "ERROR: Alternative path also failed (status=%d)\n"
- "ERROR: Failed to add network to Espresso plan (status=%d)\n"
- "ERROR: Failed to build Espresso plan (status=%d)\n"
- "ERROR: Failed to create Espresso context"
- "ERROR: Failed to create Espresso plan"
- "ERROR: Model file does not exist at: %s\n"
- "ERROR: Network path was: %s\n"
- "ERROR: Unable to locate model.espresso.net file in bundle"
- "Found .shape file at: %s\n"
- "Found .weights file at: %s\n"
- "Found N=%d zero-quality tones, power_sum=%lf, normalized by %lf"
- "Found model in system bundle: %s\n"
- "GetRange"
- "Initializing BTCS Neural Network from bundle: %s\n"
- "NOTE: No .shape file found, using inline shapes from .net file"
- "PRDeviceAngleStateMonitor"
- "PRDeviceAngleStateMonitor.mm"
- "Raw range %.4f m exceeds 30m, flagging RangeNotAvailable"
- "SUCCESS: Loaded network using base path"
- "Successfully located model .net file at: %s\n"
- "System bundle not found or resource missing at: %s\n"
- "TB,N,V_smoothingEnabled"
- "TQ,N,V_leAlgoVer"
- "Trying alternative base path: %s\n"
- "_lastRawRange"
- "_leAlgoVer"
- "_smoothingEnabled"
- "_stateInitialized"
- "angleStateToIndex:"
- "btcs ranging algorithm selection is %ld"
- "btcs_nn.isConfigured()"
- "cfr_input"
- "initDeviceAngleStateListener"
- "interpolated_output"
- "leAlgoVer"
- "result.output.size() == kNumFreqBin79*2"
- "setLeAlgoVer:"
- "setSmoothingEnabled:"
- "shape"
- "smoothingEnabled"
- "teardownDeviceAngleStateListener"
- "trimmedEvent:forBWMode:"
- "v96@0:8Q16{CSRange=ddidddddI}24"
- "weights"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x81"
```
