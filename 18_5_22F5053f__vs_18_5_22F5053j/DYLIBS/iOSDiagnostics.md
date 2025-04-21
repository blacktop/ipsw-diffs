## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-820.120.76.0.0
-  __TEXT.__text: 0x3c54
+820.120.91.0.0
+  __TEXT.__text: 0x3c5c
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x814
+  __TEXT.__objc_methlist: 0x824
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x5df
+  __TEXT.__cstring: 0x5d9
   __TEXT.__gcc_except_tab: 0x110
   __TEXT.__oslogstring: 0x1e6
   __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x11a2
-  __TEXT.__objc_methtype: 0x501
+  __TEXT.__objc_methname: 0x11bf
+  __TEXT.__objc_methtype: 0x512
   __TEXT.__objc_stubs: 0xca0
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d0
+  __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 146
-  Symbols:   659
-  CStrings:  326
+  Functions: 147
+  Symbols:   661
+  CStrings:  328
 
Symbols:
+ -[DADiagnosticFlow initWithDestination:serialNumber:sessionID:]
+ -[DADiagnosticFlow initWithDestination:serialNumber:sessionID:passcode:]
+ -[DADiagnosticFlow passcode]
+ -[DADiagnosticFlow setPasscode:]
+ _OBJC_IVAR_$_DADiagnosticFlow._passcode
+ _objc_msgSend$initWithDestination:serialNumber:sessionID:passcode:
+ _objc_msgSend$passcode
- -[DADiagnosticFlow initWithDestination:serialNumber:sessionID:serviceName:]
- -[DADiagnosticFlow serviceName]
- -[DADiagnosticFlow setServiceName:]
- _OBJC_IVAR_$_DADiagnosticFlow._serviceName
- _objc_msgSend$initWithDestination:serialNumber:sessionID:serviceName:
- _objc_msgSend$serviceName
CStrings:
+ "<%@: %p> destination: %lu, serialNumber: %@, sessionID: %@, passcode: %@"
+ "@40@0:8Q16@24@32"
+ "T@\"NSString\",&,N,V_passcode"
+ "_passcode"
+ "initWithDestination:serialNumber:sessionID:"
+ "initWithDestination:serialNumber:sessionID:passcode:"
+ "passcode"
+ "setPasscode:"
- "<%@: %p> destination: %lu, serialNumber: %@, sessionID: %@, serviceName: %@"
- "T@\"NSString\",&,N,V_serviceName"
- "_serviceName"
- "initWithDestination:serialNumber:sessionID:serviceName:"
- "serviceName"
- "setServiceName:"

```
