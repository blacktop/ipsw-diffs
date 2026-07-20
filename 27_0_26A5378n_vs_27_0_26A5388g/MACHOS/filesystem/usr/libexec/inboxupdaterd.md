## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-274.0.0.0.0
-  __TEXT.__text: 0x84094
-  __TEXT.__auth_stubs: 0x1330
-  __TEXT.__objc_stubs: 0x7be0
-  __TEXT.__objc_methlist: 0x37d4
-  __TEXT.__cstring: 0x4935
-  __TEXT.__objc_methname: 0x7b12
-  __TEXT.__objc_classname: 0x526
-  __TEXT.__objc_methtype: 0x102f
-  __TEXT.__const: 0xce73
-  __TEXT.__oslogstring: 0x9cc1
-  __TEXT.__gcc_except_tab: 0x1410
-  __TEXT.__unwind_info: 0x1c18
-  __DATA_CONST.__const: 0xe168
-  __DATA_CONST.__cfstring: 0x4240
-  __DATA_CONST.__objc_classlist: 0x150
+274.0.9.0.0
+  __TEXT.__text: 0x8a690
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_stubs: 0x83c0
+  __TEXT.__objc_methlist: 0x3b6c
+  __TEXT.__cstring: 0x4d3e
+  __TEXT.__objc_methname: 0x861e
+  __TEXT.__objc_classname: 0x5af
+  __TEXT.__objc_methtype: 0x121b
+  __TEXT.__const: 0xced3
+  __TEXT.__gcc_except_tab: 0x1678
+  __TEXT.__oslogstring: 0xa3f1
+  __TEXT.__unwind_info: 0x1da8
+  __DATA_CONST.__const: 0xe788
+  __DATA_CONST.__cfstring: 0x4760
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __DATA_CONST.__objc_intobj: 0x1878
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_intobj: 0x18c0
   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_arrayobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x9a8
-  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x7808
-  __DATA.__objc_selrefs: 0x22d8
-  __DATA.__objc_ivar: 0x39c
-  __DATA.__objc_data: 0xd20
-  __DATA.__data: 0x2260
+  __DATA.__objc_const: 0x8550
+  __DATA.__objc_selrefs: 0x24e8
+  __DATA.__objc_ivar: 0x408
+  __DATA.__objc_data: 0xe10
+  __DATA.__data: 0x29f0
   __DATA.__bss: 0x130
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/Frameworks/ServiceManagement.framework/Versions/A/ServiceManagement
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/Versions/A/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/Versions/A/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/Versions/A/MobileMulticastTransfer

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3901
-  Symbols:   438
-  CStrings:  3371
+  Functions: 4090
+  Symbols:   473
+  CStrings:  3571
 
