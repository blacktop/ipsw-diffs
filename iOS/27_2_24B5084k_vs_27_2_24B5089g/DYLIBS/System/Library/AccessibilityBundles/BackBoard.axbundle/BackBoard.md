## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

```diff

-3050.3.0.0.0
-  __TEXT.__text: 0x275c0
-  __TEXT.__objc_methlist: 0x237c
+3050.3.1.0.0
+  __TEXT.__text: 0x278ac
+  __TEXT.__objc_methlist: 0x2394
   __TEXT.__dlopen_cstrs: 0x33b
-  __TEXT.__const: 0x510
-  __TEXT.__cstring: 0x23d1
-  __TEXT.__oslogstring: 0x2233
+  __TEXT.__const: 0x518
+  __TEXT.__cstring: 0x23f1
+  __TEXT.__oslogstring: 0x23ac
   __TEXT.__constg_swiftt: 0x2e0
   __TEXT.__swift5_typeref: 0x17e
   __TEXT.__swift5_reflstr: 0x115

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x18
   __TEXT.__gcc_except_tab: 0x5e8
-  __TEXT.__unwind_info: 0xff8
+  __TEXT.__unwind_info: 0x1008
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c38
+  __DATA_CONST.__objc_selrefs: 0x1c50
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__got: 0x6b0
   __AUTH_CONST.__const: 0x1040
-  __AUTH_CONST.__cfstring: 0x1e20
+  __AUTH_CONST.__cfstring: 0x1e40
   __AUTH_CONST.__objc_const: 0x3158
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1037
-  Symbols:   2869
-  CStrings:  506
+  Functions: 1040
+  Symbols:   2875
+  CStrings:  510
 
Symbols:
+ -[AXBDisplayWakeManager _setupBuddyCompletionMonitoring]
+ -[AXBDisplayWakeManager _suppressAccessibilityHelpBannerIfFeatureEnabledDuringSetup]
+ GCC_except_table635
+ GCC_except_table648
+ GCC_except_table660
+ GCC_except_table693
+ GCC_except_table731
+ GCC_except_table745
+ GCC_except_table819
+ __buddySetupDidComplete
+ _objc_msgSend$_setupBuddyCompletionMonitoring
+ _objc_msgSend$_suppressAccessibilityHelpBannerIfFeatureEnabledDuringSetup
+ _objc_msgSend$distantPast
- GCC_except_table632
- GCC_except_table645
- GCC_except_table657
- GCC_except_table690
- GCC_except_table728
- GCC_except_table742
- GCC_except_table816
CStrings:
+ "Accessibility feature was enabled during device setup, help banner will not be shown: VoiceOver=%{BOOL}d, SwitchControl=%{BOOL}d, TouchAccommodations=%{BOOL}d"
+ "Denying request to set Guided Access enabled=%i: no bundle identifier for sender pid %d (process is gone, or is not bundled)."
+ "Device setup is in progress, not showing accessibility help banner"
+ "Received request to set Guided Access enabled=%i from %{public}@ (pid %d), but GAXBackboard was nil."
+ "com.apple.purplebuddy.setupdone"
- "Received request to set Guided Access enabled=%i, but GAXBackboard was nil."
```
