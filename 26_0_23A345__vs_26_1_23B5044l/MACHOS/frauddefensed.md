## frauddefensed

> `/usr/libexec/frauddefensed`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x8845c
-  __TEXT.__auth_stubs: 0x1e90
-  __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__const: 0x41c4
-  __TEXT.__cstring: 0x7102
-  __TEXT.__swift5_typeref: 0x14a0
-  __TEXT.__swift5_capture: 0x6d0
-  __TEXT.__objc_methname: 0xcd9
+55.0.0.0.0
+  __TEXT.__text: 0x897e4
+  __TEXT.__auth_stubs: 0x1eb0
+  __TEXT.__objc_methlist: 0x2c8
+  __TEXT.__const: 0x4414
+  __TEXT.__cstring: 0x78f2
+  __TEXT.__swift5_typeref: 0x148a
+  __TEXT.__swift5_capture: 0x6b4
+  __TEXT.__objc_methname: 0xd54
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1674
+  __TEXT.__constg_swiftt: 0x165c
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x14b3
-  __TEXT.__swift5_fieldmd: 0x18ac
+  __TEXT.__swift5_reflstr: 0x1603
+  __TEXT.__swift5_fieldmd: 0x18bc
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__swift5_proto: 0x2bc
+  __TEXT.__swift5_proto: 0x2c0
   __TEXT.__swift5_types: 0x194
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x230

   __TEXT.__objc_methtype: 0x204
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__oslogstring: 0xbf
-  __TEXT.__unwind_info: 0x1d38
-  __TEXT.__eh_frame: 0x4dd0
-  __DATA_CONST.__auth_got: 0xf48
+  __TEXT.__unwind_info: 0x1d88
+  __TEXT.__eh_frame: 0x4e78
+  __DATA_CONST.__auth_got: 0xf58
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__auth_ptr: 0x588
-  __DATA_CONST.__const: 0x3df8
+  __DATA_CONST.__const: 0x3db0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA.__objc_const: 0x1820
-  __DATA.__objc_selrefs: 0x500
+  __DATA.__objc_const: 0x1870
+  __DATA.__objc_selrefs: 0x520
   __DATA.__objc_data: 0x8b0
-  __DATA.__data: 0x2c90
-  __DATA.__common: 0x180
-  __DATA.__bss: 0x4c80
+  __DATA.__data: 0x2cc8
+  __DATA.__common: 0x178
+  __DATA.__bss: 0x4d00
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3A9C924-D68E-3101-9300-AA1F9A96903B
-  Functions: 2073
-  Symbols:   787
-  CStrings:  796
+  UUID: 5FE22BF8-A972-3324-9AA8-6215676CF5CD
+  Functions: 2090
+  Symbols:   790
+  CStrings:  838
 
Symbols:
+ _$sSo8NSNumberC10FoundationE14integerLiteralABSi_tcfC
+ _$ss12StaticStringV11descriptionSSvg
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSError
- _$sSo17OS_dispatch_queueC8DispatchE5async5group3qos5flags7executeySo0a1_b1_F0CSg_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
CStrings:
+ "        CREATE TABLE IF NOT EXISTS CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR\n         );"
+ "$__lazy_storage_$_angelServerClient"
+ "%s"
+ ", radarComponentID="
+ ", radarComponentName="
+ ", radarComponentVersion="
+ ", radarDescription="
+ "CipherML.CipherMLError"
+ "Created CKSignatures table. { createQuery=        CREATE TABLE IF NOT EXISTS CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR\n         ); }"
+ "Error state detected, iMessage reported from Oscar."
+ "NSCocoaErrorDomain"
+ "NSURLErrorDomain"
+ "Oscar decision maker was marked on non-iMessage reported message.\n\nPlease provide any additional information about the message possible:"
+ "Sender look-up failed because XPC connection was interrupted."
+ "Sender look-up failed because of NSCocoaErrorDomain error."
+ "Sender look-up failed due to CipherML NetworkManager error."
+ "Sender look-up failed due to CipherML error."
+ "Sender look-up failed due to CipherML missing configuration error."
+ "Sender look-up failed due to CipherML server error."
+ "Sender look-up failed due to netowork timeout (Code=-1001)"
+ "Sender look-up failed with connection error (Code=-1004)"
+ "Sender look-up failed with host not found error (Code=-1003)"
+ "Sender look-up failed with privacy proxy error (Code=-1004)"
+ "Sender look-up failed with unknown network error."
+ "Spam Detection Error State"
+ "Spam Detection Reporting Error State Detected"
+ "TTR is not available on non-internal device."
+ "The spam reported you submitted has erroneous state. Please file a radar."
+ "Trust and Safety"
+ "bannerWith:and:radarTitle:radarDescription:radarComponentID:radarComponentName:radarComponentVersion:"
+ "code"
+ "domain"
+ "enableTelemetry=YES"
+ "oscarFromImessageTTRPrompts"
+ "senderLookUpFailureNS_1001"
+ "senderLookUpFailureNS_1003"
+ "senderLookUpFailureNS_1004"
+ "senderLookUpFailureOtherCMLError"
+ "senderLookUpFailureOtherCocoaDomain"
+ "senderLookUpFailureXPCInterrupted"
+ "senderLookupFailureMissingConfig"
+ "senderLookupFailureNS_1009"
+ "senderLookupFailureNS_Other"
+ "senderLookupFailureNWManagerError"
+ "senderLookupFailureServerError"
+ "userInfo"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48@\"NSString\"56@\"NSString\"64"
+ "v72@0:8@16@24@32@40@48@56@64"
- "        CREATE TABLE CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR\n         );"
- "Created CKSignatures table. { createQuery=        CREATE TABLE CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR\n         ); }"
- "com.apple.trustkit.signposts"
- "isPrepared"
- "prepare"
- "signpostsQueue"

```
