## nfcd

> `/usr/libexec/nfcd`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x1f10a8
-  __TEXT.__auth_stubs: 0x17b0
+366.4.0.0.0
+  __TEXT.__text: 0x1fa044
+  __TEXT.__auth_stubs: 0x17c0
   __TEXT.__delay_stubs: 0x500
   __TEXT.__delay_helper: 0x16f4
-  __TEXT.__objc_stubs: 0xd400
-  __TEXT.__objc_methlist: 0x9b40
+  __TEXT.__objc_stubs: 0xdbc0
+  __TEXT.__objc_methlist: 0x9d58
   __TEXT.__const: 0x1384
-  __TEXT.__objc_methname: 0x149b0
-  __TEXT.__cstring: 0x21b12
-  __TEXT.__objc_classname: 0x1d80
-  __TEXT.__objc_methtype: 0x4ded
-  __TEXT.__oslogstring: 0x1f392
-  __TEXT.__unwind_info: 0x2dc8
-  __DATA_CONST.__auth_got: 0xc80
-  __DATA_CONST.__got: 0x5e8
+  __TEXT.__objc_methname: 0x15481
+  __TEXT.__cstring: 0x226e9
+  __TEXT.__objc_classname: 0x1e0e
+  __TEXT.__objc_methtype: 0x4ec6
+  __TEXT.__oslogstring: 0x1fc1d
+  __TEXT.__unwind_info: 0x2e88
+  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x95a0
-  __DATA_CONST.__cfstring: 0x11580
-  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__const: 0x9958
+  __DATA_CONST.__cfstring: 0x11820
+  __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x390
+  __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e8
-  __DATA_CONST.__objc_superrefs: 0x460
-  __DATA_CONST.__objc_intobj: 0x77e8
-  __DATA_CONST.__objc_arraydata: 0x1d30
-  __DATA_CONST.__objc_arrayobj: 0x2d0
-  __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA.__objc_const: 0x147e8
-  __DATA.__objc_selrefs: 0x4870
-  __DATA.__objc_ivar: 0x10a4
-  __DATA.__objc_data: 0x3d40
-  __DATA.__data: 0x2b94
-  __DATA.__bss: 0x290
+  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_intobj: 0x7a28
+  __DATA_CONST.__objc_arraydata: 0x1dd8
+  __DATA_CONST.__objc_arrayobj: 0x2e8
+  __DATA_CONST.__objc_dictobj: 0xfc8
+  __DATA.__objc_const: 0x14b90
+  __DATA.__objc_selrefs: 0x4ab8
+  __DATA.__objc_ivar: 0x10dc
+  __DATA.__objc_data: 0x3de0
+  __DATA.__data: 0x2bf4
+  __DATA.__bss: 0x2a0
   __DATA.__common: 0x12
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C940D517-2D08-30F7-836C-EFD7C293B629
-  Functions: 4163
-  Symbols:   585
-  CStrings:  13594
+  UUID: A45DADC0-8C43-3B07-BA25-C8B4A817BE2E
+  Functions: 4221
+  Symbols:   594
+  CStrings:  13812
 
