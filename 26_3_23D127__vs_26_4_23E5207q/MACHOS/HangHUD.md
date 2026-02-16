## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x195fc
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x3620
-  __TEXT.__objc_methlist: 0x1c74
-  __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x2cca
-  __TEXT.__objc_classname: 0x2c9
-  __TEXT.__objc_methname: 0x6eef
-  __TEXT.__oslogstring: 0x1ade
-  __TEXT.__objc_methtype: 0xd8a
-  __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__unwind_info: 0x6f0
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x1570
-  __DATA_CONST.__cfstring: 0x3f60
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x58
+397.0.0.0.0
+  __TEXT.__text: 0x27120
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_stubs: 0x4840
+  __TEXT.__objc_methlist: 0x259c
+  __TEXT.__const: 0x458
+  __TEXT.__gcc_except_tab: 0x2f4
+  __TEXT.__objc_methname: 0x8793
+  __TEXT.__cstring: 0x30a9
+  __TEXT.__objc_classname: 0x39c
+  __TEXT.__objc_methtype: 0x13cc
+  __TEXT.__oslogstring: 0x4381
+  __TEXT.__unwind_info: 0xa98
+  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x1828
+  __DATA_CONST.__cfstring: 0x49a0
+  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x138
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x41e8
-  __DATA.__objc_selrefs: 0x14a0
-  __DATA.__objc_ivar: 0x3b0
-  __DATA.__objc_data: 0x820
-  __DATA.__data: 0x450
-  __DATA.__bss: 0x268
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_intobj: 0x168
+  __DATA_CONST.__objc_arraydata: 0x180
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA.__objc_const: 0x51e8
+  __DATA.__objc_selrefs: 0x19d8
+  __DATA.__objc_ivar: 0x4c8
+  __DATA.__objc_data: 0xaa0
+  __DATA.__data: 0x4b0
+  __DATA.__bss: 0x2d8
+  - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
+  - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
+  - /usr/lib/libIOReport.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9CE4370-191F-30D7-BD5C-BB2245E60DD2
-  Functions: 804
-  Symbols:   200
-  CStrings:  2476
+  UUID: FEF8B4A3-C552-346F-9BE2-5723180CF92E
+  Functions: 1203
+  Symbols:   263
+  CStrings:  3149
 
