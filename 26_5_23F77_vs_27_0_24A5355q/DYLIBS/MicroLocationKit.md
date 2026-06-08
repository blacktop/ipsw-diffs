## MicroLocationKit

> `/System/Library/PrivateFrameworks/MicroLocationKit.framework/MicroLocationKit`

```diff

-62.0.3.0.0
-  __TEXT.__text: 0x1c7c4
-  __TEXT.__auth_stubs: 0xaa0
+106.0.2.0.0
+  __TEXT.__text: 0x1cc08
   __TEXT.__objc_methlist: 0x190
   __TEXT.__const: 0x3bf0
   __TEXT.__swift5_typeref: 0xcb3

   __TEXT.__swift5_reflstr: 0x3da
   __TEXT.__swift5_fieldmd: 0x9a0
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__cstring: 0x54c
+  __TEXT.__cstring: 0x56c
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x36c
   __TEXT.__swift5_types: 0x110
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x70
-  __TEXT.__oslogstring: 0x1b1
+  __TEXT.__oslogstring: 0x1d5
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x8
-  __TEXT.__unwind_info: 0x990
-  __TEXT.__eh_frame: 0x898
-  __TEXT.__objc_classname: 0xcd
-  __TEXT.__objc_methname: 0x436
-  __TEXT.__objc_methtype: 0x164
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x1b8
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__eh_frame: 0x820
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x188
+  __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x558
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x17b0
   __AUTH_CONST.__objc_const: 0x3a8
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH.__objc_data: 0xb8
   __AUTH.__data: 0x218
-  __DATA.__data: 0xb90
+  __DATA.__data: 0xbb8
   __DATA.__bss: 0x6d00
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B28207CE-1F20-3172-B8CA-0B0B3EC916BE
+  UUID: 1463D8B6-EB8E-369E-BF2E-199B7A21CEEA
   Functions: 901
-  Symbols:   579
-  CStrings:  126
+  Symbols:   603
+  CStrings:  42
 
Symbols:
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.4
+ __os_signpost_emit_with_name_impl
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x27
+ _swift_retain_x8
+ _swift_retain_x9
+ _symbolic _____Sg 16MicroLocationKit7MapItemV
- _objc_msgSend$setPredictionsUpdateType:
- _objc_retain_x28
- _swift_bridgeObjectRelease_n
- _swift_errorRelease
- _swift_errorRetain
- _swift_release_n
- _swift_retain
- _swift_unexpectedError
- _symbolic ______p s5ErrorP
CStrings:
+ "Adding an anchor with name: %s, contextLayer: %s, timestamp: %s"
+ "ProcessMapItems"
+ "[Error] Interval already ended"
+ "mapItems=%{public}ld"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "Adding an anchor with name: %s, contextLayer: %s"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "MicroLocationKit"
- "NSObject"
- "Q16@0:8"
- "Swift/Dictionary.swift"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "ULConnectionDelegate"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC16MicroLocationKit17ConnectionManager"
- "_TtC16MicroLocationKit20MicroLocationService"
- "_TtC16MicroLocationKit25ConnectionDelegateAdapter"
- "addLabel:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "connection"
- "connection:didEnableMicrolocationAtCurrentLocationWithError:"
- "connection:didFailWithError:"
- "connection:didUpdatePrediction:"
- "connection:didUpdateServiceStatus:"
- "connectionDelegateAdapter"
- "connectionDidUpdateMap:"
- "connectionDidUpdatePredictionContext:"
- "connectionManager"
- "contextLayer"
- "contextLayers"
- "createServiceIdentifierForToken:"
- "currentMap"
- "dealloc"
- "debugDescription"
- "description"
- "deviceClass"
- "entityType"
- "hash"
- "init"
- "initWithContextLayers:"
- "initWithDelegate:serviceIdentifier:"
- "initWithName:timestamp:contextLayerType:deviceClass:"
- "initWithName:timestamp:deviceClass:entityType:"
- "initWithName:timestamp:rssi:"
- "isEqual:"
- "isKindOfClass:"
- "isMapValid"
- "isMemberOfClass:"
- "isProxy"
- "labels"
- "mapItems"
- "name"
- "numberOfLabelsInSameSpaceForMapItem:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rssi"
- "runWithConfiguration:"
- "self"
- "setPredictionsUpdateType:"
- "state"
- "superclass"
- "timestamp"
- "v16@0:8"
- "v24@0:8@\"ULConnection\"16"
- "v24@0:8@16"
- "v32@0:8@\"ULConnection\"16@\"NSError\"24"
- "v32@0:8@\"ULConnection\"16@\"ULPrediction\"24"
- "v32@0:8@\"ULConnection\"16@\"ULServiceStatus\"24"
- "v32@0:8@16@24"
- "value"
- "zone"

```
