## findmylocated

> `/usr/libexec/findmylocated`

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
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-141.30.6.14.7
-  __TEXT.__text: 0x58cc9c
-  __TEXT.__auth_stubs: 0x5cf0
+141.30.6.14.11
+  __TEXT.__text: 0x58fc7c
+  __TEXT.__auth_stubs: 0x5d00
   __TEXT.__objc_stubs: 0x2000
   __TEXT.__objc_methlist: 0xf4c
-  __TEXT.__const: 0x20988
-  __TEXT.__cstring: 0xb922
-  __TEXT.__swift5_typeref: 0x72c2
+  __TEXT.__const: 0x209a8
+  __TEXT.__cstring: 0xb9b2
+  __TEXT.__swift5_typeref: 0x72d8
   __TEXT.__constg_swiftt: 0x7140
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x7e5d
-  __TEXT.__swift5_fieldmd: 0x8fdc
+  __TEXT.__swift5_reflstr: 0x7e7d
+  __TEXT.__swift5_fieldmd: 0x9000
   __TEXT.__swift5_assocty: 0xa48
   __TEXT.__swift5_proto: 0x17e8
   __TEXT.__swift5_types: 0x7f4

   __TEXT.__objc_methtype: 0x11e8
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__oslogstring: 0x18fcc
-  __TEXT.__swift_as_entry: 0x16e8
-  __TEXT.__swift_as_ret: 0x2864
-  __TEXT.__swift_as_cont: 0x43f4
-  __TEXT.__swift5_capture: 0x4d74
+  __TEXT.__oslogstring: 0x191ac
+  __TEXT.__swift_as_entry: 0x16e0
+  __TEXT.__swift_as_ret: 0x285c
+  __TEXT.__swift_as_cont: 0x4400
+  __TEXT.__swift5_capture: 0x4d84
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x16358
-  __TEXT.__eh_frame: 0x487f0
-  __DATA_CONST.__const: 0x18270
+  __TEXT.__unwind_info: 0x16350
+  __TEXT.__eh_frame: 0x487e8
+  __DATA_CONST.__const: 0x18288
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__linkguard: 0x33
-  __DATA_CONST.__auth_got: 0x2e80
-  __DATA_CONST.__got: 0x1d48
+  __DATA_CONST.__auth_got: 0x2e88
+  __DATA_CONST.__got: 0x1d70
   __DATA_CONST.__auth_ptr: 0x1a70
   __DATA.__objc_const: 0x6358
   __DATA.__objc_selrefs: 0xd60
   __DATA.__objc_data: 0x1430
-  __DATA.__data: 0xf050
+  __DATA.__data: 0xf080
   __DATA.__bss: 0x2e580
   __DATA.__common: 0x1420
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17533
-  Symbols:   2879
-  CStrings:  3845
+  Functions: 17535
+  Symbols:   2884
+  CStrings:  3851
 
Symbols:
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
+ "NIFanout: sending findingToken deviceScoped: %{bool,public}d to %{private,mask.hash}s for handle %{private,mask.hash}s"
+ "locationLabelId"
+ "receiveFindingConfig(_:from:)"
+ "receivedConfigData(_:tokenData:replyHandle:peerDestination:)"
+ "respondToFindingTokenRequest(_:replyTo:)"
+ "sendConfigData(_:peerToken:peerHandle:ownerHandle:peerDestination:)"
+ "startFindeeRangingForConfigData(with:replyHandle:configData:peerDestination:)"
+ "startFinderRangingForConfigData(with:peerHandle:ownerHandle:peerDestination:)"
- "receiveFindingConfig(_:)"
- "receivedConfigData(_:tokenData:replyHandle:)"
- "respondToFindingTokenRequest(_:)"
- "sendConfigData(_:peerToken:peerHandle:ownerHandle:)"
- "startFindeeRangingForConfigData(with:replyHandle:configData:)"
```
