## DisplayAndBrightnessSettings

> `/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`

```diff

-1215.1.6.0.0
-  __TEXT.__text: 0x4d138
-  __TEXT.__objc_methlist: 0x2c04
-  __TEXT.__const: 0x1474
+1215.1.6.600.0
+  __TEXT.__text: 0x4df20
+  __TEXT.__objc_methlist: 0x2c7c
+  __TEXT.__const: 0x1484
   __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__cstring: 0xd3edd
-  __TEXT.__oslogstring: 0x905
+  __TEXT.__cstring: 0xd400d
+  __TEXT.__oslogstring: 0xb85
   __TEXT.__constg_swiftt: 0x44c
   __TEXT.__swift5_typeref: 0x79fa
   __TEXT.__swift5_capture: 0x304

   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1700
+  __TEXT.__unwind_info: 0x1740
   __TEXT.__eh_frame: 0xa0c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6c0
+  __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2338
+  __DATA_CONST.__objc_selrefs: 0x23a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0xb90
   __AUTH_CONST.__const: 0xda0
-  __AUTH_CONST.__cfstring: 0x3500
+  __AUTH_CONST.__cfstring: 0x3680
   __AUTH_CONST.__objc_const: 0x49d0
-  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH_CONST.__auth_got: 0xfe8
   __AUTH.__objc_data: 0xce0
   __AUTH.__data: 0x390
   __DATA.__objc_ivar: 0x32c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1625
-  Symbols:   2470
-  CStrings:  581
+  Functions: 1642
+  Symbols:   2488
+  CStrings:  602
 
Symbols:
+ -[DBSZoomAndProSpecifiers _dimWindowBeforeRestart]
+ -[DBSZoomAndProSpecifiers _displayEdgeCompensationConfirmationDictForEnable:]
+ -[DBSZoomAndProSpecifiers _displayEdgeCompensationGroupSpecifier]
+ -[DBSZoomAndProSpecifiers _displayEdgeCompensationSpecifier]
+ -[DBSZoomAndProSpecifiers _restartRenderServerForDisplayEdgeCompensation]
+ -[DBSZoomAndProSpecifiers _userDidCancelDisplayEdgeCompensationWithSpecifier:]
+ -[DBSZoomAndProSpecifiers _userDidConfirmDisplayEdgeCompensationWithSpecifier:]
+ -[DBSZoomAndProSpecifiers _writeDisplayEdgeCompensationEnabled:]
+ -[DBSZoomAndProSpecifiers isDisplayEdgeCompensationEnabled:]
+ -[DBSZoomAndProSpecifiers setDisplayEdgeCompensationEnabled:specifier:]
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table59
+ _CFDictionaryGetValue
+ _DBSDisplayEdgeCompensationAvailable
+ _DBSSuppressesSmartCoverSettings
+ _DBS_LocalizedStringForDisplayEdgeCompensation
+ ___73-[DBSZoomAndProSpecifiers _restartRenderServerForDisplayEdgeCompensation]_block_invoke
+ ___73-[DBSZoomAndProSpecifiers _restartRenderServerForDisplayEdgeCompensation]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
CStrings:
+ "ArtworkDeviceSubType"
+ "ArtworkTraits"
+ "CONFIRMATION_OK_DISABLE"
+ "CONFIRMATION_OK_ENABLE"
+ "DBSDisplayEdgeCompensationPendingEnabled"
+ "DISPLAY_EDGE_COMPENSATION"
+ "DISPLAY_EDGE_COMPENSATION_FOOTER"
+ "DISPLAY_EDGE_COMPENSATION_GROUP"
+ "Display Edge Compensation"
+ "Display Edge Compensation applied dimming layer before restart"
+ "Display Edge Compensation cancelled; reverting switch"
+ "Display Edge Compensation confirmed; applying enabled=%{BOOL}d"
+ "Display Edge Compensation could not dim before restart: no window on delegate view"
+ "Display Edge Compensation read: key=%{public}@ set=%{BOOL}d resolved=%{BOOL}d"
+ "Display Edge Compensation sending render-server restart (reason='%{public}@', target='%{public}@')"
+ "Display Edge Compensation specifiers omitted: device is not a cover-display device"
+ "Display Edge Compensation toggled to %{BOOL}d"
+ "Display Edge Compensation writing %{public}@=%{BOOL}d in %{public}@"
+ "DisplayEdgeCompensation"
+ "EdgeSwipeBandExpansionEnabled"
+ "com.apple.backboardd"
```
