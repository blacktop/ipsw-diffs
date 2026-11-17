## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-925.0.4.0.0
-  __TEXT.__text: 0x902c0
-  __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0xbd40
-  __TEXT.__objc_methlist: 0x57ec
-  __TEXT.__cstring: 0x1390b
-  __TEXT.__const: 0x6f8
-  __TEXT.__gcc_except_tab: 0x3484
-  __TEXT.__objc_methname: 0x13c89
-  __TEXT.__oslogstring: 0x113a2
-  __TEXT.__objc_classname: 0x6f2
-  __TEXT.__objc_methtype: 0x2387
+925.0.12.0.0
+  __TEXT.__text: 0x968fc
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_stubs: 0xc4c0
+  __TEXT.__objc_methlist: 0x5b7c
+  __TEXT.__cstring: 0x1598f
+  __TEXT.__const: 0x738
+  __TEXT.__gcc_except_tab: 0x3654
+  __TEXT.__objc_methname: 0x14a4b
+  __TEXT.__oslogstring: 0x1193b
+  __TEXT.__objc_classname: 0x725
+  __TEXT.__objc_methtype: 0x2460
   __TEXT.__dlopen_cstrs: 0xd9
-  __TEXT.__unwind_info: 0x25f8
-  __DATA_CONST.__const: 0x2a00
-  __DATA_CONST.__cfstring: 0x8f40
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__unwind_info: 0x2778
+  __DATA_CONST.__const: 0x2aa8
+  __DATA_CONST.__cfstring: 0x9ca0
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_intobj: 0x690
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_arraydata: 0x1640
-  __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_dictobj: 0xf50
-  __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__objc_arraydata: 0x1918
+  __DATA_CONST.__objc_arrayobj: 0x150
+  __DATA_CONST.__objc_dictobj: 0xfc8
+  __DATA_CONST.__auth_got: 0xb58
+  __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0xa878
-  __DATA.__objc_selrefs: 0x38c0
-  __DATA.__objc_ivar: 0x788
-  __DATA.__objc_data: 0x13b0
+  __DATA.__objc_const: 0xade0
+  __DATA.__objc_selrefs: 0x3ae0
+  __DATA.__objc_ivar: 0x7e4
+  __DATA.__objc_data: 0x1450
   __DATA.__data: 0x740
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3141
-  Symbols:   513
-  CStrings:  6110
+  Functions: 3267
+  Symbols:   518
+  CStrings:  6391
 
