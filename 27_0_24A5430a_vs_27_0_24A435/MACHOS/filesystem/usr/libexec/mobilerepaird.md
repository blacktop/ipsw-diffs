## mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 1307.2.4.0.0
-  __TEXT.__text: 0xe1c8
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0xcfc
-  __TEXT.__const: 0xaa
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__objc_methname: 0x2140
-  __TEXT.__cstring: 0x242b
-  __TEXT.__oslogstring: 0xac6
-  __TEXT.__objc_classname: 0x2e1
-  __TEXT.__objc_methtype: 0x3da
-  __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__const: 0x458
-  __DATA_CONST.__cfstring: 0x2380
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__text: 0x1cea4
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x3660
+  __TEXT.__objc_methlist: 0x17fc
+  __TEXT.__const: 0x152
+  __TEXT.__gcc_except_tab: 0x988
+  __TEXT.__objc_methname: 0x3f4a
+  __TEXT.__cstring: 0x3de6
+  __TEXT.__oslogstring: 0x2ad9
+  __TEXT.__objc_classname: 0x55f
+  __TEXT.__objc_methtype: 0xce2
+  __TEXT.__ustring: 0x12a
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_typeref: 0x3b
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x718
+  __DATA_CONST.__const: 0xbc0
+  __DATA_CONST.__cfstring: 0x3e40
+  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x330
-  __DATA.__objc_const: 0x1b08
-  __DATA.__objc_selrefs: 0x8e0
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x820
-  __DATA.__data: 0x190
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x2e28
+  __DATA.__objc_selrefs: 0x1058
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_data: 0xe20
+  __DATA.__data: 0x458
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
   - /System/Library/PrivateFrameworks/BatteryDischarge.framework/BatteryDischarge

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 292
-  Symbols:   201
-  CStrings:  824
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 594
+  Symbols:   292
+  CStrings:  1549
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDictionaryGetValue
+ _CFGetTypeID
+ _CFPreferencesCopyAppValue
+ _CFPreferencesGetAppBooleanValue
+ _CFRetain
+ _CFStringGetTypeID
+ _DeviceIdentityIssueClientCertificateWithCompletion
+ _IOPSShippingChargeLimitEnable
+ _IOPSShippingChargeLimitGetState
+ _MAECopyActivationRecordWithError
+ _MAEGetActivationStateWithError
+ _MAGetActivationState
+ _NSCocoaErrorDomain
+ _NSHomeDirectory
+ _NSLocalizedFailureReasonErrorKey
+ _NSURLAuthenticationMethodServerTrust
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_CRBatteryAuxStatus
+ _OBJC_CLASS_$_CRDisplayMainStatus
+ _OBJC_CLASS_$_CRFcamMainStatus
+ _OBJC_CLASS_$_CRFcamStatus
+ _OBJC_CLASS_$_CRIOBoardStatus
+ _OBJC_CLASS_$_CRShipModeBatteryDischargeShim
+ _OBJC_CLASS_$_CRShipModeServerResponse
+ _OBJC_CLASS_$_DDRResetOptions
+ _OBJC_CLASS_$_DDRResetRequest
+ _OBJC_CLASS_$_DDRResetService
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSURLCredential
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_CRShipModeBatteryDischargeShim
+ _SecCertificateCopyData
+ _SecCertificateCreateWithData
+ _SecCertificateGetTypeID
+ _SecKeyCreateSignature
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_NETWORK_TRANSFER_DIRECTION
+ _XPC_ACTIVITY_NETWORK_TRANSFER_DIRECTION_UPLOAD
+ __Block_copy
+ __Block_release
+ ___NSDictionary0__struct
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _dispatch_get_global_queue
+ _kMAActivationStateFactoryActivated
+ _kMADeviceConfigurationFlags
+ _kMAOptionsBAAOIDDeviceIdentifiers
+ _kMAOptionsBAAOIDDeviceOSInformation
+ _kMAOptionsBAAOIDSToInclude
+ _kMAOptionsBAAOIDUCRTDeviceIdentifiers
+ _kMAOptionsBAASCRTAttestation
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_opt_self
+ _objc_retainBlock
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_setProperty_nonatomic_copy
+ _objc_terminate
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_transaction_create
+ _swift_allocObject
+ _swift_deallocObject
+ _swift_getObjectType
+ _swift_once
+ _swift_release_x19
+ _xpc_activity_unregister
CStrings:
+ "\n"
+ "\n\n"
+ "\n…[truncated, %lu bytes total]…"
+ "   "
+ " |"
+ "%02x "
+ "%08lx  "
+ "%@: %@\n"
+ "%C"
+ "%c"
+ "%s: IOPSShippingChargeLimitGetState failed (0x%08x); treating ship mode as unavailable (will retry)"
+ "%s: ship mode unsupported on this hardware; rejecting connection."
+ "%s: virtual device; ship mode unavailable"
+ "(empty)"
+ "(no error)"
+ "(none)"
+ "+[CRShipModeBatteryDischargeDriver dischargeUntilShippingCompliantWithThermalMode:completion:]"
+ "+[CRShipModeHelper isShipModeAvailable]"
+ "--- No Response ---\n(neither transport error nor HTTP response — should not happen)\n"
+ "--- Request ---\n"
+ "--- Request Body (%lu bytes) ---\n"
+ "--- Request Headers ---\n"
+ "--- Response ---\n"
+ "--- Response Body (%lu bytes) ---\n"
+ "--- Response Headers ---\n"
+ "--- Transport Error ---\n"
+ "-----BEGIN CERTIFICATE-----\n%@\n-----END CERTIFICATE-----\n"
+ "-[MRShipModeDelegate listener:shouldAcceptNewConnection:]"
+ "/"
+ "/tmp"
+ "/v/shipMode"
+ "/v/shipMode/status"
+ "1"
+ "<nil>"
+ "<none>"
+ "<set>"
+ "<unknown>"
+ "=== Shipmode Notify (X-Reference-Id: %@) ===\n"
+ "@\"CRShipModeNotifyEngine\""
+ "@\"CRShipModeOperation\""
+ "@\"CRShipModeOperationStore\""
+ "@\"NSError\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSUUID\""
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@?16"
+ "@28@0:8@16B24"
+ "@32@0:8q16@24"
+ "@40@0:8@16^{__SecKey=}24^@32"
+ "@48@0:8q16@24@32@40"
+ "@?"
+ "B24@0:8@?16"
+ "B24@0:8@?<v@?B>16"
+ "B28@0:8@16B24"
+ "B32@0:8@16^@24"
+ "B32@0:8^@16^@24"
+ "B32@0:8q16@?24"
+ "B32@0:8q16@?<v@?B@\"NSString\">24"
+ "B40@0:8^^{__SecKey}16^@24^@32"
+ "B48@0:8B16B20@24^@32^@40"
+ "B80@0:8@16^B24^B32^@40^@48^@56^q64^@72"
+ "B8@?0"
+ "BAA authentication failed (401)"
+ "BAA certificate chain invalid"
+ "BAA certificate issuance failed"
+ "BAA certificate issuance timed out"
+ "BAA leaf certificate malformed"
+ "BAA leaf certificate not valid X.509"
+ "BAA signing failed"
+ "Battery discharge failed"
+ "Battery is not trusted"
+ "CRDisplayMainTCONStatus"
+ "CRRepairShipModeProtocol"
+ "CRShipMode-TradeIn"
+ "CRShipModeBatteryDischargeBackend"
+ "CRShipModeBatteryDischargeDriver"
+ "CRShipModeBatteryDischargeDriver: nil completion passed to %s; refusing"
+ "CRShipModeBatteryDischargeRealBackend"
+ "CRShipModeBatteryDischargeShim"
+ "CRShipModeDDREraseObserver"
+ "CRShipModeDeviceErrorReported"
+ "CRShipModeHelper"
+ "CRShipModeHelper: cleared ship lock marker"
+ "CRShipModeHelper: device-error report already delivered this session; skipping re-notify"
+ "CRShipModeHelper: fetchShipModeResumeState → InProgress (tradeIn=%d erase=%d)"
+ "CRShipModeHelper: fetchShipModeResumeState → Ineligible (marker present, not ship-ready, viaTradeIn=%d)"
+ "CRShipModeHelper: fetchShipModeResumeState → None (eligible=%d marker=%d)"
+ "CRShipModeHelper: fetchShipModeResumeState → ReadyToUndo (viaTradeIn=%d)"
+ "CRShipModeHelper: fetchShipModeStatus"
+ "CRShipModeHelper: recorded ship-mode device-error report"
+ "CRShipModeHelper: set ship lock marker (viaTradeIn=%d)"
+ "CRShipModeHelper: setShipChargeLimit enable=%d timeout=%lu"
+ "CRShipModeHelper: submitShipModeNotification enabled=%d deviceError=%d partner=%{public}@"
+ "CRShipModeLockMarker"
+ "CRShipModeLockProvenanceViaTradeIn"
+ "CRShipModeNotifyEngine"
+ "CRShipModeNotifyEngine: Environment '%{public}@' is not recognized; falling through"
+ "CRShipModeNotifyEngine: Environment '%{public}@' → %{public}@"
+ "CRShipModeNotifyEngine: NotifyBaseURL '%{public}@' is not a valid https URL; falling through"
+ "CRShipModeNotifyEngine: NotifyBaseURL override → %{public}@"
+ "CRShipModeNotifyPinningDelegate"
+ "CRShipModeOperation"
+ "CRShipModeOperation: decoded %s out of range (%ld); rejecting archive"
+ "CRShipModeOperationScheduler"
+ "CRShipModeOperationScheduler: %{public}@ submit %{public}@ enqueued (discharge=%d notify=%d erase=%d)"
+ "CRShipModeOperationScheduler: %{public}@ submit persistence failed: %{private}@"
+ "CRShipModeOperationScheduler: BatteryDischarge SPI reported success=%d err=%{public}@"
+ "CRShipModeOperationScheduler: BatteryDischarge SPI unavailable; relying on firmware compliance poll"
+ "CRShipModeOperationScheduler: BatteryDischarge stopDischarge returned %d"
+ "CRShipModeOperationScheduler: DDR completion reported failure: %{private}@"
+ "CRShipModeOperationScheduler: DDR completion reported success"
+ "CRShipModeOperationScheduler: DDR observer reported failure (domain=%{public}@ code=%ld): %{private}@"
+ "CRShipModeOperationScheduler: DDR observer reported success"
+ "CRShipModeOperationScheduler: IOPSShippingChargeLimitGetState read failure; will retry"
+ "CRShipModeOperationScheduler: armed notify-retry activity"
+ "CRShipModeOperationScheduler: battery locked and compliant; discharge step done"
+ "CRShipModeOperationScheduler: battery not trusted at discharge step for %{public}@; refusing to latch"
+ "CRShipModeOperationScheduler: cancel issued with empty slot — preserving any posted followups"
+ "CRShipModeOperationScheduler: cancelled operation %{public}@"
+ "CRShipModeOperationScheduler: cleared Ready to Ship followup (marker preserved)"
+ "CRShipModeOperationScheduler: cleared ship-mode followup"
+ "CRShipModeOperationScheduler: disarmed notify-retry activity"
+ "CRShipModeOperationScheduler: discharge monitor stopping; operation no longer live"
+ "CRShipModeOperationScheduler: discharge not yet ready (enabled=%d compliant=%d); will retry"
+ "CRShipModeOperationScheduler: discharge step for %{public}@"
+ "CRShipModeOperationScheduler: erase step for %{public}@"
+ "CRShipModeOperationScheduler: failed to clear FollowUp %{public}@: %{public}@"
+ "CRShipModeOperationScheduler: failed to post FollowUp %{public}@: %{public}@"
+ "CRShipModeOperationScheduler: hydrated %{public}@ (step=%ld)"
+ "CRShipModeOperationScheduler: invoking DDR reset"
+ "CRShipModeOperationScheduler: notify step for %{public}@"
+ "CRShipModeOperationScheduler: operation %{public}@ complete; retaining slot for UI poll"
+ "CRShipModeOperationScheduler: posted FollowUp %{public}@"
+ "CRShipModeOperationScheduler: ship charge limit unsupported; treating discharge as complete"
+ "CRShipModeOperationStore"
+ "CRShipModeOperationStore: delete failed: %{private}@"
+ "CRShipModeOperationStore: encode failed: %{private}@"
+ "CRShipModeOperationStore: failed to create %{public}@: %{private}@"
+ "CRShipModeOperationStore: failed to decode %{public}@: %{private}@"
+ "CRShipModeOperationStore: read failed for %{public}@: %{private}@"
+ "CRShipModeOperationStore: write failed for %{public}@: %{private}@"
+ "CRShipModeReadShipChargeLimitFlags: IOPSShippingChargeLimitGetState failed (0x%08x); treating as unsupported"
+ "Cannot create ship-mode listener"
+ "Captured-At: %@\n\n"
+ "Code:        %ld\n"
+ "Content-Type"
+ "DDR erase failed"
+ "DDRResetObserver"
+ "DDRResetRequest -initWithMode:options:reason: returned nil"
+ "DDRResetService sharedInstance returned nil"
+ "DER did not round-trip through SecCertificateCreateWithData"
+ "DER too short: %lu bytes"
+ "DISPLAYMAINTCON_FOLLOWUP_INFO"
+ "DISPLAYMAINTCON_FOLLOWUP_TITLE"
+ "DISPLAYMAINTCON_POPUP_INFO"
+ "DISPLAYOUTRTCON_FOLLOWUP_INFO"
+ "DISPLAYOUTRTCON_FOLLOWUP_TITLE"
+ "DISPLAYOUTRTCON_POPUP_INFO"
+ "Description: %@\n"
+ "Device erase failed after chain completed"
+ "Device not found (404)"
+ "DeviceError"
+ "DeviceIdentity did not complete within %llds"
+ "DeviceIdentity returned no key"
+ "Domain:      %@\n"
+ "Empty status response body"
+ "Enabled"
+ "Enabled and DeviceError must be present"
+ "Environment"
+ "FINISH_BATTERYAUX_REPAIR_DESC"
+ "FINISH_BATTERYAUX_REPAIR_TITLE"
+ "FINISH_BATTERYMAIN_REPAIR_DESC"
+ "FINISH_BATTERYMAIN_REPAIR_TITLE"
+ "FINISH_DISPLAYMAIN_REPAIR_DESC"
+ "FINISH_DISPLAYMAIN_REPAIR_TITLE"
+ "FINISH_DISPLAYOUTR_REPAIR_DESC"
+ "FINISH_DISPLAYOUTR_REPAIR_TITLE"
+ "FINISH_FCAM_MAIN_REPAIR_DESC"
+ "FINISH_FCAM_MAIN_REPAIR_TITLE"
+ "FINISH_FCAM_REPAIR_DESC"
+ "FINISH_FCAM_REPAIR_TITLE"
+ "FINISH_IOBOARD_REPAIR_DESC"
+ "FINISH_IOBOARD_REPAIR_TITLE"
+ "Failed to initialize ship mode notify engine"
+ "Failed to persist ship mode operation"
+ "Failed to register for EIC strobe notification B: %@. Ensure daemon is part of conclave: com.apple.mobilerepaird.conclave"
+ "Failed to serialize ShipModeRequestInfo plist"
+ "Failed to serialize ShipModeStatus request plist"
+ "HTTP Status: %ld\n\n"
+ "HTTPBody"
+ "HTTPMethod"
+ "IMPORTANT_BATTERYAUX_MESSAGE"
+ "IMPORTANT_BATTERYMAIN_MESSAGE"
+ "IMPORTANT_DISPLAYMAIN_MESSAGE"
+ "IMPORTANT_DISPLAYOUTR_MESSAGE"
+ "IMPORTANT_FCAM_MAIN_MESSAGE"
+ "IMPORTANT_FCAM_MESSAGE"
+ "IOPSShippingChargeLimitEnable failed (0x%08x)"
+ "IsVirtualDevice"
+ "JSONObjectWithData:options:error:"
+ "Library/MobileRepair"
+ "Localizable-V68"
+ "LogRequestsToTmp"
+ "MRBatteryAuxComponentHandler"
+ "MRDisplayMainComponentHandler"
+ "MRDisplayMainTCONComponentHandler"
+ "MRFcamComponentHandler"
+ "MRFcamMainComponentHandler"
+ "MRIOBoardComponentHandler"
+ "MRShipModeDelegate"
+ "Method:  %@\n"
+ "Missing ShipModeServerInfo in response"
+ "NSCoding"
+ "NSSecureCoding"
+ "NSURLSessionDelegate"
+ "NSURLSessionTaskDelegate"
+ "Network request failed"
+ "No leaf certificate in chain"
+ "Non-HTTP response"
+ "Non-HTTP response to status request"
+ "NotifyBaseURL"
+ "POST"
+ "PartnerID"
+ "PartnerInfo"
+ "PartnerName"
+ "Ready to Ship"
+ "Received a connection on com.apple.mobilerepair.shipmode!"
+ "Registering for EIC strobe daemon notification B: %@"
+ "Response was not XML plist"
+ "SHIPMODE_READY_FOLLOWUP_INFO"
+ "SHIPMODE_READY_FOLLOWUP_TITLE"
+ "Serial"
+ "SerialNumber"
+ "Server processing error (500)"
+ "Server rejected request (400)"
+ "ShipChargeLimitCompliant"
+ "ShipChargeLimitEnabled"
+ "ShipChargeLimitSupported"
+ "ShipModeNotify: HTTP %ld"
+ "ShipModeNotify: POST %{public}@"
+ "ShipModeNotify: dumped request/response to %{public}@"
+ "ShipModeNotify: failed to write dump to %{public}@: %{private}@"
+ "ShipModeNotify: fetchStatus replyOnce called more than once — ignoring"
+ "ShipModeNotify: refusing HTTP redirect to %{private}@ (status=%ld)"
+ "ShipModeNotify: rejecting TLS challenge for unexpected host %{private}@ (allowed=%{private}@)"
+ "ShipModeNotify: replyOnce called more than once — ignoring"
+ "ShipModeNotify: skipping server-cert verification for non-production host %{private}@"
+ "ShipModeNotify: status HTTP %ld"
+ "ShipModeNotify: status HTTP %ld with empty body"
+ "ShipModeNotify: status fetch failed after successful write (204); reporting write success and echoing committed inputs: %{private}@"
+ "ShipModeNotify: status transport failure: %{private}@"
+ "ShipModeNotify: transport failure: %{private}@"
+ "ShipModeRequestInfo"
+ "ShipModeServerInfo"
+ "ShipModeServerInfo missing required fields"
+ "ShipModeTimerDuration"
+ "ShipModeTimerUnit"
+ "Status request failed"
+ "Successfully registered for EIC strobe notification B: %@"
+ "T@\"CRShipModeNotifyEngine\",R,N,V_engine"
+ "T@\"CRShipModeNotifyEngine\",R,N,V_notifyEngine"
+ "T@\"CRShipModeOperation\",&,N,V_operation"
+ "T@\"CRShipModeOperationStore\",R,N,V_store"
+ "T@\"NSError\",C,N,V_error"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_inFlightTransaction"
+ "T@\"NSString\",C,N,V_notifyPartnerID"
+ "T@\"NSUUID\",C,N,V_requestID"
+ "TB,N,R"
+ "TB,N,V_inFlight"
+ "TB,N,V_isRegisteredB"
+ "TB,N,V_needsDischarge"
+ "TB,N,V_needsErase"
+ "TB,N,V_needsNotify"
+ "TB,N,V_notifyDeviceError"
+ "TB,N,V_notifyEnabled"
+ "TB,N,V_readyFollowUpPosted"
+ "TB,N,V_retryActivityArmed"
+ "TB,R"
+ "T^{tb_daemon_listener_s=},N,V_notificationListenerB"
+ "Timeout: %.0fs\n\n"
+ "Tq,N,V_currentStep"
+ "Tq,N,V_failedStep"
+ "UNABLE_TO_VERIFY_BATTERYAUX_MESSAGE"
+ "UNABLE_TO_VERIFY_BATTERYAUX_NOTIF_TEXT"
+ "UNABLE_TO_VERIFY_BATTERYMAIN_MESSAGE"
+ "UNABLE_TO_VERIFY_BATTERYMAIN_NOTIF_TEXT"
+ "UNABLE_TO_VERIFY_DISPLAYMAIN_MESSAGE"
+ "UNABLE_TO_VERIFY_DISPLAYMAIN_NOTIF_TEXT"
+ "UNABLE_TO_VERIFY_DISPLAYOUTR_MESSAGE"
+ "UNABLE_TO_VERIFY_DISPLAYOUTR_NOTIF_TEXT"
+ "UNABLE_TO_VERIFY_FCAM_MAIN_MESSAGE"
+ "UNABLE_TO_VERIFY_FCAM_MAIN_NOTIF_TEXT"
+ "UNABLE_TO_VERIFY_FCAM_MESSAGE"
+ "UNABLE_TO_VERIFY_FCAM_NOTIF_TEXT"
+ "URL"
+ "URL:     %@\n"
+ "URLByAppendingPathComponent:"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByDeletingLastPathComponent"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didCreateTask:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didCompleteWithError:"
+ "URLSession:task:didFinishCollectingMetrics:"
+ "URLSession:task:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didReceiveInformationalResponse:"
+ "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
+ "URLSession:task:needNewBodyStream:"
+ "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
+ "URLSession:task:willBeginDelayedRequest:completionHandler:"
+ "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
+ "URLSession:taskIsWaitingForConnectivity:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "URLWithString:relativeToURL:"
+ "UTC"
+ "UUID"
+ "UUIDString"
+ "Unexpected HTTP status %ld"
+ "Unregistering exclave daemon notification listener B"
+ "User-Agent"
+ "UserInfo:    %@\n"
+ "X-BAA-Certificate"
+ "X-BAA-Signature"
+ "X-Reference-Id"
+ "Your iPhone battery has been discharged and is ready to ship."
+ "_advanceOperation"
+ "_allowedHost"
+ "_armNotifyRetryActivity"
+ "_boolFromInternalOnlyDefaultsKey:defaultValue:"
+ "_buildBodyEnabled:deviceError:partnerID:body:error:"
+ "_buildStatusBody:error:"
+ "_currentStep"
+ "_dataAsTextOrHex:"
+ "_deliverQueue"
+ "_delivered"
+ "_deviceSerialNumber"
+ "_disarmNotifyRetryActivity"
+ "_dumpRequestIfEnabled:command:responseBody:httpResponse:transportError:"
+ "_engine"
+ "_error"
+ "_errorForHTTPStatus:body:"
+ "_errorWithCode:description:reason:underlyingError:"
+ "_extractReasonFromBody:"
+ "_failedStep"
+ "_fetchStatusAndReply:"
+ "_fileURL"
+ "_inFlight"
+ "_inFlightTransaction"
+ "_ioQueue"
+ "_isDischargeStepLiveForID:"
+ "_isInternalBuild"
+ "_isProductionURL:"
+ "_isRegisteredB"
+ "_isRequestLoggingEnabled"
+ "_issueBAA:certificatePEM:error:"
+ "_mapDischargeStatusLocked"
+ "_mapNotifyStatusLocked"
+ "_needsDischarge"
+ "_needsErase"
+ "_needsNotify"
+ "_nextStepLocked"
+ "_notificationListenerB"
+ "_notifyDeviceError"
+ "_notifyEnabled"
+ "_notifyEngine"
+ "_notifyPartnerID"
+ "_notifyStepFinishedFor:error:"
+ "_operation"
+ "_overwriteSlotWith:kind:reply:"
+ "_parseServerInfoFromXMLPlist:enabled:deviceError:partnerID:partnerName:timerUnit:timerDuration:error:"
+ "_pemEncodedCertificateFromDER:"
+ "_performRequest:baseURL:enabled:deviceError:partnerID:replyOnce:"
+ "_performStatusRequest:statusURL:replyOnce:"
+ "_providerStepFinishedFor:step:errorCode:errorDescription:success:errorMessage:"
+ "_queue"
+ "_readyFollowUpPosted"
+ "_requestID"
+ "_resolveBaseURL"
+ "_resolveStatusURL"
+ "_resultHandler"
+ "_retryActivityArmed"
+ "_runDischargeStepFor:"
+ "_runEraseStepFor:"
+ "_runNotifyStepFor:"
+ "_runWithEnabled:deviceError:partnerID:replyOnce:"
+ "_signData:withKey:error:"
+ "_singleLinePEM:"
+ "_skipsVerification"
+ "_stopInFlightDischargeSPI"
+ "_store"
+ "_stringFromInternalOnlyDefaultsKey:"
+ "_urlForEnvironmentName:"
+ "absoluteString"
+ "absoluteURL"
+ "activation-notify"
+ "activation-notify-factory"
+ "activation_state changed"
+ "activation_state: device deactivated; invalidating ship-lock marker so the next boot re-derives from the server"
+ "addOberver:"
+ "allHTTPHeaderFields"
+ "allHeaderFields"
+ "allKeys"
+ "appendFormat:"
+ "appendString:"
+ "application/xml"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "authenticationMethod"
+ "backend"
+ "base64EncodedStringWithOptions:"
+ "bytes"
+ "cancelOperationWithReply:"
+ "cancelShipModeOperationWithReply:"
+ "caseInsensitiveCompare:"
+ "characterAtIndex:"
+ "clearReadyToShipFollowUpKeepingMarker"
+ "clearShipModeFollowupsWithReply:"
+ "clearShipModeLockMarker"
+ "code"
+ "com.apple.mobile.lockdown.activation_state"
+ "com.apple.mobilerepair.BatteryAuxRepair"
+ "com.apple.mobilerepair.DisplayMainRepair"
+ "com.apple.mobilerepair.batteryauxunlockchecker"
+ "com.apple.mobilerepair.displaymainnotifyServer"
+ "com.apple.mobilerepair.displaymainunlockchecker"
+ "com.apple.mobilerepair.shipmode"
+ "com.apple.mobilerepair.shipmode connection interrupted."
+ "com.apple.mobilerepair.shipmode connection invalidated."
+ "com.apple.mobilerepair.shipmode.chargelimitreply"
+ "com.apple.mobilerepair.shipmode.ddrobserver"
+ "com.apple.mobilerepair.shipmode.ddrreply"
+ "com.apple.mobilerepair.shipmode.discharge"
+ "com.apple.mobilerepair.shipmode.dischargesignal"
+ "com.apple.mobilerepair.shipmode.iokit"
+ "com.apple.mobilerepair.shipmode.notify"
+ "com.apple.mobilerepair.shipmode.readyToShip"
+ "com.apple.mobilerepair.shipmode.store"
+ "com.apple.mobilerepaird.eicstrobeb"
+ "com.apple.mobilerepaird.shipchargelimit"
+ "com.apple.mobilerepaird.shipmode.device-error-report"
+ "com.apple.mobilerepaird.shipmode.notify"
+ "com.apple.mobilerepaird.shipmode.notify-retry"
+ "com.apple.mobilerepaird.shipmode.operation"
+ "com.apple.mobilerepaird.shipmode.server-check"
+ "com.apple.mobilerepaird.shipmode.server-check.arbiter"
+ "com.apple.mobilerepaird.shipmode.status"
+ "com.apple.private.mobilerepair.shipmode"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "credentialForTrust:"
+ "currentStep"
+ "dataTaskWithRequest:completionHandler:"
+ "dataWithContentsOfURL:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "dealloc"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "deliver:errorMessage:"
+ "dev"
+ "development"
+ "deviceError"
+ "discharge"
+ "dischargeResultForRequestID:reply:"
+ "dischargeUntilShippingCompliantWithThermalMode:completion:"
+ "disengageBatteryShipChargeLimitWithTimeout:reply:"
+ "domain"
+ "en_US_POSIX"
+ "enabled"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "engine"
+ "ephemeralSessionConfiguration"
+ "error"
+ "exportedInterface"
+ "failedStep"
+ "fetchShipModeResumeStateWithReply:"
+ "fetchShipModeStatusWithReply:"
+ "fetchShipModeStatusWithResponseReply:"
+ "fetchStatusWithCompletion:"
+ "fileURLWithPath:isDirectory:"
+ "finishTasksAndInvalidate"
+ "firstUIDisplayedTimeForDisplayMain"
+ "hasDisplayedFollowupForBatteryAux"
+ "hasDisplayedFollowupForDisplayMain"
+ "hasNotifiedServerForBatteryAux"
+ "hasNotifiedServerForDisplayMain"
+ "host"
+ "https"
+ "https://activity-servicemap-dev-reno.us-west-2h.app.apple.com"
+ "https://deviceactivation-ut.shld.apple.com"
+ "https://deviceactivations.apple.com"
+ "inFlight"
+ "inFlightOperationSnapshotWithReply:"
+ "inFlightTransaction"
+ "initWithAllowedHost:skipsVerification:"
+ "initWithCoder:"
+ "initWithCompletion:"
+ "initWithEnabled:deviceError:partnerID:partnerName:shipModeTimerUnit:shipModeTimerDuration:"
+ "initWithMode:options:reason:"
+ "initWithRequestID:"
+ "integerValue"
+ "isAvailable"
+ "isFDRDataClassSupported:"
+ "isRegisteredB"
+ "isShipModeAvailable"
+ "isShipModeDeviceErrorReported"
+ "isShipModeLockMarkerPresent"
+ "lastCheckTimeForBatteryAux"
+ "lastCheckTimeForDisplayMain"
+ "lastKnownIDForDisplayMain"
+ "lastPathComponent"
+ "load"
+ "localeWithLocaleIdentifier:"
+ "lowercaseString"
+ "mobilerepaird-ShipModeNotify/1.0"
+ "needsDischarge"
+ "needsErase"
+ "needsNotify"
+ "notificationListenerB"
+ "notify"
+ "notifyDeviceError"
+ "notifyEnabled"
+ "notifyEngine"
+ "notifyPartnerID"
+ "notifyResultForRequestID:reply:"
+ "operation"
+ "operationResultForRequestID:reply:"
+ "partnerID"
+ "partnerName"
+ "path"
+ "postReadyToShipFollowUpWithReply:"
+ "prod"
+ "production"
+ "propertyListWithData:options:format:error:"
+ "protectionSpace"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "queue"
+ "readyFollowUpPosted"
+ "recordShipModeDeviceErrorReported"
+ "recordShipModeLockMarkerPresentViaTradeIn:"
+ "removeItemAtURL:error:"
+ "removeObserver:"
+ "requestID"
+ "requestWithURL:cachePolicy:timeoutInterval:"
+ "resetService:didBeginDataResetWithMode:"
+ "resetService:didCompleteDataResetMode:withError:completion:"
+ "resetService:willBeginDataResetWithMode:"
+ "resetWithRequest:completion:"
+ "resultForPersistentBatteryDischargeWithRequestID:reply:"
+ "resultForPersistentShipModeNotificationWithRequestID:reply:"
+ "resultForPersistentShipModeOperationWithRequestID:reply:"
+ "resumeWithActivity:"
+ "retriggerCheckCountForBatteryAux"
+ "retriggerCheckCountForDisplayMain"
+ "retryActivityArmed"
+ "save:error:"
+ "scheme"
+ "server-off"
+ "serverTrust"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "setBackendForTesting:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setCurrentStep:"
+ "setDateFormat:"
+ "setEraseDataPlan:"
+ "setError:"
+ "setFailedStep:"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setInFlight:"
+ "setInFlightTransaction:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setIsRegisteredB:"
+ "setLocale:"
+ "setNeedsDischarge:"
+ "setNeedsErase:"
+ "setNeedsNotify:"
+ "setNotificationListenerB:"
+ "setNotifyDeviceError:"
+ "setNotifyEnabled:"
+ "setNotifyPartnerID:"
+ "setOperation:"
+ "setReadyFollowUpPosted:"
+ "setRequestID:"
+ "setRetryActivityArmed:"
+ "setShipChargeLimit:timeout:reply:"
+ "setTimeZone:"
+ "setTimeoutIntervalForRequest:"
+ "setTimeoutIntervalForResource:"
+ "setValue:forHTTPHeaderField:"
+ "setWithObject:"
+ "setWithObjects:"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE/BatteryAux"
+ "settings-navigation://com.apple.Settings.General/About/MAIN_PARTS_AND_SERVICE/DisplayMain"
+ "settings-navigation://com.apple.Settings.General/Reset"
+ "sharedScheduler"
+ "sharedStore"
+ "shipModeLockMarkerViaTradeIn"
+ "shiplock-eval(%s): cleared Ready to Ship followup"
+ "shiplock-eval(%s): disengage failed: 0x%08x (%@); deferring to next activation/boot"
+ "shiplock-eval(%s): disengaged orphaned ship lock; clearing Ready to Ship followup"
+ "shiplock-eval(%s): failed to clear Ready to Ship followup: %@; deferring for XPC retry"
+ "shiplock-eval(activation-notify): activation record reports in ship mode; adopting"
+ "shiplock-eval(activation-notify): activation record reports not in ship mode; disengaging orphaned lock"
+ "shiplock-eval(activation-notify): activation record unreadable; scheduling network-gated server status check"
+ "shiplock-eval(activation-notify): device factory-activated; disengaging orphaned lock"
+ "shiplock-eval(activation-notify): device not activated; leaving lock untouched"
+ "shiplock-eval(activation-notify): failed to read activation state (%{public}@); continuing with activation record check"
+ "shiplock-eval(daemon-start): device not activated; leaving lock untouched"
+ "shiplock-eval(daemon-start): marker absent but lock engaged; scheduling network-gated server status check"
+ "shiplock-eval(daemon-start): marker present but cannot ship (enabled=%d compliant=%d trusted=%d); clearing Ready to Ship followup and scheduling network-gated device-error report"
+ "shiplock-eval(daemon-start): marker present, battery trusted, lock enabled and compliant; ship mode owns this lock, leaving it engaged"
+ "shiplock-eval(daemon-start): no marker and lock not engaged; nothing to do"
+ "shiplock-eval: activation record DeviceConfigurationFlags=0x%lx inShipMode=%d"
+ "shiplock-eval: failed to post Ready to Ship followup: %{public}@; deferring for XPC retry"
+ "shiplock-eval: failed to read activation record (%@); falling back to server status check"
+ "shiplock-eval: network available; querying server for ship mode status"
+ "shiplock-eval: network available; reporting ship-mode device error to server (marker present, lock disengaged)"
+ "shiplock-eval: operation in flight; skipping device-error report, will re-evaluate next boot"
+ "shiplock-eval: server reports ship mode disabled; disengaging orphaned lock"
+ "shiplock-eval: server reports ship mode enabled; leaving lock engaged"
+ "shiplock-eval: server status query failed: %{public}@; deferring for XPC retry"
+ "shiplock-eval: server status query reply did not arrive within %lus; deferring for XPC retry"
+ "shiplock-eval: ship-mode device error already reported this session; nothing to do"
+ "shiplock-eval: ship-mode device-error report enqueued"
+ "shiplock-eval: ship-mode device-error report failed to enqueue: %{public}@; deferring for XPC retry"
+ "shipmode-%@-%@.log"
+ "shipmode-operation.plist"
+ "sortedArrayUsingComparator:"
+ "sortedArrayUsingSelector:"
+ "status"
+ "statusCode"
+ "stopDischargeWithReply:"
+ "store"
+ "string"
+ "stringByAppendingFormat:"
+ "stringByAppendingPathComponent:"
+ "stringByTrimmingCharactersInSet:"
+ "stringFromDate:"
+ "stringWithCapacity:"
+ "subdataWithRange:"
+ "submitDischargeWithRequestID:notifyServerOnComplete:notifyEnabled:notifyDeviceError:notifyPartnerID:eraseDeviceOnComplete:reply:"
+ "submitNotifyWithRequestID:enabled:deviceError:partnerID:reply:"
+ "submitPersistentBatteryDischargeWithRequestID:notifyServerOnComplete:notifyEnabled:notifyDeviceError:notifyPartnerID:eraseDeviceOnComplete:reply:"
+ "submitPersistentShipModeNotificationWithRequestID:enabled:deviceError:partnerID:reply:"
+ "submitShipModeNotificationWithEnabled:deviceError:partnerID:reply:"
+ "submitWithEnabled:deviceError:partnerID:completion:"
+ "supportsSecureCoding"
+ "sysut"
+ "tcrt-outr"
+ "timeZoneWithAbbreviation:"
+ "timeoutInterval"
+ "uat"
+ "unarchivedObjectOfClass:fromData:error:"
+ "unknown"
+ "unlockCheckCountForBatteryAux"
+ "unlockCheckCountForDisplayMain"
+ "userInfo"
+ "ut"
+ "v12@?0B8"
+ "v20@?0B8@\"NSString\"12"
+ "v20@?0i8@\"NSError\"12"
+ "v20@?0i8^{__CFDictionary=}12"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@\"NSURLSession\"16"
+ "v24@0:8@?<v@?@\"CRShipModeServerResponse\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?BB@\"NSString\"@\"NSString\"@\"NSError\">16"
+ "v24@0:8@?<v@?q@\"NSUUID\"BB@\"NSError\">16"
+ "v24@?0@\"CRShipModeServerResponse\"8@\"NSError\"16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
+ "v28@0:8B16@20"
+ "v28@?0B8@\"NSUUID\"12B20B24"
+ "v32@0:8@\"DDRResetService\"16q24"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v32@0:8@\"NSUUID\"16@?<v@?q@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?qB@\"NSUUID\"@\"NSError\">24"
+ "v32@0:8@16@24"
+ "v32@0:8@16q24"
+ "v32@0:8Q16@?<v@?i@\"NSError\">24"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
+ "v36@0:8B16Q20@?28"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24@?32"
+ "v40@0:8B16B20@\"NSString\"24@?<v@?BB@\"NSString\"@\"NSString\"@\"NSError\">32"
+ "v40@0:8B16B20@24@?32"
+ "v40@?0B8B12@\"NSString\"16@\"NSString\"24@\"NSError\"32"
+ "v48@0:8@\"DDRResetService\"16q24@\"NSError\"32@?<v@?>40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v48@0:8@\"NSUUID\"16B24B28@\"NSString\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24q32@?40"
+ "v48@0:8@16B24B28@32@?40"
+ "v48@0:8@16q24@32@?40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@\"NSUUID\"16B24B28B32@\"NSString\"36B44@?<v@?@\"NSUUID\"@\"NSError\">48"
+ "v56@0:8@16@24@32@40@48"
+ "v56@0:8@16@24@32@40@?48"
+ "v56@0:8@16@24B32B36@40@?48"
+ "v56@0:8@16@24q32q40q48"
+ "v56@0:8@16B24B28B32@36B44@?48"
+ "v56@?0B8B12@\"NSString\"16@\"NSString\"24@\"NSString\"32q40@\"NSError\"48"
+ "v60@0:8@16q24q32@40B48@52"
+ "valueForHTTPHeaderField:"
+ "vcrt-4081"
+ "whitespaceAndNewlineCharacterSet"
+ "writeToFile:atomically:encoding:error:"
+ "writeToURL:options:error:"
+ "x-jmet-serial"
+ "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"
+ "|\n"
+ "…[truncated, %lu bytes total]…\n"
- "!"
```
