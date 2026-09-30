## loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

-  __TEXT.__text: 0xc8bbc
+  __TEXT.__text: 0xc9304
   __TEXT.__auth_stubs: 0x2cd0
-  __TEXT.__objc_stubs: 0xfe00
-  __TEXT.__objc_methlist: 0x6abc
-  __TEXT.__const: 0x2f0
-  __TEXT.__gcc_except_tab: 0x1064
-  __TEXT.__objc_methname: 0x1215c
-  __TEXT.__oslogstring: 0x2947c
-  __TEXT.__cstring: 0x12a18
-  __TEXT.__objc_classname: 0x84a
+  __TEXT.__objc_stubs: 0xfe40
+  __TEXT.__objc_methlist: 0x6af4
+  __TEXT.__const: 0x2e8
+  __TEXT.__gcc_except_tab: 0x103c
+  __TEXT.__objc_methname: 0x121ec
+  __TEXT.__oslogstring: 0x2973c
+  __TEXT.__cstring: 0x12a68
+  __TEXT.__objc_classname: 0x87a
   __TEXT.__objc_methtype: 0x21af
   __TEXT.__ustring: 0x1c
-  __TEXT.__swift5_typeref: 0x3c
+  __TEXT.__swift5_typeref: 0x36
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_reflstr: 0x40
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
   __TEXT.__dlopen_cstrs: 0x53
-  __TEXT.__unwind_info: 0x1dc8
-  __DATA_CONST.__const: 0x20c8
+  __TEXT.__unwind_info: 0x1dd0
+  __DATA_CONST.__const: 0x2118
   __DATA_CONST.__cfstring: 0x6e60
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_intobj: 0x240

   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x1678
-  __DATA_CONST.__got: 0x9d8
+  __DATA_CONST.__got: 0xac0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x8ce8
-  __DATA.__objc_selrefs: 0x4ea8
+  __DATA.__objc_const: 0x8d00
+  __DATA.__objc_selrefs: 0x4ec8
   __DATA.__objc_ivar: 0x860
   __DATA.__objc_data: 0x1a70
-  __DATA.__data: 0x938
+  __DATA.__data: 0x990
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x88
   __DATA.__bss: 0x6c8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2594
-  Symbols:   1065
-  CStrings:  9909
+  Functions: 2597
+  Symbols:   1063
+  CStrings:  9927
 
Sections:
~ __TEXT.__objc_methtype : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_types : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
Symbols:
- _$sytN
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "%s |      custom UI provider owns the screen, not taking front or first responder"
+ "%s |      makePasswordFieldFirstResponder called"
+ "%s |      no dock-desktop-ready timer armed, nothing to do"
+ "%s |      screen unlocked while login transition pending; expediting transition now"
+ "%s |      sharedKeyBindingManager"
+ "%s |      transition already complete, ignoring late desktop ready notification"
+ "%s |      transition already complete, nothing to do"
+ "%s |     Attempt to call showScreenLock: ignored, shield window was already gone"
+ "%s |     calling showScreenLock: (psso path)"
+ "%s |     expedite path: skipping 0.1s warmup, completing transition synchronously"
+ "%s |     fading %lu windows"
+ "%s |     hiding password field"
+ "%s |     immediately hiding %lu windows"
+ "%s |     number of snapshot windows to fade out: %lu"
+ "%s |     there are no snapshot windows to fade out."
+ "%s | enter, _transitionComplete:%d, timerArmed:%d"
+ "-[LoginTransition _fadeOutSnapshotWindows:]"
+ "-[LoginTransition _fadeOutSnapshotWindows:]_block_invoke_2"
+ "-[LoginTransition _hideSnapshotWindowsImmediately:]"
+ "-[LoginTransition _hideSnapshotWindowsImmediately:]_block_invoke"
+ "-[LoginTransition expediteIfWaitingForDockDesktopReady]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UYw6Bx/Sources/loginwindow/Source/FirstLoginOptimizer.m"
+ "LFSessionAgentListenerPublicInterface"
+ "_fadeOutSnapshotWindows:"
+ "_hideSnapshotWindowsImmediately:"
+ "dockDesktopReadyAndTALTimer_forTesting"
+ "expediteIfWaitingForDockDesktopReady"
+ "resetTransitionComplete_forTesting"
- "%s | \t makePasswordFieldFirstResponder called"
- "%s | \t sharedKeyBindingManager"
- "%s |     hiding %lu windows"
- "%s | hide password field complete"
- "%s | kLSNotifyApplicationCoalitionMembersChanged: asn: %@"
- "-[LWScreenLock startUnlock:]_block_invoke_2"
- "-[LoginTransition _hideSnapshotWindows:]"
- "-[LoginTransition _hideSnapshotWindows:]_block_invoke_2"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wcOe50/Sources/loginwindow/Source/FirstLoginOptimizer.m"
- "_hideSnapshotWindows:"
- "kLSNotifyApplicationCoalitionMembersChanged"

```
