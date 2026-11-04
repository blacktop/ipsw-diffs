## AccessibilityUIUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities`

```diff

-3245.8.9.0.0
-  __TEXT.__text: 0x6502c
-  __TEXT.__objc_methlist: 0x65e4
-  __TEXT.__const: 0x11e0
+3245.8.14.0.0
+  __TEXT.__text: 0x65864
+  __TEXT.__objc_methlist: 0x6664
+  __TEXT.__const: 0x11e8
   __TEXT.__dlopen_cstrs: 0x450
   __TEXT.__constg_swiftt: 0x99c
   __TEXT.__swift5_typeref: 0x133d

   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_capture: 0x1d0
-  __TEXT.__cstring: 0x6219
+  __TEXT.__cstring: 0x623c
   __TEXT.__swift5_assocty: 0x158
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__oslogstring: 0x11dc
+  __TEXT.__oslogstring: 0x1247
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__gcc_except_tab: 0x838
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2110
+  __TEXT.__unwind_info: 0x2120
   __TEXT.__eh_frame: 0x43c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0xe28
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5240
+  __DATA_CONST.__objc_selrefs: 0x52c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x1200
+  __DATA_CONST.__got: 0x1218
   __AUTH_CONST.__const: 0xe58
-  __AUTH_CONST.__cfstring: 0x6aa0
-  __AUTH_CONST.__objc_const: 0xa3e8
+  __AUTH_CONST.__cfstring: 0x6ae0
+  __AUTH_CONST.__objc_const: 0xa480
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1368
+  __AUTH_CONST.__auth_got: 0x1370
   __AUTH.__objc_data: 0x23e0
   __AUTH.__data: 0x680
-  __DATA.__objc_ivar: 0x59c
-  __DATA.__data: 0x1578
+  __DATA.__objc_ivar: 0x5a4
+  __DATA.__data: 0x15d8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x28

   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
+  - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BannerKit.framework/BannerKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2569
-  Symbols:   4757
-  CStrings:  1115
+  Functions: 2578
+  Symbols:   4780
+  CStrings:  1121
 
Symbols:
+ -[AXUIFloatingViewPresenter _updateAvoidanceForMagicPose:]
+ -[AXUIFloatingViewPresenter followsHingePose]
+ -[AXUIFloatingViewPresenter hingePoseMonitor:didUpdateMagicPose:]
+ -[AXUIFloatingViewPresenter setFollowsHingePose:]
+ -[GuidedAccessDevicePINPane _frameForPINView:withinSafeAreaInsets:]
+ -[GuidedAccessDevicePINPane _isTitleCompressedInPINView:]
+ -[GuidedAccessDevicePINPane keypadRaiseSuppressed]
+ -[GuidedAccessDevicePINPane setKeypadRaiseSuppressed:]
+ GCC_except_table1169
+ GCC_except_table1170
+ GCC_except_table1171
+ GCC_except_table1213
+ GCC_except_table1269
+ GCC_except_table1420
+ GCC_except_table1537
+ GCC_except_table1648
+ GCC_except_table1855
+ GCC_except_table1856
+ GCC_except_table1857
+ GCC_except_table1880
+ GCC_except_table1888
+ GCC_except_table1901
+ GCC_except_table1904
+ GCC_except_table1911
+ GCC_except_table1936
+ GCC_except_table633
+ GCC_except_table678
+ GCC_except_table683
+ GCC_except_table694
+ GCC_except_table716
+ GCC_except_table756
+ GCC_except_table757
+ GCC_except_table758
+ GCC_except_table759
+ GCC_except_table771
+ GCC_except_table791
+ GCC_except_table793
+ GCC_except_table798
+ GCC_except_table986
+ _AXHingeFoldAxisForMagicPose
+ _AXUIDisplayConfigurationForDisplayID
+ _AXUIScreenForDisplayIDWithFallback
+ _OBJC_CLASS_$_AXHingePoseMonitor
+ _OBJC_CLASS_$_CADisplay
+ _OBJC_CLASS_$_FBSDisplayConfiguration
+ _OBJC_IVAR_$_AXUIFloatingViewPresenter._followsHingePose
+ _OBJC_IVAR_$_GuidedAccessDevicePINPane._keypadRaiseSuppressed
+ __OBJC_$_INSTANCE_VARIABLES_GuidedAccessDevicePINPane
+ __OBJC_$_PROP_LIST_GuidedAccessDevicePINPane
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXHingePoseObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AXHingePoseObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXHingePoseObserver
+ __OBJC_CLASS_PROTOCOLS_$_AXUIFloatingViewPresenter
+ __OBJC_LABEL_PROTOCOL_$_AXHingePoseObserver
+ __OBJC_PROTOCOL_$_AXHingePoseObserver
+ ___58-[AXUIFloatingViewPresenter _updateAvoidanceForMagicPose:]_block_invoke
- -[AXUIFloatingViewPresenter _avoidanceRegionDidChange:]
- GCC_except_table1160
- GCC_except_table1161
- GCC_except_table1162
- GCC_except_table1204
- GCC_except_table1260
- GCC_except_table1411
- GCC_except_table1528
- GCC_except_table1639
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1848
- GCC_except_table1871
- GCC_except_table1879
- GCC_except_table1892
- GCC_except_table1895
- GCC_except_table1902
- GCC_except_table1927
- GCC_except_table629
- GCC_except_table674
- GCC_except_table679
- GCC_except_table690
- GCC_except_table712
- GCC_except_table752
- GCC_except_table753
- GCC_except_table754
- GCC_except_table755
- GCC_except_table767
- GCC_except_table787
- GCC_except_table789
- GCC_except_table794
- GCC_except_table980
- ___55-[AXUIFloatingViewPresenter _avoidanceRegionDidChange:]_block_invoke
CStrings:
+ "Answering call being screened, status: %lu"
+ "Floating view fold avoidance: %{public}@"
+ "Passcode keypad raise %{public}s; pin view height if raised: %.1f"
+ "_titleLabel"
+ "horizontal"
+ "restored"
+ "suppressed"
+ "vertical"
- "AXFloatingUIAvoidanceRegionDidChangeNotification"
- "isVertical"
```
