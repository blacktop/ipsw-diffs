## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-147.0.4.0.0
-  __TEXT.__text: 0x357130
+150.0.2.0.0
+  __TEXT.__text: 0x354a18
   __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_stubs: 0x9180
-  __TEXT.__objc_methlist: 0x8c68
-  __TEXT.__gcc_except_tab: 0x11510
-  __TEXT.__const: 0x44166
-  __TEXT.__cstring: 0x1a778
-  __TEXT.__oslogstring: 0x10828
-  __TEXT.__objc_classname: 0x10a6
-  __TEXT.__objc_methtype: 0x5ed4
-  __TEXT.__objc_methname: 0xbf29
+  __TEXT.__objc_stubs: 0x9420
+  __TEXT.__objc_methlist: 0x8d78
+  __TEXT.__gcc_except_tab: 0x11d38
+  __TEXT.__const: 0x441be
+  __TEXT.__cstring: 0x1d2ab
+  __TEXT.__oslogstring: 0x10fdf
+  __TEXT.__objc_classname: 0x10cc
+  __TEXT.__objc_methtype: 0x5f43
+  __TEXT.__objc_methname: 0xc1a9
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc088
+  __TEXT.__unwind_info: 0xc3d0
   __TEXT.__eh_frame: 0x590
   __DATA_CONST.__auth_got: 0xb70
-  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x25330
-  __DATA_CONST.__cfstring: 0x6620
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __DATA_CONST.__const: 0x25558
+  __DATA_CONST.__cfstring: 0x69c0
+  __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x440
+  __DATA_CONST.__objc_superrefs: 0x448
   __DATA_CONST.__objc_intobj: 0x1968
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xff38
-  __DATA.__objc_selrefs: 0x2f90
-  __DATA.__objc_ivar: 0x930
-  __DATA.__objc_data: 0x2f80
-  __DATA.__data: 0x2010
+  __DATA.__objc_const: 0x10630
+  __DATA.__objc_selrefs: 0x3038
+  __DATA.__objc_ivar: 0x948
+  __DATA.__objc_data: 0x2fd0
+  __DATA.__data: 0x2020
   __DATA.__bss: 0x230
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 242E8002-50D9-3889-949B-49947F56D8FF
-  Functions: 16062
-  Symbols:   572
-  CStrings:  9766
+  UUID: E879CC81-F904-3ACC-A76F-189666785E3B
+  Functions: 16393
+  Symbols:   573
+  CStrings:  9958
 
