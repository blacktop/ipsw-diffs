## LockedContentServices

> `/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`

```diff

-58.2.5.0.0
-  __TEXT.__text: 0x95ec
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x70c
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x22c
+58.2.6.0.0
+  __TEXT.__text: 0xc264
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x980
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x2e8
   __TEXT.__oslogstring: 0xcb9
-  __TEXT.__cstring: 0x6e3
-  __TEXT.__unwind_info: 0x2e0
-  __TEXT.__objc_classname: 0x234
-  __TEXT.__objc_methname: 0x226f
-  __TEXT.__objc_methtype: 0x680
-  __TEXT.__objc_stubs: 0x1b00
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x368
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x78
+  __TEXT.__cstring: 0x949
+  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__objc_classname: 0x321
+  __TEXT.__objc_methname: 0x2896
+  __TEXT.__objc_methtype: 0x7e7
+  __TEXT.__objc_stubs: 0x2000
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x4d0
+  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x830
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x620
-  __AUTH_CONST.__objc_const: 0x29c0
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0x28
+  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0x3360
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0xf0
+  __DATA.__data: 0x6c0
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 240
-  Symbols:   408
-  CStrings:  598
+  Functions: 309
+  Symbols:   506
+  CStrings:  700
 
Symbols:
+ _OBJC_CLASS_$_BSHashBuilder
+ _OBJC_CLASS_$_LCSCaptureApplicationAttributes
+ _OBJC_CLASS_$_LCSCaptureApplicationTCCMonitor
+ _OBJC_CLASS_$_LCSCaptureApplicationTCCUpdate
+ _OBJC_CLASS_$__LCSCaptureApplicationTCCObservationToken
+ _OBJC_METACLASS_$_LCSCaptureApplicationAttributes
+ _OBJC_METACLASS_$_LCSCaptureApplicationTCCMonitor
+ _OBJC_METACLASS_$_LCSCaptureApplicationTCCUpdate
+ _OBJC_METACLASS_$__LCSCaptureApplicationTCCObservationToken
+ _kTCCServiceCamera
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_storeWeak
+ _tcc_authorization_record_get_authorization_right
+ _tcc_authorization_record_get_subject_identity
+ _tcc_events_filter_create_with_criteria
+ _tcc_events_subscribe
+ _tcc_events_unsubscribe
+ _tcc_identity_get_identifier
+ _tcc_identity_get_type
+ _tcc_message_options_create
+ _tcc_message_options_set_reply_handler_policy
+ _tcc_message_options_set_request_prompt_policy
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_service_singleton_for_CF_name
+ _xpc_array_create
+ _xpc_array_set_string
+ _xpc_dictionary_create
CStrings:
+ "\x05"
+ "\b"
+ "\x11"
+ "\x17"
+ "@\"<LCSCaptureApplicationTCCObservationToken>\""
+ "@\"<LCSCaptureApplicationTCCObserver>\""
+ "@\"BSDescriptionBuilder\"16@0:8"
+ "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
+ "@\"LCSCaptureApplicationAttributes\""
+ "@\"LCSCaptureApplicationAttributes\"16@0:8"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@32@0:8@16Q24"
+ "B16@?0@\"LCSCaptureApplicationTCCUpdate\"8"
+ "B16@?0@\"NSString\"8"
+ "B16@?0@\"_LCSCaptureApplicationTCCObservationToken\"8"
+ "BSDescriptionProviding"
+ "LCSCaptureApplicationAttributes"
+ "LCSCaptureApplicationTCCMonitor"
+ "LCSCaptureApplicationTCCObservationToken"
+ "LCSCaptureApplicationTCCObserver"
+ "LCSCaptureApplicationTCCUpdate"
+ "Q24@0:8@16"
+ "T@\"<LCSCaptureApplicationTCCObserver>\",W,N,V_observer"
+ "T@\"LCSCaptureApplicationAttributes\",R,N"
+ "T@\"LCSCaptureApplicationAttributes\",R,N,V_attributes"
+ "T@\"LCSCaptureApplicationTCCMonitor\",R,N"
+ "T@\"NSSet\",&,N,V_bundleIdentifiers"
+ "T@\"NSString\",R,C,N,V_bundleIdentifier"
+ "TCCServer"
+ "TQ,R,N,V_cameraTCCStatus"
+ "TQ,R,N,V_tccStatus"
+ "_LCSCaptureApplicationTCCObservationToken"
+ "_attributes"
+ "_beginObservingTCC"
+ "_bundleHasCameraEntitlement:"
+ "_bundleIdentifiers"
+ "_cameraTCCStatus"
+ "_captureApplicationsFromKnownExtensions:currentCaptureApplications:"
+ "_endObservingTCC"
+ "_fetchCameraTCCUpdatesForBundleIdentifiers:"
+ "_lock_evaluateCaptureApplicationRequirementsForKnownExtensions:"
+ "_lock_updateKnownCaptureApplications:"
+ "_notifyObserversOfUpdates:"
+ "_observer"
+ "_observerQueue"
+ "_observerQueue_fetchInitialTCCStateForUpdatedBundleIdentifiers"
+ "_observerQueue_notifyObserversOfUpdates:"
+ "_observerQueue_observerTokens"
+ "_removeObserver:"
+ "_setupQueue_setupTCCEventsSubscription"
+ "_stringForTCCStatus:"
+ "_tccObservationToken"
+ "_tccSetupQueue"
+ "_tccStatus"
+ "_tccUpdateForAuthorizationRecord:"
+ "_tccUpdatesAccessQueue"
+ "_tccUpdatesAccessQueue_handleTCCEventOfType:authorizationRecord:"
+ "_tccUpdatesAccessQueue_latestTCCUpdatesByBundleIdentifier"
+ "_updateTCCMonitorForBundleIdentifiers:"
+ "addObjectsFromArray:"
+ "addObserver:forBundleIdentifiers:"
+ "allKeys"
+ "allowed"
+ "appendObject:withName:"
+ "appendUnsignedInteger:"
+ "attributes"
+ "bs_filter:"
+ "bundleIdentifiers"
+ "cameraTCCStatus"
+ "cameraTCCStatusForBundleIdentifier:"
+ "changeType"
+ "com.apple.LockedContentServices.TCCMonitor"
+ "com.apple.LockedContentServices.tccMonitor.server"
+ "com.apple.LockedContentServices.tccmonitor.observers"
+ "com.apple.LockedContentServices.tccmonitor.setup"
+ "com.apple.LockedContentServices.tccmonitor.updates"
+ "com.apple.private.tcc.allow"
+ "denied"
+ "differenceFromArray:"
+ "hasCachedLinkAction"
+ "hasChanges"
+ "initWithBundleIdentifier:status:"
+ "initWithCameraTCCStatus:"
+ "initWithExtensionInfo:attributes:"
+ "invalid"
+ "isEqualToAttributes:"
+ "isEqualToSet:"
+ "limited"
+ "mutableCopy"
+ "object"
+ "observer"
+ "set"
+ "setBundleIdentifiers:"
+ "setObserver:"
+ "sharedMonitor"
+ "stringWithCString:encoding:"
+ "tccMonitor:didUpdateCameraTCCStatuses:"
+ "tccStatus"
+ "unknown"
+ "unresolved"
+ "v24@?0@\"NSObject<OS_tcc_authorization_record>\"8^{__CFError=}16"
+ "v24@?0Q8@\"NSObject<OS_tcc_authorization_record>\"16"
+ "v32@0:8@\"LCSCaptureApplicationTCCMonitor\"16@\"NSArray\"24"
+ "v32@0:8Q16@24"
- "\x04\x12"
- "\a"
- "_captureApplicationsFromKnownExtensions:"
- "_evaluateCaptureApplicationRequirementsForKnownExtensions:"
- "initWithExtensionInfo:"

```
