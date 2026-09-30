## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-988.9.0.0.0
-  __TEXT.__text: 0x1b0550
+988.12.4.5.0
+  __TEXT.__text: 0x1b0eb8
   __TEXT.__auth_stubs: 0x1ad0
-  __TEXT.__objc_methlist: 0x107dc
-  __TEXT.__const: 0x2f08
-  __TEXT.__dlopen_cstrs: 0x966
+  __TEXT.__objc_methlist: 0x1081c
+  __TEXT.__const: 0x2f18
+  __TEXT.__dlopen_cstrs: 0x9be
   __TEXT.__swift5_typeref: 0x7e5
   __TEXT.__swift5_reflstr: 0x2fd
   __TEXT.__swift5_assocty: 0x78

   __TEXT.__swift5_fieldmd: 0x6a0
   __TEXT.__swift5_proto: 0x270
   __TEXT.__swift5_types: 0xac
-  __TEXT.__cstring: 0x1e119
-  __TEXT.__gcc_except_tab: 0x7b0c
-  __TEXT.__oslogstring: 0x1b869
+  __TEXT.__cstring: 0x1e12c
+  __TEXT.__gcc_except_tab: 0x7b9c
+  __TEXT.__oslogstring: 0x1ba5c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5568
+  __TEXT.__unwind_info: 0x5588
   __TEXT.__eh_frame: 0x570
   __TEXT.__objc_classname: 0xfb1
-  __TEXT.__objc_methname: 0x278e2
+  __TEXT.__objc_methname: 0x27a0e
   __TEXT.__objc_methtype: 0x3934
-  __TEXT.__objc_stubs: 0x1c3e0
+  __TEXT.__objc_stubs: 0x1c4c0
   __DATA_CONST.__got: 0x918
-  __DATA_CONST.__const: 0x50c0
+  __DATA_CONST.__const: 0x50b0
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8308
+  __DATA_CONST.__objc_selrefs: 0x8340
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1a00
   __AUTH_CONST.__auth_got: 0xd78
   __AUTH_CONST.__const: 0x32d0
   __AUTH_CONST.__cfstring: 0x18340
-  __AUTH_CONST.__objc_const: 0x158b8
+  __AUTH_CONST.__objc_const: 0x15918
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_intobj: 0x3828
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0xe58
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x1258
+  __DATA.__objc_ivar: 0x1260
   __DATA.__data: 0x1700
   __DATA.__bss: 0x4fa0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x80
   __DATA_DIRTY.__objc_data: 0x1568
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x298
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EB09EE11-31CA-3AD4-965D-EE3C152BA179
-  Functions: 7540
+  UUID: E874EAB8-0073-3395-B5E8-2F5371E061E4
+  Functions: 7548
   Symbols:   1082
-  CStrings:  15080
+  CStrings:  15095
 
CStrings:
+ "OSEligibilityQuery"
+ "TB,V_waitingForAuthorizationUI"
+ "TB,V_waitingForUpdatedAuthLevel"
+ "[corewifi] WiFiNetworkSharing is not eligible (answer=%llu, domain=%llu, conn=[%{public}@])"
+ "[corewifi] [OSEligibilityQuery initWithDomain:auditToken:error:] failed (error=%{public}@, domain=%llu, conn=[%{public}@])"
+ "[corewifi] [wifi-network-sharing] Accessory scan completed (error=%{public}@, clientID=%{public}@, duration=%llums, results=%{public}@, )"
+ "[corewifi] [wifi-network-sharing] Current network ask-to-share eligible, but proxcard is already presented for matching clientID during authorization (clientID=%{public}@, metadata=%{public}@, authLevel=%lu, knownNetwork=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Invoking completion handler for authorization request (clientID=%{public}@, error=%{public}@, authLevel=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Local scan completed (error=%{public}@, clientID=%{public}@, duration=%llums, results=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Will not invoke completion handler (yet) for authorization request, waiting for auth level to change and/or proxcard UI to complete (clientID=%{public}@, waitingForUpdatedAuthLevel=%d, waitingForAuthorizationUI=%d)"
+ "__didCompleteAskToShareScan"
+ "_waitingForAuthorizationUI"
+ "_waitingForUpdatedAuthLevel"
+ "answer"
+ "initWithDomain:auditToken:error:"
+ "setWaitingForAuthorizationUI:"
+ "setWaitingForUpdatedAuthLevel:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility"
+ "waitingForAuthorizationUI"
+ "waitingForUpdatedAuthLevel"
- "[corewifi] [wifi-network-sharing] Accessory scan completed (error=%{public}@, results=%{public}@)"
- "[corewifi] [wifi-network-sharing] Ask-to-share scan(s) completed"
- "[corewifi] [wifi-network-sharing] Current network ask-to-share eligible, but proxcard is already presented for matching clientID (clientID=%{public}@, metadata=%{public}@, authLevel=%lu, knownNetwork=%{public}@)"
- "[corewifi] [wifi-network-sharing] Invoking completion handler to authorization request (clientID=%{public}@, error=%{public}@, authLevel=%{public}@)"
- "[corewifi] [wifi-network-sharing] Local scan completed (error=%{public}@, results=%{public}@)"

```