Symbols:
+ _CGBitmapContextCreate
+ _CGBitmapContextCreateImage
+ _CGColorGetConstantColor
+ _CGColorRelease
+ _CGColorSpaceCreateDeviceGray
+ _CGColorSpaceCreateWithName
+ _CGColorSpaceRelease
+ _CGContextClipToMask
+ _CGContextDrawSVGDocument
+ _CGContextFillRect
+ _CGContextRelease
+ _CGContextScaleCTM
+ _CGContextSetFillColorWithColor
+ _CGContextSetGrayFillColor
+ _CGContextTranslateCTM
+ _CGImageRelease
+ _CGSVGDocumentCreateFromURL
+ _CGSVGDocumentGetCanvasSize
+ _CGSVGDocumentRelease
+ _CTFontCreateCopyWithAttributes
+ _CTFontCreateWithName
+ _CTFontGetAscent
+ _CTFontGetCapHeight
+ _CTFontGetDescent
+ _CTFontGetLeading
+ _CTFontGetSize
+ _CTLineCreateWithAttributedString
+ _CTLineGetTypographicBounds
+ _IOReportChannelGetChannelName
+ _IOReportChannelGetGroup
+ _IOReportChannelGetSubGroup
+ _IOReportCopyChannelsInGroup
+ _IOReportCreateSamples
+ _IOReportCreateSamplesDelta
+ _IOReportCreateSubscription
+ _IOReportIterate
+ _IOReportPrune
+ _IOReportStateGetCount
+ _IOReportStateGetIDForIndex
+ _IOReportStateGetResidency
+ _OBJC_CLASS_$_CLPCInternalInterface
+ _OBJC_CLASS_$_CLPCReportingInterpreter
+ _OBJC_CLASS_$_CLPCReportingTranslation
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSMutableAttributedString
+ __os_log_default
+ _clock_gettime_nsec_np
+ _dispatch_source_set_cancel_handler
+ _host_page_size
+ _host_statistics64
+ _kCAAlignmentCenter
+ _kCACornerCurveContinuous
+ _kCATruncationNone
+ _kCGColorBlack
+ _kCGColorSpaceSRGB
+ _kCGColorWhite
+ _kCTBaselineOffsetAttributeName
+ _kCTFontAttributeName
+ _kCTForegroundColorAttributeName
+ _mach_error_string
+ _mach_host_self
+ _notify_cancel
+ _notify_get_state
+ _notify_register_check
+ _objc_autorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x28
+ _vm_page_size
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ " "
+ "  Severity changed from %ld to %ld"
+ "%.*f"
+ "%lu"
+ "-"
+ "3"
+ "<LostPerfEvent: stateName=%@ stateID=0x%llx severity=%ld residencyMs=%llums>"
+ "=== HTSystemConditionsHUDLine init END ==="
+ "=== HTSystemConditionsHUDLine init START ==="
+ "=== createIconLayerForType END ==="
+ "=== createIconLayerForType START: type=%ld ==="
+ "=== layoutColumns END ==="
+ "=== layoutColumns START ==="
+ "=== updateCondition type=%ld END ==="
+ "=== updateCondition type=%ld START ==="
+ "=== updateWithConditionsWithoutTransaction END ==="
+ "=== updateWithConditionsWithoutTransaction START ==="
+ "@\"CLPCReportingInterpreter\""
+ "@\"CLPCReportingInterpreter\"24@0:8^@16"
+ "@\"HTLostPerfMonitor\""
+ "@\"HTPageInsMonitor\""
+ "@\"HTSystemConditionsColors\""
+ "@\"HTSystemConditionsHUDLine\""
+ "@\"LostPerfEvent\""
+ "@\"NSNumber\"16@0:8"
+ "@\"NSObject\"40@0:8@\"NSObject\"16@\"NSObject\"24^@32"
+ "@24@0:8^@16"
+ "@24@0:8^^{__CFDictionary}16"
+ "@24@0:8q16"
+ "@32@0:8@16q24"
+ "@40@0:8@16@24^@32"
+ "@40@0:8@16@24d32"
+ "@40@0:8Q16@24Q32"
+ "@40@0:8q16@24q32"
+ "@48@0:8{?=@qqB}16"
+ "@56@0:8q16@24q32@40q48"
+ "@64@0:8^{CGColor=}16^{CGColor=}24^{CGColor=}32^{CGColor=}40^{CGColor=}48^{CGColor=}56"
+ "@96@0:8^{CGColor=}16^{CGColor=}24^{CGColor=}32^{CGColor=}40^{CGColor=}48^{CGColor=}56^{CGColor=}64^{CGColor=}72^{CGColor=}80@88"
+ "@?40@0:8@16^Q24^Q32"
+ "ADAPTDIS"
+ "ARCHILIM"
+ "ARCHTEMP"
+ "ARCHTRTL"
+ "ARKit"
+ "Attributed string color is NULL. Using fallback white color"
+ "Attributed string display value is nil. Using fallback display value \"%@\""
+ "B24@0:8Q16"
+ "B24@0:8^Q16"
+ "B24@0:8^^{__CFDictionary}16"
+ "B28@0:8B16^@20"
+ "B32@0:8Q16^@24"
+ "B36@0:8Q16B24^@28"
+ "B40@0:8@16@24^B32"
+ "B40@0:8Q16^Q24^@32"
+ "B40@0:8Q16f24i28^@32"
+ "B44@0:8f16Q20Q28^@36"
+ "B48@0:8@16^Q24^@32^Q40"
+ "B48@0:8q16@24@32q40"
+ "BATTEMP"
+ "BLKDSLOT"
+ "BackBoard"
+ "Both system conditions font and system font \"%@\" creation failed. Creating minimal attributed string with color only. System will use default font rendering"
+ "CLKILIM"
+ "CLKTEMP"
+ "CLKTRTL"
+ "CLPC Lost Perf state interpreter in nil, cannot decipher State Identity."
+ "CLPC Lost Perf state interpreter in nil, cannot sample Lost Perf residencies."
+ "CLPC Stats"
+ "CLPCInternalAccess"
+ "CPU reason"
+ "CPUZONE"
+ "CRIT"
+ "CTFontCreateCopyWithAttributes returned NULL at %.1f%% size from main font. Caller will use main font for units display. Units will render at full font size instead of superscript size"
+ "Camera"
+ "Cannot create channel block, CPC interpreter is nil."
+ "Cannot setup IOReporting subscription - no CLPC interpreter available"
+ "Checking for initial column expansions"
+ "Column type %ld: left-aligned text within fixed column (iconX=%.1f, textX=%.1f)"
+ "Column type %ld: text='%@', severity=%ld"
+ "Could not create IOReporting subscription, error: %@"
+ "Could not create Lost Perf samples delta: %@"
+ "Could not get Lost Perf samples: %@"
+ "Could not get baseline Lost Perf samples, error: %@"
+ "Critical"
+ "DRAMTEMP"
+ "EMPTYBAT"
+ "ERROR: Failed to create SVG document"
+ "ERROR: Failed to create SVG document from: %@"
+ "ERROR: Failed to create bitmap context"
+ "ERROR: Failed to create final CGImage"
+ "ERROR: Failed to create mask context"
+ "ERROR: Failed to create mask image"
+ "ERROR: Failed to render SVG to CGImage"
+ "ERROR: Failed to render icon image"
+ "ERROR: No SVG file name for type %ld"
+ "ERROR: No SVG filename for type %ld"
+ "ERROR: SVG file not found in bundle: %@.svg"
+ "ERROR: SVG file not found: %@"
+ "Either the 'CLPCInternalAccess' protocol or 'CLPCInternalInterface' class is not available at runtime, not initializing CLPC client interpreter."
+ "Expanded column type %ld: %.2f -> %.2f (text='%@', prominence=%ld, totalWidth now %.2f)"
+ "FANNOISE"
+ "FASTCHRG"
+ "FASTTEMP"
+ "FDIE_LTS"
+ "Failed to create CLPC client: %@"
+ "Failed to create CLPC reporting interpreter: %@"
+ "Failed to create Lost Perf monitoring timer"
+ "Failed to create page-ins monitoring timer"
+ "Failed to create scaled font at size %.2f, creating retained copy of base font"
+ "Failed to get CLPC Stats channels"
+ "Failed to get thermal pressure level state"
+ "Failed to register for thermal pressure level notification"
+ "Frame width changed from %.2f to %.2f, triggering relayout"
+ "GB/s"
+ "HEATPIPE"
+ "HI"
+ "HIP"
+ "HTLostPerf: Residency conversion overflow for state '%{public}@' (ID: 0x%llx), MATU value %llu would exceed milliseconds_t max. Clamped to UINT64_MAX."
+ "HTLostPerf: Unknown Lost Perf state name '%{public}@' (ID: 0x%llx), defaulting to low severity for consistent light black coloring"
+ "HTLostPerfMonitor"
+ "HTLostPerfMonitor already monitoring"
+ "HTLostPerfMonitor cannot start - CLPC interpreter not available (check CLPC client initialization)"
+ "HTLostPerfMonitor cleaned up existing timer"
+ "HTLostPerfMonitor data maintenance mode active"
+ "HTLostPerfMonitor entering data maintenance mode (sampling every %llums)"
+ "HTLostPerfMonitor not monitoring, ignoring data maintenance mode request"
+ "HTLostPerfMonitor started successfully"
+ "HTLostPerfMonitor starting monitoring (sampling every %llums)"
+ "HTLostPerfMonitor stopped (subscription kept alive for reuse)"
+ "HTLostPerfMonitor stopping monitoring"
+ "HTLostPerfMonitor timer cancellation in progress, deferring start"
+ "HTLostPerfMonitor timer cancelled and cleaned up"
+ "HTLostPerfMonitor: CLPC client created successfully"
+ "HTLostPerfMonitor: CLPC interpreter available, fetching CLPC Stats channels"
+ "HTLostPerfMonitor: CLPC reporting interpreter created successfully"
+ "HTLostPerfMonitor: Cannot sample - no interpreter"
+ "HTLostPerfMonitor: Cannot sample - no subscription"
+ "HTLostPerfMonitor: Cannot start - failed to establish subscription"
+ "HTLostPerfMonitor: Creating monitoring timer"
+ "HTLostPerfMonitor: Delta created successfully"
+ "HTLostPerfMonitor: Extracted state ID 0x%llx name='%@' from state index %d with residency %llu"
+ "HTLostPerfMonitor: Failed to create LostPerfEvent for state ID 0x%llx name='%@'"
+ "HTLostPerfMonitor: Failed to create timer"
+ "HTLostPerfMonitor: Failed to create timer in data maintenance mode"
+ "HTLostPerfMonitor: Failed to decipher channel name: %@"
+ "HTLostPerfMonitor: Failed to decipher state ID 0x%llx: %@"
+ "HTLostPerfMonitor: Failed to decipher subgroup: %@"
+ "HTLostPerfMonitor: Found target channel - subgroup: '%@', channel: '%@'"
+ "HTLostPerfMonitor: Getting baseline samples"
+ "HTLostPerfMonitor: IOReporting subscription cleaned up"
+ "HTLostPerfMonitor: IOReporting subscription created"
+ "HTLostPerfMonitor: IOReporting subscription established successfully"
+ "HTLostPerfMonitor: Initializing CLPC client"
+ "HTLostPerfMonitor: Initializing IOReporting subscription"
+ "HTLostPerfMonitor: Lost Perf active - state: %@ (ID: 0x%llx), severity: %ld, residency: %llums"
+ "HTLostPerfMonitor: Max residency: %llu at index %d"
+ "HTLostPerfMonitor: No Lost Perf active"
+ "HTLostPerfMonitor: No active state found (maxResidencyIndex=%d, maxResidency=%llu)"
+ "HTLostPerfMonitor: Pruning channels using CLPC interpreter"
+ "HTLostPerfMonitor: Pruning complete - kept %lu of %lu channels"
+ "HTLostPerfMonitor: Samples retrieved successfully"
+ "HTLostPerfMonitor: Setting up IOReporting subscription"
+ "HTLostPerfMonitor: Start conditions not met"
+ "HTLostPerfMonitor: Starting IOReportIterate to examine states"
+ "HTLostPerfMonitor: State[%llu] failed to decipher ID 0x%llx: %@"
+ "HTLostPerfMonitor: State[%llu] obfuscatedID=0x%llx (decipher returned nil) residency=%llu"
+ "HTLostPerfMonitor: State[%llu] originalID=%llu name='%@' residency=%llu"
+ "HTLostPerfMonitor: Successfully retrieved CLPC Stats channels"
+ "HTLostPerfMonitor: Timer created and started"
+ "HTPageInsMonitor"
+ "HTPageInsMonitor already monitoring"
+ "HTPageInsMonitor baseline sample: %llu pageins"
+ "HTPageInsMonitor data maintenance mode active"
+ "HTPageInsMonitor entering data maintenance mode (sampling every %llums)"
+ "HTPageInsMonitor found existing timer when starting, cleaning up"
+ "HTPageInsMonitor not monitoring, ignoring data maintenance mode request"
+ "HTPageInsMonitor started successfully"
+ "HTPageInsMonitor starting monitoring (sampling every %llums)"
+ "HTPageInsMonitor stopping monitoring"
+ "HTPageInsMonitor timer cancellation in progress, deferring start"
+ "HTPageInsMonitor timer cancelled and cleaned up"
+ "HTPageInsMonitor: %llu pageins in %llums = %lu MBps (page size: %lu bytes)"
+ "HTSystemConditionInfo"
+ "HTSystemConditionsColors"
+ "HTSystemConditionsHUDLine"
+ "HTSystemConditionsMonitor"
+ "HTSystemConditionsMonitor already monitoring"
+ "HTSystemConditionsMonitor cancelling data maintenance mode"
+ "HTSystemConditionsMonitor data maintenance countdown: %lu seconds remaining"
+ "HTSystemConditionsMonitor data maintenance mode active, countdown: %lu seconds"
+ "HTSystemConditionsMonitor data maintenance update: %lu conditions (seconds remaining: %lu)"
+ "HTSystemConditionsMonitor entering data maintenance mode (will teardown in %llums)"
+ "HTSystemConditionsMonitor entering data maintenance mode state"
+ "HTSystemConditionsMonitor force teardown complete"
+ "HTSystemConditionsMonitor forcing immediate teardown (feature disabled)"
+ "HTSystemConditionsMonitor full teardown complete"
+ "HTSystemConditionsMonitor performing full teardown (data maintenance period expired)"
+ "HTSystemConditionsMonitor resuming from data maintenance mode (had %lu seconds remaining)"
+ "HTSystemConditionsMonitor starting monitoring"
+ "HTSystemConditionsMonitor updated all %lu conditions"
+ "HTSystemConditionsMonitor: Redundancy check detected feature is disabled - forcing teardown"
+ "HTSystemConditionsMonitor: Refusing to start - feature is disabled"
+ "HangTracerEnableSystemConditionsHUD"
+ "Helvetica"
+ "Hiding System Conditions Line because main HUD is clearing"
+ "Hiding system conditions line (line: %s, timer: %s)"
+ "INTELBAT"
+ "Icon SVG: type %ld"
+ "Initial expansion for type %ld: text='%@', totalWidth now %.2f"
+ "LONGCHRG"
+ "LOW"
+ "LOWPOWER"
+ "LTSVCAP"
+ "Lost Perf"
+ "Lost Perf: %@ (severity: %@) - residency: %llums"
+ "Lost Performance"
+ "LostPerfEvent"
+ "LostPerfEvent is nil, unable to find active Lost Perf state, including NONE"
+ "Low"
+ "MB/s"
+ "MED"
+ "Minimum dimensions calculated: %.2f (preserved current: %.2f)"
+ "Minimum dimensions expanded: totalWidth %.2f -> %.2f"
+ "Moderate"
+ "NANDTEMP"
+ "NONE"
+ "NULL output parameter for thermal pressure level"
+ "Neccessary class 'CLPCReportingTranslation' is not available at runtime, cannot sample Lost Perf residencies."
+ "Neccessary classes 'CLPCReportingInterpreter' and 'CLPCReportingTranslation' are not available at runtime, cannot create IOReport channel reference."
+ "No changes for condition type %ld, skipping update"
+ "No column found for condition type %ld"
+ "None"
+ "OK"
+ "OTHER"
+ "PKGZONE"
+ "PMUEM"
+ "PMUTEMP"
+ "PREPCKUP"
+ "PSUTEMP"
+ "Page-in counter decreased (was %llu, now %llu), re-establishing baseline"
+ "Page-ins"
+ "Page-ins: %lu MBps (Below threshold - Gray)"
+ "Page-ins: %lu MBps (Critical - Red)"
+ "Page-ins: %lu MBps (Elevated - Prominent)"
+ "Page-ins: %lu MBps (Warning - Orange)"
+ "Page-ins: Current=%lu MB/s, Average=%lu MB/s (window size: %lu)"
+ "Power Exceptions"
+ "Prominence value %ld is invalid for system condition type %ld. Valid range is %ld (Normal) to %ld (Subdued). Defaulting to HTSystemConditionProminenceNormal"
+ "Q24@0:8^@16"
+ "Q32@0:8Q16Q24"
+ "Q32@0:8Q16^@24"
+ "SDIETEMP"
+ "SKINTEMP"
+ "SLOWTEMP"
+ "SMCPOWER"
+ "SUSTAIN"
+ "SYSZONE"
+ "Searched in bundle: %@"
+ "SecInit"
+ "Security Soft Traps"
+ "Severity value %ld is invalid for system condition type %ld. Valid range is %ld (None) to %ld (Critical). Defaulting to HTSystemConditionSeverityNone"
+ "System Conditions HUD is disabled via preference"
+ "System Conditions HUD is not available on customer devices"
+ "System Conditions HUD preference is disabled - ensuring teardown"
+ "System Conditions Inset Background"
+ "System conditions font is NULL. Attempting system font \"%@\" fallback"
+ "System conditions line already exists"
+ "System conditions line created and added to HUD"
+ "System conditions line expanded from %.2f to %.2f - resizing container in same transaction"
+ "SystemConditionColumn"
+ "SystemConditions"
+ "T@\"CALayer\",&,N,V_iconLayer"
+ "T@\"CALayer\",R,N,V_insetBackgroundLayer"
+ "T@\"CATextLayer\",&,N,V_statusTextLayer"
+ "T@\"HTSystemConditionsColors\",R,N,V_systemConditionsColors"
+ "T@\"HTSystemConditionsHUDLine\",&,N,V_systemConditionsLine"
+ "T@\"NSNumber\",C,N,SsetRPCBufferSize:"
+ "T@\"NSString\",C,N,V_statusValue"
+ "T@\"NSString\",C,N,V_units"
+ "T@\"NSString\",R,C,N,V_displayName"
+ "T@\"NSString\",R,C,N,V_statusText"
+ "T@\"NSString\",R,C,N,V_units"
+ "T@\"NSString\",R,N,V_stateName"
+ "T@\"NSTimer\",&,N,V_systemConditionsUpdateTimer"
+ "TB,N,V_systemConditionsLineVisible"
+ "TB,R,N,GisMonitoring,V_monitoring"
+ "TB,R,V_isSystemConditionsHUDEnabled"
+ "TDDBVCAP"
+ "TQ,R,N,V_residencyMs"
+ "TQ,R,N,V_stateID"
+ "T^{CGColor=},R,N,V_elevatedTextColor"
+ "T^{CGColor=},R,N,V_insetBackgroundColor"
+ "T^{CGColor=},R,N,V_prominentIconColor"
+ "T^{CGColor=},R,N,V_prominentTextColor"
+ "T^{CGColor=},R,N,V_subduedIconColor"
+ "T^{CGColor=},R,N,V_subduedTextColor"
+ "Thermal pressure level state: %llu"
+ "Thermal pressure level: Heavy (HI) (%llu)"
+ "Thermal pressure level: Light (LOW) (%llu)"
+ "Thermal pressure level: Moderate (MED) (%llu)"
+ "Thermal pressure level: Nominal (OK)"
+ "Thermal pressure level: Sleeping (CRIT) (%llu)"
+ "Thermal pressure level: Trapping (CRIT) (%llu)"
+ "Thermals"
+ "Time delta invalid (no time elapsed), skipping sample"
+ "Tq,N,V_prominence"
+ "Tq,N,V_severity"
+ "Tq,N,V_type"
+ "Tq,R,N,V_prominence"
+ "Tq,R,N,V_severity"
+ "Tq,R,N,V_type"
+ "Type %ld: Minimum text='%@', width=%.2f"
+ "Type PageIns: Minimum width=%.2f cached for fontSize=%.2f"
+ "UPO-AV"
+ "URLForResource:withExtension:"
+ "Unknown"
+ "Unknown thermal pressure level: %llu"
+ "Updated bounds to width=%.2f (expanded)"
+ "Updating column type %ld: text='%@', severity=%ld, prominence=%ld"
+ "Updating with %lu conditions"
+ "^{CGColor=}28@0:8q16B24"
+ "^{CGContext=}32@0:8{CGSize=dd}16"
+ "^{CGContext=}40@0:8{CGSize=dd}16^{CGColorSpace=}32"
+ "^{CGImage=}56@0:8^{CGSVGDocument=}16{CGSize=dd}24d40^{CGColor=}48"
+ "^{CGSVGDocument=}24@0:8q16"
+ "^{__CFDictionary=}"
+ "^{__IOReportSubscriptionCF=}"
+ "_cachedPageInsMinFontSize"
+ "_cachedPageInsMinWidth"
+ "_columns"
+ "_currentColumnWidths"
+ "_currentConditions"
+ "_currentEvent"
+ "_currentRateMBps"
+ "_currentSamplingIntervalMS"
+ "_currentTotalWidth"
+ "_dataMaintenanceSecondsRemaining"
+ "_dataMaintenanceTimer"
+ "_displayName"
+ "_elevatedTextColor"
+ "_fontSize"
+ "_hostPort"
+ "_iconLayer"
+ "_inDataMaintenanceMode"
+ "_insetBackgroundColor"
+ "_insetBackgroundLayer"
+ "_interpreter"
+ "_isSystemConditionsHUDEnabled"
+ "_lastLoggedReasonCode"
+ "_lastPageInsCount"
+ "_lastSampleTimeMs"
+ "_lock"
+ "_lostPerfMonitor"
+ "_minimumColumnWidths"
+ "_monitorQueue"
+ "_monitoring"
+ "_monitoringTimer"
+ "_pageInsMonitor"
+ "_pageInsRateHistory"
+ "_pageSize"
+ "_prev_samples"
+ "_prominence"
+ "_prominentIconColor"
+ "_prominentTextColor"
+ "_residencyMs"
+ "_severity"
+ "_stateID"
+ "_stateName"
+ "_statusText"
+ "_statusTextLayer"
+ "_statusValue"
+ "_subbed_channels"
+ "_subduedIconColor"
+ "_subduedTextColor"
+ "_subscription"
+ "_systemConditionsColors"
+ "_systemConditionsLine"
+ "_systemConditionsLineVisible"
+ "_systemConditionsUpdateTimer"
+ "_timerCancelling"
+ "_type"
+ "_units"
+ "activeConditions"
+ "adjustMaxWidthForSystemConditions:"
+ "allowsPowerBudgetsFrom:error:"
+ "allowsPowerBudgetsFromPPM:"
+ "appendAttributedString:"
+ "applyMaskImage:toContext:withColor:size:"
+ "arkit"
+ "backboard"
+ "buildConditionsList"
+ "bundlePath"
+ "calculateActualColumnWidth:"
+ "calculateActualContentWidth"
+ "calculateLayoutMetrics"
+ "calculateMinimumDimensionsWithIconSize:orderedTypes:"
+ "calculatePageInRateMBpsWithDelta:overTime:"
+ "calculatePageInsAverage"
+ "calculateSVGRenderingMetricsForCanvasSize:targetSize:scale:"
+ "calculateSeverityFromStateName:"
+ "camera"
+ "cancelDataMaintenanceMode"
+ "checkLostPerf"
+ "checkPageIns"
+ "checkThermals"
+ "cleanupExistingTimer"
+ "cleanupIOReporting"
+ "colorForSeverity:isIcon:"
+ "com.apple.hangtracer.lostperf"
+ "com.apple.hangtracer.pageins"
+ "com.apple.system.thermalpressurelevel"
+ "configureInsetBackgroundLayerWithTheme:"
+ "createAndConfigureTimer"
+ "createAndShowSystemConditionsLine"
+ "createBitmapContextWithSize:colorSpace:"
+ "createChannelPruneBlockWithInterpreter:totalChannels:keptChannels:"
+ "createClient:"
+ "createColumnForCondition:"
+ "createIOReportingSubscription:"
+ "createIconLayerForType:"
+ "createLostPerfConditionInfo:"
+ "createLostPerfDisplayData:"
+ "createMaskContextWithSize:"
+ "createReportingInterpreter:"
+ "createSampleDelta:"
+ "createThermalConditionInfo:severity:"
+ "currentLostPerfEvent"
+ "currentPageInRateMBps"
+ "d152@0:8Q16d24{?=ddddddddddddddd}32"
+ "d24@0:8@16"
+ "d24@0:8q16"
+ "d32@0:8@16@24"
+ "d40@0:8@16@24q32"
+ "d40@0:8d16d24Q32"
+ "dataMaintenanceTimerTick"
+ "decipherChannelName:error:"
+ "decipherLostPerfStateID:error:"
+ "decipherStateIdentity:stateID:stateName:"
+ "decipherSubGroupName:error:"
+ "determinePageInsSeverity:"
+ "displayName"
+ "elevatedTextColor"
+ "ensureIOReportingSubscription"
+ "enterDataMaintenanceMode"
+ "establishBaselineSamples"
+ "expandColumnIfNeeded:forText:units:prominence:"
+ "expandColumnsForInitialConditions:"
+ "extractActiveStateFromDelta:stateID:stateName:residency:"
+ "findColumnForType:"
+ "forceTeardown"
+ "formatPageInsDisplayValue:statusText:units:"
+ "gauge.with.dots.needle.0percent"
+ "getCurrentTimeMs"
+ "getInitialSystemConditions"
+ "getThermalPressureLevel:"
+ "hideSystemConditionsLine"
+ "host_page_size() returned %s (%d). Using vm_page_size (%u bytes) as fallback"
+ "host_statistics64() returned %s (%d). Skipping this page-in sample, monitoring continues"
+ "i16@?0^{__CFDictionary=}8"
+ "iconLayer"
+ "initInternal"
+ "initPropertySystemConditionsHUDEnabled:"
+ "initWithConditions:theme:fontSize:"
+ "initWithElevatedTextColor:insetBackgroundColor:prominentTextColor:subduedTextColor:prominentIconColor:subduedIconColor:"
+ "initWithPreviousHangTextColor:currentHangTextColor:currentHangSevereTextColor:previousHangSevereTextColor:currentHangCriticalTextColor:previousHangCriticalTextColor:backgroundColor:currentProcessExitTextColor:processExitReasonNamespaceTextColor:systemConditionsColors:"
+ "initWithStateID:stateName:residencyMATU:"
+ "initWithString:attributes:"
+ "initWithType:statusText:severity:"
+ "initWithType:statusText:severity:units:prominence:"
+ "initializeBasicState"
+ "initializeCLPCClient"
+ "initializeSystemConditionsLine:"
+ "insetBackgroundColor"
+ "insetBackgroundLayer"
+ "isMonitoring"
+ "isSystemConditionsHUDEnabled"
+ "lastObject"
+ "layoutColumnAtIndex:xOffset:metrics:"
+ "layoutColumns"
+ "layoutSublayers called - skipping parent implementation to preserve custom layout"
+ "loadSVGDocumentForType:"
+ "mainBundle"
+ "mapLostPerfSeverity:"
+ "mapThermalStateToCondition:"
+ "minimumTextWidthForConditionType:"
+ "monitoring"
+ "nil"
+ "numberWithUnsignedInteger:"
+ "originalID"
+ "originalName"
+ "performFullTeardown"
+ "performRPC:withParams:error:"
+ "positionSystemConditionsLine:maxWidth:numOfHUDLinesToDisplay:"
+ "power exceptions"
+ "prominence"
+ "prominentIconColor"
+ "prominentTextColor"
+ "pruneChannelsForLostPerf"
+ "q24@0:8@16"
+ "q24@0:8Q16"
+ "q24@0:8q16"
+ "queryVMStatistics:"
+ "rectangle.2.swap"
+ "removeObjectAtIndex:"
+ "renderSVGDocument:toMaskContext:withMetrics:"
+ "renderSVGDocument:toSize:scale:fillColor:"
+ "residencyMs"
+ "restartTimerWithInterval:"
+ "rpcBufferSize"
+ "sampleLostPerf"
+ "samplePageIns"
+ "secinit"
+ "security soft traps"
+ "setAllowsPowerBudgetsFrom:allowed:error:"
+ "setAllowsPowerBudgetsFromPPM:error:"
+ "setBounds:"
+ "setCLPCTrialID:error:"
+ "setContents:"
+ "setCornerCurve:"
+ "setIconLayer:"
+ "setPowerBudget:forReason:withTimescale:error:"
+ "setPowerBudget:toValue:withReason:error:"
+ "setProminence:"
+ "setRPCBufferSize:"
+ "setSeverity:"
+ "setStatusTextLayer:"
+ "setStatusValue:"
+ "setSystemConditionsLine:"
+ "setSystemConditionsLineVisible:"
+ "setSystemConditionsUpdateTimer:"
+ "setType:"
+ "setUnits:"
+ "setWithArray:"
+ "setupColumns:"
+ "setupDataMaintenanceTimers"
+ "setupIOReportingSubscription"
+ "severity"
+ "severityToStatesMapping"
+ "shouldShowSystemConditionsLine"
+ "startMonitoring"
+ "startSystemConditionsMonitoring"
+ "stateID"
+ "stateName"
+ "stateNameToSeverityMapping"
+ "statusText"
+ "statusText is nil for type %ld. Using fallback \"-\""
+ "statusTextLayer"
+ "statusValue"
+ "stopMonitoring"
+ "subduedIconColor"
+ "subduedTextColor"
+ "svg"
+ "svgFileNameForType:"
+ "systemConditionsColors"
+ "systemConditionsLine"
+ "systemConditionsLineVisible"
+ "systemConditionsUpdateTimer"
+ "thermometer.variable"
+ "type"
+ "units"
+ "updateColumn:withCondition:textChanged:"
+ "updateCondition:"
+ "updateConditions"
+ "updateConditionsDuringDataMaintenance"
+ "updateCurrentEventWithState:name:residency:found:"
+ "updateIconLayerForColumn:withColor:"
+ "updateSamplingStateWithPageIns:atTime:rate:"
+ "updateSharedConditions:"
+ "updateStatusTextForColumn:statusValue:severity:prominence:"
+ "updateSystemConditionsLine"
+ "updateWithConditions:"
+ "updateWithConditionsWithoutTransaction:"
+ "v24@0:8@\"NSNumber\"16"
+ "v32@0:8@16^{CGColor=}24"
+ "v32@0:8d16@24"
+ "v40@0:8Q16Q24Q32"
+ "v40@0:8Q16^@24^@32"
+ "v44@0:8Q16@24Q32B40"
+ "v48@0:8@16@24q32q40"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "v56@0:8^{CGImage=}16^{CGContext=}24^{CGColor=}32{CGSize=dd}40"
+ "v88@0:8^{CGSVGDocument=}16^{CGContext=}24{?=d{CGSize=dd}dd{CGSize=dd}}32"
+ "validateStartConditions"
+ "verifyEnablementOrTeardown"
+ "widthForAttributedString:"
+ "widthForText:"
+ "widthForTextWithUnits:units:"
+ "widthForTextWithUnits:units:prominence:"
+ "{?=@qqB}24@0:8@16"
+ "{?=ddddddddddddddd}16@0:8"
+ "{?=d{CGSize=dd}dd{CGSize=dd}}56@0:8{CGSize=dd}16{CGSize=dd}32d48"
+ "\x91"
- "@88@0:8^{CGColor=}16^{CGColor=}24^{CGColor=}32^{CGColor=}40^{CGColor=}48^{CGColor=}56^{CGColor=}64^{CGColor=}72^{CGColor=}80"
- "initWithPreviousHangTextColor:currentHangTextColor:currentHangSevereTextColor:previousHangSevereTextColor:currentHangCriticalTextColor:previousHangCriticalTextColor:backgroundColor:currentProcessExitTextColor:processExitReasonNamespaceTextColor:"

```
