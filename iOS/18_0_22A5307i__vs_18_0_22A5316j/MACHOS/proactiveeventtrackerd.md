## proactiveeventtrackerd

> `/usr/libexec/proactiveeventtrackerd`

```diff

-397.0.0.0.0
-  __TEXT.__text: 0x4184
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x218
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__cstring: 0x5de
+399.0.0.0.0
+  __TEXT.__text: 0x4cb8
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_methlist: 0x238
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0x184
+  __TEXT.__cstring: 0x673
   __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0xc13
-  __TEXT.__objc_methtype: 0xf1
-  __TEXT.__oslogstring: 0x644
+  __TEXT.__objc_methname: 0xde9
+  __TEXT.__objc_methtype: 0x119
+  __TEXT.__oslogstring: 0x71f
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__info_plist: 0x5c4
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x248
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__info_plist: 0x5cd
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x238
-  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x3c8
-  __DATA.__objc_selrefs: 0x468
+  __DATA.__objc_selrefs: 0x520
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xf0
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 55
-  Symbols:   112
-  CStrings:  293
+  Functions: 59
+  Symbols:   120
+  CStrings:  328
 
Symbols:
+ _COMAPPLEPROACTIVEGMSGMSUberEventReadFrom
+ _OBJC_CLASS_$_COMAPPLEPETCOMMONPETMetadata
+ _OBJC_CLASS_$_COMAPPLEPROACTIVEGMSGMSPETUploadEvent
+ _OBJC_CLASS_$_COMAPPLEPROACTIVEGMSGMSUberEvent
+ _OBJC_CLASS_$_PBDataReader
+ _objc_opt_respondsToSelector
+ _objc_retain_x21
+ _objc_retain_x4
CStrings:
+ "%!@(MISSING) has been sent to FBFv2. Size: %!l(MISSING)u"
+ "%!@(MISSING) is failed to upload to PFA backend"
+ "%!@(MISSING) to report data to FBFv2. Error: %!@(MISSING)"
+ "@44@0:8@16@24@32I40"
+ "B36@0:8@16@24B32"
+ "Found GMS Event Message Group: %!@(MISSING)"
+ "PFA"
+ "PFA-backend is not available "
+ "Repackaged %!l(MISSING)u GMS messages, ready for uploading to PFA with schema: %!@(MISSING)"
+ "_canLog:messageGroup:isInternal:"
+ "_createMetadataFrom:submissionId:messageName:typeId:"
+ "_uploadBatchedDataToPFA:schema:messageGroup:"
+ "_uploadGMSDataToPFA:"
+ "addUnaggregatedMessages:"
+ "array"
+ "build"
+ "clearAggregatedMessages"
+ "clearUnaggregatedMessages"
+ "com.apple.generativefunctions.instrumentation.UberEvent"
+ "com.apple.proactive"
+ "com.apple.proactive.gms.PetUploadEvent"
+ "configVersion"
+ "country"
+ "device"
+ "isGm"
+ "isInternalCarry"
+ "isTesting"
+ "language"
+ "platform"
+ "reportDataPlatformBatchedEvent:forBundleID:ofSchema:completion:"
+ "setMessageName:"
+ "setPseudoDeviceId:"
+ "setTypeId:"
+ "setUberEvent:"
+ "sharedLoggerWithPersistenceConfiguration:"
+ "typeId"
+ "uploadTime"
+ "v40@0:8@16@24@32"
- "B32@0:8@16@24"
- "_canLog:messageGroup:"
- "setName:"

```