Symbols:
+ _CC_SHA256
+ _DeviceIdentityIssueClientCertificateWithCompletion
+ _SecKeyCreateSignature
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ ","
+ ".realtimeProxy"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1530: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIVdugDP8ekJNqtnXzwVM6n0S9AsM7-WeTL63WA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/Daemon/main.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/DataCollection/CSKappaTap2Radar.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/DataCollection/CSMartyTap2Radar.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CLKappaDeescalator.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CLKappaFeaturesAlgZg.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CSAOPSvc.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CSAnomalyEventService.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CSKappaDetectionService.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CSMartyDetectionService.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyAlgorithms/CSSafetySOSStateMachine.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyCompanion/CSCompanionService.mm"
+ "/Library/Caches/com.apple.xbs/D9C054B2-67CD-4826-864C-BA79DEA42485/TemporaryDirectory.FeSrOu/Sources/CoreSafety/SafetyCore/CSInjectionService.mm"
+ "@\"CSStudiesServerSubmitterIgneous\""
+ "@48@0:8@16@24^@32^@40"
+ "Added BAA certificates to HTTP header"
+ "Added BAA data hash to HTTP header (%zu bytes)"
+ "Added BAA signature to HTTP header (%zu bytes)"
+ "BAA certificates unavailable for authentication"
+ "BAA request times out"
+ "BAA-Certificates"
+ "BAA-DataHash"
+ "BAA-Signature"
+ "CSIgneousBAAValidityPeriodMin"
+ "CSIgneousKeepAuxiliaryFile"
+ "CSStudiesServerSubmitterIgneous"
+ "Created request with method: %{public}@ to URL: %{public}@"
+ "Created request with method: %{public}@ to URL: %{public}@ for %@"
+ "Failed to create signature: %@"
+ "Failed to get data from certificate"
+ "Failed to obtain BAA certificates for authentication"
+ "Failed to read file: %@, error: %@"
+ "Failed to request BAA certificates: %@"
+ "Failed to save data to %@: %@"
+ "File does not exist"
+ "File does not exist: %@"
+ "HTTPMethod"
+ "Initialized Igneous submitter"
+ "Initialized Igneous uploader: monitoring %d, harvestTimeWindowSec %.0f, readManifestTimeoutSec %.0f, retentionPeriod %llu"
+ "Invalid BAA certificate response"
+ "Invalid BAA certificates"
+ "Invalid JSON format: %@"
+ "Invalid certificate object in BAA certificates array"
+ "Invalid data hash for authentication (hash: %@, length: %zu)"
+ "Invalid or missing data hash for authentication"
+ "Invalid or missing signature for authentication"
+ "Invalid signature for authentication (signature: %@, length: %zu)"
+ "JSON content is not a valid dictionary"
+ "No data provided to sign"
+ "On filePicker, %@ doesn't contain value for key 'spooled'"
+ "On filePicker, %@ is newer than all events in the manifest. Try again later"
+ "On filePicker, cannot create unarchiver for %@"
+ "On filePicker, cannot read %@. Try again later"
+ "On filePicker, picked %@ for upload later"
+ "On filePicker, removed %@ since it doesn't match any event in the manifest"
+ "On filePicker, removed %@ since it's too old"
+ "On realtime proxy, failed to create submitter"
+ "On realtime proxy, failed to read JSON from %@"
+ "On realtime proxy, failed to sign data: %@"
+ "On realtime proxy, failed to upload %@ - no response received"
+ "On realtime proxy, failed to upload %@ - session error: %@"
+ "On realtime proxy, proxy upload created and signed: %@"
+ "On realtime proxy, read JSON content from %@"
+ "On realtime proxy, studies Server ingest: %ld %@"
+ "On realtime proxy, uploaded %@ to server: %{public}d"
+ "On submitter, %@ doesn't contain value for key 'spooled'"
+ "On submitter, %@ doesn't exist"
+ "On submitter, %@ will be bundled with metadata"
+ "On submitter, JSON bundle file created and signed: %@"
+ "On submitter, cannot create unarchiver for %@"
+ "On submitter, failed to create submitter"
+ "On submitter, failed to sign data: %@"
+ "On submitter, failed to upload %@ - no response received"
+ "On submitter, failed to upload %@ - session error: %@"
+ "On submitter, removed %@ since it's too old"
+ "On submitter, studies Server ingest: %ld %@"
+ "On submitter, uploaded %@ to server: %{public}d"
+ "Original request method: %{public}@ to URL: %{public}@"
+ "Request BAA certificates, baaValidityPeriodMin %d"
+ "Request completed with method: %{public}@ to URL: %{public}@"
+ "Request failed with error: %{public}@"
+ "Requested BAA certificates successfully"
+ "StudiesSubmitterIgneous"
+ "Successfully saved data to %@ and created signature (%zu bytes)"
+ "T@\"CSFolderMonitor\",&,V_proxyMonitor"
+ "T@\"CSStudiesServerSubmitterIgneous\",&,V_igneousSubmitter"
+ "T@\"NSArray\",&,V_baaCertificates"
+ "T^{__SecKey=},V_baaKey"
+ "URL"
+ "Unknown error"
+ "While scanning, can't find file to bundle at: %@"
+ "[Igneous] Created realtime proxy file, %@"
+ "[Igneous] Failed to serialize JSON for realtime proxy: %@"
+ "[Igneous] Failed to write realtime proxy file, %@, error, %@"
+ "^{__SecKey=}"
+ "^{__SecKey=}16@0:8"
+ "_baaCertificates"
+ "_baaKey"
+ "_igneousSubmitter"
+ "_proxyMonitor"
+ "accumulatedRotation"
+ "angleThreshold"
+ "angularFenceReference"
+ "angularFenceState"
+ "baaCertificates"
+ "baaKey"
+ "base64EncodedStringWithOptions:"
+ "budSide"
+ "centerXPixels"
+ "centerYPixels"
+ "com.apple.anomalydetectiond.CSStudiesServerSubmitterIgneous:%@"
+ "componentsJoinedByString:"
+ "createSubmitter"
+ "currentRequest"
+ "dataWithJSONObject:options:error:"
+ "detectionClass"
+ "detectionConfidence"
+ "didExceedAngleThreshold"
+ "displacementUncertaintyX"
+ "displacementUncertaintyY"
+ "displacementUncertaintyZ"
+ "entityKitBoundingBoxCorrection"
+ "entityKitBoundingBoxDataList"
+ "entityKitDataPoC"
+ "fulldata"
+ "gtbTimestampUS"
+ "heightPixels"
+ "https://gsp131.ls.apple.com/hvr/eqdt"
+ "https://gsp131.ls.apple.com/hvr/eqmd"
+ "igneousSubmitter"
+ "intentionState"
+ "kMAOptionsBAAIgnoreExistingKeychainItems"
+ "kMAOptionsBAAValidity"
+ "metaData"
+ "mslData"
+ "nil"
+ "numberOfTotalDetectedObjects"
+ "originalRequest"
+ "present"
+ "primaryBudSide"
+ "proxyMonitor"
+ "qBF"
+ "qCB"
+ "quaternionRefW"
+ "quaternionRefX"
+ "quaternionRefY"
+ "quaternionRefZ"
+ "rB_SB"
+ "rF_SB"
+ "readJSONFile:error:"
+ "realtime"
+ "realtimeProxy"
+ "requestBAACert"
+ "serializedBAACertificates"
+ "setBaaCertificates:"
+ "setBaaKey:"
+ "setIgneousSubmitter:"
+ "setProxyMonitor:"
+ "signDataWithBAACert:outputURL:hash:error:"
+ "submitFileWithURL: %@ with signature"
+ "submitFileWithURL:signature:hash:andCompletionHandler:"
+ "timestampMicroSeconds"
+ "v24@0:8^{__SecKey=}16"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
+ "widthPixels"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/Daemon/main.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/DataCollection/CSKappaTap2Radar.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/DataCollection/CSMartyTap2Radar.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CLKappaDeescalator.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CLKappaFeaturesAlgZg.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSAOPSvc.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSAnomalyEventService.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSKappaDetectionService.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSMartyDetectionService.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSSafetySOSStateMachine.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyCompanion/CSCompanionService.mm"
- "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyCore/CSInjectionService.mm"
- "Failed to append data from file %@"
- "Failed to finalize encrypting file %@"
- "Failed to register with server to upload %@"
- "Failed to remove file %@"
- "Failed to start output file %@"
- "File %@ doesn't contain value for key 'spooled'"
- "File %@ has been encrypted as %@"
- "File %@ is newer than all events in the manifest. Try again later"
- "File %@ will be encrypted"
- "File to be encrypted %@ doesn't exist"
- "Initialized Igneous uploader: registered %d, monitoring %d, harvestTimeWindowSec %.0f, readManifestTimeoutSec %.0f, retentionPeriod %llu"
- "On filePicker, cannot create unarchiver"
- "On filePicker, cannot read file %@. Try again later"
- "On submitter, cannot create unarchiver"
- "Picked file %@ for upload later"
- "Registered with server to upload %@ as %@"
- "Removed %@ since it doesn't match any event in the manifest"
- "Removed %@ since it's too old"
- "Uploaded %@ to server: %{public}d, deregister with server"

```