Symbols:
+ _OBJC_CLASS_$_OSEligibilityQuery
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_walltime
+ _localtime_r
+ _mktime
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "!1"
+ "%@ could not identify the target app named by the audit token of the indirect object"
+ "%@ indirect object audit token has the wrong size"
+ "%@ reset does not accept an indirect object named by an audit token"
+ "%s OSEligibilityQuery eligible for isEligibleForFullSheetATTAllowed (%{public}@) with eligibility status: %llu"
+ "%s: service %{public}@ has no text indirect object to write, indirectObjectType: %ld"
+ "%{public}@ decides per indirect object, and there is none with an identifier"
+ "%{public}@: target %{public}@ (type %d, %{public}s)"
+ "%{public}s: %{public}@ has no fine grained records"
+ "%{public}s: database error %d for %{public}@"
+ "%{public}s: failed to attribute an identity for %{public}@"
+ "%{public}s: failed to create the request context: %{public}@"
+ "%{public}s: missing or invalid authorization right"
+ "%{public}s: passing nil pointer as struct."
+ "%{public}s: requestor %{public}@ is not entitled to check %{public}@ for accessor %{public}@"
+ "(none)"
+ "-[TCCDMainDatabase copyFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithService:record:list:]_block_invoke"
+ "-[TCCDMainDatabase fineGrainedStatusWithService:subjectIdentity:right:status:]_block_invoke"
+ "-[TCCDMainDatabase fineGrainedStatusWithService:subjectIdentity:right:status:]_block_invoke_2"
+ "-[TCCDMainDatabase fineGrainedTableExists:forService:]_block_invoke"
+ "-[TCCDMainDatabase getFineGrainedAuthResultForSchemaTypeTextIDAndSessionWithContext:result:]_block_invoke"
+ "-[TCCDMainDatabase sessionTimeRecordsForService:rows:]_block_invoke"
+ "-[TCCDMainDatabase setFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithAccessRecord:]"
+ "-[TCCDMainDatabase setFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithAccessRecord:]_block_invoke"
+ "-[TCCDMainDatabase setFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithContext:result:]_block_invoke"
+ "-[TCCDPlatformIOSFamily isEligibleForFullSheetATTAllowedForBundleID:]"
+ "-[TCCDServer evaluateComposedAuthorizationToService:context:andAccessSubject:indirectObject:withRelation:authorizationResult:authorizationReason:subjectCodeIdentityDataResult:]"
+ "-[TCCDServer getFineGrainedStatusWithComposedService:subjectIdentity:right:status:]"
+ "-[TCCDServer handleSessionExpiryForRecord:]_block_invoke"
+ "@\"TCCDSessionTimeConfiguration\""
+ "@48@0:8@16@24@32@40"
+ "@72@0:8{?=[8I]}16@48@56^@64"
+ "@80@0:8@16@24q32@40q48Q56q64q72"
+ "A"
+ "Allowed for session time"
+ "An indirect object named by an audit token is only accepted for an access request"
+ "B32@0:8q16q24"
+ "B40@0:8@16^Q24^Q32"
+ "B80@0:8@16@24@32@40q48^Q56^Q64^@72"
+ "B80@0:8@16B24@28B36^Q40^Q48^i56^@64^B72"
+ "CREATE TABLE IF NOT EXISTS %@ (    service            TEXT        NOT NULL,     category           TEXT        NOT NULL,     category_type      INTEGER     NOT NULL,     client             TEXT        NOT NULL,     client_type        INTEGER     NOT NULL,     auth_value         INTEGER     NOT NULL,     auth_reason        INTEGER     NOT NULL,     indirect_object_identifier TEXT NOT NULL DEFAULT 'UNUSED',     session_expiry     INTEGER,     session_boot_uuid  TEXT,     session_version    INTEGER     NOT NULL DEFAULT 0,     target_csreq       BLOB,     PRIMARY KEY (category, category_type, client, client_type)    FOREIGN KEY (service, client, client_type, indirect_object_identifier) REFERENCES access(service, client, client_type, indirect_object_identifier) ON DELETE CASCADE)"
+ "DO UPDATE SET auth_value=excluded.auth_value, auth_reason=excluded.auth_reason, session_expiry=CASE WHEN excluded.auth_value=auth_value THEN session_expiry ELSE NULL END, session_boot_uuid=CASE WHEN excluded.auth_value=auth_value THEN session_boot_uuid ELSE NULL END, session_version=CASE WHEN excluded.auth_value=auth_value THEN session_version ELSE session_version+1 END, target_csreq=COALESCE(excluded.target_csreq, target_csreq)"
+ "DO UPDATE SET auth_value=excluded.auth_value, auth_reason=excluded.auth_reason, session_expiry=excluded.session_expiry, session_version=session_version+1, target_csreq=COALESCE(excluded.target_csreq, target_csreq)"
+ "DO UPDATE SET target_csreq=excluded.target_csreq"
+ "Error: process.responsiblePath is nil"
+ "INSERT INTO %@ (service, category, category_type, client, client_type, auth_value, auth_reason, indirect_object_identifier, session_expiry, session_version) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, (random() & 0x7FFFFFFFFFFFFFFF)) ON CONFLICT(category, category_type, client, client_type) DO UPDATE SET auth_value=excluded.auth_value, auth_reason=excluded.auth_reason, session_expiry=excluded.session_expiry, session_version=session_version+1 RETURNING session_version"
+ "INSERT INTO %@ (service, category, category_type, client, client_type, auth_value, auth_reason, indirect_object_identifier, session_version, target_csreq, session_expiry) VALUES(?, ?, ?, ?, ?, ?, ?, ?, (random() & 0x7FFFFFFFFFFFFFFF), ?, ?) ON CONFLICT(category, category_type, client, client_type) %@ RETURNING session_version"
+ "NULL"
+ "Posted notification: %s, composed with %{public}@"
+ "SELECT 1 FROM access WHERE service=? AND client=? AND client_type=? LIMIT 1"
+ "SELECT 1 FROM sqlite_schema WHERE type='table' AND name=?"
+ "SELECT auth_value, %@ FROM %@ WHERE client=? AND client_type=?"
+ "SELECT auth_value, auth_reason, session_expiry, session_version, target_csreq FROM %@ WHERE category=? AND category_type=? AND client=? AND client_type=?"
+ "SELECT auth_value, session_expiry, session_version FROM %@ WHERE category=? AND category_type=? AND client=? AND client_type=?"
+ "SELECT category, category_type, client, client_type, auth_value, auth_reason, session_expiry, session_boot_uuid, session_version, target_csreq FROM %@ WHERE service=? AND client=? AND client_type=?"
+ "SELECT category, category_type, client, client_type, session_expiry, session_version, auth_value FROM %@ WHERE auth_value=?"
+ "Service %{public}@ allows Session Time but has no sessionTimeConfig"
+ "Session demotion failed for %{public}@: %d"
+ "Session expiry check failed for %{public}@: %d"
+ "Session sweep failed for %{public}@: %d"
+ "Session time auth expired for client %@"
+ "SetSessionEndTime"
+ "SetSessionEndTime: %{public}@ now %lld seconds after midnight"
+ "SetSessionEndTime: needs a service that allows Session Time and a time of day (service %{public}s, seconds %lld)"
+ "SetSessionTimeDuration"
+ "SetSessionTimeDuration: %{public}@ now %lld seconds"
+ "SetSessionTimeDuration: needs a service that allows Session Time and a positive length (service %{public}s, seconds %lld)"
+ "T@\"NSArray\",C,N,V_lowFrictionEntitlements"
+ "T@\"NSData\",&,N,V_fineGrainedTargetCSReq"
+ "T@\"NSNumber\",&,N,V_fineGrainedSessionVersion"
+ "T@\"NSString\",C,N,V_category"
+ "T@\"NSString\",C,N,V_client"
+ "T@\"TCCDAccessIdentity\",&,V_targetIdentity"
+ "T@\"TCCDSessionTimeConfiguration\",&,N,V_sessionTimeConfig"
+ "TB,N,V_attributesTargetApp"
+ "TB,N,V_composedServiceCodeRequirementMismatch"
+ "TB,N,V_keepMainRowWithEmptyIndirectObjectList"
+ "TB,V_targetIdentityAttributed"
+ "TCCAccessGetFineGrainedStatus"
+ "TCCDSessionTimeConfiguration"
+ "TCCDSessionTimeRecord"
+ "TCCD_MSG_HAS_FINE_GRAINED_RECORD_KEY"
+ "TCCD_MSG_HAS_MAIN_RECORD_KEY"
+ "TCCD_MSG_HAS_RECORD_WITH_RIGHT_KEY"
+ "TCCD_MSG_QUERY_AUTHORIZATION_RIGHT_KEY"
+ "TQ,N,V_defaultExpiredAuth"
+ "Ti,N,V_doUpdateOfTargetVerifierData"
+ "Tq,N,V_categoryType"
+ "Tq,N,V_clientType"
+ "Tq,N,V_fineGrainedSessionExpiry"
+ "Tq,N,V_sessionExpiry"
+ "Tq,N,V_sessionVersion"
+ "_attributesTargetApp"
+ "_category"
+ "_categoryType"
+ "_client"
+ "_composedServiceCodeRequirementMismatch"
+ "_defaultExpiredAuth"
+ "_doUpdateOfTargetVerifierData"
+ "_endsAtTimeOfDay"
+ "_fineGrainedSessionExpiry"
+ "_fineGrainedSessionVersion"
+ "_fineGrainedTargetCSReq"
+ "_keepMainRowWithEmptyIndirectObjectList"
+ "_lowFrictionEntitlements"
+ "_postAuthorizationChangedNotificationOfComposedService:composedWith:"
+ "_postAuthorizationChangedNotificationsForServicesComposedWithService:"
+ "_seconds"
+ "_sessionExpiry"
+ "_sessionTimeConfig"
+ "_sessionTimeQueue"
+ "_sessionVersion"
+ "_targetIdentity"
+ "_targetIdentityAttributed"
+ "accessRecordForDemotedSessionTimeRecord:"
+ "allowed_for_session_time"
+ "answer"
+ "attributed"
+ "attributesTargetApp"
+ "authorization_indirect_object"
+ "category"
+ "categoryType"
+ "com.apple.AMSUIAuthenticationViewService"
+ "com.apple.AMSUIPaymentViewService"
+ "com.apple.AVKit.OutputDeviceMenuService"
+ "com.apple.AVKit.RoutePickerViewService"
+ "com.apple.Arabesque"
+ "com.apple.CMViewSrvc"
+ "com.apple.CharacterPicker.RemoteGenerationViewService"
+ "com.apple.DataDetectorsViewService"
+ "com.apple.Flurry"
+ "com.apple.GameOverlayViewService"
+ "com.apple.GenerativePlaygroundApp.remoteUIExtension"
+ "com.apple.HydraQLPreviewExtension"
+ "com.apple.HydraRenderingService"
+ "com.apple.InstallerRemotePluginService.arm64"
+ "com.apple.InstallerRemotePluginService.x86_64"
+ "com.apple.LinkedNotesUIService"
+ "com.apple.LookupViewService"
+ "com.apple.MADViewServiceExtension"
+ "com.apple.MediaRemoteUIService"
+ "com.apple.Music.VisualizerService"
+ "com.apple.OFDPreview"
+ "com.apple.PaperKit.extension.ui"
+ "com.apple.PressAndHold"
+ "com.apple.PreviewShell"
+ "com.apple.PreviewShellMac"
+ "com.apple.QuickLookUIFramework.QLPreviewGenerationExtension"
+ "com.apple.RAQLPreviewExtension"
+ "com.apple.ReminderKitUI.ReminderCreationViewService"
+ "com.apple.RemotePDEService"
+ "com.apple.RemotePDEServiceARM"
+ "com.apple.Safari.SafariQuickLookPreview"
+ "com.apple.SceneKitQLPreviewExtension"
+ "com.apple.ScreenSaver.Computer-Name"
+ "com.apple.ScreenSaver.Drift"
+ "com.apple.ScreenSaver.Engine.legacyScreenSaver"
+ "com.apple.ScreenSaver.Engine.legacyScreenSaver.x86-64"
+ "com.apple.ScreenSaver.Hello"
+ "com.apple.ScreenSaver.Monterey"
+ "com.apple.ScreenSaver.Ventura"
+ "com.apple.ScreenSaver.iLife-Slideshow-Extension"
+ "com.apple.ScreenTime.ScreenTimeWebExtension"
+ "com.apple.ScreenTimeViewService"
+ "com.apple.Shell"
+ "com.apple.TextInputUI.xpc.CursorUIViewService"
+ "com.apple.Translation.TranslationAPIExtension"
+ "com.apple.Translation.TranslationAPISupportExtension"
+ "com.apple.TranslationUIServices.TranslationUIService"
+ "com.apple.WebKit."
+ "com.apple.WordOfTheDay"
+ "com.apple.WorkflowUI.FocusConfigurationXPCServiceMac"
+ "com.apple.appkit.xpc.LegacyExternalColorPickerService.arm64"
+ "com.apple.appkit.xpc.LegacyExternalColorPickerService.x86_64"
+ "com.apple.appkit.xpc.ThemeWidgetControlViewService"
+ "com.apple.audio.AUHostingService.arm64e"
+ "com.apple.audio.AUHostingService.x86-64"
+ "com.apple.developer.assistive-technology"
+ "com.apple.developer.full-disk-access"
+ "com.apple.freeform.USDRendererExtension"
+ "com.apple.gamecenter.GameCenterUIService"
+ "com.apple.helpviewer.HelpViewer-Quicklook"
+ "com.apple.inputmethod.ChineseHandwriting"
+ "com.apple.inputmethod.EmojiFunctionRowItem"
+ "com.apple.inputmethod.Korean"
+ "com.apple.inputmethod.Kotoeri.KanaTyping"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping"
+ "com.apple.inputmethod.SCIM"
+ "com.apple.inputmethod.TCIM"
+ "com.apple.inputmethod.TYIM"
+ "com.apple.inputmethod.TransliterationIM"
+ "com.apple.inputmethod.VietnameseIM"
+ "com.apple.mail.MailQuickLookExtension"
+ "com.apple.mapkit.private.RemoteUI"
+ "com.apple.osanalytics.IPSExtension"
+ "com.apple.private.tcc.mobileasset.check"
+ "com.apple.quicklook.QuickLookUIService"
+ "com.apple.reminders.quicklookextension"
+ "com.apple.replayKit.RPBroadcastActivityExtension-macOS"
+ "com.apple.replayKit.RPVideoEditorExtension-macOS"
+ "com.apple.screensaver.AlbumArtwork"
+ "com.apple.shortcuts.QuickLookExtension"
+ "com.apple.sidecar.DisplayMarkup"
+ "com.apple.speech.VoiceControlUIService"
+ "com.apple.springboard.SBRendererService"
+ "com.apple.tccd.session-time.expiry"
+ "com.apple.tips.TipsQuicklook"
+ "com.apple.xpc.TypographyPanelService"
+ "composedServiceCodeRequirementMismatch"
+ "configurationEndingAtLocalSecondsOfDay:"
+ "configurationWithDurationSeconds:"
+ "copyFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithService:record:list:"
+ "decomposedStringWithCanonicalMapping"
+ "defaultExpiredAuth"
+ "demoteAllExpiredSessions"
+ "demoteSessionTimeRecord:to:"
+ "demoting all expired sessions"
+ "doUpdateOfTargetVerifierData"
+ "evaluateAccessToService:defaultAccessAllowed:by:checkCodeRequirements:authorizationResult:authorizationReason:flags:subjectCodeIdentityDataResult:subjectRequirementMismatch:"
+ "evaluateComposedAuthorizationToService:context:andAccessSubject:indirectObject:withRelation:authorizationResult:authorizationReason:subjectCodeIdentityDataResult:"
+ "evaluateFineGrainedAccessWithContext:authorizationResult:authorizationReason:"
+ "expiryForSessionSetAt:"
+ "fineGrainedSessionExpiry"
+ "fineGrainedSessionVersion"
+ "fineGrainedStatusWithService:subjectIdentity:right:status:"
+ "fineGrainedTableExists:forService:"
+ "fineGrainedTargetCSReq"
+ "fine_grained_session_boot_uuid"
+ "fine_grained_session_expiry"
+ "fine_grained_session_version"
+ "fine_grained_target_csreq"
+ "getFineGrainedAuthResultForSchemaTypeTextIDAndSessionWithContext:result:"
+ "getFineGrainedStatusWithComposedService:subjectIdentity:right:status:"
+ "handleSessionExpiryForRecord:"
+ "handle_TCCAccessGetFineGrainedStatus"
+ "i32@0:8^B16@24"
+ "i48@0:8@16@24Q32^{?=BBBQ@@}40"
+ "indirect_object_audit_token"
+ "indirect_object_bundle_path"
+ "indirect_object_target_app_attribution_method"
+ "initSessionTimeRecordWithService:category:categoryType:client:clientType:authorizationValue:sessionExpiry:sessionVersion:"
+ "initWithAccessingProcess:requestingProcess:evaluateResponsibility:"
+ "initWithDomain:bundleID:persona:error:"
+ "initWithService:subjectIdentity:indirectObject:attributionChain:"
+ "initWithUnattributedProcess:requestingProcess:"
+ "isEligibleForFullSheetATTAllowedForBundleID:"
+ "isExpired:now:"
+ "kTCCServiceAccessibilityPerTarget"
+ "kTCCServiceListenEventPerTarget"
+ "kTCCServicePostEventPerTarget"
+ "keepMainRowWithEmptyIndirectObjectList"
+ "lowFrictionEntitlements"
+ "main_set_allowed_for_session_time"
+ "not attributed"
+ "notifyUserOfDeniedAccessTo:forService:indirectObject:"
+ "q24@0:8q16"
+ "scheduleSessionExpiryCheckForRecord:"
+ "scheduleSessionExpiryCheckForRecord:afterSeconds:"
+ "sessionExpiry"
+ "sessionTimeConfig"
+ "sessionTimeRecordsForService:rows:"
+ "sessionVersion"
+ "session_expiry"
+ "setAttributesTargetApp:"
+ "setCategory:"
+ "setCategoryType:"
+ "setClient:"
+ "setClientType:"
+ "setComposedServiceCodeRequirementMismatch:"
+ "setDefaultExpiredAuth:"
+ "setDoUpdateOfTargetVerifierData:"
+ "setFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithAccessRecord:"
+ "setFineGrainedAuthRecordForSchemaTypeTextIDAndSessionWithContext:result:"
+ "setFineGrainedSessionExpiry:"
+ "setFineGrainedSessionVersion:"
+ "setFineGrainedTargetCSReq:"
+ "setKeepMainRowWithEmptyIndirectObjectList:"
+ "setLowFrictionEntitlements:"
+ "setSessionExpiry:"
+ "setSessionTimeConfig:"
+ "setSessionTimeConfigForTesting:"
+ "setSessionVersion:"
+ "setTargetIdentity:"
+ "setTargetIdentityAttributed:"
+ "supportsSessionTime"
+ "targetAppForAuditToken:requestingProcess:service:error:"
+ "targetIdentity"
+ "targetIdentityAttributed"
+ "wallClockSeconds"
+ "{os_unfair_recursive_lock_s=\"_os_unfair_recursive_lock_opaque\"[2I]}"
+ "\xf0\xf0\xf0\xf01\xf0\x83"
- "-[TCCDPlatformIOSFamily isEligibleForFullSheetATTAllowed]"
- "-[TCCDServer evaluateComposedAuthorizationToService:andAccessSubject:withRelation:authorizationResult:authorizationReason:subjectCodeIdentityDataResult:]"
- "B64@0:8@16@24q32^Q40^Q48^@56"
- "TB,R,V_isEligibleForFullSheetATTAllowed"
- "_isEligibleForFullSheetATTAllowed"
- "evaluateComposedAuthorizationToService:andAccessSubject:withRelation:authorizationResult:authorizationReason:subjectCodeIdentityDataResult:"
- "isEligibleForFullSheetATTAllowed"
- "notifyUserOfDeniedAccessBy:forService:"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "\xf0\xf0\xf0\xf01\xf0c"
```
