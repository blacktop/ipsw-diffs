## SmartRepliesServer

> `/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer`

```diff

-122.21.0.0.0
-  __TEXT.__text: 0xe918
-  __TEXT.__auth_stubs: 0xc10
+161.1.0.0.0
+  __TEXT.__text: 0xe5ec
   __TEXT.__objc_methlist: 0x184
-  __TEXT.__const: 0x968
+  __TEXT.__const: 0x960
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__swift5_typeref: 0x36c
+  __TEXT.__swift5_typeref: 0x374
   __TEXT.__constg_swiftt: 0x2ec
   __TEXT.__swift5_reflstr: 0x2a5
   __TEXT.__swift5_fieldmd: 0x350

   __TEXT.__cstring: 0x6d2
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_capture: 0xec
   __TEXT.__oslogstring: 0x406
-  __TEXT.__swift5_capture: 0xbc
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift_as_cont: 0xc
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__unwind_info: 0x400
-  __TEXT.__eh_frame: 0x6a8
-  __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0x4fd
-  __TEXT.__objc_methtype: 0x1bc
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x118
+  __TEXT.__eh_frame: 0x640
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x618
-  __AUTH_CONST.__const: 0x7b8
+  __DATA_CONST.__got: 0x118
+  __AUTH_CONST.__const: 0x7e0
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x510
+  __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0x48
   __DATA.__data: 0x240
   __DATA.__bss: 0x600

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 39E535A0-02EA-3C97-B440-7056BD45DD1B
-  Functions: 363
-  Symbols:   146
-  CStrings:  148
+  UUID: E5B09B7F-E467-3C29-8801-4874975D657B
+  Functions: 352
+  Symbols:   164
+  CStrings:  62
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retainAutorelease
+ _objc_retain_x26
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x24
+ _swift_retain_x25
- _objc_autorelease
- _objc_release_x22
CStrings:
- "#16@0:8"
- "$defaultActor"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "SRSStringPreprocessor"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC18SmartRepliesServer20ServerRequestHandler"
- "_TtC18SmartRepliesServer22MultiHeadEspressoModel"
- "_TtC18SmartRepliesServer30SRSSmartRepliesServerXPCServer"
- "_TtP12SmartReplies25SRSmartRepliesXPCProtocol_"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "currentHandler"
- "dealloc"
- "debugDescription"
- "description"
- "espressoContext"
- "espressoModel"
- "espressoPlan"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "headDimensionality"
- "init"
- "initWithMachServiceName:"
- "inputName"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener:shouldAcceptNewConnection:"
- "numberOfInputParameters"
- "objectAtIndexedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predictForMessage:conversationTurns:language:plistPath:espressoModelPath:vocabPath:heads:completion:"
- "processIdentifier"
- "purgableModelKey"
- "purgeableModel"
- "release"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serverRequestHandler"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "stringWithUTF8String:"
- "superclass"
- "transformBatch:"
- "transformMessage:withMethods:"
- "v16@0:8"
- "v80@0:8@\"NSString\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSArray\"64@?<v@?@\"NSDictionary\"@\"NSError\">72"
- "v80@0:8@16@24@32@40@48@56@64@?72"
- "valueForEntitlement:"
- "withMethods:"
- "xpcListener"
- "zone"

```
