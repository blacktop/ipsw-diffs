## sharingd

> `/usr/libexec/sharingd`

```diff

-2094.20.31.2.1
-  __TEXT.__text: 0x6cfe38
-  __TEXT.__auth_stubs: 0x9990
-  __TEXT.__objc_stubs: 0x350a0
-  __TEXT.__objc_methlist: 0x1fc2c
-  __TEXT.__cstring: 0x4a0ca
-  __TEXT.__objc_methname: 0x4aa9f
+2094.20.65.0.0
+  __TEXT.__text: 0x6de9f4
+  __TEXT.__auth_stubs: 0x99b0
+  __TEXT.__objc_stubs: 0x35180
+  __TEXT.__objc_methlist: 0x1fc94
+  __TEXT.__cstring: 0x4a43a
+  __TEXT.__objc_methname: 0x4ac17
   __TEXT.__objc_classname: 0x2e42
-  __TEXT.__objc_methtype: 0xa4c8
-  __TEXT.__const: 0x19700
-  __TEXT.__gcc_except_tab: 0x6e2c
-  __TEXT.__oslogstring: 0x3da33
+  __TEXT.__objc_methtype: 0xa50d
+  __TEXT.__const: 0x19c90
+  __TEXT.__gcc_except_tab: 0x6e6c
+  __TEXT.__oslogstring: 0x3ddc3
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
-  __TEXT.__swift5_typeref: 0xa3b6
-  __TEXT.__swift5_fieldmd: 0x8f98
-  __TEXT.__constg_swiftt: 0xb3f0
+  __TEXT.__swift5_typeref: 0xa462
+  __TEXT.__swift5_fieldmd: 0x90e4
+  __TEXT.__constg_swiftt: 0xb4b0
   __TEXT.__swift5_builtin: 0x35c
-  __TEXT.__swift5_reflstr: 0x7557
-  __TEXT.__swift5_assocty: 0x15e8
+  __TEXT.__swift5_reflstr: 0x7637
+  __TEXT.__swift5_assocty: 0x1618
   __TEXT.__swift5_protos: 0x218
-  __TEXT.__swift5_proto: 0x15e8
-  __TEXT.__swift5_types: 0x938
-  __TEXT.__swift_as_entry: 0xecc
-  __TEXT.__swift5_capture: 0x4f94
-  __TEXT.__swift_as_ret: 0xebc
+  __TEXT.__swift5_proto: 0x1644
+  __TEXT.__swift5_types: 0x94c
+  __TEXT.__swift_as_entry: 0xee8
+  __TEXT.__swift5_capture: 0x4ff0
+  __TEXT.__swift_as_ret: 0xee8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x157c8
-  __TEXT.__eh_frame: 0x25f74
-  __DATA_CONST.__auth_got: 0x4cd8
+  __TEXT.__unwind_info: 0x15a40
+  __TEXT.__eh_frame: 0x267cc
+  __DATA_CONST.__auth_got: 0x4ce8
   __DATA_CONST.__got: 0x3428
-  __DATA_CONST.__auth_ptr: 0x18a0
-  __DATA_CONST.__const: 0x21bb0
-  __DATA_CONST.__cfstring: 0x19ce0
-  __DATA_CONST.__objc_classlist: 0xf38
+  __DATA_CONST.__auth_ptr: 0x18c8
+  __DATA_CONST.__const: 0x21f98
+  __DATA_CONST.__cfstring: 0x19d60
+  __DATA_CONST.__objc_classlist: 0xf40
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x708
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x16f8
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3c428
-  __DATA.__objc_selrefs: 0x11338
-  __DATA.__objc_ivar: 0x2b24
-  __DATA.__objc_data: 0xb220
-  __DATA.__data: 0x1a1b0
-  __DATA.__bss: 0x160a0
-  __DATA.__common: 0xaf8
+  __DATA.__objc_const: 0x3c560
+  __DATA.__objc_selrefs: 0x11380
+  __DATA.__objc_ivar: 0x2b28
+  __DATA.__objc_data: 0xb318
+  __DATA.__data: 0x1a2a0
+  __DATA.__bss: 0x16c20
+  __DATA.__common: 0xb00
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8C380EBC-B151-3C80-819F-1C90E89271D9
-  Functions: 28429
-  Symbols:   4412
-  CStrings:  31956
+  UUID: 1A6F35C7-0B5E-3FCB-9FA7-C5B5ED5D574D
+  Functions: 28582
+  Symbols:   4414
+  CStrings:  32016
 
Symbols:
+ _$s7Sharing21SFAirDropUserDefaultsC20idmsDefaultBackoffMSSivg
+ _$s7Sharing21SFAirDropUserDefaultsC27idmsHandleRetryDelaySecondsSivg
+ _CNContactIdentifierKey
+ __swift_stdlib_strtod_clocale
- _OBJC_CLASS_$_SFAppleIDClient
- _objc_release_x11
CStrings:
+ " nextAttemptDelayMS: "
+ " responseMessage: "
+ "%ld needing retry detected"
+ "-[SDAppleIDAgent _altDSIDLookupWithEmails:phoneNumbers:completion:]"
+ "-[SDAppleIDAgent _handleAltDSIDLookupResponse:requestError:serverTask:completion:]"
+ "-[SDAppleIDServerTask _handleServerError:withStatusCode:nextSuggestedAttemptDelay:responseInfo:]"
+ "-[SDAppleIDServerTask _urlWithCompletion:]_block_invoke_5"
+ ".+@([A-Za-z0-9-]+\\.)+[A-Za-z]{2}[A-Za-z]*"
+ "/private/var/tmp/ShareSheetTestingSnapshots/"
+ "AirDrop unavailable - wireless CarPlay connected"
+ "Batch success: %s"
+ "BatchResponse - responseCode: "
+ "Checking if local handles need retry"
+ "Failed to fetch contacts for email %s: %@"
+ "Failed to fetch contacts for phone %s: %@"
+ "Failed to fetch retry handles - %@"
+ "Failed to get /private/var/tmp/ShareSheetTestingSnapshots/ folder for moving Share Sheet snapshot (URL: %@)"
+ "Failed to move Share Sheet snapshot (URL: %@) to %@: %@"
+ "Fetching batch %ld with %ld emails and %ld phone numbers"
+ "Found %ld contacts for email: %s"
+ "Found %ld contacts for phone: %s"
+ "Found %ld total contacts matching retry handles"
+ "Ignoring non-legacy AppleTVSetup: %@"
+ "Lookup AltDSIDs"
+ "Main entry write error %@"
+ "Missing ASK request"
+ "Missing UPLOAD request"
+ "Missing connection definition"
+ "Missing identity share info / connection"
+ "Missing request transferID"
+ "Missing totalBytes / contentType"
+ "No contactID match for handle response"
+ "No handles need retry"
+ "Parsing %s"
+ "Person lookup response %@\n"
+ "Processing %ld results - contactSet %ld"
+ "Removing retry handle, matching add entry found"
+ "Requesting %ld handles"
+ "ResultResponse - handle "
+ "Retry entry write error %@"
+ "Running altDSID request %@ and %@"
+ "SDAirDropIDMSServiceAccountAltDSID"
+ "Server altDSID fetch failure %s"
+ "URL bag fetch failures %@"
+ "Unable to finish IDMS update from contacts - %@"
+ "Unable to parse error response %s"
+ "Unable to parse response %s"
+ "Unexpected error type %@"
+ "Unknown altDSID fetch error %@"
+ "Unsupported message type"
+ "User change detected - clearing store"
+ "_TtC16DaemoniOSLibrary29SDAirDropIDMSServiceTelemetry"
+ "_altDSIDLookupWithEmails:phoneNumbers:completion:"
+ "_altDSIDRequests"
+ "_handleAltDSIDLookupResponse:requestError:serverTask:completion:"
+ "_handleServerError:withStatusCode:nextSuggestedAttemptDelay:responseInfo:"
+ "_saveSnapshotToFile:withReferenceSnapshot:sessionID:completionHandler:"
+ "altDSIDLookupWithEmails:phoneNumbers:completion:"
+ "appleIDAgent"
+ "com.apple.sharing.AirDrop.IDMSFetch"
+ "currentUpdateToken"
+ "evaluateWithObject:"
+ "finishedBatchCount"
+ "https://aidc.apple.com/aidcert/services/lookupPersonHandles"
+ "initWithStringValue:"
+ "isAirPodsPro"
+ "lookupPersonHandles"
+ "lookupResults"
+ "myAltDSIDKey"
+ "queryBatchSize"
+ "sessionStart"
+ "sessionTelemetry"
+ "setTestName:"
+ "stagedRetryHandles"
+ "testName"
+ "testSuiteName"
+ "totalBatchCount"
+ "updatePreconditionsIfNeededWithReferenceSnapshot:"
+ "urlForKey:completion:"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v48@0:8q16q24q32@40"
- "-[SDAppleIDServerTask _handleServerError:withStatusCode:nextSuggestedAttemptDelay:]"
- "AirDrop unavailable - CarPlay connected"
- "AltDSID already present - skipping IDMS fetch"
- "Attempting to query %s"
- "Found local altDSID %s for handle %s"
- "Missing altDSID in person info for handle %s"
- "No local altDSID found for: %s"
- "No person info for handle %s - %@"
- "Scheduling client backoff retry in %ld seconds"
- "Staging altDSID %s for handle %s"
- "Unable to fetch person info for handle %s - backoff %ld - %@"
- "Unable to finish IDMS update from contacts %@"
- "Unknown error for handle, not attempting retry %s - %@"
- "Write error %@"
- "_handleServerError:withStatusCode:nextSuggestedAttemptDelay:"
- "altDSIDKey"
- "altProductID"
- "appleIDClient"
- "contactBatchSize"
- "defaultBackoff"
- "handleKey"
- "updatePreconditionsIfNeeded"
- "urlAtKey:"
- "v24@?0@\"SFAppleIDAccount\"8@\"NSError\"16"
- "v40@0:8q16q24q32"

```
