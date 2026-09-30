## Diagnostic-8262

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262`

```diff

-921.80.171.0.1
-  __TEXT.__text: 0x3e24
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x284
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x897
-  __TEXT.__oslogstring: 0x585
+921.100.255.0.0
+  __TEXT.__text: 0x2874
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x1fc
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x5cc
+  __TEXT.__oslogstring: 0x380
   __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0xaff
+  __TEXT.__objc_methname: 0x7e7
   __TEXT.__objc_methtype: 0x163
-  __TEXT.__gcc_except_tab: 0x314
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x8e0
+  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x550
-  __DATA.__objc_selrefs: 0x388
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x400
+  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 457D3F3D-A8D2-3A0B-89A9-EF72958B6BC8
-  Functions: 41
-  Symbols:   101
-  CStrings:  372
+  UUID: F62EAF99-0305-31DA-B264-BF6AC7C82703
+  Functions: 32
+  Symbols:   89
+  CStrings:  272
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _MGCopyAnswer
- _OBJC_CLASS_$_CRURLSessionDelegate
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_CLASS_$_NSMutableURLRequest
- _OBJC_CLASS_$_NSURLSession
- _OBJC_CLASS_$_NSURLSessionConfiguration
- _dispatch_time
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
- _sleep
CStrings:
- "-[UpdatePluginsController _downloadPDIWithCDN:]"
- "-[UpdatePluginsController _requestUpdateURLAndDigestFromAST2WithError:]"
- "Asset Download Failed:%@"
- "Asset digest match success"
- "Asset download success"
- "Content-Type"
- "Digest Mismatched, Download Failure:%@:%@"
- "Downloading the Disk Image:counter:%d"
- "Error    : %@"
- "Failed to download Disk Image::location:%@:error:%@"
- "Failed to download asset"
- "Failed to get OS version from MG"
- "Failed to get repair update URL and digest, error: %@"
- "Failed to move file"
- "File moved to:%@"
- "Get repair update PDI URL & digest from AST2: %@"
- "Invaild PDI URL from AST2"
- "JSONObjectWithData:options:error:"
- "Location : %@"
- "NSStringFromRequiredKey:maxLength:failed:"
- "PDIDigest"
- "PDIDigest: %@"
- "PDIURL"
- "PDIURL is invalid"
- "PDIURL: %@"
- "POST"
- "ProductVersion"
- "Request repair udpate pdiURL: %@, pdiDigest: %@"
- "Request repair update pdiURL & pdiDigest with OS version: %@"
- "Requesting repair update PDI URL and digest from: %@"
- "SHA256DigestString"
- "T@\"NSString\",&,N,V_pdiDigest"
- "T@\"NSString\",R,N,VPDIDigest"
- "T@\"NSString\",R,N,Vast2RequestURL"
- "T@\"NSURL\",&,N,V_pdiURL"
- "T@\"NSURL\",R,N,VPDIURL"
- "TB,R,N,VneedRequestURL"
- "TB,R,N,VuseMobileAsset"
- "Waiting for pdiURL & pdiDigest from AST2 timeout"
- "_downloadPDIWithCDN:"
- "_pdiDigest"
- "_pdiURL"
- "_requestUpdateURLAndDigestFromAST2WithError:"
- "application/json"
- "ast2RequestURL"
- "dataTaskWithRequest:completionHandler:"
- "dataWithJSONObject:options:error:"
- "dmgDigest"
- "dmgURL"
- "downloadTaskWithURL:completionHandler:"
- "ephemeralSessionConfiguration"
- "http error: %@, http status code: %d"
- "http response: %@"
- "https://diagnostics-mdn1.apple.com/api/v1/ast2-companion/public/services/assets/plugin"
- "moveItemAtURL:toURL:error:"
- "needRequestURL"
- "osVersion"
- "pdiDigest"
- "pdiURL"
- "plugin"
- "requestWithURL:"
- "response : %@"
- "resume"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setObject:forKey:"
- "setPdiDigest:"
- "setPdiURL:"
- "setValue:forHTTPHeaderField:"
- "statusCode"
- "useMobileAsset"
- "useMobileAsset: %@"
- "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
- "v32@?0@\"NSURL\"8@\"NSURLResponse\"16@\"NSError\"24"

```
