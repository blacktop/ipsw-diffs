## com.apple.MessageSecurity.MSTimestampXPCService

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/XPCServices/com.apple.MessageSecurity.MSTimestampXPCService.xpc/com.apple.MessageSecurity.MSTimestampXPCService`

```diff

-195.122.4.0.0
-  __TEXT.__text: 0x1d0c
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x600
-  __TEXT.__objc_methlist: 0x8c
+330.0.0.0.0
+  __TEXT.__text: 0x23c0
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_methlist: 0xa4
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x372
-  __TEXT.__oslogstring: 0x2a2
+  __TEXT.__cstring: 0x4c4
+  __TEXT.__oslogstring: 0x385
   __TEXT.__objc_classname: 0x15
-  __TEXT.__objc_methtype: 0x76
-  __TEXT.__objc_methname: 0x43a
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x2a0
-  __DATA_CONST.__cfstring: 0x140
+  __TEXT.__objc_methtype: 0x81
+  __TEXT.__objc_methname: 0x4f9
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_selrefs: 0x1d0
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A429D9F0-6A4D-3024-AC45-26EFEB4F6646
-  Functions: 42
-  Symbols:   89
-  CStrings:  113
+  UUID: EC4F036D-6E68-354B-935D-76BC1658A959
+  Functions: 52
+  Symbols:   103
+  CStrings:  141
 
Symbols:
+ _CFRelease
+ _MSTimestampHTTPErrorDomain
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSMutableArray
+ _SecPolicyCreateAppleQuartzTimeStamping
+ _kMSAppleTimestampDomain
+ _kMSAppleTimestampEndpoint_tsa_mldsa87_rsa3072_pss_sha512
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _os_variant_allows_internal_security_policies
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "B16@0:8"
+ "Failed to create Quartz timestamp policy"
+ "MSTimestampXPCServer: Failed to create Quartz timestamp policy"
+ "MSTimestampXPCServer: Internal build detected, allowing internal-use TSA domains"
+ "MSTimestampXPCServer: Internal build detected: allowing internal-use TSA endpoints"
+ "Network error: %@"
+ "addObjectsFromArray:"
+ "allowedTimestampDomains"
+ "arrayWithArray:"
+ "com.apple.messagesecurity"
+ "containsObject:"
+ "domain"
+ "gateway-oblivious.apple.com"
+ "host"
+ "https://quartz-test.cs.apple.com/api/v0/timestamp/tsa-mldsa87-rsa3072-pss-sha512"
+ "https://quartz-test.cs.apple.com/api/v0/timestamp/tsa-rsa2048-pkcs15-sha256"
+ "isInternalBuild"
+ "objectForKeyedSubscript:"
+ "quartz-test.cs.apple.com"
+ "sendErrorReply:toPeer:errorCode:description:underlyingError:"
+ "setUsesClassicLoadingMode:"
+ "underlyingErrorCode"
+ "underlyingErrorDomain"
+ "userInfo"
+ "v56@0:8@16@24q32r*40@48"
+ "verifyWithRequest:policies:error:"
- "sendErrorReply:toPeer:errorCode:description:"
- "v48@0:8@16@24q32r*40"
- "verifyWithRequest:error:"

```
