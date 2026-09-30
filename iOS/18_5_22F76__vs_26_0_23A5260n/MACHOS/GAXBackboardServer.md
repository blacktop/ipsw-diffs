## GAXBackboardServer

> `/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer`

```diff

-1002.2.2.0.0
-  __TEXT.__text: 0x2a454
+1018.0.0.0.0
+  __TEXT.__text: 0x2a768
   __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_stubs: 0x6660
-  __TEXT.__objc_methlist: 0x27ec
-  __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x8c4
-  __TEXT.__objc_methname: 0x885e
-  __TEXT.__cstring: 0x434f
-  __TEXT.__oslogstring: 0x35db
+  __TEXT.__objc_methlist: 0x2814
+  __TEXT.__const: 0x190
+  __TEXT.__gcc_except_tab: 0x8c8
+  __TEXT.__objc_methname: 0x88cb
+  __TEXT.__cstring: 0x4402
+  __TEXT.__oslogstring: 0x36d3
   __TEXT.__objc_classname: 0x363
   __TEXT.__objc_methtype: 0x1836
   __TEXT.__unwind_info: 0xb08
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x15e0
-  __DATA_CONST.__cfstring: 0x35e0
+  __DATA_CONST.__const: 0x15e8
+  __DATA_CONST.__cfstring: 0x3600
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__linkguard: 0x18
   __DATA.__objc_const: 0x2a58
-  __DATA.__objc_selrefs: 0x1e00
+  __DATA.__objc_selrefs: 0x1e18
   __DATA.__objc_ivar: 0x198
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x588

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F5F163AF-81E9-3D22-890F-031B8F7607CC
-  Functions: 1039
-  Symbols:   563
-  CStrings:  2608
+  UUID: 0640CE21-89F7-34E0-8878-A508CB1AEC3B
+  Functions: 1043
+  Symbols:   564
+  CStrings:  2618
 
Symbols:
+ _GAXAccessibilityUIServerIdentifier
CStrings:
+ "-[AXSpringBoardServer(GAXAdditions) acquireSystemApertureInertAssertion]"
+ "-[AXSpringBoardServer(GAXAdditions) invalidateSystemApertureInertAssertion]"
+ "-[GAXEventProcessor _handleGAXActiveSystemEvent:gaxState:]_block_invoke"
+ "Biometrics attempt was successful"
+ "Biometrics failed, prepare to show passcode sheet"
+ "Could not get app name for %{public}@ appID for confirmation prompt"
+ "Could not get app name for ASAM for confirmation banner"
+ "Oops - _shouldDispatchLocally"
+ "Showing passcode view"
+ "Start ignoring all touches via override for verifying integrity - for 5 minutes max"
+ "Stop ignoring all touches via override for verifying integrity - exceeded 5 minutes"
+ "Tried to show passcode view, but it was already visible!"
+ "_showPasscodeViewForVerification:"
+ "acquireSystemApertureInertAssertion"
+ "com.apple.AccessibilityUIServer"
+ "invalidateSystemApertureInertAssertion"
+ "self.locked = NO (Biometrics)"
- "-[GAXEventProcessor _handleGAXActiveSystemEvent:gaxState:]_block_invoke_2"
- "Could not get app name for %{public}@ appID"
- "Failed to show, as it was already visible."
- "Show passcode view."
- "Start ignoring all touches via override for verifying integrity"
- "Touch ID attempt was not successful"
- "Touch ID attempt was successful"
- "self.locked = NO (Touch ID)"

```
