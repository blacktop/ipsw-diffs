## UnilogIngestion

> `/System/Library/PrivateFrameworks/UnilogIngestion.framework/UnilogIngestion`

```diff

 1.10.0.0.0
-  __TEXT.__text: 0x1f46c
-  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__text: 0x1c828
   __TEXT.__objc_methlist: 0x174
-  __TEXT.__const: 0xd58
+  __TEXT.__const: 0xd20
   __TEXT.__constg_swiftt: 0x6e8
-  __TEXT.__swift5_typeref: 0x63a
+  __TEXT.__swift5_typeref: 0x5f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x2a1
   __TEXT.__swift5_fieldmd: 0x424
   __TEXT.__swift5_types: 0x5c
   __TEXT.__oslogstring: 0x2fc
-  __TEXT.__swift5_capture: 0x98
   __TEXT.__swift5_assocty: 0x68
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_protos: 0x14
+  __TEXT.__swift5_capture: 0x58
   __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_cont: 0x30
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__cstring: 0x151
-  __TEXT.__unwind_info: 0x618
-  __TEXT.__eh_frame: 0x6a8
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x293
-  __TEXT.__objc_methtype: 0x100
-  __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x208
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__eh_frame: 0x5d0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0xb30
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xa90
   __AUTH_CONST.__objc_const: 0x588
+  __AUTH_CONST.__auth_got: 0x950
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x3f8
-  __DATA.__data: 0x728
+  __AUTH.__data: 0x2c8
+  __DATA.__data: 0x678
   __DATA.__bss: 0x780
   __DATA.__common: 0x80
-  __DATA_DIRTY.__data: 0x38
+  __DATA_DIRTY.__data: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 86434175-164C-3EB5-B429-A5E3E23FF1A1
-  Functions: 550
-  Symbols:   365
-  CStrings:  107
+  UUID: 7D0508BD-2DD9-3D94-9415-7770E5EFD6F5
+  Functions: 528
+  Symbols:   390
+  CStrings:  28
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_exist.box.addr_destructor
+ _objc_retain_x20
+ _swift_release_x1
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_willThrowTypedImpl
- _objc_release_x26
- _objc_retain_x21
- _objectdestroyTm
- _swift_release_n
- _symbolic _____ 19UnilogCommonLibrary11AddLogEntryV
- _symbolic _____ 19UnilogCommonLibrary13SetSpanStatusV
- _symbolic _____ 19UnilogCommonLibrary7EndSpanV
- _symbolic _____ 19UnilogCommonLibrary9StartSpanV
- _symbolic _____3key_ShyAAG5valuetSg 15UnilogIngestion17TracingIdentifierO
- _symbolic ______pSg 10Foundation15ContiguousBytesP
- _symbolic ______pSg 15UnilogIngestion26RankableDisjointSetElementP
CStrings:
- "#16@0:8"
- "@\"NSData\"16@0:8"
- "@\"NSDictionary\"16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@28@0:8@\"NSData\"16I24"
- "@28@0:8@16I24"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BMStoreData"
- "I16@0:8"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TI,?,R,N"
- "TI,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC15UnilogIngestion12UnstagingRun"
- "_TtC15UnilogIngestion13WorkflowState"
- "_TtC15UnilogIngestion15WorkflowContext"
- "_TtC15UnilogIngestion19ProcessingTelemetry"
- "_all"
- "_allBy"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "contained"
- "dataVersion"
- "debugDescription"
- "description"
- "doubleForKey:"
- "endAt"
- "endedAt"
- "eventBodyData"
- "eventWithData:dataVersion:"
- "hash"
- "head"
- "initWithBytes:length:encoding:"
- "initWithSuiteName:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "json"
- "jsonDict"
- "latestDataVersion"
- "lock"
- "map"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "rank"
- "release"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "serialize"
- "setValue:forKey:"
- "start"
- "state"
- "statistics"
- "superclass"
- "telemetry"
- "telemetrySession"
- "useCase"
- "userDefaults"
- "zone"

```
