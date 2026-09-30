## SpringBoardFoundation

> `/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`

```diff

-4557.0.10.114.0
-  __TEXT.__text: 0xb4ae0
-  __TEXT.__auth_stubs: 0x1940
-  __TEXT.__objc_methlist: 0x802c
-  __TEXT.__const: 0x23a8
-  __TEXT.__cstring: 0xde5b
+4557.1.8.105.0
+  __TEXT.__text: 0xb543c
+  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__objc_methlist: 0x8064
+  __TEXT.__const: 0x2350
+  __TEXT.__cstring: 0xde6c
   __TEXT.__gcc_except_tab: 0x7c8
   __TEXT.__dlopen_cstrs: 0x4d2
-  __TEXT.__oslogstring: 0x2f17
+  __TEXT.__oslogstring: 0x2fc6
   __TEXT.__ustring: 0x2e4
-  __TEXT.__unwind_info: 0x2238
-  __TEXT.__objc_classname: 0x1a10
-  __TEXT.__objc_methname: 0x19969
-  __TEXT.__objc_methtype: 0x335f
-  __TEXT.__objc_stubs: 0xe460
-  __DATA_CONST.__got: 0xc20
-  __DATA_CONST.__const: 0x1940
+  __TEXT.__unwind_info: 0x2290
+  __TEXT.__objc_classname: 0x1a1a
+  __TEXT.__objc_methname: 0x198f5
+  __TEXT.__objc_methtype: 0x33bd
+  __TEXT.__objc_stubs: 0xe400
+  __DATA_CONST.__got: 0xc18
+  __DATA_CONST.__const: 0x1978
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5008
+  __DATA_CONST.__objc_selrefs: 0x4ff0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x508
-  __AUTH_CONST.__auth_got: 0xcb0
+  __AUTH_CONST.__auth_got: 0xd10
   __AUTH_CONST.__const: 0xd20
-  __AUTH_CONST.__cfstring: 0xb480
-  __AUTH_CONST.__objc_const: 0x19ab8
+  __AUTH_CONST.__cfstring: 0xb4a0
+  __AUTH_CONST.__objc_const: 0x19f60
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH.__objc_data: 0x37a0
-  __DATA.__objc_ivar: 0x9dc
+  __DATA.__objc_ivar: 0x9f0
   __DATA.__data: 0x14ca
-  __DATA.__bss: 0x850
+  __DATA.__bss: 0x870
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C032ADE1-A26F-3BB3-A76C-8F5FA1B25995
-  Functions: 3669
-  Symbols:   12680
-  CStrings:  8570
+  UUID: 3CB0B072-3F98-3F12-A654-D1D03806EC91
+  Functions: 3698
+  Symbols:   12762
+  CStrings:  8575
 
Symbols:
+ -[SBFMachNextMinuteDateProvider .cxx_destruct]
+ -[SBFMachNextMinuteDateProvider _nextMinuteDateWithAbsoluteTime:machAbsoluteTimeForNextMinute:]
+ -[SBFMachNextMinuteDateProvider _onMachTimer]
+ -[SBFMachNextMinuteDateProvider _onNotifyClockSet]
+ -[SBFMachNextMinuteDateProvider _setupClockSetNotification]
+ -[SBFMachNextMinuteDateProvider _setupMachTimer]
+ -[SBFMachNextMinuteDateProvider _tearDownClockSetNotification]
+ -[SBFMachNextMinuteDateProvider _tearDownMachTimer]
+ -[SBFMachNextMinuteDateProvider _updateHandlers]
+ -[SBFMachNextMinuteDateProvider _updateTimerEnablement]
+ -[SBFMachNextMinuteDateProvider clockSetNotifyToken]
+ -[SBFMachNextMinuteDateProvider date]
+ -[SBFMachNextMinuteDateProvider dealloc]
+ -[SBFMachNextMinuteDateProvider initWithReferenceView:]
+ -[SBFMachNextMinuteDateProvider machTimer]
+ -[SBFMachNextMinuteDateProvider minuteHandlers]
+ -[SBFMachNextMinuteDateProvider observeMinuteUpdatesWithHandler:]
+ -[SBFMachNextMinuteDateProvider referenceView]
+ -[SBFMachNextMinuteDateProvider removeMinuteUpdateHandler:]
+ -[SBFMachNextMinuteDateProvider setClockSetNotifyToken:]
+ -[SBFMachNextMinuteDateProvider setMachTimer:]
+ -[SBFMachNextMinuteDateProvider setMinuteHandlers:]
+ -[SBFMachNextMinuteDateProvider setReferenceView:]
+ _CFMachPortCreateRunLoopSource
+ _CFMachPortCreateWithPort
+ _CFMachPortInvalidate
+ _CFRunLoopAddSource
+ _CFRunLoopRemoveSource
+ _CFRunLoopSourceInvalidate
+ _HomeScreenMenuBarDefaultValueFunction
+ _OBJC_CLASS_$_SBFMachNextMinuteDateProvider
+ _OBJC_IVAR_$_SBFMachNextMinuteDateProvider._clockSetNotifyToken
+ _OBJC_IVAR_$_SBFMachNextMinuteDateProvider._hasMachTimer
+ _OBJC_IVAR_$_SBFMachNextMinuteDateProvider._machTimer
+ _OBJC_IVAR_$_SBFMachNextMinuteDateProvider._minuteHandlers
+ _OBJC_IVAR_$_SBFMachNextMinuteDateProvider._nextToken
+ _OBJC_IVAR_$_SBFMachNextMinuteDateProvider._referenceView
+ _OBJC_METACLASS_$_SBFMachNextMinuteDateProvider
+ _SBFIsHomeScreenMenuBarAvailable
+ _SBFTestWithHomeScreenMenuBar
+ __OBJC_$_INSTANCE_METHODS_SBFMachNextMinuteDateProvider
+ __OBJC_$_INSTANCE_VARIABLES_SBFMachNextMinuteDateProvider
+ __OBJC_$_PROP_LIST_SBFMachNextMinuteDateProvider
+ __OBJC_CLASS_PROTOCOLS_$_SBFMachNextMinuteDateProvider
+ __OBJC_CLASS_RO_$_SBFMachNextMinuteDateProvider
+ __OBJC_METACLASS_RO_$_SBFMachNextMinuteDateProvider
+ __SBFMachTimerAddToRunLoop
+ __SBFMachTimerArm
+ __SBFMachTimerCancel
+ __SBFMachTimerInit
+ __SBFMachTimerKill
+ __SBFMachTimerRemoveFromRunLoop
+ ___48-[SBFMachNextMinuteDateProvider _updateHandlers]_block_invoke
+ ___59-[SBFMachNextMinuteDateProvider _setupClockSetNotification]_block_invoke
+ ___HomeScreenMenuBarStorage
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ _fmod
+ _kCFAbsoluteTimeIntervalSince1970
+ _machTimerCallback
+ _mach_msg
+ _mk_timer_arm_leeway
+ _mk_timer_cancel
+ _mk_timer_create
+ _mk_timer_destroy
+ _notify_cancel
+ _objc_msgSend$_onMachTimer
+ _objc_msgSend$maximumFramesPerSecond
+ _runloopCallback
- -[SBAnalyticsDefaults _bindAndRegisterDefaults]
- -[SBLocalDefaults analyticsDefaults]
- _IRDCResetDefaultValueFunction
- _MGIsDeviceOneOfType
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_SBAnalyticsDefaults
- _OBJC_IVAR_$_SBLocalDefaults._lazy_analyticsDefaults
- _OBJC_METACLASS_$_SBAnalyticsDefaults
- _SBFIsIRDCResetAvailable
- _SBFTestWithIRDCReset
- __OBJC_$_INSTANCE_METHODS_SBAnalyticsDefaults
- __OBJC_$_PROP_LIST_SBAnalyticsDefaults
- __OBJC_CLASS_RO_$_SBAnalyticsDefaults
- __OBJC_METACLASS_RO_$_SBAnalyticsDefaults
- ___36-[SBLocalDefaults analyticsDefaults]_block_invoke
- ___IRDCResetStorage
- _analyticsDefaults.__once
- _objc_msgSend$emulatedArtworkSubtype
- _objc_msgSend$emulatedDeviceClass
- _objc_msgSend$emulatedDisplayCornerRadius
- _objc_msgSend$emulatedHomeButtonType
- _objc_msgSend$isEmulatedDevice
CStrings:
+ "EmergencyDialer"
+ "Got date for next minute boundary: %{public}@\n now: %lu seconds: %f correction: %f remaining: %lu"
+ "HomeScreenMenuBar"
+ "SBFMachNextMinuteDateProvider"
+ "SBHomeScreenMenuBar"
+ "ShallowInteraction"
+ "_SBFMachTimer callback fired"
+ "_clockSetNotifyToken"
+ "_hasMachTimer"
+ "_machTimer"
+ "_onMachTimer"
+ "_referenceView"
+ "_updateHandlers %@"
+ "com.apple.system.clock_set"
+ "initWithReferenceView:"
+ "maximumFramesPerSecond"
+ "onMachTimer"
+ "onNotifyClockSet"
+ "{_SBFMachTimer=\"machPort\"I\"cfPort\"^{__CFMachPort}\"runloopSource\"^{__CFRunLoopSource}\"callback\"^?\"callbackContext\"^v}"
- "@\"SBAnalyticsDefaults\""
- "SBAnalyticsDefaults"
- "SBAnalyticsEngagementPlistRepresentation"
- "SBIRDCReset"
- "T@\"NSDictionary\",C,D,N"
- "T@\"SBAnalyticsDefaults\",R,&,N"
- "_lazy_analyticsDefaults"
- "analyticsDefaults"
- "emulatedArtworkSubtype"
- "emulatedDeviceClass"
- "emulatedDisplayCornerRadius"
- "emulatedHomeButtonType"
- "engagementPlistRepresentation"
- "isEmulatedDevice"

```
