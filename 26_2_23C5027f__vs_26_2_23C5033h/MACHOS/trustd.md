## trustd

> `/usr/libexec/trustd`

```diff

-61901.60.29.0.0
-  __TEXT.__text: 0x63038
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_stubs: 0x2dc0
-  __TEXT.__objc_methlist: 0xc2c
+61901.60.37.0.0
+  __TEXT.__text: 0x637a4
+  __TEXT.__auth_stubs: 0x2430
+  __TEXT.__objc_stubs: 0x2ee0
+  __TEXT.__objc_methlist: 0xc5c
   __TEXT.__const: 0x5c81
-  __TEXT.__gcc_except_tab: 0xca0
-  __TEXT.__cstring: 0x701d
-  __TEXT.__oslogstring: 0x5fad
+  __TEXT.__gcc_except_tab: 0xca4
+  __TEXT.__cstring: 0x70d1
+  __TEXT.__oslogstring: 0x6029
   __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x2cc0
+  __TEXT.__objc_methname: 0x2daa
   __TEXT.__objc_methtype: 0xaf6
-  __TEXT.__unwind_info: 0x10a8
-  __DATA_CONST.__auth_got: 0x1218
-  __DATA_CONST.__got: 0x798
+  __TEXT.__unwind_info: 0x10b8
+  __DATA_CONST.__auth_got: 0x1228
+  __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x4c48
-  __DATA_CONST.__cfstring: 0x63c0
+  __DATA_CONST.__const: 0x4cd8
+  __DATA_CONST.__cfstring: 0x6480
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA.__objc_const: 0x14b0
-  __DATA.__objc_selrefs: 0xd20
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_const: 0x14e0
+  __DATA.__objc_selrefs: 0xd68
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x510
+  __DATA.__bss: 0x520
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3693330E-9F45-3ADC-B600-ED3BE5F5035A
-  Functions: 1274
-  Symbols:   838
-  CStrings:  3041
+  UUID: 191306E4-4D76-31DD-BA75-5FE5B4EEB322
+  Functions: 1281
+  Symbols:   843
+  CStrings:  3069
 
Symbols:
+ _BiomeLibrary
+ _NSLog
+ _OBJC_CLASS_$_BMDeviceTLS
+ _OBJC_CLASS_$_BMSource
+ _OBJC_CLASS_$_BMStreamBase
CStrings:
+ "CRLite found definitive data for cert %ld: isRevoked = %d"
+ "CRLite result not being enforced, falling back to Valid"
+ "CRLiteStatus"
+ "Device.Networking.TLS"
+ "Enforcing CRLite result"
+ "Failed to create Biome stream: %@"
+ "T@\"NSDate\",&,V_startedDownload"
+ "TLSBiomeConnectionEvent"
+ "UseCRLiteEnforcement"
+ "ValidDownloadMetric"
+ "ValidIngestionMetric"
+ "_startedDownload"
+ "download started at %@"
+ "downloadTime"
+ "initWithHostname:tlsVersion:"
+ "logMetric:withName:"
+ "pqtls_used"
+ "sendEvent:"
+ "server_name"
+ "setStartedDownload:"
+ "shouldReportSampleForEventName:"
+ "source"
+ "startedDownload"
+ "streamWithIdentifier:error:"
+ "timeIntervalSinceDate:"
+ "update finished at %@ (took %f)"
+ "update started at %@"
- "CRLiteUsed"
- "download finished at %f"
- "download started at %f"
- "update finished at %f"
- "update started at %f"

```
