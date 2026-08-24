## findmylocateagent

> `/usr/libexec/findmylocateagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-141.20.6.14.8
-  __TEXT.__text: 0x481d20
-  __TEXT.__auth_stubs: 0x4f30
-  __TEXT.__objc_stubs: 0x1800
+141.20.6.14.14
+  __TEXT.__text: 0x4846c8
+  __TEXT.__auth_stubs: 0x4f70
+  __TEXT.__objc_stubs: 0x1820
   __TEXT.__objc_methlist: 0xba4
-  __TEXT.__const: 0x1c5c8
-  __TEXT.__cstring: 0x9af2
-  __TEXT.__swift5_typeref: 0x61b4
+  __TEXT.__const: 0x1c5e8
+  __TEXT.__cstring: 0x9ba2
+  __TEXT.__swift5_typeref: 0x61d8
   __TEXT.__constg_swiftt: 0x5ccc
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x6fcd
-  __TEXT.__swift5_fieldmd: 0x7eec
+  __TEXT.__swift5_reflstr: 0x6fed
+  __TEXT.__swift5_fieldmd: 0x7f10
   __TEXT.__swift5_assocty: 0x970
   __TEXT.__swift5_proto: 0x1520
   __TEXT.__swift5_types: 0x6c4
   __TEXT.__objc_classname: 0xeda
-  __TEXT.__objc_methname: 0x3cd5
+  __TEXT.__objc_methname: 0x3ce5
   __TEXT.__objc_methtype: 0xd30
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__oslogstring: 0x12a46
-  __TEXT.__swift_as_entry: 0x1328
-  __TEXT.__swift_as_ret: 0x2078
-  __TEXT.__swift_as_cont: 0x36b4
-  __TEXT.__swift5_capture: 0x3d14
+  __TEXT.__oslogstring: 0x12ba6
+  __TEXT.__swift_as_entry: 0x1320
+  __TEXT.__swift_as_ret: 0x2070
+  __TEXT.__swift_as_cont: 0x36c0
+  __TEXT.__swift5_capture: 0x3d20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x116e8
-  __TEXT.__eh_frame: 0x3b488
-  __DATA_CONST.__const: 0x13c98
+  __TEXT.__unwind_info: 0x11700
+  __TEXT.__eh_frame: 0x3b478
+  __DATA_CONST.__const: 0x13cb0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__linkguard: 0x33
-  __DATA_CONST.__auth_got: 0x27a0
-  __DATA_CONST.__got: 0x19c0
-  __DATA_CONST.__auth_ptr: 0x1808
+  __DATA_CONST.__auth_got: 0x27c0
+  __DATA_CONST.__got: 0x19f0
+  __DATA_CONST.__auth_ptr: 0x1818
   __DATA.__objc_const: 0x4f90
-  __DATA.__objc_selrefs: 0x9f8
+  __DATA.__objc_selrefs: 0xa00
   __DATA.__objc_data: 0xbf0
-  __DATA.__data: 0xca00
+  __DATA.__data: 0xca20
   __DATA.__bss: 0x29000
   __DATA.__common: 0x1360
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14442
-  Symbols:   2527
-  CStrings:  3025
+  Functions: 14448
+  Symbols:   2536
+  CStrings:  3032
 
Symbols:
+ _$s10Foundation12URLQueryItemV4name5valueACSSh_SSSghtcfC
+ _$s10Foundation12URLQueryItemVMa
+ _$s10Foundation12URLQueryItemVMn
+ _$s10Foundation13URLComponentsV10queryItemsSayAA12URLQueryItemVGSgvs
+ _$s11SwiftSQLite3RowV3getyxAA10ExpressionVyxGKAA5ValueRzlF
+ _$s12FindMyLocate21LabelLocationResponseV5label0G2IdACSSSg_AFtcfC
+ _$s12FindMyLocate8LocationV8latitude9longitude18horizontalAccuracy08verticalH05speed8altitude5floor9timestamp9placemark12locationType19motionActivityState11customLabel7labelIdACSd_S5dSi10Foundation4DateVAA9PlaceMarkVSgAA0dP0OAA06MotionrS0OSSSgA_tcfC
+ _$s15FindMyMessaging11DestinationV0D4TypeO6deviceyA2EmFWC
+ _$s15FindMyMessaging11DestinationV0D4TypeO8apsTokenyA2EmFWC
+ _$s15FindMyMessaging11DestinationV0D4TypeO9selfTokenyA2EmFWC
+ _$s15FindMyMessaging11DestinationV0D4TypeOSQAAMc
- _$s12FindMyLocate21LabelLocationResponseV5labelACSSSg_tcfC
- _$s12FindMyLocate8LocationV8latitude9longitude18horizontalAccuracy08verticalH05speed8altitude5floor9timestamp9placemark12locationType19motionActivityState11customLabelACSd_S5dSi10Foundation4DateVAA9PlaceMarkVSgAA0dP0OAA06MotionrS0OSSSgtcfC
CStrings:
+ "NIFanout: findee captured peerDestination deviceScoped: %{bool,public}d from %{private,mask.hash}s"
+ "NIFanout: finder captured peerDestination deviceScoped: %{bool,public}d from %{private,mask.hash}s"
+ "NIFanout: sending findingConfigData deviceScoped: %{bool,public}d to %{private,mask.hash}s for handle %{private,mask.hash}s"
+ "fence_confirmation"
+ "locationLabelId"
+ "receiveFindingConfig(_:from:)"
+ "receivedConfigData(_:tokenData:replyHandle:peerDestination:)"
+ "respondToFindingTokenRequest(_:replyTo:)"
+ "sendConfigData(_:peerToken:peerHandle:ownerHandle:peerDestination:)"
+ "setDefaultActionURL:"
+ "startFindeeRangingForConfigData(with:replyHandle:configData:peerDestination:)"
+ "startFinderRangingForConfigData(with:peerHandle:ownerHandle:peerDestination:)"
- "receiveFindingConfig(_:)"
- "receivedConfigData(_:tokenData:replyHandle:)"
- "respondToFindingTokenRequest(_:)"
- "sendConfigData(_:peerToken:peerHandle:ownerHandle:)"
- "startFindeeRangingForConfigData(with:replyHandle:configData:)"
```
