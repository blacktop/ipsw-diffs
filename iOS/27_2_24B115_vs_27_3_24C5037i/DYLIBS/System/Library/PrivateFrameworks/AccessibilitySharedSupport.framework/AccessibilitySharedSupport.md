## AccessibilitySharedSupport

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport`

```diff

-591.4.5.0.0
-  __TEXT.__text: 0x16ccdc
-  __TEXT.__objc_methlist: 0x5734
-  __TEXT.__const: 0x206d8
-  __TEXT.__dlopen_cstrs: 0x211
-  __TEXT.__swift5_typeref: 0x69ea
-  __TEXT.__constg_swiftt: 0x600c
-  __TEXT.__swift5_reflstr: 0x2de6
-  __TEXT.__swift5_fieldmd: 0x5898
+591.4.12.0.0
+  __TEXT.__text: 0x176870
+  __TEXT.__objc_methlist: 0x5894
+  __TEXT.__const: 0x20ca8
+  __TEXT.__dlopen_cstrs: 0x25c
+  __TEXT.__swift5_typeref: 0x6ba2
+  __TEXT.__constg_swiftt: 0x6198
+  __TEXT.__swift5_reflstr: 0x2e56
+  __TEXT.__swift5_fieldmd: 0x59ac
   __TEXT.__swift5_builtin: 0x230
   __TEXT.__swift5_assocty: 0x528
-  __TEXT.__swift5_proto: 0x1e54
-  __TEXT.__swift5_types: 0x9c4
-  __TEXT.__cstring: 0x897f
-  __TEXT.__swift5_protos: 0x88
-  __TEXT.__swift_as_entry: 0x20c
-  __TEXT.__swift_as_ret: 0x4f0
-  __TEXT.__swift_as_cont: 0x724
-  __TEXT.__swift5_capture: 0xbac
-  __TEXT.__oslogstring: 0x51c5
+  __TEXT.__swift5_proto: 0x1e7c
+  __TEXT.__swift5_types: 0x9f0
+  __TEXT.__cstring: 0x8b38
+  __TEXT.__swift5_protos: 0x84
+  __TEXT.__swift_as_entry: 0x22c
+  __TEXT.__swift_as_ret: 0x51c
+  __TEXT.__swift_as_cont: 0x75c
+  __TEXT.__swift5_capture: 0xcb0
+  __TEXT.__oslogstring: 0x544d
   __TEXT.__swift5_mpenum: 0xc8
-  __TEXT.__gcc_except_tab: 0x116c
+  __TEXT.__gcc_except_tab: 0x11d4
   __TEXT.__ustring: 0x182
-  __TEXT.__unwind_info: 0x8cb8
-  __TEXT.__eh_frame: 0x903c
+  __TEXT.__unwind_info: 0x8fb8
+  __TEXT.__eh_frame: 0x94a4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x17f8
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__const: 0x18b0
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b08
+  __DATA_CONST.__objc_selrefs: 0x3c70
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x188
-  __DATA_CONST.__objc_arraydata: 0x478
-  __DATA_CONST.__got: 0xd58
-  __AUTH_CONST.__const: 0x18108
-  __AUTH_CONST.__cfstring: 0x4d40
-  __AUTH_CONST.__objc_const: 0x9ce0
-  __AUTH_CONST.__objc_arrayobj: 0x1b0
-  __AUTH_CONST.__objc_intobj: 0xa20
+  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_arraydata: 0x440
+  __DATA_CONST.__got: 0xd78
+  __AUTH_CONST.__const: 0x18748
+  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__objc_const: 0xa078
+  __AUTH_CONST.__objc_arrayobj: 0x198
+  __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x1c0
-  __AUTH_CONST.__auth_got: 0x1b58
-  __AUTH.__objc_data: 0x1b80
-  __AUTH.__data: 0x1820
-  __DATA.__objc_ivar: 0x580
-  __DATA.__data: 0x6580
+  __AUTH_CONST.__auth_got: 0x1b70
+  __AUTH.__objc_data: 0x1bd0
+  __AUTH.__data: 0x1960
+  __DATA.__objc_ivar: 0x5a4
+  __DATA.__data: 0x6680
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xc8
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12134
-  Symbols:   6763
-  CStrings:  1645
+  Functions: 12342
+  Symbols:   6884
+  CStrings:  1676
 
