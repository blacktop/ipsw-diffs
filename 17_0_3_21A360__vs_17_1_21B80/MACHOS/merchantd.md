## merchantd

> `/System/Library/Frameworks/ProximityReader.framework/merchantd`

```diff

-120.51.0.0.0
-  __TEXT.__text: 0xed17c
+121.4.0.0.0
+  __TEXT.__text: 0xf3040
   __TEXT.__auth_stubs: 0x38b0
-  __TEXT.__objc_methlist: 0x5b0
+  __TEXT.__objc_methlist: 0x5a0
   __TEXT.__const: 0x459c
-  __TEXT.__objc_methname: 0x14e5
-  __TEXT.__cstring: 0x6c71
+  __TEXT.__objc_methname: 0x14d8
+  __TEXT.__cstring: 0x7251
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2270
+  __TEXT.__constg_swiftt: 0x2268
   __TEXT.__swift5_typeref: 0x1a18
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_reflstr: 0x1942

   __TEXT.__swift5_capture: 0xf90
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3308
-  __TEXT.__eh_frame: 0x65e8
+  __TEXT.__unwind_info: 0x3654
+  __TEXT.__eh_frame: 0x68e0
   __DATA_CONST.__auth_got: 0x1c58
-  __DATA_CONST.__got: 0x6e0
+  __DATA_CONST.__got: 0x700
   __DATA_CONST.__auth_ptr: 0x138
   __DATA_CONST.__const: 0x5bf8
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3c18
-  __DATA.__objc_selrefs: 0x670
+  __DATA.__objc_const: 0x3c10
+  __DATA.__objc_selrefs: 0x668
   __DATA.__objc_protorefs: 0xb8
   __DATA.__objc_classrefs: 0x110
-  __DATA.__objc_data: 0x1200
-  __DATA.__data: 0x4808
+  __DATA.__objc_data: 0x11e8
+  __DATA.__data: 0x4820
   __DATA.__common: 0x268
   __DATA.__bss: 0x7f00
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3621
-  Symbols:   1322
-  CStrings:  1035
+  Functions: 3632
+  Symbols:   1326
+  CStrings:  1075
 
Symbols:
+ _$s15ProximityReader08IdentityB13ErrorInternalV4CodeO21osVersionNotSupportedyA2EmFWC
+ _$s15ProximityReader08IdentityB13ErrorInternalV4CodeO27nfcNegotiatedHandoverFailedyA2EmFWC
+ _$s15ProximityReader19BaselineErrorDialogC16localizedMessageACSSSg_tcfc
+ _$s15ProximityReader9UtilitiesC31showOSVersionNotSupportedDialog7handleryySbc_tFZ
+ _$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO14osNotSupportedyA2GmFWC
+ _$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO27nfcNegotiatedHandoverFailedyA2GmFWC
- _$s15ProximityReader19BaselineErrorDialogCACycfc
- _$s7CoreIDV27MobileDocumentReaderSessionC11isSupportedSbvgTj
CStrings:
+ "Building IDV request"
+ "Checking prepare preconditions"
+ "Checking read preconditions"
+ "Created"
+ "Creating analytics reporter"
+ "Destroyed"
+ "Executing Raw Data Request:\n%@"
+ "Executing cleanup"
+ "Executing host app cancel read request"
+ "Executing request to cancel current read"
+ "Executing request with scanned payload"
+ "IDV pre-flight checks passed"
+ "Identity UI is visible"
+ "Identity analytics reporter is not available, trying to create it"
+ "Identity analytics session is not available, trying to create it"
+ "Identity registration UI is visible"
+ "Identity registration UI was dismissed"
+ "Identity registration completed"
+ "Identity registration error: [ %@ ]"
+ "Install iOS update settings open: [%{bool}d]"
+ "Loading merchant"
+ "Mapping IDV configuration response"
+ "Mapping IDV merchant response"
+ "Mapping IDV prepare response"
+ "MerchantKit-121.4"
+ "MerchantKit-121.4 (9ec9ea7a)"
+ "No entitlement"
+ "Performing IDV Data request"
+ "Performing IDV Display Only request"
+ "Performing IDV Raw Data request"
+ "Performing IDV configuration request"
+ "Performing IDV merchant request"
+ "Performing IDV prepare request"
+ "Reader configuration precondition error: [ %@ ]"
+ "Reader configuration returned to host app"
+ "Reading configuration"
+ "Received prepare request"
+ "Releasing analytics reporter"
+ "Reporting host app error: [ %@ ]"
+ "Returning IDV Data response"
+ "Returning IDV Display Only response"
+ "Returning IDV Raw Data response"
+ "Returning error during prepare: [ %@ ]"
+ "Returning reader configuration error: [ %@ ]"
+ "Returning result to host app"
+ "Returning session to host app"
+ "Running IDV pre-flight checks"
+ "Sending identity analytics event [ %s ]"
+ "Show alert for iOS version not supported"
+ "Show identity UI"
+ "Show registration UI"
+ "XPC is disconnecting and UI still visible"
- "Executing cancel read request"
- "Identity analytics reporter is not available, trying to create it again"
- "Identity analytics session is not available, trying to create it again"
- "Identity registration completed: [%@]"
- "IdentityUIDidLoad"
- "MerchantKit-120.51"
- "MerchantKit-120.51 (3a961ced)"
- "identityRegUIFinished()"
- "isSupported:"
- "readDocumentFromScannedQRCode(payload:)"
- "requestCancelRead(isEngagementTransition:)"
- "returnReadResult()"

```