Symbols:
+ _CFRetain
+ _DeviceIdentityIssueClientCertificateWithCompletion
+ _NSURLAuthenticationMethodClientCertificate
+ _NSURLAuthenticationMethodServerTrust
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSURLCredential
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _SecIdentityCreate
+ _SecItemDelete
+ _kMAOptionsBAAAccessControls
+ _kMAOptionsBAAIgnoreExistingKeychainItems
+ _kMAOptionsBAAKeychainAccessGroup
+ _kMAOptionsBAAKeychainLabel
+ _kMAOptionsBAANetworkTimeoutInterval
+ _kMAOptionsBAANonce
+ _kMAOptionsBAAOIDAccessControls
+ _kMAOptionsBAAOIDDeviceIdentifiers
+ _kMAOptionsBAAOIDDeviceOSInformation
+ _kMAOptionsBAAOIDHardwareProperties
+ _kMAOptionsBAAOIDIMG4Manifest
+ _kMAOptionsBAAOIDKeyUsageProperties
+ _kMAOptionsBAAOIDNonce
+ _kMAOptionsBAAOIDSToInclude
+ _kMAOptionsBAAOIDUCRTDeviceIdentifiers
+ _kMAOptionsBAASCRTAttestation
+ _kMAOptionsBAAValidity
+ _kSecAttrAccessGroup
+ _kSecAttrLabel
+ _kSecClass
+ _kSecClassCertificate
+ _kSecClassKey
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "%"
+ "%{public}@ terminated; ignoring session restart timer fire"
+ "/ProductPersonalization/v1.0/consumeNotification"
+ "1.0.0"
+ "@\"<MIBUPersonalizationDelegate>\""
+ "@\"<MIBUPersonalizationOperationDelegate>\""
+ "@\"MIBUPersonalizationOperation\""
+ "@\"MIBUPersonalizationStatusReporter\""
+ "@\"NSDate\""
+ "@\"NSURLSession\""
+ "@60@0:8q16B24@28@36@44@52"
+ "Accept"
+ "Attempting to fetch record from CloudKit (attempt %d)"
+ "BAA cert request finished"
+ "BAA credential fetch timed out after %d seconds"
+ "Bypassing server trust validation for test reporting server URL override"
+ "Cached personalization is expired or invalid; deleting and re-personalizing."
+ "Content-Type"
+ "Creating Product Personalization Service request to URL: %{public}@"
+ "DOWNLOAD_COMPLETE"
+ "DOWNLOAD_FAILED"
+ "Download successful"
+ "Failed to create SU key: %{public}@"
+ "Failed to create SecAccessControl: %{public}@"
+ "Failed to create SecIdentity from SU certificate and key"
+ "Failed to create certificates from SU cert data: %{public}@"
+ "Failed to create status update request: %{public}@"
+ "Failed to delete BAA %{public}@ from keychain: %d"
+ "Failed to delete expired personalization: %{public}@"
+ "Failed to fetch record from CloudKit"
+ "Failed to fetch record on attempt %d"
+ "Failed to fetch. err: %@"
+ "Failed to generate BAA nonce; aborting credential fetch"
+ "Failed to get pandora certs data for context: %@, error: %@"
+ "Failed to obtain BAA certificates: %@"
+ "Failed to open SMC service — conservatively treating as RTC reset"
+ "Failed to read RPF0 key: %{public}@ — conservatively treating as RTC reset"
+ "Failed to read SU certificate: %{public}@"
+ "Failed to read personalization cache: %{public}@; deleting and re-personalizing."
+ "Failed to serialize status payload: %{public}@"
+ "Failed to sign status payload: %{public}@"
+ "Idle timer fired but personalization is in progress; deferring cleanup"
+ "MIBUPersonalizationDelegate"
+ "MIBUPersonalizationOperation"
+ "MIBUPersonalizationOperationDelegate"
+ "MIBUPersonalizationStatus"
+ "MIBUPersonalizationStatusReporter"
+ "NSURLSessionDelegate"
+ "No BAA reference key available for signing"
+ "ONLINE"
+ "ONLINE status not delivered: %{public}@"
+ "Override Reporting Server URL: %{public}@"
+ "PERSONALIZATION_COMPLETE"
+ "PERSONALIZATION_FAILED"
+ "POST"
+ "Personalization completion after teardown, ignoring"
+ "Personalization controller not running; cancellation flagged for pending start"
+ "Personalization finished with error: %{public}@; shutdown=%d"
+ "Personalization terminated after WiFi association"
+ "Personalization terminated before saving to cache"
+ "Personalization terminated during CloudKit fetch retry"
+ "Personalization watchdog timed out after %d seconds"
+ "Personalization watchdog timer fired!"
+ "RPF0"
+ "RPF0 key not supported on this platform — conservatively treating as RTC reset"
+ "RPF0 returned unexpected data length %zu — conservatively treating as RTC reset"
+ "RPF0=0x%02x, POR bit=%d"
+ "ReportingServerURL"
+ "Requesting BAA certs"
+ "SHUTDOWN"
+ "Signing failed: %{public}@"
+ "Skipping Shelf Life Mode for personalization-completion shutdown to preserve RTC for next-boot expiry check"
+ "Starting personalization watchdog timer with %ds timeout..."
+ "Status POST failed (attempt %lu/%lu): %{public}@"
+ "Status POST received unexpected response type (attempt %lu/%lu): %{public}@"
+ "Status POST returned HTTP %ld (attempt %lu/%lu, %{public}@)"
+ "Status POST succeeded: HTTP %ld"
+ "Stopping personalization watchdog timer..."
+ "T@\"<MIBUPersonalizationDelegate>\",W,N,V_delegate"
+ "T@\"<MIBUPersonalizationOperationDelegate>\",W,N,V_personalizationDelegate"
+ "T@\"MIBUPersonalizationOperation\",&,N,V_personalizationOperation"
+ "T@\"MIBUPersonalizationStatusReporter\",&,N,V_statusReporter"
+ "T@\"NSDate\",&,N,V_downloadedAssetExpiryTimestamp"
+ "T@\"NSDate\",&,N,V_shutdownTimestamp"
+ "T@\"NSDate\",R,C,N,V_assetExpiryTimestamp"
+ "T@\"NSDate\",R,C,N,V_shutdownTimestamp"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_cancelSem"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_cancelSemaphore"
+ "T@\"NSString\",C,N,V_downloadedOrderID"
+ "T@\"NSString\",C,N,V_downloadedWorkflowID"
+ "T@\"NSString\",R,C,N,V_orderID"
+ "T@\"NSString\",R,C,N,V_serialNumber"
+ "T@\"NSString\",R,C,N,V_workflowID"
+ "T@\"PCPersistentTimer\",&,N,V_watchdogTimer"
+ "TB,N,V_skipShelfLifeMode"
+ "TB,R,N,V_personalizationComplete"
+ "TB,V_cancelled"
+ "TB,V_terminated"
+ "Tq,R,N,V_status"
+ "UNKNOWN"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "URLWithString:relativeToURL:"
+ "Unrecognized pandora cert context: %@"
+ "Use Pandora Key Server certificates of grade: %{public}@, use case: %{public}@"
+ "WORKFLOW_ID"
+ "Watchdog fired after termination, ignoring"
+ "WiFi cancelled; stop retrying wifi connection"
+ "WiFi connection cancelled"
+ "WiFi connection wait cancelled"
+ "^{__SecIdentity=}"
+ "^{__SecIdentity=}16@0:8"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
+ "_URLSession"
+ "_assetExpiryTimestamp"
+ "_cancelSem"
+ "_cancelSemaphore"
+ "_certificateChain"
+ "_clientIdentity"
+ "_createStatusUpdateRequestForURL:withSignedPayload:outError:"
+ "_deleteBAAKeychainItems"
+ "_downloadedAssetExpiryTimestamp"
+ "_downloadedOrderID"
+ "_downloadedWorkflowID"
+ "_fetchBAACredentials"
+ "_interruptibleSleepForInterval:"
+ "_loadClientIdentity"
+ "_operationDoneWithShutdown:reportStatus:error:"
+ "_orderID"
+ "_pandoraCertificatesForContext:error:"
+ "_personalizationComplete"
+ "_personalizationDelegate"
+ "_personalizationOperation"
+ "_postURL"
+ "_referenceKey"
+ "_reportFinalStatusWithError:"
+ "_reportingServerURL"
+ "_sendQueue"
+ "_shutdownTimestamp"
+ "_signPayload:error:"
+ "_skipShelfLifeMode"
+ "_statusReporter"
+ "_workflowID"
+ "addValue:forHTTPHeaderField:"
+ "aks_get_convenience_bio_state"
+ "application/json"
+ "array"
+ "assetExpiryTimestamp"
+ "authenticationMethod"
+ "cancelAllOperations"
+ "cancelSem"
+ "cancelSemaphore"
+ "certificate"
+ "certificateChain"
+ "com.apple.inboxupdaterd.statusreporter"
+ "com.apple.mobileinboxupdater.personalizationwatchdog"
+ "credentialForTrust:"
+ "credentialWithIdentity:certificates:persistence:"
+ "dataTaskWithRequest:completionHandler:"
+ "defaultSessionConfiguration"
+ "dictionaryWithDictionary:"
+ "didRTCReset"
+ "download complete status"
+ "download failed status"
+ "downloadedAssetExpiryTimestamp"
+ "downloadedOrderID"
+ "downloadedWorkflowID"
+ "en_US_POSIX"
+ "finished status"
+ "handleWatchdogTimer:"
+ "https://production-personalization-coreos.ext.pos.apple.com"
+ "inboxupdaterd"
+ "initWithArray:"
+ "initWithPersonalizationDelegate:"
+ "initWithStatus:personalizationComplete:workflowID:orderID:shutdownTimestamp:assetExpiryTimestamp:"
+ "initWithURL:"
+ "invalidateAndCancel"
+ "isPersonalizationExpired:"
+ "key"
+ "localeWithLocaleIdentifier:"
+ "mTLS challenge received but no client identity available"
+ "not retriable"
+ "orderID"
+ "pandoraCertsDataForContext:error:"
+ "personalizationComplete"
+ "personalizationDelegate"
+ "personalizationDoneWithShutdown:reportStatus:error:"
+ "personalizationFinishedWithError:shutdown:"
+ "personalizationOperation"
+ "protectionSpace"
+ "recordDownloadDidFail"
+ "recordDownloadDidFinishWithWorkflowID:orderID:assetExpiryTimestamp:"
+ "reportStatus:"
+ "reportStatus:completion:"
+ "reportingServerURL"
+ "retriable"
+ "serverTrust"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "setCancelSem:"
+ "setCancelSemaphore:"
+ "setDownloadedAssetExpiryTimestamp:"
+ "setDownloadedOrderID:"
+ "setDownloadedWorkflowID:"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setPersonalizationDelegate:"
+ "setPersonalizationOperation:"
+ "setShutdownTimestamp:"
+ "setSkipShelfLifeMode:"
+ "setStatusReporter:"
+ "shutdown status"
+ "shutdownTimestamp"
+ "signature"
+ "skipShelfLifeMode"
+ "statusCode"
+ "statusReporter"
+ "timeZoneForSecondsFromGMT:"
+ "timestamp"
+ "v24@0:8@\"NSURLSession\"16"
+ "v28@0:8@\"NSError\"16B24"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8B16B20@\"NSError\"24"
+ "v32@0:8B16B20@24"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v32@?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8@\"NSArray\"16@\"NSError\"24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDate\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@16@24@?32"
+ "wifiAssociationDidFinish"
+ "workflowID"
+ "yyyy-MM-dd'T'HH:mm'Z'"
+ "yyyy-MM-dd'T'HH:mm:ss'Z'"
- "@\"<MIBUPersonalizationControllerDelegate>\""
- "Attempting to fetch record from CloudKit (attempt %d/%d)"
- "Failed to fetch record after %d attempts"
- "Failed to fetch record from CloudKit after %d attempts"
- "Failed to fetch record on attempt %d/%d"
- "Failed to serialize stripped personalization data: %{public}@"
- "Failed to strip sensitive personalization data: %{public}@"
- "Failed to write stripped personalization data: %{public}@"
- "MIBUPersonalizationControllerDelegate"
- "MobileAssetAssetAudience-com.apple.MobileAsset.MobileSoftwareUpdate.UpdateBrain"
- "MobileAssetAssetAudience-com.apple.MobileAsset.SoftwareUpdate"
- "No personalization data found, nothing to strip"
- "No valid expiration date found, treating as not expired"
- "Overridden MA defaults: %{public}@"
- "Overridding MA defaults for reset: %{bool}d"
- "PallasUrlOverrideV2"
- "Personalization controller not running"
- "Personalization data has expired (expiration date: %{public}@), stripping sensitive data"
- "Sensitive key already absent, no stripping needed"
- "Successfully stripped sensitive data from personalization file"
- "T@\"<MIBUPersonalizationControllerDelegate>\",W,N,V_delegate"
- "TB,N,V_terminated"
- "Use Pandora Key Server certificates of grade: %{public}@"
- "_operationDoneWithShutdown:error:"
- "_pandoraCertificates:"
- "checkAndStripExpiredPersonalizationData:"
- "com.apple.MobileAsset"
- "initWithSuiteName:"
- "overrideMAPallasDefaultsForReset:"
- "pandoraCertsData:"
- "personalizationDoneWithShutdown:error:"
- "v28@0:8B16@\"NSError\"20"
- "v28@0:8B16@20"
```