Symbols:
+ +[AXHingePoseMonitor isAvailable]
+ +[AXHingePoseMonitor sharedMonitor]
+ -[AXHingePoseMonitor .cxx_destruct]
+ -[AXHingePoseMonitor _angleDidUpdate:]
+ -[AXHingePoseMonitor _deliverAngle:]
+ -[AXHingePoseMonitor _deliverMagicPose:toObservers:]
+ -[AXHingePoseMonitor _init]
+ -[AXHingePoseMonitor _isMonitoringForTesting]
+ -[AXHingePoseMonitor _isObserving:]
+ -[AXHingePoseMonitor _magicPoseDidUpdate:error:]
+ -[AXHingePoseMonitor _notifyObservers:usingBlock:]
+ -[AXHingePoseMonitor _observersSnapshot]
+ -[AXHingePoseMonitor _recalculateMagicPose]
+ -[AXHingePoseMonitor _resetInitialPose]
+ -[AXHingePoseMonitor _resolveInitialPose:posture:]
+ -[AXHingePoseMonitor _startSourceUpdates]
+ -[AXHingePoseMonitor _startUpdates]
+ -[AXHingePoseMonitor _stopSourceUpdates]
+ -[AXHingePoseMonitor _stopUpdatesIfUnobserved]
+ -[AXHingePoseMonitor _stopUpdates]
+ -[AXHingePoseMonitor _updateWithAngleDegrees:]
+ -[AXHingePoseMonitor _updateWithHingePosture:tabletopPose:tabletopPoseKnown:deviceOrientationPose:]
+ -[AXHingePoseMonitor addObserver:]
+ -[AXHingePoseMonitor angleDegrees]
+ -[AXHingePoseMonitor currentMagicPose]
+ -[AXHingePoseMonitor currentPosture]
+ -[AXHingePoseMonitor isAngleValid]
+ -[AXHingePoseMonitor removeObserver:]
+ GCC_except_table1062
+ GCC_except_table1064
+ GCC_except_table1066
+ GCC_except_table1069
+ GCC_except_table1071
+ GCC_except_table1075
+ GCC_except_table1097
+ GCC_except_table1110
+ GCC_except_table1120
+ GCC_except_table1130
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1211
+ GCC_except_table1488
+ GCC_except_table1530
+ GCC_except_table1534
+ GCC_except_table1618
+ GCC_except_table1648
+ GCC_except_table1749
+ GCC_except_table1750
+ GCC_except_table1752
+ GCC_except_table1885
+ GCC_except_table1894
+ GCC_except_table1898
+ GCC_except_table1905
+ GCC_except_table1918
+ GCC_except_table1926
+ GCC_except_table1948
+ _AXHingeFoldAxisForMagicPose
+ _CoreMotionLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_AXHingePoseMonitor
+ _OBJC_CLASS_$_AXMVisionAnalysisOptions
+ _OBJC_CLASS_$_AXMVoiceOverVisionEngine
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_AXHingePoseMonitor._angleManager
+ _OBJC_IVAR_$_AXHingePoseMonitor._currentMagicPose
+ _OBJC_IVAR_$_AXHingePoseMonitor._fusionInput
+ _OBJC_IVAR_$_AXHingePoseMonitor._hasResolvedPose
+ _OBJC_IVAR_$_AXHingePoseMonitor._isMonitoring
+ _OBJC_IVAR_$_AXHingePoseMonitor._magicPoseManager
+ _OBJC_IVAR_$_AXHingePoseMonitor._observers
+ _OBJC_IVAR_$_AXHingePoseMonitor._observersAwaitingInitialPose
+ _OBJC_IVAR_$_AXHingePoseMonitor._observersLock
+ _OBJC_METACLASS_$_AXHingePoseMonitor
+ __AXHingeFuseMagicPose
+ __DATA__TtC26AccessibilitySharedSupport21AXNamedPeopleDetector
+ __DATA__TtCC26AccessibilitySharedSupport21AXNamedPeopleDetector12PendingNames
+ __IVARS__TtC26AccessibilitySharedSupport21AXNamedPeopleDetector
+ __IVARS__TtCC26AccessibilitySharedSupport21AXNamedPeopleDetector12PendingNames
+ __METACLASS_DATA__TtC26AccessibilitySharedSupport21AXNamedPeopleDetector
+ __METACLASS_DATA__TtCC26AccessibilitySharedSupport21AXNamedPeopleDetector12PendingNames
+ __OBJC_$_CLASS_METHODS_AXHingePoseMonitor
+ __OBJC_$_CLASS_PROP_LIST_AXHingePoseMonitor
+ __OBJC_$_INSTANCE_METHODS_AXHingePoseMonitor
+ __OBJC_$_INSTANCE_VARIABLES_AXHingePoseMonitor
+ __OBJC_$_PROP_LIST_AXHingePoseMonitor
+ __OBJC_CLASS_RO_$_AXHingePoseMonitor
+ __OBJC_METACLASS_RO_$_AXHingePoseMonitor
+ ___34-[AXHingePoseMonitor addObserver:]_block_invoke
+ ___35+[AXHingePoseMonitor sharedMonitor]_block_invoke
+ ___36-[AXHingePoseMonitor _deliverAngle:]_block_invoke
+ ___37-[AXHingePoseMonitor removeObserver:]_block_invoke
+ ___41-[AXHingePoseMonitor _startSourceUpdates]_block_invoke
+ ___41-[AXHingePoseMonitor _startSourceUpdates]_block_invoke_2
+ ___50-[AXHingePoseMonitor _notifyObservers:usingBlock:]_block_invoke
+ ___52-[AXHingePoseMonitor _deliverMagicPose:toObservers:]_block_invoke
+ ___CoreMotionLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32w_e17_v16?0"CMAngle"8lw32l8
+ ___block_descriptor_40_e8_32w_e38_v24?0"CMMagicPoseEvent"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s_e31_v16?0"<AXHingePoseObserver>"8ls32l8
+ ___getCMAngleManagerClass_block_invoke
+ ___getCMMagicPoseManagerClass_block_invoke
+ ___swift_closure_destructor.213Tm
+ ___swift_closure_destructor.375Tm
+ ___swift_closure_destructor.411Tm
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO015AppSwitcherLeftF0VSHAASQ
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO015AppSwitcherLeftF10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO015AppSwitcherLeftF10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO016AppSwitcherRightF0VSHAASQ
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO016AppSwitcherRightF10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO016AppSwitcherRightF10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO14BackCodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO14BackCodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 26AccessibilitySharedSupport0A12SystemActionO4BackVSHAASQ
+ _audit_stringCoreMotion
+ _getCMAngleManagerClass
+ _getCMAngleManagerClass.softClass
+ _getCMMagicPoseManagerClass
+ _getCMMagicPoseManagerClass.softClass
+ _sharedMonitor.monitor
+ _sharedMonitor.onceToken
+ _swift_release_x3
+ _swift_task_isCancelledWithFlags
+ _symbolic SDySS_____G 26AccessibilitySharedSupport0A12ShortcutInfoV
+ _symbolic ScCySo15AXMVisionResultCSg_____G s5NeverO
+ _symbolic ScTySo15AXMVisionResultCSg_____G s5NeverO
+ _symbolic ScTyyt_____G s5NeverO
+ _symbolic ShySSG
+ _symbolic So15AXMVisionResultCSg
+ _symbolic So15AXMVisionResultCSgIeAgHr_
+ _symbolic So24AXMVisionAnalysisOptionsC
+ _symbolic So24AXMVoiceOverVisionEngineC
+ _symbolic So7CIImageC
+ _symbolic _____ 26AccessibilitySharedSupport0A12SystemActionO015AppSwitcherLeftF0V
+ _symbolic _____ 26AccessibilitySharedSupport0A12SystemActionO015AppSwitcherLeftF10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____ 26AccessibilitySharedSupport0A12SystemActionO016AppSwitcherRightF0V
+ _symbolic _____ 26AccessibilitySharedSupport0A12SystemActionO016AppSwitcherRightF10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____ 26AccessibilitySharedSupport0A12SystemActionO14BackCodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____ 26AccessibilitySharedSupport0A12SystemActionO4BackV
+ _symbolic _____ 26AccessibilitySharedSupport0A15ShortcutChangesV
+ _symbolic _____ 26AccessibilitySharedSupport0A15ShortcutTrackerV
+ _symbolic _____ 26AccessibilitySharedSupport21AXNamedPeopleDetectorC
+ _symbolic _____ 26AccessibilitySharedSupport21AXNamedPeopleDetectorC12PendingNamesC
+ _symbolic _____ So11CVBufferRefa
+ _symbolic _____Iegn_ 26AccessibilitySharedSupport0A15ShortcutChangesV
+ _symbolic _____XDXMT 26AccessibilitySharedSupport21AXNamedPeopleDetectorC
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 26AccessibilitySharedSupport0D12ShortcutInfoV
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AccessibilitySharedSupport0D12SystemActionO015AppSwitcherLeftI10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AccessibilitySharedSupport0D12SystemActionO016AppSwitcherRightI10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 26AccessibilitySharedSupport0D12SystemActionO14BackCodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AccessibilitySharedSupport0D12SystemActionO015AppSwitcherLeftI10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AccessibilitySharedSupport0D12SystemActionO016AppSwitcherRightI10CodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 26AccessibilitySharedSupport0D12SystemActionO14BackCodingKeys33_3BD9F8F3A30BDD71BA99D49F4E197118LLO
+ _symbolic _____ytIegnr_ 26AccessibilitySharedSupport0A15ShortcutChangesV
+ _symbolic _____yy_____ScMYccSg_____G s13ManagedBufferCsRi__rlE 26AccessibilitySharedSupport0C15ShortcutChangesV So16os_unfair_lock_sV
+ _type_layout_string 26AccessibilitySharedSupport0A15ShortcutChangesV
+ _type_layout_string 26AccessibilitySharedSupport0A15ShortcutTrackerV
- GCC_except_table1063
- GCC_except_table1065
- GCC_except_table1067
- GCC_except_table1070
- GCC_except_table1072
- GCC_except_table1076
- GCC_except_table1101
- GCC_except_table1112
- GCC_except_table1122
- GCC_except_table1131
- GCC_except_table1135
- GCC_except_table1137
- GCC_except_table1212
- GCC_except_table1489
- GCC_except_table1531
- GCC_except_table1535
- GCC_except_table1619
- GCC_except_table1649
- GCC_except_table1843
- GCC_except_table1852
- GCC_except_table1856
- GCC_except_table1863
- GCC_except_table1876
- GCC_except_table1884
- GCC_except_table1906
- _AXAccessibilityBundlesDirectory
- _AXSSArrangementGestures.arrangementGestures
- _AXSSArrangementGestures.onceToken
- ___AXSSArrangementGestures_block_invoke
- ___swift_closure_destructor.212Tm
- ___swift_closure_destructor.371Tm
- ___swift_closure_destructor.410Tm
- _symbolic $s26AccessibilitySharedSupport03PopA14ResolvedActionP
- _symbolic Say_____GIegg_ 26AccessibilitySharedSupport0A12ShortcutInfoV
- _symbolic Say_____GytIegnr_ 26AccessibilitySharedSupport0A12ShortcutInfoV
- _symbolic _____yySay_____GScMYccSg_____G s13ManagedBufferCsRi__rlE 26AccessibilitySharedSupport0C12ShortcutInfoV So16os_unfair_lock_sV
CStrings:
+ " recognizedTextIdle="
+ "ARRANGEMENT_APP_SWITCHER_LEFT"
+ "ARRANGEMENT_APP_SWITCHER_RIGHT"
+ "AXHingePoseMonitor"
+ "Automatic endpoint did fire. Ending transcription. %{public}s"
+ "CMAngleManager"
+ "CMMagicPoseManager"
+ "Hinge pose changed: %{public}@ -> %{public}@ (angle %.1f, posture %ld)"
+ "Hinge pose monitoring started (angle: %{public}@, MagicPose: %{public}@)"
+ "Hinge pose monitoring stopped"
+ "Hinge pose observer added: %{public}@ (%lu observers)"
+ "Hinge pose observer removed (%lu observers)"
+ "Hinge pose resolved: %{public}@ (angle %.1f, posture %ld)"
+ "MagicPose update failed: %{public}@"
+ "Named-people: detection timed out after %fs; describing without names."
+ "Named-people: detection trigger error: %@"
+ "Named-people: engine has no image node."
+ "Named-people: no photo library URL; skipping."
+ "ambiguous"
+ "appSwitcherLeftApp"
+ "appSwitcherRightApp"
+ "book.upsidedown"
+ "chevron.backward"
+ "laptop"
+ "laptop.upsidedown"
+ "rectangle.lefthalf.inset.filled.arrow.left"
+ "rectangle.righthalf.inset.filled.arrow.right"
+ "softlink:o:path:/System/Library/Frameworks/CoreMotion.framework/CoreMotion"
+ "tent"
+ "v16@?0@\"<AXHingePoseObserver>\"8"
+ "v16@?0@\"CMAngle\"8"
+ "v24@?0@\"CMMagicPoseEvent\"8@\"NSError\"16"
- "/SpringBoardPopFramework.axbundle"
```
