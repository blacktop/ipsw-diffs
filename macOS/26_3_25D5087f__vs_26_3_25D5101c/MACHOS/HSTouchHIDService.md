## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/Contents/MacOS/HSTouchHIDService`

```diff

-9430.1.0.0.0
-  __TEXT.__text: 0xc94d8
+9430.3.0.0.0
+  __TEXT.__text: 0xca254
   __TEXT.__auth_stubs: 0x1710
-  __TEXT.__objc_stubs: 0x63e0
+  __TEXT.__objc_stubs: 0x6740
   __TEXT.__init_offsets: 0x11f0
-  __TEXT.__objc_methlist: 0x4a38
+  __TEXT.__objc_methlist: 0x4ba0
   __TEXT.__const: 0x3e4e
-  __TEXT.__gcc_except_tab: 0xd438
-  __TEXT.__cstring: 0xb0f7
-  __TEXT.__oslogstring: 0x35e8
-  __TEXT.__objc_methname: 0x6feb
-  __TEXT.__objc_classname: 0xb7b
-  __TEXT.__objc_methtype: 0x52dd
-  __TEXT.__unwind_info: 0x4260
+  __TEXT.__gcc_except_tab: 0xd540
+  __TEXT.__cstring: 0xb2d7
+  __TEXT.__oslogstring: 0x3730
+  __TEXT.__objc_methname: 0x7597
+  __TEXT.__objc_classname: 0xb9a
+  __TEXT.__objc_methtype: 0x5372
+  __TEXT.__unwind_info: 0x42b0
   __DATA_CONST.__auth_got: 0xb98
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x1c10
-  __DATA_CONST.__cfstring: 0x6b20
-  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__cfstring: 0x6c60
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_intobj: 0x600
   __DATA_CONST.__objc_doubleobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x588
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x258
-  __DATA.__objc_const: 0x8b98
-  __DATA.__objc_selrefs: 0x1dd0
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__objc_data: 0x23a0
+  __DATA.__objc_const: 0x8e18
+  __DATA.__objc_selrefs: 0x1ea0
+  __DATA.__objc_ivar: 0x60c
+  __DATA.__objc_data: 0x23f0
   __DATA.__data: 0x14d0
   __DATA.__bss: 0xc0
   __DATA.__common: 0x890

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73336685-A212-3FC3-9423-C7EF06BA267B
-  Functions: 4680
-  Symbols:   30102
-  CStrings:  4470
+  UUID: 474C09C3-7BE6-363A-B221-03C491247FB0
+  Functions: 4709
+  Symbols:   30306
+  CStrings:  4550
 
Symbols:
+ -[MTTrackpadUberAlg algButtonStateManager]
+ -[MTTrackpadUberAlg cacheAndUpdateDeviceButtonState:currentDeviceTimestampSec:isTouching:]
+ -[MTTrackpadUberAlg canDelayClicks]
+ -[MTTrackpadUberAlg setAlgButtonStateManager:]
+ -[MTTrackpadUberAlg updateClickDelayState:]
+ -[TrackpadAlgButtonStateManager cacheDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:isTouching:]
+ -[TrackpadAlgButtonStateManager cachedDeviceButtonState]
+ -[TrackpadAlgButtonStateManager clearState]
+ -[TrackpadAlgButtonStateManager currentlyDelayingClick]
+ -[TrackpadAlgButtonStateManager debug]
+ -[TrackpadAlgButtonStateManager delayDownClick:until:]
+ -[TrackpadAlgButtonStateManager delayedButtonState]
+ -[TrackpadAlgButtonStateManager delayedDownClickIsQueued]
+ -[TrackpadAlgButtonStateManager delayedDownClickTimestampSec]
+ -[TrackpadAlgButtonStateManager downClickDelaySec]
+ -[TrackpadAlgButtonStateManager fwDeviceButtonState]
+ -[TrackpadAlgButtonStateManager handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:]
+ -[TrackpadAlgButtonStateManager init]
+ -[TrackpadAlgButtonStateManager newClickBlockedDueToExistingDelay]
+ -[TrackpadAlgButtonStateManager setCachedDeviceButtonState:]
+ -[TrackpadAlgButtonStateManager setCurrentlyDelayingClick:]
+ -[TrackpadAlgButtonStateManager setDelayedButtonState:]
+ -[TrackpadAlgButtonStateManager setDelayedDownClickTimestampSec:]
+ -[TrackpadAlgButtonStateManager setFwDeviceButtonState:]
+ -[TrackpadAlgButtonStateManager setNewClickBlockedDueToExistingDelay:]
+ -[TrackpadAlgButtonStateManager setUpClickOccuredDuringDelay:]
+ -[TrackpadAlgButtonStateManager upClickOccuredDuringDelay]
+ -[TrackpadAlgButtonStateManager updateCachedButtonState:currentDeviceTimestampSec:isTouching:]
+ -[TrackpadAlgButtonStateManager updateFwButtonStateTo:]
+ /AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/
+ /AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSMachPortListener.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSObserverStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPUtil.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPlaybackStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPreferenceStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage+Remote.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject+Additions.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServerStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServiceDirectory.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSSocketListener.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage+Util.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStageProxy.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSCoder.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSSocket.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSTime.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(Contact.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTBackboardBridge.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCREventGenerator.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCircularBuffer.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTContactStabilizer.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCoreAnalytics.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTEvent.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame+Python.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrameParser.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventGenerator.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventStatistics.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEvents.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPencilVirtualService.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPipeline_vers.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTRecordingManager.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTSensingAlgs.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTServerStage.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTTipOffsetFilter.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(Types.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTActionEvent_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCyclingTrackpad_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCycling_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordGestureSet_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordIntegrating_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordTable_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerEllipseTip_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerToPathMap_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceBehavior_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceConfig.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceFilter_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceManagement_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceThresholding_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTGestureConfig_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHIDEventAppend.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandMotion_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandStatistics_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPListGestureConfig_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParameterFactory_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParserPath_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPathStates_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTRestZoneIntegrator_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSlideGesture_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSurfaceDimensions_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTapDragManager_.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTrackpadUberAlg.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(TrackpadAlgButtonStateManager.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(USBKey.o)
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTPipeline.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationManager.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationMultipliers.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationTone.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationWaveform.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorLimits.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/CoreAccessoryManager.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/DeviceInfoManager.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadFirmwareManager.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadHIDEventProcessor.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/FirmwareUtil.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSMousePipelineCreation.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTFirmwareManager.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTHelpers.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTPipelineCreation.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTSAPipelineCreation.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService_vers.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadDefs.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadPipelineCreation.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTGestureConfigGenerator.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPluginLogging.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPreferences.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacOSTrackpadHIDEventProcessor.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacTrackpadBridge.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MomentumCurve.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MouseBridge.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PeppyHIDService.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerBridge.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerHIDEventProcessor.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerSettings.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadActuatorStage.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadAlgStage.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadBridge.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadFirmwareManager.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadHIDEventProcessor.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadMomentumGeneratorStage.o
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Helpers/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/TrackpadActuatorStage/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/Managers/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/FirmwareManagers/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/Plugin/
+ /AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/Plugin/Parser/
+ GCC_except_table194
+ GCC_except_table206
+ GCC_except_table218
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table250
+ OBJC_IVAR_$_MTTrackpadUberAlg._algButtonStateManager
+ OBJC_IVAR_$_MTTrackpadUberAlg._shouldDelayClick
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._cachedDeviceButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._currentlyDelayingClick
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._delayedButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._delayedDownClickTimestampSec
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._downClickDelaySec
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._fwDeviceButtonState
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._newClickBlockedDueToExistingDelay
+ OBJC_IVAR_$_TrackpadAlgButtonStateManager._upClickOccuredDuringDelay
+ TrackpadAlgButtonStateManager.mm
+ _OBJC_CLASS_$_TrackpadAlgButtonStateManager
+ _OBJC_METACLASS_$_TrackpadAlgButtonStateManager
+ __OBJC_$_INSTANCE_METHODS_TrackpadAlgButtonStateManager
+ __OBJC_$_INSTANCE_VARIABLES_TrackpadAlgButtonStateManager
+ __OBJC_$_PROP_LIST_TrackpadAlgButtonStateManager
+ __OBJC_CLASS_RO_$_TrackpadAlgButtonStateManager
+ __OBJC_METACLASS_RO_$_TrackpadAlgButtonStateManager
+ _objc_msgSend$algButtonStateManager
+ _objc_msgSend$cacheAndUpdateDeviceButtonState:currentDeviceTimestampSec:isTouching:
+ _objc_msgSend$cacheDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:isTouching:
+ _objc_msgSend$cachedDeviceButtonState
+ _objc_msgSend$canDelayClicks
+ _objc_msgSend$currentlyDelayingClick
+ _objc_msgSend$delayDownClick:until:
+ _objc_msgSend$delayedButtonState
+ _objc_msgSend$delayedDownClickIsQueued
+ _objc_msgSend$delayedDownClickTimestampSec
+ _objc_msgSend$downClickDelaySec
+ _objc_msgSend$fwDeviceButtonState
+ _objc_msgSend$handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:
+ _objc_msgSend$isTouching
+ _objc_msgSend$newClickBlockedDueToExistingDelay
+ _objc_msgSend$setAlgButtonStateManager:
+ _objc_msgSend$setCachedDeviceButtonState:
+ _objc_msgSend$setCurrentlyDelayingClick:
+ _objc_msgSend$setDelayedButtonState:
+ _objc_msgSend$setDelayedDownClickTimestampSec:
+ _objc_msgSend$setFwDeviceButtonState:
+ _objc_msgSend$setNewClickBlockedDueToExistingDelay:
+ _objc_msgSend$setUpClickOccuredDuringDelay:
+ _objc_msgSend$upClickOccuredDuringDelay
+ _objc_msgSend$updateCachedButtonState:currentDeviceTimestampSec:isTouching:
+ _objc_msgSend$updateClickDelayState:
+ _objc_msgSend$updateFwButtonStateTo:
- /AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/
- /AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSMachPortListener.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSObserverStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPUtil.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPlaybackStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSPreferenceStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage+Remote.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingPlaybackStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRecordingStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject+Additions.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSRemoteObject.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServerStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSServiceDirectory.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSSocketListener.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage+Util.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingPipeline.a(HSStageProxy.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSCoder.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSSocket.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX26.3.Internal.sdk/usr/local/lib/libHIDSensingUtil.a(HSTime.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(Contact.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTBackboardBridge.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCREventGenerator.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCircularBuffer.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTContactStabilizer.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTCoreAnalytics.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTEvent.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame+Python.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrame.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTFrameParser.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventGenerator.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEventStatistics.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTHIDEvents.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPencilVirtualService.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTPipeline_vers.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTRecordingManager.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTSensingAlgs.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTServerStage.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(HSTTipOffsetFilter.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libHSTPipeline.a(Types.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTActionEvent_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCyclingTrackpad_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordCycling_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordGestureSet_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordIntegrating_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTChordTable_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerEllipseTip_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTFingerToPathMap_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceBehavior_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceConfig.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceFilter_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceManagement_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTForceThresholding_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTGestureConfig_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHIDEventAppend.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandMotion_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTHandStatistics_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPListGestureConfig_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParameterFactory_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTParserPath_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTPathStates_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTRestZoneIntegrator_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSlideGesture_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTSurfaceDimensions_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTapDragManager_.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(MTTrackpadUberAlg.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/Symbols/BuiltProducts/libTrackpadHostAlg.a(USBKey.o)
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTPipeline.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationManager.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationMultipliers.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationTone.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuationWaveform.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/ActuatorLimits.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/CoreAccessoryManager.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/DeviceInfoManager.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadFirmwareManager.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/EmbeddedTrackpadHIDEventProcessor.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/FirmwareUtil.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSMousePipelineCreation.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTFirmwareManager.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTHelpers.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTPipelineCreation.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTSAPipelineCreation.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTouchHIDService_vers.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadDefs.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/HSTrackpadPipelineCreation.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTGestureConfigGenerator.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPluginLogging.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MTPreferences.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacOSTrackpadHIDEventProcessor.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MacTrackpadBridge.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MomentumCurve.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/MouseBridge.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PeppyHIDService.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerBridge.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerHIDEventProcessor.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/PointerSettings.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadActuatorStage.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadAlgStage.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadBridge.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadFirmwareManager.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadHIDEventProcessor.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Binaries/Multitouch_executables/install/TempContent/Objects/MultitouchSoftware.build/HSTouchHIDService.build/Objects-normal/arm64e/TrackpadMomentumGeneratorStage.o
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Helpers/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/TrackpadActuatorStage/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/Managers/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/FirmwareManagers/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/Plugin/
- /AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/Plugin/Parser/
- GCC_except_table186
- GCC_except_table187
- GCC_except_table204
- GCC_except_table210
- GCC_except_table216
- GCC_except_table236
- GCC_except_table237
- GCC_except_table238
- GCC_except_table239
- GCC_except_table240
- GCC_except_table241
- GCC_except_table242
CStrings:
+ "-[TrackpadAlgButtonStateManager handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:]"
+ "-[TrackpadAlgButtonStateManager updateCachedButtonState:currentDeviceTimestampSec:isTouching:]"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSMachPortListener.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPlaybackStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPreferenceStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingPlaybackStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingTypes.h"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject+Additions.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServerStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServiceDirectory.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSSocketListener.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStage+Util.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStageProxy.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/HSIOUtil.h"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/HSPortRight.h"
+ "/AppleInternal/Library/BuildRoots/4~CGH5ugBpeHHqs2FwbVx7M7jFyIQMy7f2QoCfdDw/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/HSSocket.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Contact.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTBackboardBridge.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTContactStabilizer.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTEvent.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTFrame.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTFrameParser.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTHIDEventGenerator.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTHIDEvents.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTRecordingManager.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTSensingAlgs.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTServerStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTTipOffsetFilter.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Helpers/HSTHelpers.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Types.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSMousePipelineCreation.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTFirmwareManager.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTPipelineCreation.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTSAPipelineCreation.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTouchHIDService.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTrackpadPipelineCreation.m"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/MTTrackpadUberAlg.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/MTForceManagement_.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTChordCycling_.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTGestureConfig_.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTHandStatistics_.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTPathStates_.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTSurfaceDimensions_.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/TrackpadAlgStage.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/HSTrackpadDefs.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/EmbeddedTrackpadHIDEventProcessor.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/PointerHIDEventProcessor.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/PointerBridge.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/TrackpadBridge.mm"
+ "/AppleInternal/Library/BuildRoots/4~CGH8ugDNVWsZ2vIG7__c-yThBAbGP5_H_1Zq2rg/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/PointerSettings.mm"
+ "9430.3"
+ "@\"TrackpadAlgButtonStateManager\""
+ "AlgButtonStateManager"
+ "C20@0:8I16"
+ "CachedDeviceButtonState"
+ "CurrentlyDelayingClick"
+ "DelayedButtonState"
+ "DelayedDownClickTimestampSec"
+ "DownClickDelaySec"
+ "FirmwareDeviceButtonState"
+ "I32@0:8I16d20B28"
+ "I40@0:8I16B20B24d28B36"
+ "NewClickBlockedDueToExistingDelay"
+ "ShouldDelayClick"
+ "T@\"TrackpadAlgButtonStateManager\",&,N,V_algButtonStateManager"
+ "TB,N,V_currentlyDelayingClick"
+ "TB,N,V_newClickBlockedDueToExistingDelay"
+ "TB,N,V_upClickOccuredDuringDelay"
+ "TI,N,V_cachedDeviceButtonState"
+ "TI,N,V_delayedButtonState"
+ "TI,N,V_fwDeviceButtonState"
+ "Td,N,V_delayedDownClickTimestampSec"
+ "Td,R,N,V_downClickDelaySec"
+ "TrackpadAlgButtonStateManager"
+ "UpClickOccuredDuringDelay"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Dispatching queued downclick (button mask = %d)"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Dispatching queued upclick (button mask = %d)"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Queued downclick (button mask = %d) until %.3f sec"
+ "[HID] [MT] %s%s%s [ClickDelay] %.3f sec : Queued upclick"
+ "_algButtonStateManager"
+ "_cachedDeviceButtonState"
+ "_currentlyDelayingClick"
+ "_delayedButtonState"
+ "_delayedDownClickTimestampSec"
+ "_downClickDelaySec"
+ "_fwDeviceButtonState"
+ "_newClickBlockedDueToExistingDelay"
+ "_shouldDelayClick"
+ "_upClickOccuredDuringDelay"
+ "algButtonStateManager"
+ "cacheAndUpdateDeviceButtonState:currentDeviceTimestampSec:isTouching:"
+ "cacheDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:isTouching:"
+ "cachedDeviceButtonState"
+ "canDelayClicks"
+ "currentlyDelayingClick"
+ "delayDownClick:until:"
+ "delayedButtonState"
+ "delayedDownClickIsQueued"
+ "delayedDownClickTimestampSec"
+ "downClickDelaySec"
+ "fwDeviceButtonState"
+ "handleButtonStateChange:currentDeviceButtonState:shouldDelayClick:shouldSecondaryClick:currentDeviceTimestampSec:"
+ "newClickBlockedDueToExistingDelay"
+ "setAlgButtonStateManager:"
+ "setCachedDeviceButtonState:"
+ "setCurrentlyDelayingClick:"
+ "setDelayedButtonState:"
+ "setDelayedDownClickTimestampSec:"
+ "setFwDeviceButtonState:"
+ "setNewClickBlockedDueToExistingDelay:"
+ "setUpClickOccuredDuringDelay:"
+ "upClickOccuredDuringDelay"
+ "updateCachedButtonState:currentDeviceTimestampSec:isTouching:"
+ "updateClickDelayState:"
+ "updateFwButtonStateTo:"
+ "v24@0:8d16"
+ "v28@0:8I16d20"
+ "v32@0:8I16d20B28"
+ "v40@0:8C16I20B24B28d32"
+ "\xf0\xd11"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSMachPortListener.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPlaybackStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSPreferenceStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingPlaybackStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRecordingTypes.h"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject+Additions.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSRemoteObject.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServerStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSServiceDirectory.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSSocketListener.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStage+Util.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingPipeline/HSStageProxy.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/HSIOUtil.h"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/HSPortRight.h"
- "/AppleInternal/Library/BuildRoots/4~CEJTugAxzp6Y9c5gPNz_uLaVl992kA-RMLipDjk/Library/Caches/com.apple.xbs/Sources/HIDSensingPipeline/HIDSensingUtil/HSSocket.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Contact.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTBackboardBridge.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTContactStabilizer.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTEvent.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTFrame.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTFrameParser.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTHIDEventGenerator.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTHIDEvents.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTRecordingManager.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTSensingAlgs.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTServerStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/HSTTipOffsetFilter.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Helpers/HSTHelpers.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTPipeline/Types.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSMousePipelineCreation.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTFirmwareManager.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTPipelineCreation.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTSAPipelineCreation.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTouchHIDService.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/HIDSensingTouch/HSTouchHIDService/HSTrackpadPipelineCreation.m"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/MTTrackpadUberAlg.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Force/MTForceManagement_.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTChordCycling_.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/Gestures/MTGestureConfig_.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTHandStatistics_.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTPathStates_.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/Parser/PathsNHands/MTSurfaceDimensions_.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/Alg/TrackpadAlgStage.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/HSTrackpadDefs.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/EmbeddedTrackpadHIDEventProcessor.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PostAlg/EventProcessors/PointerHIDEventProcessor.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/PointerBridge.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/Bridges/TrackpadBridge.mm"
- "/AppleInternal/Library/BuildRoots/4~CEJVugDgUakgSc_5PxjhF7pWLswQCvvAJ1Un-jU/Library/Caches/com.apple.xbs/Sources/Multitouch_executables/MT2TPHIDService/HSTrackpad/PreAlg/PointerSettings.mm"
- "9430.1"
- "\xf0\xd1"

```
