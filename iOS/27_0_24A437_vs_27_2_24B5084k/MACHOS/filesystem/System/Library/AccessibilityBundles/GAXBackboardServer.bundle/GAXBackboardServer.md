## GAXBackboardServer

> `/System/Library/AccessibilityBundles/GAXBackboardServer.bundle/GAXBackboardServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1064.0.0.0.0
-  __TEXT.__text: 0x2ab98
+1067.3.0.0.0
+  __TEXT.__text: 0x2ae48
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x6980
-  __TEXT.__objc_methlist: 0x28ac
+  __TEXT.__objc_stubs: 0x69c0
+  __TEXT.__objc_methlist: 0x28cc
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x84c
-  __TEXT.__objc_methname: 0x8d7a
-  __TEXT.__cstring: 0x4737
-  __TEXT.__oslogstring: 0x41e2
+  __TEXT.__objc_methname: 0x8df7
+  __TEXT.__cstring: 0x47a4
+  __TEXT.__oslogstring: 0x42ca
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methtype: 0x18ca
-  __TEXT.__unwind_info: 0xda8
-  __DATA_CONST.__const: 0x16b8
-  __DATA_CONST.__cfstring: 0x3720
+  __TEXT.__objc_methtype: 0x18cd
+  __TEXT.__unwind_info: 0xdb0
+  __DATA_CONST.__const: 0x16c8
+  __DATA_CONST.__cfstring: 0x3760
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2a30
-  __DATA.__objc_selrefs: 0x1ed8
+  __DATA.__objc_const: 0x2a38
+  __DATA.__objc_selrefs: 0x1ee8
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x588

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 967
-  Symbols:   583
-  CStrings:  2262
+  Functions: 970
+  Symbols:   586
+  CStrings:  2268
 
Symbols:
+ _GAXIPCPayloadKeyHostedApplicationCornerRadii
+ _GAXUIMessageKeyHostedApplicationCornerRadii
+ _deserializeGAXBackboardState
CStrings:
+ "-[AXSpringBoardServer(GAXAdditions) gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:cornerRadiiStringRepresentation:animationDurationNumber:]"
+ "GAXIPCPayloadKeyHostedApplicationCornerRadii"
+ "Reconciling implicit GAX client check-in for still-frontmost session app %@ (pid:%@). Its one-shot check-in ping was lost, not absent"
+ "Session app is still frontmost but its GAX client never checked in; reconciling the lost check-in"
+ "didReconcileCheckInForEffectiveSessionApp"
+ "didReconcileSessionAppCheckInForIntegrityVerifier:"
+ "gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:cornerRadiiStringRepresentation:animationDurationNumber:"
+ "hosted application corner radii"
+ "v56@0:8@16@24@32@40@48"
- "-[AXSpringBoardServer(GAXAdditions) gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:animationDurationNumber:]"
- "gaxUpdateStateOfHostedApplicationWithIdentifier:scaleFactorNumber:centerStringRepresentation:animationDurationNumber:"
- "v48@0:8@16@24@32@40"
```