Symbols:
+ _CFArrayGetTypeID
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NFCoreNFCPollConfig
+ _OBJC_CLASS_$_NFLocationService
+ _OBJC_CLASS_$_NFPaymentTagReaderDeveloperPresentmentReport
+ _OBJC_CLASS_$_NFPaymentTagReaderDeveloperPresentmentSessionData
+ _OBJC_CLASS_$_NFReportingService
+ _OBJC_CLASS_$_NSJSONSerialization
CStrings:
+ "%{public}s:%i %llu reports"
+ "%{public}s:%i %{public}@ %{public}@activation for endpoints %{public}@"
+ "%{public}s:%i %{public}@ - Saving developer presentment data, but no location!"
+ "%{public}s:%i Cannot create SecTaskRef with XPC Connection: %{public}@"
+ "%{public}s:%i Checking availability for BundleID %{public}@, TeamID %{public}@"
+ "%{public}s:%i Error fetching receipt: %@"
+ "%{public}s:%i Existing receipt is too old (%lf seconds)"
+ "%{public}s:%i Failed to configure reporter: %{public}@"
+ "%{public}s:%i Failed to fetch report %{public}@: %{public}@"
+ "%{public}s:%i Failed to send report - got HTTP Response code %d"
+ "%{public}s:%i Failed to send report: %{public}@: %{public}@"
+ "%{public}s:%i Failed to serialize report JSON: %{public}@"
+ "%{public}s:%i Failed to start wired mode to eSE"
+ "%{public}s:%i Ignore dev mode check"
+ "%{public}s:%i Ignore due to first unlock not completed"
+ "%{public}s:%i Invalid configuration, %{public}@"
+ "%{public}s:%i Invalid session type %lu"
+ "%{public}s:%i Location for %{public}@ updated"
+ "%{public}s:%i Location service start error: %{public}@"
+ "%{public}s:%i Missing NFCReaderUsageDescription"
+ "%{public}s:%i Missing entitlement required for Core NFC operation; reject connection"
+ "%{public}s:%i Missing required entitlement."
+ "%{public}s:%i No receipt stored"
+ "%{public}s:%i Receipt is recent (%lf seconds), denied: %d"
+ "%{public}s:%i Report %{public}@ is ready to be sent, sending now"
+ "%{public}s:%i Report send failed: %{public}@"
+ "%{public}s:%i Report sent, HTTP %d"
+ "%{public}s:%i Saving presentment data for %{public}@/%{public}@: %@"
+ "%{public}s:%i Sending report: %@"
+ "%{public}s:%i Server reporting not available yet, report %{public}@ not sent. Allowing feature to be used"
+ "%{public}s:%i Session was stopped before it started"
+ "%{public}s:%i Temporary %{public}@activation for keys %{public}@"
+ "%{public}s:%i Terminate session due to fraudulent location detected"
+ "%{public}s:%i Time traveler!"
+ "%{public}s:%i Unexpected state; fail to retrieve app bundle record."
+ "%{public}s:%i Unexpected state; missing bundle identifier."
+ "%{public}s:%i Unexpected state; missing signer organization."
+ "%{public}s:%i [PaymentReader] Developer presentment denied for bundle %{public}@"
+ "%{public}s:%i applet: activate:%d  %{public}@  keyIdentifiers: %{public}@"
+ "%{public}s:%i config=%{public}@, validUiMode=%d, validSessionType=%d"
+ "%{public}s:%i visible=%d"
+ "+[_NFReaderSession(Entitlement) _locationServiceValidationWithAuditToken:outBundleIdentifier:]"
+ "+[_NFReaderSession(Entitlement) isCNFCPaymentEligibleWithUserPrompt:auditToken:ignoreAuditToken:outBundleIdentifier:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentLogger checkAvailabilityForBundleID:teamID:completion:]_block_invoke"
+ "-[NFPaymentTagReaderDeveloperPresentmentLogger savePresentmentDataForBundleID:teamID:presentmentData:]_block_invoke"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter _checkLocalAvailabilityForBundleID:teamID:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter _sendPresentmentReport:outError:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter _sendReportToServer:outError:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter postDailyReports]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter savePresentmentDataForBundleID:teamID:presentmentData:]"
+ "-[NFSecureElementWrapper(CardManagement) _setTemporaryVisibilityOnAllEndpointsOfSelectedApplet:]"
+ "-[NFSecureElementWrapper(CardManagement) _setupEndpoints:activate:]"
+ "-[NFSecureElementWrapper(CardManagement) activateKeys:forIdentifiers:onApplet:]"
+ "-[_NFContactlessSession _activateKeys:forIdentifiers:onApplet:]"
+ "-[_NFHardwareManager _queuePaymentReaderSession:sessionConfig:allowList:xpcConnection:completion:]"
+ "-[_NFHardwareManager _queuePaymentReaderSession:sessionConfig:allowList:xpcConnection:completion:]_block_invoke"
+ "-[_NFHardwareManager _validateCoreNfcReaderSessionConfig:]"
+ "-[_NFHardwareManager(Headless) disableLPEMFeatureFromSession:completion:]_block_invoke"
+ "-[_NFHardwareManager(Headless) enableLPEMFeature:completion:]_block_invoke"
+ "-[_NFHardwareManager(Headless) enableLPEMFeatureFromSession:completion:]_block_invoke"
+ "-[_NFHardwareManager(LocationService) _resumeSessionWaitingOnLocationUpdate:]"
+ "-[_NFHardwareManager(LocationService) _startLocationServiceListener:]"
+ "-[_NFHardwareManager(LocationService) _terminateSessionInLocationSimulation:]"
+ "-[_NFHardwareManager(LocationService) listenerStartedWithBundleIdentifier:]"
+ "-[_NFHardwareManager(LocationService) locationAuthDenied:]"
+ "-[_NFHardwareManager(LocationService) locationSimulationDetected:]"
+ "-[_NFHardwareManager(LocationService) locationUpdated:location:]"
+ "-[_NFHardwareManager(NSXPCListenerDelegate) _validateCoreNFCConnection:]"
+ "-[_NFReaderSession _saveDeveloperPresentmentData]"
+ "-[_NFReaderSession locationUpdated:]"
+ "-[_NFReaderSession(Entitlement) validateEntitlements:sessionType:outError:]"
+ "@\"NFLocation\""
+ "@\"NFLocationService\""
+ "@\"NFReportingService\""
+ "@\"NFStorageService\""
+ "@36@0:8B16@20@28"
+ "@80@0:8@16@24@32Q40Q48Q56@64B72B76"
+ "B40@0:8@16Q24^@32"
+ "DisablePaymentReaderDevevelopmentServerReporting"
+ "Failed to set instance visibility"
+ "I32@0:8@16@24"
+ "ISO15693"
+ "IgnorePaymentReaderDevelopmentEntitlementCheck"
+ "Location service is not authorized"
+ "Location simulation detected"
+ "LocationService"
+ "LocationServiceListener"
+ "Missing required entitlement to enable NFCPaymentTagReaderSession developer mode"
+ "NFCD built from (B&I) Stockholm_Base-366.4"
+ "NFLocationServiceListenerDelegate"
+ "NFPaymentTagReaderDeveloperPresentmentLogger"
+ "NFPaymentTagReaderDeveloperPresentmentReporter"
+ "No Response from SE"
+ "No Response from SE for endpoint keyID: %@"
+ "Non-9000 Response from SE for endpoint keyID: %@, Response: 0x%04X"
+ "Non-90000 response. Response: 0x%04X"
+ "PST"
+ "PTA"
+ "Q24@0:8d16"
+ "Q56@0:8{?=[8I]}16^@48"
+ "Q64@0:8B16{?=[8I]}20B52^@56"
+ "T@\"NSDate\",R,&,V_sessionEndDate"
+ "T@\"NSDate\",R,&,V_sessionStartDate"
+ "TAG"
+ "TB,V_startOnLocationUpdate"
+ "Unable to set endpoint visibility"
+ "Unexpected class"
+ "User has denied access to location services"
+ "VAS"
+ "Z"
+ "_NFReaderSession+Entitlement.m"
+ "_activateKeys:forIdentifiers:onApplet:"
+ "_allowedBeforeFirstUnlock"
+ "_checkLocalAvailabilityForBundleID:teamID:"
+ "_configureReporter"
+ "_devPresentmentTapCount"
+ "_disableServerReporting"
+ "_iReporterTimestampForUTCTimeInterval:"
+ "_isCNFCDevTestMode"
+ "_isProdSE"
+ "_isReporterConfigured"
+ "_location"
+ "_locationService"
+ "_locationServiceValidationWithAuditToken:outBundleIdentifier:"
+ "_queuePaymentReaderSession:sessionConfig:allowList:xpcConnection:completion:"
+ "_queueReaderSession:sessionConfig:serviceType:allowList:xpcConnection:completion:"
+ "_reportingService"
+ "_saveDeveloperPresentmentData"
+ "_sendPresentmentReport:outError:"
+ "_sendReportToServer:outError:"
+ "_sessionEndDate"
+ "_sessionListForBundleIdentifier:"
+ "_sessionStartDate"
+ "_setupEndpoints:activate:"
+ "_startOnLocationUpdate"
+ "_storageService"
+ "_terminateSessionInLocationSimulation:"
+ "_terminateSessionWaitingOnLocationUpdate:"
+ "_validateCoreNFCConnection:"
+ "activateKeys:forIdentifiers:onApplet:"
+ "allowedBeforeFirstUnlock"
+ "altitude"
+ "bundleID"
+ "calendarWithIdentifier:"
+ "checkAvailabilityForBundleID:teamID:completion:"
+ "city"
+ "com.apple.developer.nfc.hce"
+ "com.apple.developer.nfc.readersession.formats"
+ "com.apple.nfc.reader.developerpresentments"
+ "configureReporterWithSEKeying:"
+ "coreNFCUISetAccess:"
+ "coreNFCUISetScanMode:"
+ "country"
+ "createPreUnlockSession:workQueue:sessionQueuer:didStartWork:"
+ "dataWithJSONObject:options:error:"
+ "deleteDeveloperPaymentReportWithID:"
+ "disableLPEMFeatureFromSession:completion:"
+ "enableLPEMFeatureFromSession:completion:"
+ "endTimestamp"
+ "fetchDeveloperPaymentReportWithID:outError:"
+ "fetchDeveloperPaymentReportsWithError:"
+ "getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:"
+ "horizontalAccuracy"
+ "i32@0:8@16^@24"
+ "initWithRemoteObject:workQueue:whitelist:serviceType:showSharingUI:coreNFCSessionType:scanText:delayConnectionHandoverRestart:isCNFCDevTestMode:"
+ "initWithReportId:timestampDay:bundleID:teamID:developmentPresentments:"
+ "initWithStartTimestamp:endTimestamp:latitude:longitude:altitude:horizontalAccuracy:city:state:country:successfulTapCount:"
+ "invalidateListener:"
+ "isBeta"
+ "isCNFCPaymentEligibleWithUserPrompt:auditToken:ignoreAuditToken:outBundleIdentifier:"
+ "isDevTestMode"
+ "isProfileValidated"
+ "jsonDictionary"
+ "latitude"
+ "listenerStartedWithBundleIdentifier:"
+ "locationAuthDenied:"
+ "locationSimulationDetected"
+ "locationSimulationDetected:"
+ "locationUpdated:"
+ "locationUpdated:location:"
+ "longitude"
+ "nfcPaymentTagReaderDeveloperMode"
+ "nil != entitlementCheckError"
+ "postDailyReports"
+ "postPaymentTagReaderDeveloperPresentmentReportsWithCompletion:"
+ "reportId"
+ "saveDeveloperPaymentPresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:"
+ "savePresentmentDataForBundleID:teamID:presentmentData:"
+ "sendReport:outError:"
+ "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:startOnLocationUpdate:isDevTestMode:"
+ "sessionEndDate"
+ "sessionStartDate"
+ "setIsDevTestMode:"
+ "setProductionSEKeying:"
+ "setStartOnLocationUpdate:"
+ "setTimeZone:"
+ "sharedInstance"
+ "signerOrganization"
+ "startListenerWithBundleIdentifier:delegate:error:"
+ "startOfDayForDate:"
+ "startOnLocationUpdate"
+ "teamID"
+ "teamIdentifier"
+ "temporary"
+ "timeZoneWithAbbreviation:"
+ "updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:"
+ "v20@?0I8@\"NSError\"12"
+ "v32@0:8@\"NSString\"16@\"NFLocation\"24"
+ "validateEntitlements:sessionType:outError:"
+ "\xf0Aa"
- "%{public}s:%i Cannot disable LPEM feature when recovery is active"
- "%{public}s:%i Cannot enable LPEM feature when recovery is active"
- "+[_NFReaderSession(Entitlement) isCNFCPaymentEligibleWithUserPrompt:auditToken:ignoreAuditToken:]"
- "-[_NFHardwareManager(Headless) enableLPEMFeature:rebootIfNeeded:completion:]_block_invoke"
- "@76@0:8@16@24@32Q40Q48Q56@64B72"
- "NFCD built from (B&I) Stockholm_Base-365.3.1"
- "Q56@0:8B16{?=[8I]}20B52"
- "X"
- "_sessionStartTime"
- "enableLPEMFeature:rebootIfNeeded:completion:"
- "initWithRemoteObject:workQueue:whitelist:serviceType:showSharingUI:coreNFCSessionType:scanText:delayConnectionHandoverRestart:"
- "isCNFCPaymentEligibleWithUserPrompt:auditToken:ignoreAuditToken:"
- "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:"
- "\xf0!q"

```
